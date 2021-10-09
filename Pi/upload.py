from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive



gauth = GoogleAuth()
folder_id = 0


def makingroot():
# Try to load saved client credentials
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

def upload(int x):

    subFolder = drive.CreateFile({"title": x ,"mimeType" : "application/vnd.google-apps.folder","parents": [{"kind": "drive#fileLink", "id": folder_id, "isRoot": True }]})
    subFolder.Upload()
    subFolder_id = subFolder['id']





    file = drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": subFolder_id , "isRoot" : False}]})
    file.SetContentFile('1.jpg')
    file.Upload() # Upload the file.
    return 0