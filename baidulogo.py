import requests

response = requests.get('https://www.baidu.com/img/bd_logo1.png')
with open('./logo.png', 'wb') as f:
    f.write(response.content)