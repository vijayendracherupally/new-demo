word_list = input("Enter a list of words (comma-separated): ").split(',')
word_list = [word.strip() for word in word_list]
xyz=''
for i in word_list:
    if(len(i)>len(xyz)):
        xyz=i
print(xyz)