# ✍️ Equation Eye – AI-Powered Math Solving from Air-Writing

An intelligent, interactive math assistant that lets users **draw equations in the air**, **speak instructions**, and **solve them using Gemini AI**. Built with OpenCV, Mediapipe, Flask, and Gemini Vision & LLM APIs.

---

## 🚀 Demo Features

📌 Air-write any math expression using hand gestures  
📌 Extract the equation using Gemini Vision (image-to-text)  
📌 Speak instructions (e.g., "solve step-by-step")  
📌 Combines both and sends to Gemini for instant solving  
📌 Toggle between dark/light themes  
📌 Real-time UI built with TailwindCSS  

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
