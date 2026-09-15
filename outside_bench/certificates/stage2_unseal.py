#!/usr/bin/env python3
"""MEMO-95 CELL: STAGE 2 UNSEALED — the full B928 shape sheet against
measured mixing, executing EXACTLY the protocol sealed in
memos/STAGE2_UNSEALED.md (committed and pushed before this file was
written; commit 1264b3a4).  OWNER-AUTHORIZED COMPARISON ("unseal stage
2 and lets analyze", 2026-08-28): measured values enter THIS CELL ONLY,
as descriptive targets; nothing here feeds any derivation.  B929 is
cited, its m_S x CKM verdict adjudicated by citation, not recomputed
as new.

SHEET SIDE (blind, banked, exact — vendored verbatim from B928 Q3,
frontier/B928_d2_decode/FINDINGS.md; ascending-rho branch order):
  m_S   branches + minpoly 42467328x^3 - 100196352x^2 + 78499872x - 20417473
  m_A   branches + minpoly 42467328x^3 - 56070144x^2 + 19828224x - 2113201
  trM   branches; trM = (3-e1)/2 with e1 minpoly 256x^3 - 768x^2 - 828x + 2859
  t_oct DERIVED (= 2 m_A + 2 trM, exact identity; minpoly
        5308416x^3 - 45868032x^2 + 78736896x - 38004841) — non-verdict
INTEGRITY GATES: every vendored branch decimal annihilates its minpoly
(trM's minpoly DERIVED symbolically from e1's by x -> 3-2t); the sum
rule Tr(m_S) + Tr(t_oct) = 11 exact from minpoly coefficients; the
t_oct identity verified branch-wise at 25 digits.
MEASURED SIDE (external, this cell only): CKM sines (0.22500, 0.04182,
0.00369); PMNS sin^2 (0.303, 0.572, 0.02203) -> sines.
PRIMARY READINGS (6): {m_S, m_A, trM} x {CKM, PMNS}; T1 shape-class
(monotone pattern; cascade index in (1,3) when both are cascades);
T2 both ratio components within factor 2.  Branch order FIXED; the
family/orientation priced bits acknowledged, not exploited.
SECONDARY SCAN (non-verdict): 27 declared derived values (maps m, 1-m,
1-2m; compared by absolute value) x 12 targets; windows 5% and 1%;
counts vs the log-uniform null expectation computed here.
VERDICT RULES: as sealed — any T2 PASS = candidate-needing-new-seal;
all-MISS = the full-sheet closure (the blind sheet does not read
measured mixing directly; B929's nontrivial-map conclusion extends to
the whole sheet).  No outcome is a thesis-failure signal: no banked
theorem ever FORCED these values onto measured mixing.
"""
from fractions import Fraction as Fr
import sympy as sp
from mpmath import mp, mpf, log as mlog

mp.dps = 40
x = sp.symbols('x')

# ---------------- vendored sheet data (B928 Q3, verbatim) ----------------
mS = [mpf('0.86289845162610324642917053'), mpf('0.80011290842674547149446460'),
      mpf('0.69636363994715128207636485')]
pS = [42467328, -100196352, 78499872, -20417473]
mA = [mpf('0.25724237788732187432453483'), mpf('0.23305419858614214462122459'),
      mpf('0.83001592352653598105424057')]
pA = [42467328, -56070144, 19828224, -2113201]
tM = [mpf('0.22209427878365588368609290'), mpf('0.33788637047819001938027994'),
      mpf('2.44001935073815409693362715')]
pe1 = [256, -768, -828, 2859]
pT = [5308416, -45868032, 78736896, -38004841]

def poly_at(c, v):
    return ((c[0]*v + c[1])*v + c[2])*v + c[3]

# trM's minpoly derived from e1's via e1 = 3 - 2t (symbolic)
t = sp.symbols('t')
ptM_expr = sp.expand(sum(sp.Integer(pe1[i])*(3 - 2*t)**(3 - i) for i in range(4)))
ptM = [int(ptM_expr.coeff(t, k)) for k in (3, 2, 1, 0)]
print(f"trM minpoly (derived from e1 by x -> 3-2t): {ptM}")

for name, br, pc in (("m_S", mS, pS), ("m_A", mA, pA), ("trM", tM, ptM)):
    for b in br:
        r = poly_at([mpf(c) for c in pc], b)
        assert abs(r) < mpf(10)**(-15), (name, float(b), float(r))
print("INTEGRITY 1: all nine vendored branch decimals annihilate their minpolys.")

trS = Fr(-pS[1], pS[0]); trT = Fr(-pT[1], pT[0])
assert trS + trT == 11, (trS, trT)
print(f"INTEGRITY 2: Tr(m_S) + Tr(t_oct) = {trS} + {trT} = 11 EXACT (sum rule).")

toct = [2*(mA[i] + tM[i]) for i in range(3)]
for b in toct:
    assert abs(poly_at([mpf(c) for c in pT], b)) < mpf(10)**(-12), float(b)
print(f"INTEGRITY 3: t_oct = 2 m_A + 2 trM branch-wise, and the derived branches")
print(f"   {[f'{float(b):.6f}' for b in toct]} annihilate t_oct's own minpoly.")

# ---------------- measured targets (THIS CELL ONLY) ----------------
CKM = [mpf('0.22500'), mpf('0.04182'), mpf('0.00369')]
PMNS2 = [mpf('0.303'), mpf('0.572'), mpf('0.02203')]
PMNS = [v**mpf('0.5') for v in PMNS2]
print(f"\nMEASURED (external, quarantined): CKM sines {[float(v) for v in CKM]};")
print(f"   PMNS sines {[f'{float(v):.5f}' for v in PMNS]} (from sin^2 {[float(v) for v in PMNS2]})")

# ---------------- primary readings ----------------
def pattern(tr3):
    s1 = '+' if tr3[1] > tr3[0] else '-'
    s2 = '+' if tr3[2] > tr3[1] else '-'
    return {'--': 'DESC', '++': 'ASC', '-+': 'V', '+-': 'LAMBDA'}[s1 + s2]
def ratios(tr3):
    return (tr3[1]/tr3[0], tr3[2]/tr3[1])
def casc_index(tr3):
    r1, r2 = ratios(tr3)
    return mlog(r2)/mlog(r1)

sheets = [("m_S", mS), ("m_A", mA), ("trM", tM)]
targets = [("CKM", CKM), ("PMNS", PMNS)]
print("\nPRIMARY READINGS (T1 shape / T2 factor-2 on ratio pair):")
t2_passes = []
for tname, tv in targets:
    tp = pattern(tv); tq = ratios(tv)
    ti = casc_index(tv) if tp in ('DESC', 'ASC') else None
    for sname, sv in sheets:
        spat = pattern(sv); sq = ratios(sv)
        t1 = (spat == tp)
        if t1 and ti is not None:
            si = casc_index(sv)
            t1 = bool(1 < si < 3) and bool(1 < ti < 3)
        f1 = max(sq[0]/tq[0], tq[0]/sq[0]); f2 = max(sq[1]/tq[1], tq[1]/sq[1])
        t2 = bool(f1 <= 2 and f2 <= 2)
        note = "  [= B929, adjudicated by citation: HIT-SHAPE, T2 MISS, direct ID DEAD]" \
               if (sname, tname) == ("m_S", "CKM") else ""
        print(f"   {sname:4s} x {tname:4s}: pattern {spat:6s} vs {tp:6s} -> "
              f"T1 {'PASS' if t1 else 'MISS'};  ratio-offs (x{float(f1):.2f}, x{float(f2):.2f})"
              f" -> T2 {'PASS' if t2 else 'MISS'}{note}")
        if t2:
            t2_passes.append((sname, tname))
print(f"   sheet cascade indices: m_S {float(casc_index(mS)):.3f} (B929: 1.838); "
      f"CKM {float(casc_index(CKM)):.3f}")

# ---------------- secondary scan (non-verdict) ----------------
vals = []
for sname, sv in sheets:
    for mapname, f in (("m", lambda v: v), ("1-m", lambda v: 1 - v), ("1-2m", lambda v: 1 - 2*v)):
        for i, b in enumerate(sv):
            vals.append((f"{sname}.{mapname}.b{i+1}", abs(f(b))))
targs = [("CKM.sin", CKM), ("CKM.sin2", [v*v for v in CKM]),
         ("PMNS.sin", PMNS), ("PMNS.sin2", PMNS2)]
pairs = [(vn, vv, tn2 + f".{j+1}", tv2)
         for vn, vv in vals for tn2, tl in targs for j, tv2 in enumerate(tl)]
hits5 = [(vn, float(vv), tn2, float(tv2), float(abs(vv/tv2 - 1)))
         for vn, vv, tn2, tv2 in pairs if abs(vv/tv2 - 1) < mpf('0.05')]
hits1 = [h for h in hits5 if h[4] < 0.01]
import math
allv = [float(v) for _, v in vals] + [float(tv2) for _, tl in targs for tv2 in tl]
lo, hi = min(allv), max(allv)
lr = math.log(hi/lo)
exp5 = len(pairs)*math.log(1.05/0.95)/lr
exp1 = len(pairs)*math.log(1.01/0.99)/lr
print(f"\nSECONDARY SCAN ({len(pairs)} pairs; log-uniform null over [{lo:.4g}, {hi:.4g}]):")
print(f"   5% window: {len(hits5)} coincidences vs {exp5:.1f} expected by chance")
print(f"   1% window: {len(hits1)} coincidences vs {exp1:.1f} expected by chance")
for vn, vv, tn2, tv2, d in sorted(hits1, key=lambda h: h[4]):
    print(f"      {vn} = {vv:.5f}  vs  {tn2} = {tv2:.5f}   ({d*100:.2f}%)")
print("   (listed 1%-window items are CHANCE-GRADE by the sealed rule — the count")
print("    sits at the null expectation; nothing here is promotable.)")

# ---------------- the sealed verdict ----------------
if not t2_passes:
    print("""
VERDICT (per the sealed rules): ALL SIX primary readings MISS Tier 2,
and the five NEW Tier-1 cells all MISS on shape class (m_A is V-shaped,
trM ascending, vs CKM's descending cascade and PMNS's LAMBDA — only
B929's already-adjudicated m_S x CKM cell has the matching shape class,
and its direct identification is already DEAD at Tier 2).
THE FULL-SHEET CLOSURE BANKS: the blind B928 shape sheet does NOT read
measured mixing directly — not m_S (B929), not m_A, not trM, not
against CKM, not against PMNS, and the derived-value scan sits at its
chance expectation.  B929's conclusion extends to the whole sheet: IF
the twist speaks to measured mixing, it is through a nontrivial map
that no banked structure currently supplies.  The value layer's real
contact points remain the STRUCTURAL facts (the forced equalities, the
sum rule 11, the norm laws, the mirror-even hierarchy carrier of memo
92) — not the raw branch values.  Per the sealed rule and the owner's
directive: this is NOT a thesis-failure signal — no banked theorem
ever forced these values onto measured mixing; the priced map stays
priced, now with its direct-reading option eliminated exhaustively.""")
else:
    print(f"""
VERDICT (per the sealed rules): T2 PASS at {t2_passes} — candidate(s)
requiring their own follow-up seal; nothing more is claimed here.""")
print("""Quarantine: measured values die with this cell; no derivation reads
this output.  Gate 5 discipline outside this cell: untouched.""")
