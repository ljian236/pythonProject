"""import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-3,3,50)
y1=2*x+1
y2=x**2

#plt.figure()
#plt.plot(x,y1)

plt.figure(num=4,figsize=(8,5))
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=3.0,linestyle='--')

plt.xlim(-1,2)
plt.ylim(-2.7)
plt.xlabel('I am X')
plt.ylabel('I am Y')




plt.show()


x=np.linspace(-3,3,50)
y1=2*x+1
y2=x**2

plt.figure()
plt.plot(x,y1)

plt.figure(num=3, figsize=(8,5))
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=10.0,linestyle='--')

plt.show()

"""


import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig,ax=plt.subplots()

x=np.arange(0,2*np.pi,0.01)
line,=ax.plot(x,np.sin(x))

def animate(i):
    line.set_ydata(np.sin(x+i/100))
    return line,

def init():
    line.set_ydata(np.sin(x))
    return line,

ani=animation.FuncAnimation(fig=fig,func=animate,frames=100,init_func=init,interval=20,blit=True)
plt.show()