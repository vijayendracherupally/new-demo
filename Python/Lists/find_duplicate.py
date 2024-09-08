l=[1,2,3,4,5,6,5,4,3,2,1,10,11]
n=len(l)
fl=True
i=0
while(i<n):
    j = i + 1
    while(j<n-1):
        if(l[i] == l[j]):
            fl=False
            break
        j += 1
    if(fl == False):
        print(l[i])
        fl=True
    i+=1