n=int(input())
r=0
c=n
a=0
sum=0
while(n != 0):
    a=n%10
    r=r*10+a
    sum+=a
    n//=10
if(c % sum == 0):
    print("Harshad",r)
else:
    print("Not Harshad",r)