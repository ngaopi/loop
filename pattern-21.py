# A
# B C
# D E F
# G H I J
# K L M N O

i=1 
k=ord("A")
while i<=5:
    j=1
    while j<=i:
        print(chr(k),end=" ")
        k=k+1
        j=j+1
    i=i+1
    print()
