#write object data to file
import json
file = open("items.txt","w")
item = [{"name": "shoes", "price": 59.99, "availability": True}, 
        {"name": "jacket", "price": 49.99, "availability": True},
        {"name": "cotton shirt", "price": 29.99, "availability": True},
        {"name": "shirt", "price": 39.99, "availability": True},
        {"name": "trousers", "price": 59.99, "availability": True},
        {"name": "dress", "price": 79.99, "availability": True},
        {"name": "black dress", "price": 79.99, "availability": True}]
json.dump(item, file)

#retrieve file and open with read permission
file = open("items.txt","r")
data = json.load(file)
print(data)
file.close()
