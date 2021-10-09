import os
import datetime
import sys
import time
import subprocess
import serial
from flask import Flask, render_template
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


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
        session=1
        photo()
        upload(session)
    templateData= {
        'title' : 'Arduino '
    }
    
    return render_template('index.html', **templateData)

def firststart():
    ser0.flush()
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
    rootname = datetime.datetime.now().strftime("%Y-%m-%d_%H%M")
# Create folder.
    folder_metadata = {
        'title' : rootname,
    # The mimetype defines this new file as a folder, so don't change this.
        'mimeType' : 'application/vnd.google-apps.folder'
    }
    folder = drive.CreateFile(folder_metadata)
    folder.Upload()
# Get folder info and print to screen.
#folder_title = folder['title']
    folder_id = folder['id']
    return 0


def upload(session):
    drive = GoogleDrive(gauth)
    subFolder = drive.CreateFile({"title": session ,"mimeType" : "application/vnd.google-apps.folder","parents": [{"kind": "drive#fileLink", "id": folder_id, "isRoot": True }]})
    subFolder.Upload()
    subFolder_id = subFolder['id']
    file = drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": subFolder_id , "isRoot" : False}]})
    file.SetContentFile('1.jpg')
    file.Upload() # Upload the file.
    session=session+1
    return 0



def photo():
    script_dir = os.path.dirname(__file__)
    os.system('/home/pi/cam/capture.sh')
    rel_path = "1.jpg"
    abs_file_path = os.path.join(script_dir, rel_path)
    return 0



if __name__ == "__main__":
    ser0 = serial.Serial('/dev/ttyACM0',9600, timeout = 1)
    app.run(host='0.0.0.0', port = 80, debug = True)
    firststart()




