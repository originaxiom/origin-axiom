# B1520 ADDENDUM (2026-10-02, the same day): the lemmas L1–L3 are B1297's, and B1297's P is this arc's s

Found after banking, from main's B1455 addendum (`8d1c1329`), and checked for this seat in sm:B1521. Nothing in this arc's
table, stabilisers, verdict or kill changes. Only the credit and one reading change.

- **The credit.** B1520's "Seen first" ran `prior_work.py` on ten terms in the handoff's vocabulary, plus main's
  `topic_sweep.py` (100 arcs). Neither returned main's B1297 (2026-09-08). B1297 states the class index's properties as
  "antisymmetry universal, closed ⇒ 0, self-dual ⇒ 0, … homeomorphism-invariant", which are L1 and L2. Its
  T-PERIOD-2-INVERTS-THE-ALEXANDER-MODULE is L3 with σ = P. §1, §2 and the verdict credit L1 to this seat's B1512 and main's
  B1455, and L3 to main's B1455; the earlier source of all three is B1297. Main's B1455 made the same miss and found it with
  a second sweep in the record's own vocabulary. This one is logged as an E54 instance in `docs/ERROR_LEDGER.md`.
- **P is s.** B1297's period-2 symmetry P (a ↦ a⁻¹, b ↦ a³b in SnapPy's presentation) is this arc's s, the swap of the two
  meridians, up to an inner automorphism: P = conj(nM) ∘ s. sm:B1521 C1 shows this through an explicit isomorphism between
  SnapPy's presentation and Ballas', proved by free-group reduction (`frontier/B1521_genesis_v13/verification/which_class_is_P.py`).
  This seat's B1279 (2026-09-06) had already named it "the period-2 swap".
  - So the s in the stabiliser {id, s, D.θ, D.sθ} of every vacuum is B1297's P, and it fixes ρ_q.
  - The count-odd fixers are the inversion θ and θ after P, both followed by dualising. P itself dualises ρ_q only at q = 1.
- **What this means for the levels.** B1297's tower theorem uses P, which acts as −1 on every torsion character of every
  cyclic cover. The vanishing on this family uses θ, which dualises ρ_q. On a level, a vacuum ρ_q ⊗ ψ is fixed by a
  count-odd map D∘σ only if one σ does both jobs. That is main's L242 (b), open; this seat takes it next (sm:B1522).
