# Unit-I Introduction to Counting Principles: Set Theory, Functions and Relations, POSETS and Lattices, Permutation and Combination, Probability, Pigeon-hole principle.

# Unit-I: Counting Principles Implementation in Python

# 1. Set Theory
print("=== Set Theory ===")
A = {1, 2, 3}
B = {2, 3, 4}
print("Union:", A | B)
print("Intersection:", A & B)
print("Difference (A - B):", A - B)
print("Symmetric Difference:", A ^ B)
print()

# 2. Functions and Relations
print("=== Functions and Relations ===")
X = [1, 2, 3]
Y = [4, 5]
relation = [(x, y) for x in X for y in Y]
function = {x: x**2 for x in X}
print("Relation from X to Y:", relation)
print("Function f(x) = x^2:", function)
print()

# 3. POSETS (Partially Ordered Sets)
print("=== POSETS ===")
# A poset is a set with a partial order relation (e.g., divisibility)
S = {1, 2, 4, 8}
poset = [(a, b) for a in S for b in S if a <= b]
print("POSET (<= relation):", poset)
print()

# 4. Lattices
print("=== Lattices ===")
# A lattice is a poset where every pair has a unique least upper bound (join) and greatest lower bound (meet)
def meet(a, b):
    return a & b

def join(a, b):
    return a | b

a, b = 0b1100, 0b1010
print("Meet (AND) of", bin(a), "and", bin(b), ":", bin(meet(a, b)))
print("Join (OR) of", bin(a), "and", bin(b), ":", bin(join(a, b)))
print()

# 5. Permutation and Combination
import math
print("=== Permutation and Combination ===")
n, r = 5, 3
perm = math.perm(n, r)
comb = math.comb(n, r)
print(f"Permutation P({n},{r}) = {perm}")
print(f"Combination C({n},{r}) = {comb}")
print()

# 6. Probability
print("=== Probability ===")
# Simple probability of an event
sample_space = ['H', 'T']
event = ['H']
prob = len(event) / len(sample_space)
print("Probability of getting Heads:", prob)
print()

# 7. Pigeon-hole Principle
print("=== Pigeon-hole Principle ===")
items = ['apple', 'banana', 'cherry', 'banana', 'apple', 'apple']
counts = {}
for item in items:
    counts[item] = counts.get(item, 0) + 1
print("Item counts (Pigeon-hole distribution):", counts)
pigeonholes = len(set(items))
print("Items:", len(items), "| Pigeonholes:", pigeonholes)
if len(items) > pigeonholes:
    print("By pigeon-hole principle, at least one pigeonhole has more than one item.")
print()
