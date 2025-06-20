fr = open("copyfile/target.txt" , mode="r")
fw = open("copyfile/copy.txt" , mode="w")

while True :
    data = fr.read(128)
    if len(data) == 0 :
        break
    fw.write(data)
fw.write("\n")
fw.write("Copy from copyfile/copy.txt")

fr.close()
fw.close()