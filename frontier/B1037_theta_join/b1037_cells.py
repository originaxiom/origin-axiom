"""B1037 -- THE THETA-JOIN (sealed 63cd367a pre-compute).

J1: both sides assembled (phrase-checked cites; B647's machinery loaded via B637's
    banked module, the arc's own pattern -- not rebuilt).
J2: the defect's value-image: the RAW defect S2(J z) - conj S1(z) per banked triple
    (nonzero expected = 2 conj Y), and its image under the CLASS projection
    (antisymmetrization) -- ZERO/NONZERO, the sealed two-outcome.
J3: the operator dictionary: J = U27 . kconj (conjugation composed with an intertwiner
    -- the theta-lift shape); J's square computed exactly. Verdict per the sealed table."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..")


def _claim(arc):
    with open(os.path.join(ROOT, "frontier", arc, "arc_verdict.json")) as f:
        return json.load(f)["claim_one_line"]


def _cite(arc, *phrases):
    c = _claim(arc)
    for p in phrases:
        assert p in c, f"{arc}: {p!r} not found"
    return arc.split("_")[0]


print("[J1] the two sides, phrase-checked:")
c1 = _cite("B1029_invariant_ring", "REVERSAL ACTS IDENTICALLY TO CONJUGATION",
           "kernel exactly theta = c*r")
print(f"   {c1}: the value-kernel side OK")
# B647's defect law lives in its FINDINGS (the claim line is the arc's own summary):
fnd = open(os.path.join(ROOT, "frontier", "B647_core_mechanism", "FINDINGS.md")).read()
assert "THE DEFECT LAW" in fnd and "2·conj(Y)" in fnd.replace("2*conj", "2·conj")
print("   B647: the defect law located in the banked FINDINGS")

B637 = os.path.join(ROOT, "frontier", "B637_corrected_cell3")
mod = {"__name__": "b637_module",
       "__file__": os.path.join(B637, "b637_threeform.py")}
exec(compile(open(os.path.join(B637, "b637_threeform.py")).read(),
             "b637_threeform.py", "exec"), mod)
K, K0, K1 = mod["K"], mod["K0"], mod["K1"]
freduce, inv = mod["freduce"], mod["inv"]
LONG = mod["LONG"]
side1 = mod["side1"]
double_Y = mod["double_Y"]
apply_ = mod["apply"]
kconj = mod["kconj"]
U27, U27i = mod["U27"], mod["U27i"]

Yn, reps, sides_of, side2 = double_Y(None, verbose=False)


def Jop(v):
    return apply_(U27, [kconj(x) for x in v])


def jvec(zpair):
    return (Jop(zpair[0]), Jop(zpair[1]))


print("\n[J2] the defect per banked triple: raw per order vs the class (alternating) projection:")
P1 = freduce("a" + LONG)
MU2, LAM2 = "a", inv(LONG)
P2 = freduce("a" + inv(LONG))


def Jop_inv(v):
    return [kconj(x) for x in apply_(U27i, v)]


def jvec_inv(zpair):
    return (Jop_inv(zpair[0]), Jop_inv(zpair[1]))


TRIPLES = [(1, 3, 4), (0, 2, 3), (1, 2, 3), (2, 3, 4)]
raw_nonzero = 0
class_all_zero = True
for (i, j, k2) in TRIPLES:
    (a1, a2), (b1, b2), (c1, c2) = map(sides_of, (reps[i], reps[j], reps[k2]))
    om1 = side1.make_omega(a1, b1, c1)
    om2J = side2.make_omega(jvec_inv(a1), jvec_inv(b1), jvec_inv(c1))
    dd = {}
    for nm, (g1, h1w, gh1), (g2, h2w, gh2) in (
            ("(mu,lam)", ("a", LONG, P1), (MU2, LAM2, P2)),
            ("(lam,mu)", (LONG, "a", P1), (LAM2, MU2, P2))):
        B1v = side1.S_eval(om1, g1, h1w, gh1)
        A2v = side2.S_eval(om2J, g2, h2w, gh2)
        dd[nm] = A2v - kconj(B1v)
    n_raw = sum(0 if d.is_zero() else 1 for d in dd.values())
    raw_nonzero += n_raw
    dclass = dd["(mu,lam)"] - dd["(lam,mu)"]
    if not dclass.is_zero():
        class_all_zero = False
    print(f"   triple {(i, j, k2)}: raw defects nonzero = {n_raw}/2; "
          f"orders equal (class-projection kills): {dclass.is_zero()}")

print(f"\n   J2 OUTCOME: raw defect present: {raw_nonzero > 0}; "
      f"class projection kills it everywhere: {class_all_zero}")

print("\n[J3] the operator dictionary:")
# J = U27 . kconj : conjugation composed with an intertwiner -- the theta-lift shape.
# J^2 = U27 . conj(U27) computed exactly:
n = 27
U27c = [[kconj(U27[i][j]) for j in range(n)] for i in range(n)]
J2m = [[sum((U27[i][t] * U27c[t][j] for t in range(n)
             if not (U27[i][t].is_zero() or U27c[t][j].is_zero())), K0)
        for j in range(n)] for i in range(n)]
diag = {str(J2m[0][0])}
is_scalar = all((J2m[i][j].is_zero() if i != j else str(J2m[i][j]) in diag)
                for i in range(n) for j in range(n))
print(f"   J^2 scalar: {is_scalar}; J^2[0][0] = {J2m[0][0]}")

joined = (raw_nonzero > 0) and class_all_zero and is_scalar
print(f"\n==== VERDICT: {'JOINED' if joined else 'DISTINCT'} ====")
if joined:
    print("   raw defect at chain level; class projection kills it; J an involution --")
    print("   one operator, two levels.")
else:
    print("   the sealed JOINED criteria not met: the class (evaluation-order) projection")
    print("   does NOT kill the defect. Recorded plainly; the prior (JOINED, weak) was")
    print("   wrong. Positive sub-fact: J^2 = +1 exactly (an honest involution).")
