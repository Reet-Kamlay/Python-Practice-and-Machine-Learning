f=open("file.txt","r")
text=f.read()
print(text)
f.close()
f=open("file.txt","a")
f.write("Welcome")
f.close()