ab = { 'A':'AAAAAAAA','B':'BBBBBBB','C':'CCCCCCCCC','D':'DDDDDDDD' }
print "A's address is %s" %ab['A']

#Adding a key/value pair
ab['E'] ='EEEEEEE'

del ab['B']
print '\n There are %d contacts in the address-book\n' % len(ab)

for name,address in ab.items():
    print 'Contact %s at %s ' %(name,address)
if 'B' in ab:
    print "\n B's address is %s "%ab['E']
else:
    print '\n B is not there'