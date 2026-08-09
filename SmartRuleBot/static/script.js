async function sendMessage() {

    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    const message = input.value.trim();

    if (!message) {
        return;
    }

    // Display user message
    const userMessage = document.createElement("div");

    userMessage.className = "message user";

    userMessage.textContent = message;

    chatBox.appendChild(userMessage);

    input.value = "";

    // Send message to Flask
    const response = await fetch("/chat", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            message: message
        })
    });

    const data = await response.json();

    // Display bot response
    const botMessage = document.createElement("div");

    botMessage.className = "message bot";

    botMessage.textContent = data.response;

    chatBox.appendChild(botMessage);

    chatBox.scrollTop = chatBox.scrollHeight;
}


document
    .getElementById("user-input")
    .addEventListener("keypress", function(event) {

        if (event.key === "Enter") {
            sendMessage();
        }

    });