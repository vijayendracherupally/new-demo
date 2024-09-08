s="a aabb b bdsccdcsd"
f={}
l=['a','c']
for i in s:
    if (i in f and i not in l):
        f[i]+=1
    else:
        if (i not in l):
            f[i]=1
print(f)