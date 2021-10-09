import serial
import time
from flask import Flask, render_template


app = Flask(__name__)



@app.route("/")
def index():
    templateData = {
    'title' : 'Arduino '
    }
    return render_template('keybord.htm',**templateData)
@app.route("/<action>")
def action(action):
    if action == 'action1':
        ser0.write(b'ek')
    if action == 'action2':
        ser0.write(b'pr')
    if action == 'action3':
        ser0.write(b'to')
    if action == 'action7':
        ser0.write(b'ek')
    templateData= {
    'title' : 'Arduino '
    }
    return render_template('keybord.htm', **templateData)
if __name__ == "__main__":
    ser0 = serial.Serial('/dev/ttyACM0',9600, timeout = 1)
    ser0.flush()
    app.run(host='0.0.0.0', port = 80, debug = True)

