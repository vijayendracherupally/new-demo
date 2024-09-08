# n=int(input())
# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print(" ",end="")
#     for k in range((n+1)-i,0,-1):
#         print(" * ",end="")
#     print("\n")
# # end=""
# # for i in range(1,n+1):
# #     for j in range(1,i+1):
# #         print(" * ",end="")
# #     print("\n")
a=5
for i in range(0,a+1):
    for j in range(a,0,-1):
        print(j,end=" ")
    print("\n")
    a-=1