i=1
count_odd=0
count_even=0
while i<10:
    if i%2==0:
        count_even=count_even+1
    else:
        count_odd=count_odd+1
    i=i+1
print(count_even)
print(count_odd)