fw = open("writetest.txt" , mode="w")
fw.write("Hello!\n")
fw.write("Hello World \n")
fw.close()

fr = open("writetest.txt" , mode="r")
pf = fr.read()
print(pf)