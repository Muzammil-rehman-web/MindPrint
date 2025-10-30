async function analyzeText() {
  const userText = document.getElementById("userInput").value;
  const resultDiv = document.getElementById("result");

  if (!userText.trim()) {
    resultDiv.innerHTML = "<p>Please enter some text!</p>";
    return;
  }

  resultDiv.innerHTML = "<p>Analyzing...</p>";

  try {
    const response = await fetch("https://your-backend-url/analyze_text", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: userText }),
    });

    const data = await response.json();
    resultDiv.innerHTML = `
      <h3>Emotion: ${data.mood || data.emotion}</h3>
      <p>Confidence: ${(data.confidence * 100).toFixed(1)}%</p>
    `;
  } catch (error) {
    resultDiv.innerHTML = "<p>⚠️ Error connecting to backend.</p>";
  }
}
