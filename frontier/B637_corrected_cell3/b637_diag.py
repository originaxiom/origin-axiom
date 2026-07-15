"""B637 part 2b — diagnostics for the class-level gate failure."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
mod = {"__name__": "b637_module", "__file__": os.path.join(
    HERE, "b637_threeform.py")}
exec(compile(open(os.path.join(HERE, "b637_threeform.py")).read(),
             "b637_threeform.py", "exec"), mod)

K, K0, K1 = mod["K"], mod["K0"], mod["K1"]
freduce, inv = mod["freduce"], mod["inv"]
LONG = mod["LONG"]
side1 = mod["side1"]
double_Y = mod["double_Y"]

Yn, reps, sides_of, side2 = double_Y(None, verbose=False)
z0_1, z0_2 = sides_of(reps[0])
z1_1, z1_2 = sides_of(reps[1])
z2_1, z2_2 = sides_of(reps[2])

print("\n(D1) cocycle consistency across the identification:", flush=True)
for nm, (s1z, s2z) in (("rep0", (z0_1, z0_2)), ("rep1", (z1_1, z1_2))):
    va1 = side1.zval(s1z, "a")
    va2 = side2.zval(s2z, "a")
    okmu = all((va1[t] - va2[t]).is_zero() for t in range(27))
    vl1 = side1.zval(s1z, LONG)
    vl2 = side2.zval(s2z, inv(LONG))
    oklam = all((vl1[t] - vl2[t]).is_zero() for t in range(27))
    print(f"  {nm}: z(mu) side1==side2: {okmu};  z(lam) side1==side2(inv): "
          f"{oklam}", flush=True)

print("\n(D2) res omega equality on P-triples:", flush=True)
om1 = side1.make_omega(z0_1, z1_1, z2_1)
om2 = side2.make_omega(z0_2, z1_2, z2_2)
tests = [("a", LONG, "a"), (LONG, "a", LONG), ("a", "a", LONG)]
for (x, y, z) in tests:
    x2 = x.replace(LONG, "") or x            # crude map below instead
for (x, y, z) in tests:
    def m2(w):
        # P-words: replace lam-word by side-2 lam-word
        return w if w == "a" else (inv(LONG) if w == LONG else w)
    v1 = om1(x, y, z)
    v2 = om2(m2(x), m2(y), m2(z))
    print(f"  omega({x[:4]}..,{y[:4]}..,{z[:4]}..): side1==side2: "
          f"{(v1 - v2).is_zero()}", flush=True)

print("\n(D3) delta S = omega on PERIPHERAL side-1 cells:", flush=True)
S1 = lambda g, h, gh: side1.S_eval(om1, g, h, gh)
MU, LAM = "a", LONG
PROD = freduce("a" + LONG)
# consistent sections: sig(mu)=a, sig(lam)=LONG, sig(mulam)=PROD,
# products needed for [mu|lam|mu]: (lam,mu)->? sig(lammu)=PROD too (same elt)
LM = PROD
# triple [mu|lam|mu]: needs S(lam,mu,LM), S(mulam? ...)
# deltaS(g,h,k) = S(h,k) - S(gh,k) + S(g,hk) - S(g,h) with section words:
def dS(g, h, k, gh, hk, ghk):
    return (S1(h, k, hk) - S1(gh, k, ghk) + S1(g, hk, ghk) - S1(g, h, gh))
# [mu|lam|mu]: gh = mulam (PROD), hk = lammu (PROD), ghk = mu lam mu word
GHK = freduce("a" + LONG + "a")
lhs = dS(MU, LAM, MU, PROD, PROD, GHK)
rhs = om1(MU, LAM, MU)
print(f"  [mu|lam|mu]: {(lhs - rhs).is_zero()}", flush=True)
# [lam|mu|lam]
GHK2 = freduce(LONG + "a" + LONG)
lhs = dS(LAM, MU, LAM, PROD, PROD, GHK2)
rhs = om1(LAM, MU, LAM)
print(f"  [lam|mu|lam]: {(lhs - rhs).is_zero()}", flush=True)

print("\n(D4) is eta = S1 - S2 a P-cocycle? (trivial-coeff delta on P):",
      flush=True)
S2f = lambda g, h, gh: side2.S_eval(om2, g, h, gh)
MU2, LAM2 = "a", inv(LONG)
PROD2 = freduce("a" + inv(LONG))
def eta(pq):
    # pq in cell notation: ('mu','lam') etc.
    w1 = {"mu": MU, "lam": LAM, "mulam": PROD}
    w2 = {"mu": MU2, "lam": LAM2, "mulam": PROD2}
    g, h = pq
    gh = "mulam"
    return (S1(w1[g], w1[h], w1[gh]) - S2f(w2[g], w2[h], w2[gh]))
# delta eta on [mu|lam|mu] with trivial coefficients:
# eta(lam,mu-cell...) needs eta on (lam,mu) too: gh key same 'mulam'
e_ml = eta(("mu", "lam"))
e_lm = eta(("lam", "mu"))
print(f"  eta(mu,lam) = {e_ml}", flush=True)
print(f"  eta(lam,mu) = {e_lm}", flush=True)
print(f"  Y = eta(mu,lam) - eta(lam,mu) = {e_ml - e_lm}", flush=True)
print("B637 diagnostics DONE", flush=True)
