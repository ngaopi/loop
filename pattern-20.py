# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

i=1 
sum=1 
while i<=5:
    j=1
    while j<=i:
        print(sum,end=" ")
        sum=sum+1
        j=j+1
    i=i+1
    print()


