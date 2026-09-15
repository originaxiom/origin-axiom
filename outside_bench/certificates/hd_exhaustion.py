#!/usr/bin/env python3
"""MEMO-129 CELL (the owner's "elaborate" on memo 128): THE Hd MENU IS
EXHAUSTED — the cubic supplies EXACTLY THREE couplings with an Hd leg and
EXACTLY ONE canonical linear condition, so the P^3's "one condition short"
is STRUCTURAL; plus the one matrix-valued cut B1206's candidate list never
named, and why it is probably not independent.

WHERE MEMO 128 LEFT IT.  Memo 128 closed B1206's candidates (i) and (iii)
negatively by showing that rank in COMPONENT space measures the gauge
contraction tensor (eps for SU(2), delta for SU(3)) and never the number of
conditions.  That kills three NAMED routes.  It does not, by itself, say
whether some UNNAMED route exists.  This cell settles that, because the
menu is finite and memo 80 already enumerated it.

EXHAUST BEFORE BUILDING (the standing rule).  Memo 80's SECTOR TRIPLE TABLE
is a CLOSED CENSUS — every one of the 45 nonzero C entries is accounted for
by a multiplet triple (its own assert).  So the list of couplings with an Hd
leg is COMPLETE BY CONSTRUCTION, and nothing needs rebuilding: it is read
off the banked table and re-verified here.

THE GENERAL LEMMA MEMO 128 PROVED, stated once as a reusable instrument:
  GAUGE-RANK LEMMA.  For a coupling C(A, B, .) with A, B gauge multiplets,
  the rank of the component matrix is the rank of the GAUGE CONTRACTION
  TENSOR joining them (eps: rank 2; delta_3: rank 3), and it is fixed by the
  gauge group alone.  The number of CONDITIONS is the number of independent
  INVARIANT contractions, which is what must be counted.  Reading a
  component rank as a count of conditions overcounts by exactly the
  dimension of the gauge representation.

THE CELLS:
  E1  THE EXHAUSTION: filter memo 80's closed census to triples with an Hd
      leg.  Report the complete list and re-verify the census closes at 45.
  E2  THE CANONICAL COUNT: of those, how many have BOTH other legs pinned to
      a unique multiplet (B1206's own criterion for a canonical condition)?
  E3  THE UNNAMED CANDIDATE: any OTHER matrix-valued Hd coupling supplies a
      determinantal (nonlinear) cut just as B1205's det Y_d(h) does.  Report
      which, and note that B1206's ledger counts only one such cut.
  E4  IS IT INDEPENDENT?  Compare the two matter rows' C coefficients and
      entry counts.  Preregistered reading, fixed before the numbers print:
        * identical coefficient magnitudes AND entry counts in the ratio
          (colour dim) : 1  =>  ONE shared operator (the 10.5bar.5bar_H
          shape, Y_e = Y_d^T), so det Y_e is NOT an independent cut;
        * differing magnitudes  =>  two operators, and det Y_e is a genuine
          SECOND nonlinear condition that would CLOSE B1206's ledger.
  E5  VERDICT and the one bounded question this bench cannot settle.
Gate 5 untouched: zero/nonzero patterns, counts and coefficient magnitudes
only; no coupling is asserted to take any value.
"""
import os, io, contextlib, itertools
from fractions import Fraction as F
from collections import Counter

SCR = os.path.dirname(os.path.abspath(__file__))
src = open(SCR + "/yukawa_texture.py").read()
cut = src.index("# full triple census")
_buf = io.StringIO()
with contextlib.redirect_stdout(_buf):
    exec(compile(src[:cut], "yukawa_texture.py[prefix]", "exec"))
print("E0 — memo 80's cubic and roster rebuilt in-run (imported verbatim).")
print(f"    Hu {Hu}  Hd {Hd}  neutrals {nuS}  ec {MULT['ec']}")

# ---- E1: the exhaustion, from memo 80's CLOSED census
names = list(MULT)
cens = Counter()
for na, nb, nc in itertools.combinations_with_replacement(names, 3):
    seen = set(); cnt = 0
    for a in MULT[na]:
        for b in MULT[nb]:
            for c_ in MULT[nc]:
                t = tuple(sorted((a, b, c_)))
                if t in seen:
                    continue
                seen.add(t)
                if Cval(*t) != 0:
                    cnt += 1
    if cnt:
        cens[(na, nb, nc)] = cnt
total = sum(cens.values())
assert total == 45, total
print(f"\nE1 — THE EXHAUSTION.  memo 80's census re-verified CLOSED: {total} of 45"
      f" nonzero C entries accounted for by {len(cens)} multiplet triples.")
hd_rows = {k: v for k, v in cens.items() if "Hd" in k}
print("    COUPLINGS WITH AN Hd LEG — the complete menu of functionals on B0:")
for k, v in sorted(hd_rows.items(), key=lambda x: -x[1]):
    print(f"        {'.'.join(k):<16s} : {v:2d} entries")
print(f"    => EXACTLY {len(hd_rows)} couplings touch Hd.  The census is closed,")
print("       so this list is COMPLETE: there is no unnamed linear route.")

# ---- E2: the canonical count
PINNED = {"Hu", "N1", "N2", "ec"}     # unique multiplet per B1161's sector table
print("\nE2 — THE CANONICAL COUNT (B1206's own criterion: BOTH other legs pinned")
print("     to a unique multiplet, so the functional does not depend on a choice):")
canon = []
for k, v in sorted(hd_rows.items()):
    others = [n for n in k if n != "Hd"] if k.count("Hd") == 1 else \
             [n for n in k if n != "Hd"] + ["Hd"]
    ok = all(n in PINNED for n in others)
    print(f"        {'.'.join(k):<16s} other legs {str(others):<16s} "
          f"{'CANONICAL' if ok else 'depends on matter states — texture data'}")
    if ok:
        canon.append(k)
assert len(canon) == 1, canon
print(f"    => EXACTLY {len(canon)} canonical linear condition: {'.'.join(canon[0])}")
print("       — the lambda-term.  Memo 128 showed it supplies ONE invariant")
print("       functional; E1 now shows it is the ONLY one the cubic can supply.")
print("       B1206's 'one condition short' is therefore STRUCTURAL, not a gap")
print("       in the search: no unnamed linear route exists to be found.")

# ---- E3: the unnamed candidate
matter = [k for k in hd_rows if k not in canon]
print("\nE3 — THE CANDIDATE B1206's LIST NEVER NAMED.")
print("     A matrix-valued Hd coupling supplies a DETERMINANTAL (nonlinear) cut,")
print("     exactly as B1205's det Y_d(h) = 0 does.  Matrix-valued Hd rows:")
for k in sorted(matter):
    print(f"        {'.'.join(k):<16s} -> det of this row is a candidate cut")
print("     B1206's ledger counts ONE nonlinear cut (det Y_d).  The lepton row")
print("     l.ec.Hd is the SECOND, and it appears in NONE of B1206's three")
print("     candidates.  If independent, it closes the ledger: 3 - 1 - 1 - 1 = 0.")

# ---- E4: is it independent?
def row_entries(na, nb):
    out = {}
    for a in MULT[na]:
        for b in MULT[nb]:
            for h in Hd:
                v = Cval(a, b, h)
                if v != 0:
                    out[(a, b, h)] = v
    return out
qd = row_entries("q", "dc")
le = row_entries("l", "ec")
mag_qd = sorted({abs(v) for v in qd.values()})
mag_le = sorted({abs(v) for v in le.values()})
NCOL = len(MULT['D'])          # colour dimension, read off the roster (a 3)
print("\nE4 — IS THE SECOND CUT INDEPENDENT?  (preregistered reading above)")
print(f"    q.dc.Hd : {len(qd)} entries, coefficient magnitudes {mag_qd}")
print(f"    l.ec.Hd : {len(le)} entries, coefficient magnitudes {mag_le}")
print(f"    entry-count ratio {len(qd)}:{len(le)} = {len(qd)//len(le)}:1,"
      f" and the colour dimension read off the roster is {NCOL}")
same = (mag_qd == mag_le)
ratio_ok = (len(qd) == NCOL * len(le))
print(f"    identical magnitudes: {same}      ratio = colour dim : 1 : {ratio_ok}")
assert NCOL == 3, NCOL
assert same and ratio_ok
print("    ==> ONE SHARED OPERATOR.  Both rows carry unit coefficients and the")
print("        counts differ by exactly the colour factor (6 = 3x2 vs 2 = 1x2):")
print("        the signature of a single 10.5bar.5bar_H-shaped operator, i.e.")
print("        Y_e = Y_d^T.  On the cubic the two determinants are NOT")
print("        independent, so det Y_e supplies NO new condition and B1206's")
print("        ledger still STANDS at dim 1.")

# ---- E5
print("""
E5 — VERDICT, and the one bounded question this bench cannot settle.
  THE STRUCTURAL RESULT: the object's cubic touches Hd in exactly THREE
  couplings (closed census), of which exactly ONE is canonical (the
  lambda-term) and TWO are matter rows whose determinants are the SAME
  cut because they descend from one operator.  So the cubic supplies
  exactly ONE linear and ONE nonlinear condition on B0 — precisely
  B1206's ledger — and NO FOURTH ROUTE EXISTS INSIDE THE CUBIC.  The
  P^3's "one condition short" is a structural fact about the cubic, not
  an unfinished search.  B1196's CLOSED-PERMANENT verdict is hardened
  a second time, now by exhaustion rather than by candidate-by-candidate
  refutation.
  THE ONE BOUNDED QUESTION, named and handed on: this cell works on ONE
  27, where "Y_e = Y_d^T" is read off shared unit coefficients.  The
  GENERATION-level embedding (B1161's selection cochain, not on this
  bench) could in principle distinguish the two rows and make det Y_e an
  independent cut after all — which would CLOSE the ledger.  That is a
  single, bounded check for whoever holds B1161, and it is the only
  route to closure this exhaustion leaves open.
  FENCE: counts, zero/nonzero patterns and coefficient magnitudes only.
  Nothing here asserts a coupling value, and "Y_e = Y_d^T" is stated as
  the SHAPE the cubic carries on one 27, not as a physical prediction at
  any scale.  Gate 5 untouched.""")
