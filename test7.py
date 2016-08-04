n=23
flag=True
while flag:
    guess=int(input('Enter Integer: '))
    if guess==n:
        print 'Congratulations!You find it!'
        flag=False
    elif guess<n:
        print 'No,it is a little Lower'
    else:
        print 'No,it is a little Higher'
else:
    print '---This While Is Over---'
print 'Done'

        
