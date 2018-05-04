import  matplotlib.pyplot as plt
import  numpy as np

x = np.linspace(-np.pi,np.pi,256,endpoint=True)
c,s = np.cos(x),np.sin(x)
plt.figure(1)
plt.plot(x,c)
plt.plot(x,s)
plt.title("COS 和 SIN")
plt.show()