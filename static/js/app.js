const sendBtn =
document.getElementById("sendBtn");

const userInput =
document.getElementById("userInput");

const chatBox =
document.getElementById("chatBox");

sendBtn.addEventListener(
"click",
sendMessage
);

async function sendMessage(){

let message =
userInput.value.trim();

if(message==="") return;

chatBox.innerHTML +=

`
<div class="user-message">
${message}
</div>
`;

userInput.value="";

let typing = document.createElement(
"div"
);

typing.className =
"bot-message";

typing.innerHTML =
"Typing...";

chatBox.appendChild(
typing
);

let response = await fetch(
"/ask",
{
method:"POST",
headers:{
"Content-Type":
"application/json"
},
body:JSON.stringify({
message
})
}
);

let data =
await response.json();

typing.remove();

chatBox.innerHTML +=

`
<div class="bot-message">
${data.response}
</div>
`;

chatBox.scrollTop =
chatBox.scrollHeight;
}
