f = open('file.txt', 'w')
f.write("Hi it's Ruslan")
f.close()
f = open('file.txt')
print(f.read())
f.close()
#print(f.read())
#print(f.read(1))
#for line in f:
#    print(line)
#