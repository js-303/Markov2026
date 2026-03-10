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


