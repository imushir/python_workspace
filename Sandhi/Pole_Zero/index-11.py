import pylab as plt
from deltasigma import synthesizeNTF, plotPZ
order = 5
osr = 32
f0 = 0.
Hinf = 1.5
ntf = synthesizeNTF(order, osr, 2, Hinf, f0)
plt.figure(figsize=(8, 6))
plotPZ(ntf, color=('r', 'b'), showlist=True)
plt.title("NTF singularities")
plt.show()