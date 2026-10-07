# B1604 — THE CLASS INDEX IS NOT AN INDEX: on a cusped 3-manifold every twisted Euler characteristic vanishes, the stacked instrument's numbers obey that constraint at every module checked across the eight kinds, and the class index is a difference of interior ranks that no characteristic class governs — so the dictionary cannot be earned on a thread or any cover of one, and the earning condition is named

**Verdict: PROVED** (T-NO-INDEX-IN-THREE; standard topology applied to the record's instrument) — E1 holds on five of the six threads and **fails on −LLRLRLRR**, exactly as the reading rule provided for: an instrument error, found — the stacked index at 40 digits is noise on long-relator covers, and the audit it forced withdraws B1602's third carrier and five of B1603's readings (§2b).
cc (main), 2026-10-08. Sealed `12631d402` before the control ran on any thread but −LR. A theorem about the frame, not
about any thread; it rules out a road rather than opening one. No physical quantity. **0 of 19.**

**Credit.** B1496's research for stating what a physical generation count is; the SM seat for the dictionary whose
status this arc settles; B1492 for the instrument whose numbers now carry a consistency control.

## 0. Seen first, and literature

As sealed: `VERDICT topic-sweep /Euler characteristic|chi\(N|index theorem|Chern character|ch_3|shape identity|not an index|Poincar/: 10 of 1376 arcs on main match (NEGATIVE 1, OPEN 1, PROVED 8)`
— B1496, B1487, B1297/B1418, B1603; −LR seen (20 modules, χ = 0). **Literature:** χ(N) = ½χ(∂N) for a compact
3-manifold with boundary; Poincaré–Lefschetz duality with local coefficients; Hirzebruch–Riemann–Roch on a Calabi–Yau
threefold. All standard; the application to the record's class index is this arc's.

## 1. The theorem (as sealed)

**T-NO-INDEX-IN-THREE.** For N the interior of a compact 3-manifold with torus boundary and E any flat module:
(i) χ(N; E) = χ(N, ∂N; E) = rank(E) · χ(N) = 0. (ii) h²(N; E) = dim H¹(N, ∂N; E*) = n(E*) + Σ_i t0_i(E*) − h⁰(E*) and
h³(N; E) = 0, so a0(E) − a1(E) + n(E*) + Σ t0(E*) − a0(E*) = 0 at every module in the stacked instrument's numbers.
(iii) I(E) = n(E) − n(E*) is the interior rank of E in degree one minus its interior rank in degree two: not an Euler
characteristic; no identity I(Λ²E) = f(I(E)) holds (B1603). **Corollary:** the dictionary FK11 cannot be earned by any
index on a thread or a cover of one; a physical generation count needs an even-dimensional object with a non-flat
bundle, or "a generation" means a sector selected by a character — a selection.

Proof of (i): ∂N is a union of tori, χ(∂N) = 0, and for a compact 3-manifold χ(N) = ½χ(∂N); twisted Euler
characteristics equal rank · χ. (ii): the long exact sequence of the pair with coefficients E*, in which H⁰(N; E*) →
⊕ H⁰(T_i; E*) has cokernel of dimension Σ t0_i(E*) − h⁰(E*) (injective for a connected N with the character
non-trivial somewhere, and in general of rank h⁰(E*)) and H¹(N, ∂N; E*) → H¹(N; E*) has image the interior classes
n(E*); H⁰(N, ∂N; E*) = 0; duality H^k(N; E) ≅ H^{3−k}(N, ∂N; E*)^∨. (iii): the same duality applied to n(E*). □

## 2. The control (`euler.py`; six threads, 196 modules)

| | sealed prediction | prior | result |
|---|---|---|---|
| **E1** | χ = 0 at every module on +LR, ±LLR, −LLLLRR, −LLRLRLRR, +LLLLLLRR | 95% | **HOLDS on five threads, 176 modules** (+LR 68, +LLR 36, −LLR 36, −LLLLRR 16, +LLLLLLRR 20: χ = 0 at every one); **FAILS on −LLRLRLRR**: 15 of its 18 modules give χ ∈ {−5, −3, −2, −1} — the instrument's h¹ there is overestimated by two or three |
| **E2** | the ranks mutually consistent (no negative h², no non-integral χ) | 95% | **HOLDS** on the five; the sixth is E1's failure |

With −LR's 20 (seen), 196 modules on six clean covers obey the constraint — the first consistency control the stacked
index has had — and the seventh cover does not.

### 2b. The catch, and the audit it forced (`audit_precision.py`, `tiers.json`; post-seal, disclosed)

On −LLRLRLRR's forced cover SnapPy's presentation has relators of 720–902 letters, and the four's relator residual
max |four(r) − I| at B1492's 40 digits is **6 × 10²**: the Fox matrices there are noise, and the singular values of
10⁻⁶…10⁻¹³ the instrument read as rank deficiency are not structure (on +LR's cover the residual is 10⁻³⁹ and the
spectrum's gap spans 37 orders). The audit over all 148 forced kernels of B1602's census, by the same residual (the sign
of SnapPy's SL(2, ℂ) lift cancels in the four; the bare SL(2) residual of 2.83 = ‖−2I‖ on many covers is that sign, not
a loss): **89 reliable** (< 10⁻²⁸), **28 marginal** (10⁻²⁸ to 10⁻²⁴, ranks probably right, not guaranteed), **31
unreliable** (≥ 10⁻²⁴, the ranks not established) — every length-eight odd-trace cover among the last, with −LLLRLR,
±LLRLRR and +LLLRLLR. The instrument's validity condition is now stated (B1492's addendum): the four's relator residual
must sit well below the rank tolerance. Consequences, written as addenda on the arcs: **B1602's third odd-trace
carrier is withdrawn** (an artifact); its T2 is undetermined at 40 digits, not failed; its T1 holds where readable;
its even-trace results stand on the reliable covers (32 carriers among 81). **B1603's (1, 0) and (3, 1) kinds are
withdrawn** with +LLLLLLR's six on its second kernel; on reliable covers the generation shape has **116** readings (+LR
24; ±LLR, ±LLLLR, ±LLRR 12 each; −LLLLLLR 4, −LLLLRR 8, +LLLLLLRR 8) and the kinds are **six**: (−1, −2), (−1, −1),
(0, −1), (0, −2), (2, −2), (0, −3). The seat's census at 160 digits stands where main's is undetermined. The re-read of
the 31 unreliable covers at high precision (polished holonomy) is the next arc.

## 3. What it says

- **Why eight kinds.** The physical count χ(X, V) = ∫ch₃(V) on a threefold is governed by the Chern character, which
  forces n_5̄ = n_10 at rank five. The class index on a 3-manifold is governed by nothing of the sort: it is a signed
  count of interior classes in two degrees, and the readings (−1, −2), (0, −1), (2, −2), (+3, +1), … are not
  violations of an identity — there is no identity to violate.
- **FK11 is unearnable where the record reads.** No count of flat-module cohomology on any thread or cover of a
  thread is an index. "Generation-shaped" stays a label; three in F-HE or F-CI is a selection — THE_BAR's baseline, now
  a theorem.
- **The earning condition.** A derivation of three generations in this programme needs a count that *is* an index:
  an even-dimensional object the weave forces, carrying a non-flat bundle, with the count its index — or an honest
  orbifold reading in which a generation is a sector selected by a character and the number of sectors is forced by
  the weave (the three parities, W1/W4) while the content per sector is what a thread's cover carries (B1603). The
  second is what the record has; what it lacks is the rule internal to the genesis that selects the thread (B1602).

## 4. Disclosed

- The control rebuilds each forced cover exactly as B1602 did and reads the dual's numbers by the same instrument;
  numerical ranks at 40 digits; the first kernel only on threads with several (the constraint is per module).
- The theorem is standard; nothing here is new mathematics beyond its application to the record's instrument.
- The audit (§2b) was written after the control failed; its criterion (the four's residual against the rank tolerance) is the natural one and was not tuned to any result; the tiers' thresholds (10⁻²⁸, 10⁻²⁴) are stated, the marginal band kept separate.
- Not blind to B1603 or to −LR.

## 5. Files

`verification/euler.py` (sealed), the seven `euler_<thread>.json`, `euler_run.txt`; `audit_precision.py` (post-seal), the 74
`audit_<thread>.json`, `tiers.json`; `adoption/amend.py` (GENESIS v1.27). Test: `tests/test_b1604_the_class_index_is_not_an_index.py`.
