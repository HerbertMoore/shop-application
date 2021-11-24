#write object data to file
import json
file = open("items.txt","w")
item = {"name": "shoes", "price": 59.99, "availability": True}
json.dump(item, file)

#retrieve file and open with read permission
file = open("items.txt","r")
data = json.load(file)
print(data)
file.close()
