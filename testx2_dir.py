#!user/bin/python

ab={
    'red':'flag',
    'yellow':0,
    'orange':'orange'
    }
print 'Red have is %s'%ab['red']

#add key/value
ab['blue']='sky'

print '------There are now dir length-----'
print len(ab)

#delet a key/value
del ab['orange']

print '------There are now dir-----'
for color,st in ab.items():
    print '%s ---> %s'%(color,st)
    
