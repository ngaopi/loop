# 1
# 4 9
# 16 25 36
# 49 64 81 100

i=1 
sum=1 
while i<=4:
    j=1
    while j<=i:
        print(sum*sum,end=" ")
        sum=sum+1
        j=j+1
    i=i+1
    print()