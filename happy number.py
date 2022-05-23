num=int(input("enter the number:"))
rem=0
res=0
while num>0:
    rem=num%10
    res=res+rem*rem 
    num=num//10
if rem==1:
    print("happy number")
else:
    print("sad number")


    