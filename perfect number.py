# num=int(input("enter the number:"))
# result=0
# for i in range(1,num):
#     if num%i==0:
#         result=result+i
# if result==num:
#     print(num,"is perfect number")
# else:
#     print(num,"is not perfect number")

n=int(input("enter the number:"))
s=0
i=1
while i<n:
    if n%i==0:
        s=s+i
    i=i+1
if n==s:
    print("perfect")
else:
    print("not perfect")

