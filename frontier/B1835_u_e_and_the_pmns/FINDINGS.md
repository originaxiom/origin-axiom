# B1835 — U_e AND THE PMNS IN B1656's FRAME: A CANDIDATE SECOND HELD-OUT QUANTITY (P-638; OPEN)

*Opened 2026-11-04 (S300d) at the owner's ruling on P-660 ("do for p660 as u recomend"). Data-free so far: no measured
neutrino datum and no frame output of the neutrino sector has been computed or read; nothing about y_b/y_t, y_τ/y_b or
tan β (P-585's firewall).*

**The question.** P-597: the record's candidate (THE SIX ON THE STRIP) has one clean held-out target, y_b/y_t; GAP1
v1.60 needs two. U_e was never computed (L189 item (1), lost by merge; B1833). Does the frame's neutrino sector supply a
second?

## 1. The control (PASSED, main's code)

B1728's order-5 law Y_e = Y_dᵀ implies U_e^L = conj(U_d^R) up to a phase per column. On all 24 order-5 lines, at two τ,
two seeds and two radii (a₀ = 0, the down and lepton reading S): Y_e = c·Y_dᵀ to ≤ 7 × 10⁻¹⁵ and U_e^L = conj(U_d^R) to
≤ 9 × 10⁻¹⁶. On the order-10 lines (2/5, odd/10), where no such law is claimed, the same comparison differs by 0.33–0.40
(the negative control). `verification/control_ue_order5.py`, `_run.txt`, through B1827's module.

**Repeated through the card's own instrument** (`verification/card_instrument.py`: B1726's compute() Yukawa construction line
for line, with its DR direction, its readings and its radius column, returning the matrices; it reproduces compute()'s
outputs exactly, difference 0.0). On the 24 order-5 lines, at two τ and both horocycles, Y_e = c·Y_dᵀ to ≤ 7 × 10⁻¹⁵ and
U_e^L = conj(U_d^R) to ≤ 1.1 × 10⁻¹⁵. On the order-10 lines the deviation is 0.06–0.12: smaller than with a random Higgs,
since DR is fixed, and clearly nonzero. `verification/control_via_b1726.py`, `_run.txt`.

## 1b. The planted relations (re-derived by main from B1728's charge-shift law; verified, two-sided)

A charge shift by a multiple of the line's order N changes a sector's matrices only by a phase. The neutrino (−3, 0) and
the electron (−3, 6) differ by 6 in the right charge; the neutrino and the up quark (1, −4) differ by 4 in both; so do the
electron and the down quark (1, 2). Hence:

- M_ν ∝ M_e on every line whose order divides 6 (holds on the orders 2, 3, 6 to ≤ 1.1 × 10⁻¹⁴; breaks on 4 and 5 by
  ≥ 0.10);
- M_ν ∝ M_u and M_e ∝ M_d on every line whose order divides 4 (holds on the orders 2, 4 to ≤ 6 × 10⁻¹⁵; breaks on 3, 5
  and 6 by ≥ 0.09);
- so, with the neutrino read like the up quark (I-35), ∣U_PMNS∣ = ∣V_CKM†∣ on the order-2 and order-4 lines (to ≤ 2 ×
  10⁻¹²) — the frame's quark–lepton relation there.

`verification/planted_relations.py`, `_run.txt`. The candidate's address lies on order-10 lines, where none of these
holds, so they are positive controls for the card's extraction, not predictions at the address.

## 1c. The line's order and the sectors it identifies, with the neutrino (S303; data-free)

B1728's law decides exactly when two sectors' matrices coincide on a line of order N. They are proportional when their
charge pairs agree modulo N, up to an overall sign; they are transposed when the pairs agree with left and right swapped.
`verification/order_dictionary.py` predicts this from the charges and checks it on the card's instrument, at two lines of
exact order N and two τ, for N = 2, 3, 4, 5, 6, 8, 10, 12, 15, 20 and 30:
- every predicted relation holds to ≤ 1.1 × 10⁻¹⁴;
- every relation not predicted fails by ≥ 0.046;
- no relation holds that was not predicted.

| order | what is identified |
|---|---|
| 2 | up ∝ down ∝ lepton ∝ ν (one Yukawa for all) |
| 3 | up ∝ down and lepton ∝ ν, every sector symmetric (left–right) |
| 4 | ν ∝ up, lepton ∝ down (Pati–Salam) |
| 5 | lepton ∝ downᵀ, up symmetric (minimal SU(5)) |
| 6 | up ∝ down, lepton ∝ ν |
| 8, 10, 12, 15, 20, 30 | none exactly; at 8 and 10, the half-lift with a Higgs flip (T-HALF-LIFT) |

**Seen first.** The charged part is B1698's and B1703's (LAW_MAP's "WHICH LINES SPLIT THE CHARGED SECTORS": d = e at
orders 4 and 5, u = d at N ∣ 6, u = e at N ∣ 2 or 7). New here are the neutrino rows and the self-transpose entries. The
reading of the line's order as a unification pattern (P-682) is that row's own, extended.

## 2. The design (a reader's draft in the audit room; main verified what is stated here)

- **The address** is frozen on the family's best sealed row, chosen by the already-seen six only: the lowest χ²_six among
  B1749's and B1753's sealed rows, with mirror ties broken by Re τ mod 1 in [0, ½). The Higgs direction there is DR, the
  Serre derivative of the theta triplet (B1691; B1726's compute). The scoreboard's A04 was corrected to say so (P-666).
  The line must be named in one convention: B1726 writes w = ατ + b, while B1821 and B1827 write p₁τ − p₂, so b flips
  sign.
- **The neutrino** is the Dirac pairing L ν^c with sector charges (−3, 0) (B1799's code). Its reading is S̃ under I-35,
  the hypercharge sign rule (UNEARNED, so one priced bit unless adopted). It adds no continuous parameter for the angles,
  cos δ or the splitting ratio r. δ's sign is mirror-odd, so it is not predicted. A seesaw or Weinberg term adds typed
  choices and enters only as members of the null's menu.
- **Scope.** The PMNS angles come out of I-33's mixing half (U_e†U_ν), and that half already fails for the quarks at
  this address (B1749's nine; B1825). P-585 scopes the candidate to a mass dictionary. So the angles cannot confirm it
  unless a separate, priced, lepton-scoped identification is adopted (P-665, the owner's). **The mass half leaves one
  quantity: r = Δm²₂₁/Δm²₃₁.**
- **r's structure** (re-derived by main from the channel-exponent law, LAW_MAP's B1832 S300 row). For (q_L, q_R) =
  (−3, 0) on α = 2/5:
  - the entries are e₀₀ = −0.085, e₁₁ = 0.215, e₀₁ = 0.165 and e₁₀ = −0.035;
  - the within-sector gap is 1/20, as for down and lepton;
  - the dominant pair is (j, k), the lepton sector's being (1, i).

  So at leading order r scales with Im τ like the lepton hierarchy the six already used. Its held-out information sits in
  the prefactors, and the matched null and P-611's budget must measure it before r can count as a second target. r is
  independent of y_b/y_t by structure.
- **The look count.** m_V is one number per attempt. Adding the most-looked targets (the angles) would raise the
  threshold for y_b/y_t too, which is a reason to keep the target set to what the scope allows.
- **Main's rulings on the draft's decisions** (by the record's rules):
  - the address rule (D1);
  - Dirac, with seesaw and Weinberg only in the null (D3, D12);
  - S̃ under I-35 stated as the card's rule (D4);
  - one m_V per attempt, and targets chosen by the power rule before any output (D5);
  - δ's sign graded an input (D6);
  - one look per target touched (D7);
  - numerical error plus running banded, with H = I and loops disclosed (D8);
  - tree level at M_Z with the running priced (D9);
  - KIND_TABLE's kind clause answered in the preregistration (D10).
- **To the owner (P-665):** D2, which identification the card earns, and D11, no data-touching existence scan for a held-out
  target.

## 3. Next

1. (done) The control through B1726's compute(); the planted relations re-derived and verified (§ 1b).
2. After the owner's D2 and D11: write the card, compute r (and, if D2 allows, the angles) unread with a hash pin, then
   run the budget and the matched null, seal, and compare.

## Seen first

- `VERDICT topic-sweep /U_e|PMNS|neutrino/ (full text): 57 of 1581 arcs on main match (NEGATIVE 12, OPEN 4, PROVED 41); 11 register rows match` — B1799 (the neutrino's self-pairing; the Dirac sector's zeros);
  B1713 ("PMNS (no neutrino sector)"); B1616 (Majorana on the weave NEGATIVE); B1625, B1628 (P10, P10′: TM1 readings);
  B342, B343 (residual symmetries); L189 (1); and the independent lane's unsealed PMNS look (harvest row 1550). U_e was
  never computed on main.
- **Literature (pointers):** U_PMNS = U_e†U_ν and its sensitivity to the charged-lepton rotation are standard (e.g. the
  charged-lepton-correction literature in flavour model-building). This arc only computes it in the frame.

## Disclosed

- The card is not written. No neutrino output of the frame has been computed. The exponent figures above are structure
  (the channel-exponent law at one slope), not outputs.
- The design draft is a reader's, kept in the audit room. Its "derived here" relations are not yet re-derived on main.
