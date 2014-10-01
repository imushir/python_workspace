from deltasigma import *
import numpy as np
import pylab as plt
order = 4
osr = 64
nlev = 2
f0 = 0.
Hinf = 1.5
form = 'CRFB'
ntf = synthesizeNTF(order, osr, 2, Hinf, f0)
a, g, b, c = realizeNTF(ntf, form)
b = np.concatenate(( # Use a single feed-in for the input
                    np.atleast_1d(b[0]),
                    np.zeros((b.shape[0] - 1,))
                  ))
ABCD = stuffABCD(a, g, b, c, form)
DocumentNTF(ABCD, osr, f0)