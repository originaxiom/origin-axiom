# B1465 — THE MIRROR-BROKEN STATES AT THEIR COMPLETE POINTS: NO COUNT FOR ANY CHARACTER, THE MERIDIAN TWIST INCLUDED

**Verdict: PROVED, agreeing with sm:B1527's Part H by a route sharing nothing with it** (scope: frame F-CI, the class
index of SL(2)-tensor modules; object the four mirror-broken word states ±LLRLRR and ±L³RLR² (sm:B1523's first two
pairs) at the parabolic κ = −2 points of their periodic curves, level one; reach *class* for these modules at these
points, silent on the projective (SL(4)) type-one curves, which are the seat's and read). cc (main), 2026-10-03. Pays
R59-1 / L242 (e) as a verification. Design fixed before any run (the scratchpad draft, sha `b22aa96a98fd06fc…`,
`verification/draft_sha.txt`; the arc's script differs in paths and a `--quick` switch).

## 0. Seen first

- **Repo, by sweep.** `topic_sweep.py "mirror-broken|projective (family|deformation|structure)|type-one|meridian
  twist|hyperbolic point of (a|every) word state|Lemma T"`: *VERDICT topic-sweep: 4 of 1337 arcs on main match
  (PROVED 4)* — B1451 (the complete points and their finder), B1455, B1459, B1462; read. B1459 is the theorem this
  arc leans on and extends: it covers fibre characters χ at every doubly parabolic point (ι̃*V ≅ V* ⊗ ε), **not a
  meridian twist λ** — a twist of the meridian by λ turns the identity into ι̃*V ≅ V* ⊗ ε ⊗ λ², so for λ ≠ ±1 nothing
  on main forced the index to vanish. That is what this arc tests. The SM seat's sm:B1527 read at `69693e54`: its
  Part H claims I(ν ⊗ ρ) = I(ν ⊗ Λ²ρ) = 0 at the hyperbolic point for every character ν of H₁, on ten states; its
  type-one curves (Part A, Lemma C) are SL(4) convex-projective and outside main's instruments. **Literature:** none
  beyond the record; the projective four at the hyperbolic point is ρ ⊗ ρ̄ (the SO(3,1) representation of SL(2,ℂ)
  complexified), which is how Part H becomes an SL(2)-tensor statement main can test.

## 1. What was computed

On each of the four states at level one (`mt.Level`, N = 13, 17, 18, 22): every periodic curve ℓ was followed to its
κ = −2 end by B1451's finder (`complete_points.Points.cusp`), and the points whose meridian is parabolic were kept
(12, 12, 14, 20 of 12, 16, 17, 21 curves; the draft recorded only the parabolic ones). At each such point ρ is the
SL(2) rep, ρ̄ its entrywise complex conjugate (a second point of the same level, Galois-conjugate under complex
conjugation), and **V = ρ ⊗ ρ̄ ⊗ χ with meridian λ·(T ⊗ T̄)**, for every fibre character χ ∈ (ℤ/N)² and
**λ ∈ {1, −1, i, e^{2πi/3}, 0.6 + 0.8i, 1.3, 0.7 + 0.4i}** — four roots of unity, a generic unimodular, a generic
real off the circle, a generic complex off the circle. The index by main's instrument (`index_num.index`, B1446), with
its rank gaps.

## 2. Result

| state | N | parabolic points | rows (points × χ × λ) | non-zero | ranks resolved (kept ≥ / dropped ≤) |
|---|---|---|---|---|---|
| +LLRLRR | 13 | 12 | 1 092 | **0** | 8.6e−4 / 4.5e−59 |
| −LLRLRR | 17 | 12 | 1 428 | **0** | 2.2e−4 / 4.0e−59 |
| +L³RLR² | 18 | 14 | 1 764 | **0** | 4.7e−4 / 9.6e−59 |
| −L³RLR² | 22 | 20 | 3 080 | **0** | 1.3e−4 / 1.3e−58 |

**7 364 indices, all zero, no instrument error.** The meridian twist does not open a count at the complete points
of the mirror-broken states, for any of the seven λ, any fibre character, any point. sm:B1527's Part H holds on the
four states main tested, by a different construction (the finder on periodic curves, not the seat's export of the
hyperbolic point; the complex-conjugate pair, not its projective matrices) and a different instrument.

## 3. What it means, and what it does not

With B1459 (λ = 1, a theorem on every once-punctured-torus bundle) and this (λ ≠ 1, computed on the four states), the
reductive SL(2)-tensor modules carry no count at the complete points of the first mirror-broken states either. The
mirror's breaking (sm:B1523) does not by itself make a count — the seat's conclusion, now by two routes. **What is
not tested here:** the type-one projective curves away from the hyperbolic point (the seat's Lemma C, read), and any
non-split module. The record's specification stands: a count needs a non-split module, an open end and a source — the
sourced non-split configuration is the next arc, by the owner's word.

**The instrument's positive control** is on the record, same instrument: I(W₁) = −1 on the non-split module at q₀
(B1453, B1455). No in-arc positive exists for this population, which is the point.

## 4. Errors in this arc

None found at landing. The run was slower than its design assumed (one state took three hours under the suite's load);
the sequential loop was replaced by two parallel runs for the last pair, with a duplicate stopped — no result differs.
