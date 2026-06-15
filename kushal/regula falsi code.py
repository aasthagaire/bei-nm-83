def f(x):
    return x**3 - x - 2

a = 1
b = 2
tolerance = 0.0001
max_iter = 100

if f(a) * f(b) >= 0:
    print("Invalid interval. Root is not bracketed.")
else:
    print("Iteration\tc\t\tf(c)")

    for i in range(max_iter):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))

        print(f"{i+1}\t\t{c:.6f}\t{f(c):.6f}")

        if abs(f(c)) < tolerance:
            print("\nApproximate root =", round(c, 6))
            break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c