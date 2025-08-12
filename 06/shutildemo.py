import shutil

fr = open("file/test.txt" , mode="r")
fw = open("file/target.txt" , mode="w")
shutil.copyfileobj(fr,fw)

fr.close()
fw.close()