document.getElementById("analyzeBtn").addEventListener("click", async () => {
  const text = document.getElementById("userInput").value.trim();
  const resultDiv = document.getElementById("result");

  if (!text) {
    resultDiv.innerText = "Please enter some text!";
    return;
  }

  resultDiv.innerText = "Analyzing...";

  try {
    const response = await fetch("/analyze_text", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });

    const data = await response.json();
    resultDiv.innerText = `Detected Emotion: ${data.emotion}`;
  } catch (error) {
    console.error(error);
    resultDiv.innerText = "Error connecting to server.";
  }
});
