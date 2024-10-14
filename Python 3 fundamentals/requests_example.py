import requests
respose=requests.get("http://api.open-notify.org/astros.json")
json_object=respose.json()
print("List of people in space:")
for people in json_object["people"]:
    print(people["name"])