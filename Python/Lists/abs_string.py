s = "hello"
x = 0
i = 0
while i < len(s) - 1:
    x += abs(ord(s[i+1]) - ord(s[i]))
    i += 1
print(x)
