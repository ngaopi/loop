num=int(input("enter the number"))
temp=num 
sum=0
while temp>0:
    sum=sum+(temp%10)
    temp=temp//10
if num%sum==0:
    print("harshad")
else:
    print("not harshad")
    


        
    

        
        
        