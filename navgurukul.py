# make a program that should do the following thing from 1 to 100.
#1.numbers that are divisible by 3,you have to print "nav"
#2.numbers that are divisible by 7 print "gurukul".
#3.numbers that are divisible by both 3 and 7 print "navgurukul"
#4.if the number does not come in the above three cases then print the number only
i=1 
while i<=100:
    if i%3==0:
        print("nav")
    if i%7==0:
        print("gurukul")
    if i%3==0 and i%7==0:
        print("navgurukul")
    if i%3!=0 and i%7!=0:
        print(i)
    i=i+1