# B1320 — PHASE 2, ARC 0: Pantev–Wijnholt's localized count on the cyclic descent — the signed zero-locus count of the Higgs eigenform on C₃ and C₄ is the fixed-locus parity on the cover's one cusp: DESIGN (pre-registration, sealed before any of main's computations)

**Date:** 2026-09-09 · **Seat:** cc (main) · **Plan:** MASTERPLAN v3.1 §4, Arc 0 ("PW's own count on the descent, cheap, first"); §1b Q2 (PW arXiv:0905.1968
§3.1 eq. (3.18): chiral matter is the SIGNED INTERSECTION COUNT of the spectral cover with the zero section; the smooth bulk spectrum is vector-like;
non-trivial solutions need singular Higgs fields). · **Number:** B1320, main's next free number after B1306–B1307 (the alias table; RESERVED untouched). ·
**Read in full before this seal:** B1291 (T-CUSP-PARITY-EXCLUDES-THREE), B1295's `cover_scan.py` and its record (87 covers of m004 to degree 10; every
cusp-fixing isometry's |det(A − I)| ∈ {0, 4}; the degree-3 record H₁ = ℤ/4 + ℤ/4 + ℤ, 24 isometries; two degree-4 covers, the cyclic one H₁ = ℤ/3 + ℤ/15 + ℤ,
32 isometries), B1297 §1 (the correction: the index I = t₀ − r₁ is the BULK net count under I-26; PW's localized count on the descent is the zero-locus
count), fc R69 (the charge locus on Fix(θ): two arcs, net ±2 or 0). **Nothing below is computed before the seal; B1295's record is READ, and the two
covers are re-run live.**

## 0. The rule lines

`already_banked.py "Pantev Wijnholt localized count descent cyclic cover fixed locus parity"` → B1295 (the cover scan), B1291 (the parity theorem), B1297
(the index) — the ingredients are banked; the PW-frame reading on the descent specifically is not written anywhere (B1297 §1's correction names it as a
consequence and does not compute it). `absence_sweep.py "localized count"` at the seal. Receipt: `verification/already_banked_at_seal.txt`.

## 1. The view from above

PW's chirality on a 3-manifold with a Higgs field is not a bulk cohomology count; it is the signed count of zeros of the Higgs eigenform on the matter
curve — on a cusped 3-manifold, the fixed-locus count of the involution on the cusp torus, with signs. B1291 proved that on ONE cusp the fixed-point set of
any orientation-preserving cusp-fixing isometry has an even number of isolated points; B1295 measured |det(A − I)| ∈ {0, 4} on every cusp of every cover
to degree 10. The plan's Arc 0 asks the question in PW's own frame for the two cyclic covers that carry the ℤ/3 and ℤ/4 descent (C₃ is B298's cover with the
3-torsion twist; C₄ its neighbour): what does the localized count come to, and can it be 3 or 6? **The one thing it means if the count is 0 or 4 on both:**
the localized half of D2 is closed on the cyclic tower in PW's frame, exactly as the bulk half was closed by B1297, and the only remaining place for a
localized 3 is a cover that is NOT in the tower's degree-≤10 census or a partial filling (Arc B's priced route), or the sibling (L205).

## 2. Pre-registration

**Computation** (`verification/b1320_arc0_pw_count.py`, SnapPy 3.3.2): (a) enumerate m004's covers of degree 3 and 4; identify the CYCLIC ones by H₁ (the
cyclic cover of degree d has H₁ ⊇ ℤ with the torsion of Y_d's abelianisation: degree 3 → ℤ/4 + ℤ/4 + ℤ; degree 4 → ℤ/3 + ℤ/15 + ℤ) and by the deck group
(the cover's covering group is cyclic); (b) for each: the isometry group, every isometry fixing the cusp, its matrix A on H₁(cusp), |det(A − I)|, and the
orientation type; (c) the PW reading: the localized count is Σ over the Higgs eigenform's zeros with signs = the isolated fixed points of the involution on
the cusp torus counted with the sign of det(A − I)'s local index — for an orientation-preserving involution every isolated fixed point has index +1, so
the localized count is |Fix| = |det(A − I)| when ≠ 0, and 0 (a one-dimensional or empty fixed set) otherwise. **Expectation (pre-registered):** the set of
values on C₃ and C₄ is ⊆ {0, 2, 4}; **prior 0.95** that it is exactly {0, 4} (B1295's record, read); **a value 3 or 6 on either cover is the finding** that
reopens the localized half of D2 on the tower (prior 0.02); a value 2 (prior 0.03) would mean an order-4 rotation on a square cusp, which B1295 says no
cover to degree 10 has. **Controls:** m004 itself (the base: its own cusp-fixing isometries give {0, 4}, the record's D4 group); a manifold with an order-3
cusp rotation (SnapPy `m202` or another with a hexagonal cusp and an order-3 symmetry: the seat's and B1302's three-line sibling) must show |det(A − I)| = 3
on the same code path — the positive control that the method can see a 3.

**What is banked either way:** the localized PW count on the ℤ/3 and ℤ/4 descents (a number per cover, per isometry class), the reading in PW's frame
written once where B1297 §1 only named it, and the statement of what remains: Arc A (the bulk index in domain D beyond the cyclic tower), Arc B (the
chiral covers / partial fillings), L205. **Fail condition for the phase, restated:** if every configuration on the object's tower that the three conjugations
do not dualise still has index 0, the bit is on the observer's side by computation (v3.1 §4).

## 3. Landing list

`frontier/B1320_phase2_arc0_pw_count/{DESIGN.md, DESIGN.sha256, FINDINGS.md, arc_verdict.json, verification/{b1320_arc0_pw_count.py, .out, .json,
already_banked_at_seal.txt}}`, `tests/test_b1320_phase2_arc0_pw_count.py`, OPEN_LEADS L202 note, MAIN_GOAL's door table (Arc 0 done), the alias table's
next-free line (B1321), CHANGELOG + PROGRESS_LOG + CAMPAIGN_STATUS, the kill graph if NEGATIVE.
