with open("file3.txt","r") as f:
    f.seek(10)
    print(f.tell())
    data=f.read(15)
    print(data)
with open("file3.txt","w") as f:
    f.write("Hello World")
    f.truncate(3)