import requests
import webbrowser
url = 'http://127.0.0.1:8000/uploadImage'
files = {'file': open('data1.jpg', 'rb')}
# requests.post(url, file=files)
r = requests.post(url, files=files)
print(r)
lable='Black jacket'
webbrowser.open(f'http://localhost:3000/?itemName={lable}')
