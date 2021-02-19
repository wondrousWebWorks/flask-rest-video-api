import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"name": "Testing 1", "views": 15, "likes": 4},
    {"name": "Testing 2", "views": 567, "likes": 103},
    {"name": "Testing 3", "views": 2387, "likes": 1024}
]

for i in range(len(data)):
    response = requests.put(
        BASE + "video/" + str(i), data[i])
    print(response.json())

# input()
# response = requests.delete(BASE + "video/0")
# print(response)
input()
response = requests.get(BASE + "video/5")
print(response.json())
