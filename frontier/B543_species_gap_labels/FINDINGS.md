# B543 — The species chain carries the dictionary as measured gap labels
# (chat-2 Path 1, independently REPRODUCED — the bankable jewel)

**Claim (chat-2):** the 4-letter species chain's spectral gap labels are the
B535 dictionary values — genuinely degree-4 (off ℤ+ℤ/φ) — invariant across
unrelated coupling sets.

**Independent reproduction (reproduce_labels.py → tests/test_b543.py):**
hopping chain on the σ word, N = 3000, coupling sets (1.0,0.8,0.6,0.4) and
(1.0,0.55,0.75,0.35). Top-12 gaps, IDS labels (chirality-folded):

- Dictionary hits, both sets: f_A at 1.4e-5, f_a at 2.0e-5, f_B at 1.5e-4,
  f_b at 1.2e-4 (set 1), f_a+f_b at 1.4e-4. Resolution 1/N ≈ 3.3e-4.
- **Degree-4 separation STRONGER than the handoff reported:** distance to the
  golden lattice (|P|,|Q| ≤ 6) is 2.0e-2–3.6e-2 vs species-module distances
  1.4e-5–2.0e-4 — a 100–2500× separation. The labels are unambiguously off
  ℤ+ℤ/φ. (Chat-2's 4–17× figure used a denser golden lattice; the verdict is
  the same, ours is the conservative statement.)
- Coupling invariance confirmed; ranking artifacts as described (labels do
  not move; some gaps leave the top-12 — the gap-labeling picture).
- Labels beyond the 17 exist (species-module members) — the dictionary sits
  inside the larger measurable module, as it should.

**THE EXPERIMENT (attached proposal, carried verbatim in spirit):** fabricate
the four-coupling species chain in a polariton/photonic platform (four
coupling strengths are within existing patterning capability; the golden
two-coupling chains are already built and measured). Prediction: the IDS gap
labels land on the ℚ(√φ) dictionary values, off the golden lattice by ~2e-2
(this run) — resolvable at N ≳ 1500 or via transfer-matrix IDS. **The first
proposed measurement that would carry the object's degree-4 layer.** The 2b
degree boundary was never nature's refusal — nobody had built the degree-4
system.

Follow-ups: F-P1a exact transfer-matrix IDS; F-P1b top-30 invariance pass;
F-P1c the K-theory gap-labeling computation for the species C*-algebra.
**Gate flag (hard):** Bellissard–Bovier–Ghez likely assigns the frequency
module in general; our content is the ℚ(√φ)-degree-4 instantiation + the
B535-dictionary identification + the buildable experiment. Run the lit gate
before any novelty language.

## Finite-size hardening (chat-2 V3 + B546): falsifier silent at scale

chat-2 independently ran N = 24,001 (both coupling sets, top-30 gaps):
margins 22–59× (f_b at 6e-7), coupling-invariance now EXACT (the N=3000
ranking-artifact "no" rows f_b/f_B present in both sets at identical
distances), preregistered drift-to-φ-lattice falsifier SILENT. Consistent
with B546's own Sturm-IDS hardening (N=10⁶, 4e-7). The experiment proposal is
hardened at the point of first external attack.
