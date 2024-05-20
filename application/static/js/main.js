/*
 * CHAT.HTML
 */

const checkbox = document.getElementById("checkbox");
const dyslexicCheckbox = document.getElementById("dyslexic-checkbox");
const twoColRight = document.querySelector(".two-col-right");
const twoColLeft = document.querySelector(".two-col-left");
let isDarkMode = false;
/*
 * Dark-mode Checkbox
 */

checkbox.addEventListener("change", () => {
  const received = document.querySelectorAll(".received");
  const sent = document.querySelectorAll(".sent");
  twoColRight.classList.toggle("dark");
  twoColLeft.classList.toggle("dark");
  isDarkMode = !isDarkMode;

  if (received) {
    received.forEach((rec) => {
      r = rec.classList;
      r.toggle("dark");
    });
  }
  if (sent) {
    sent.forEach((sen) => {
      s = sen.classList;
      s.toggle("dark");
    });
  }
});

/*
 * Open Dyslexic Checkbox
 */

dyslexicCheckbox.addEventListener("change", () => {
  const main = document.querySelector("main");
  main.classList.toggle("dyslexic");
});

/*
 * Expand two-column style
 */

const container = document.querySelector(".chat-two-col");
const sessions = document.querySelector(".sessions-scrollbar");
const collapseButton = document.querySelector(".collapse-history");
const sendBtn = document.querySelector(".btn-send");

cl = container.classList;
sl = sessions.classList;

collapseButton.addEventListener("click", () => {
  cl.toggle("expanded");
  sl.toggle("hidden");
});

const messagesList = document.querySelector(".messages-list");
const messageForm = document.querySelector(".new-message-form");
const messageInput = document.querySelector(".new-message-input");

function submitMessage(event) {
  event.preventDefault();
  sendBtn.disabled = true;

  const message = messageInput.value.trim();
  if (message.length === 0) return;

  const messageItem = document.createElement("div");
  messageItem.classList.add("message-container", "sent-end");
  isDarkMode
    ? (messageItem.innerHTML = `
          <li class="message sent dark">
            <div class='message-text'>
                <p class='message-sender'>
                    <b>You</b>
                </p>
                <p class='message-content'>
                    ${message}
                </p>
            </div>
          </li>
          `)
    : (messageItem.innerHTML = `
          <li class="message sent">
            <div class='message-text'>
                <p class='message-sender'>
                    <b>You</b>
                </p>
                <p class='message-content'>
                    ${message}
                </p>
            </div>
          </li>
          `);
  messagesList.appendChild(messageItem);
  messageInput.value = "";

  const spinner = document.createElement("div");
  spinner.classList.add("stage");
  spinner.innerHTML = `
    <div class="dot-typing"></div>
  `;
  messagesList.appendChild(spinner);
  remove_spinner = messagesList.lastChild;

  fetch("", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      csrfmiddlewaretoken: document.querySelector("[name=csrfmiddlewaretoken]")
        .value,
      message: message,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      const response = data.response;
      //* @see https://www.hiclipart.com/free-transparent-background-png-clipart-dcdxh/
      const avatarUrl = '/static/media/robot.png';
      // const messageId = data.message_id;

      const messageItem = document.createElement("div");
      messageItem.classList.add("message-container");
      isDarkMode
        ? (messageItem.innerHTML = `
                <img src="${avatarUrl}" alt="Robot Avatar" class="avatar-ai" />
                <li class="message received dark">
                  <div class='message-text'>
                    <p class='message-sender'>
                        <b>Ai Chatbot</b>
                    </p>
                    <p class='message-content'>
                        ${response}
                    </p>
                  </div>
                </li>
            `)
        : (messageItem.innerHTML = `
                <img src="${avatarUrl}" alt="Robot Avatar" class="avatar-ai" />
                <li class="message received">
                  <div class='message-text'>
                    <p class='message-sender'>
                        <b>Ai Chatbot</b>
                    </p>
                    <p class='message-content'>
                        ${response}
                    </p>
                  </div>
                </li>
            `);

      messagesList.removeChild(remove_spinner);
      messagesList.appendChild(messageItem);
      sendBtn.disabled = false;
    });
}

/*
 * Event Listeners
 */
messageForm.addEventListener("submit", submitMessage);
