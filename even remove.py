n=(input("enter numbers followed by space"))
l=n.split(" ")
l=list(map(int,l))
le=len(l)
s=list()
for i in range(0,le):
    if l[i] % 2 != 0:
        s.append(l[i])
print(s)
