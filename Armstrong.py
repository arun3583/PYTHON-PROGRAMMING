n=int(input("enter a number"))
s=0
k=n
while k>0:
    r=k%10
    s=s+r*r*r
    k=k//10
if n==s:
    print("armstrong")
else:
    print("not armstrong")
