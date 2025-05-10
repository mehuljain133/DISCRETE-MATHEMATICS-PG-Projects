# Unit-III Growth of Functions: Asymptotic notations, monotonicity, comparison of standardfunctions - floors and ceilings, polynomials, exponentials, logarithms and factorials, summations:summation formulas and properties, bounding summations, approximation by integrals


import math
import sympy as sp
from sympy import symbols, Sum, factorial, log, ceiling, floor, integrate, oo, simplify, Function
from sympy.abc import n

print("=== Growth of Functions ===")

# 1. Asymptotic Notations
print("\n--- Asymptotic Notations ---")
f = n**2 + 3*n + 2
g = n**2
print("f(n) =", f)
print("g(n) =", g)
print("Big-O: f = O(n^2)?", simplify(f/g).limit(n, oo).is_finite)

# 2. Monotonicity
print("\n--- Monotonicity ---")
f = n**2
diff = sp.diff(f, n)
print("f(n) =", f)
print("f'(n) =", diff)
print("Monotonic Increasing?" , diff > 0)

# 3. Comparison of Standard Functions
print("\n--- Comparison of Standard Functions ---")
ns = list(range(1, 10))
print(f"{'n':>3} {'log(n)':>10} {'n':>5} {'n*log(n)':>10} {'n^2':>7} {'2^n':>10} {'n!':>10}")
for i in ns:
    try:
        print(f"{i:>3} {math.log(i):>10.3f} {i:>5} {i*math.log(i):>10.3f} {i**2:>7} {2**i:>10} {math.factorial(i):>10}")
    except:
        pass

# 4. Floor and Ceiling
print("\n--- Floor and Ceiling ---")
x = sp.Symbol('x', real=True)
expr = 2.7
print("Floor of 2.7:", floor(expr))
print("Ceiling of 2.7:", ceiling(expr))

# 5. Polynomial, Exponential, Logarithmic, Factorial
print("\n--- Standard Function Growth ---")
print("n^2 vs 2^n:")
for i in range(1, 11):
    print(f"n={i}, n^2={i**2}, 2^n={2**i}")

print("\nn vs log(n):")
for i in range(1, 11):
    print(f"n={i}, log(n)={math.log(i):.4f}")

print("\nn! vs n^2:")
for i in range(1, 10):
    print(f"n={i}, n!={math.factorial(i)}, n^2={i**2}")

# 6. Summations
print("\n--- Summation Formulas ---")
sum1 = Sum(n, (n, 1, 10)).doit()
sum2 = Sum(n**2, (n, 1, 10)).doit()
print("Sum of n from 1 to 10:", sum1)
print("Sum of n^2 from 1 to 10:", sum2)

# 7. Bounding Summations
print("\n--- Bounding Summations ---")
bound_expr = Sum(1/n, (n, 1, 100))
print("Approximate value of Harmonic Series sum H_100:", bound_expr.doit())

# 8. Approximation by Integrals
print("\n--- Approximation by Integrals ---")
expr = 1/x
integral_approx = integrate(expr, (x, 1, 100))
print("Integral approximation of ∑1/n from 1 to 100:", integral_approx.evalf())

# 9. Additional: Stirling’s Approximation
print("\n--- Stirling’s Approximation ---")
for i in range(1, 10):
    exact = math.factorial(i)
    stirling = math.sqrt(2 * math.pi * i) * (i / math.e)**i
    print(f"n={i}, n!={exact}, Stirling ≈ {stirling:.2f}")
