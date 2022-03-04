f = open("cycle5/file1.txt",'r')
file = open('cycle5/file2.txt','w')
for num,line in enumerate(f):
    if (num+1)%2 != 0:
        file.write(line)
file.close()
f.close()