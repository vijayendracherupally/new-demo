n=int(input("Enter number:"))
for i in range(2,n):
    for j in range(2,i+1):
        if(i%j!=0):
            print(i)
            break
