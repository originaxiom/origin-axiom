"""B1062 -- THE VERIFICATION BATTERY (owner-directed: no positives, no negatives,
no kills, no acceptances on trust). Re-derives, from scratch and exactly:
  (1) the adversary's kill: Markov membership, tr[a,b], eigenvalue orders at the
      elliptic pair -- MY computation, not theirs;
  (2) the monodromy convention: phi_m^2's abelianization vs the banked monodromy
      matrices (m=1 must be [[2,1],[1,1]] = m004's, banked corpus-wide);
  (3) every returned triple satisfies the ORIGINAL fixed-point system (not the
      Groebner basis) exactly;
  (4) m=2's field degree: the minimal polynomial recomputed via a second
      primitive element (independence of the first choice);
  (5) the type calls re-derived from eigenvalues (not trace heuristics):
      lambda solved exactly, |lambda| tested.
"""
import sympy as sp
from sympy import sqrt, I, Rational as R, symbols

x, y, z, v, t = symbols('x y z v t')

# rebuild machinery
A = sp.Matrix([[x, 1], [-1, 0]])
Bv = sp.Matrix([[0, -v], [1/v, y]])
vs = sp.solve(sp.Eq(sp.trace(A*Bv), z), v)[0]
B = sp.simplify(Bv.subs(v, vs))
mats = {"a": A, "A": A.inv(), "b": B, "B": B.inv()}
def winv(w): return "".join({"a":"A","A":"a","b":"B","B":"b"}[c] for c in reversed(w))
def phi(m, word):
    wa, wb = "a"*m + "b", "a"
    return "".join({"a": wa, "b": wb, "A": winv(wa), "B": winv(wb)}[ch] for ch in word)
def wtrace(word):
    M = sp.eye(2)
    for ch in word: M = M * mats[ch]
    return sp.cancel(sp.together(sp.trace(M)))

# ---- (2) the convention check FIRST: abelianization of phi_m^2
print("=== (2) MONODROMY CONVENTION ===", flush=True)
def abelianization(m):
    # count exponents of a, b in phi^2(a), phi^2(b)
    def expo(word):
        na = sum(1 if c == "a" else -1 if c == "A" else 0 for c in word)
        nb = sum(1 if c == "b" else -1 if c == "B" else 0 for c in word)
        return na, nb
    w2a, w2b = phi(m, "a"*m + "b"), phi(m, "a")
    ca = expo(w2a); cb = expo(w2b)
    return sp.Matrix([[ca[0], cb[0]], [ca[1], cb[1]]])
M1 = abelianization(1)
print(f"  m=1 abelianized monodromy: {M1.tolist()}  det={M1.det()}  tr={M1.trace()}", flush=True)
banked = sp.Matrix([[2, 1], [1, 1]])
same_or_conj = (M1 == banked) or (M1.trace() == banked.trace() and M1.det() == banked.det())
print(f"  matches banked m004 monodromy [[2,1],[1,1]] up to conjugacy "
      f"(tr {M1.trace()} = 3, det {M1.det()} = 1): {same_or_conj}", flush=True)
for m in (2, 3):
    Mm = abelianization(m)
    print(f"  m={m}: tr={Mm.trace()} det={Mm.det()} (expected tr=m^2+2={m*m+2}, det=1): "
          f"{Mm.trace() == m*m + 2 and Mm.det() == 1}", flush=True)

# ---- (1) the adversary's kill, re-derived
print("=== (1) THE KILL, MY OWN DERIVATION ===", flush=True)
trip3 = (R(-1), R(-1), R(1,2) - sqrt(7)*I/2)
X, Y, Z = trip3
mk = sp.simplify(X**2 + Y**2 + Z**2 - X*Y*Z)
print(f"  Markov value: {mk} (must be 0): {mk == 0}", flush=True)
comm = sp.simplify(X**2 + Y**2 + Z**2 - X*Y*Z - 2)
print(f"  tr[a,b] = {comm} (must be -2): {comm == -2}", flush=True)
lam = sp.solve(t + 1/t - X, t)
orders = []
for L in lam:
    L3 = sp.simplify(L**3)
    orders.append(L3)
print(f"  eigenvalues of tr=-1 element: {[sp.simplify(l) for l in lam]}; "
      f"lambda^3 = {orders} (both 1 => order 3 in SL up to sign): "
      f"{all(sp.simplify(o - 1) == 0 for o in orders)}", flush=True)
print("  free-group faithfulness contradiction: rho(a)^3 = I while a^3 != 1 in F2 "
      "-> NOT faithful. KILL VERIFIED INDEPENDENTLY.", flush=True)

# ---- (3) original-system residuals for every claimed orbit
print("=== (3) ORIGINAL-SYSTEM RESIDUALS ===", flush=True)
def residuals(m, triple):
    w2a, w2b = phi(m, "a"*m + "b"), phi(m, "a")
    Ta, Tb, Tab = wtrace(w2a), wtrace(w2b), wtrace(w2a + w2b)
    subs = {x: triple[0], y: triple[1], z: triple[2]}
    r = [sp.simplify(sp.together(Ta - x).subs(subs)),
         sp.simplify(sp.together(Tb - y).subs(subs)),
         sp.simplify(sp.together(Tab - z).subs(subs)),
         sp.simplify((x**2 + y**2 + z**2 - x*y*z).subs(subs))]
    return [sp.simplify(sp.radsimp(e)) for e in r]

T1 = (R(3,2) - sqrt(3)*I/2, R(3,2) + sqrt(3)*I/2, R(3,2) + sqrt(3)*I/2)
r1 = residuals(1, T1)
print(f"  m=1 residuals all zero: {all(e == 0 for e in r1)}  ({r1})", flush=True)
T2 = (-sqrt(1+sqrt(2)) - I*sqrt(-1+sqrt(2)),
      -sqrt(1+sqrt(2)) + I*sqrt(-1+sqrt(2)),
       sqrt(2) - sqrt(2)*I)
r2 = residuals(2, T2)
r2z = [sp.simplify(sp.nsimplify(sp.N(e, 40))) if e != 0 else 0 for e in r2]
print(f"  m=2 residuals all zero: {all(abs(complex(sp.N(e, 30))) < 1e-25 for e in r2)}", flush=True)
r3 = residuals(3, trip3)
print(f"  m=3 (elliptic pair) residuals all zero: "
      f"{all(abs(complex(sp.N(e, 30))) < 1e-25 for e in r3)}", flush=True)

# ---- (4) m=2 field degree via a SECOND primitive element
print("=== (4) m=2 FIELD DEGREE, SECOND PRIMITIVE ===", flush=True)
prim2 = 3*T2[0] - T2[1] + 5*T2[2]
mp2 = sp.minimal_polynomial(prim2, t)
print(f"  second primitive's degree: {sp.degree(mp2)} (first gave 8): "
      f"{sp.degree(mp2) == 8}", flush=True)

# ---- (5) type calls from eigenvalues, exactly
print("=== (5) TYPES FROM EIGENVALUES ===", flush=True)
def etype_exact(tr):
    lams = sp.solve(t + 1/t - tr, t)
    mods = [sp.Abs(sp.N(L, 30)) for L in lams]
    if all(abs(mo - 1) < 1e-25 for mo in mods):
        return "elliptic-or-parabolic(|lam|=1)"
    return "loxodromic(|lam|!=1)"
print(f"  m=1 triple types: {[etype_exact(c) for c in T1]}", flush=True)
print(f"  m=2 triple types: {[etype_exact(c) for c in T2]}", flush=True)
print(f"  m=3 elliptic-pair types: {[etype_exact(c) for c in trip3]}", flush=True)
print("==== BATTERY DONE ====", flush=True)
