#!usr/bin/python
#Filename d:test4
n=23
guess=int(raw_input("Enteran integer:"))

if guess == n:
    print 'Congratulations you guessed it.'
    print "(but you do not in any prizes)"
elif guess < n:
    print("No,it is a little higher than that")
else:
    print("No,it is a little lower than that")

print ("Done")
