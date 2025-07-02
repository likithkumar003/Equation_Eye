// function fetchGeminiOutput() {
//   fetch("/gemini")
//     .then((response) => response.text())
//     .then((data) => {
//       document.getElementById("gemini-output").innerText = data;
//     });
// }
// function fetchGeminiOutput() {
//   fetch("/gemini")
//     .then((response) => response.text())
//     .then((data) => {
//       document.getElementById("gemini-output").innerText = data;
//     })
//     .catch((error) => {
//       console.error("Error fetching solution:", error);
//     });
// }

// document.addEventListener("DOMContentLoaded", function () {
//   const themeToggle = document.getElementById("themeToggle");
//   const solveButton = document.getElementById("captureButton");
//   const solutionDisplay = document.getElementById("solutionDisplay");
//   const canvas = document.getElementById("drawingCanvas");
//   const ctx = canvas.getContext("2d");

//   let drawing = false;
//   let erasing = false;

//   // Theme switching
//   themeToggle.addEventListener("click", function () {
//       document.body.classList.toggle("light-mode");
//   });

//   // Pen and eraser functionality
//   document.getElementById("penButton").addEventListener("click", function () {
//       erasing = false;
//   });

//   document.getElementById("eraserButton").addEventListener("click", function () {
//       erasing = true;
//   });

//   document.getElementById("clearButton").addEventListener("click", function () {
//       ctx.clearRect(0, 0, canvas.width, canvas.height);
//   });

//   canvas.addEventListener("mousedown", () => { drawing = true; });
//   canvas.addEventListener("mouseup", () => { drawing = false; ctx.beginPath(); });

//   canvas.addEventListener("mousemove", (event) => {
//       if (!drawing) return;

//       ctx.lineWidth = erasing ? 15 : 3;
//       ctx.strokeStyle = erasing ? "#ffffff" : "#000000";
//       ctx.lineCap = "round";

//       ctx.lineTo(event.offsetX, event.offsetY);
//       ctx.stroke();
//       ctx.beginPath();
//       ctx.moveTo(event.offsetX, event.offsetY);
//   });

//   // Capture button to send image for solving
//   solveButton.addEventListener("click", function () {
//       solutionDisplay.textContent = "Solving...";

//       // Convert canvas drawing to image
//       const imageData = canvas.toDataURL("image/png");

//       fetch("/gemini", {
//           method: "POST",
//           body: JSON.stringify({ image: imageData }),
//           headers: { "Content-Type": "application/json" }
//       })
//       .then(response => response.text())
//       .then(data => { solutionDisplay.textContent = data; })
//       .catch(error => { solutionDisplay.textContent = "Error: Unable to solve."; });
//   });
// });







// befor voice and OCR






// document.addEventListener("DOMContentLoaded", function () {
//   const themeToggle = document.getElementById("theme-toggle");
//   let darkMode = true;

//   themeToggle.addEventListener("click", () => {
//       darkMode = !darkMode;
//       document.body.classList.toggle("dark-mode", darkMode);
//       document.body.classList.toggle("light-mode", !darkMode);
//       themeToggle.textContent = darkMode ? "🌙" : "☀️";
//   });

//   function createEquation() {
//       const equations = ["x^2 + y^2 = r^2", "E = mc^2", "∫ e^x dx", "π ≈ 3.1415"];
//       const equation = document.createElement("div");
//       equation.classList.add("equation");
//       equation.textContent = equations[Math.floor(Math.random() * equations.length)];

//       equation.style.left = Math.random() * 100 + "vw";
//       equation.style.top = Math.random() * 100 + "vh";
//       equation.style.animationDuration = Math.random() * 5 + 5 + "s";

//       document.getElementById("math-background").appendChild(equation);

//       setTimeout(() => equation.remove(), 10000);
//   }

//   setInterval(createEquation, 1000);

//   // ✅ Add function to call /gemini API
//   async function fetchGeminiOutput() {
//       console.log("Magic Solve button clicked!"); // Debugging log

//       try {
//           const response = await fetch("/gemini", { method: "GET" });

//           if (!response.ok) {
//               throw new Error(`HTTP error! Status: ${response.status}`);
//           }

//           const data = await response.text(); // Fetch response as text
//           document.getElementById("gemini-output").innerText = `Solution:\n${data}`;
//           console.log("Response received:", data);
//       } catch (error) {
//           console.error("Error fetching solution:", error);
//           document.getElementById("gemini-output").innerText = "Error fetching solution.";
//       }
//   }

//   // ✅ Attach function to button
//   document.querySelector(".btn-purple").addEventListener("click", fetchGeminiOutput);
// });





// After voice and OCR

// document.addEventListener("DOMContentLoaded", function () {
//     const themeToggle = document.getElementById("theme-toggle");
//     let darkMode = true;
  
//     themeToggle.addEventListener("click", () => {
//       darkMode = !darkMode;
//       document.body.classList.toggle("dark-mode", darkMode);
//       document.body.classList.toggle("light-mode", !darkMode);
//       themeToggle.textContent = darkMode ? "🌙" : "☀️";
//     });
  
//     function createEquation() {
//       const equations = ["x^2 + y^2 = r^2", "E = mc^2", "∫ e^x dx", "π ≈ 3.1415"];
//       const equation = document.createElement("div");
//       equation.classList.add("equation");
//       equation.textContent = equations[Math.floor(Math.random() * equations.length)];
//       equation.style.left = Math.random() * 100 + "vw";
//       equation.style.top = Math.random() * 100 + "vh";
//       equation.style.animationDuration = Math.random() * 5 + 5 + "s";
//       document.getElementById("math-background").appendChild(equation);
//       setTimeout(() => equation.remove(), 10000);
//     }
  
//     setInterval(createEquation, 1000);
  
//     let ocrText = "";
//     let voiceText = "";
  
//     async function getOCR() {
//       try {
//         const res = await fetch("/ocr_text");
//         const data = await res.json();
//         ocrText = data.text.trim();
//         document.getElementById("ocrText").innerText = "✏️ OCR Output: " + ocrText;
//       } catch (err) {
//         console.error("OCR Error:", err);
//         document.getElementById("ocrText").innerText = "❌ Error reading image.";
//         ocrText = "";
//       }
//     }
  
//     async function getVoice() {
//       try {
//         const res = await fetch("/voice_input");
//         const data = await res.json();
//         voiceText = data.voice_text.trim();
//         document.getElementById("voiceText").innerText = "🗣️ Voice Input: " + voiceText;
//       } catch (err) {
//         console.error("Voice Error:", err);
//         document.getElementById("voiceText").innerText = "❌ Error with voice input.";
//         voiceText = "";
//       }
//     }
  
//     async function solve() {
//       const combinedText = `${ocrText}. ${voiceText}`.trim();
//       document.getElementById("finalQuery").innerText = "📦 Combined Input: " + combinedText;
  
//       try {
//         const res = await fetch("/solve_equation", {
//           method: "POST",
//           headers: { "Content-Type": "application/json" },
//           body: JSON.stringify({ full_input: combinedText })
//         });
  
//         const data = await res.json();
//         document.getElementById("geminiResponse").innerText = "🧠 Gemini Response:\n\n" + data.answer;
//       } catch (err) {
//         console.error("Gemini Error:", err);
//         document.getElementById("geminiResponse").innerText = "❌ Error fetching Gemini response.";
//       }
//     }
  
//     document.getElementById("getOCR").addEventListener("click", getOCR);
//     document.getElementById("getVoice").addEventListener("click", getVoice);
//     document.getElementById("magicSolve").addEventListener("click", solve);
//   });

// After UI

document.addEventListener("DOMContentLoaded", () => {
    // 🎬 Hide Splash Screen After Delay
    const splash = document.getElementById("splash-screen");
    setTimeout(() => {
      if (splash) {
        splash.style.opacity = "0";
        splash.style.visibility = "hidden";
      }
    }, 4500);
  
    // 🌙 Theme Toggle
    const themeToggle = document.getElementById("theme-toggle");
    let darkMode = true;
  
    themeToggle.addEventListener("click", () => {
      darkMode = !darkMode;
      document.body.classList.toggle("dark-mode", darkMode);
      document.body.classList.toggle("light-mode", !darkMode);
      themeToggle.textContent = darkMode ? "🌙" : "☀️";
    });
  
    // ✨ Floating Equations Background
    const equations = [
      "x^2 + y^2 = r^2",
      "E = mc^2",
      "∫ e^x dx",
      "π ≈ 3.1415",
      "a² + b² = c²",
      "∇⋅E = ρ/ε₀"
    ];
    setInterval(() => {
      const eq = document.createElement("div");
      eq.classList.add("equation");
      eq.textContent = equations[Math.floor(Math.random() * equations.length)];
      eq.style.left = Math.random() * 100 + "vw";
      eq.style.top = Math.random() * 100 + "vh";
      eq.style.animationDuration = Math.random() * 5 + 5 + "s";
      document.getElementById("math-background").appendChild(eq);
      setTimeout(() => eq.remove(), 10000);
    }, 1000);
  
    // 🎤 AI Interaction Logic
    let ocrText = "";
    let voiceText = "";
  
    async function getOCR() {
      try {
        const res = await fetch("/ocr_text");
        const data = await res.json();
        ocrText = data.text.trim();
        document.getElementById("ocrText").textContent = ocrText;
      } catch (err) {
        console.error("OCR error:", err);
      }
    }
  
    async function getVoice() {
      try {
        const res = await fetch("/voice_input");
        const data = await res.json();
        voiceText = data.voice_text.trim();
        document.getElementById("voiceText").textContent = voiceText;
      } catch (err) {
        console.error("Voice error:", err);
      }
    }
  
    async function solve() {
      await getOCR();
      await getVoice();
  
      const fullInput = `${ocrText}. ${voiceText}`.trim();
      document.getElementById("finalQuery").textContent = fullInput;
  
      try {
        const res = await fetch("/solve_equation", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ full_input: fullInput })
        });
  
        const data = await res.json();
        document.getElementById("geminiResponse").textContent = data.answer;
      } catch (err) {
        console.error("Gemini solve error:", err);
        document.getElementById("geminiResponse").textContent = "Error fetching solution.";
      }
    }
  
    // ✨ Solve Button Trigger
    document.getElementById("solve-btn").addEventListener("click", solve);
  });
  
  
// document.addEventListener("DOMContentLoaded", () => {
//   const themeToggle = document.getElementById("theme-toggle");
//   let darkMode = true;

//   themeToggle.addEventListener("click", () => {
//     darkMode = !darkMode;
//     document.body.classList.toggle("dark-mode", darkMode);
//     document.body.classList.toggle("light-mode", !darkMode);
//     themeToggle.textContent = darkMode ? "🌙" : "☀️";
//   });

//   const equations = ["x^2 + y^2 = r^2", "E = mc^2", "∫ e^x dx", "π ≈ 3.1415", "a² + b² = c²", "∇⋅E = ρ/ε₀"];
//   setInterval(() => {
//     const eq = document.createElement("div");
//     eq.classList.add("equation");
//     eq.textContent = equations[Math.floor(Math.random() * equations.length)];
//     eq.style.left = Math.random() * 100 + "vw";
//     eq.style.top = Math.random() * 100 + "vh";
//     eq.style.animationDuration = Math.random() * 5 + 5 + "s";
//     document.getElementById("math-background").appendChild(eq);
//     setTimeout(() => eq.remove(), 10000);
//   }, 1000);

//   let ocrText = "";
//   let voiceText = "";

//   async function getOCR() {
//     try {
//       const res = await fetch("/ocr_text");
//       const data = await res.json();
//       ocrText = data.text.trim();
//       document.getElementById("ocrText").textContent = ocrText;
//     } catch (err) {
//       console.error("OCR error:", err);
//     }
//   }

//   async function getVoice() {
//     try {
//       const res = await fetch("/voice_input");
//       const data = await res.json();
//       voiceText = data.voice_text.trim();
//       document.getElementById("voiceText").textContent = voiceText;
//     } catch (err) {
//       console.error("Voice error:", err);
//     }
//   }

//   async function solve() {
//     await getOCR();
//     await getVoice();

//     const fullInput = `${ocrText}. ${voiceText}`.trim();
//     document.getElementById("finalQuery").textContent = fullInput;

//     try {
//       const res = await fetch("/solve_equation", {
//         method: "POST",
//         headers: { "Content-Type": "application/json" },
//         body: JSON.stringify({ full_input: fullInput })
//       });

//       const data = await res.json();
//       document.getElementById("geminiResponse").textContent = data.answer;
//     } catch (err) {
//       console.error("Gemini solve error:", err);
//       document.getElementById("geminiResponse").textContent = "Error fetching solution.";
//     }
//   }

//   document.getElementById("solve-btn").addEventListener("click", solve);
// });


// document.addEventListener("DOMContentLoaded", function () {
//   const themeToggle = document.getElementById("theme-toggle");
//   let darkMode = true;
//   let extraVoiceText = "";

//   themeToggle.addEventListener("click", () => {
//     darkMode = !darkMode;
//     document.body.classList.toggle("dark-mode", darkMode);
//     document.body.classList.toggle("light-mode", !darkMode);
//     themeToggle.textContent = darkMode ? "🌙" : "☀️";
//   });

//   function createEquation() {
//     const equations = ["x^2 + y^2 = r^2", "E = mc^2", "∫ e^x dx", "π ≈ 3.1415"];
//     const equation = document.createElement("div");
//     equation.classList.add("equation");
//     equation.textContent = equations[Math.floor(Math.random() * equations.length)];
//     equation.style.left = Math.random() * 100 + "vw";
//     equation.style.top = Math.random() * 100 + "vh";
//     equation.style.animationDuration = Math.random() * 5 + 5 + "s";
//     document.getElementById("math-background").appendChild(equation);
//     setTimeout(() => equation.remove(), 10000);
//   }

//   setInterval(createEquation, 1000);

//   // Inject dynamic voice section
//   const camCard = document.querySelector(".grid-cols-1 .card"); // cam side
//   const voicePromptDiv = document.createElement("div");
//   voicePromptDiv.id = "voice-extension-section";
//   voicePromptDiv.style.display = "none";
//   voicePromptDiv.innerHTML = `
//     <p class="text-lg mt-4">Need to extend the question?</p>
//     <button id="speak-btn" class="btn-purple mt-2">🎤 Speak</button>
//     <p id="voice-result" class="mt-2 text-sm italic text-green-300"></p>
//   `;
//   camCard.appendChild(voicePromptDiv);

//   // =============== Core Interactions ===============
//   // 1. "Send" button logic
//   const sendBtn = document.createElement("button");
//   sendBtn.textContent = "📤 Send";
//   sendBtn.className = "btn-purple mt-4";
//   sendBtn.style.float = "right";
//   sendBtn.addEventListener("click", () => {
//     console.log("Send button clicked");

//     // Show voice section after send
//     document.getElementById("voice-extension-section").style.display = "block";

//     // Optionally give feedback (e.g. alert or toast)
//   });
//   camCard.appendChild(sendBtn);

//   // 2. "Speak" voice recognition
//   const speakBtn = voicePromptDiv.querySelector("#speak-btn");
//   speakBtn.addEventListener("click", () => {
//     console.log("Speak button clicked");

//     if (!("webkitSpeechRecognition" in window)) {
//       alert("Speech Recognition not supported in this browser.");
//       return;
//     }

//     const recognition = new webkitSpeechRecognition();
//     recognition.lang = "en-US";
//     recognition.interimResults = false;
//     recognition.maxAlternatives = 1;

//     recognition.start();

//     recognition.onresult = function (event) {
//       const transcript = event.results[0][0].transcript;
//       extraVoiceText = transcript;
//       document.getElementById("voice-result").textContent = `🗣️ You said: "${transcript}"`;
//       console.log("Voice input:", transcript);
//     };

//     recognition.onerror = function (event) {
//       console.error("Speech recognition error", event.error);
//     };
//   });

//   // 3. "Magic Solve" logic
//   async function fetchGeminiOutput() {
//     console.log("Magic Solve button clicked!");
//     try {
//       const response = await fetch("/gemini", {
//         method: "POST",
//         headers: { "Content-Type": "application/json" },
//         body: JSON.stringify({ extraText: extraVoiceText })
//       });

//       if (!response.ok) {
//         throw new Error(`HTTP error! Status: ${response.status}`);
//       }

//       const data = await response.text();
//       document.getElementById("gemini-output").innerText = `Solution:\n${data}`;
//     } catch (error) {
//       console.error("Error fetching solution:", error);
//       document.getElementById("gemini-output").innerText = "Error fetching solution.";
//     }
//   }

//   // Attach to Magic Solve
//   document.querySelector(".btn-purple").addEventListener("click", fetchGeminiOutput);
// });
