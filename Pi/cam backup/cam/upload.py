from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()

gauth = GoogleAuth()
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

# Create folder.
folder_metadata = {
    'title' : 'photos',
    # The mimetype defines this new file as a folder, so don't change this.
    'mimeType' : 'application/vnd.google-apps.folder'
}
folder = drive.CreateFile(folder_metadata)
folder.Upload()

# Get folder info and print to screen.
folder_title = folder['title']
folder_id = folder['id']
print('title: %s, id: %s' % (folder_title, folder_id))

x=1
folder2 = drive.CreateFile({"title": x ,"mimeType" : "application/vnd.google-apps.folder","parents": [{"kind": "drive#fileLink", "id": folder_id, "isRoot": True }]})
folder2.Upload()
folder2_id = folder2['id']





file5 = drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": folder2_id , "isRoot" : False}]})
file5.SetContentFile('2020-01-15_1828.jpg')
file5.Upload() # Upload the file.
print('title: %s, mimeType: %s' % (file5['title'], file5['mimeType']))
