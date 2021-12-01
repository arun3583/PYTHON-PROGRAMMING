n=int(input("enter 1st numbers"))
p=int(input("enter 2nd numbers"))
if p>n:
    t=p
else:
    t=n
for i in range(1,t+1):
    if(p%i==0)and(n%i==0):
        gcd=i
print(gcd)
