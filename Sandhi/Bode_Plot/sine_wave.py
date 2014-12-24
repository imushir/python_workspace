import math
import matplotlib.pyplot as plt

a = []
for i in range(0,20):
    t = 0.02*i
    print"Time",t
    a.append(math.sin(t))
print "Sin30",math.sin(30)
print "A :",a
plt.plot(a)
plt.show()