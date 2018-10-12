import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

rho = 27.0
sigma = 10.5
beta = 8.0 / 3.0

def f(state, t):
  x, y, z = state  
  return sigma * (y - x), x * (rho - z) - y, x * y - beta * z  

state0 = [1.0, 1.0, 1.0]
t = np.linspace(0 , 40 , 100000)

states = odeint(f, state0, t)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(states[:,0], states[:,1], states[:,2])
plt.show()
