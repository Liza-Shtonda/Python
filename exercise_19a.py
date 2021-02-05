#

import matplotlib.pyplot as plt
%matplotlib inline

def f(x):
    return (x**3+2*x**2-3*x-2)/(x**2+x-2)

a=2
b=5
n=21
x=np.linspace(a, b, n)
y=f(x)
plt.plot(x, y, color='red', marker='x', linestyle='none')
plt.show()