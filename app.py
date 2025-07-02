from flask import Flask, render_template, Response, request, jsonify
import cv2 as cv
import numpy as np
import os
import handTrack as ht
from gtts import gTTS
import speech_recognition as sr
import requests
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Drawing variables
brushThickness = 10
eraserThickness = 100
drawColor = (0, 0, 255)
xp, yp = 0, 0
imgCanvas = np.zeros((720, 1280, 3), np.uint8)

# Load header buttons
folderPath = "assets"
overlayList = [cv.imread(f"{folderPath}/{im}") for im in os.listdir(folderPath)]
asset = overlayList[0]

# Initialize webcam
cap = cv.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Hand detection
detector = ht.handDetector(detectionCon=0.85)

# Gemini API
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


# OCR.space API Key
OCR_API_KEY = "K87398137988957"



def gen_frames():
    global xp, yp, asset, drawColor, imgCanvas
    while True:
        success, img = cap.read()
        if not success:
            break
        img = cv.flip(img, 1)
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)

        if lmList:
            x1, y1 = lmList[8][1:]
            x2, y2 = lmList[12][1:]
            fingers = detector.fingersUp()

            if fingers[0] and fingers[1] and not fingers[2] and not fingers[3] and not fingers[4]:
                cv.imwrite("saved_canvas.jpg", imgCanvas)

            if fingers[1] and fingers[2]:
                xp, yp = 0, 0
                cv.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv.FILLED)
                if y1 < 125:
                    if 550 < x1 < 750:
                        asset = overlayList[1]
                        drawColor = (255, 0, 0)
                    elif 800 < x1 < 950:
                        asset = overlayList[2]
                        drawColor = (0, 0, 255)
                    elif 1050 < x1 < 1200:
                        asset = overlayList[3]
                        drawColor = (0, 0, 0)

            if fingers[1] and not fingers[2]:
                cv.circle(img, (x1, y1), 15, drawColor, cv.FILLED)
                if xp == 0 and yp == 0:
                    xp, yp = x1, y1
                if drawColor == (0, 0, 0):
                    cv.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
                    cv.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)
                else:
                    cv.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
                    cv.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)
                xp, yp = x1, y1

        imgGray = cv.cvtColor(imgCanvas, cv.COLOR_BGR2GRAY)
        _, imgInv = cv.threshold(imgGray, 50, 255, cv.THRESH_BINARY_INV)
        imgInv = cv.cvtColor(imgInv, cv.COLOR_GRAY2BGR)
        img = cv.bitwise_and(img, imgInv)
        img = cv.bitwise_or(img, imgCanvas)

        img[0:125, 0:1280] = asset
        img = cv.addWeighted(img, 0.5, imgCanvas, 0.5, 0)

        ret, buffer = cv.imencode('.jpg', img)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/video_feed")
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')




import requests

@app.route("/extract_from_image", methods=["GET"])
def extract_from_image():
    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash", 
    generation_config={"temperature": 0.3}
)

    image_path = "saved_canvas.jpg"

    try:
        with open(image_path, "rb") as img_file:
            img_bytes = img_file.read()

        response = model.generate_content(
            [genai.upload_file(image_path), "if the image is blank return nothing, Else Extract the math expression or question from this image."]
        )
        extracted_text = response.text.strip()
        return jsonify({"text": extracted_text})
    except Exception as e:
        print("Error using Gemini to extract text:", e)
        return jsonify({"text": ""})




@app.route("/voice_input")
def voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for voice...")
        audio = recognizer.listen(source, timeout=5)
    try:
        query = recognizer.recognize_google(audio)
        return jsonify({"voice_text": query})
    except sr.UnknownValueError:
        return jsonify({"voice_text": ""})


@app.route("/solve_equation", methods=["POST"])
def solve_equation():
    data = request.get_json()
    full_text = data.get("full_input", "")
    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash", 
    generation_config={"temperature": 0.3}
)

    response = model.generate_content(
        f"You are given a math question: {full_text}\nSolve it. Give direct answer followed by explanation."
    )
    return jsonify({"answer": response.text})


if __name__ == "__main__":
    app.run(debug=True)
