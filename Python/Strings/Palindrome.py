s=input()
for i in s:
    print(i,end="")
print("\n")
for j in s[::-1]:
    print(j,end="")
print("\n")
if(i==j):
    print('palindrome')
else:
    print("NO")