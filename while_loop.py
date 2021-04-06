#while loop
#while[condition]-->true
#this this
#then go back to the while loop
#condition example
#5<6 ->true
#6<5-->false

#print 1 to 100 using while loop
count = 0
while count < 101:
    print(count)
    count =count + 1

#print 100 to 1 and when it comes up on zero then print 'blast off!'
count = 100
while count >= 0:
    if count == 0:
        print("blast off!")
    else:
        print(count)
    count = count - 1
