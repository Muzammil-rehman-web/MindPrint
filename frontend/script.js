// 🔹 MindPrint Frontend Script
// Handles user input, sends it to backend, and displays emotion result

const form = document.querySelector("#emotionForm");
const input = document.querySelector("#userText");
const result = document.querySelector("#result");

// ✅ Your live API endpoint from Replit
const API_URL = "https://2195dbb5-e56e-45c7-9af4-b0c924055f21-00-1j6xsuhfgxmb4.sisko.replit.dev/analyze_text";

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const text = input.value.trim();
  if (!text) {
    result.textContent = "⚠️ Please enter some text!";
    return;
  }

  result.textContent = "⏳ Analyzing your emotion...";

  try {
    // 📨 Send request to backend API
    const response = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text })
    });

    // 📦 Convert response to JSON
    const data = await response.json();

    // 🎯 Display the predicted emotion
    result.textContent = `💡 Detected Emotion: ${data.emotion}`;
  } catch (error) {
    console.error("Error:", error);
    result.textContent = "❌ Something went wrong. Please try again.";
  }
});
