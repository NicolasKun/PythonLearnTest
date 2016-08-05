#!user/bin/python
colors=('red','orange','yellow')
print 'Number of colors in my right-hand',len(colors)

new_colors=('green','blue',colors)
print 'Number of colors in my left-hand',len(new_colors)
print 'All colors in my left-hand',new_colors
print 'colors brought from right-hand',new_colors[2]
print 'Last color brought from right-hand',new_colors[2][2]

s=()
ss=(1,)
print 'there are one empty tuple',s
print 'also have one',ss

name='Yu'
age=23
print '%s is %d years old'%(name,age)
print 'What\'s matter with %s ?'%name
