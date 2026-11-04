# Harvest reader, Review 74 (2026-11-04): three seats since the S298 pins — saved by main from the reader's hand-back

(The harness refused the reader's file write; main saved this copy verbatim in substance. PART_III_SEALED.md beside it holds
the firewalled values and is NOT opened by main.)

Scope: web seat e40d0fb1 → 8ed19bbd4 (2b515e748, a993b7df6, fe2f972cd, 8ed19bbd4); SM seat 254c09df4 → 886dc3a3c
(2a1653df5, 1c2ce95b7, 874fdedfe, 886dc3a3c); agy lane 9366d7c61 → d9a04edd7 (one commit). Unrowed inside the old pin: the web
seat's check scripts for both new relays (relations_check.py v1 5aecc2bce→b3be3f9f2, v2 796f02e2b→5c98cc7e5;
halfperiod_check.py v1 41451dbee→cef31ebfe; theta_rule_check.py v1 ba981b3e8→eb876fb39, v2 2e545afc4→e40d0fb19). Arrival
order from main's fetch reflog: 2026-11-03 23:51:25 +0100 saw SM at 2a1653df5 (W183's rule), web at fe2f972cd, agy at
d9a04edd7; 05:51:30 saw 886dc3a3c and 8ed19bbd4.

## 0. Firewalled material — locations only
1. agy d9a04edd7's commit SUBJECT names a qualitative claim about a P-585 firewalled quantity on the family's lines: list it
   with `git log --format=%h` only.
2. agy relay relays/AGY_TO_ALL_SEATS_2026-11-03_SIX_STAGE_BULLETPROOF_ROAD_PLAN_THEOREM_15_AND_4B91B9BE7_CLEANUP.md § 7
   (lines 255–259, 266–268, 271) and § 6.2–6.3 (~200–232, counted at S298 row 1539): do not open § 6.2–7.
3. agy src/origin_axiom/toe_closure.py line 3344 and 3589–3686 (Theorem 20); tests/test_elevation_operator_gate.py lines
   803, 806–807, 828–831, 836–837 (pre-pin 767–768). Not run.
4. Web seat near the firewall (relation level): halfperiod_check_out.txt @ a993b7df6 lines 211–229 and the relations relay
   @ fe2f972cd lines 198–209 (distances of down and lepton spectra from equality on half-period class lines, third
   generation included, at two τ off the strip, raw frame); relations relay lines 255–258 (direction-conditional equalities
   of the largest singular values; none reaches the family's address for the up sector). halfperiod_check.py not re-run.
5. Web seat θ relay @ 8ed19bbd4: line 50, 53–58 quote θ_Y facts already on main (row 1538; P-323's row; row 1414); line 203
   θ_Y mod π in closed form only on the mirror's fixed set (J = 0); evaluates nothing on slope 2/5 (its check refuses a =
   2/5, 3/5); line 231: main's own row 1443 prints four θ_Y values at candidate addresses.
6. SM seat: nothing firewalled (W183's JSON: within-sector ratios, CKM moduli, rates, a₀, D).

## 1. Web seat, THE RELATIONS THE FRAME FORCES (fe2f972cd)
Claim: on FR-FIB as B1825 typed it, τ is the only continuous input on a branch; f(d) = 2 on all 1 536 branches sampled (1 on
32 null branches of orders 1–2; none of the ten varies on 192 order-4 null branches), so 8 relations among the ten (11 of
13). Explicit relations: B1728's table as relations (orders ≤ 7, 62 of 266 lines; 4+16+6+12+24+156+48 = 266); exact zeros
(order 4 first generation massless in every sector, ∣V_us∣ = ∣V_ub∣ = J = 0 where defined; order 12 leptons e = 0; null
directions m₁ = 0 on every line, rank one on null matter); half-period coincidences computed at two τ (d = e on every
order-8 and order-10 line for a Higgs lacking the unit the line's class fixes or along one unit only; u = d = e on order 4
likewise; order 6 equal in ratios only; 21 random directions agree on 33 516 comparisons). § 3 scale: within-sector relations
move at most by B1718's running; inter-sector need a declared scale (P-574). § 4: P-568's rigid inter-sector outputs not
computed. Asks (lines 277–290): record f(d) = 2 (FL-15, P-568 first half, B1809's owed count, P-418); record the
classification as the rest of P-355's list; order P-568's second half against P-585 (compute the rigid outputs only inside
the sealed level-2 card, or drop y_b/y_t from P-585 — the seat proposes neither now); any relations card declares its scale.
Corrects main: B1809 FINDINGS.md:129 "m₂ ≡ 0 only at L = ∞" for the null directions fails on order-4 lines (every sector)
and order-12 lepton rows (m₂/m₃ < 1e-12 at both radii; halfperiod_check_out.txt lines 248, 256; B1659's adjugate law).
Pays B1809:251's owed f(d); finds S297's QI class independently. Caveat: f(d) a pointwise rank at 16 (line, τ) points.
Data: none. Re-run (§ 5): relations_check.py v2 from a git archive of main 354a4ea4d, python 3.12.1, numpy 2.4.0, 484 s;
3 312 rows against the committed 3 328 — 16 null-direction rows skipped because ∣V_ub∣ evaluated to exactly 0 at one
finite-difference point in this environment (tiny non-zero in the seat's); f(d) = 2 reproduces on every row computed; global
minimum 0.043 and every per-point median unchanged; one per-point minimum moved (4/9, 1/3) at 0.13 + 2.2i 0.129 → 0.177;
the committed output depends on the environment at the numerical floor.

## 2. Web seat, THE STRONG ANGLE NEEDS A RULE (8ed19bbd4)
Claim: θ_Y = arg det Y_u + arg det Y_d is not invariant under the frame's relabellings, so it is defined only mod 2π/N; CP
fixes θ̄ only on the mirror's fixed set, where J = 0. Theorem 1 (sketch; checked on 14 lines off slopes 2/5, 3/5, residuals
≤ 7.4e-9): A (a, b+1, τ) moves θ_Y by 264πa = 12πa Σ(q_L² + q_R²) (204πa up, 60πa down); P (a+1, b, τ) and N (−a, −b, τ)
leave it; T (a, b−a, τ+1) moves it by −132πa² + 3π/2 + 3φ(σ_u + σ_d) = −132πa² − π/2 for every direction in (S̃, S) and
(S, S̃); M (a, −b, −τ̄) sends θ_Y → −θ_Y; masses and ∣V∣ unchanged by all five, J unchanged by A, P, N, T and odd under M.
Corollary 2: N = lcm(ord 132a, ord(66a² + ¼)); N = 100 on slopes 1/5, 2/5, 1/10, 3/10. Theorem 3: any θ_QCD rule making θ̄
invariant under A, P, N, T and odd under M gives θ̄ ∈ {0, π} on the mirror's fixed set (where J = 0) and fixes nothing off it.
A compensating rule θ_ct = −264πab + (π/2 − 132πa²) Re τ (0 ≤ a < ½), (π/2 − 33π) Re τ at a = ½ — N-even, M-odd, not
P-invariant; a P323_RULE counterterm, so S232's NOT HARMONIC applies. § 4: FPST's modular route (P-461) closed on every
line in the SM reading (66a² + ¼ ∈ ℤ forces s² ∣ 264, s ∈ {1, 2}, a parity contradiction; 48 678 slopes). § 2/§ 5: θ_Y
already on record at seven of the family's addresses (four from e20's F2, four from P-323's read-outs, one shared); every
candidate row on record or within 0.03 of one; with θ_ct public θ̄ there is one addition from main's ledger. Reader's hand
checks: the A and T shifts, N = 100 on 2/5, θ_ct's cancellation and parities, the FPST parity argument; the T-step formula
reproduces P-323's row. Asks (285–297): record Theorems 1–3 (FL-16, P-323); drop θ̄ from P-585 and grade it as an input
(the card is then one target short of GAP1 v1.60's two, needing y_τ/y_b made clean by a forced scale, P-574, or another
held-out quantity; if θ̄ is kept, the § 2 addresses count as looks); re-scope P-569 to the mirror's fixed set or attach a
rule; P-461's FPST half answered negative, its Dabholkar–Hull half untouched. Corrects main: P-585's row says "θ̄ (one prior
look, P-323)"; the record holds θ_Y at seven addresses plus e20's F4 lines, P-323's unread census and the agy look (row 1539).

## 3. SM seat, W183 (rule 2a1653df5 → script 1c2ce95b7 → output 874fdedfe → reading 886dc3a3c)
RI-1 at τ = i: the kernel's Laurent constant a₀ odd between up and down (parity to 1e-60); as the singlet at τ = i it lifts
the coarse corner fact from 8% to 14%, as any odd singlet does. Cells verified by the reader against the committed JSON: O0
held (1 242 features); O1 held (residual 1e-60.4, lepton = down exactly, route 2 at 1e-39.8); O2 held (none 20/261 = 7.7%);
O3 held (even 5.7% vs 8.2%, 244 lines); O4 failed (N 13.5% vs 8.2%); O5 held (N 14.7% within 0–16.1%, 224 lines); O6 failed
(B 13.8% vs 8.1%, 246 lines); O7 held; O8 failed (four hits under B: (4/9, 1/3), (4/9, 2/3) D = 10.265; (4/9, 4/9), (4/9, 5/9)
D = 10.393). No hierarchical point; 47 lines with a₀ purely imaginary; median ∣a₀∣/∣DR∣ 6.21. Asks (§345 items 4–6): τ = i is
not P-566's regime; a₀ ≡ 0 on the 15 half-period lines; DR·DR real positive at τ = i; RI-1 TESTED at τ = i, not earned (an
UNEARNED IDENTIFICATION_LEDGER row at most); the band test needs main's address rule; the B1814 blind rerun next (not
started). Sealed by commit order (rule on the remote before the script). Data: yes, sealed (coarse CKM facts; (r₂, r₁);
D in [10.25, 10.91]). Debts: LOOK_LEDGER entry; P-566 notes; P-591 RI-1 TESTED; an address rule for the band.

## 4. agy lane, d9a04edd7 (Theorems 19–20)
Value-free summary: Theorem 19 (P-524's lemma checked numerically at one twist; an order-5 uniqueness that restates B1728
plus a slope 'sign selection' built on a P-585 firewalled quantity; a P-233 control that hard-codes the target hypercharge
multiset over a restricted 625-point space, no rule first); Theorem 20 (order-5 versus order-10 with a singlet; a det-1
operator fitted to measured D; a tuned singlet; a tan β from a strip ratio and measured-derived m_b/m_t; F₂ transport;
docstring 52 words vs 84 unreduced strings in code). A second unsealed seat computation of a P-585 target on the family's
lines (after row 1539). No output file; results only in test asserts; not run. Overclaims 'closed' for P-524, P-384, P-233.
Debts: count d9a04edd7 as a further prior look at P-585's targets (values unread by main); do not adopt Part B's selection;
P-524, P-233, P-384 stay open.

## 6. For main's decisions
1. P-585 receives three seat inputs: the relations relay keeps y_b/y_t held out; the θ relay asks to drop θ̄; the agy lane
   made a second unsealed y_b/y_t-type computation. Taking both web-seat proposals leaves one target, one short of GAP1's two.
2. Corrections to carry: B1809 FINDINGS.md:129; POINT_REGISTER.md:733 (P-585's "one prior look").
3. Looks: W183 a sealed look at D and the coarse CKM facts; d9a04edd7 an unsealed look at D, measured m_b/m_t and P-585's
   targets.
4. The kernel claims P-524, P-559, P-337 untouched except by the agy lane's numerical P-524 check.
