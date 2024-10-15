import requests
city=input("Enter the city name you want to know weather:\n")
response=requests.get(f"http://api.weatherapi.com/v1/current.json?key=b0f924bd95054c02894131441241410&q={city}&aqi=no")
data=response.json()
desc=data.get('current').get('condition').get('text')
temp=data.get('current').get('temp_f')
print(f"The weather in {city} is {desc} and temperature is {temp} degree farhenite")