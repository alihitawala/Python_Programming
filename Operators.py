__author__ = 'alihitawala'

# all the regular ones are there +-/*

a = 2**4 # power
print(a)

b = 9//2 # floor divide
print b

#extra comparasion operator <> which works same as !=
print hex(a)
c = a<<2
print hex(c)
print id(a)
print id(c)
print a is c
a = 90
print a is 90 #True

list = [ a, c, 90]
print a in list #True
print a not in list #False
print 90 in list # True
