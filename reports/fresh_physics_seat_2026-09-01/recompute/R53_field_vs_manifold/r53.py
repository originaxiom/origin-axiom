#!/usr/bin/env python3
"""R53 -- does the object select E6, or does the ROUTE only ever emit E6?

B8118 (structure-genesis head) attaches E6 to m004 by the chain
    shape field disc -> conductor N = |disc| -> SL(2, Z/N) -> (binary polyhedral?) -> McKay label
and shows E6 is a function of the FIELD (14 of the first 1200 census manifolds share it).

Fresh-eyes questions this cell answers by computation:
  Q1. Over ALL conductors, what can the route emit at all?  (For which N is SL(2,Z/N) a finite
      subgroup of SU(2)?)  If the answer is "only N=3 and N=5", then on hyperbolic manifolds
      (imaginary shape fields, disc<0, so N=5 is unreachable) the route has exactly ONE possible
      output, E6, and "m004 selects E6" means "m004's field is the one imaginary quadratic field
      for which the route emits anything".
  Q2. Census-wide label distribution for the first 1200 orientable cusped manifolds, and the
      shape-field degree distribution (how often the route even applies).
  Q3. The sister bit: m004 vs m003 are the SAME field, SAME volume, SAME E6, both amphichiral,
      and differ by the sign of the SL(2,Z) lift of the monodromy.  What sees that bit?
  Q4. Are the 14 field-sharers commensurable (volumes rational multiples of V_tet)?  m004's index
      in the Bianchi group PSL(2, O_{-3}) from the covolume formula.
"""
import json, os, sys, math
from fractions import Fraction
from itertools import product
import snappy
from snappy import pari

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = {}
def say(*a): print(*a); sys.stdout.flush()

def rat(x, maxden=64, tol=1e-9):
    f = Fraction(x).limit_denominator(maxden)
    return f if abs(float(f) - x) < tol else None

def quad_disc(z):
    """B8118's helper, verbatim in substance: squarefree discriminant of Q(z) if z is quadratic."""
    b, c = rat(-2 * z.real), rat(abs(z) ** 2)
    if b is None or c is None:
        return None
    d = b * b - 4 * c
    if d >= 0:
        return None
    n = d.numerator * d.denominator
    for s in range(2, 60):
        while n % (s * s) == 0:
            n //= s * s
    return n

def field_disc(n):
    """Field discriminant of Q(sqrt(n)), n squarefree: n if n = 1 mod 4 else 4n."""
    return n if n % 4 == 1 else 4 * n

# ----------------------------------------------------------------- Q1: what can the route emit?
def sl2(N):
    els = [(a, b, c, d) for a, b, c, d in product(range(N), repeat=4) if (a * d - b * c) % N == 1]
    return els
def mul(x, y, N):
    return ((x[0]*y[0]+x[1]*y[2]) % N, (x[0]*y[1]+x[1]*y[3]) % N,
            (x[2]*y[0]+x[3]*y[2]) % N, (x[2]*y[1]+x[3]*y[3]) % N)
def elt_order(g, N):
    I = (1, 0, 0, 1); h, k = g, 1
    while h != I:
        h = mul(h, g, N); k += 1
    return k

def su2_type(N):
    """Classify SL(2,Z/N) against the finite subgroups of SU(2): C_n, Dic_n (order 4n, has an
    element of order 2n), 2T (24), 2O (48), 2I (120) -- all with at most one involution.
    Returns (order, n_involutions, max_element_order, type_or_None, McKay_label_or_None)."""
    if N == 1:
        return 1, 0, 1, "cyclic", "A_0"
    G = sl2(N); order = len(G)
    ords = [elt_order(g, N) for g in G]
    inv = sum(1 for o in ords if o == 2)
    mo = max(ords)
    abelian = all(mul(g, h, N) == mul(h, g, N) for g in G[:40] for h in G[:40]) and order <= 6
    if inv > 1:
        return order, inv, mo, None, None
    if abelian:
        return order, inv, mo, "cyclic", f"A_{order-1}"
    if mo == order // 2:
        return order, inv, mo, f"Dic_{order//4}", f"D_{order//4+2}"
    if order == 24 and sorted(set(ords)) == [1, 2, 3, 4, 6]:
        return order, inv, mo, "2T", "E6"
    if order == 48 and sorted(set(ords)) == [1, 2, 3, 4, 6, 8]:
        return order, inv, mo, "2O", "E7"
    if order == 120 and sorted(set(ords)) == [1, 2, 3, 4, 5, 6, 10]:
        return order, inv, mo, "2I", "E8"
    return order, inv, mo, None, None

say("=" * 78); say("Q1 -- WHAT CAN THE ROUTE EMIT?  SL(2,Z/N) vs finite subgroups of SU(2)"); say("=" * 78)
route_table = {}
for N in range(1, 25):
    order, inv, mo, typ, label = su2_type(N)
    route_table[N] = dict(order=order, involutions=inv, max_elt_order=mo, su2_type=typ, mckay=label)
    say(f"  N={N:2d}  |SL(2,Z/N)|={order:6d}  involutions={inv:3d}  max elt order={mo:3d}  "
        f"-> {typ or '-':8s} {label or 'NO LABEL'}")
emitting = [N for N, r in route_table.items() if r['mckay']]
say(f"\n  conductors N<=24 for which the route emits ANY McKay label: {emitting}")
say("  N=1 is the trivial group (label A_0, no field); N=2 is S3 (three involutions).")
say("  => Over hyperbolic manifolds the shape field is non-real, disc<0, so |disc| in {3,4,7,8,11,...}.")
say("     The ONLY imaginary conductor the route can ever label is N=3 -> E6.  N=5 (E8) needs the")
say("     REAL field Q(sqrt5), which is never a shape field of a hyperbolic manifold.")
OUT['Q1_route_table'] = route_table
OUT['Q1_emitting_conductors_le_24'] = emitting

# --------------------------------------------------------- Q2: census-wide label distribution
say(); say("=" * 78); say("Q2 -- CENSUS SCAN (first 1200 orientable cusped): field degree and label"); say("=" * 78)
pari.set_real_precision(80)
def shape_degree(M, maxdeg=12):
    """Degree over Q of each tetrahedron shape: PARI lindep on [1, z, ..., z^k] at ~64 digits
    (SnapPy high_precision), accepted when the relation evaluates below 1e-30 with coefficients < 1e6."""
    try:
        sh = M.high_precision().tetrahedra_shapes('rect')
    except Exception:
        return None
    degs = []
    for z in sh:
        w = z.gen(); d = None
        for k in range(1, maxdeg + 1):
            v = pari.lindep([w ** i for i in range(k + 1)])
            if len(v) < k + 1:
                continue
            P = sum(int(v[i]) * pari('x') ** i for i in range(k + 1))
            if abs(complex(P.subst('x', w))) < 1e-30 and max(abs(int(c)) for c in v) < 10 ** 6:
                d = k; break
        degs.append(d)
    return degs

scan = []
count = 0
for M in snappy.OrientableCuspedCensus():
    count += 1
    if count > 1200:
        break
    try:
        sh = [complex(z) for z in M.tetrahedra_shapes('rect')]
    except Exception:
        scan.append(dict(name=M.name(), status='no shapes')); continue
    ds = {quad_disc(z) for z in sh}
    quad = (None not in ds and len(ds) == 1)
    n = next(iter(ds)) if quad else None
    N = abs(field_disc(n)) if quad else None
    label = route_table.get(N, {}).get('mckay') if N else None
    regular = all(abs(z - complex(0.5, 3 ** .5 / 2)) < 1e-9 for z in sh)
    scan.append(dict(name=M.name(), n_tet=len(sh), quad=quad, sqfree=n, conductor=N, mckay=label,
                     all_regular=regular, volume=float(M.volume())))
scanned = len(scan)
quads = [r for r in scan if r.get('quad')]
from collections import Counter
by_disc = Counter(r['sqfree'] for r in quads)
by_label = Counter((r['mckay'] or 'NO LABEL') for r in scan)
say(f"  scanned: {scanned}")
say(f"  quadratic shape field (all shapes in one quadratic field): {len(quads)}")
say(f"  by squarefree n of Q(sqrt n): {dict(sorted(by_disc.items()))}")
say(f"  label distribution over the 1200: {dict(by_label)}")
e6 = [r['name'] for r in scan if r.get('mckay') == 'E6']
say(f"  E6 carriers ({len(e6)}): {e6}")
OUT['Q2_scanned'] = scanned
OUT['Q2_n_quadratic'] = len(quads)
OUT['Q2_by_squarefree'] = {str(k): v for k, v in by_disc.items()}
OUT['Q2_label_distribution'] = dict(by_label)
OUT['Q2_E6_carriers'] = e6
b8118 = ["m003","m004","m202","m203","m206","m207","m208","m410","m412","s118","s119","s594","s595","s596"]
say(f"  matches B8118's 14: {sorted(e6) == sorted(b8118)}")
OUT['Q2_matches_B8118'] = sorted(e6) == sorted(b8118)

# degree distribution on a sample (first 300; algdep is slower)
degs = Counter()
for r in scan[:300]:
    try:
        M = snappy.Manifold(r['name'])
        d = shape_degree(M)
    except Exception:
        d = None
    key = 'unknown' if (d is None or None in d) else str(max(d))
    degs[key] += 1
say(f"  shape degree (max over tetrahedra), first 300: {dict(sorted(degs.items(), key=lambda kv: kv[0]))}")
OUT['Q2_shape_degree_first300'] = dict(degs)

# --------------------------------------------------------------- Q3: the sister bit
say(); say("=" * 78); say("Q3 -- THE SISTER BIT: m004 (b++RL) vs m003 (b+-RL)"); say("=" * 78)
A = [[2, 1], [1, 1]]  # RL monodromy, trace 3
def det2(m): return m[0][0]*m[1][1] - m[0][1]*m[1][0]
def addI(m, s): return [[m[0][0]+s, m[0][1]], [m[1][0], m[1][1]+s]]
sis = {}
for name, word in (("m004", "b++RL"), ("m003", "b+-RL")):
    M = snappy.Manifold(name); B = snappy.Manifold(word)
    iso = M.is_isometric_to(B)
    G = M.symmetry_group()
    sh = [complex(z) for z in M.tetrahedra_shapes('rect')]
    ds = {quad_disc(z) for z in sh}
    sis[name] = dict(bundle=word, isometric_to_bundle=bool(iso), homology=str(M.homology()),
                     volume=float(M.volume()), sym_order=G.order(), amphichiral=bool(G.is_amphicheiral()),
                     shape_disc=sorted(ds), n_tet=len(sh))
    say(f"  {name} = {word}: isometric={iso}  H1={M.homology()}  vol={float(M.volume()):.9f}  "
        f"|Sym|={G.order()}  amphichiral={G.is_amphicheiral()}  shape field disc {sorted(ds)}")
dm, dp = det2(addI(A, -1)), det2(addI(A, +1))
say(f"  det(A - I) = {dm}  (m004: H1 torsion = |{dm}| = 1)     det(A + I) = {dp}  (m003 = -A: torsion Z/{dp})")
phi = (1 + 5 ** .5) / 2
say(f"  identity: det(A-I) = (phi - 1/phi)^2 = {(phi-1/phi)**2:.12f},  det(A+I) = (phi + 1/phi)^2 = {(phi+1/phi)**2:.12f} = 5")
say("  => the sister's Z/5 is (sqrt5)^2 = disc Q(sqrt5): a Fibonacci identity of the monodromy, not a new input.")
# spin structures on T^2: quadratic refinements q on (Z/2)^2; action of A mod 2
A2 = [[0, 1], [1, 1]]
vecs = [(0, 1), (1, 0), (1, 1)]
def act(v): return ((A2[0][0]*v[0] + A2[0][1]*v[1]) % 2, (A2[1][0]*v[0] + A2[1][1]*v[1]) % 2)
# a quadratic form is determined by its values on the 3 nonzero vectors with q(x+y)=q(x)+q(y)+x.y;
# x.y = 1 for distinct nonzero vectors, so q(v3) = q(v1)+q(v2)+1
forms = []
for q1, q2 in product((0, 1), repeat=2):
    q = {vecs[0]: q1, vecs[1]: q2, vecs[2]: (q1 + q2 + 1) % 2}
    arf = 1 if sum(q.values()) == 3 else 0   # Arf = 1 iff q is 1 on all three nonzero vectors
    forms.append((q, arf))
def pull(q): return {v: q[act(v)] for v in vecs}
orbits = []
for q, arf in forms:
    img = pull(q)
    orbits.append((tuple(q[v] for v in vecs), arf, tuple(img[v] for v in vecs), img == q))
say("  spin structures on the fibre T^2 (values on (0,1),(1,0),(1,1); Arf; image under A; fixed?):")
for row in orbits: say(f"    {row}")
fixed = sum(1 for _, _, _, f in orbits if f)
say(f"  A mod 2 has order 3, fixes exactly the Arf-1 structure and cycles the three Arf-0 ones ({fixed} fixed).")
say("  -A == A mod 2, so the spin action is IDENTICAL for m004 and m003: the sister bit is invisible")
say("  to the field, the volume, the tetrahedra, amphichirality, and the spin-structure action.")
say("  It is seen by H1 (1 vs Z/5) and by the sign of the SL(2,Z) lift only.")
OUT['Q3'] = dict(sisters=sis, det_A_minus_I=dm, det_A_plus_I=dp, spin_fixed_count=fixed,
                 spin_action_identical_for_sisters=True)

# ------------------------------------------------- Q4: commensurability of the 14; Bianchi index
say(); say("=" * 78); say("Q4 -- THE 14 FIELD-SHARERS: volumes vs V_tet, and m004's index in PSL(2,O_-3)"); say("=" * 78)
Vtet = float(snappy.Manifold('m004').volume()) / 2
L2 = float(pari.lfun(pari.lfuncreate(-3), 2))
covol = 3 ** 1.5 * (math.pi ** 2 / 6) * L2 / (4 * math.pi ** 2)   # |d|^{3/2} zeta_K(2) / (4 pi^2)
say(f"  V_tet = {Vtet:.12f};  L(2,chi_-3) = {L2:.12f};  covol PSL(2,O_-3) = {covol:.12f} = V_tet/{Vtet/covol:.6f}")
ratios = {}
for r in scan:
    if r.get('mckay') == 'E6':
        q = rat(r['volume'] / covol, maxden=1, tol=1e-6)
        ratios[r['name']] = dict(volume=r['volume'], index_in_bianchi=(int(q) if q is not None else None),
                                 n_tet=r['n_tet'], all_regular=r['all_regular'])
        say(f"    {r['name']:6s} vol={r['volume']:.9f}  vol/covol={r['volume']/covol:.6f}  n_tet={r['n_tet']}  regular={r['all_regular']}")
say(f"  m004 index in PSL(2,O_-3): {ratios['m004']['index_in_bianchi']}")
say("  => every carrier is a finite-index subgroup of the SAME Bianchi group; the route lands on the")
say("     group PSL(2,O_-3), and choosing m004 among its finite-index subgroups is a separate, unpriced choice.")
OUT['Q4'] = dict(V_tet=Vtet, L2_chi_minus3=L2, bianchi_covolume=covol, carriers=ratios)

with open(os.path.join(HERE, 'r53_results.json'), 'w') as fh:
    json.dump(OUT, fh, indent=1, sort_keys=True, default=str)
say("\nr53_results.json written")
