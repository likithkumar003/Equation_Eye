# ✍️ Equation Eye – AI-Powered Virtual Math Solving from Air-Writing

An intelligent, interactive math assistant that lets users **draw equations in the air**, **speak instructions**, and **solve them using Gemini AI**. Built with OpenCV, Mediapipe, Flask, and Gemini Vision & LLM APIs.

---

## 📂 Features

- ✅ Real-time hand gesture tracking with Mediapipe
- ✅ Drawing captured from webcam using OpenCV
- ✅ Math OCR using Gemini Vision (image input)
- ✅ Voice command transcription via Gemini STT
- ✅ Query combination and intelligent solving using Gemini Pro
- ✅ Interactive UI with TailwindCSS + Dark/Light toggle
- ✅ Fully modular Flask backend with clean separation

---

## 🛠️ Tech Stack

| Component         | Technology                  |
|------------------|-----------------------------|
| UI/Frontend       | HTML, TailwindCSS, JavaScript |
| Backend API       | Python + Flask              |
| Hand Tracking     | Mediapipe + OpenCV          |
| OCR (Image to Text)| Gemini Vision API          |
| Voice to Text     | Gemini Speech-to-Text       |
| LLM Solver        | Gemini Pro (via Google GenAI SDK) |
| App Architecture  | Flask + Modular File System |

---
## 🧠 Architecture Flow
![Architecture (10)](https://github.com/user-attachments/assets/cdf932ee-6844-4fb8-8cc8-db2d0ab1388f)

---
## 🧠 Quick Architecture Flow

```mermaid
flowchart TD
    A[✍️ Air-Writing using Hand Gestures] --> B[OpenCV + Mediapipe Tracks Motion]
    B --> C[Canvas Image Captured]
    C --> D[Gemini Vision OCR → Math Expression]
    E[🎤 Voice Input] --> F[Gemini STT → Instruction Text]
    D --> G[Combine Equation + Instruction]
    F --> G
    G --> H[Gemini Text API → AI Solving]
    H --> I[Formatted Response Shown in UI]
```
---


## 🚀 Demo Features

![image](https://github.com/user-attachments/assets/c7eb56c0-a5ec-4bf4-aa12-eed517ba3173)
![image](https://github.com/user-attachments/assets/50e7d653-99da-4eb5-bc15-e6b28b47b49d)
![image](https://github.com/user-attachments/assets/3d4e455b-ff52-4b29-bb89-54ba12acf34e)
![image](https://github.com/user-attachments/assets/b97b3d70-cafa-4e0e-a2c1-ed2e096f2fe6)
![image](https://github.com/user-attachments/assets/71226d6b-5540-4705-b29b-8a2985e03ea7)
![image](https://github.com/user-attachments/assets/f8cff73a-6821-4828-88fb-7d2284463d91)
![image](https://github.com/user-attachments/assets/a5abeca4-d910-42aa-a048-dfbf6e577864)








📌 Air-write any math expression using hand gestures  
📌 Extract the equation using Gemini Vision (image-to-text)  
📌 Speak instructions (e.g., "solve step-by-step")  
📌 Combines both and sends to Gemini for instant solving  
📌 Toggle between dark/light themes  
📌 Real-time UI built with TailwindCSS  

---


## 📦Installation & Running Locally

    git clone "https://github.com/likithkumar003/Equation_Eye.git"
    cd Equation_eye

## (Optional) Create a virtual environment
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

## Install dependencies
    pip install -r requirements.txt

## 🚀Start the Flask app
    python app.py

