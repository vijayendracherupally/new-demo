l=[-7,-7,-7,-7,-6]
b=l[0]
r=l[0]
for i in l:
    if(b < i):
        b=i
for i in l:
    if(r < i and i != b):
        r=i
print(r)