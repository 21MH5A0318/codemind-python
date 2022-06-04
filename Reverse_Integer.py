n=int(input())
f=n
r=0
a=-1
b=1
if n<0:
    n=n*a
else:
    n=n*b
while n>0:
    d=n%10
    r=r*10+d
    n=int(n/10)
if f<0:
    print(r*a)
else:
    print(r)