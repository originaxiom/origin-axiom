# B1737 — THE SLOPE IS A ZETA VALUE (P-311): THE SLOPE LAW'S s(χ) IS THE χ-TWISTED SHINTANI ZETA VALUE AT s = 0 OF ℤ² MODULO THE MONODROMY (SCZECH'S EISENSTEIN COCYCLE AT THE TORSION POINT), LESS ½·#(−I); THE TRIVIAL CHARACTER GIVES −Ψ/12 (RADEMACHER) — B1623'S "RELATED, NOT THE SAME" BECOMES AN IDENTITY

**Verdict: PROVED** (an identity verified exactly to 2.5 × 10⁻¹³ on all 601 non-trivial monodromy-fixed characters at
16 levels, with main's exact slopes; the general proof is sketched in §3, not written in full). cc (main), 2026-10-23.
No data. **0 of 19.**

## 0. Why

The parked-items sweep (L233 (b), P-311, QUEUE item 2): its reader found numerically, in scratch, that B1438's slope
s(χ) equals the χ-twisted Shintani zeta value at s = 0, and that the trivial character gives Rademacher's −Ψ/12.
B1623 had graded T-SLOPE-LAW "related, not the same" as the Dedekind–Rademacher and Meyer functions. This arc checks
the identity on main with main's own instruments: the exact slopes (B1438's `exact_slopes`, cyclotomic arithmetic, not
the letter formula the reader used) against an independent cone computation.

## Seen first

`VERDICT topic-sweep /Shintani|Sczech|Eisenstein cocycle|Rademacher|Meyer'?s|Dedekind sum|zeta value at s ?= ?0|twisted zeta/ (full text): 3 of 1510 arcs on main match (NEGATIVE 1, PROVED 2)`.

Bearing on it: B1438 (the slope law), B1623 (its literature grading, which this corrects). **Literature** (from memory,
not fetched): T. Shintani, *On evaluation of zeta functions of totally real algebraic number fields at non-positive
integers*, J. Fac. Sci. Univ. Tokyo 23 (1976); R. Sczech's Eisenstein cocycle (*Eisenstein group cocycles for GL_n and
values of L-functions*, Invent. Math. 113 (1993)); C. Meyer's ζ(0) for real quadratic orders; H. Rademacher and E.
Grosswald, *Dedekind Sums* (1972), for Φ and Ψ.

## Disclosed

- The reader's scratch (audit/drafts/leads_reeval/L233.md, its code reproduced there) was read first, and its method
  for the cone value (a half-open fundamental parallelogram of the positive cone) is used. The code here is main's own:
  the abelianised monodromy from B1438's `Phi_of`, an exact enumeration of the parallelogram, and B1438's exact slopes.
- The same script was run once in the audit room; the recorded run is its rerun from this folder.

## 1. The identity (part A)

For a level of a signed word state, M the monodromy's action on H₁ of the fibre (the columns the abelianised images of
x, y), χ = (i, j) mod N a non-trivial character fixed by M, and C the positive cone of M's eigen-covectors:

  **s(χ) = Z(0, χ) − ½·#(−I),   Z(0, χ) = Σ_{p ∈ Π(w, w′)} χ(p) / (1 − χ(w))²**

with Π the half-open parallelogram {t₁w + t₂w′ : 0 < t₁ ≤ 1, 0 ≤ t₂ < 1}, w′ = gen·w, gen = M when its eigenvalues are
positive and M² (the value halved per generator) when they are negative, and #(−I) the number of −I letters in the
level's word (k for a − state at level k, 0 for a + state).

- **All 601 characters** at +LR levels 2–5, +LLR 3, +LLLR 3, +LLRLR 2, −LR levels 1–4, −LLRLR 1, −LLLRLR 1, −LLR 2
  and 3, −LLRR 1: **max ∣s − (Z − ½#(−I))∣ = 2.5 × 10⁻¹³**.
- **Control (part B):** Z at two different w agrees to 3.3 × 10⁻¹³.
- The constant ½#(−I) is the same for every character of a level, so B1438's "only differences of slopes carry
  content" is untouched.

## 2. The trivial character (part C)

Shintani's constant-term value on C modulo ⟨gen⟩ equals **−Ψ(M)/12** with Rademacher's Ψ = Φ − 3·sign(c(a + d)) on all
16 levels (to 3.5 × 10⁻¹¹): 0 on every LR level (Ψ(LR) = 0), −1/4 (+LLR 3, −LLR 3), −1/2 (+LLLR 3), −1/6 (+LLRLR 2,
−LLLRLR 1, −LLR 2), −1/12 (−LLRLR 1), 0 (−LLRR 1).

## 3. The mechanism (sketch, not a written proof)

B1438's R-letter term −X/((X − 1)(X′ − 1)) is the generating function of the half-open unimodular cone (e₁, e₁ + e₂) at
z = 0; the orbit sum is a cone decomposition of the fundamental domain along the word's Farey path, the L letters
contributing 0 in the gauge σ(x) = 0, and B1438 D's telescoping imaginary parts are the cones' boundary terms. So the
letter cocycle is Shintani's cone cocycle — Sczech's Eisenstein cocycle on SL(2, ℤ) ⋉ (ℚ/ℤ)² — whose v = 0 member is
Rademacher's Φ (Meyer's ζ(0)). Writing this out in full is owed; the identity above does not rest on it.

## 4. What it means

- **The slope law, Rademacher's Φ and Meyer's ζ(0) are one Eisenstein cocycle**, at the torsion point χ and at 0.
  B1623's "related, not the same" is corrected by a dated note: the slope is the χ-twisted member of that family.
- **The follow-on (registered, not computed):** whether B1656's channel norms c_s are Kronecker-limit logs of the same
  L-function per (thread, line), −2π ln∣θ[v](0)∣² plus a τ-only term. If so, the slope and the channel norms are two
  coefficients of one L-function, a candidate rule for the line (P-312, C1). Data-free; any data comparison sealed.

## Files

- `verification/the_slope_is_a_zeta_value.py` → `the_slope_is_a_zeta_value.json`, `the_slope_is_a_zeta_value_run.txt`.
- The lock: `tests/test_b1737_the_slope_is_a_zeta_value.py`.
