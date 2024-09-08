n=int(input("number:"))
a=(n/2)+1
b=1
c=1
for i in range(n):
    if(i==a):
        print('*', end="")
    for j in range(1,n-i):
        print(' ',end="")
    for k in range(1,b+1):
        print('*',end="")
    b+=2
    print("\n")
# for i in range()