<<<<<<< HEAD
# site com os scripts: https://cdnjs.com/ 
# pip install python-socketio flask-socketio simple-websocket

from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# funcionalidade de enviar mensagem
@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)


# criar a minha 1ª página = 1ª rota
@app.route("/") # decorator
def mypage():
    return render_template("mypage.html")

# roda o meu aplicativo
socketio.run(app, host="192.168.0.19")
=======
# site com os scripts: https://cdnjs.com/ 
# pip install python-socketio flask-socketio simple-websocket

from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# funcionalidade de enviar mensagem
@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)


# criar a minha 1ª página = 1ª rota
@app.route("/") # decorator
def mypage():
    return render_template("mypage.html")

# roda o meu aplicativo
socketio.run(app, host="192.168.0.19")
>>>>>>> e53ededc913629bd4830edeac01d18d0bdf0202c
