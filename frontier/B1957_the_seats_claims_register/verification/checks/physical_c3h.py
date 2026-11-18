"""B1957: the physical lane's package C3h (its branch at 4e27d6d41: COMPLETE_CHARGED_KERNEL_ON_THE_B_FAMILY.md and its sender
note), the finite steps recomputed on main (data-free; the lane's note is a hand derivation and it ran no code).
NOT computed: the contraction's analytic extension to complete domains, the Hodge passage, the stationary family itself,
and every step that needs the lane's bundles and sections.
 H1  the spin-3/2 module: X = e13 + e24 kills the three fibre representatives of degrees 0 and 1, and sends the degree-2
     one to |1/2, 1/2>, orthogonal to it.
 H2  the ten-frame: the symmetric form [[0, I5], [I5, 0]] under diag(I5, J5) and the real Hadamard change becomes
     diag(J5, -J5), not diag(J5, J5).
 H3  T = diag(1, -1) anticommutes with an off-diagonal A0 and commutes with a diagonal D; the polarized cubic with the
     sections (f, g) and (f, -g) cancels, and with (f, g) twice it does not.
 H4  the counts: 24 left coefficients in the 128 block, 42 in the charged roster, and the Euler characteristic of (0, 3, 3, 0)."""
import sympy as sp
e = lambda i, j, n=4: sp.Matrix(n, n, lambda a, b: 1 if (a, b) == (i - 1, j - 1) else 0)
X = e(1, 3) + e(2, 4); ket = lambda i: sp.Matrix(4, 1, lambda a, b: 1 if a == i else 0)        # 0..3 is m = 3/2, 1/2, -1/2, -3/2
XX = sp.kronecker_product(X, X); kk = lambda a, b: sp.kronecker_product(ket(a), ket(b))
reps = {"k=0 |j,j>": kk(0, 0), "k=1 |-j,j>": kk(3, 0), "k=1 |j,-j>": kk(0, 3), "k=2 |-j,-j>": kk(3, 3)}
img = {n: XX * v for n, v in reps.items()}
print("H1: X x X on the representatives: %s; the degree-2 image is |1/2, 1/2>: %s, orthogonal to |-j,-j>: %s"
      % ({n: ("0" if v == sp.zeros(16, 1) else "non-zero") for n, v in img.items()}, img["k=2 |-j,-j>"] == kk(1, 1), (img["k=2 |-j,-j>"].T * reps["k=2 |-j,-j>"])[0] == 0))
I5 = sp.eye(5); J5 = sp.Matrix(5, 5, lambda a, b: (-1) ** a if a + b == 4 else 0); Z5 = sp.zeros(5, 5)
B = sp.Matrix(sp.BlockMatrix([[Z5, I5], [I5, Z5]])); D = sp.Matrix(sp.BlockMatrix([[I5, Z5], [Z5, J5]])); H = sp.Matrix(sp.BlockMatrix([[I5, I5], [I5, -I5]])) / sp.sqrt(2)
want, wrong = sp.Matrix(sp.BlockMatrix([[J5, Z5], [Z5, -J5]])), sp.Matrix(sp.BlockMatrix([[J5, Z5], [Z5, J5]]))
res = {}
for name, M in (("Hadamard after diag(I5, J5)", H * D), ("diag(I5, J5) after Hadamard", D * H)):
    Mi = M.inv(); Bp = (Mi.T * B * Mi).applyfunc(sp.simplify); res[name] = ("diag(J5, -J5)" if Bp == want else "diag(J5, J5)" if Bp == wrong else "other")
print("H2: the form [[0, I5], [I5, 0]] in the new frame (inverse transpose): %s; J5 = antidiag(1, -1, 1, -1, 1) is its own inverse up to sign: J5^2 = %s" % (res, "I" if J5 * J5 == I5 else "-I" if J5 * J5 == -I5 else "other"))
T = sp.diag(1, -1); A0 = sp.Matrix([[0, 1], [1, 0]]); D3 = sp.diag(sp.Symbol("d1"), sp.Symbol("d2"))
f, g, C = sp.symbols("f g C")
pol = lambda s: C * (f * (s * g) + f * g)                       # kappa(Z, [u+, v-] + [u-, v+]) with v- = s g: the two terms carry f g and f (s g)
print("H3: T A0 T^-1 = -A0: %s; T D T^-1 = D: %s; the polarized cubic with (f, g) and (f, -g): %s; with (f, g) twice: %s"
      % (T * A0 * T.inv() == -A0, T * D3 * T.inv() == D3, sp.simplify(pol(-1)), sp.simplify(pol(1))))
roster = {"3_(+2/3)": (3, 3), "3bar_(-2/3)": (3, 3), "3_(-1/3)": (3, 3), "3bar_(+1/3)": (3, 3), "1_(+1)": (1, 3), "1_(-1)": (1, 3)}
print("H4: the 128 block, 1_(+1) + 3_(-1/3) and its conjugate, three per coefficient: %d; the roster's left coefficients (colour dimension x multiplicity): %d; Euler characteristic of (0, 3, 3, 0): %d"
      % ((1 + 3) * 2 * 3, sum(a * b for a, b in roster.values()), 0 - 3 + 3 - 0))
