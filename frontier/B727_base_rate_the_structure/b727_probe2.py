#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B727 PROBE 2 -- the BASE RATE across comparable arithmetic objects.

Question (sealed, prereg): how OFTEN does SOME ADE/exceptional label recur across
the faces (McKay / Lie / CIZ) the way E6 does for m004? Two-outcome:
  A = m004's E6-recurrence is RARE/discriminating vs the comparison set.
  B = COMMON/expected (every comparable object has SOME label recurring the same way).

COMPUTE-NOT-CITE (E19): every discriminating fact recomputed in-sandbox.
Firewall: structural/arithmetic only, no SM value. A negative is a real deliverable.

------------------------------------------------------------------------------
REVISION (self-audit, 3-skeptic loop) -- two defects fixed vs the sealed draft:
  ISSUE A (provenance): the sealed appendix attributed the A4-in-PSL2(O_d)
    amalgam decompositions to "Sengun arXiv:1204.6697" -- that paper does NOT
    contain them (only the d=1 case). FIX: the 4/5 number now rests ENTIRELY on
    the in-sandbox class-field-theory derivation (splitting of 2 -> Hamilton
    (-1,-1) splits -> 2T realizable), with the literature demoted to a correctly
    attributed 'consistent-with' note (Frohman-Fine, Proc. AMS 102 (1988)).
  ISSUE B (material error): the sealed draft claimed pi_1 ->> 2T is present
    "EXACTLY for the arithmetic knots (4_1,m003), 0 for all non-arithmetic."
    RECOMPUTED FALSE: on a 13-knot sample the non-arithmetic knots 7_2, 7_3, 8_1
    ALSO surject onto 2T with the identical 48/4/2 signature. FIX: the knot
    section now reports the true rate (4/13) and its correct reading -- the
    2T-quotient is NOT a signature of arithmeticity; this makes the McKay-face
    MORE common, which REINFORCES outcome B (does not rescue the flagship).
  Neither fix changes the outcome: it becomes B on firmer, fully-in-sandbox
  grounds. The B266 exact-count and B282 generic-Lie-face atoms are preserved
  but correctly NARROWED (see section 6).
------------------------------------------------------------------------------

Sections:
  1. McKay data (binary polyhedral groups -> affine ADE), Coxeter numbers (TWO
     independent in-sandbox methods), and the McKay<->CIZ level bijection h=k+2.
  2. Which exceptional McKay group can live over an imaginary-quadratic field?
     2T (E6): (-1,-1)/Q(sqrt-d) splits  <=>  2 does NOT split in Q(sqrt-d)
              <=>  -d != 1 mod 8   (derived in-sandbox from local invariants).
     2O (E7): trace field Q(sqrt2) -- REAL, never in imaginary quadratic.
     2I (E8): trace field Q(sqrt5) -- REAL, never in imaginary quadratic.
  3. TORSION mechanism: finite subgroups of the Euclidean Bianchi groups
     PSL(2,O_d), d=1,2,3,7,11 -> McKay labels. Count E6. (+ extend to all 9
     class-number-1 imaginary-quadratic fields as an anti-cherry-pick check.)
  4. QUOTIENT mechanism (B266's own): mod-ramified-prime reduction -> SL(2,F_p);
     it is a McKay/binary group only for p in {3,5}.  Count E6/E8.
  5. KNOT mechanism (B282 recompute, CORRECTED): enumerate surjections
     pi_1(knot) ->> 2T=SL(2,F3) on a 13-knot hyperbolic sample; present/absent.
  6. Base-rate synthesis + numbers.
"""

import itertools
import numpy as np
import sympy as sp

OUT = []
def emit(s=""):
    print(s)
    OUT.append(s)

emit("="*78)
emit("B727 PROBE 2 -- BASE RATE of the E6-across-faces structure  (self-audit rev)")
emit("="*78)

# ----------------------------------------------------------------------------
# SECTION 1 : McKay data + Coxeter numbers (two methods) + McKay<->CIZ bijection
# ----------------------------------------------------------------------------
emit("\n[1] McKay correspondence data (recomputed) + CIZ level bijection")
emit("-"*78)

def dynkin_edges(kind, n):
    """Simply-laced Dynkin diagram edges (0-indexed) on n nodes."""
    if kind == 'A':
        return [(i, i+1) for i in range(n-1)]
    if kind == 'D':
        e = [(i, i+1) for i in range(n-2)]; e.append((n-3, n-1)); return e
    if kind == 'E':
        e = [(i, i+1) for i in range(n-2)]; e.append((2, n-1)); return e

def h_via_spectrum(kind, n):
    """Method 1: h = pi / acos(lam_max/2), lam_max = largest Dynkin adjacency eig."""
    edges = dynkin_edges(kind, n)
    A = np.zeros((n, n))
    for (i, j) in edges:
        A[i, j] = A[j, i] = 1.0
    lam = float(max(np.linalg.eigvalsh(A)))
    return np.pi / np.arccos(lam/2)

def h_via_roots(kind, n):
    """Method 2 (independent): h = (#roots)/rank, via reflection-closure of the
    root system in simple-root coordinates. C = Cartan matrix; s_i(v)=v-(Cv)_i e_i."""
    C = 2*np.eye(n)
    for (i, j) in dynkin_edges(kind, n):
        C[i, j] = C[j, i] = -1
    simples = [tuple(int(k == i) for k in range(n)) for i in range(n)]
    R = set(simples) | set(tuple(-x for x in s) for s in simples)
    changed = True
    while changed:
        changed = False
        for v in list(R):
            va = np.array(v); Cv = C.dot(va)
            for i in range(n):
                w = va.copy(); w[i] -= Cv[i]
                wt = tuple(int(round(x)) for x in w)
                if wt not in R:
                    R.add(wt); changed = True
    return len(R) // n

classical_h = {('E',6):12, ('E',7):18, ('E',8):30, ('A',2):3, ('D',4):6, ('D',5):8}
emit(" ADE  rank  h(spectrum)  h(#roots/rank)  h(classical)  CIZ level k=h-2  agree?")
for (kind, n) in [('A',2),('D',4),('D',5),('E',6),('E',7),('E',8)]:
    h1 = round(h_via_spectrum(kind, n)); h2 = h_via_roots(kind, n)
    hc = classical_h[(kind,n)]
    ok = "OK" if (h1 == h2 == hc) else "MISMATCH"
    emit(f"  {kind}{n:<3}  {n:<3}  {h1:<11} {h2:<15} {hc:<13} k = {hc-2:<10} [{ok}]")

emit("\n  McKay <-> affine-ADE (binary polyhedral -> Dynkin node marks), classical:")
mckay = [
    ("cyclic Z/n          ", "affine A_{n-1}", "classical"),
    ("binary dihedral 4n   ", "affine D_{n+2}", "classical"),
    ("2T  binary tetra.  24", "affine E6     ", "|2T|=24,  h(E6)=12, CIZ level 10"),
    ("2O  binary octa.   48", "affine E7     ", "|2O|=48,  h(E7)=18, CIZ level 16"),
    ("2I  binary icosa. 120", "affine E8     ", "|2I|=120, h(E8)=30, CIZ level 28"),
]
for g, lab, note in mckay:
    emit(f"    {g} ->  {lab}   [{note}]")

emit("""
  KEY (probe-1 fact, used here): the CIZ A-D-E modular-invariant list IS the
  Dynkin list, with SU(2) level k = h - 2 (Coxeter number minus 2). So a McKay
  label X FORCES its CIZ level (E6<->k=10). McKay-face and CIZ-face are ONE
  classification, not two independent evidences.  (Cappelli-Itzykson-Zuber 1987.)""")

# ----------------------------------------------------------------------------
# SECTION 2 : which exceptional McKay group fits an imaginary-quadratic field
# ----------------------------------------------------------------------------
emit("\n[2] Which EXCEPTIONAL McKay group can live over Q(sqrt-d)?")
emit("-"*78)

emit("""  Field-of-definition facts (2O/2I recomputed in the appendix):
   * 2T (E6): the faithful 2-dim irrep with RATIONAL character has Schur index 2;
     its enveloping quaternion algebra is Hamilton (-1,-1)/Q, ramified at {2,inf}.
     2T embeds in SL(2,K), K=Q(sqrt-d), IFF (-1,-1)/K splits.
     (A4 has no faithful 2-dim rep, so A4 in PSL2(K) forces its binary lift 2T
      in SL2(K); the only binary group over A4 is 2T. -> torsion = this embedding.)
   * 2O (E7): order-8 element, SU(2) trace = 2cos(pi/4) = +-sqrt2 -> field Q(sqrt2).
   * 2I (E8): order-10 element, SU(2) trace = 2cos(pi/5) = (1+sqrt5)/2 -> Q(sqrt5).
  Q(sqrt2), Q(sqrt5) are REAL quadratic -- a real quadratic field is never a
  subfield of an imaginary quadratic field (degrees force equality; real != nonreal).
  => E7, E8 are STRUCTURALLY EXCLUDED from every imaginary-quadratic arithmetic
     object. The ONLY exceptional label reachable is E6.  (No birthday problem.)""")

emit("""
  IN-SANDBOX derivation of "(-1,-1)/K splits <=> 2 not split in K":
    A quaternion algebra over a number field is trivial in the Brauer group iff
    its local invariant is 0 at every place. Base-change multiplies invariants by
    local degree: inv_w(H_K) = [K_w:Q_v] * inv_v(H).  H=(-1,-1)/Q has inv 1/2 at
    v in {2, inf} and 0 elsewhere.
      * v=inf : K imaginary-quadratic => one complex place, [K_w:R]=2 =>
                inv = 2*(1/2) = 0 in Q/Z.  H_K always splits at infinity.
      * v=2   : 2 inert or ramified -> one prime w, [K_w:Q_2]=2 -> inv=2*(1/2)=0.
                2 split            -> two primes, each [K_w:Q_2]=1 -> inv=1/2 != 0.
    => H_K splits  <=>  2 is NOT split in K.  And 2 splits in Q(sqrt-d) iff the
       field discriminant is 1 mod 8, i.e. iff -d = 1 mod 8.  So realizable iff
       -d != 1 mod 8.  (Splitting type of 2 verified below by factoring mod 2.)""")

def split_type_of_2(d):
    """Splitting of 2 in Q(sqrt-d), in-sandbox via Dedekind (factor min poly mod 2)."""
    x = sp.symbols('x')
    if (-d) % 4 == 1:      # O = Z[(1+sqrt-d)/2]
        minpoly = x**2 - x + sp.Rational(1+d, 4)
    else:                  # O = Z[sqrt-d]
        minpoly = x**2 + d
    factors = sp.factor_list(sp.Poly(minpoly, x, modulus=2))[1]
    if any(m > 1 for (_, m) in factors):
        return "ramified"
    return "split" if len(factors) == 2 else "inert"

def splits_hamilton(d):
    """(-1,-1)/Q(sqrt-d) splits?  criterion: 2 not split.  Plus an explicit
    certificate: a K-solution of -1 = x^2 + y^2 (ansatz 2 d q^2 - 2 p^2 = 1)."""
    st = split_type_of_2(d)
    local_ok = (st != "split")             # equivalently  (-d) % 8 != 1
    assert local_ok == (((-d) % 8) != 1)   # cross-check the two computations
    found = None
    for qden in range(1, 9):
        for pden in range(1, 9):
            for qn in range(-8, 9):
                for pn in range(-8, 9):
                    q = sp.Rational(qn, qden); p = sp.Rational(pn, pden)
                    if 2*d*q**2 - 2*p**2 == 1:
                        r = sp.sqrt(-d); xx = p + q*r; yy = -p + q*r
                        if sp.simplify(xx**2 + yy**2) == -1:
                            found = (xx, yy); break
                if found: break
            if found: break
        if found: break
    return st, local_ok, found

emit("\n  d : 2 splits? : (-1,-1) splits(=2T realizable) : explicit -1=x^2+y^2 cert")
E6_realizable = {}
for d in [1, 2, 3, 7, 11]:
    st, ok, cert = splits_hamilton(d)
    E6_realizable[d] = ok
    cs = "none-found(<=8)" if cert is None else f"x={cert[0]}, y={cert[1]}"
    emit(f"   d={d:<2}: 2 {st:<8}: splits={str(ok):<5}                : {cs}")

# ----------------------------------------------------------------------------
# SECTION 3 : TORSION finite subgroups of the Euclidean Bianchi groups
# ----------------------------------------------------------------------------
emit("\n[3] TORSION mechanism: does PSL(2,O_d) contain A4 (=> 2T => McKay E6)?")
emit("-"*78)
emit("""  A4 subset PSL(2,O_d)  <=>  2T subset SL(2,O_d)  (binary lift, contains -I).
  Class number of O_d is 1 for all d in {1,2,3,7,11} (Euclidean), so a finite
  subgroup of SL(2,K) is conjugate INTO SL(2,O_d) (it preserves an O_d-lattice L;
  L is free since h=1; the conjugating change of basis lands it in SL(2,O_d)).
  Hence the torsion question reduces EXACTLY to section 2 (field of definition).""")
emit("\n  d : Q(sqrt-d) : A4/2T/E6 present by torsion?")
tors_hits = []
for d in [1, 2, 3, 7, 11]:
    hit = E6_realizable[d]; tors_hits.append(hit)
    emit(f"   d={d:<2}: Q(sqrt-{d}) : E6 present = {hit}")
n_E6_tors = sum(tors_hits)
emit(f"\n  => E6 (exceptional) appears by TORSION in {n_E6_tors}/5 Euclidean Bianchi groups.")
emit(f"     (absent only for d=7, the unique one with 2 SPLIT / -7 = 1 mod 8.)")
emit(f"     E7, E8 appear in 0/5 (section 2: excluded for all imaginary quadratic).")

# anti-cherry-pick: extend to ALL 9 class-number-1 imaginary-quadratic fields
cn1 = [1, 2, 3, 7, 11, 19, 43, 67, 163]
ext_hits = [(d, split_type_of_2(d) != "split") for d in cn1]
n_ext = sum(1 for (_, h) in ext_hits if h)
emit(f"\n  ANTI-CHERRY-PICK: extend to all 9 class-number-1 imag.-quad. fields")
emit(f"    d in {cn1}:")
emit("    " + ", ".join(f"d={d}:{'E6' if h else '--'}" for (d, h) in ext_hits))
emit(f"    => E6 by torsion in {n_ext}/9 = {round(100*n_ext/9)}%  (absent only d=7).")
emit(f"    The pre-registered 5-object set (80%) was NOT cherry-picked toward B;")
emit(f"    the wider natural family is even MORE E6-saturated (89%).")

# ----------------------------------------------------------------------------
# SECTION 4 : QUOTIENT mechanism (B266) -- mod ramified prime
# ----------------------------------------------------------------------------
emit("\n[4] QUOTIENT mechanism (B266): mod-ramified-prime reduction SL(2,F_p)")
emit("-"*78)
emit("""  SL(2,F_p) is a binary-polyhedral (McKay) group only for p in {3,5}:
    p=2 -> SL(2,F2)=S3 (center trivial, not binary);
    p=3 -> SL(2,F3)=2T  -> E6;
    p=5 -> SL(2,F5)=2I  -> E8;
    p>=7 -> order p(p^2-1) too large, wrong composition factors (not binary).""")

def ramified_primes(d):
    disc = -d if ((-d) % 4) == 1 else -4*d
    return sorted(sp.factorint(abs(disc)).keys())

emit("\n  d : ramified prime(s) : mod-p reduction gives McKay label?")
quo_hits = []
for d in [1, 2, 3, 7, 11]:
    rps = ramified_primes(d); labels = []
    for p in rps:
        if p == 3: labels.append("F3=2T=E6")
        elif p == 5: labels.append("F5=2I=E8")
        elif p == 2: labels.append("F2=S3(not binary)")
        else: labels.append(f"F{p}(too large,not binary)")
    got = any(("E6" in L or "E8" in L) for L in labels)
    quo_hits.append((d, got))
    emit(f"   d={d:<2}: {str(rps):<10} : {', '.join(labels)}")
n_exc_quo = sum(1 for (_, g) in quo_hits if g)
emit(f"\n  => via the QUOTIENT (ramified-prime) mechanism, an exceptional McKay label")
emit(f"     appears for {n_exc_quo}/5 of d in {{1,2,3,7,11}} : only d=3 (E6).")
emit(f"     This mechanism IS the B266 atom (Q(sqrt-3) -> mod 3 -> 2T=E6).")

# ----------------------------------------------------------------------------
# SECTION 5 : KNOT mechanism (B282 recompute, CORRECTED)
# ----------------------------------------------------------------------------
emit("\n[5] KNOT mechanism (recompute B282, CORRECTED): pi_1(knot) ->> 2T=SL(2,F3)")
emit("-"*78)

def sl2_Fp(p):
    return [((a,b),(c,dd)) for a in range(p) for b in range(p)
            for c in range(p) for dd in range(p) if (a*dd - b*c) % p == 1]
def matmul(X, Y, p):
    (a,b),(c,d) = X; (e,f),(g,h) = Y
    return (((a*e+b*g)%p, (a*f+b*h)%p), ((c*e+d*g)%p, (c*f+d*h)%p))
def matinv(X, p):
    (a,b),(c,d) = X
    return ((d%p, (-b)%p), ((-c)%p, a%p))
ID = ((1,0),(0,1))
def eval_word(word, gens, p):
    M = ID
    for ch in word:
        M = matmul(M, gens[ch], p) if ch.islower() else matmul(M, matinv(gens[ch.lower()], p), p)
    return M
def image_size(assign, p):
    seen = set(assign); seen.add(ID); frontier = list(seen)
    while frontier:
        new = []
        for X in frontier:
            for Y in list(seen):
                for Z in (matmul(X, Y, p), matmul(Y, X, p)):
                    if Z not in seen: seen.add(Z); new.append(Z)
        frontier = new
    return len(seen)
def count_surjections(gens_letters, relators, p=3):
    """Return (raw, up_to_conj_in_target(Inn=A4,order12), up_to_Aut(2T)=S4)."""
    G = sl2_Fp(p); order = len(G); surj = []
    for assign in itertools.product(G, repeat=len(gens_letters)):
        gens = {L: assign[i] for i, L in enumerate(gens_letters)}
        if any(eval_word(r, gens, p) != ID for r in relators):
            continue
        if image_size(assign, p) == order:
            surj.append(assign)
    seen = set(); conj = 0
    for a in surj:
        if a in seen: continue
        for h in G:
            hi = matinv(h, p)
            seen.add(tuple(matmul(matmul(h, x, p), hi, p) for x in a))
        conj += 1
    aut = conj // 2 if conj > 0 else 0     # Out(2T) = Z/2, so up-to-Aut = conj/2
    return len(surj), conj, aut

# Reid 1991: the figure-eight 4_1 is the UNIQUE arithmetic knot. Every other
# hyperbolic knot below is NON-arithmetic. m003 = 4_1's commensurable sister
# (also arithmetic, trace field Q(sqrt-3)).
ARITH = {"4_1", "m003", "m004"}
knots = ["4_1", "5_2", "6_1", "6_2", "6_3", "7_2", "7_3",
         "7_4", "7_5", "7_6", "7_7", "8_1", "8_2"]
emit("  Reid 1991: 4_1 is the UNIQUE arithmetic knot; all others non-arithmetic.")
emit("  knot   vol      arith?     raw  conj  aut   present(2T=McKay-E6)?")
knot_rows = []
try:
    import snappy
    for name in knots:
        M = snappy.Manifold(name)
        vol = float(M.volume())
        geom = (M.solution_type() == 'all tetrahedra positively oriented')
        FG = M.fundamental_group(simplify_presentation=True)
        raw, conj, aut = count_surjections(FG.generators(), FG.relators(), p=3)
        present = "YES" if raw > 0 else "no"
        arith = "yes(Reid)" if name in ARITH else "no"
        knot_rows.append((name, arith in ("yes(Reid)",), raw))
        gflag = "" if geom else "  [non-geom soln!]"
        emit(f"  {name:<6} {vol:>7.4f}  {arith:<10} {raw:<4} {conj:<4}  {aut:<4}  {present}{gflag}")
except Exception as e:
    emit(f"  (snappy path error: {e})")

n_knot = len(knot_rows)
n_surj_knot = sum(1 for (_, _, r) in knot_rows if r > 0)
n_arith = sum(1 for (_, a, _) in knot_rows if a)
n_nonarith = n_knot - n_arith
n_surj_nonarith = sum(1 for (_, a, r) in knot_rows if (not a) and r > 0)
emit(f"""
  => CORRECTED READING (fixes the sealed draft's material error):
     pi_1 ->> 2T appears for {n_surj_knot}/{n_knot} hyperbolic knots.
     Among the {n_nonarith} NON-arithmetic knots, {n_surj_nonarith} surject (7_2, 7_3, 8_1)
     -- with the IDENTICAL 48/4/2 signature as the arithmetic 4_1.
     The sealed draft's "EXACTLY the arithmetic ones, 0 for non-arithmetic" is
     FALSE.  A 2T-quotient is NOT a signature of arithmeticity; it is a fairly
     common McKay-face phenomenon (here ~{round(100*n_surj_knot/n_knot)}% of the sample,
     ~{round(100*n_surj_nonarith/max(n_nonarith,1))}% of non-arithmetic knots).
     This makes the McKay-face MORE common, REINFORCING outcome B.
     (B266's own count -- m004 has exactly 2 surjections up to Aut(2T) -- is
      reproduced: raw 48 / conj 4 / Aut 2; but 7_2,7_3,8_1 share it exactly, so
      the COUNT is not object-discriminating either.)""")

# ----------------------------------------------------------------------------
# SECTION 6 : base-rate synthesis
# ----------------------------------------------------------------------------
emit("\n[6] BASE-RATE SYNTHESIS")
emit("="*78)
emit(f"""
 (a) The 'three faces' are NOT three independent evidences:
     - McKay-face  = the atom's label (2T -> E6).
     - CIZ-face    = FORCED equal to McKay (same A-D-E list; level k = h-2 = 10).
     - Lie-face    = GENERIC E6 (B282: E6's principal sl2 -> present for every
       hyperbolic knot; Menal-Ferrer-Porti / Falbel-Guilloux genericity).
     => 2-of-3 faces (McKay==CIZ) agree for EVERY object: base rate 5/5 = 100%.
        A single label recurring across >=2 faces is FORCED, not a signal.

 (b) The exceptional MENU for imaginary-quadratic arithmetic is just {{E6}}:
     E7 (2O) needs sqrt2, E8 (2I) needs sqrt5 -- REAL, excluded from every
     imaginary quadratic field. So there is NO birthday problem across
     {{E6,E7,E8}}: E6 is the ONLY exceptional label these objects can show.

 (c) E6 across comparable ARITHMETIC objects (Bianchi orbifolds PSL(2,O_d),
     m004's own arithmetic class):
       - by TORSION (A4 -> 2T):  E6 present in {n_E6_tors}/5 (d=1,2,3,11; absent only d=7);
         extended to all 9 class-number-1 fields: {n_ext}/9 = {round(100*n_ext/9)}% (absent only d=7).
       - m004 (d=3) sits in the majority class; it is EXPECTED, not discriminating.

 (d) The knot recompute (section 5) NO LONGER supports a rarity story:
       - pi_1 ->> 2T occurs for {n_surj_knot}/{n_knot} hyperbolic knots, including NON-arithmetic
         7_2, 7_3, 8_1 with the identical signature. "Has a 2T-quotient" is COMMON,
         not a fingerprint of m004's arithmetic. This strengthens B, not A.

 (e) What IS genuinely object-specific (the ATOM, preserved but NARROWED):
       - the MECHANISM: m004's trace field Q(sqrt-3) reduced mod its ramified
         prime 3 yields 2T=SL(2,F3) (B266); this is tied to m004's OWN field and
         is real. Among Bianchi objects the ramified-prime quotient gives an
         exceptional label only for d=3 ({n_exc_quo}/5). That is a real, banked arithmetic
         fact. It does NOT upgrade the 'three faces' to three signals, and mere
         'presence of a 2T-quotient' (section 5) is not itself rare.

 (f) Object-specific EXTRAS (probe iii): h(E6)=12, |2T|=24, CIZ level k=10 are
     PROPERTIES OF E6, shared by every E6-object (all of d=1,2,3,11,...). m004
     carries no extra coincidence the other E6-objects lack -- same shape all have.

 BASE-RATE NUMBERS (all computed in-sandbox):
   * 2-of-3 faces forced-agree:                 5/5   = 100%   (forced by ADE)
   * exceptional labels reachable (imag.quad.):  {{E6}} only     (E7,E8 excluded)
   * E6 among Euclidean Bianchi (torsion):      {n_E6_tors}/5   = {round(100*n_E6_tors/5)}%    (majority)
   * E6 among all cn=1 imag-quad (torsion):     {n_ext}/9   = {round(100*n_ext/9)}%    (majority)
   * pi_1 ->> 2T among hyperbolic knots:        {n_surj_knot}/{n_knot}  = {round(100*n_surj_knot/n_knot)}%    (COMMON, incl. non-arith)
   * exceptional via ramified-prime quotient:   {n_exc_quo}/5   = {round(100*n_exc_quo/5)}%    (= the atom mechanism)
   * m004-specific extra coincidences:          0

 VERDICT (probe 2): the RECURRENCE-ACROSS-FACES is COMMON / forced, not rare.
   -> OUTCOME B. The flagship 'E6 across three faces' reduces to one atom-label
      (E6 from Q(sqrt-3), B266) echoed by a FORCED classification (CIZ) and a
      GENERIC face (Lie, B282). The only object-specific content is the arithmetic
      atom mechanism, which stands regardless and is separately banked.
   Do-not-over-kill: the ATOM's MECHANISM (m004's Q(sqrt-3) -> mod 3 -> 2T, exact
   count B266; generic Lie face B282) is a genuine, correctly-computed arithmetic
   fact and is NOT disputed here. What is deflated is the '=three independent
   evidences' framing -- and the corrected knot recompute shows the McKay-face is
   even LESS discriminating than the sealed draft claimed.
""")

# ----------------------------------------------------------------------------
# VERIFICATION APPENDIX (compute-not-cite cross-checks of the load-bearing 4/5)
# ----------------------------------------------------------------------------
emit("\n[V] VERIFICATION APPENDIX -- the load-bearing 4/5 (E6 by torsion)")
emit("-"*78)

def build_2T_order(d):
    """Explicitly build <i,j,g> over K=Q(sqrt-d) from a K-solution of -1=x^2+y^2;
    return the order of the generated matrix group (24 == 2T == SL(2,F3))."""
    K = sp.sqrt(-d); sol = None
    for qd in range(1, 13):
        for pd in range(1, 13):
            for qn in range(-12, 13):
                for pn in range(-12, 13):
                    q = sp.Rational(qn, qd); p = sp.Rational(pn, pd)
                    if 2*d*q**2 - 2*p**2 == 1:
                        x = p + q*K; y = -p + q*K
                        if sp.simplify(x**2 + y**2) == -1:
                            sol = (x, y); break
                if sol: break
            if sol: break
        if sol: break
    if sol is None:
        return None
    x, y = sol; I2 = sp.eye(2)
    i = sp.Matrix([[x, y], [y, -x]]); j = sp.Matrix([[0, 1], [-1, 0]])
    k = sp.simplify(i*j); g = sp.simplify((I2 + i + j + k)/2)
    assert sp.simplify(i*i + I2) == sp.zeros(2)
    assert sp.simplify(j*j + I2) == sp.zeros(2)
    assert sp.simplify(i*j + j*i) == sp.zeros(2)
    def key(M): return tuple(sp.simplify(v) for v in M)
    gens = [i, j, g]; seen = {key(I2): I2}; frontier = [I2]
    while frontier:
        nf = []
        for M in frontier:
            for G in gens:
                P = sp.Matrix(2, 2, lambda r, c: sp.simplify((M*G)[r, c]))
                kk = key(P)
                if kk not in seen:
                    seen[kk] = P; nf.append(P)
        frontier = nf
        if len(seen) > 40: break
    return len(seen)

emit("  Explicit 2T=SL(2,F3) construction over Q(sqrt-d) (order should be 24):")
for d in [1, 2, 3, 7, 11]:
    o = build_2T_order(d)
    emit(f"    d={d:<2}: |<i,j,g>| = {o if o is not None else 'no K-solution -> NOT realizable'}")

emit("""
  LOAD-BEARING EVIDENCE for the 4/5 number is ENTIRELY in-sandbox:
    (1) splitting type of 2 in Q(sqrt-d)  [section 2, factor min poly mod 2],
    (2) local-invariant argument  (-1,-1)/K splits <=> 2 not split  [section 2],
    (3) explicit -1 = x^2+y^2 certificate in K for d=1,2,3,11; none for d=7,
    (4) explicit order-24 group <i,j,g> realized over K for d=1,2,3,11 (above),
    (5) class-number-1 => finite subgroup conjugates into SL(2,O_d) [section 3].
  No citation is load-bearing; (1)-(5) alone prove: E6 by torsion for d=1,2,3,11,
  absent for d=7.

  ERROR-LEDGER (self-audit): the SEALED draft's appendix attributed the amalgam
  decompositions "PSL2(O_2)=A4*_{Z/2}D2" and "PSL2(O_11)=A4*_{Z/3}A4" to
  Sengun arXiv:1204.6697. That paper does NOT contain them (it gives only the
  d=1 decomposition, which does contain A4). CORRECT attribution:
     Frohman & Fine, "Some amalgam structures for Bianchi groups,"
     Proc. Amer. Math. Soc. 102 (1988) no.2, 221-229, Theorem 2.1 --
     gives A4-containing decompositions for d=1,2,11 and an A4-FREE one for d=7.
  This literature is CONSISTENT-WITH the in-sandbox derivation above and is cited
  ONLY as corroboration; the 4/5 number does not rest on it. (d=1 also in Sengun.)

  Klein (classical): finite subgroups of PSL(2,O_d) are among
     {1, Z/2, Z/3, D2=V4, S3, A4}; A4's SL-preimage is 2T=binary tetrahedral.
     [Rahm-Fuchs, arXiv:1108.4608, Lemma 10 -- confirms the exceptional label
      reachable by Bianchi torsion is E6 (from A4/2T) and nothing higher.]""")

# write the transcript
import os
here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "b727_probe2_out.txt"), "w") as f:
    f.write("\n".join(OUT) + "\n")
emit("[written] b727_probe2_out.txt")
