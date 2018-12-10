f=open ('text.txt','r')
print(f.read(10))
print(f.read())
f.close()

f=open('text.txt','r')
for x in f:
    print(x)

f.close()

f=open("text.txt","a")
f.write("Now the file has one more line")
f.close()

f=open("text.txt")
print(f.read())
f.close()
