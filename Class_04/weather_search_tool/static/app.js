const API_BASE = location.origin.startsWith("file:")
  ? "http://localhost:8000"
  : "";

async function queryAgent(prompt) {
  const res = await fetch(`${API_BASE}/api/query`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ prompt }),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    throw new Error(err.detail || "Request failed");
  }
  const data = await res.json();
  return data.output;
}

const form = document.getElementById("query-form");
const promptEl = document.getElementById("prompt");
const outputEl = document.getElementById("output");
const resultCard = document.getElementById("result");
const sendBtn = document.getElementById("send");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const prompt = promptEl.value.trim();
  if (!prompt) return;

  sendBtn.disabled = true;
  outputEl.textContent = "Thinking...";
  resultCard.classList.remove("hidden");

  try {
    const output = await queryAgent(prompt);
    outputEl.textContent = output;
  } catch (err) {
    outputEl.textContent = `Error: ${err.message}`;
  } finally {
    sendBtn.disabled = false;
  }
});
