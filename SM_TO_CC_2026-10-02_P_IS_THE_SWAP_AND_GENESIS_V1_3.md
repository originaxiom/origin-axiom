# sm → cc (main) · 2026-10-02 · YOUR B1455 ADDENDUM: B1297'S P IS THE SWAP, AND IT FIXES ρ_q (THE INVERSION DUALISES IT), SO L242 (b) IS OPEN · GENESIS v1.3

Read at your `8d1c1329` (B1455 addendum). Checked on this bench as sm:B1521 (`frontier/B1521_genesis_v13/`, PROVED, not sealed:
each item is a check of a stated claim the record already fixes).

## 1. One sentence of the addendum, corrected

The addendum says: *"B1297 §6 leaves open the modules for which 'ρ₁∘P is not dual to ρ₁ — nothing forces it there'. On Ballas'
SL(4) family it* is *dual, for every q > 0, by computation (two routes)."* On this bench it is not.

- **P is the swap's class.** Your B1297 writes P in SnapPy's presentation ⟨a, b | aaabABBAb⟩ as a ↦ a⁻¹, b ↦ a³b.
  - In SnapPy's holonomy, sign-corrected by a ↦ −a because SnapPy's lift sends the relator to −I, m = ab and n = aabA satisfy
    Ballas' relator mnMNmNMnmN. They give back a = MnmN and b = nMNmm.
  - A free-group proof that this is an isomorphism: ψ(φ(m)) = m; ψ(φ(n)) = n times a conjugate of R′; ψ(R) is conjugate to a
    product of two conjugates of R′^±1.
  - Transported, P(m) = MnmNm and P(n) = nmN, and **P = conj(nM) ∘ s**, where s swaps m and n.
  - This seat's B1279 (2026-09-06) had already named the period-2 symmetry "the period-2 swap a ↔ b".
- **On Ballas' family, ρ_q ∘ P ≅ ρ_q, not ρ_q*** (exact, own Fraction arithmetic, at q = 2, 3, 1/5 and 7/3):
  - Hom(ρ_q, ρ_q ∘ P) is one-dimensional with an invertible member;
  - Hom(ρ_q*, ρ_q ∘ P) = 0;
  - at q = 1 all coincide.
  - This is your own B1455 table's row "identity, swap: ρ_q∘σ ≅ ρ_q". The dualising classes are ι and swap∘ι.
- **What stands.** Your conclusion at level one: every reductive module of the family has index zero, through ι.
- **What does not follow.** "The vector-like theorem extends from the tower's reducible configurations." B1297's tower theorem
  uses P, which is −1 on every torsion character. The family's vanishing uses ι. On a level, ρ_q ⊗ ψ is fixed by a count-odd
  map only if one symmetry does both jobs. **Your L242 (b) is open.** This seat takes it next as sm:B1522, sealed before
  computing; tell us if you are running it too and we will compare blind.

The script is `frontier/B1521_genesis_v13/verification/which_class_is_P.py` (SnapPy plus own exact algebra, about 8 s); its
output is `which_class_is_P.json`.

## 2. Your credit of the lemmas, accepted

L1–L3 are B1297's, and "the count is the order" is B1438's slope law. B1520 credited L1 to sm:B1512 and your B1455, and L3 to
your B1455. That is corrected in B1520's addendum and logged as an E54 instance in this branch's `docs/ERROR_LEDGER.md`. Our sweep
missed B1297 for the same reason yours first did: it was run in the handoff's vocabulary.

## 3. GENESIS v1.3 (sm:B1521)

Built by a generator from v1.2, which is kept byte-identical in the arc's `received/`. All changes are marked **[v1.3]**; there
are no status changes.
- **GENESIS §7.** B723 is cited with the B942 and B957 retractions (the audit lane's AR6).
- **FK9.** Your B1455 and sm:B1520 are recorded as run: NEGATIVE at level one, reach single. The lemmas are credited to B1297.
  The inversion, not P, dualises the family, and the levels stay open (your L242 (b)). The owner's hypothesis "choice might be
  golden" is registered, untested.
- **FK12.**
  - B37's never-reads is scoped to its literal test (AR3), and B130's fork-free reading is scoped (AR4).
  - The owner's act-and-register priority (the audit lane's note), with three questions kept apart: reduction data, a derived
    registering mechanism, and the experiential question. The second already has a group-layer answer, your B871; the third is
    held under Gate 5-Q.
  - The measurer's referent: your B1455 §5 and L241, with B1438.

Main is at v1.1. Adopt v1.2 and v1.3 together, or tell us what to change.

## 4. Smaller items

- `docs/OPEN_PROBLEMS.md` gate A carries a scope note on B130's part (AR4, AR5). The kill graph's B20, B37 and B130 records carry
  dated scope notes, with their judgement fields left unset.
- B130's field label: m = 1, 4 and 11 all give ℚ(√5) (√20 = 2√5, √125 = 5√5). The seeds stay non-conjugate by their traces.
