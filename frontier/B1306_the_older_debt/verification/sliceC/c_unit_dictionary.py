"""C14 -- hostile memo 21 (UNIT_DICTIONARY): every closed geodesic of m004 has holonomy eigenvalue a unit of a palindromic quartic labelled by two rational
integers (a, b) with trace t = a + b*omega in Z[omega], and its length is the log-Mahler measure of that quartic. SnapPy length spectrum to LEN, the
holonomy of each word evaluated numerically, the trace recognised in Z[omega] (omega = e^{2 pi i/3}), the quartic (x^2 - t x + 1)(x^2 - conj(t) x + 1)."""
import sys, json, cmath, math
import snappy, sympy as sp
LEN = float(sys.argv[1]) if len(sys.argv) > 1 else 3.0
M = snappy.Manifold("m004"); G = M.fundamental_group(); spec = M.length_spectrum(LEN, include_words=True)
om = complex(-0.5, math.sqrt(3) / 2); x = sp.symbols("x"); rows = []; ok_all = True
for g in spec:
    word = getattr(g, "word", "?"); ell = complex(g.length); t = 2 * cmath.cosh(ell / 2)      # trace from the complex length: lambda + 1/lambda
    # t = a + b*omega  =>  b = Im(t)/Im(omega), a = Re(t) - b*Re(omega)
    b = t.imag / om.imag; a = t.real - b * om.real; ai, bi = round(a), round(b); rec = abs(a - ai) < 1e-6 and abs(b - bi) < 1e-6
    tr_sym = ai + bi * sp.Rational(-1, 2) + bi * sp.sqrt(3) * sp.I / 2
    quart = sp.Poly(sp.expand((x**2 - tr_sym * x + 1) * (x**2 - sp.conjugate(tr_sym) * x + 1)), x)
    coeffs = [sp.nsimplify(c) for c in quart.all_coeffs()]; coeffs = [int(c) for c in coeffs]
    palindromic = coeffs == coeffs[::-1]; unit = coeffs[-1] == 1 and coeffs[0] == 1
    lam = cmath.exp(ell / 2); val = sum(c * lam ** (4 - i) for i, c in enumerate(coeffs))
    import numpy as np
    rts = [complex(r) for r in np.roots([float(c) for c in coeffs])]; logM = sum(max(0.0, math.log(abs(r))) for r in rts)
    row = dict(word=word, length=round(ell.real, 9), torsion=round(ell.imag, 6), a=ai, b=bi, recognised=rec, quartic=coeffs, palindromic=palindromic, unit=unit,
               root_residual=abs(val), logM=round(logM, 9), length_eq_logM=abs(logM - ell.real) < 1e-6)
    rows.append(row); ok_all &= rec and palindromic and unit and abs(val) < 1e-6 and row["length_eq_logM"]
    print(f"  {word:<12} l={ell.real:.6f} t=({ai},{bi})  quartic {coeffs}  palindromic {palindromic} unit {unit} |f(lam)|={abs(val):.1e}  logM={logM:.6f} == l: {row['length_eq_logM']}")
print(f"geodesics to length {LEN}: {len(rows)}; all obey the dictionary: {ok_all}")
json.dump(dict(LEN=LEN, n=len(rows), ok=ok_all, rows=rows), open("c_unit_dictionary.json", "w"), indent=1)
print("C14:", "PASS" if ok_all else "FAIL")
