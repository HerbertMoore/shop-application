#write object data to file
import json
file = open("items.txt","w")
item = {"name": "shoes", "price": 59.99, "availability": True}
json.dump(item, file)
file.close()

#retrieve file and open with read permission
import json
file = open("items.txt","r")
data = json.load(file)
print(data)
file.close()

#creates database and stores dictionary entries in it
import shelve
s = shelve.open("items")
s['name'] = "socks"
s['price'] = 9.99
s['availability'] = True
print(list(s.items()))
print(list(s.values()))
d = {"availability": False}
s.update(d)
print(list(s.items()))
print(list(s.values()))
s.close()
