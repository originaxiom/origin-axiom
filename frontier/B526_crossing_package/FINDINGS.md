# B526 — Verification of the "UNDENIABLE PHYSICS CROSSING" package (owner upload, 2026-07-12)

**What arrived.** A package titled `UNDENIABLE_PHYSICS_CROSSING_PACKAGE.zip` (5 files: a path document, a
handoff, a prereg yaml, a reproducer, a test). Extracted to quarantine, read in full, and every load-bearing
claim **independently recomputed** (numerical eigenvalues, from-scratch code — not by re-running their
symbolic script). Firewalled; nothing to `CLAIMS.md`.

## Headline: the title is a misnomer — the content is the OPPOSITE of a crossing claim
The document's own executive conclusion (its line 12): *"There is no remaining purely internal path from the
Origin Axiom corpus to an undeniable claim about nature."* Its prereg sets `claim_level: structure_only`,
`claims_md: forbidden`, and defines a crossing as requiring the **external blind test** (gates P0–P6 ending in
independent measurement). **So it REINFORCES the master negative (PHYS-REFUTED), it does not overturn it.** It
is a research-direction verdict + two new structural results + a reframing. The alarmist filename is not the
content; the content is disciplined and firewall-consistent.

## The two technical results — INDEPENDENTLY VERIFIED (`independent_verify.py`)
On the B517/B524 abelianization M = [[1,1,1,1],[1,0,1,0],[2,1,1,1],[1,1,1,0]] (charpoly x⁴−2x³−5x²−4x−1,
det −1, Perron r = (φ,1,φ√φ,√φ), β = φ(1+√φ)):

1. **The canonical tetrahedral spatial metric** S_tet = D_r⁻¹(I − ¼𝟙𝟙ᵀ)D_r⁻¹ (D_r = diag r): rank **3**,
   **S_tet·r = 0**, and the weighted directions dᵢ = rᵢeᵢ have Gram = the regular tetrahedron (¾ diagonal,
   −¼ off). *Verified.* **Honest reading:** the Gram-match is essentially *by construction* (dᵢᵀS_tet dⱼ =
   C_ij algebraically); the elegant part is that D_r⁻¹r = 𝟙 and C𝟙 = 0, so the kernel is exactly the time-line
   r. And the tetrahedral isotropy is an **imposed** demand (the object does *not* force the four letters to
   be equivalent — the substitution treats them asymmetrically) — the document says so ("a selection principle
   the symbolic symmetry group could not provide"). So: canonical *conditional on* an isotropy assumption, not
   object-forced.

2. **The isotropy–Stein no-go** (the genuinely non-trivial result). With ℓ the left Perron covector (ℓᵀr=1),
   G_iso = S_tet − ℓℓᵀ has **signature (3,1)** (r timelike, G_iso(r,r)=−1); and
   **W_iso = G_iso − MᵀG_isoM is NOT positive definite** (signature (3,1)), with the obstruction already on
   the spatial stable space E_s = ker ℓᵀ (W_stable signature (2,1), det < 0). *Verified via eigenvalues,
   independent of their leading-minor method.* ⟹ **M cannot be both the locally-isotropic propagation law and
   a positive one-step Stein (dissipative-time) evolution.**
   - **Adversarial check — is this just "β>1 restated"? No.** W_iso(r,r) = +12.5 > 0, so the *expanding*
     direction is fine — the negativity is not from β>1. M restricted to E_s is *spectrally contracting* (all
     |eig| = 0.786, 0.786, 0.44 < 1), yet W_stable is indefinite. The obstruction is **non-normality**
     (transient growth of a non-normal contraction), a genuine phenomenon — not automatic. The no-go is real.
   - **Caveat:** G_iso's (3,1) is again the *generic* 2-real-1-complex signature (cf. B517 SIGNATURE_HUNT,
     B523 C3) — real but not object-forced. The new content is the *incompatibility with a positive Stein
     driver for the canonical isotropic metric*, not the signature.

3. **Exact RG correction exponents** (from the spectrum, verified to 15 digits): ω_h = 0.6303718738…,
   ω_γ = 0.1848140631…, log-frequency Ω = 1.9013667683…, scale ratio exp(2π/Ω) = **27.23662275649545…**. The
   document correctly flags these as **not yet physical** — no observable with a *proved* nonzero coupling to
   the mode has been specified, so absence of the oscillation would not falsify anything. Exact structure, not
   a prediction.

## The reframing (firewalled hypothesis, not a theorem)
The no-go motivates: **M_* = renormalization / inflation** (scale, hierarchy, correction exponents), and
**physical time = a separate local unitary / QCA** (Hilbert space, one-step unitary, finite propagation). This
is a reasonable architecture, but it is an *interpretation* the no-go permits, not one it forces — the no-go
rules out M_* as positive-Stein isotropic time; it does not prove M_* *is* renormalization. Held behind the
firewall. The forward program (P0–P6: exact Rauzy contact complex → classify substitution-covariant local
unitaries → continuum/RG theorem → frozen dimensionless prediction → controls → blind external test) is a
genuine, well-gated plan — and its terminal arrow is external, exactly as the firewall requires.

## Disposition
- **Math: CORRECT** (independently verified — tetrahedral metric, the no-go signatures, the RG exponents).
- **Framing: HONEST and firewall-consistent** (structure-only; the "no internal crossing" verdict SUPPORTS
  PHYS-REFUTED). The title oversells; the substance does not.
- **Banked as STRUCTURE:** the tetrahedral metric (conditional on imposed isotropy) + the non-normal
  isotropy–Stein no-go + the exact RG exponents (not-yet-physical). No crossing; no B398 event; the firewall
  is untouched. This is a third independent arrival at the program's negative, with new supporting structure.
- Lock `tests/test_b526.py`. Reproducers: `physics_crossing_reproducer.py` (theirs), `independent_verify.py`
  (this trunk's from-scratch recomputation). Cross-refs: [[B517]] (Perron r, Stein), [[B523]] (C3 cone),
  [[B524]] (the F₄ automorphism, β), docs/CLOSURE_2026-07-11 (PHYS-REFUTED, which this supports).
