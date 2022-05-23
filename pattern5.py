# A
# B C
# C D E
# D E F G
# E F G H I 
i=1
k=ord("A")
while i<=5:
    j=1 
    while j<=i:
        print(chr(k),end=" ")
        j=j+1
    i=i+1
    print()
    