f=input("enter list of  values seperated by a space")
k=f.split()
j=list(map(int,k))
l=len(k)
print(l)
for i in range(0,l):
    if j[i]>100:
        j[i]="over"
print(j)
