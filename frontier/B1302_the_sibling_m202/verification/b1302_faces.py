"""B1302 Q4: the two-variable Alexander polynomial of m202 from the Fox derivatives of aabbAbAABBaB (a -> t1, b -> t2), its Newton polygon,
the 96 primitive specialisations (|p|,|q| <= 6) and divisibility by the golden polynomial t^2 - 3t + 1; the diagonal Delta(t, t).
sm:B1282 addendum: seven monomials, coefficients +-1; no specialisation divisible by t^2 - 3t + 1; Delta(t,t) = -(2t^2 + 3t + 2)."""
import sympy as sp, itertools, json, math
t1, t2, t = sp.symbols('t1 t2 t')
REL = "aabbAbAABBaB"
def fox(word, var):
    total = 0; prefix = 1
    for ch in word:
        g = ch.lower(); e = 1 if ch.islower() else -1; img = t1 if g == "a" else t2
        if g == var:
            total += prefix if e == 1 else -prefix * img**-1
        prefix *= img**e
    return sp.expand(sp.simplify(total))
dRa, dRb = fox(REL, "a"), fox(REL, "b")
# fundamental formula: dR/da = (t2 - 1) Delta, dR/db = -(t1 - 1) Delta  (up to a unit)
Da = sp.factor(sp.simplify(dRa / (t2 - 1))); Db = sp.factor(sp.simplify(-dRb / (t1 - 1)))
print("dR/da / (t2-1) =", Da); print("-dR/db / (t1-1) =", Db)
Delta = sp.expand(sp.simplify(Da)); ratio = sp.simplify(Da / Db); print("ratio of the two Deltas (a unit):", ratio)
poly = sp.Poly(sp.expand(Delta * t1**2 * t2**2), t1, t2)   # clear denominators to read monomials
terms = poly.terms(); print("Delta (times a unit) monomials:", len(terms), " coefficients:", sorted(set(int(c) for _, c in terms)))
gold = t**2 - 3 * t + 1
prims = [(p, q) for p in range(-6, 7) for q in range(-6, 7) if (p, q) != (0, 0) and math.gcd(abs(p), abs(q)) == 1]
# identify (p,q) ~ (-p,-q) (same specialisation up to t -> 1/t): count primitive classes
divisible = []; monic = 0; n = 0
seen = set()
for p, q in prims:
    if (-p, -q) in seen: continue
    seen.add((p, q)); n += 1
    spec = sp.expand(sp.simplify(Delta.subs({t1: t**p, t2: t**q}) * t**60))
    P = sp.Poly(sp.cancel(spec), t)
    # strip powers of t
    while P.degree() > 0 and P.eval(0) == 0: P = sp.Poly(sp.quo(P.as_expr(), t), t)
    if abs(P.LC()) == 1: monic += 1
    if sp.rem(P.as_expr(), gold, t) == 0: divisible.append((p, q))
print(f"primitive classes tested: {n}; monic (up to sign): {monic}; divisible by t^2 - 3t + 1: {divisible}")
diag = sp.factor(sp.expand(sp.simplify(Delta.subs({t1: t, t2: t}) * t**2)))
print("Delta(t, t) (times t^2):", diag, " roots:", [sp.nsimplify(r) for r in sp.Poly(diag, t).all_roots()] if sp.Poly(diag, t).degree() <= 2 else "")
ok = (len(terms) == 7 and set(abs(int(c)) for _, c in terms) == {1} and not divisible)
json.dump(dict(monomials=len(terms), coefficients=sorted(set(int(c) for _, c in terms)), classes=n, monic=monic, divisible=divisible, diag=str(diag)), open("b1302_faces.json", "w"))
print("Q4:", "PASS" if ok else "FAIL")
