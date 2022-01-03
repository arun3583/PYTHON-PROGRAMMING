def fib(a):
    var=0
    var1=1
    temp=0
    print(var)
    for i in range(0,n-1):
        temp=var+var1
        print(temp,"\t")
        var1=var
        var=temp
n=int(input("enter the limit"))
fib(n)
