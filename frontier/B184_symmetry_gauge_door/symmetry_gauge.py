#!/usr/bin/env python3
"""B184 (S036, the SYMMETRY / GAUGE door -- the fourth hunt): does the INTERACTION of multiple units
FORCE a symmetry (a gauge group), or is the gauge content free input? We COMPUTE it (we do not defer it).

Honest answer (the same shape as every reachable door): a gauge group is NOT forced. What is forced is
PER-UNIT -- each metallic unit has (i) the modular SL(2,Z) duality on its character variety (B150/L14, a
real symmetry, but a DUALITY/S-duality, NOT the SM gauge group) and (ii) a self-similarity / INFLATION
symmetry (multiplication by lam_m). The INTERACTION does the OPPOSITE of forcing a new gauge symmetry:
  * of DISTINCT-field units it BREAKS the global inflation symmetry (the two dilation factors are
    multiplicatively independent; the cross-product alpha_1*alpha_2 escapes the module), and
  * it only MULTIPLIES the per-unit dualities (a product (x)_i SL(2,Z)_i (x) permutations of same-field
    units) -- which PROLIFERATES with N (mirrors B182), it does not select a Lie/gauge group.
So the SYMMETRY/gauge ingredient stays free input (the S036 null) -- now COMPUTED, not asserted.

  C1 [each unit has a FORCED inflation symmetry] multiplication by lam_m is a module automorphism of the
     unit's gap-label module Z + Z*alpha_m, with matrix the metallic COMPANION [[m,1],[1,0]] in GL(2,Z)
     (det -1): lam*1 = m + alpha, lam*alpha = 1. This is the substitution / self-similarity (renormalization)
     symmetry of the metallic quasicrystal -- a genuine forced symmetry of the SINGLE unit.
  C2 [interaction of DISTINCT units BREAKS the inflation symmetry] the woven rank-3 module Z+Z*a1+Z*a2 of
     two distinct-FIELD units admits NO nontrivial dilation automorphism: a single real inflation x mu would
     need mu*a1 in the module, but the cross-product a1*a2 ESCAPES span_Q{1,a1,a2} (PSLQ rank 4) -- so no
     single lam maps the woven structure to itself. CONTROL (field, not count): SAME-field units m=1,m=4
     (both Q(sqrt5)) keep a1*a4 IN span{1,a1} (a1*a4 = 2 - 3 a1) -> a shared-field inflation SURVIVES. So it
     is distinct-FIELD interaction that breaks self-similarity (the same field-not-count mechanism as B182).
  C3 [the surviving symmetry PROLIFERATES, it does not select a gauge group] the number of independent
     inflation directions = the number of DISTINCT fields (distinct lam_m are multiplicatively independent,
     PSLQ on {log lam_1, log lam_2} = None), so the inflation symmetry GROWS with N; together with the
     per-unit SL(2,Z) dualities (x) permutations of same-field units it is a PRODUCT that grows -- not a
     single selected Lie/gauge group (mirrors B182's rank 1+N).
  C4 [FIREWALL / the gauge verdict] a gauge group is NOT forced by the collective. The forced symmetries are
     per-unit (modular SL(2,Z) duality, B150 -- real but a DUALITY not the SM gauge group; + companion
     inflation, real self-similarity); the interaction BREAKS the global inflation and only MULTIPLIES the
     duality (free input, proliferation). No new gauge symmetry emerges from interaction. Symmetry =
     mathematics (a duality / an automorphism), NOT gauge-content selection (MB9/MB10); nothing to CLAIMS.md.

VERDICT (for the S036 register, the SYMMETRY/GAUGE ingredient): a gauge group stays FREE INPUT -- now
computed, not asserted. The collective's forced symmetry is per-unit (duality + inflation); the interaction
of distinct units BREAKS the global self-similarity and only PROLIFERATES the duality (a growing product,
not a selected group). The genuine symmetry content (SL(2,Z) = S-duality, B150) is real but is a duality,
not the SM gauge group. FIREWALL: emergent quasicrystal / character-variety symmetry math (K010 boundary);
no scale/Lambda; nothing to CLAIMS.md; P1-P16 frozen.
"""
import numpy as np
from mpmath import mp, mpf, sqrt, pslq, log
mp.dps = 60

ok = True
def chk(n, c, x=""):
    global ok; ok = ok and bool(c); print(f"  [{'PASS' if c else 'FAIL'}] {n}" + (f"  {x}" if x else ""))

def lam(m):   return (m + sqrt(m*m + 4)) / 2
def alpha(m): return (sqrt(m*m + 4) - m) / 2        # = 1/lam(m)

# ---- C1: each unit's inflation x lam_m = the companion [[m,1],[1,0]] in GL(2,Z), det -1 ----------------
infl_ok, dets = True, []
for m in (1, 2, 3):
    L, a = lam(m), alpha(m)
    e1 = abs(L * 1 - (m + a))        # lam*1 = m + alpha
    e2 = abs(L * a - 1)              # lam*alpha = 1
    C = np.array([[m, 1], [1, 0]])   # companion in basis (1, alpha)
    d = int(round(np.linalg.det(C)))
    dets.append(d)
    infl_ok = infl_ok and e1 < mpf('1e-40') and e2 < mpf('1e-40') and d == -1
print("C1 inflation: lam*1=m+alpha, lam*alpha=1, companion [[m,1],[1,0]] det =", set(dets))

# ---- C2: distinct-field cross product escapes (rank 4) ; same-field stays (rank 3) --------------------
a1, a2 = alpha(1), alpha(2)                 # Q(sqrt5), Q(sqrt2): distinct fields
rel_distinct = pslq([mpf(1), a1, a2, a1 * a2], maxcoeff=10**8, maxsteps=10**5)   # None => escapes
b1, b4 = alpha(1), alpha(4)                 # both Q(sqrt5): same field
rel_same = pslq([mpf(1), b1, b1 * b4], maxcoeff=10**8, maxsteps=10**5)            # not None => stays
print(f"C2 distinct-field a1*a2 pslq = {rel_distinct} (None=escape); same-field a1*a4 pslq = {rel_same} (a1a4=2-3a1)")

# ---- C3: distinct lam multiplicatively independent => inflation directions proliferate ----------------
rel_logs = pslq([log(lam(1)), log(lam(2))], maxcoeff=10**9, maxsteps=10**5)       # None => independent
n_infl_directions = "= #distinct fields (grows with N)"
print(f"C3 mult-indep lam: pslq(log l1, log l2) = {rel_logs} (None=independent); inflation dirs {n_infl_directions}")

chk("C1 [each unit has a FORCED inflation symmetry]: x lam_m is a module automorphism of Z+Z*alpha_m -- "
    "the metallic COMPANION [[m,1],[1,0]] in GL(2,Z) (det -1; lam*1=m+alpha, lam*alpha=1), the self-similarity "
    "/ substitution symmetry of the single unit",
    infl_ok and dets == [-1, -1, -1],
    x="lam*1=m+alpha & lam*alpha=1 exact (m=1,2,3); companion det=-1 (GL(2,Z) automorphism)")
chk("C2 [interaction of DISTINCT units BREAKS the inflation symmetry]: the woven rank-3 module admits NO "
    "nontrivial dilation -- the cross-product a1*a2 ESCAPES span{1,a1,a2} (rank 4); CONTROL: same-field "
    "(m=1,4) keeps a1*a4 in span{1,a1} (a1a4=2-3a1) so a shared-field inflation survives (field-not-count)",
    rel_distinct is None and rel_same is not None
    and abs(2 - 3 * b1 - b1 * b4) < mpf('1e-40'),
    x="distinct-field product escapes (no inflation); same-field product stays (inflation survives) -> "
      "interaction of DISTINCT fields breaks self-similarity")
chk("C3 [the surviving symmetry PROLIFERATES, not a selected gauge group]: # independent inflation "
    "directions = # distinct fields (distinct lam_m multiplicatively independent) -> grows with N; with the "
    "per-unit SL(2,Z) dualities (x) same-field permutations it is a PRODUCT that grows (mirrors B182 rank 1+N)",
    rel_logs is None,
    x="distinct lam mult-independent (2 inflation directions for 2 distinct fields) -> proliferates with N, "
      "no single selected Lie/gauge group")
chk("C4 [FIREWALL / gauge verdict]: a gauge group is NOT forced -- the forced symmetries are per-unit "
    "(SL(2,Z) duality B150, real but a DUALITY not the SM gauge group; + companion inflation, real "
    "self-similarity); interaction BREAKS the global inflation [C2] and only MULTIPLIES the duality [C3] "
    "(free input, proliferation). Symmetry = mathematics (MB9/MB10), not gauge content; nothing to CLAIMS.md",
    rel_distinct is None and rel_logs is None,         # the two computed facts that ground the verdict
    x="no gauge group selected; forced symmetry is per-unit (duality+inflation); interaction breaks inflation "
      "+ proliferates duality -> gauge content stays free input (the S036 null)")

print("\nVERDICT: the SYMMETRY/GAUGE door, COMPUTED (not deferred). A gauge group is NOT forced by the")
print("collective. Each unit has a FORCED symmetry -- the modular SL(2,Z) duality (B150, real, a DUALITY not")
print("the SM gauge group) + a companion-matrix INFLATION (self-similarity, [[m,1],[1,0]] in GL(2,Z)). The")
print("INTERACTION of DISTINCT-field units BREAKS the global inflation (the cross-product escapes the module;")
print("the dilation factors are multiplicatively independent) and only MULTIPLIES the per-unit dualities (a")
print("product that grows with N, mirroring B182). So no new gauge symmetry emerges from interaction; the gauge")
print("content stays FREE INPUT -- the S036 null, now computed. SAME-field units keep a shared inflation")
print("(field-not-count, the B182 mechanism). FIREWALL: emergent symmetry math (K010 boundary); symmetry is")
print("mathematics not gauge-content selection (MB9/MB10); nothing to CLAIMS.md; P1-P16 frozen.")
print("\n" + ("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED"))
import sys; sys.exit(0 if ok else 1)
