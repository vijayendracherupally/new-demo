q=5
s=0
r=0
i=0
while(q != 1):
    i+=1
    while(q != 0):
        r=q%10
        s+=(r*r)
        q//=10
    q=s
    s=0
    r=0
    if(i == 100):
        print("Not a happy number")
        break
    else:
        print("Happy NUmber")
        break