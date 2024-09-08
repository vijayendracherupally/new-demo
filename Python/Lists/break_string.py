# s = "What is the solution to this problem"
# k=4
# word=s.split()
# t=""
# i=0
# while(i<k):
#     t.append(word[i])
#     i+=1
# print(t)



s = "Hello how are you Contestant"
k = 4

words = s.split()  # Split the string into words
truncated_words = words[:k]  # Take the first k words
truncated_sentence = ' '.join(truncated_words)  # Join the words back into a string

print(truncated_sentence)  # Output: "Hello how are you"
