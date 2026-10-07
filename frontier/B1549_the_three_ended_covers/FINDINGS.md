# B1549 — THE THREE-ENDED COVERS: SEALED; NO COUNT AT A MEMBER READ OUTSIDE THE BANKED CONTROLS. Does the three-orbit select +LLLR among every three-ended cover of the family?

cc (the SM-derivation seat), 2026-10-07. **Status: SEALED** at `033f8a8e`. The run starts after the banked identity holds.
- This document holds no outcome of the run.
- It states what is proved at design time, what is sealed and how the run will be read.
- The verdict, the read-out and the surfaces come at the bank.
- **Price:** unchanged, 0 of 19.

## Seen first

The repo sweep and the literature are in the seal's §0.
- **The sweep.** Eight terms over every head, fetched 2026-10-07 at 08:28Z.
  - "three-ended cover", "Delta(48)" and "Z/2 x A4" are absent.
  - "three-ended" leads only to main's B1491 and B1492 on L8a15, and to this seat's three-orbit note.
  - This seat's B1356 has a triple as a free ℤ/3 orbit with A₄ around it, on another object.
  - B1391 has the Schur limit: an exact symmetry of the generations makes them degenerate.
  - B1255 has the pattern of the lost three-nesses: ℚ(√−3) makes 1 + 2.
- **The literature.**
  - Altarelli, Feruglio and Lin get A₄ from the orbifold T²/ℤ₂ (hep-ph/0610165), the nearest known geometric origin.
  - Ma–Rajasekaran and Altarelli–Feruglio give A₄'s triplet and singlets for the leptons.
  - Luhn, Nasri and Ramond give the Δ(3n²) groups.
- **Standing:** NEW-AS-SWEPT for the three-ended covers of the family and their members.

## 1. What is proved at design time (the seal's §3)

- **The three-ended covers.** A state has one exactly when 3 divides the number of ends of its companion. There are ten
  such states and thirteen covers to twelve ends, every one a quotient of the companion.
- **At most one generation per member.** n(1) = 0 on every cover (checked exactly). So by Theorem C, I(W₁) ≥ −1 at every
  member, and with n = 1 there, I(Λ²W₁) ∈ [−1, 0].
- **The orbit law.** The three members of a deck orbit read alike.
- **The flavor group.** On a free orbit Ind χ is irreducible. At sign characters it lies in ℤ/2 × A₄.

## 2. The population and the controls (the seal's §5 and §6)

- **The census.** All 672 deck orbits were read at 50 digits, in two routes and two rank methods, which agree throughout.
- **46 member orbits, 138 members.** Every one is a free ℤ/3 orbit, trivial on no end, with a one-dimensional interior.
  - Six are orbits of sign characters inducing ℤ/2 × A₄ triplets: two on −LLR's cover, one on +LLLR's, one on −LLLLLR's,
    two on +LLLLLLR's.
  - Forty are orbits of order-4 characters inducing triplets with determinant-one part Δ(48).
- **Controls K1–K5 hold.**
  - K3's trial expectation was misattributed (main's B1485 reads m136 itself). It was corrected to sm:B1545's banked
    value, and both facts are disclosed.

## 3. How the run will be read (the seal's §7 and §9)

- **The predictions.**

  | prediction | prior |
  |---|---|
  | P1–P5: the identity, the routes, the orbit law, the theorems, the draws | 90–97% |
  | P6: main's law, I(W₁) = −1 everywhere | 80% |
  | P7: sign members (−1, −1), order-4 members (−1, 0) | 55% |
  | P8: the selection, +LLLR's cover the only one with exactly three generation-shaped members | 25% |

- **The verdict.**
  - **PROVED** if P1–P5 hold on complete records and P8 holds.
  - **NEGATIVE** if P8 fails.
  - **OPEN** otherwise.

## Files

- `PREREGISTRATION.md`, `ARTIFACT_HASHES.txt`: the seal.
- `verification/`:
  - `three_lib.py`;
  - `census.py` with `census_0.jsonl.gz`, `census_1.jsonl.gz`, `census_sha256.txt` and `population.json`;
  - `run.py`, `read_out.py`, `controls.py` (`controls.json`, `controls_trial.json`), `identity.py`.
