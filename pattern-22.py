# 1
# 2 *
# 3 * 3
# 4 * 4 *
# 5 * 5 * 5
i=1
while i<=5:
    j=1
    while j<=i:
        if j%2!=0:
            print(i,end=" ")
        else:
            print("*",end=" ")
        j=j+1
    i=i+1
    print()
                                                                                