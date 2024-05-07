import os.path
import shutil
f = open('dict.txt')
contents = open('zzxxyyxx.html')
for word in f:
	str = word.strip()+ ".html"
	print(str)
	if not os.path.isfile("./"+str):
		newFile = open(str, "x");
		shutil.copyfileobj(contents, newFile)
		newFile.close()
contents.close()
f.close()
