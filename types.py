dic = {"city": "Москва", "temperature": "20"}
print(dic["city"])
temp = int(dic["temperature"]) - 5
dic["temperature"] = temp
print(dic.get("country", "Russia"))
dic["date"] = "27.05.2019"
print(dic)