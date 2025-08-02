name , age , list01 = "simon" , 25 , [1,2]

str01 = "name: " + name + ",age: " + str(age)
print(str01)

str02 = "name: %s, age: %s, %s" % (name,age,list01)
print(str02)

str03 = f"name: {name}, age: {age}, {list01}"
print(str03)