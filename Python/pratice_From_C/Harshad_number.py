n=int(input("Enter a number:"))
sum=0
y=n
z=0
while(n!=0):
    z=n%10
    sum=sum+z
    n=n//10
if(y%sum==0):
    print("It is a HarshadNumber")
else:
    print("NO")