num=int(input("enter the number of rows:"))
for row in range(num):
    for col in range(row+1):
        print("*",end=" ")
    print()
