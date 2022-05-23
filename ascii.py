n=int(input("enter the number of rows:"))
i=0
while i<n:
    k=ord("A")+i
    j=0
    while j<=i:
        print(chr(k),end=" ")
        k=k+1
        j=j+1
    i=i+1
    print()
#
# n=int(input("enter the number of rows:"))
# for i in range(n):
#     k=ord("A")+i
#     for j in range(i+1):
#         print(chr(k),end=" ")
#         k=k+1
#     print()

# chr=input("enter the chr:")
# a=ord(chr)
# print("chr=",a)

# ord=int(input("enter the ord:"))
# a=chr(ord)
# print("order=",a)

