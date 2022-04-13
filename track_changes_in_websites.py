import time
import hashlib
from urllib.request import urlopen, Request

url = Request('https://rentry.co/megaman', headers={'User-Agent': 'Mozilla/5.0'})

while True:
    try:
        response = urlopen(url).read()
        current_hash = hashlib.sha224(response).hexdigest()
        time.sleep(5)
        response = urlopen(url).read()
        new_hash = hashlib.sha224(response).hexdigest()

        if new_hash == current_hash:
            continue
        else:
            print('New Announcment')
            continue
    except Exception as e:
        print('Error')

