# 1
# 2 6
# 3 7 10
# 4 8 11 13
# 5 9 12 14 15

# n=5 
# for i in range(1,n+1):
#     k=i 
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k=k+(n-j)
#     print()

i=1 
while i<=5:
    j=1
    a=0
    k=0
    while j<=i:
        print(i+k,end=" ")
        j=j+1
        a=a+1
        k=k+5-a
    i=i+1
    print()
