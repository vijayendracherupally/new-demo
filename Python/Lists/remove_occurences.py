l = [5, 20, 15, 20, 25, 50, 20,5,15]
s=set()
t=[]
i=0
print(l)
while(i<len(l)-1):
    j=i+1
    while(j<len(l)):
        if (l[i] == l[j]):
            t.append(l[i])
            break
        j+=1
    i+=1
print(t)
