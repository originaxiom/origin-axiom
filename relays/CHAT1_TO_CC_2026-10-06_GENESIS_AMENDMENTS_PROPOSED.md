# HANDOFF — proposed amendments to GENESIS v1.11, from the web seat (chat1)
### 2026-10-06. Proposals only: nothing committed to main. GENESIS is amended by an arc (§0); these are inputs to one.
### Read against `GENESIS.md` at main, v1.11 (2026-10-04).

Each proposal names the item, the change, the status the evidence supports, and the evidence. Sealing first is cc's call.

---

## A1 — GAP6's remedy: "a frame with curvature" is necessary, not sufficient

**Item:** §7 GAP6, last sentence ("The remedy for this one is a frame with curvature; none is on the record").
**Proposed addition:** *A smooth closed bulk gives ind(V) ≠ ind(V̄) only in dimension ≡ 2 (mod 4).* The Dirac index is
∫Â·ch(V); Â has components only in degrees 0, 4, 8, …, ch_k sits in degree 2k, and ch_k(V̄) = (−1)^k ch_k(V). In
dimension n only the k with n − 2k ≡ 0 (mod 4) contribute, and odd k occur exactly when n ≡ 2 (mod 4). So in
dimension 4 only ch₀ and ch₂ enter, both conjugation-even: **ind(27) = ind(27̄) on a 4d bulk, curved or not.**
**Status:** DERIVED (textbook: why K3 compactifications are non-chiral and Calabi–Yau threefolds chiral).
**Consequence for the frames:** a 4d curved bulk is not a remedy; a 7d G₂ bulk is odd (chirality only at singular
points — F-AP's setting); the six-dimensional frame bundle Γ\PSL(2,ℂ) of a closed filling is the natural candidate of the
right parity (its rational cohomology is (1,0,0,2,0,0,1), so N_gen = ∫c₃/2 there; no published admissible bundle with
c₃ ≠ 0 found).
**Evidence:** `chat1_HANDOFF_ROBUSTNESS.zip` → `code/v03_parity_rule.py`.

## A2 — GAP6's value sentence, scoped in the other direction

**Item:** §7 GAP6: "the flat frame … cannot reach CONTINUOUS values (a mass, a coupling)."
**Problem:** read literally it now over-reaches the other way. The rigid geometric point is in the flat sector and is
not a modulus, and it fixes continuous numbers exactly.
**Proposed wording:** *cannot reach continuous MODULI; rigid flat invariants are fixed.*
**Status:** COMPUTED (known mathematics; scope: the root only — m004 is the one word state that is a knot complement).
**Evidence** (`chat1_HANDOFF_ARITHMETIC_ATOM.zip` → `code/v08`): the figure-eight's Kashaev invariant, fitted from data
to N = 1600 and not assumed — prefactor 0.759835685622931 against 3^(−1/4) (11 digits); first correction
0.554216604118 against 11π/(36√3) (7 digits); exponent vol(m004) = 12·√3·L(2,χ₋₃)/8. Garoufalidis–Zagier quantum
modularity; the fit confirms, does not discover. m003 has H₁ = ℤ ⊕ ℤ/5, so no Kashaev invariant.

## A3 — "the family" needs one referent (proposed glossary rule under §6)

**Item:** §1 ("The family is the intended shape") and §6 scope tags.
**Problem, measured today:** at least five sets are called "the family" in the record and the seats' reports —
X_gen's word states (§3), m004's commensurability class (99), B1186's 112, the regular-tetrahedral class, and the seven
amphichiral members of B1474/B1475. A statement true on one is false on another. **Measured on X_gen to word length 8
(74 hyperbolic realisations, cyclic words up to swap, reverses unmerged):** 2 are regular-tetrahedral (+LR, −LR);
Chern–Simons is irrational on 56 and rational on 18, with denominators {1, 2, 4, 48}; the 16 amphichiral states have
CS ∈ {0, ¼}. **On the regular-tetrahedral class** (all 16 in the first 6000 census manifolds): CS rational on 16 of 16,
every denominator dividing 24. The web seat's "1/24 lattice", "the family's quantum partition function" and "the
arithmetic atom" readings (ARITHMETIC_ATOM §3–§5) are statements about the tetrahedral class; on X_gen they hold at the
root and its twin only.
**Proposed rule:** the bare phrase "the family" is not used; the scope tag's `object` names the set (X_gen to length n,
the commensurability class, the tetrahedral class, a named list). The owner's rule "the family is the object" is read
with GENESIS §1's family, X_gen.
**Status:** a rule (the glossary's own reason: ambiguity in a term has produced errors — here twice in one day).
**Evidence:** reproduce with the inline script in this handoff's companion message (SnapPy `b++w` = +w, `b+-w` = −w).

## A4 — the extra U(1) is two objects; name them apart

**Item:** §5 F-MC (run on the root only) and the record's Z′ arcs.
**Problem:** the paper's Y₃ closing leaves SM × U(1)′ with U(1)′ **the η direction, family-universal**; sm:B1283 and
sm:B1303's closing leaves SM × U(1)_Z′ with Z′ = (5ψ − 3χ)/2 **plus a family part (−10, 5, 5), family-non-universal**,
with the VEV'd generation's N and ν^c exactly neutral. Both share the E₆ part (charges 4/−2/10/−8/−2 per 27, reproduced
independently from the branching). They give opposite answers on Majorana neutrinos: on the paper's closing every ν^c has
η = −20 and a ν^cν^c mass needs charge +40, absent from 27, 27̄ and 78 (verified); on sm:B1303's closing the VEV'd
generation's ν^c is neutral and nothing in the Z′ forbids its Majorana mass.
**Proposed:** distinct IDs for the two U(1)s, and both entered under F-MC's "computed nowhere yet" as root-only (F-MC
has never run on another word state, so the existence of either Z′ is not a family statement).
**Status:** COMPUTED (charges, anomaly freedom Σq = Σq³ = 0 on one 27, the no-+40 census).

## A5 — two root-only results to list under "Computed nowhere yet"

- **Dark-matter stability** (memo 122, NEGATIVE): tested the root's forced gauge 2-torsion only. On other word states
  the symmetry group differs, so the negative does not reach them by its own scope tag.
- **Dirac against Majorana:** decided by the residual discrete symmetry after the Z′ is broken (sm:B1303: radiatively),
  which no arc computes.

---

## Corrections to the web seat's own statements of today (so they are not carried)
- "On the seven swap members … CS non-zero (m202 1/12, s959 1/3)": **wrong.** The seven are amphichiral word states
  (CS ∈ {0, ¼}); m202 and s959 are two-cusped and not word states. What B1474/B1475 give is the mirror acting genuinely
  on the spin structure there — a fermionic, not a CS-phase, statement.
- "The SM lane found the same U(1)" — two different U(1)s (A4).
- "Dirac neutrinos while U(1)_η is unbroken" — a prediction inside a regime excluded by a massless Z′; the decisive
  quantity is the residual discrete symmetry (A5).
- "B1166 verified a dilaton" — B1166's C3 is one ℝ₊ of scalings; whether it is a field (a fifth-force mediator,
  bounded by Eöt-Wash and Cassini) or a unit is open, and should be read from the gravity charter before it is tested.
