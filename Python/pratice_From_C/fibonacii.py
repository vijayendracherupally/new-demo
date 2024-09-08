n=int(input("enter number:"))
n1=0
n2=1
count=0
while(count<=n):
    n3 = n1 + n2
    print(n3)
    n1=n2
    n2=n3
    count+=1