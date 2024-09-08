s = "helloworld"
print(s[-5:])
print(s[5:10])
print(s[-1:-6:-1])
print(s[1:4])
f="college"
print(f[-1:-8:-1])
e="I am Vijayendra"
n=len(e)
print(e[-1::-1])
#print(e[-1:-n-1:-1])
t="12323"
c=0
for i in t:
    if(i.isdigit()):
        c+=1
print(c == len(t))
ph="+91-4322433426"
co=0
print(ph[2])
if(ph.startswith("+91-") == False):
    print("Not Indian")
else:
    i=4
    while(i < len(ph)) :
        if(ph[i].isdigit()):
            co+=1
            i+=1
if(co == 10):
    print("Correct number")
st="abc def ghij"
print(st.find('d'))
words=st.split()
l=[]
words.sort()
for i in words:
    l.append(i[-1::-1])
l.reverse()
print(l)