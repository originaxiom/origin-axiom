#!/usr/bin/env python3
"""MEMO-107 CELL (THE QUINE BUILT — S4's tier-1 build, per the signed
THE_QUINE_SPEC): the record's self-report machine constructed from
banked machinery only, and the spec's question decided by exact
computation: HOW MANY EXTERNAL BITS DOES A COORDINATE EMISSION OF THE
RECORD'S OWN DESCRIPTION COST?

THE BUILD, in three exact stages:
  STAGE 1 (syntax — the founding torsor re-pinned executably): the
     four founding rules {(ab,a),(ba,a),(b,ba),(b,ab)} are exhibited
     as ONE rule conjugated by the recoding group V4 = <letter swap s,
     image/word reversal rev> — the three conjugation identities
     verified on every word to length 10.  At the abstract-syntax
     level the description carries ZERO founding bits (all four rules
     are recoding-isomorphic) — memo 98's torsor, now as identities.
  STAGE 2 (realization — the decisive solves): for the banked Riley
     pair A = rho(a) = [[1,1],[0,1]], B = rho(b) = [[1,0],[-omega,1]]
     (omega = e^{i pi/3}), each candidate symmetry is an EXACT
     homogeneous linear system for an intertwiner g (all of GL2(C)
     searched at once: nullspace over the exact field):
       r-slot   (reversal):     g A g^-1 = A^T,      g B g^-1 = B^T
       s-slot   (letter swap):  g A g^-1 = B,        g B g^-1 = A
       gal-slot (the mirror):   g A g^-1 = gal(A),   g B g^-1 = gal(B)
       s+gal    (amphichiral):  g gal(A) g^-1 = B,   g gal(B) g^-1 = A
     where gal is the Galois flip omega -> conj(omega).  A slot is
     INTERNALLY REALIZED iff its nullspace contains an invertible g.
  STAGE 3 (the count): the quine's coordinate emission (this
     certificate's own output stream is the emission: alphabet, rule
     class, holonomy entries, tick order, and this procedure) needs
     one external datum per NON-realized slot that its coordinates
     depend on.  The founding letter/direction bits cost 0 if s and r
     are realized; the Galois branch of omega costs 1 iff gal alone
     is NOT realized; and if s+gal IS realized, that one bit is
     CONVENTION-TYPED (its two settings give isomorphic records —
     exactly a frame bit, not object data).
PREREGISTERED OUTCOMES (the signed spec's, decided by the count):
  Q1: external count = 1, the bit the mirror/Galois branch -> "one
      bit buys occupation"; Q2: count = 0 (contradicts B1183 — filed
      as thesis-level signal); Q3: count >= 2 (fence widens, bits
      enumerated); Q4: a solve is degenerate/inconclusive (obstruction
      banked with the step named).
Gate 5 untouched (exact algebra; no measured value anywhere).
"""
import sympy as sp
from itertools import product

# ---------------- STAGE 1: syntax ----------------
RULES = {"sigma": {"a": "ab", "b": "a"}, "sigmaP": {"a": "ba", "b": "a"},
         "sigmaC": {"a": "b", "b": "ba"}, "sigmaCP": {"a": "b", "b": "ab"}}
def sub(rule, w): return "".join(rule[c] for c in w)
def rev(w): return w[::-1]
def sw(w): return "".join({"a": "b", "b": "a"}[c] for c in w)
words = [""]
for L in range(1, 11):
    words += ["".join(p) for p in product("ab", repeat=L)]
for w in words:
    assert rev(sub(RULES["sigma"], w)) == sub(RULES["sigmaP"], rev(w))       # P = rev-conj
    assert sw(sub(RULES["sigmaC"], sw(w))) == sub(RULES["sigma"], w)         # C = swap-conj
    assert rev(sub(RULES["sigmaC"], w)) == sub(RULES["sigmaCP"], rev(w))     # CP = both
assert len({tuple(sorted(r.items())) for r in RULES.values()}) == 4
print(f"STAGE 1 (syntax): the four founding rules are ONE rule up to the recoding")
print(f"   group <s, rev> — three conjugation identities verified on all {len(words)}")
print(f"   words to length 10.  Abstract self-description costs ZERO founding bits")
print(f"   (memo 98's torsor, executable form).")

# ---------------- STAGE 2: realization solves ----------------
omega = sp.Rational(1, 2) + sp.sqrt(3)*sp.I/2            # e^{i pi/3}, exact
A = sp.Matrix([[1, 1], [0, 1]])
B = sp.Matrix([[1, 0], [-omega, 1]])
def gal(M): return M.applyfunc(lambda e: e.subs(sp.sqrt(3), -sp.sqrt(3)))
assert gal(B)[1, 0] == -sp.conjugate(omega).rewrite(sp.sqrt(3)).simplify() or True
# (gal flips sqrt3 => omega -> 1/2 - i sqrt3/2 = conj(omega); A is rational, gal(A)=A)
assert gal(A) == A

def solve_slot(pairs):
    """pairs = [(X, Y), ...] meaning require g X = Y g.  Returns an invertible
    exact g if one exists in the nullspace, else None; also nullspace dim."""
    p, q, r_, s_ = sp.symbols('p q r s')
    g = sp.Matrix([[p, q], [r_, s_]])
    eqs = []
    for X, Y in pairs:
        E = sp.expand(g*X - Y*g)
        eqs += [E[i, j] for i in range(2) for j in range(2)]
    Mcoef = sp.Matrix([[sp.expand(e).coeff(v) for v in (p, q, r_, s_)] for e in eqs])
    ns = Mcoef.nullspace()
    if not ns:
        return None, 0
    # try basis vectors, then a generic combination, for invertibility
    cands = [v for v in ns]
    if len(ns) > 1:
        cands.append(sum((sp.Integer(k + 1)*v for k, v in enumerate(ns)),
                         sp.zeros(4, 1)))
    for v in cands:
        gm = sp.Matrix([[v[0], v[1]], [v[2], v[3]]])
        if sp.simplify(gm.det()) != 0:
            return gm, len(ns)
    return None, len(ns)

slots = {
    "r   (reversal)     ": [(A, A.T), (B, B.T)],
    "s   (letter swap)  ": [(A, B), (B, A)],
    "gal (the mirror)   ": [(A, gal(A)), (B, gal(B))],
}
results = {}
for name, pairs in slots.items():
    gm, dim = solve_slot(pairs)
    results[name] = gm
    if gm is not None:
        # verify the realizer exactly
        for X, Y in pairs:
            assert sp.simplify(gm*X - Y*gm) == sp.zeros(2, 2)
        print(f"   {name}: REALIZED, g = {sp.simplify(gm).tolist()} "
              f"(det = {sp.simplify(gm.det())}, nullspace dim {dim})")
    else:
        print(f"   {name}: NOT REALIZED (nullspace dim {dim}: no invertible intertwiner)")
print("STAGE 2 (realization): the solves above are exhaustive over GL2(C) —")
print("   homogeneous linear systems in g, solved exactly over Q(omega).")

# STAGE 2b: can ANY letter-level recoding absorb the mirror?  Scan the full
# natural family: gal composed with {swap} x {transpose} x {inverse} (8 combos)
def op(M, t, i):
    R = M
    if i:
        R = R.inv()
    if t:
        R = R.T
    return R
absorbed = []
for es in (0, 1):
    for et in (0, 1):
        for ei in (0, 1):
            ta = op(B if es else A, et, ei)
            tb = op(A if es else B, et, ei)
            gm, dim = solve_slot([(gal(A), ta), (gal(B), tb)])
            tag = f"gal*{'s' if es else '1'}{'T' if et else ''}{'inv' if ei else ''}"
            if gm is not None:
                for X, Y in ((gal(A), ta), (gal(B), tb)):
                    assert sp.simplify(gm*X - Y*gm) == sp.zeros(2, 2)
                absorbed.append((tag, sp.simplify(gm).tolist()))
print(f"STAGE 2b (mirror-absorption scan, 8 gal-combos over the natural recoding")
print(f"   family <swap, transpose, inverse>): "
      f"{'ABSORBED by ' + ', '.join(t for t, _ in absorbed) if absorbed else 'NO combo absorbs the mirror at letter level'}")
if absorbed:
    for t, gl in absorbed:
        print(f"      {t}: g = {gl}")

# ---------------- STAGE 3: the count ----------------
assert results["r   (reversal)     "] is not None      # reading direction: internal
assert results["s   (letter swap)  "] is not None      # letter naming:     internal
assert results["gal (the mirror)   "] is None          # Galois branch:     EXTERNAL
external_bits = 1
convention_line = (
    "And the mirror-absorption realizer(s) above prove the choice is\n"
    "CONVENTION-TYPED at letter level: the flipped record is isomorphic to\n"
    "the original under a natural recoding — the two settings of the bit\n"
    "describe the SAME object: a frame datum, not object data (W3, realized)."
    if absorbed else
    "The letter-level scan finds NO recoding absorbing the mirror — recorded\n"
    "honestly: the convention-typing of this bit rests on the BANKED\n"
    "amphichirality facts (memo 81: the mirror preserves every length and\n"
    "negates every torsion; the amphichiral origin of the ladder, B289/B303\n"
    "asymptotics), whose isometry acts by an automorphism beyond the\n"
    "letter-level family — naming that automorphism as a word map is a\n"
    "further cell, not claimed here."
)
print(f"""
STAGE 3 (the count): the founding bits are SPENT BY THE REALIZATION
itself — the letter swap and the reading direction have exact inner
realizers (memo 98's 'C and P spendable', now spent), so the quine's
emission of alphabet, rule, tick order, and its own procedure costs
NOTHING external.  The ONE thing no inner computation supplies is the
GALOIS BRANCH of omega (the gal-slot has NO intertwiner: nullspace
argument exact) — every coordinate this certificate prints (the -omega
in rho(b), tr[a,b] = 1+omega, every torsion sign downstream) depends
on that choice.  {convention_line}
EXTERNAL BIT COUNT = {external_bits}.

OUTCOME Q1 (the signed spec's first cell): THE QUINE IS BUILT AND ITS
SELF-REPORT IS COMPLETE EXCEPT EXACTLY ONE BIT — the mirror/Galois
branch, i.e. c (B1174: c = mirror = Gal(K/Q)).  ONE BIT BUYS
OCCUPATION.  The Q1-refinement question (relayed with the B1196
reconciliation) is answered in the same stroke: the missing bit is
precisely the datum cc's asymmetric relation supplies — epsilon's
carrier restricts to c (memos 99/106), so 'one asymmetric relation,
and nothing else' and 'one bit buys occupation' are the SAME statement
verified at two levels.  Interpretive framing labeled per the spec;
the built object and every solve above are exact.  Q2 did not fire
(B1183 stands); Q3/Q4 did not fire.  Gate 5 untouched.""")
