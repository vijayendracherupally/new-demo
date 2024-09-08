n=int(input("Number:"))
for i in range(n):
    for j in range(0,i+1):
        if((i+j)%2==0 or i==j):
            print('1',end="")
        else:
            print('0',end="")
    print('\n')