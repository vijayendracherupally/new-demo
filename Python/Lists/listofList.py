'''
Write a Python program to listify the list of strings individually using Python map.
Example1:
Enter a list of strings separated by commas: hello,India,singing                                                        
[['h', 'e', 'l', 'l', 'o'], ['I', 'n', 'd', 'i', 'a'], ['s', 'i', 'n', 'g', 'i', 'n', 'g']]  
'''
l=[]
s=input("Enter a list of strings separated by commas:")
l1=s.split()
for i in l1:
    l.append(list(i))
print(l)
print(l1)













