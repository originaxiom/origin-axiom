# B1665 — THE LAYERS, RE-SEALED: the gate failed again, now at D's other zero (ω); the read-outs are B1664's, unchanged

**Verdict: OPEN.** The sealed gate L0 failed, so L1 and L2 are read-outs, not results. B1666 seals the test with a
phase estimator that no zero can spoil. cc (main), 2026-10-16.
- Sealed `043c90b6a` (sha256 9955d1b6). The output was committed unread at `2a0f41394`: one run of 167 s, exit 0, the
  instrument unchanged since the seal (sha256 1c14e0a9).
- **0 of 19.** POINT_REGISTER P-183, steps 1–2.

> *Sharpened 2026-10-17 (Review 65): the sha beside the seal commit is the preregistration's; the instrument's is the first line of ARTIFACT_HASHES.txt. The "1.4 × 10⁻⁸ on all threads" of its diagnosis is the one-period least-squares estimator; B1666's 1.1 × 10⁻⁷ is the two-period estimator it sealed.*

## 0. Seen first

As sealed: `VERDICT topic-sweep /Duke|equidistribut|trace formula|cycle integral|period phase|layer average/: 2 of 1435 arcs on main match (NEGATIVE 1, PROVED 1)`
(B1664's sweep), plus B1664 itself. **Literature:** as B1664 (Bowen, Margulis; Duke; Sarnak; Hejhal; Katok–Sarnak).

## 0b. Disclosed

As the preregistration's §0b: B1664's run and diagnosis seen, a smoke test, and no reviewing agent.

## 1. The run

- **L0 FAILS.** The sizes, finiteness and §8.3b's four coherences hold, but the period-phase error reaches 3.7 × 10⁶.
- **L1** (read-out): 0.3144 over traces 451–600, against 0.3692 at t ≤ 20.
- **L2** (read-out): slope −0.269 ± 0.083 over 7688 phase-1 threads.
- **The cusp family** (read-out): 0.637 (LR), 0.285, 0.717, 0.861, … 0.9923 at word length 54.
- **All read-outs are B1664's,** to 10⁻⁷. The computation is deterministic.

## 2. The diagnosis (post-seal, labelled; `verification/after_the_seal/gate_diagnosis.py`)

- **Where it failed.** The repair started each period at its lowest point in the reduced domain, which lies at the
  corners at ω, where D also vanishes. 22 threads started close enough to ω that the one-point phase ratio divided by
  almost nothing (3.7 × 10⁶ for the worst).
- **The robust phase.** The least-squares phase over a whole period, Σ g(s + ℓ)·conj g(s) / Σ∣g∣², equals
  i^(#L−#R) on **every** one of the 30 674 threads, to 1.4 × 10⁻⁸.
- **The phase claim holds everywhere;** the estimator was fragile at D's two zeros.
- **Main's second instance in a day of the error class it had just filed** (E74, and its stated remedy: try the
  guard's region in the smoke test). This seal had no reviewing agent, which the preregistration said. B1666 has one.

## 3. What it does not show

L1 and L2 as results (B1666), or any Standard Model value.
