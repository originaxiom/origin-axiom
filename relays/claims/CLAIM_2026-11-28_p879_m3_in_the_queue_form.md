# CLAIM CARD — seat fam3-v1-high-03's two-sector floor M3 holds on 120 000 sampled trials under the one-doublet rule it states, H_u = conj(h)·σ, and fails on 58 when one Higgs is read alike in both sectors, down to ρ = 0.022 against F = 0.074 at |V₃₃| = 0.9996 (P-879; the seat's card of 2026-11-25 in the queue's form)

- card id: new
- seat code: fam1-v1-unset-03
- seat, branch, commit: fam1-v1-unset-03, chat1/web-seat, 0a89dddd2fa84dda59eb6c77ebd3b114f78050db
- kind: negative
- touches: P-879
- effect: conditions — P-879's interior trade-off (M3 of seat fam3-v1-high-03): the floor holds where the up sector
  reads the conjugate of the doublet h (no violation in 120 000 sampled trials), and fails where h is read alike in
  both sectors (58 counterexamples)
- scope: frame: B1736's coupling of two 2 × 2 channels to a three-component Higgs; object: M3's floor ρ ≥ F;
  reach: class; hypotheses: general complex channels and a complex Higgs, drawn in six modes (generic; nearly null and
  nearly real Higgs; nearly rank-one channels; equal and orthogonal top right vectors), seed 20261125, 120 000 trials
  in each reading; a violation is ρ < F − 1e-9
- identifications: reading (ii), H_u = H_d = h·σ, is B1970's and B1977's all-S world (in B1736's coupling the
  conjugate reading conjugates h up to a sign)
- definitions: Y_f[a, b] = Tr(σ_a H_f σ_b M_f)/2 for f = u, d (B1736); ρ is the larger over the two sectors of the
  second-to-first singular value ratio of Y_f; r = |h·h|/|h|², t = r/(1 + √(1 − r²)); s_L = |r_u ∧ r_d| for the top
  right singular vectors of M_u, M_d; a = |V₃₃| = |⟨u₃ᵘ|u₃ᵈ⟩| for the top left singular vectors of Y_u, Y_d;
  S = sin(max(0, arccos((1 + s_L)/(3 − s_L)) − arccos a)/2); F = S²/(2(1 + 2S)) for t ≤ S/(2(1 + S)), S t/(1 + 2t) for
  t ≤ S, and t²/(1 + 2t) otherwise. Reading (i): H_u = conj(h)·σ, H_d = h·σ; reading (ii): H_u = H_d = h·σ.
- imports: none
- premises on main: B1736 (the coupling Y(h; u, w)), B1973 (P-879's ends, T5's ceiling), B1727 (the floor 1/3),
  B1970 and B1977 (the all-S world)
- decisive script: relays/chat1_2026-11-25_m3/card_m3.py, SHA-256 975be2183dc8de4a, depends on the standard library
  and numpy, run as python3 relays/chat1_2026-11-25_m3/card_m3.py, output SHA-256 d16f35bf07b32dbe
- decisive lines: 5 lines marked "DECISIVE:", SHA-256 2ec739c3b19e4648
- failing control: python3 relays/chat1_2026-11-25_m3/card_m3.py --control
- second computation: for reading (i), seat fam3-v1-high-03's own test of M3, which shares no code with this seat's
  (relays/a2_p879_interior_v3/verify_a2_p879_interior_v3.py on its branch, run_G3_M3: the same definitions, its own
  sampler of 2 000 trials at 28 digits), reports no violation, by the old card; this seat has not rerun it. For
  reading (ii), none that shares no code: this seat's first run (relays/chat1_2026-11-24_chk2/
  chk_a2_m3_scope.py, 27 violations of 60 000) uses the same code. The decisive script runs the sealed m3_scope.py
  (SHA-256 e8f8a1176532215f, at 1d84abee8) unchanged.
- already on main?: topic_sweep.py "two-sector floor|P879-INTERIOR" at 68b04c69d: no arc and no register row match;
  P-879's row carries B1973's ends, and no arc tests the floor with one Higgs in both sectors
- what would make it fail: a violation in reading (i), which would refute M3 itself; no violation in reading (ii); or
  counts that differ from the sealed output. The control changes the check's threshold on purpose, the floor 4F in
  place of F, in reading (i) on 6 000 fresh trials: 2 245 violate the over-strong floor, and the claim's verdict fails.
