dict1 = {"name" : "Alice" , "age" : 12}

# print(dict1["age"])
# print("name" in dict1)

# data = dict1.get("name" , "No name")
# print(data)
# data = dict1.get("score" , "No score")
# print(data)

# key = dict1.keys()
# print(key)
# value = dict1.values()
# print(value)
# item = dict1.items()
# print(item)
#
# for item in dict1.items():
#     print(item)

print(dict1)
dict1.update({"age" : 25 , "status" : "Alive"})
print(dict1)
dict1["hobby"] = "Nope"
print(dict1)
# dict1.pop("hobby")
# print(dict1)
del dict1["hobby"]
print(dict1)
dict1.clear()
print(dict1)