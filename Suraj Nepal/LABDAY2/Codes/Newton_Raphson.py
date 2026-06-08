import matplotlib.pyplot as plt
import numpy as np
def f(x1):
    return 4*x**3-3

def newton(f,x0,x1,tol=1e-7,ite=10):
    for i in range(ite):
        f_x0=f(x0)
        f_x1=f(x1)

        xn=x1-(f_x0/f_x1)
        x0=x1
        x1=xn
        if abs(f_x1-f_x0)<tol:
            print("found root ", xn)
func= lambda x:  x**4-3*x-2
root=secant(func,2.5,3)
x=np.linspace(-3,3,400)
y=func(x)
plt.figure(figsize=(8,5))
plt.plot(x,y,label='f(x)=x^4-3x-2')
plt.axhline(0)
plt.legend()
plt.show 