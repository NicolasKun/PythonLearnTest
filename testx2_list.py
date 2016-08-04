#!user/bin/python
#These my colors!
colors=['red','orange','yellow','green']

print 'I have',len(colors),'item color'

print '\n\n------These my color-----'
for item in colors:
    print item

print '\nI also have one color'
colors.append('blue')
print '\n\n------These my color-----'
for item in colors:
    print item

print '\nI will sort my colors'
colors.sort()
print '\n-----These my color now----'
print colors

print '\nThe second item i will use is',colors[1]
olditem=colors[1]
del colors[1]
print '\nI used the',olditem

print '\n-----These my color now----'
print colors
