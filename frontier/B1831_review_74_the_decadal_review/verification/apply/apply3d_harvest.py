"""Review 74 (S299), apply 3d: the three seats' commits since S298's pins, harvested (the firewalled reader's report,
audit/review74/harvest/REPORT.md; main verified the theta rule check on its own tree; main did not open PART_III_SEALED.md,
the agy relay's § 6.2-7, or the agy commit's subject)."""
import pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[3]; D = "2026-11-04"
H = ROOT / "docs/HARVEST_LEDGER.md"; t = H.read_text(encoding="utf-8")
rows = [
 (1544, "web seat (chat1)", "THE RELATIONS THE FRAME FORCES (relay fe2f972cd; relations_check.py v1 5aecc2bce → b3be3f9f2, v2 796f02e2b → 5c98cc7e5; halfperiod_check.py v1 41451dbee → cef31ebfe)",
  "on FR-FIB as B1825 typed it τ is the only continuous input: f(d) = 2 on 1 536 sampled branches (1 on 32 null branches of orders 1–2), 8 relations among the ten; the explicit ones B1728's table, the exact zeros and the half-period coincidences in three classes (computed at two τ); B1809's 'm₂ ≡ 0 only at L = ∞' scoped; the rigid inter-sector outputs left to P-585's card",
  "relays/CHAT1_TO_CC_2026-11-03_THE_RELATIONS_THE_FRAME_FORCES.md @ fe2f972cd",
  "**READ; VERIFIED-PENDING** (Review 74): f(d) = 2 reproduced by the review's reader with the seat's code on every row computed (16 null-direction rows skipped at the numerical floor in its environment); B1809:129 corrected by main's own check with B1821's evaluator; the half-period output carries near-firewall distances and was not re-run; P-596, P-355, P-568", "B1809, B1831"),
 (1545, "web seat (chat1)", "THE STRONG ANGLE NEEDS A RULE (relay 8ed19bbd4; theta_rule_check.py v1 ba981b3e8 → eb876fb39, v2 2e545afc4 → e40d0fb19)",
  "θ_Y = arg det Y_u + arg det Y_d moves under the frame's relabellings (b → b+1 by 264πa; T by −132πa² − π/2; the mirror odd), so it is defined only modulo 2π/N (N = 100 on slope 2/5); an invariant CP-odd rule pins θ̄ only on the mirror's fixed set, where J = 0; a compensating counterterm; FPST's modular route closed in the SM reading; θ_Y already on record at seven of the family's addresses; proposes dropping θ̄ from P-585",
  "relays/CHAT1_TO_CC_2026-11-03_THE_STRONG_ANGLE_NEEDS_A_RULE.md @ 8ed19bbd4",
  "**VERIFIED** (Review 74): Theorems 1–2 re-run on main's tree from the seat's script with one worker (Pool(2) → Pool(1), disclosed): every law to ≤ 5 × 10⁻⁹, the N table identical, the fixed-set law to 4 × 10⁻¹², the counterterm's invariances, no slope with s ≤ 400 T-anomaly-free; Theorem 3 by logic; main's ruling: θ̄ off P-585's held-out list (P-597)", "B1831"),
 (1546, "SM-derivation seat", "W183 and §344–§345 (rule 2a1653df5 → script 1c2ce95b7 → output 874fdedfe → reading 886dc3a3c)",
  "RI-1, the kernel's Laurent constant a₀ as the sector-odd singlet at τ = i on 261 lines: the parity to 10⁻⁶⁰ and a₀ = 0 on 15 half-period lines; the coarse corner fact rises 8% → 14% under both sizes (O4, O6 failed), the phase not special, the even singlet does nothing; O8 failed (two order-9 mirror pairs put D in the window under the bare singlet, the split in the first generation only); TESTED at τ = i, not earned; the B1814 blind rerun next",
  "SM_TO_CC_AND_CODEX_2026-10-07_THE_CHIRAL_TRIPLETS_COUNT.md and the W183 folder @ 886dc3a3c",
  "**READ, SEALED BY COMMIT ORDER** (Review 74; the rule on the remote before the script, main's fetch reflog): every cell verified by the review's reader against the committed JSON, not re-run on main (474 s on four workers); LOOK_LEDGER; P-566, P-591, P-584", "B1831"),
 (1547, "the agy lane (audit-2026-11-02)", "d9a04edd7 (Theorems 19–20; toe_closure.py, test_elevation_operator_gate.py; its relay's § 7)",
  "Theorem 19: P-524's lemma checked numerically at one twist, an order-5 uniqueness restating B1728 plus a slope selection, a P-233 control not as the register words it; Theorem 20: order-5 against order-10 with a singlet, a det-1 operator fitted to D, a tan β from a strip ratio, F₂ transport (values firewalled)",
  "src/origin_axiom/toe_closure.py, tests/test_elevation_operator_gate.py @ d9a04edd7",
  "**READ** (Review 74; post hoc, unsealed, no output file, not run): a further prior look at P-585's targets, counted in m_V, values unread by main (the commit's subject, the relay's § 6.2–7 and the code's lines 3344, 3589–3686 not opened by main); Part B's selection not adopted; P-524, P-233, P-384 not paid", "B1831"),
]
add = "\n".join("| %d | %s | %s | %s | %s | %s | %s | %s |" % (n, s, i, h, p, d, a, D) for n, s, i, h, p, d, a in rows)
assert "|" not in "".join("".join(r[1:]) for r in rows)
last = [l for l in t.split("\n") if l.startswith("| 1543 |")][0]; assert t.count(last) == 1
t = t.replace(last, last + "\n" + add)
def pin(key, old, new, note):
    global t
    ls = t.split("\n"); k = [i for i, l in enumerate(ls) if l.startswith("| %s |" % key)]; assert len(k) == 1, key
    c = [x.strip() for x in ls[k[0]].strip().strip("|").split(" | ")]
    assert c[2] == "`%s`" % old, (key, c[2]); c[2] = "`%s`" % new; c[3] = "%s (Review 74): %s — before: %s" % (D, note, c[3]); ls[k[0]] = "| " + " | ".join(c) + " |"; t = "\n".join(ls)
pin("chat1", "e40d0fb1", "8ed19bbd", "rows 1544–1545 (the relations relay, the strong-angle relay and their check scripts)")
pin("sm", "254c09df", "886dc3a3", "row 1546 (W183, §344–§345)")
pin("agyaudit", "9366d7c6", "d9a04edd", "row 1547 (Theorems 19–20; values firewalled)")
H.write_text(t, encoding="utf-8")
R = ROOT / "docs/RELAY_LEDGER.md"; r = R.read_text(encoding="utf-8")
anchor = [l for l in r.split("\n") if l.startswith("| `CHAT1_TO_CC_2026-11-03_THE_CHANNEL_NORMS_PAIR_SUMS")][0]
new = ["| `CHAT1_TO_CC_2026-11-03_THE_RELATIONS_THE_FRAME_FORCES.md` (on the web seat's branch @ `fe2f972cd`) | READ (HARVEST_LEDGER row 1544) | 2026-11-03 | the web seat->cc: τ the only continuous input on FR-FIB as typed, f(d) = 2, eight relations among the ten; B1809's m₂ claim scoped (corrected by main, B1809's dated note); asks: record f(d) (P-596), the classification on P-355, the P-568/P-585 ordering held, a declared scale on any relations card (B1831) |",
       "| `CHAT1_TO_CC_2026-11-03_THE_STRONG_ANGLE_NEEDS_A_RULE.md` (on the web seat's branch @ `8ed19bbd4`) | READ AND VERIFIED (HARVEST_LEDGER row 1545) | 2026-11-03 | the web seat->cc: θ_Y defined only modulo 2π/N on the frame's points; an invariant CP-odd rule pins θ̄ only where J = 0; asks: drop θ̄ from P-585 (done: main's ruling at Review 74, P-597), re-scope P-569, P-461's FPST half negative (B1831) |"]
assert r.count(anchor) == 1; r = r.replace(anchor, anchor + "\n" + "\n".join(new))
ag = [l for l in r.split("\n") if l.startswith("| `AGY_TO_ALL_SEATS_2026-11-03_SIX_STAGE")][0]; assert r.count(ag) == 1
r = r.replace(ag, ag.rstrip()[:-1].rstrip() + " [Review 74: its § 7, added at d9a04edd7, carries P-585 firewalled values on the slope-2/5 lines; not opened by main; harvest row 1547] |")
R.write_text(r, encoding="utf-8")
L = ROOT / "docs/LOOK_LEDGER.md"; l = L.read_text(encoding="utf-8")
w = [x for x in l.split("\n") if x.startswith("| W182 (row 1542")][0]; assert l.count(w) == 1
l = l.replace(w, w + "\n" + "| W183 (row 1546; rule 2a1653df5) | sealed, one look: RI-1's sector-odd singlet at τ = i on 261 lines, its size two ways | D, the coarse CKM corner facts | O4, O6, O8 failed: the corner fact 8% → 14%, as any odd singlet; two order-9 mirror pairs put D in [10.25, 10.91] under the bare singlet (10.265, 10.393), the split in the first generation only |\n"
                    "| the agy lane's d9a04edd7 (row 1547) | unsealed, post hoc | D, measured m_b/m_t, and P-585's held-out targets | a det-1 operator fitted to D, a tuned singlet, a tan β from a strip ratio; values firewalled and unread by main; counted in m_V for P-585 |")
L.write_text(l, encoding="utf-8")
print("harvest rows 1544-1547, pins, relays, looks")
