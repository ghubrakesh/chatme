from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
@app.route('/')
def message():
    return render_template("message.html")


@socketio.on("message")
def sendMessage(message):
    send(message, broadcast=True)




if __name__ == "__main__":
    app.run(debug=True)