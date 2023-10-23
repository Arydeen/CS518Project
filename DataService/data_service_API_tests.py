import requests

url = 'http://localhost:7071/api/CreateRecord'
document = {'title': 'test'}

x = requests.post(url, json=document)
print("response text", x.text)
print("response code", x.status_code)

document = {'title': 'test2', 'message': "hello world"}
x = requests.post(url, json=document)
print("response text", x.text)
print("response code", x.status_code)

document = {}
x = requests.post(url, json=document)
print("response text", x.text)
print("response code", x.status_code)

url = 'http://localhost:7071/api/ReadRecords'
x = requests.get(url, params={"query":'{"title":"test"}'})
print("response text", x.text)
print("response code", x.status_code)

x = requests.get(url, params={"query":'{"title":"test2"}'})
print("response text", x.text)
print("response code", x.status_code)

x = requests.get(url, params={"query":'{"title":"test3"}'})
print("response text", x.text)
print("response code", x.status_code)


