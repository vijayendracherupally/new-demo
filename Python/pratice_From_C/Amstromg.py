n=int(input("Enter a number:"))
sum=0
y=n
z=0
while(n!=0):
    z=n%10
    sum=sum+(z*z*z)
    n//=10
if(sum==y):
    print("It is a Amstrong number")
else:
    print("NO")