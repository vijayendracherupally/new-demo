l1 = ["M", "na", "i", "Ke"]
l2 = ["y", "me", "s", "lly"]
i=0
s=""
t=[]
while(i<len(l1)):
    s+=l1[i]+l2[i]
    t.append(s)
    s=""
    i+=1
print(t)