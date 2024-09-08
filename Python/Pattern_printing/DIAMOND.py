n=int(input("Number:"))
a=1
for i in range(n):
    for j in range(1,n+1-i):
        print(" ",end="")
    for k in range(1, a+1):
        print('*', end="")
    a+=2
    print('\n')
