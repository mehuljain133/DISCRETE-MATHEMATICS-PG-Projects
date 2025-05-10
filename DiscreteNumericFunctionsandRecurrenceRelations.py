# Unit-V Discrete Numeric Functions and Recurrence Relations Discrete Numeric Functions, Generating functions, Recurrence Relations.

pip install sympy

import sympy as sp
from sympy.abc import n, x
from sympy import Function, rsolve, Eq, symbols, factorial, simplify, apart, expand

print("=== Unit-V: Discrete Numeric Functions and Recurrence Relations ===")

# 1. Discrete Numeric Function
print("\n--- Discrete Numeric Functions ---")
def f(n): return n**2 + 2*n + 1
print("f(n) = n^2 + 2n + 1")
print("f(0 to 5):", [f(i) for i in range(6)])

# 2. Generating Functions
print("\n--- Generating Function ---")
# Example: Sequence a_n = 1 (constant sequence)
a_n = [1]*6
G = sum([a_n[i]*x**i for i in range(len(a_n))])
print("Generating function for a_n = 1:", G)
G_sum = 1 / (1 - x)
print("Closed form: G(x) = 1 / (1 - x)")

# For a_n = n
print("\nGenerating function for a_n = n")
gen_fn = x / (1 - x)**2
print("G(x) =", gen_fn)

# 3. Recurrence Relations
print("\n--- Recurrence Relations ---")
# Example: a_n = 2a_(n-1), a_0 = 1 → a_n = 2^n
a = Function('a')
rec = Eq(a(n) - 2*a(n-1), 0)
sol = rsolve(rec, a(n), {a(0): 1})
print("Solving a_n = 2a_(n-1), a_0 = 1")
print("Solution: a(n) =", sol)

# Fibonacci: F(n) = F(n-1) + F(n-2), F(0)=0, F(1)=1
print("\nSolving Fibonacci: F(n) = F(n-1) + F(n-2)")
F = Function('F')
fib_eq = Eq(F(n) - F(n-1) - F(n-2), 0)
fib_sol = rsolve(fib_eq, F(n), {F(0): 0, F(1): 1})
print("Fibonacci closed form:")
print("F(n) =", fib_sol)

# 4. Generating Function for Geometric Series
print("\n--- Generating Function for Geometric Series ---")
a_n = [2**i for i in range(6)]
gen_geom = sum([a_n[i]*x**i for i in range(len(a_n))])
print("First terms: ", a_n)
print("Generating function (2^n):", gen_geom)
closed_form = 1 / (1 - 2*x)
print("Closed form: G(x) = 1 / (1 - 2x)")

# 5. Generating Function to Sequence (Inverse)
print("\n--- Generating Function to Sequence ---")
gf = x / (1 - x)**2
terms = [gf.series(x, 0, i).removeO().coeff(x, i-1) for i in range(1, 6)]
print("Sequence from G(x) = x / (1 - x)^2:", terms)

# 6. Advanced: Solving linear homogeneous recurrence with constant coefficients
print("\n--- Linear Homogeneous Recurrence ---")
# a_n = 3a_(n-1) - 2a_(n-2), a_0 = 2, a_1 = 3
a = Function('a')
rec = Eq(a(n) - 3*a(n-1) + 2*a(n-2), 0)
solution = rsolve(rec, a(n), {a(0): 2, a(1): 3})
print("Solving a_n = 3a_(n-1) - 2a_(n-2), a_0 = 2, a_1 = 3")
print("a(n) =", solution)
