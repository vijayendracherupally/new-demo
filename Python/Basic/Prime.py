n=int(input("Enter number:"))
a=0
for i in range(2,n):
    if(n%i==0):
        a=1
        break
    if (a == 0):
        print(i)
    else:
        print("no")