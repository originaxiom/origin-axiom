#!/usr/bin/env python3
"""R55 -- the locking dictionary: what the object can still say once reality has chosen the bits.

Part A: the object's locking table, recomputed from the symmetry group (R54e) and B766's derived entries.
Part B: reality's bit space.  A world carries three discrete choices: h (which chirality the weak current
        couples), m (which of the two charge sectors is 'matter'), t (the arrow of time).  P flips h, C flips
        m, T flips t.  CPT is a theorem of local Lorentz-invariant QFT, so the world with all three flipped is
        the same physics: the PHYSICAL bit space is (Z/2)^3 / <CPT>, rank 2, coordinates x = h+m, y = m+t.
Part C: enumerate every dictionary (isomorphism) between the object's two manifold bits {c, gamma5} and
        reality's two physical bits, subject to the object's own axis semantics (c flips 'chirality-side' T4,
        gamma5 flips 'time-direction' T7), and print what each surviving dictionary PREDICTS.
No physical value is used; only the sign structure.  The measured facts live in DICTIONARY.md.
"""
import itertools, json, os, sys
import sympy as sp
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = {}
def say(*a): print(*a); sys.stdout.flush()

say("=" * 78); say("A. THE OBJECT'S LOCKING TABLE"); say("=" * 78)
# generators of the object's discrete closing lattice (B766): c = mirror (orientation reversal = complex
# conjugation on Q(sqrt-3), R54 §4), gamma5 = flow reversal A -> A^-1 (= eigenvalue inversion phi^2 -> phi^-2
# = the Q(sqrt5) Galois flip on eigenvalues, R54e: realised by an orientation-PRESERVING isometry), theta = the
# SL(2)/PSL(2) central lift sign (a symmetry of the representation, not of the manifold).
phi = (1 + sp.sqrt(5)) / 2
say("  c : orientation-reversing isometry; on traces = complex conjugation (R54 §4: 132 words realise it)")
say(f"  gamma5 : A -> A^-1 realised by [[-3,-2],[5,3]] (det +1, R54e); eigenvalues {sp.nsimplify(phi**2)} <-> {sp.nsimplify(phi**-2)};"
    f" (1-phi)^2 - phi^-2 = {sp.simplify((1-phi)**2 - phi**-2)} so this IS the sqrt5 Galois flip on eigenvalues")
say("  theta : the central sign of the SL(2,C) lift (Culler: two lifts, differing by the sign character)")
# axes and flip-vectors in the (c, theta, gamma5) basis.  Derived entries: T4 (c flips: conjugate character is
# a different point, R54 §4; gamma5 fixes: orientation-preserving; theta fixes: traces are lift-sign-blind only
# up to the sign character -- B766 records FIX), T7 (only gamma5 flips), T3 (Out(A5) = 5A/5B swap = gamma5, B701),
# T6 chord (c flips: value sqrt3*i purely odd -- B766 derived; theta flips: matrix-level, cc3's audit_compute).
axes = {
    'T4 chirality-side': (1, 0, 0),
    'T6 chord-sign':     (1, 1, 0),
    'T7 time-direction': (0, 0, 1),
    'T3 basepoint-bit':  (0, 0, 1),
}
prov = {'T4 chirality-side': 'c: R54 §4 (seat); theta, gamma5: B766 derived',
        'T6 chord-sign': 'c: B766 derived (chord value sqrt3 i); theta: B766 audit (matrix-level) -- NOT re-derived by the seat',
        'T7 time-direction': 'gamma5: seat (eigenvalue inversion, above); c, theta: B766 derived',
        'T3 basepoint-bit': 'B701/B766 identification Out(A5) = gamma5 -- NOT re-derived by the seat'}
for a, v in axes.items(): say(f"  {a:20s} flip-vector (c,theta,gamma5) = {v}   [{prov[a]}]")
say("  relations: T7 = T3 (same vector);  T6 = T4 (+) theta;  rank over F2 =",
    sp.Matrix([list(v) for v in axes.values()]).rank(iszerofunc=lambda z: z % 2 == 0))
OUT['A_axes'] = axes; OUT['A_provenance'] = prov

say(); say("=" * 78); say("B. REALITY'S BIT SPACE"); say("=" * 78)
# world bits (h, m, t); transformations P, C, T; CPT identifies (h,m,t) ~ (h+1,m+1,t+1)
worlds = list(itertools.product((0, 1), repeat=3))
P = lambda w: ((w[0] + 1) % 2, w[1], w[2]); C = lambda w: (w[0], (w[1] + 1) % 2, w[2]); T = lambda w: (w[0], w[1], (w[2] + 1) % 2)
CPT = lambda w: C(P(T(w)))
classes = {}
for w in worlds:
    k = min(w, CPT(w)); classes.setdefault(k, []).append(w)
say(f"  8 worlds (h,m,t); CPT identifies them in pairs -> {len(classes)} physical classes (rank 2).")
say("  CPT-invariant coordinates: x = h+m (handedness relative to the matter label), y = m+t (matter label relative to the arrow).")
say("  Physical transformations on (x,y): P: x->x+1;  C: x->x+1, y->y+1;  T: y->y+1;  CP: y->y+1;  PT: x->x+1, y->y+1 (= C);  CT: x->x+1 (= P).")
say("  So mod CPT there are exactly THREE nontrivial physical flips: {P ~ CT, C ~ PT, T ~ CP}.")
OUT['B_physical_flips_mod_CPT'] = {'P~CT': 'x', 'C~PT': 'x,y', 'T~CP': 'y'}

say(); say("=" * 78); say("C. EVERY DICTIONARY, ENUMERATED (proper parity bookkeeping)"); say("=" * 78)
# A measured, nonzero sign is CPT-even, so its parities (eP, eC, eT) satisfy eP*eC*eT = +1.  Four types:
TYPES = {'EVEN': (1, 1, 1), 'W (P-odd, C-odd, T-even: a handedness, e.g. the Wu asymmetry, neutrino helicity)': (-1, -1, 1),
         'K (P-even, C-odd, T-odd: a CP/T rate asymmetry, e.g. K_L charge asymmetry, baryon excess w.r.t. the arrow)': (1, -1, -1),
         'E (P-odd, C-even, T-odd: an EDM-type sign)': (-1, 1, -1)}
say("  types of measured sign (CPT-even): " + "; ".join(TYPES))
# a dictionary assigns the object's manifold bits c and gamma5 to two DISTINCT physical flips in {P, C, T}
# (mod CPT these are the only three).  An object axis with (c,gamma5)-parity (a,b) must be a type with
# parity a under c's flip and b under gamma5's flip.
idx = {'P': 0, 'C': 1, 'T': 2}
obj_axes = {'T4 chirality-side': (-1, 1), 'T6 chord-sign': (-1, 1), 'T7 time-direction': (1, -1), 'T3 basepoint-bit': (1, -1),
            '(no axis) (odd,odd)': (-1, -1)}
results = {}
for cflip, gflip in itertools.permutations('PCT', 2):
    table = {}
    for ax, (a, b) in obj_axes.items():
        fits = [name for name, e in TYPES.items() if e[idx[cflip]] == a and e[idx[gflip]] == b]
        table[ax] = fits
    # semantics: T4 must be a handedness (P-odd); T7 must be T-odd
    ok = any(TYPES[t][0] == -1 for t in table['T4 chirality-side']) and any(TYPES[t][2] == -1 for t in table['T7 time-direction'])
    results[(cflip, gflip)] = (ok, table)
    say(f"\n  dictionary c={cflip}, gamma5={gflip}: {'ADMISSIBLE' if ok else 'rejected by axis semantics'}")
    for ax, fits in table.items(): say(f"    {ax:26s} <- {fits[0].split(' (')[0] if fits else '-'}   {fits[0] if fits else ''}")
adm = [k for k, (ok, _) in results.items() if ok]
say(f"\n  admissible dictionaries: {adm}")
say("""
  READING:
   (c=P, gamma5=T): T4, T6 are W-type (handedness signs); T7=T3 are K-type (CP/T rate-asymmetry signs); no axis is E-type.
                    Both rows are populated by signs reality has ALREADY measured (Wu 1957 / Goldhaber 1958; K_L charge
                    asymmetry; baryon excess).  This is the testable dictionary.
   (c=C, gamma5=T): T4, T6 W-type; T7=T3 E-type (EDM signs) -- assigns the time/basepoint row to signs not yet measured.
   (c=P, gamma5=C): T4, T6 E-type; T7=T3 K-type -- assigns the chirality row to EDM-type signs; 'chirality-side' would not
                    be a weak handedness.  Admissible by parity, implausible by the axis's own meaning.
  CONTENT COMMON TO ALL THREE: the object has NO (odd,odd) axis.  Whatever type lands there (E-type under c=P,gamma5=T)
  is predicted NOT to be an independent closing bit: its sign must be the product of the two row bits.  Under (P,T):
  every EDM-type sign is determined by (handedness bit) x (CP bit) -- so the RELATIVE signs of different EDMs (electron,
  neutron, atomic) are predicted fixed.  In the SM they are (one CKM phase); in generic new physics they are independent.
  That is a falsifier that two measured EDMs would decide.
""")
OUT['C_admissible'] = [list(k) for k in adm]
OUT['C_tables'] = {f"c={k[0]},gamma5={k[1]}": {ax: [f.split(' (')[0] for f in v] for ax, v in t.items()} for k, (ok, t) in results.items() if ok}
json.dump(OUT, open(os.path.join(HERE, 'r55_results.json'), 'w'), indent=1, default=str)
say("r55_results.json written")
