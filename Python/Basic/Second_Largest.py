n=int(input("Enter number:"))
l1=[]
for i in range(n):
    s=int(input())
    l1.append(s)
xyz = float('-inf')
for i in range(n):
    if(l1[i]>l1[0]):
        xyz=l1[i]
zyz = float('-inf')
for i in range(n):
    if(l1[i]>l1[0] and l1[i]!=xyz):
        zyz=l1[i]
print(zyz)