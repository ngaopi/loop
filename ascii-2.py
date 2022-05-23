n=int(input("enter the number:"))
i=0
while i<n:
    k=ord("A")
    j=0
    while j<=i:
        print(chr(k),end=" ")
        k=k+1
        j=j+1
    i=i+1
    print()


