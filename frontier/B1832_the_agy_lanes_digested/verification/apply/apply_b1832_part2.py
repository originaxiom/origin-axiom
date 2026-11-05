"""B1832 part 2: the register, LOOK_LEDGER, the harvest rows and the pin."""
import pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[2]; D = "2026-11-04"
REG = ROOT / "docs/POINT_REGISTER.md"; text = REG.read_text(encoding="utf-8")
def row_edit(pid, fn):
    global text
    ls = text.split("\n"); k = [i for i, l in enumerate(ls) if l.startswith("| %s |" % pid)]; assert len(k) == 1, pid
    c = [x.strip() for x in ls[k[0]].strip().strip("|").split(" | ")]; assert len(c) == 7, pid; fn(c)
    assert all("|" not in x for x in c), pid; ls[k[0]] = "| " + " | ".join(c) + " |"; text = "\n".join(ls)
def note(pid, s): row_edit(pid, lambda c: (c.__setitem__(5, c[5] + " " + s), c.__setitem__(6, D)))
def done(pid, s): row_edit(pid, lambda c: (c.__setitem__(4, "DONE"), c.__setitem__(5, s + " [was: " + c[5][:500] + ("…" if len(c[5]) > 500 else "") + "]"), c.__setitem__(6, D)))
done("P-390", "B1832 (the agy lanes digested): the residue law re-derived as T-KERNEL-SUM-TWIST, the i-residue fact corrected and generalised ({5w ≡ ½} ∪ {3w ≡ ½}); the gates of P-391 stay on P-391")
done("P-621", "B1832: every claim of both agy branches and the independent lane typed and dispositioned; every data-free one checked on main's code, about sixty checks re-run by main (identical); four theorems and three exact identities banked; B1784 and B1826 corrected; a dozen agy claims refuted; the scorecard 0 of 19; the y_b/y_t and y_τ/y_b parts unread by main, put to the owner")
note("P-524", "**[B1832: the lemma has a written derivation — T-KERNEL-SUM-TWIST, an explicit four-channel factorisation (Jacobi's product formula at period 2τ), checked on main's code to 2 × 10⁻¹⁴; the agy lane's Theorem 19 and the web seat's kernels note credited. Remaining: a hostile referee of the written derivation]**")
note("P-355", "**[B1832: the owed item on the 40 β-half-lifts PAID — T-HALF-LIFT-LEPTON-DOWN proves Y_e(S) = λ·D·Y_d(Σ₁₀S)ᵀ·D on the order-10 points and λ·D·Y_d(Σ₈S)·D on the order-8 points for every Higgs (S297's coincidence proved; the agy lane's Theorem 21); new: a₀ ≠ 0 splits the order-8 points]**")
note("P-559", "[B1832: the replacement exponents verified asymptotically on main's code (11 slopes × 2 offsets; exceptions confirmed); as worded 48 of 183 cross-pair cases fail hypothesis (a), term by term 0 of 183; the '18 of 171' counts 51 untested cases and both α and 1 − α]")
note("P-591", "[B1832: RI-1's sign identity is a theorem — a₀^up = −a₀^down = −a₀^lepton in every channel, line and τ (T-KERNEL-SUM-TWIST's corollary); the identification rows and FL-05 remain]")
note("P-593", "[B1832: the residue-level cusp law derived (each lepton/down residue ratio → 0, ∞, 1 or ∣cos πb_e/cos πb_d∣); the agy lane's Theorem 22 laws A.1, A.2, A.4 refuted; W181's D∞ itself unchecked]")
note("P-323", "[B1832: T-THETA-Y-BSTEP — the b-step 264πa proved; 66a² + ¼ ∉ ℤ, so the T-step is never trivial on a rational line]")
note("P-569", "[B1832: with T-THETA-Y-BSTEP and Review 74's ruling, θ̄ is fixed by CP only on the mirror's fixed set]")
note("P-557", "[B1832: the '7 680' is arithmetic (n_lines × 10 × 2 × 8), not a census count]")
note("P-558", "[B1832: FR-COV's a₀ (the independent lane, reproduced): χ²₈ 277.2 at a₀ = 0, 1 287 at the lane's a₀, best 257.5, ≥ 514 wherever the corner flips (55% of the ∣a₀∣ ≤ 1 disc); the witness depends on whether the reading map acts on a₀ (0.678 against 1.177); FR-COV's cell (2/5, 0) lies outside Fix((LR)³)]")
note("P-564", "[B1832: Fix((LR)³) has five ⟨T, −I⟩ orbits; (2/5, 1/5) is negated, not fixed; Γ(2) has one orbit on the NS coset]")
note("P-391", "[B1832, evidence for the gates: the agy audit branch's literal flags (Theorem 24, 28's guardrails; '23 observables', '0 fitted'), docstring numbers its code does not produce, 9 of 12 'seen first' arc names that do not exist on main, tests that assert agreement with measured numbers, and its own checks failing at 951998a73]")
note("P-585", "[B1832: more exposures of the held-out targets, counted in m_V — the agy lane's Theorem 8 inter-sector ratios on its FR-COV (2/5, 0) cell against PDG (y_b/y_t- and y_τ/y_b-type, unsealed) and the independent lane's sensitivity check of them; four of main's verifiers disclose such values entering their own contexts before masking (none copied); main has read none]")
NEW = [("P-622", "B1826 § 1.3 AND § 3 OVERSTATED THE CORNER INVERSION (the independent lane's scan, read by main at B1832): the '52 of 250' are hierarchical AND SM-ordered rows; 719 of all 1 127 hierarchical rows (64%) already have the measured corner order", "DONE", "B1826's dated note of 2026-11-04; RETRACTIONS; B1832 § 3"),
       ("P-623", "B1784's TWO WORDINGS (B1832's frontier verifier, checked by main): the up i-residue vanishes on {5w ≡ ½} ∪ {3w ≡ ½}, not only 5w ≡ ½; τ* is not a critical point of E3 − tE2, not 'a saddle without flux'", "DONE", "B1784's dated note of 2026-11-04; RETRACTIONS; B1832 § 3")]
ls = text.split("\n"); last = max(i for i, l in enumerate(ls) if re.match(r"^\| P-\d{3} \|", l)); assert ls[last].startswith("| P-621 |")
for pid, body, disp, where in NEW:
    ls.insert(last + 1, "| %s | %s | MA | %s | %s | %s | %s |" % (pid, D, body, disp, where, D)); last += 1
text = "\n".join(ls); REG.write_text(text, encoding="utf-8")
fp = ROOT / "scripts/checks/point_debt.py"; s = fp.read_text(encoding="utf-8"); assert "FLOOR = 621" in s; fp.write_text(s.replace("FLOOR = 621", "FLOOR = 623", 1), encoding="utf-8")
# LOOK_LEDGER
L = ROOT / "docs/LOOK_LEDGER.md"; l = L.read_text(encoding="utf-8")
w = [x for x in l.split("\n") if x.startswith("| the agy lane's d9a04edd7 (row 1547)")][0]; assert l.count(w) == 1
l = l.replace(w, w + "\n" +
  "| the agy lane's Theorem 8 inter-sector ratios (row 1549; sm_19_gate.py ~754–797) | unsealed, post hoc | P-585's held-out targets (y_b/y_t-type, y_τ/y_b-type), on its FR-COV (2/5, 0) cell against PDG | values firewalled, unread by main; counted in m_V |\n"
  "| the independent lane's data-touching scans (row 1550) | unsealed (other frames and FR-COV) | the ten, the six, CKM corners, PMNS (NuFIT), M_t and M_h (PDG), the inter-sector ratios | a τ map (12 221 points), 600 closed-form τ, 2 048 characters, the a₀-plane χ²₈, a 371 293-vector γ search, the no-go scan's realistic cut, T12's matched masses; reproduced by B1832's verifier; inter-sector values firewalled |")
L.write_text(l, encoding="utf-8")
# HARVEST rows and the pin
H = ROOT / "docs/HARVEST_LEDGER.md"; t = H.read_text(encoding="utf-8")
rows = [
 (1548, "the agy lane (frontier-2026-10-26)", "the whole branch re-read for B1832 (25 arcs, agy:B1758–B1782)", "every claim typed and checked; agy:B1759's residue law and agy:B1761's fact re-derived and corrected; agy:B1773's flux potential, agy:B1774's Bessel term, agy:B1779's torsion, agy:B1767's Q₈ cover and agy:B1768's ω₁ row refuted; the value rows declined as at B1784", "frontier/agy:B1758–B1782 @ 05e6caab", "**DIGESTED** (B1832; main re-ran every check, identical; the ledger rows agy:B1769, B1772, B1776–B1778, B1781 firewalled, unread by main)", "B1832, B1784"),
 (1549, "the agy lane (audit-2026-11-02)", "8b3d48662, 18c607040 (Theorems 23–28, the master scorecard) and the whole branch re-read for B1832", "Theorems 10–28 and the phases typed and checked: P-524's lemma, the half-lift theorem, F₁₀'s norm, the b-step banked (B1832 § 1); Theorem 22's laws, Theorem 24's θ sum, Theorem 26's docstring, Theorem 28's provenance refuted; the scorecard 0 of 19 by the lane's own literal", "src/origin_axiom/toe_closure.py, sm_19_gate.py, relays/ @ 18c607040", "**DIGESTED** (B1832; Theorem 18, Theorem 20 and the six-stage relay from § 6.2 unread by main — P-585's firewall)", "B1832, B1826"),
 (1550, "the independent audit lane (2026-11-03)", "audit_independent/ (56 files) re-run for B1832", "22 of 22 committed outputs reproduced; B1826 § 1.3's population corrected (719 of 1 127 hierarchical rows have the measured order); FR-COV's a₀ costs; Theorem 10 selects nothing; agy's checks failing at 951998a73", "audit_independent/ @ 4b91b9be", "**REPRODUCED and DIGESTED** (B1832; its inter-sector lines firewalled, unread by main)", "B1832"),
]
last = [x for x in t.split("\n") if x.startswith("| 1547 |")][0]; assert t.count(last) == 1
add = "\n".join("| %d | %s | %s | %s | %s | %s | %s | %s |" % (n, s, i, h, pth, d, a, D) for n, s, i, h, pth, d, a in rows)
assert all("|" not in "".join(r[1:]) for r in rows)
t = t.replace(last, last + "\n" + add)
ls = t.split("\n"); k = [i for i, x in enumerate(ls) if x.startswith("| agyaudit |")]; assert len(k) == 1
c = [x.strip() for x in ls[k[0]].strip().strip("|").split(" | ")]; assert c[2] == "`d9a04edd`", c[2]
c[2] = "`18c60704`"; c[3] = "%s (B1832): rows 1549 (the branch digested; Theorems 23–28) — before: %s" % (D, c[3]); ls[k[0]] = "| " + " | ".join(c) + " |"
H.write_text("\n".join(ls), encoding="utf-8")
print("part 2 applied")
