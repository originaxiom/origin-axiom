"""
Step 2: identify h (self-adjoint operator on W=P(+)P giving t_w as a Jeffrey/Deloup-Turaev
Gauss sum), and compare det(h) = det(w + w^{-1} - 3I)  [derived for word RL, tr(mono(RL))=3]
against the empirically registered conductor  det(A x w - I4)  (weil_mechanism.py's
conductor_menu), A = mono("RL").
"""
import sympy as sp

S1 = sp.Matrix([[-1, 0], [1, 1]])
S2 = sp.Matrix([[1, 1], [0, -1]])
WEYL = []
for word in ((), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)):
    M = sp.eye(2)
    for g in word:
        M = (S1 if g == 0 else S2) * M
    WEYL.append((M, (-1) ** len(word)))

R2 = sp.Matrix([[1, 1], [0, 1]])
L2 = sp.Matrix([[1, 0], [1, 1]])
A = R2 * L2   # mono("RL")
print("A = mono(RL) =", A.tolist(), " tr=", A.trace(), " det=", A.det())

I4 = sp.eye(4)
I2 = sp.eye(2)

print(f"{'wi':>3} {'pm':>3} {'det(h)=det(w+w^-1-3I)':>24} {'det(A x w - I4)':>18}  ratio")
for wi, (Wm, sg) in enumerate(WEYL):
    for pm in (1, -1):
        w = pm * Wm
        winv = w.inv()
        h_det = (w + winv - 3 * I2).det()
        cond = (sp.Matrix(sp.kronecker_product(A, w)) - I4).det()
        ratio = sp.nsimplify(cond / h_det) if h_det != 0 else None
        print(f"{wi:>3} {pm:>+3} {str(h_det):>24} {str(cond):>18}  {ratio}")
