s=input("enter list1 of  values seperated by a space")
s2=input("enter list2 of  values seperated by a space")
g1=s.split()
g2=s2.split()
k1=list(map(int,g1))
k2=list(map(int,g2))
l1=len(k1)
l2=len(k2)
if l1==l2:
    print("list are same length")
else:
    print("list are different length")
s=0
s2=0
for i in range(0,l1):
    s=k1[i]+s
for i in range(0,l2):
    s2=k2[i]+s2
if s==s2:
    print("sum of list values are same")
else:
    print("sum of list values are not same")

for i in range(0,l1):
    for j in range(0,l2):
        if k1[i]==k2[j]:
            print(k1[i],"occur in both")
