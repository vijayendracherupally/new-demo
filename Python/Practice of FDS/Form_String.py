s="weiufhwfi"
t=s[0:2]
t+=s[len(s)-2:]
print(t)
str="restart"
print(str.replace('e',''))
ch=str[0]
i=1
print(ch,end="")
res=str[1:]
print(res.replace('r','$'))
# while(i<len(str)):
#     if(str[i] == ch):
#         print(str.replace(str[i],'$'))
#     i+=1
l = ["abc", "xyz"]
s = " ".join(l)
i=0
while(s[i] != ' '):
    i+=1
re=s.replace(s[0:2],s[i+1:i+3])
print(re)
print(re.replace(s[i+1:i+3],s[0:2]))
ty="djfh,f,fjjr,cbjuierg,ckuhtt"
tyu=ty.split(',')
tyu.sort()
print(tyu)