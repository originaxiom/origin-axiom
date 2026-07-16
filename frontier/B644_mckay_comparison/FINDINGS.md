# B644 — THE EAR IS THE MOD-5 CONGRUENCE SHADOW (L94 closed)

**Claim (verification strength, elementwise).** On ker(det) ≅ 2I of the
hearing group (B640), the θ-odd hearing representation FACTORS through
literal reduction mod 5:

> **ρ_hear = χ_golden ∘ (mod-5 reduction)** — where mod-5 reduction is
> R ↦ [[1,1],[0,1]], L ↦ [[1,0],[1,1]] over 𝔽₅ (closing to SL(2,𝔽₅),
> order 120), and χ_golden is ONE of the two Galois-conjugate 2-dim
> irreducible characters of SL(2,𝔽₅) ≅ 2I.

The ear at the minimal bearing stage κ = 5 hears the infinite Anosov
monodromy through its congruence shadow **at the conductor**: the
conductor is the modulus of the ear.

Prereg `PREREGISTRATION.md` (sha256 b77e5bdf, sealed first); run
`b644_mckay.py` (4b7e4881) → `b644_output.txt`; the character addendum
`b644_character_check.py` (exact sympy).

## The gates

| gate | sealed criterion | outcome |
|---|---|---|
| M1 | ⟨R₅,L₅⟩ = SL(2,𝔽₅), order 120 | **PASS** (120) |
| M2 | kernel match: ρ_hear(w) scalar ⟺ mod5(w) = ±I, 360 canonical + 200 seeded random | **PASS** (0/560 mismatches) |
| M3 | class-function factorization: tr ρ_hear constant on mod-5 classes; matches one golden table | **factorization PASS** (well-defined on all 120); table clause see adjudication |
| M4 | the cat map RL: mod-5 class value = −1/φ = tr ρ_hear(RL) | **PASS** (class (10, QR); 25 digits) |

## The M3 adjudication (a sealing error, disclosed per MB12)

The prereg's two reference tables were both internally INCONSISTENT as
characters: they violated χ(−g) = −χ(g) on the order-10 rows (order-10
elements are −(order-5 unipotents); the sealed tables paired
(5,True)→1/φ with (10,True)→+φ, which no 2-dim faithful character can
satisfy). As written, the table-match clause could never pass for ANY
genuine irrep — the vacuity class MB12 exists to catch, caught here
post-run. The factorization CONTENT of M3 (the discriminating fact:
tr ρ_hear is a well-defined function of the mod-5 class) passed as
sealed. The observed table was then verified to be a genuine golden
character by exact class arithmetic (`b644_character_check.py`):

- class sizes from the actual group: 1, 1, 30, 20, 20, 12, 12, 12, 12
  (sum 120);
- χ(−g) = −χ(g) on every paired class: exact;
- Schur: ⟨χ,χ⟩ = 1 — irreducible;
- every value = 2cos(kπ/5) exactly: (10,T)→−1/φ, (10,F)→+φ,
  (5,T)→+1/φ, (5,F)→−φ, plus 2, −2, 0, ±1.

So the corrected statement of M3 holds with the table that is forced by
character theory; nothing about the object was adjusted — only the
prereg's transcription of the reference table.

## What this closes and upgrades

1. **L94 CLOSED.** The dual-McKay D-row's ear placement upgrades from
   PLACEMENT to DERIVED: B206/B210's congruence-McKay 2I (monodromy
   arithmetic at the ramified prime 5) and B640's hearing 2I are **the
   same homomorphism** on ker(det), not merely isomorphic images.
2. **The B210 reconciliation (standing obligation).** B210's banked
   resolved-negative — "the WRT modular-rep image at the golden level
   is not 2I" — concerned the SU(2)₃ FULL modular image (order 2880,
   congruence level 20). B644's operator is the SU(3)₂ θ-ODD-PLANE
   image (level 15). Different stage, different plane: B210 stands, and
   B644 locates WHERE the congruence shadow is realized — the θ-odd
   plane of the κ = 5 stage, not the full WRT space.
3. **The order reconciliation gains its mechanism.** ρ(RL) has order 10
   because the cat map mod 5 has order 10 in SL(2,𝔽₅) (class (10, QR));
   the mirror twist M_odd = −ρ is literally −I in the congruence shadow.
4. **B642's Galois ear is now derived, not just observed.** The two
   2-dim irreps of SL(2,𝔽₅) are the two Galois conjugates (√5 ↦ −√5);
   the k = 7 stage twist picks the other one (+φ on RL). K020-in-the-ear
   is exactly "which of the two characters of the SAME shadow the stage
   selects."
5. **The κ-gating law connects.** 5 | κ (B620/B621) gates the hearing
   field; B644 says WHY the golden values appear: the ear's arithmetic
   IS arithmetic mod the conductor.

## Honest status

All verification internal (owner + AI seats). The ingredients are
classical (congruence quotients of SL(2,ℤ); Ng–Schauenburg gives the
level); the identification of the θ-odd hearing with the golden irrep
of the mod-5 shadow, and its role as "the conductor is the ear's
modulus," is the program's assembly — **novelty NEEDS-SPECIALIST**
(prior-art not run; do not claim). No SM numbers; Gate 5 untouched;
no physics reading (L91 stands).

## Reproduction

- `python3 b644_mckay.py` (pyenv; ~2 min, 60 dps) → `b644_output.txt`
- `python3 b644_character_check.py` — the exact character arithmetic.
- `tests/test_b644_mckay.py` — the locks.
