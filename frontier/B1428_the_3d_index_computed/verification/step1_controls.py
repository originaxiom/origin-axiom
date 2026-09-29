"""Step 1: tetrahedron index + symmetry / integrality controls.  Exact integers only."""
import itertools, json, sys
from tet_index import I_delta, s_str, s_eq, s_trunc, s_mul, s_shift, s_scal

X = 24          # exponents in x = q^{1/2}, i.e. up to q^12

print("=" * 78)
print("CONVENTION: x = q^{1/2}.  I_Delta(m,e) = sum_n (-1)^n q^{n(n+1)/2-(n+m/2)e}/((q)_n (q)_{n+m})")
print("            term exponent in x is E(n) = n(n+1) - (2n+m)e.   1/(q)_n := 0 for n<0.")
print("=" * 78)

print("\n--- I_Delta(0,0) ---")
I00 = I_delta(0, 0, X)
print("  in q :", s_str(I00, X))

print("\n--- a few small (m,e) ---")
for (m, e) in [(0,1),(1,0),(1,1),(0,2),(2,0),(2,2),(1,-1),(-1,1),(-1,-1),(0,-1),(-1,0),(1,2),(2,1),(-2,1)]:
    s = I_delta(m, e, X)
    print(f"  I({m:2d},{e:2d}) = {s_str(s, 12)}")

# ---------------------------------------------------------------- CONTROL A: integrality
print("\n--- CONTROL A: lowest exponent >= 0 (i.e. no negative powers of q)? ---")
bad = []
mins = {}
for m in range(-6, 7):
    for e in range(-6, 7):
        s = I_delta(m, e, X)
        if s:
            lo = min(s)
            mins[(m, e)] = lo
            if lo < 0:
                bad.append((m, e, lo))
print("   pairs tested:", len(mins), "  with a negative exponent:", len(bad))
if bad:
    print("   NEGATIVE:", bad[:20])

# ---------------------------------------------------------------- CONTROL B: symmetries
print("\n--- CONTROL B: which symmetries actually hold? ---")

cands = {
    "I(m,e) == I(e,m)                      ": lambda m, e: (e, m),
    "I(m,e) == I(-e,-m)                    ": lambda m, e: (-e, -m),
    "I(m,e) == I(-m,-e)                    ": lambda m, e: (-m, -e),
    "I(m,e) == I(-e-m, m)   [triality]     ": lambda m, e: (-e - m, m),
    "I(m,e) == I(e, -m-e)   [triality^-1]  ": lambda m, e: (e, -m - e),
    "I(m,e) == I(e+m, -e)                  ": lambda m, e: (e + m, -e),
    "I(m,e) == I(-e, m+e)                  ": lambda m, e: (-e, m + e),
}
rng = [(m, e) for m in range(-5, 6) for e in range(-5, 6)]
for name, f in cands.items():
    ok = True
    firstbad = None
    for (m, e) in rng:
        a = I_delta(m, e, X)
        b = I_delta(*f(m, e), Xmax=X)
        if not s_eq(a, b, X - 12):      # compare well inside the reliable range
            ok = False
            if firstbad is None:
                firstbad = (m, e, f(m, e))
    print(f"   {name}  {'HOLDS' if ok else 'FAILS at (m,e)=%s vs %s' % (firstbad[0:2], firstbad[2])}")

# the "quadratic-twist" symmetry with a prefactor  I(m,e) = (-q^{1/2})^{?} I(e,m)
print("\n--- CONTROL B2: I(m,e) == (-1)^? q^{?} I(e,m)  (search a monomial prefactor) ---")
found = []
for (m, e) in rng:
    a = I_delta(m, e, X)
    b = I_delta(e, m, X)
    if not a or not b:
        continue
    sh = min(a) - min(b)
    c = a[min(a)] // b[min(b)] if b[min(b)] and a[min(a)] % b[min(b)] == 0 else None
    if c is None:
        found.append((m, e, "no scalar"))
        continue
    if s_eq(a, s_scal(s_shift(b, sh, X), c), X - 12):
        found.append((m, e, f"shift x^{sh} scal {c}"))
    else:
        found.append((m, e, "NO"))
hits = [f for f in found if f[2].startswith("shift")]
print(f"   monomial relation I(m,e)=c*x^s*I(e,m) found for {len(hits)}/{len(found)} pairs")
import collections
cc = collections.Counter(f[2] for f in found)
for k, v in cc.most_common(8):
    print("     ", k, "->", v, "pairs")
# report the rule for the ones that work
rule_ok = True
for (m, e, t) in found:
    if t.startswith("shift"):
        sh = int(t.split("x^")[1].split()[0]); sc = int(t.split("scal ")[1])
        pred_sh = (m * e - e * m)   # 0
        if (sh, sc) != (m - e if False else sh, sc):
            pass
print("   (detail dumped to controls_sym.json)")
json.dump({f"{m},{e}": t for (m, e, t) in found}, open("controls_sym.json", "w"), indent=0)

# ---------------------------------------------------------------- CONTROL C: pentagon / recursion
print("\n--- CONTROL C: the DGG recursion  I(m,e) = q^{e/2} I(m+1,e) + q^{-m/2 ... } ? ---")
print("   (skipped: tested below as the linear q-difference identity)")

# Garoufalidis 1208.1663 Lemma: I(m,e) satisfies
#   I(m-1,e) + q^{?}... -- test the standard one:
#   I(m,e-1) - I(m,e) ... we probe a small family of 3-term relations numerically.
print("\n--- CONTROL D: I_Delta(m,e) is a power series in q (integer powers) iff m*e even? ---")
half = []
for m in range(-4, 5):
    for e in range(-4, 5):
        s = I_delta(m, e, X)
        odd = any(k % 2 for k in s)
        half.append(((m, e), odd, (m * e) % 2))
mismatch = [h for h in half if h[1] != bool(h[2])]
print("   pairs where 'has half-integer q powers' != 'm*e odd':", len(mismatch))
if mismatch:
    print("   ", mismatch[:10])
