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


gauth = GoogleAuth()
folder_id = 0
app = Flask(__name__)


@app.route("/")
def index():
    templateData = {
    'title' : 'Arduino '
    }
    return render_template('index.html',**templateData)
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
    if action == 'action4':
        ser0.write(b'bb')
        photo()
        upload(session)
        
    templateData= {
        'title' : 'Arduino '
    }
    
    return render_template('index.html', **templateData)

def firststart():
    gauth.LoadCredentialsFile("mycreds.txt")
    if gauth.credentials is None:
    # Authenticate if they're not there
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
    # Refresh them if expired
        gauth.Refresh()
    else:
        # Initialize the saved creds
        gauth.Authorize()
# Save the current credentials to a file
    gauth.SaveCredentialsFile("mycreds.txt")
# gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    rootname = datetime.datetime.now().strftime("%Y-%m-%d_%H%M")
# Create folder.
    folder_metadata = {
        "title" : rootname,
    # The mimetype defines this new file as a folder, so don't change this.
        "mimeType" : "application/vnd.google-apps.folder"
    }
    #folder = drive.CreateFile(folder_metadata)
    #folder.Upload()
# Get folder info and print to screen.
#folder_title = folder['title']
    #folder_id = folder['id']
    return 0


def upload(session):
    drive = GoogleDrive(gauth)
    gauth.LoadCredentialsFile("mycreds.txt")
    subFolder = drive.CreateFile({"title": session, "mimeType" : "application/vnd.google-apps.folder"})
    subFolder.Upload()
    subFolder_id = subFolder['id']
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
    url.svg("myqr.svg", scale = 8)
    return session



def photo():
    script_dir = os.path.dirname(__file__)
    os.system('/home/pi/cam/capture.sh')
    rel_path = "1.jpg"
    abs_file_path = os.path.join(script_dir, rel_path)
    return 0



if __name__ == "__main__":
    session = 0
    ser0 = serial.Serial('/dev/ttyACM0',9600, timeout = 1)
    ser0.flush()
    app.run(host='0.0.0.0', port = 80, debug = True)
    firststart()
    




