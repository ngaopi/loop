# 1
# A B
# 1 2 3
# A B C D
# 1 2 3 4 5
i=1 
while i<=5:
    j=1
    while j<=i:
        if i%2==0:
            print(chr(64+j),end=" ")
        else:
            print(j,end=" ")
        j=j+1
    i=i+1
    print()




        
