n=int(input())
for i in range(0,n):
    for j in range(1,n+1-i):
        print('*',end="")
    print('\n')