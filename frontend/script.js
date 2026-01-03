async function submitGuess() {
  const input = document.getElementById("guessInput");
  const result = document.getElementById("result");

  // Reset animations
  result.className = "";

  const response = await fetch("http://127.0.0.1:5000/guess", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ guess: input.value }),
  });

  const data = await response.json();
  result.textContent = data.message;

  if (data.message.includes("Correct")) {
    result.classList.add("correct");
  } else {
    result.classList.add("wrong");
  }

  input.value = "";
  input.focus();
}
