"""B1343 -- HOW TO DERIVE THE OTHER ADE FACES, AND WHETHER THEY CAN ENRICH.

THE QUESTION (owner): "if our program is derived from the substitution rule, how can we derive the
rest of the faces so we see if our principles emerge or enrich?"

THE CHAIN IS: substitution phi -> abelianisation in GL2(Z) -> trace map -> kappa = tr[a,b] ->
Q(sqrt-3) -> 2T -> E6 by McKay. So EVERY other ADE face is a standard functor F applied to the SAME
2T (or to the same Dynkin datum). Deriving them therefore needs nothing new -- which is exactly
B727's fence: the faces are one classification, so none adds evidential weight for E6.

So "can we derive them" is the wrong question; they are all reachable. The right question is the
owner's second half -- ENRICH -- and B1258 turns it into a theorem:

    B1258 (NEGATIVE): "2T is too small: its eigenvalues are 12TH ROOTS OF UNITY and the two
    decompositions are congruent modulo exactly that."

=> THE BLINDNESS INHERITANCE. Any face that is a functor of 2T ALONE inherits 2T's blindness. It can
   decorate the programme with a new home; it cannot decide anything 2T cannot decide.
   Enrichment can come ONLY from data the substitution supplies BEYOND 2T.

WHAT THE SUBSTITUTION SUPPLIES BEYOND 2T (all banked): the specific leaf kappa = -2 (B1248, = the
Markov surface, B448); the golden characteristic polynomial lambda^2-lambda-1 (B1341); the
orientation bit det = -1 (the genesis swap, B448/B1341); the specific monodromy LR; and the stratum
(B1342: stratum 1 of 4). A face enriches iff it CONSUMES one of these.

TESTED HERE, on the face the forwarded survey ranked highest and which genuinely returns zero in the
corpus -- the ELLIPTIC-FIBRATION face (Kodaira IV* = E6-tilde, the Minahan-Nemeschansky home).

PRE-REGISTERED (DESIGN B1343): Q1 every Kodaira fibre monodromy is quasi-unipotent, |trace| <= 2,
verified by enumerating the classification; Q2 the object's monodromy LR has trace 3, hence is
HYPERBOLIC, hence is NOT conjugate to any Kodaira fibre monodromy -- a NO-GO for the obvious bridge;
Q3 no power of it escapes (powers of a hyperbolic element are hyperbolic), so the no-go is not a
parametrisation artefact; Q4 the IV* monodromy has order 3 and its eigenvalue field is Q(zeta_3) =
Q(sqrt-3) = the object's OWN forced 'being' face (B730) -- so the correct place to look is the FIELD,
not the dynamics; Q5 the near-miss is adjudicated: the HALF step has trace 1, matching Kodaira II*,
but det -1 against II*'s +1, so they are not conjugate and the coincidence is only the trace.
PASS iff all five hold.
"""
import json
import sympy as sp

fails = []
def check(tag, label, ok):
    print(f"   [{'PASS' if ok else 'FAIL'}] {tag}: {label}")
    if not ok: fails.append(tag)

M = lambda *e: sp.Matrix([[e[0], e[1]], [e[2], e[3]]])
# Kodaira's classification of singular fibres, with the standard local monodromy representatives.
# The affine Dynkin type each carries is the second column -- IV* is E6-tilde, which is why this
# face is the one the programme would want.
n = sp.symbols('n', positive=True, integer=True)
KODAIRA = [
    ("I_n  (n>=1)", "A_{n-1}~", M(1, 1, 0, 1), "parabolic"),      # T^n; trace 2 for every n
    ("I_0* ",       "D_4~",     M(-1, 0, 0, -1), "elliptic"),
    ("I_n* (n>=1)", "D_{n+4}~", M(-1, -1, 0, -1), "parabolic"),
    ("II   ",       "A_0~",     M(1, 1, -1, 0), "elliptic"),
    ("III  ",       "A_1~",     M(0, 1, -1, 0), "elliptic"),
    ("IV   ",       "A_2~",     M(0, 1, -1, -1), "elliptic"),
    ("IV*  ",       "E6~",      M(-1, -1, 1, 0), "elliptic"),
    ("III* ",       "E7~",      M(0, -1, 1, 0), "elliptic"),
    ("II*  ",       "E8~",      M(0, -1, 1, 1), "elliptic"),
]
print("Q1 -- Kodaira's fibre monodromies: every one is quasi-unipotent (|trace| <= 2)")
ok1 = True
for name, dynkin, A, kind in KODAIRA:
    tr, dt = A.trace(), A.det()
    order = None
    P = sp.eye(2)
    for k in range(1, 13):
        P = P * A
        if P == sp.eye(2): order = k; break
    print(f"      {name} = {dynkin:9s} {A.tolist()}  trace {str(tr):>3}  det {dt}  order {order}")
    ok1 &= (abs(tr) <= 2 and dt == 1)
check("Q1", "every Kodaira fibre monodromy has det +1 and |trace| <= 2 -- the monodromy theorem, "
            "which in SL2(Z) means elliptic (finite order) or parabolic, never hyperbolic", ok1)

print("\nQ2 -- the object's monodromy")
L, R, P_ = M(1, 1, 0, 1), M(1, 0, 1, 1), M(0, 1, 1, 0)
MONO = L * R                       # the figure-eight monodromy (B448: T1^2 = L.R, verified)
HALF = L * P_                      # the half step / genesis morphism (B448's C, det -1)
print(f"      monodromy  L.R  = {MONO.tolist()}  trace {MONO.trace()}  det {MONO.det()}")
print(f"      half step  L.P  = {HALF.tolist()}  trace {HALF.trace()}  det {HALF.det()}")
conj = [name for name, d, A, k in KODAIRA if A.trace() == MONO.trace() and A.det() == MONO.det()]
check("Q2", f"the monodromy has trace {MONO.trace()} > 2, hence is HYPERBOLIC (Anosov), hence "
            f"matches NO Kodaira fibre monodromy (candidates found: {conj or 'none'}) -- the obvious "
            f"bridge 'the object's monodromy IS a degeneration' is CLOSED BY A THEOREM",
      abs(MONO.trace()) > 2 and not conj)

print("\nQ3 -- can a power escape? (a parametrisation check, so the no-go is not an artefact)")
traces = []
Pw = sp.eye(2)
for k in range(1, 9):
    Pw = Pw * MONO; traces.append((k, Pw.trace()))
print(f"      traces of L.R^k: {traces}")
check("Q3", "every power of the monodromy is hyperbolic too (|trace| grows), so no iterate is "
            "quasi-unipotent and the no-go survives reparametrisation",
      all(abs(t) > 2 for k, t in traces))

print("\nQ4 -- where the IV* fibre DOES meet the object: the field")
IVstar = M(-1, -1, 1, 0)
lam = sp.symbols('lam')
cp = sp.factor(IVstar.charpoly(lam).as_expr())
roots = sp.roots(IVstar.charpoly(lam).as_expr(), lam)
print(f"      IV* monodromy char poly {cp}, roots {list(roots)}  (primitive cube roots of unity)")
print(f"      its eigenvalue field is Q(zeta_3) = Q(sqrt-3)")
check("Q4", "the IV* (= E6~) fibre monodromy has ORDER 3 and eigenvalue field Q(sqrt-3) -- which is "
            "EXACTLY the object's own forced 'being' face (B730, closed at three). So if the "
            "elliptic face is reachable at all it is through the FIELD and the LATTICE, not through "
            "the dynamics",
      sp.simplify(cp - (lam ** 2 + lam + 1)) == 0)

print("\nQ5 -- the near-miss, adjudicated rather than admired")
same_tr = [name for name, d, A, k in KODAIRA if A.trace() == HALF.trace()]
print(f"      the HALF step has trace {HALF.trace()}; Kodaira types with that trace: {same_tr}")
print(f"      but det(half) = {HALF.det()} and every Kodaira monodromy has det +1")
check("Q5", "the half step's trace 1 coincides with Kodaira II* (= E8~), but its determinant is -1 "
            "against II*'s +1, so they are NOT conjugate -- the coincidence is the trace alone, and "
            "it points at E8 rather than E6 in any case. Recorded as a near-miss KILLED, not as a hint",
      HALF.det() == -1 and all(A.det() == 1 for _, _, A, _ in KODAIRA) and "II*  " in [s for s in same_tr])

print("\nREAD-OUT -- the derivation map")
print("  Every ADE face is F(2T). B1258 proved 2T's characters see only n mod 12, so:")
print("    ANY FACE THAT IS A FUNCTOR OF 2T ALONE INHERITS 2T'S BLINDNESS.")
print("  It can supply a HOME (a 4-manifold, a chi != 0, an SCFT); it cannot DECIDE anything.")
print("  Enrichment requires a face that consumes data the substitution supplies BEYOND 2T:")
print("    kappa = -2 (the leaf / Markov surface) | the golden lam^2-lam-1 | det = -1 (orientation)")
print("    | the specific monodromy L.R | the stratum (1 of 4).")
print("  ELLIPTIC FACE: needs 2T + a Weierstrass model. The monodromy bridge is CLOSED (Q2/Q3).")
print("    What is left is the lattice E6 < NS(S), which is F(2T) -- so DERIVABLE, NOT ENRICHING.")
print("  ALE/KRONHEIMER: Kronheimer's theorem makes ALE spaces <-> (Gamma, zeta in R^3 (x) h).")
print("    2T fixes the diffeomorphism type; the DEFORMATION PARAMETER zeta is the only free datum,")
print("    so zeta is the ONLY place this face could be enriched. That is a well-posed question.")
print("  MINAHAN-NEMESCHANSKY: the Coulomb dimension and central charges follow from the IV* fibre,")
print("    hence from E6, hence F(2T). Its free data are the E6 mass parameters -- the same Cartan")
print("    the record already cannot fix (JOIN 2, 0/19). No new leverage.")

json.dump({"kodaira": {nm: [str(A.trace()), str(A.det())] for nm, d, A, k in KODAIRA},
           "monodromy_trace": str(MONO.trace()), "half_trace": str(HALF.trace()),
           "half_det": str(HALF.det()), "fails": fails},
          open("b1343_faces.json", "w"), indent=1)
print("\nB1343:", "PASS" if not fails else f"FAIL ({len(fails)}): {fails}")
raise SystemExit(0 if not fails else 1)
