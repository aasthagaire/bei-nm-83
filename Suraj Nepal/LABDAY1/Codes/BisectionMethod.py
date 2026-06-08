def f(x):
    return x**3-x-2
def bisection(f,a,b,tol=1e-6,max_ite=100):
     for i in range(max_ite):
        c = (a + b) / 2
        if abs(f(c)) < tol or (b - a) / 2 < tol:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
     return (a + b) / 2
root=bisection(f,1,2)
print("Root:",root)