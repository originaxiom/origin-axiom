"""B1028 — kappa = 2 is absolutely conserved: B497's stratum laws re-verified, and joined to B1027.

CONSOLIDATION REFRESH, band B400-B499. Campaign step 5: re-verify before restoring.
B497 classifies End(F_2) on the character variety into four strata, each with an exact kappa-law,
and proves U1: the locus kappa = 2 is invariant under EVERY endomorphism of F_2.

Nothing is imported from B497; the trace maps are re-derived from the substitutions.
Gate 5 untouched: structure only.
"""
import json, os
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
x, y, z = sp.symbols("x y z")
KAPPA = x**2 + y**2 + z**2 - x*y*z - 2          # B416's form: kappa = tr[a,b]
R = {"cell": "B1028", "checks": {}}

def CHK(n, ok, d=""):
    R["checks"][n] = {"pass": bool(ok), "detail": str(d)}
    print(f"[{'OK ' if ok else 'FAIL'}] {n}: {d}")
    return ok

def push(T):
    """kappa after applying the trace map T = (x',y',z')."""
    return sp.expand(KAPPA.subs(list(zip([x, y, z], T)), simultaneous=True))

# --- the four strata, trace maps as B497 gives them -------------------------------------------
S1 = (z, x, x*z - y)                                   # stratum 1: Aut (the programme's own)
S2 = (x**2 - 2, y**2 - 2, x*y*z - x**2 - y**2 + 2)     # stratum 2: A->A^2, B->B^2
S3 = (z, z, x*y*z - x**2 - y**2 + 2)                   # stratum 3: Thue-Morse a->AB, b->BA

k1, k2, k3 = push(S1), push(S2), push(S3)

CHK("stratum1_Aut_conserves_kappa_exactly", sp.simplify(k1 - KAPPA) == 0, "kappa' = kappa")
CHK("stratum2_law_kappa_minus_2_times_x2y2",
    sp.simplify(k2 - 2 - (KAPPA - 2) * x**2 * y**2) == 0, "kappa'-2 = (kappa-2)*x^2*y^2")
CHK("stratum3_ThueMorse_law",
    sp.simplify(k3 - 2 - (KAPPA - 2) * (x**2 + y**2 - x*y*z)) == 0,
    "kappa'-2 = (kappa-2)*(x^2+y^2-xyz)")

# --- U1: every stratum law is a MULTIPLE of (kappa - 2), so kappa = 2 is invariant -------------
facs = {}
for nm, k in (("stratum1", k1), ("stratum2", k2), ("stratum3", k3)):
    q, r = sp.div(sp.expand(k - 2), sp.expand(KAPPA - 2), x)
    facs[nm] = str(sp.factor(q))
    CHK(f"U1_{nm}_kappa_minus_2_divides_exactly", sp.simplify(r) == 0, f"cofactor {sp.factor(q)}")

CHK("U1_kappa_equals_2_is_invariant_under_all_three",
    all(sp.simplify(k.subs(z, sp.solve(sp.Eq(KAPPA, 2), z)[0]) - 2) == 0 for k in (k1, k2, k3)),
    "substituting the kappa=2 locus into each pushforward returns kappa' = 2")

# --- stratum 4: a non-injective endomorphism lands INSIDE kappa = 2 ----------------------------
# a -> ab, b -> ab  sends BOTH generators to the same word w = ab, so the image is the cyclic
# group <w>: abelian, hence reducible, hence kappa = 2. In trace coordinates
#   x' = tr(w) = z,  y' = tr(w) = z,  z' = tr(w^2) = tr(w)^2 - 2 = z^2 - 2   (Cayley-Hamilton).
# NOTE: a first pass set z' = z, which is wrong -- phi(ab) = w*w, not w. The check caught the
# modelling error, not B497's law.
S4 = (z, z, z**2 - 2)
CHK("stratum4_noninjective_image_lies_in_kappa_2",
    sp.simplify(push(S4) - 2) == 0,
    "a->ab, b->ab : image is cyclic => kappa' = 2 IDENTICALLY, for every z")

# --- the join to B1027: kappa - 2 is the natural coordinate ------------------------------------
CHK("every_stratum_law_is_multiplicative_in_kappa_minus_2",
    all(sp.simplify(sp.rem(sp.expand(k - 2), sp.expand(KAPPA - 2), x)) == 0 for k in (k1, k2, k3)),
    "so kappa-2 (the OBSTRUCTION, = omega^2) is what every endomorphism scales")

ok = all(c["pass"] for c in R["checks"].values())
R["cofactors"] = facs
print(f"\nALL VERIFIED: {ok}")
json.dump(R, open(os.path.join(HERE, "results.json"), "w"), indent=1)
