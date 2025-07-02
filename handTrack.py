# # from flask import Flask, render_template, Response, request
# # import cv2 as cv
# # import numpy as np
# # import os
# # from handTrack import handDetector
# # import google.generativeai as genai

# # app = Flask(__name__)

# # brushThickness = 15
# # eraserThickness = 100

# # # Load assets folder safely 
# # folderPath = "assets"
# # if not os.path.exists(folderPath):
# #     os.makedirs(folderPath)

# # mylist = os.listdir(folderPath)
# # overlayList = [cv.imread(f"{folderPath}/{imPath}") for imPath in mylist if cv.imread(f"{folderPath}/{imPath}") is not None]

# # # Ensure assets list is not empty
# # asset = overlayList[0] if overlayList else np.zeros((125, 1280, 3), np.uint8)
# # drawColor = (0, 0, 255)

# # # Initialize webcam
# # cap = cv.VideoCapture(0)
# # cap.set(3, 1280)
# # cap.set(4, 720)

# # detector = handDetector(detectionCon=0.85)
# # xp, yp = 0, 0
# # imgCanvas = np.zeros((720, 1280, 3), np.uint8)

# # # Configure Gemini AI
# # genai.configure(api_key="AIzaSyD6oMED-Xmvq9yx7we07_roPEtaP24JfUA")

# # def gen_frames():
# #     """Generate video frames with hand tracking and drawing."""
# #     global xp, yp, asset, drawColor, imgCanvas

# #     while True:
# #         success, img = cap.read()
# #         if not success or img is None:
# #             break
# #         try:
# #             img = cv.flip(img, 1)
# #             img = detector.findHands(img)
# #             lmList = detector.findPosition(img, draw=False)

# #             if lmList:
# #                 x1, y1 = lmList[8][1:]
# #                 x2, y2 = lmList[12][1:]

# #                 fingers = detector.fingersUp()

# #                 if fingers[:2] == [1, 1] and sum(fingers[2:]) == 0:
# #                     cv.imwrite("saved_canvas.jpg", imgCanvas)

# #                 if fingers[1] and fingers[2]:  # Selection Mode
# #                     xp, yp = 0, 0
# #                     cv.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv.FILLED)

# #                     if y1 < 125:
# #                         if 550 < x1 < 750:
# #                             asset = overlayList[1]
# #                             drawColor = (255, 0, 0)
# #                         elif 800 < x1 < 950:
# #                             asset = overlayList[2]
# #                             drawColor = (0, 0, 255)
# #                         elif 1050 < x1 < 1200:
# #                             asset = overlayList[3]
# #                             drawColor = (0, 0, 0)

# #                 if fingers[1] and not fingers[2]:  # Drawing Mode
# #                     cv.circle(img, (x1, y1), 15, drawColor, cv.FILLED)
# #                     if xp == 0 and yp == 0:
# #                         xp, yp = x1, y1

# #                     thickness = eraserThickness if drawColor == (0, 0, 0) else brushThickness
# #                     cv.line(img, (xp, yp), (x1, y1), drawColor, thickness)
# #                     cv.line(imgCanvas, (xp, yp), (x1, y1), drawColor, thickness)
# #                     xp, yp = x1, y1

# #             # Convert to grayscale and create an inverted binary image
# #             imgGray = cv.cvtColor(imgCanvas, cv.COLOR_BGR2GRAY)
# #             _, imgInv = cv.threshold(imgGray, 50, 255, cv.THRESH_BINARY_INV)
# #             imgInv = cv.cvtColor(imgInv, cv.COLOR_GRAY2BGR)

# #             # Resize if necessary
# #             imgCanvas = cv.resize(imgCanvas, (img.shape[1], img.shape[0])) if img.shape != imgCanvas.shape else imgCanvas
# #             imgInv = cv.resize(imgInv, (img.shape[1], img.shape[0])) if img.shape != imgInv.shape else imgInv

# #             # Perform bitwise operations
# #             img = cv.bitwise_and(img, imgInv)
# #             img = cv.bitwise_or(img, imgCanvas)

# #             img[0:125, 0:1280] = asset
# #             img = cv.addWeighted(img, 0.5, imgCanvas, 0.5, 0)

# #             ret, buffer = cv.imencode('.jpg', img)
# #             if not ret:
# #                 continue

# #             frame = buffer.tobytes()
# #             yield (b'--frame\r\n'
# #                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# #         except ValueError as e:
# #             print(f"Timestamp error ignored: {e}")
# #             continue  # Skip frame to avoid crashing

# # @app.route('/video_feed')
# # def video_feed():
# #     """Return video feed to the client."""
# #     return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# # @app.route('/gemini')
# # def gemini():
# #     """Send saved canvas image to Gemini AI for equation solving."""
# #     try:
# #         if not os.path.exists("saved_canvas.jpg"):
# #             return "No equation detected. Please draw something first."

# #         sample_file = genai.upload_file(path="saved_canvas.jpg", display_name="Maths Question")
# #         model = genai.GenerativeModel(model_name="gemini-1.5-pro")
# #         response = model.generate_content([
# #             sample_file, 
# #             "In the picture, you have a mathematics equation. Solve it by first writing the final solution, then explaining the steps. Provide a plain text response."
# #         ])
# #         return response.text

# #     except Exception as e:
# #         return f"An error occurred: {str(e)}"

# # @app.route('/')
# # def index():
# #     """Render the homepage."""
# #     return render_template('index.html')

# # if __name__ == '__main__':
# #     try:
# #         app.run(debug=True)
# #     finally:
# #         cap.release()  # Ensure the webcam is released when Flask stops





# import cv2 as cv
# import mediapipe as mp

# class handDetector:
#     def __init__(self, detectionCon=0.85, maxHands=2):
#         """
#         Initialize the hand detector.

#         :param detectionCon: Detection confidence threshold (default: 0.85).
#         :param maxHands: Maximum number of hands to detect (default: 2).
#         """
#         self.detectionCon = detectionCon
#         self.maxHands = maxHands

#         # Initialize Mediapipe Hands module
#         self.mpHands = mp.solutions.hands
#         self.hands = self.mpHands.Hands(
#             static_image_mode=False,
#             max_num_hands=self.maxHands,
#             min_detection_confidence=self.detectionCon,
#             min_tracking_confidence=0.5
#         )
#         self.mpDraw = mp.solutions.drawing_utils

#     def findHands(self, img, draw=True):
#         """
#         Detect hands in the given image.

#         :param img: Input image (BGR format).
#         :param draw: Whether to draw hand landmarks (default: True).
#         :return: Processed image with hand landmarks (if draw=True).
#         """
#         imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
#         self.results = self.hands.process(imgRGB)

#         if self.results.multi_hand_landmarks:
#             for handLms in self.results.multi_hand_landmarks:
#                 if draw:
#                     self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
#         return img

#     def findPosition(self, img, handNo=0, draw=True):
#         """
#         Get the position of hand landmarks.

#         :param img: Input image.
#         :param handNo: Index of the hand (default: 0 for the first detected hand).
#         :param draw: Whether to draw circles on landmarks (default: True).
#         :return: List of landmark positions (id, x, y).
#         """
#         lmList = []
#         if self.results.multi_hand_landmarks:
#             myHand = self.results.multi_hand_landmarks[handNo]
#             for id, lm in enumerate(myHand.landmark):
#                 h, w, _ = img.shape
#                 cx, cy = int(lm.x * w), int(lm.y * h)
#                 lmList.append([id, cx, cy])
#                 if draw:
#                     cv.circle(img, (cx, cy), 7, (255, 0, 255), cv.FILLED)
#         return lmList

#     def fingersUp(self):
#         """
#         Determine which fingers are up based on landmark positions.

#         :return: List of 0s and 1s representing finger states (1 = up, 0 = down).
#         """
#         fingers = []
#         tipIds = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky
        
#         if self.results.multi_hand_landmarks:
#             myHand = self.results.multi_hand_landmarks[0]
#             lmList = [lm for lm in myHand.landmark]
            
#             # Thumb: Compare tip with its lower landmark
#             if lmList[tipIds[0]].x < lmList[tipIds[0] - 1].x:  # Left hand
#                 fingers.append(1)
#             else:
#                 fingers.append(0)

#             # Other fingers: Compare tip y-coordinate with lower landmark
#             for id in range(1, 5):
#                 if lmList[tipIds[id]].y < lmList[tipIds[id] - 2].y:
#                     fingers.append(1)
#                 else:
#                     fingers.append(0)

#         return fingers


import cv2 as cv
import mediapipe as mp

class handDetector:
    def __init__(self, mode=False, maxHands=2, detectionCon=0.75, trackCon=0.75):  # Increased confidence
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.detectionCon,
            min_tracking_confidence=self.trackCon,
        )
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]

    def findHands(self, img, draw=True):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(
                        img, handLms, self.mpHands.HAND_CONNECTIONS
                    )
        return img

    def findPosition(self, img, handNo=0, draw=True):
        self.lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv.circle(
                        img, (cx, cy), 5, (255, 0, 255), cv.FILLED
                    )  # Smaller circle for less drawing overhead
        return self.lmList

    def fingersUp(self):
        fingers = []
        # Thumb
        if self.lmList[self.tipIds[0]][1] > self.lmList[self.tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # 4 Fingers
        for id in range(1, 5):
            if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers


def main():
    cap = cv.VideoCapture(0)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)  # Reduce the resolution for faster processing
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
    detector = handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if len(lmList) != 0:
            print(lmList[4])
        cv.imshow("Image", img)
        if cv.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
