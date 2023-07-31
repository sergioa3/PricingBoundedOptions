import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import math
from scipy.stats import norm
#from mpl_toolkits.mplot3d import axes3d

t_min=0
t_max=10

##parametros de la opcion
r = 0.1
T = 6
E = 1
E2 = 10000000000000000
##parametros del activo
sigma = 5
mu = 1

def option_price(S:float,t:float,r,T,E,E2,sig):
  #simplemente es la formula C(S,t) mas parametros
  
  if T==t:
    C = max(S-E,0)
  elif T<t:
    C = 0
  elif S==0:
    C = 0
  else:
    t2 = T-t
    sig2 = sig*sig/2
    logEs = np.log(E/S)
    logE2s = np.log(E2/S)
    a = norm.cdf((logE2s-((sig2+r)*t2))/(sig*np.sqrt(t2))) - norm.cdf((logEs-((sig2+r)*t2))/(sig*np.sqrt(t2)))
    b = norm.cdf((logE2s+((sig2-r)*t2))/(sig*np.sqrt(t2))) - norm.cdf((logEs+((sig2-r)*t2))/(sig*np.sqrt(t2)))
    C = S*a-E*np.exp(-r*t2)*b 
  
  return C



fig = plt.figure(figsize = (12,10))
ax = plt.axes(projection='3d')

S_infty = 50
step = 0.2

S = np.arange(0, S_infty, step)
t = np.arange(t_min,t_max, step)

S, t = np.meshgrid(S, t)

option_price = np.vectorize(option_price, otypes=[float])

C = option_price(S,t,r,T,E,E2,sigma)

surf = ax.plot_surface(S, t, C, cmap = plt.cm.cividis)

# Set axes label
ax.set_xlabel('S', labelpad=20)
ax.set_ylabel('t', labelpad=20)
ax.set_zlabel('C', labelpad=20)

#ax.invert_xaxis()

fig.colorbar(surf, shrink=0.5, aspect=8)

plt.show()

##parametros de la opcion
r = 0.15
T = t_max
E = 1
E2 = 20
##parametros del activo
sigma = 5
mu = 1



##parametros de la opcion
r = 0.1
T = t_max
E = 4
E2 = 20
##parametros del activo
sigma = 5
mu = 1


##parametros de la opcion
r = 0.15
T = 5
E = 1
E2 = 20
##parametros del activo
sigma = 5
mu = 1


##parametros de la opcion
r = 0.1
T = 9
E = 1
E2 = 20
##parametros del activo
sigma = 5
mu = 1