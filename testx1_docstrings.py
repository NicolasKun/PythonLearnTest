#!user/bin/python
def printMax(x,y):
    '''Prints the maximum or two numbers

    The two values must be in tegers'''
    x=int(x)
    y=int(y)

    if x>y:
        print x,' is maximum~'
    else:
        print y,' is maximun~s'
def printM():
    '''This test of docstrings

    The test of docstrings'''

printMax(3,5)
print printM.__doc__
print printMax.__doc__
