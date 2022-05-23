
n=int(input("enter the number:"))
temp=n 
sum=0
while n>0:
    dig=n%10
    j=1
    for i in range(1,dig+1):
        j=j*i 
    sum=sum+j 
    n=n//10
if temp==sum:
    print("strong")
else:
    print("weak")
        


    
    
    
    
