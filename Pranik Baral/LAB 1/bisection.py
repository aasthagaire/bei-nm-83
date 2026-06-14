def f(x):
    return x**3 - x - 2

a = float(input("Enter a: "))
b = float(input("Enter b: "))

tolerance = 0.001
max_iterations = 100

if f(a) * f(b) > 0:
    print("Invalid interval")
else:
    for i in range(max_iterations):
        c = (a + b) / 2

        if abs(b - a) < tolerance:
            print("Approximate root =", c)
            print("Iterations =", i + 1)
            break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c