# write a program to find the product of the digits of a number accepted from the user. 
n=int(input("enter the number"))
product=1
while i>0:
    product=product*(n%10)
    i=i//10
print("prod of digits=",product)


