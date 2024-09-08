l=[1,2,3,4,5,6,7,8,9,10]
n=len(l)
temp=l[0]
l[0]=l[n-1]
l[n-1]=temp
print(l)
print(max(l),min(l),l.index(min(l)))
print(sum(l))