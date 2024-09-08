s="vijayendra cherupally"
f={}
for i in s:
    if(i in f):
        f[i]+=1
    else:
        f[i]=1
print(f)
