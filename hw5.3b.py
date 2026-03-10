import sympy as sp

a = sp.symbols('a')

p = sp.Matrix([[1-a, a, 0],
              [a, 0, 1-a],
              [0, 1-a, a]])

p_T = p.T
evals = p_T.eigenvals()
evecs = p_T.eigenvects()

print("Eigenvalues:", evals)
print("Eigenvectors:", evecs)

p_sub = p.subs(a, 0.99)
evals_sub = p_sub.T.eigenvals()
evecs_sub = p_sub.T.eigenvects()

print("Eigenvalues with a=0.99:", evals_sub)
print("Eigenvectors with a=0.99:", evecs_sub)
