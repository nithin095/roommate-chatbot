# # from flask import Flask, request

# # app = Flask(__name__)

# # # Data
# # roommates = ["Nithin","Sampath","Srikanth","Sadulla"]

# # tasks = {
# #     "nithin":"Kitchen cleaning",
# #     "sampath":"Dishes washing",
# #     "srikanth":"Room cleaning",
# #     "sadulla":"Cooking"
# # }

# # rent_status = {
# #     "nithin":"Paid",
# #     "sampath":"Not Paid",
# #     "srikanth":"Paid",
# #     "sadulla":"Not Paid"
# # }

# # # Chatbot Logic
# # def chatbot_response(user):
# #     try:
# #         user = user.lower()

# #         if "roommate" in user:
# #             return "Roommates are " + ", ".join(roommates)

# #         elif "task" in user or "work" in user:
# #             text = ""
# #             for n, w in tasks.items():
# #                 text += n + " does " + w + ". "
# #             return text

# #         elif "clean" in user or "room" in user:
# #             return "To clean the room: sweep the floor, mop, arrange items, clean kitchen and remove garbage."

# #         elif "rent" in user:
# #             text = ""
# #             for n, s in rent_status.items():
# #                 text += n + " rent status is " + s + ". "
# #             return text

# #         elif user in tasks:
# #             return user + " is responsible for " + tasks[user] + " and rent status is " + rent_status[user]

# #         else:
# #             return "Ask about roommates, cleaning, tasks or rent."

# #     except Exception as e:
# #         return "Error occurred: " + str(e)


# # # Home Page
# # @app.route("/")
# # def home():
# #     return """
# # <!DOCTYPE html>
# # <html>
# # <head>
# # <title>Roommate Voice Chatbot</title>

# # <style>

# # body{
# # font-family:Arial;
# # background:#e6ecf0;
# # display:flex;
# # justify-content:center;
# # align-items:center;
# # height:100vh;
# # }

# # .chatbox{
# # width:420px;
# # background:white;
# # border-radius:15px;
# # box-shadow:0 5px 15px rgba(0,0,0,0.2);
# # overflow:hidden;
# # }

# # .header{
# # background:#0088cc;
# # color:white;
# # padding:15px;
# # text-align:center;
# # font-size:18px;
# # }

# # #chat{
# # height:320px;
# # overflow:auto;
# # padding:10px;
# # background-image:url('/static/room.jpg');
# # background-size:cover;
# # background-position:center;
# # }

# # .user{
# # background:#0088cc;
# # color:white;
# # padding:8px;
# # border-radius:15px;
# # margin:5px;
# # max-width:70%;
# # margin-left:auto;
# # }

# # .bot{
# # background:white;
# # color:black;
# # padding:8px;
# # border-radius:15px;
# # margin:5px;
# # max-width:70%;
# # border:1px solid #ddd;
# # }

# # .input-area{
# # display:flex;
# # gap:5px;
# # padding:10px;
# # }

# # input{
# # flex:1;
# # padding:8px;
# # border-radius:10px;
# # border:1px solid #ccc;
# # }

# # button{
# # padding:8px;
# # background:#0088cc;
# # color:white;
# # border:none;
# # border-radius:8px;
# # cursor:pointer;
# # }

# # </style>

# # </head>

# # <body>

# # <div class="chatbox">

# # <div class="header">🏠 Roommate Voice Chatbot</div>

# # <div id="chat"></div>

# # <div class="input-area">
# # <input id="msg" placeholder="Type message">
# # <button onclick="send()">Send</button>
# # <button onclick="voice()">🎤</button>
# # </div>

# # </div>

# # <script>

# # function speak(text){
# # let speech=new SpeechSynthesisUtterance(text);
# # speechSynthesis.speak(speech);
# # }

# # function send(){

# # let msg=document.getElementById("msg").value;
# # if(msg=="") return;

# # let chat=document.getElementById("chat");

# # chat.innerHTML+="<div class='user'>"+msg+"</div>";

# # fetch("/get?msg="+encodeURIComponent(msg))
# # .then(res=>res.text())
# # .then(data=>{
# # chat.innerHTML+="<div class='bot'>"+data+"</div>";
# # speak(data);
# # chat.scrollTop=chat.scrollHeight;
# # });

# # document.getElementById("msg").value="";
# # }

# # function voice(){

# # let recognition=new(window.SpeechRecognition || window.webkitSpeechRecognition)();

# # recognition.onresult=function(event){
# # let text=event.results[0][0].transcript;
# # document.getElementById("msg").value=text;
# # send();
# # }

# # recognition.start();

# # }

# # </script>

# # </body>
# # </html>
# # """

# # # Chat route
# # @app.route("/get")
# # def get_bot():
# #     try:
# #         msg = request.args.get("msg", "")
# #         return chatbot_response(msg)
# #     except Exception as e:
# #         return "Server Error: " + str(e)


# # # Run safely
# # if __name__ == "__main__":
# #     app.run(debug=True)





# from flask import Flask, request

# app = Flask(__name__)

# # ---------------- DATA ---------------- #
# roommates = ["nithin", "sampath", "srikanth", "sadulla"]

# tasks = {
#     "nithin": "Kitchen cleaning",
#     "sampath": "Dishes washing",
#     "srikanth": "Room cleaning",
#     "sadulla": "Cooking"
# }

# rent_status = {
#     "nithin": "Paid",
#     "sampath": "Not Paid",
#     "srikanth": "Paid",
#     "sadulla": "Not Paid"
# }

# # ---------------- CHATBOT LOGIC ---------------- #
# def chatbot_response(user):
#     try:
#         user = user.lower().strip()

#         # Roommates list
#         if "roommate" in user or "members" in user:
#             return "Your roommates are: " + ", ".join([n.capitalize() for n in roommates])

#         # Tasks
#         elif "task" in user or "work" in user:
#             text = "Responsibilities:\n"
#             for n, w in tasks.items():
#                 text += f"{n.capitalize()} → {w}. "
#             return text

#         # Cleaning help
#         elif "clean" in user:
#             return "Cleaning includes sweeping, mopping, arranging items, cleaning kitchen, and removing garbage."

#         # Rent
#         elif "rent" in user:
#             text = "Rent status:\n"
#             for n, s in rent_status.items():
#                 text += f"{n.capitalize()} → {s}. "
#             return text

#         # Specific roommate
#         elif user in tasks:
#             return f"{user.capitalize()} is responsible for {tasks[user]} and rent status is {rent_status[user]}."

#         # Extra smart questions
#         elif "who cooks" in user:
#             return "Sadulla is responsible for cooking."

#         elif "who cleans kitchen" in user:
#             return "Nithin handles kitchen cleaning."

#         elif "who pays rent" in user:
#             paid = [n.capitalize() for n, s in rent_status.items() if s == "Paid"]
#             return "Paid members: " + ", ".join(paid)

#         # Default
#         else:
#             return "You can ask about roommates, tasks, cleaning, or rent."

#     except Exception as e:
#         return "Error: " + str(e)


# # ---------------- FRONTEND ---------------- #
# @app.route("/")
# def home():
#     return """
# <!DOCTYPE html>
# <html>
# <head>
# <title>Roommates Chatbot</title>

# <style>
# body{
# font-family:Arial;
# background:#f0f2f5;
# display:flex;
# justify-content:center;
# align-items:center;
# height:100vh;
# }

# .chatbox{
# width:420px;
# background:white;
# border-radius:15px;
# box-shadow:0 5px 15px rgba(0,0,0,0.2);
# overflow:hidden;
# }

# .header{
# background:#4CAF50;
# color:white;
# padding:15px;
# text-align:center;
# font-size:18px;
# }

# #chat{
# height:320px;
# overflow:auto;
# padding:10px;
# background:#e9f5ec;
# }

# .user{
# background:#4CAF50;
# color:white;
# padding:8px;
# border-radius:15px;
# margin:5px;
# max-width:70%;
# margin-left:auto;
# }

# .bot{
# background:white;
# color:black;
# padding:8px;
# border-radius:15px;
# margin:5px;
# max-width:70%;
# border:1px solid #ddd;
# }

# .input-area{
# display:flex;
# gap:5px;
# padding:10px;
# }

# input{
# flex:1;
# padding:8px;
# border-radius:10px;
# border:1px solid #ccc;
# }

# button{
# padding:8px;
# background:#4CAF50;
# color:white;
# border:none;
# border-radius:8px;
# cursor:pointer;
# }

# button:hover{
# background:#45a049;
# }
# </style>

# </head>

# <body>

# <div class="chatbox">

# <div class="header">👥 Roommates Chatbot</div>

# <div id="chat"></div>

# <div class="input-area">
# <input id="msg" placeholder="Ask about roommates...">
# <button onclick="send()">Send</button>
# <button onclick="voice()">🎤</button>
# </div>

# </div>

# <script>

# function speak(text){
# let speech=new SpeechSynthesisUtterance(text);
# speechSynthesis.speak(speech);
# }

# function send(){

# let msg=document.getElementById("msg").value;
# if(msg=="") return;

# let chat=document.getElementById("chat");

# chat.innerHTML+="<div class='user'>"+msg+"</div>";

# fetch("/get?msg="+encodeURIComponent(msg))
# .then(res=>res.text())
# .then(data=>{
# chat.innerHTML+="<div class='bot'>"+data+"</div>";
# speak(data);
# chat.scrollTop=chat.scrollHeight;
# });

# document.getElementById("msg").value="";
# }

# function voice(){

# let recognition=new(window.SpeechRecognition || window.webkitSpeechRecognition)();

# recognition.onresult=function(event){
# let text=event.results[0][0].transcript;
# document.getElementById("msg").value=text;
# send();
# }

# recognition.start();

# }

# </script>

# </body>
# </html>
# """

# # ---------------- API ---------------- #
# @app.route("/get")
# def get_bot():
#     try:
#         msg = request.args.get("msg", "")
#         return chatbot_response(msg)
#     except Exception as e:
#         return "Server Error: " + str(e)


# # ---------------- RUN ---------------- #
# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, request

# ✅ CREATE APP FIRST (IMPORTANT)
app = Flask(__name__)

# ---------------- DATA ---------------- #
roommates = ["nithin", "sampath", "srikanth", "sadulla"]

tasks = {
    "nithin": "Kitchen cleaning",
    "sampath": "Dishes washing",
    "srikanth": "Room cleaning",
    "sadulla": "Cooking"
}

rent_status = {
    "nithin": "Paid",
    "sampath": "Not Paid",
    "srikanth": "Paid",
    "sadulla": "Not Paid"
}

# ---------------- CHATBOT LOGIC ---------------- #
def chatbot_response(user):
    try:
        user = user.lower().strip()

        if "roommate" in user or "members" in user:
            return "Your roommates are: " + ", ".join([n.capitalize() for n in roommates])

        elif "task" in user or "work" in user:
            text = "Responsibilities: "
            for n, w in tasks.items():
                text += f"{n.capitalize()} handles {w}. "
            return text

        elif "clean" in user:
            return "Cleaning includes sweeping, mopping, arranging items, cleaning the kitchen, and removing garbage."

        elif "rent" in user:
            text = "Rent status: "
            for n, s in rent_status.items():
                text += f"{n.capitalize()} → {s}. "
            return text

        elif user in tasks:
            return f"{user.capitalize()} is responsible for {tasks[user]} and rent status is {rent_status[user]}."

        elif "who cooks" in user:
            return "Sadulla is responsible for cooking."

        elif "who cleans kitchen" in user:
            return "Nithin handles kitchen cleaning."

        elif "who paid rent" in user:
            paid = [n.capitalize() for n, s in rent_status.items() if s == "Paid"]
            return "Paid members: " + ", ".join(paid)

        else:
            return "You can ask about roommates, tasks, cleaning, or rent."

    except Exception as e:
        return "Error: " + str(e)


# ---------------- HOME PAGE ---------------- #
@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Roommates Assistant</title>

<style>
*{
margin:0;
padding:0;
box-sizing:border-box;
font-family:'Segoe UI',sans-serif;
}

body{
background:linear-gradient(135deg,#667eea,#764ba2);
display:flex;
justify-content:center;
align-items:center;
height:100vh;
}

.chatbox{
width:420px;
height:600px;
background:white;
border-radius:20px;
box-shadow:0 10px 30px rgba(0,0,0,0.3);
display:flex;
flex-direction:column;
overflow:hidden;
}

.header{
background:linear-gradient(135deg,#4CAF50,#2e7d32);
color:white;
padding:18px;
text-align:center;
font-size:20px;
font-weight:bold;
}

#chat{
flex:1;
overflow-y:auto;
padding:15px;
background:#f5f7fb;
}

.user, .bot{
padding:10px;
margin:8px 0;
border-radius:15px;
max-width:75%;
font-size:14px;
}

.user{
background:#4CAF50;
color:white;
margin-left:auto;
}

.bot{
background:white;
border:1px solid #ddd;
}

.input-area{
display:flex;
padding:10px;
border-top:1px solid #ddd;
}

input{
flex:1;
padding:10px;
border-radius:20px;
border:1px solid #ccc;
}
# new ai chat bot
button{
margin-left:5px;
padding:10px;
border:none;
border-radius:50%;
background:#4CAF50;
color:white;
cursor:pointer;
}

button:hover{
background:#388e3c;
}
</style>

</head>

<body>

<div class="chatbox">

<div class="header">👥 Roommates Assistant</div>

<div id="chat"></div>

<div class="input-area">
<input id="msg" placeholder="Ask like 'Who cooks?' or 'Rent status'">
<button onclick="send()">➤</button>
<button onclick="voice()">🎤</button>
</div>

</div>

<script>

function speak(text){
let speech=new SpeechSynthesisUtterance(text);
speechSynthesis.speak(speech);
}

function send(){

let msg=document.getElementById("msg").value.trim();
if(msg==="") return;

let chat=document.getElementById("chat");

chat.innerHTML+=`<div class='user'>${msg}</div>`;

fetch("/get?msg="+encodeURIComponent(msg))
.then(res=>res.text())
.then(data=>{
chat.innerHTML+=`<div class='bot'>${data}</div>`;
speak(data);
chat.scrollTop=chat.scrollHeight;
});

document.getElementById("msg").value="";
}

function voice(){

let recognition=new(window.SpeechRecognition || window.webkitSpeechRecognition)();

recognition.lang="en-US";

recognition.onresult=function(event){
let text=event.results[0][0].transcript;
document.getElementById("msg").value=text;
send();
}

recognition.start();

}

// Enter key support
document.getElementById("msg").addEventListener("keypress", function(e){
if(e.key==="Enter"){
send();
}
});

</script>

</body>
</html>
"""


# ---------------- API ---------------- #
@app.route("/get")
def get_bot():
    msg = request.args.get("msg", "")
    return chatbot_response(msg)


# ---------------- RUN ---------------- #
if __name__ == "__main__":
    app.run(debug=True)