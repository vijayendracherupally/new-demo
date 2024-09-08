n=int(input("number:"))
for i in range(n+1):
    for j in range(n+1):
        a = (n//2)+1
        if(i==a or j==a):
            print('*',end="")
        else:
            print(" ",end="")
    print()