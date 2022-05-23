# 5 4 3 2 1
#   5 4 3 2
#     5 4 3
#       5 4
#         5

n=5 
i=1 
while i<=n:
    j=0
    while j<i:
        print(" ",end=" ")
        j=j+1
    k=5
    while k>=j:
        print(k,end=" ")
        k=k-1
    i=i+1
    print()
        

        
    