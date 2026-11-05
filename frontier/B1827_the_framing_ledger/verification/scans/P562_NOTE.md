# P-562 — the Higgs's own hypercharge twist (main, 2026-11-03; exploration tier, labelled; data-free)

**What the frame does** (b1656_funcs.py, B1691's correction copy of B1656):
- The matter: for a sector (q_L, q_R) on the line w = αt − b, the bilinear `bil(x, y, u, t)` of the two theta sections with
  characteristics x = twist(q_L w), y = twist(q_R w), over th1(u): a Kronecker-type kernel whose net twist is
  ū = (q_L + q_R) w (−3w for up, +3w for down and leptons). Its four channel residues R_s (s = 1, i, j, k) at the puncture
  include an identity channel R_1 = θ_1-type, nonzero for w ≠ 0 (B1656: R_1(leptons) = θ_1(−9w)).
- The Higgs: an internal 2 × 2 orientation S = a·(QI, QJ, QK), constant on the fibre, built from the UNTWISTED theta triplet
  R(τ) (w = 0) and its Serre derivatives (DR = D R; B1694, B1810). It has no identity channel and no twist.
- So the Yukawa pairs a matter bilinear of net twist ū with an untwisted Higgs. The frame works with local data at the
  puncture (residues, channel norms), where the twist is not an obstruction; a global overlap would need the Higgs to carry −ū.

**The agy lane's point, made precise:** a Higgs twisted like the matter would be built from the residue quaternion at its
twist, R(τ; ū), whose identity channel is θ_1-type at ū and nonzero. θ_1 is odd and ū has opposite signs in the two quark
sectors, so the twisted Higgs's identity channel has OPPOSITE SIGNS in up and down: a0_up = −a0_down, with no free choice.

**Data-free tests, in order:**
1. singlet_higgs_scan.py (same c in both sectors) and singlet_higgs_scan_opposite.py (c up, −c down): whether a singlet at
   its natural magnitude puts the CKM's corners in nature's order with |V_ud| near 1 where up is steeper (audit/drafts/p555/).
2. If the opposite-sign family does: define the twisted Higgs canonically (the residue quaternion of the Higgs's own section
   at ū, or the Serre derivative of R(τ; ū)) — one definition, written before any comparison — and repeat on it.
3. Only then a card (P-555's budget: 3.63 bits of room).

## CORRECTION (main, 2026-11-03, the same evening; found by the framing exercise's reader A4)

**The opposite-sign premise above is WRONG, and P-562 was largely answered before it was raised.** B1744 (THE HIGGS'S OWN
TWIST, P-324; NEGATIVE for its question, data-free parts PROVED) computed the residue quaternion at the Higgs's hypercharge
twist in B1656's frame: it is EVEN, T0(3w) = T0(−3w) to 3.6e-15 (residues(−x, −y) = residues(x, y): the identity channel is
part of a bilinear in which both legs carry the twist, so θ_1's oddness cancels) — so H_u = H_d, the same sign in both
sectors, not opposite; the quaternion is null in four dimensions, so with the scalar channel kept det Y ≡ 0; as a Higgs it
fails the nine (χ²_nine ≥ 493). Main's error: θ_1's oddness applied to one leg instead of the bilinear; and the seen-first
sweep for P-562 did not search "own twist" (B1744's title). What stays untested (B1744's scope): the twisted Serre
derivative in the finite-L four-channel frame; by evenness it is a same-sign singlet, and the same-sign class at natural
magnitude does not lift the corner order (singlet_higgs_scan.py: 2-6% at every phase, median |V_ub|/|V_td| 22-35).
singlet_higgs_scan2.py's opposite-sign family is kept as a class test (is any sector-odd singlet able to lift the corners?),
without the twisted-Higgs motivation.
