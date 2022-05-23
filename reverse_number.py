# n=int(input("enter the number:"))
# rev=0
# while n>0:
#     rev=rev*10+n%10
#     n=n//10
# print(rev)

n=int(input("enter the number:"))
rev=str(n)
b=" "
i=-1
while i>=-len(rev):
    b=b+rev[i]
    i=i-1
print(b)

