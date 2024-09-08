a=int(input())
c=a
b=0
sum=0
while(a != 0):
    b=a%10
    sum=sum+(b*b*b)
    a=a//10
if(sum == c):
    print("Amstrong")
else:
    print("Not Amstrong")