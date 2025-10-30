document.getElementById("analyzeBtn").addEventListener("click", async () => {
    const userText = document.getElementById("userText").value.trim();
    const resultBox = document.getElementById("resultBox");
    const emotionOutput = document.getElementById("emotionOutput");

    if (!userText) {
        emotionOutput.textContent = "Please type something!";
        resultBox.classList.remove("hidden");
        return;
    }

    try {
        // 🧠 Connect to your Flask API endpoint
        const response = await fetch("https://your-replit-url-or-localhost/analyze_text", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: userText })
        });

        const data = await response.json();

        if (data.mood) {
            emotionOutput.textContent = `${data.mood} 😊 (Confidence: ${Math.round(data.confidence * 100)}%)`;
        } else {
            emotionOutput.textContent = "Could not detect emotion.";
        }

        resultBox.classList.remove("hidden");

    } catch (error) {
        console.error("Error:", error);
        emotionOutput.textContent = "Error connecting to API.";
        resultBox.classList.remove("hidden");
    }
});
