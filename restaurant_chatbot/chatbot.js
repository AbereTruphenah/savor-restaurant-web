document.addEventListener("DOMContentLoaded", () => {
  const input = document.querySelector("input");
  const sendBtn = document.querySelector("button");
  const chatWindow = document.querySelector("section.bg-gray-400");

  sendBtn.addEventListener("click", async () => {
    const userMessage = input.value.trim();
    if (!userMessage) return;

    // Show user message
    const userBubble = document.createElement("div");
    userBubble.className = "bg-pink-500 text-white rounded-lg p-2 my-2 max-w-sm";
    userBubble.textContent = userMessage;
    chatWindow.appendChild(userBubble);

    input.value = "";

    try {
      const res = await fetch("https://savor-chatbot-backend.onrender.com/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ question: userMessage })
      });

      const data = await res.json();

      const botBubble = document.createElement("div");
      botBubble.className = "bg-white text-black rounded-lg p-2 my-2 max-w-sm self-end";
      botBubble.textContent = data.response || "Sorry, no response received.";
      chatWindow.appendChild(botBubble);
    } catch (err) {
      const errorBubble = document.createElement("div");
      errorBubble.className = "bg-red-500 text-white rounded-lg p-2 my-2 max-w-sm";
      errorBubble.textContent = "Something went wrong!";
      chatWindow.appendChild(errorBubble);
    }

    // Scroll to latest message
    chatWindow.scrollTop = chatWindow.scrollHeight;
  });
});
