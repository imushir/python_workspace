import cPickle as p

shoplistfile = 'demo.data' #the name of the file where we will store the object

shoplist = ['apple','mango','carrot']

#Write to the file
f = file(shoplistfile,'w')
p.dump(shoplist,f)
f.close()

#del shoplist # remove the shoplist

#Read back from the storage
f = file(shoplistfile)
storedlist = p.load(f)
print storedlist