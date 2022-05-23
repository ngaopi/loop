# num=int(input("enter the number"))
# if num>1:
#     for i in range(2,num):
#         if num%i==0:
#             print(num,"is not prime number")
#             break
#     else:
#         print(num,"is a prime")

# num=int(input("enter the number"))
# i=1 
# j=0
# while i<=num%2:
#     if num%i==0:
#         j=1
#         break2
#     i=i+1
# if j==0:
#     print("it is not a prime")
# else:
#     print("it is a prime")

a=int(input("enter the number:"))
i=1
j=0
while i<=a:
    if a%i==0 and a%a==0:
        j=j+1
    i=i+1
if j==2:
    print("it is a prime")
else:
    print("it is not a prime")

