from googleapiclient.http import MediaFileUpload
from Google import create_service
import sched
import time

s = sched.scheduler(time.time, time.sleep)


def repeat(sc):
    CLIENT_SECRET_FILE = 'client-secret.json'
    API_NAME = 'drive'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/drive']

    service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    file_metadata = {
        'name': 'google.jpg',
        'parents': ['1PqRdx6K1Th3aCboZLH_5uAyI-jZGT9ag']
    }

    media_content = MediaFileUpload('ThePhotoName.jpg', mimetype='image/jpg')

    file = service.files().create(
        body=file_metadata,
        media_body=media_content
    ).execute()
    sc.enter(60, 1, repeat, (sc,))


s.enter(60, 1, repeat, (s,))
s.run()
