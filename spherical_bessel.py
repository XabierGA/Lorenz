import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set()

def spherical_bessel_freq(a,b):
    h = b-a
    k = np.linspace(0, h , 10000)
    y = np.arctan((k*h * ( k**2 + 1/(a*b)))/(k**2+a*b*(k**2-1/(a**2))*(k**2-1/(b**2))))
    y = y/h
    return k,y

k, y = spherical_bessel_freq(9 , 10)
plt.plot(k, y , 'b-' , label = 'Characteristic frequencies solution')
plt.xlabel('K   $[L^{-1}]$')
plt.ylabel('Y')
plt.legend(loc = 1)
plt.show(True)
