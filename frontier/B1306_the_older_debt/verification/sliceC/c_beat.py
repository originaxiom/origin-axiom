"""C10 -- hostile memo 16 (FIRST_BEAT): W = [[1, q],[0, 1]] acting antilinearly by z -> conj(z) + q; W.conj(W) = [[1, q + conj(q)],[0,1]]; with q + conj(q) = 1
(q = e^{i pi/3}) the square is the meridian shear [[1,1],[0,1]]. Exact in Q(sqrt-3)."""
import sympy as sp
q = sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2; W = sp.Matrix([[1, q], [0, 1]]); WW = W * W.conjugate()
print("W conj(W) =", sp.simplify(WW)); ok = sp.simplify(WW - sp.Matrix([[1, 1], [0, 1]])) == sp.zeros(2)
print("q + conj(q) =", sp.simplify(q + sp.conjugate(q)), "; |q| =", sp.simplify(sp.Abs(q)))
print("C10:", "PASS" if ok and sp.simplify(q + sp.conjugate(q)) == 1 else "FAIL")
