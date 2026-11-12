#!/usr/bin/env python3
"""WP-1.6: the law of the rates for every sector of the three-strand braid group, the record's triplet among them.

THE TWO MOVES ARE BRAID GENERATORS.  L and R^-1 satisfy the braid relation L R^-1 L = R^-1 L R^-1, so s1 -> L,
s2 -> R^-1 is a representation of the braid group on three strands.  Put S = L R^-1 L and U = L R^-1.  Then
S^2 = U^3 = z, the centre's generator; L = U^-1 S and R = U S^-1; and in an irreducible unitary sector z is a scalar c.
So   L + R = U^-1 S + U S^-1 = (U^-1 + c^-1 U) S = U^-1 (1 + U^-1) S        (c^-1 U = U^-2, because U^3 = c),
with U^-1 and S unitary.  CONSEQUENCES, for A = (L + R) / 2:
  B1  the singular values of A are |cos(t / 2)|, t running over the arguments of U's eigenvalues: the rate is at most
      the largest of them, and |det A| is their product;
  B2  c = 1 (even sectors): U's eigenvalues are 1, w, w^2: singular values 1 and 1/2;
      c = -1 (odd): -1, -w, -w^2: 0 and sqrt 3 / 2;
      c = +-i (modules of the double cover, the record's triplet): three values, cos 15, cos 45 and cos 75 degrees.
WHAT IS COMPUTED: B1 on the record's triplet (B1610's matrices), on the three theta constants in their classical
transformation, on the two-dimensional odd sectors of levels 3 and 5 and on their six joins; the triplet's
characteristic polynomial, exactly, from its monomial form (24th roots of unity; sympy).
HOW IT COULD FAIL: the planted case replaces R by its inverse (then the two letters satisfy no braid relation with
S^2 = U^3 and B1's singular values are not U's cosines)."""
import cmath, importlib.util, json, math, pathlib, sys
import numpy as np, sympy as sp
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
CHECKS = []
def check(name, ok, detail=""):
    CHECKS.append({"check": name, "holds": bool(ok), "detail": str(detail)[:400]}); print("%s  %s%s" % ("ok  " if ok else "FAIL", name, ("  [%s]" % str(detail)[:320]) if detail else ""), flush=True)

def law(L, R):
    n = L.shape[0]; I = np.eye(n); Ri = np.linalg.inv(R)
    S, U = L @ Ri @ L, L @ Ri
    S2, U3 = S @ S, U @ U @ U
    scalar = np.allclose(S2, S2[0, 0] * I, atol=1e-8) and np.allclose(U3, S2, atol=1e-8)
    c = S2[0, 0] if scalar else None
    sv = sorted(np.linalg.svd((L + R) / 2, compute_uv=False), reverse=True)
    cos = sorted((abs(math.cos(cmath.phase(u) / 2)) for u in np.linalg.eigvals(U)), reverse=True)
    ev = np.linalg.eigvals((L + R) / 2)
    return {"S^2 = U^3 is a scalar": bool(scalar), "c": None if c is None else [round(float(c.real), 6), round(float(c.imag), 6)],
            "singular values": [round(float(x), 8) for x in sv], "cosines of half U's arguments": [round(float(x), 8) for x in cos],
            "agree": bool(scalar and np.allclose(sv, cos, atol=1e-7)), "rate": round(float(max(abs(ev))), 9), "|det|": round(float(abs(np.linalg.det((L + R) / 2))), 9)}

spec = importlib.util.spec_from_file_location("hands", ROOT / "frontier/B1610_the_hands_on_the_founding_torsor/verification/hands_on_the_torsor.py")
H = importlib.util.module_from_spec(spec); spec.loader.exec_module(H)
TB = H.PIECES["T"]; TL, TR = TB.conj().T @ H.W.ML @ TB, TB.conj().T @ H.W.MR @ TB
z8 = cmath.exp(1j * math.pi / 4)
thL = np.array([[z8, 0, 0], [0, 0, 1], [0, 1, 0]]); thS = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]], dtype=complex); thR = thS @ np.linalg.inv(thL) @ np.linalg.inv(thS)
out = {}
out["the record's triplet"] = law(TL, TR); out["the three theta constants, classical"] = law(thL, thR)
c15, c45, c75 = (math.cos(math.radians(d)) for d in (15, 45, 75))
for k in ("the record's triplet", "the three theta constants, classical"):
    r = out[k]
    check("B1 on %s: S^2 = U^3 = i, and the singular values of the averaged move are cos 15, cos 45, cos 75 degrees" % k,
          r["agree"] and r["c"] == [0.0, 1.0] and np.allclose(r["singular values"], [c15, c45, c75], atol=1e-7), "singular values %s; rate %s; |det| %s (sqrt2 / 8 = %.9f)" % (r["singular values"], r["rate"], r["|det|"], math.sqrt(2) / 8))
import the_join_at_15 as J15                                                # runs its own read-out on import; its doublets() is used
d3, d5 = J15.d3, J15.d5
allok = True
for name, ds in (("level 3", d3), ("level 5", d5)):
    for i, d in enumerate(ds):
        r = law(d["L"], d["R"]); out["%s, doublet %d" % (name, i)] = r; allok &= r["agree"] and r["c"] == [-1.0, 0.0]
check("B1 on the five two-dimensional odd sectors of levels 3 and 5: c = -1, and the singular values are U's cosines", allok,
      {k: v["singular values"] for k, v in out.items() if "doublet" in k})
joins = True
for i, a in enumerate(d3):
    for j, b in enumerate(d5):
        r = law(np.kron(a["L"], b["L"]), np.kron(a["R"], b["R"])); out["join %d x %d" % (i, j)] = r; joins &= r["agree"] and r["c"] == [1.0, 0.0]
check("B1 on their six joins: c = +1, and the singular values are 1 and 1/2 in the numbers U's fixed vectors give", joins, {k: (v["singular values"], v["rate"]) for k, v in out.items() if k.startswith("join")})
# the triplet's characteristic polynomial, exactly, from its monomial form (columns j -> row p[j] with the 24th root of unity e[j])
ROOT8 = {3: (1 + sp.I) / sp.sqrt(2), 21: (1 - sp.I) / sp.sqrt(2)}          # the two 24th roots of unity that occur: exp(i pi/4) and its conjugate, written with radicals
def mono(p, e):
    M = sp.zeros(3, 3)
    for j in range(3): M[p[j], j] = ROOT8[e[j]]
    return M
XL, XR = mono((0, 2, 1), (21, 3, 3)), mono((1, 0, 2), (21, 21, 3))            # B1866's lock gives the triplet in this form
x = sp.symbols("x"); poly = sp.Poly(sp.expand((x * sp.eye(3) - (XL + XR)).det()), x)
poly = sp.Poly([sp.nsimplify(sp.simplify(sp.expand(c))) for c in poly.all_coeffs()], x).as_expr()
target = x ** 3 - sp.sqrt(2) * x ** 2 + x + sp.sqrt(2)
num = np.array(sp.N(XL, 30).tolist(), dtype=complex), np.array(sp.N(XR, 30).tolist(), dtype=complex)
same_spec = np.allclose(sorted(np.linalg.eigvals(num[0] + num[1]), key=lambda v: (round(v.real, 6), round(v.imag, 6))), sorted(np.linalg.eigvals(TL + TR), key=lambda v: (round(v.real, 6), round(v.imag, 6))), atol=1e-8)
check("the triplet, exactly: det(x - (T_L + T_R)) = x^3 - sqrt2 x^2 + x + sqrt2 (from the monomial form of B1866's lock, which has the spectrum of B1610's matrices)",
      sp.simplify(poly - target) == 0 and same_spec, str(sp.nsimplify(poly)))
thpoly = sp.Poly(sp.expand((x * sp.eye(3) - (sp.Matrix([[ROOT8[3], 0, 0], [0, 0, 1], [0, 1, 0]]) + sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, ROOT8[21]]]))).det()), x)
thpoly = sp.Poly([sp.nsimplify(sp.simplify(sp.expand(c))) for c in thpoly.all_coeffs()], x).as_expr()
check("the three theta constants, exactly: det(x - (L + R)) = (x - sqrt2)(x - 1)(x + 1)", sp.simplify(thpoly - sp.expand((x - sp.sqrt(2)) * (x - 1) * (x + 1))) == 0)
y = sp.symbols("y"); cubic = sp.Poly(2 * y ** 3 - 2 * y ** 2 + y + 1, y)
check("with x = sqrt2 y the triplet's polynomial is 2y^3 - 2y^2 + y + 1, irreducible over the rationals, of discriminant -152", sp.simplify(sp.expand(target.subs(x, sp.sqrt(2) * y)) - sp.sqrt(2) * cubic.as_expr()) == 0 and cubic.is_irreducible and sp.discriminant(cubic.as_expr(), y) == -152,
      "discriminant %s" % sp.discriminant(cubic.as_expr(), y))
bad = law(TL, np.linalg.inv(TR))
check("planted: with R replaced by its inverse the law's hypothesis fails or its singular values are not U's cosines", not bad["agree"], bad)
json.dump({"rows": out, "checks": CHECKS, "failing": [c["check"] for c in CHECKS if not c["holds"]]}, open(HERE / "the_braid_law.json", "w"), indent=1)
print("\n%d checks, %d failing" % (len(CHECKS), sum(1 for c in CHECKS if not c["holds"])))
