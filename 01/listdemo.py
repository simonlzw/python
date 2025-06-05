testbool = True
testlist = [10, 20, "abcd", "bro", testbool, [3, 2, 1]]
print(testlist[4])
print(type(testlist[4]))

print("extra" in testlist)
testlist.append("extra")
print(testlist)
print("extra" in testlist)