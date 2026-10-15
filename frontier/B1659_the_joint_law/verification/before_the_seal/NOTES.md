# P-168 — the joint law (main's exploration, firewalled until sealed)

## 2026-10-15 ~17:45 — the joint law is EXACT (joint_exact.py numeric; joint_symbolic.py sympy, residual 0)
For B1658's coupling Y(S, M) (bilinear, 3x3; S the Higgs, M the sector's matter quaternion, both in M2(C)):
- det Y(S, M) = 4 det S det M tr(eps S M^T)      [eps = QJ; an ANTISYMMETRIC pairing: l(M, M) = 0]
- adj Y(S, M) = det S A(M) + det M At(S),  At = diag(1, -1, -1) A   [A quadratic; on null M, A = q~ p~^T (B1658 T1)]
- mirror of T1: on null S, adj Y(S, M) = det M At(S) for EVERY M (2.6e-14).
Why exact: the remainder vanishes on both cones {det S = 0}, {det M = 0} => divisible by det S det M, bidegree (2,2)
=> constant, absorbable (fit rank 19 of 21 = that gauge).
=> the spectrum EXACTLY: sigma^2 are the roots of x^3 - e1 x^2 + e2 x - e3 with
   e1 = ||Y||^2, e2 = ||det S A(M) + det M At(S)||^2, e3 = 16 |det S det M tr(eps S M^T)|^2.
Hierarchical reading: m2/m3 ~ ||d_S A + d_M At||/||Y||^2 (the SUM of the two defects, with interference),
m1 ~ 4|d_S d_M l|/ (m2 m3) (their PRODUCT, times the antisymmetric pairing). One term dominating m2 => m1 ∝ the other's
defect: B1657's conjugate-vacuum law; comparable => B1657's parallel law (sum and product). The joint law unifies both
vacua of B1657, exactly, in B1656's twisted frame, for any Higgs and any matter.
Side facts: the Higgs aligned with the matter (S ∝ M) gives l = 0: the first generation stays massless even with both
defects. On W59's lines the leptons' d_M = 0 (B1656) => m1(lep) = 0 exactly for every Higgs and every L.
Data heuristics (seen): m1 m3/m2^2 = 0.54 (up), 2.69 (down), 0.08 (leptons).

## next: joint_census.py — the inverse map on W59's 18 lines under P4 (one S, log L; 5 targets; CKM read-out)
Then the arc (B1659?): J1 the identities (symbolic), J2 the exact spectrum (numeric on the sector matter), J3 the inverse
map census (a scoreboard), J4 the CKM at the inverse map's solutions (rows vs columns as left: state the convention
FIRST — I-33), controls (a synthetic world the census must recover; a non-W59 line where the leptons lift).

## ~18:20 — identities on B1656's actual sector matter (identity_on_matter.py)
det law 3.7e-17 of ||Y||^3; adj law 1.8e-16 of ||Y||^2 (18 lines x 3 sectors x L in {5, 50, 500} x 3 Higgs).
joint_census.py's "2.5e-01" was a bad yardstick (relative to det Y, which is ~0: the leptons' det M is 1e-15 of ||M||^2).
Quarks' relative matter defect |det M|/||M||^2 runs 1.6e-4 .. 4.4e-2 over L in [5, 500].
First census lines (exploration, Nelder-Mead, 24 starts, 5% floor): chi2 89-93; up fits exactly (3.7e-3 / 7.3e-6),
down m2/m3 ~2x too large (3.8e-2 vs 1.87e-2), leptons' m2/m3 slightly low (4.6e-2 vs 5.9e-2): the leptons' middle mass
comes from the Higgs alone (d_M = 0), so down needs ~3x destructive interference too, while up needs ~16x.

## ~18:50 — the fast census (joint_census2.py: Y = KM @ kron(S, M); trf least squares, 48 starts, seeds 1, 2) running;
positive control (joint_control.py): planted worlds (random near-null S*, L* in [5, 100]) on 3 lines are recovered to
chi2 ~ 1e-26 by the same fitter. Caveat: the planted worlds are less hierarchical than the data. The first census
(Nelder-Mead) was stopped: too slow (10 min a line); its 3 lines gave chi2 89-93.
NaN guard: 2 pi L + c_s must stay > 0 (the gap reaches -5.8); census2 catches such starts (none failed so far).

## ~19:40 — census2 done (2 seeds x 48 trf starts, 18 lines): chi2 >= 131 on every line (5% floor units); the binding
residual is ALWAYS the leptons' m2/m3 (-10 .. -14: predicted ~0.03 against 0.0589); |dS| sits at 0.026-0.043; L 3.8-9.8.
NOT reliable as numbers: Nelder-Mead reached 89 where trf reached 131-154 on the same line; the seeds differ by ~10%.
The planted-world control passed (1e-26) but its worlds were less hierarchical than the data: UNSTABLE as numbers.

### Why (by hand) — the cancellation regime is rigid
- Leptons (D = 0, M null): exactly t + 1/t = ||Y||^2/(2|det S| ||M||^2) => |det S|/||S||^2 in [1/34, 4/34] = [0.029, 0.118].
- Up: m2/m3 ~ ||d_S A(M_u) + D_u At(S)||/||Y_u||^2 must be 0.0037, while the Higgs term alone is >= ~0.015 (T2b range):
  a cancellation of two near-rank-one matrices (A(M) ~ q~ p~^T near the cone; At(S) its mirror) => S's factors aligned
  with M_u's AND |D_u|/||M_u||^2 ~ |d_S|/||S||^2 (fixes L ~ 5-15, as fitted).
- Then down's middle term ~ d_S (A(M_d) - (D_d/D_u) A(M_u)): fixed by the LINE once up cancels; lep's ~ d_S A(M_l).
  => in the cancellation regime S's direction, |d_S| and L are all consumed; down/lep and both m1's are PREDICTIONS
  (no free size) — the naive count (7 params, 5 targets) is wrong; the fits fail on down/lep vs lep's scale.
- Side: S aligned with M_u => l = tr(eps S M_u^T) ~ 0 => up's m1 small: consistent with m_u/m_t ~ 7e-6.
### For the arc (B1659, THE JOINT LAW): J1, J2 identities (symbolic); J3 exact spectrum on the matter; J4 the rigid
cancellation regime as a lemma (state + prove the leading-order alignment); J5 the census = the lemma's no-free-size
predictions per line class against the data (a scoreboard), plus the global fit with a RELIABLE optimiser (the lemma's
reduction gives a low-dimensional search; planted controls IN the data's hierarchy regime, made by perturbing the best
fit). Keep: the electron is 0 on W59's lines (B1656) — the census excludes it and says so.

## ~20:15 — motion (audit/drafts/p177/motion_defect.py): <f> = <|D|/||R||^2> along 224 forward threads (length <= 10):
0.19 (L^9 R) .. 0.80 (LR = m004), median 0.51; ~1/ln(depth) decline. Small relative defects need 1/(2 pi L) (L ~ 5-10).

## ~21:30 — the joint law is NOT B1657's laws in another dress (scope for B1659)
Restricted to (i, j, k) the quaternionic coupling is not a linear image of B1657's Y(a, v) = a v^T + v a^T - (a.v) 1
(fit residual 0.86). Reasons: B1657's Y is symmetric in Higgs and matter, this one is not (At = diag(1,-1,-1) A);
det Y57 = (a.a)(v.v)(a.v) (symmetric pairing) vs det Y = 4 det S det M tr(eps S M^T) (antisymmetric: l(M, M) = 0).
Consequence: Higgs = matter gives GEOMETRIC masses in B1657's frame (the SM seat's identity) but a MASSLESS first
generation here. => B1659 states the twisted frame's own law; "unifies B1657's two vacua" is withdrawn (NOTES ~17:45).
Also (this evening): the optimiser thrash was BLAS oversubscription (load 70-98 on 16 cores): set OMP/VECLIB threads = 1.

## ~22:20 — the first reviewer's blocker B1, verified: the "frames differ" note (~21:30) is WRONG (a labelling artefact)
With N = M eps (M = N eps^-1; det N = det M): Z(S, N) = Y(S, N eps^-1) is symmetric under S <-> N (sympy), and
tr(eps S M^T) = -(det(S+N) - det S - det N): det Y = -4 det S det N polar(S, N) — the SAME form as B1657's (a.a)(v.v)(a.v).
At the coincident point N = S (M = S eps^-1) the masses are EXACTLY GEOMETRIC (m1 m3 = m2^2 to 4e-14; N != S median 0.43):
the twisted frame reproduces the SM seat's identity. S = M (old labelling) is just the zero of polar(S, S eps).
"Not a linear image of B1657's Y" is withdrawn too (the 0.86 fit used the unrelabelled M). Told the owner.
