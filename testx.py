#!user/bin/python
running=True

while running:
    index=int(input("Enter an integer: \n"))
    if index<=35:
        for i in range(1,index):
            print i
            continue
    elif index==36:
        break
    else :
        print "is to large~"

print '\nDone.'
