import os
import datetime
import sys
import time
import subprocess
import serial
from flask import Flask, render_template
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pyqrcode
from pyqrcode import QRCode
import simpleaudio as sa
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
def selfie_button(channel):
    photo()
    upload(0)
    time.sleep(2)

GPIO.add_event_detect(18, GPIO.FALLING, callback=selfie_button, bouncetime=300)




gauth = GoogleAuth()
folder_id = 0
app = Flask(__name__)


@app.route("/")
def index():
    templateData = {
    'title' : 'Arduino '
    }
    return render_template('buttons.htm',**templateData)
@app.route("/<action>")
def action(action):
    if action == 'movefstart':
       	base.write(b'f')
    if action == 'movelstart':
       	base.write(b'l')
    if action == 'moverstart':
       	base.write(b'r')
    if action == 'movebstart':
       	base.write(b'b')
    if action == 'movestop':
       	base.write(b's')
    if action == 'movefstop':
       	base.write(b's')
    if action == 'movelstop':
       	base.write(b's')
    if action == 'moverstop':
       	base.write(b's')
    if action == 'movebstop':
       	base.write(b's')
    if action == 'action2':
        hands.write(b'h')
    if action == 'action3':
        hands.write(b's')
        time.sleep(2)
        photo()
        upload(0)
    if action == 'action4':
        hands.write(b'n')
    if action == 'action6':
        head.write(b'q')
    if action == 'action7':
        head.write(b'l')
    if action == 'action8':
        head.write(b'e')
    if action == 'action9':
        head.write(b'r')
    if action == 'action10':
        head.write(b'c')
    if action == 'action11':
        head.write(b's')
    if action == 'action12':
        head.write(b'h')
    
	
	
	
    # if action == 'action1':
        # filename = 'Pillaa.wav'
        # wave_obj = sa.WaveObject.from_wave_file(filename)
        # play_obj = wave_obj.play()
        # play_obj.wait_done()
    templateData= {
        'title' : 'Arduino '
    }
    return render_template('buttons.htm', **templateData)

def firststart():
    gauth.LoadCredentialsFile("mycreds.txt")
    if gauth.credentials is None:
    # Authenticate if they're not there
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
    # Refresh them if expired
        gauth.LocalWebserverAuth()
    else:
        # Initialize the saved creds
        gauth.Authorize()
# Save the current credentials to a file
    gauth.SaveCredentialsFile("mycreds.txt")
# gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
#    rootname = datetime.datetime.now().strftime("%Y-%m-%d_%H%M")
# Create folder.
#    folder_metadata = {
#        "title" : rootname,
    # The mimetype defines this new file as a folder, so don't change this.
#       "mimeType" : "application/vnd.google-apps.folder"
#    }
    #folder = drive.CreateFile(folder_metadata)
    #folder.Upload()
# Get folder info and print to screen.
#folder_title = folder['title']
    #folder_id = folder['id']
    return 0


def upload(session):
    drive = GoogleDrive(gauth)
    gauth.LoadCredentialsFile("mycreds.txt")
    gauth.Authorize()
    gauth.SaveCredentialsFile("mycreds.txt")
#    subFolder = drive.CreateFile({"title": session, "mimeType" : "application/vnd.google-apps.folder"})
#    subFolder.Upload()
    subFolder_id = "1YLfesAdtlCV_rRcc2CxkJOP4HAoPn16V"
# Read file and set it as a content of this instance.
    #file = drive.CreateFile({"title": session })
    #file.SetContentFile('1.jpg')
    #file.Upload() # Upload the file.
    file = drive.CreateFile({"title" : session,"parents": [{"kind": "drive#parentReference", "id": subFolder_id , "isRoot" : True}]})
    file.SetContentFile('1.jpg')
    file.Upload() # Upload the file.
    file_id = file['id']
    session=session+1
    s = "https://drive.google.com/open?id="+file_id
# Generate QR code 
    url = pyqrcode.create(s) 
# Create and save the png file naming "myqr.png" 
    url.png("myqr.png", scale = 8, module_color=[0,42,54,54],  background=[0xc5, 0xa4, 0x4c])
    return session



def photo():
    script_dir = os.path.dirname(__file__)
    os.system('/home/pi/cam/capture.sh')
    rel_path = "1.jpg"
    abs_file_path = os.path.join(script_dir, rel_path)
    return 0



if __name__ == "__main__":
    session = 0
    hands = serial.Serial('/dev/ttyACM0',9600, timeout = 1)
    hands.flush()

    base = serial.Serial('/dev/ttyACM1',9600, timeout = 1)
    base.flush()
    firststart()
    app.run(host='0.0.0.0', port = 80, debug = True)






