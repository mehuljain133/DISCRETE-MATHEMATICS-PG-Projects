# Unit-II Mathematical Logic: Propositions, connectives, conditionals and biconditionals, well formedformulas, tautologies, equivalence of formulas, duality law, normal forms, inference theory forpropositional calculus; predicate calculus: predicates, free and bound variables, inference theory ofpredicate calculus.

pip install sympy

# Unit-II: Mathematical Logic using SymPy
from sympy import symbols, Not, And, Or, Implies, Equivalent, simplify_logic
from sympy.logic.boolalg import is_tautology, to_cnf, to_dnf
from sympy.abc import x, y, z

print("=== Propositions and Connectives ===")
p, q, r = symbols('p q r')
expr1 = And(p, Not(q))  # p ∧ ¬q
expr2 = Or(p, q)        # p ∨ q
expr3 = Implies(p, q)   # p → q
expr4 = Equivalent(p, q)  # p ↔ q
print("Expression (p AND NOT q):", expr1)
print("Expression (p OR q):", expr2)
print("Conditional (p → q):", expr3)
print("Biconditional (p ↔ q):", expr4)
print()

print("=== Well-formed Formulas (WFF) ===")
# All above expressions are WFFs (constructed from valid rules)
wff = And(Or(p, q), Not(And(p, Not(q))))
print("WFF example:", wff)
print()

print("=== Tautologies ===")
taut = Or(p, Not(p))  # Law of excluded middle
print("Tautology (p ∨ ¬p):", taut)
print("Is tautology?", is_tautology(taut))
print()

print("=== Equivalence of Formulas ===")
A = Implies(p, q)
B = Or(Not(p), q)
print("A: p → q =", A)
print("B: ¬p ∨ q =", B)
print("A ≡ B?", Equivalent(A, B))
print()

print("=== Duality Law ===")
# Demonstrate dual of a logical expression (AND <-> OR, T <-> F)
def dual(expr):
    return expr.replace(And, Or).replace(Or, And)

original = And(Or(p, q), r)
dual_expr = dual(original)
print("Original:", original)
print("Dual:", dual_expr)
print()

print("=== Normal Forms ===")
expr = Or(And(p, q), Not(r))
print("Original expression:", expr)
print("CNF (Conjunctive Normal Form):", to_cnf(expr, simplify=True))
print("DNF (Disjunctive Normal Form):", to_dnf(expr, simplify=True))
print()

print("=== Inference Theory (Propositional Calculus) ===")
# Modus Ponens: If p → q and p, then q
premise1 = Implies(p, q)
premise2 = p
conclusion = q
print("Premises: p → q and p")
print("Conclusion: q")
print("Is Modus Ponens valid?", is_tautology(Implies(And(premise1, premise2), conclusion)))
print()

print("=== Predicate Calculus ===")
from sympy import Function, ForAll, Exists

# Define predicates
P = Function('P')
Q = Function('Q')

print("Predicate Examples:")
predicate1 = ForAll(x, P(x))  # ∀x P(x)
predicate2 = Exists(x, Q(x))  # ∃x Q(x)
print("Universal Quantifier:", predicate1)
print("Existential Quantifier:", predicate2)
print()

print("=== Free and Bound Variables ===")
expr = ForAll(x, Exists(y, P(x) & Q(y)))
print("Expression:", expr)
print("Free variables:", expr.free_symbols)
print("Bound variables:", expr.bound_symbols)
print()

print("=== Inference Theory (Predicate Calculus) ===")
# Demonstrate a form of inference (∀x P(x) ⟹ P(a))
from sympy import Symbol
a = Symbol('a')
universal = ForAll(x, P(x))
instance = P(a)
print("From ∀x P(x), we infer P(a)")
print("Universal:", universal)
print("Instance:", instance)
print("Is instance valid from universal? (Assumed true for logical systems)")
