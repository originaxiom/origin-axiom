# B375 (PD1.3) — the compilation exists and the protocol is exact

**Status: banked (frontier) + promoted at banking (P58 — exact, locked, the identity-level
verification is machine-checked; the protocol statement is a theorem about the declared
constants). The κ-letter deliverable's in-sandbox half is COMPLETE: the level-15 algebra
compiles into two primitives on four qubits, and the declared interference protocol provably
reproduces the banked seam values. Hardware execution = owner decision, out of scope. The
letter/spirit firewall is stated in `CIRCUIT.md` and governs.**

Verified exactly (`circuit_simulation.py`, all identities in ℚ(ζ₆₀)):
1. ÛF·ÛF† = I — the normalized 15-point DFT ⊕ [1] is exactly unitary (√15 handled exactly).
2. WR̂ = ÛF·D̂⁻¹·ÛF† equals the banked generator — the TWO primitives generate the algebra.
3. The protocol theorem: the declared post-processing of the 240 Hadamard-test amplitudes
   returns the banked pair invariants exactly (flagship + minimal-sector cells checked
   cell-exact against `step0_tables.json`).
4. The κ-word U_κ = D̂·WR̂·D̂⁻¹·WR̂⁻¹ has trace exactly 1 (new exact datum; measurable).

**Provenance.** P56/P57 (the sector + parity/Weyl structure this measures), B358/B367 (the
banked targets), the relayed pricing note (the four-qubit observation, verified here).
Reproducer: `circuit_simulation.py` (~2 min); locks: `tests/test_b375_circuit.py`.
