#with open("/home/fossee/Sandhi_Intership_Work/Sandhi-CustomBlocks/gr-scigen/python/test.sci") as f:
#    for line in f:
#        print line
f = open("/home/fossee/Sandhi_Intership_Work/Sandhi-CustomBlocks/gr-scigen/python/test.sci")
x = f.read()
x = x.split("\n")
code_string = ""
for i in range(0,len(x)):
    code_string += x[i]
print(code_string.split(";"))
