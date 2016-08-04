#!user/bin/python
import sys

print 'The command line arguments are:'
for i in sys.argv:
    print i

print '\n\nThePYTHON is ',sys.path,'\n'

from testx1 import sayHello,ver
sayHello(1,1)
print ver
