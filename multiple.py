# write a code to print all the multiple of 5 from 1 to 50.but you dont need to use % .

# i=0
# while i<=50:
#     if i!=5:
#        print(i)
#     i=i+5
user=int(input("enter the number:"))
i=1 
while i<=user:
    print("table",i)
    j=1
    while j<=user:
        print(i,"*",j,"=",i*j)
        j=j+1
    i=i+1
    print()




