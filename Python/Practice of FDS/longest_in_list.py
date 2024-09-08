s="i am vijayendra cherupally"
w=s.split()
r=0
t=""
for wo in w:
    if(r < len(s)):
        t=wo
        r=len(wo)
print(r,t)