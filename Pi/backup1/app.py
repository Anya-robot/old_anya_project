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
       	ser0.write(b'f')
    if action == 'movelstart':
       	ser0.write(b'lw')
    if action == 'moverstart':
       	ser0.write(b'rw')
    if action == 'movebstart':
       	ser0.write(b'bw')
    if action == 'movefstop':
       	ser0.write(b's')
    if action == 'movelstop':
       	ser0.write(b's')
    if action == 'moverstop':
       	ser0.write(b's')
    if action == 'movebstop':
       	ser0.write(b's')
    if action == 'action4':
        photo()
        upload(session)
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
    #ser0 = serial.Serial('/dev/ttyACM0',9600, timeout = 1)
    #ser0.flush()
    firststart()
    app.run(host='0.0.0.0', port = 80, debug = True)





