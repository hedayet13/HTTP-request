import requests

url='http://127.0.0.1:5000/upload'
# files = {
#     'media':open('img/res0.jpg','rb')
# }
count=0
while True:
    files =[
    ('image[]',('res0.jpg',open('img/res0.jpg','rb'),'image/jpeg'))
    ]
    r=requests.post(url,files=files)
    count+=1
    print(r.json,  count)
