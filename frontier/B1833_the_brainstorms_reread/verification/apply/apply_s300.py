"""S300: B1833 THE BRAINSTORMS RE-READ (P-628) + the sealed exhibits' value-free mathematics banked (P-624 step 1;
P-625 answered and put to the owner; P-355 and B1832 § 2 corrected). Run once from anywhere."""
import pathlib, re, glob, shutil, json, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]; D = "2026-11-04"
def arcdir(a): return pathlib.Path(glob.glob(str(ROOT / "frontier" / (a + "_*")))[0])
def append(path, text):
    t = path.read_text(encoding="utf-8"); path.write_text(t.rstrip("\n") + "\n\n" + text.strip("\n") + "\n", encoding="utf-8")
def replace_once(path, old, new):
    t = path.read_text(encoding="utf-8"); assert t.count(old) == 1, (path, old[:80]); path.write_text(t.replace(old, new), encoding="utf-8")

# ---------------------------------------------------------------- 1. B1832: the masked checks, scrubbed, and the S300 section
SRC = ROOT / "audit/agy_digest/sealed/checks"; DST = arcdir("B1832") / "verification" / "sealed_mask"; DST.mkdir(exist_ok=True)
for f in sorted(SRC.iterdir()):
    if f.suffix not in (".py", ".txt") or f.name.startswith("_"):
        continue
    s = f.read_text(encoding="utf-8")
    s = s.replace('pathlib.Path("%s")' % ROOT, "pathlib.Path(__file__).resolve().parents[4]")
    s = s.replace('ROOT = "%s"' % ROOT, "ROOT = str(__import__('pathlib').Path(__file__).resolve().parents[4])")
    s = s.replace(str(ROOT) + "/", "").replace(str(ROOT), ".")
    assert str(ROOT) not in s, f.name
    (DST / f.name).write_text(s, encoding="utf-8")
(DST / "README.txt").write_text(
    "The firewalled reader's value-free checks of the agy lanes' sealed exhibits (P-624 step 1, 2026-11-04), re-run on main.\n"
    "The reader read the sealed regions through a mask stricter than the binding rule (every digit hidden near a trigger\n"
    "word, every decimal everywhere); no value of y_b/y_t, y_tau/y_b or tan beta reached main. c4 executes the lane's own\n"
    "matrix-construction lines (toe_closure.py 3123-3196 at the archive tag archive/agy-audit-2026-11-02, which stays in\n"
    "main's local repository) after checking the region's sha256 against SEALED_EXHIBITS.json; every claim about the\n"
    "matrices is then verified with main's own code. The others import main's frame code (B1821, B1827). *_run.txt are\n"
    "the outputs as run on main.\n", encoding="utf-8")
append(arcdir("B1832") / "FINDINGS.md", r"""
## S300 — the sealed exhibits' value-free mathematics, read through the mask (P-624 step 1; 2026-11-04)

A firewalled reader read every sealed region through a mask (`verification/sealed_mask/README.txt`) and wrote nine
value-free checks on main's code; main re-ran each (`verification/sealed_mask/*_run.txt`). No value, sign or bound of
y_b/y_t, y_τ/y_b or tan β reached main; the reader lists six qualitative phrases that reached *its* context, written nowhere.

- **The channel-exponent law (new; LAW_MAP).** Each channel residue decays as e^{−2π Im τ E} with E fixed by the bilinear's
  four entries e_ab = ‖q_L α + a/2‖² + ‖q_R α + b/2‖² − 1/8 (a, b ∈ {0, 1}): channels j, k take min(e₀₀, e₁₁), channels 1, i
  take min(e₀₁, e₁₀), independent of Re τ and of the offset. Within a sector the gap is 3/20 (up) and 1/20 (down = lepton)
  on α = 2/5, and 1/20 in every sector on α = 1/5; the up sector's R₁ and R_i vanish exactly at the strip's special offsets
  (B1703; § 1.2). Verified on main's residues at Im τ = 14 and 20, five offsets, two Re τ: 60 rows, worst deviation 0
  (`c2_exponent_law.py`). Not proved here (it follows from the residues' theta-product form, § 1.2). The cross-sector
  exponent was deliberately not computed (P-585's firewall).
- **The a₀ table (new; P-355; RETRACTIONS).** S297's "lepton and down spectra coincide for EVERY Higgs exactly on B1703's
  d = e points" was scanned at a₀ = 0. With a₀ ≠ 0 read with one sign in both sectors (FR-COV's (−adj S, S, S)) the
  coincidence holds on the plain d = e points (orders 2, 4: 18 + 72 of 18 + 72 draws) and on the order-10 half-lifts (144 of
  144), and fails on the transposed points (order 5) and the order-8 half-lifts, where opposite signs restore it (144 of 144,
  96 of 96). On the transposed points, exactly: Y_e(a₀, h) = λ·Y_d(−a₀, h)ᵀ (10⁻¹⁴), a corollary of B1827's V2
  (`c3_a0_on_the_identity_points.py`).
- **The QI admixture acts at first order (new; refutes the lane's Theorem 21 and relay line 294).** On the order-10 strip
  lines D departs linearly in h_I (doubling ratio 2.000 in 18 of 18 cases; B1742), and so does the third-generation
  lepton/down relation: the down sector's first-order coupling z₃ = u₃†Y_I v₃ is 0.17–0.20 of ‖Y_I‖, and no census direction
  cancels it (0 of 312, both readings) — the lane's "unchanged to O(∣h_i∣²)" is false (`c3b_first_order_hI.py`).
- **§ 2's compensators, corrected (RETRACTIONS).** § 2 said the stabiliser 2D4 is "realised by unitary SO(10, I₁₀)
  elements". Only projectively: the lane's compensators K_i, K_j, K_k lie in SO(10, I₁₀) and generate Z₄ ⋊ Z₄
  (SmallGroup(16,4); three central involutions, twelve elements of order 4) — not Q₈ × Z₂ (Theorem 14's label is wrong) and
  not 2D4 (no element of order 8); its image in PSO(10) is Q₈, and the quaternion relations hold only modulo ±I. The
  chiral-spinor lifts (solved independently from the Clifford intertwining equation; equal to the lane's up to sign)
  generate order 32, with K̂_i⁴ = K̂_j⁴ = −1 and K̂_k⁴ = +1 (`c4_spin10_compensators.py`).
- **The intertwiner is SU(2) covariance.** All 84 F₂ words of length ≤ 3 intertwine the 12 × 12 mass operator; the identity
  holds for every U ∈ SU(2) with arbitrary coefficients (5 × 10⁻¹⁶) and fails for det U ≠ 1 — the word list adds nothing
  (`c5_f2_intertwiner.py`).
- **T², not T, at the residue level.** τ → τ + 1 permutes the five order-10 lines as a 5-cycle but changes the residue
  moduli by 36%, so T is not a frame symmetry; τ → τ + 2m preserves them (≤ 8 × 10⁻¹⁵) and is still a 5-cycle; with the
  census Higgs the full outputs need τ + 8m, as § 1 found (`c8b_tshift.py`).
- **Verified, already on main or trivial:** the residue patterns on the strip with λ = e^{2πi(2−j)/5} (T-HALF-LIFT; 10⁻¹⁴);
  det Y = (h·h)(u₁² + m·m)(h·m) at a₀ = 0 and arg det(Y_u Y_d)'s independence of the Higgs's phase under (S̃, S, S) (B1659's
  joint law at a₀ = 0; `c1_det_factorisation.py`); Q₂ = (17, 5, 45), the lepton/down 9 being (q_L, q_R)_lepton = 3·(−1, 2)
  (reading it as Georgi–Jarlskog's c = 3 is framing); D(η) = e^{2η}·D_raw (a one-parameter fit, so "FORCED" declined);
  U = ((LR)³ − I)/4 locks 16 of 64 8-torsion points per spin character (`c8_arithmetic.py`).

**Bearing on P-597 and P-625.** No sealed region forces a scale. In any two-Higgs reading tan β absorbs y_b/y_t, so y_b/y_t
is a held-out test only in a declared one-Higgs reading with shared normalisation; the card must fix the singular values
(σ_max of each sector's Y), the reading, L, the relative kinetic normalisation and the scale. y_τ/y_b on an order-10 line
moves at first order with the same h_I as D, so its independence from D must be argued (z₃ against z₁, z₂). **P-625:** the
lane's slope selection is not value-free — the within-sector hierarchy holds on α = 1/5 as on 2/5, so what singles out 2/5
is the bottom/top ordering, i.e. the cross-sector exponent that sets y_b/y_t; adopting it spends P-585's last clean held-out
target. Put to the owner (P-625).
""")

# ---------------------------------------------------------------- 2. LAW_MAP, RETRACTIONS, the paper's count, B1830's note
LM = ROOT / "docs/LAW_MAP.md"; t = LM.read_text(encoding="utf-8")
anchor = [l for l in t.split("\n") if l.startswith("| **THE LL PAIR AT THE DOUBLED LINE")][0]
row = ("| **THE CHANNEL-EXPONENT LAW (B1832 S300; B1656's coupling; the agy lane's Theorems 18 B.1, 19 B)** | each channel "
       "residue decays as e^{−2π Im τ E} with E from the bilinear's four entries e_ab = ‖q_L α + a/2‖² + ‖q_R α + b/2‖² − 1/8: "
       "channels j, k take min(e₀₀, e₁₁), channels 1, i take min(e₀₁, e₁₀), independent of Re τ and the offset; within-sector "
       "gaps 3/20 (up) and 1/20 (down = lepton) on α = 2/5, 1/20 in every sector on α = 1/5 — so the within-sector hierarchy "
       "does not single out 2/5 (P-625) | VERIFIED on main's residues (60 rows at Im τ = 14, 20, five offsets, two Re τ; worst "
       "deviation 0), not proved; the cross-sector exponent deliberately not computed (P-585's firewall) |")
t = t.replace(anchor, anchor + "\n" + row, 1); LM.write_text(t, encoding="utf-8")
RX = ROOT / "docs/RETRACTIONS.md"
append(RX, "\n".join([
    "| S297's \"the lepton and down spectra coincide for EVERY Higgs exactly on B1703's d = e points\" (CHANGELOG S297; P-355's note) "
    "| B1830 | CORRECTED (scope) — scanned at a₀ = 0 only; with a₀ ≠ 0 read with one sign in both sectors it holds on the plain "
    "d = e points (orders 2, 4) and the order-10 half-lifts and fails on the transposed points (order 5) and the order-8 "
    "half-lifts, where opposite signs restore it: Y_e(a₀, h) = λ·Y_d(−a₀, h)ᵀ on the transposed points (10⁻¹⁴) | the "
    "firewalled reader's check re-run on main (B1832 S300, verification/sealed_mask/) |",
    "| B1832 § 2's \"the stabiliser 2D4, realised by unitary SO(10, I₁₀) elements commuting with H\" | B1832 | CORRECTED "
    "(scope) — realised only projectively: the compensators generate Z₄ ⋊ Z₄ (SmallGroup(16,4)) in SO(10), whose image in "
    "PSO(10) is Q₈; the quaternion relations hold modulo ±I (the agy lane's \"Q₈ × Z₂\" label also wrong) | B1832 S300 "
    "(verification/sealed_mask/c4_spin10_compensators.py) |"]))
replace_once(ROOT / "papers/P3_THE_PAPER/main.tex", "retractions index holds seventy-five corrected",
             "retractions index holds seventy-seven corrected")
replace_once(ROOT / "scripts/checks/paper_provenance.py", "retractions index holds seventy-five corrected",
             "retractions index holds seventy-seven corrected")
append(arcdir("B1830") / "FINDINGS.md",
       "> *Dated note %s (S300; the firewalled reader's check re-run on main, B1832's S300 section):* the recheck's \"the lepton "
       "and down spectra coincide for EVERY Higgs exactly on B1703's d = e points\" was scanned at a₀ = 0 only. With a₀ ≠ 0 "
       "read with one sign in both sectors it holds on the plain points (orders 2, 4) and the order-10 half-lifts and fails on "
       "the transposed points (order 5) and the order-8 half-lifts, where opposite signs restore it — on the transposed points "
       "exactly Y_e(a₀, h) = λ·Y_d(−a₀, h)ᵀ. RETRACTIONS.*" % D)

# ---------------------------------------------------------------- 3. corrections at source (OPEN_LEADS, the speculation file)
OL = ROOT / "docs/OPEN_LEADS.md"; t = OL.read_text(encoding="utf-8")
old = "its item (b), the Higgs's own twist, answered by B1744 (P-324 DONE)).**"
assert t.count(old) == 1
t = t.replace(old, old + " **[Dated note %s (B1833, P-654): this note mislabels item (b). This lead's own item (b) is \"an "
              "instrument that keeps the marking: the index of a based or framed module\" (Owed, in order) — never built and "
              "still owed; B1744 answered a different question (the Higgs's own twist).]**" % D)
old = "**REVIEW 70 (2026-10-24), R69-7:** (c) THE_CLAIM's restatement and (f) R58, which GENESIS cites and main has not read, are dated next actions by Review 71 (R70-5); (a) the scope tags stay a standing campaign; (g) and (h) are carried as one item with them."
assert t.count(old) == 1
t = t.replace(old, old + "\n\n**Dated note %s (B1833, P-653):** (g) and (h) fell out of the carry — R71-5 and P-428 carried only "
              "(c) and (f), and no register row held (g) or (h). Re-rowed as P-653 [DEBT]." % D)
m = re.search(r"\(8\) \*\(one further item on the private list, structural\)\*\.", t); assert m
t = t.replace(m.group(0), m.group(0) + " **[Dated note %s (B1833): item (1), U_e, was merged into P-283 and died when B1799 "
              "closed P-283 on its own ask — re-rowed as P-638; the eight dispositions drafted in the audit room on 2026-10-23 "
              "were re-checked by the web-era reader and are proposed closures for main to confirm under P-617.]**" % D, 1)
OL.write_text(t, encoding="utf-8")
SP = ROOT / "speculations/S_THE_FIELDS_GENESIS.md"
append(SP, "> *Dated note %s (B1833, P-655):* the table's \"derivation attempted\" (and § 108's \"is attempted in parallel\") "
       "describe a plan, not work done: no derivation of \"what exists is read\" from PF1 and PF2 exists on the record. The "
       "attempt stays owed in P-130 (joined under P-629).*" % D)

# ---------------------------------------------------------------- 4. the register
REG = ROOT / "docs/POINT_REGISTER.md"; text = REG.read_text(encoding="utf-8")
def row_edit(pid, fn):
    global text
    ls = text.split("\n"); k = [i for i, l in enumerate(ls) if l.startswith("| %s |" % pid)]; assert len(k) == 1, pid
    c = [x.strip() for x in ls[k[0]].strip().strip("|").split(" | ")]; assert len(c) == 7, (pid, len(c)); fn(c)
    assert all("|" not in x for x in c), pid; ls[k[0]] = "| " + " | ".join(c) + " |"; text = "\n".join(ls)
def note(pid, s): row_edit(pid, lambda c: (c.__setitem__(5, c[5] + " " + s), c.__setitem__(6, D)))
J = "joined under P-629 (B1833)"
note("P-139", "[S300, B1833: unmoved 2026-10-14 → 11-04 while the question was split across eleven rows with no owner; %s with P-073, P-130, P-572, P-419, P-411, P-422, P-366, P-373, P-384, P-327, P-466, P-475, P-625]" % J)
note("P-073", "[S300, B1833: the same finding as RECOGNITION (2026-07-03), Meditation 3 (10-28) and FL-05/P-572 (11-03), none citing the others; %s]" % J)
note("P-572", "[S300, B1833: the same finding as P-073 (2026-10-13), which this row does not cite; %s]" % J)
note("P-130", "[S300, B1833: the derivation from PF1 and PF2 was never attempted (the speculation file's \"derivation attempted\" corrected, P-655); %s]" % J)
note("P-303", "**[S300, B1833: omitted from main's 2026-10-24 list of everything waiting on the owner (the owner asked for all of them); put to the owner again 2026-11-04]**")
note("P-335", "**[S300, B1833: omitted from main's 2026-10-24 list of everything waiting on the owner; L248 § 8 here is the arithmetic atom the owner asked to take very seriously (2026-10-04); put to the owner again 2026-11-04]**")
note("P-439", "[S300, B1833: the walk-as-dynamics ruling is an owner wait typed [LEAD]; THE_CLOCK's door C (the initial law) is carried only by reader B's note here — P-645]")
note("P-328", "[S300, B1833: L151's MATCH/MISMATCH test (the anchor budget, one dimensionful plus at most one dimensionless input, against B1829's candidate's continuous inputs) never run since 2026-08-10; first step: verify the e20c J rule on main, then count]")
note("P-418", "[S300, B1833: owner-ruled twice (2026-10-29), unbuilt; seventh of B1833's recovered leads; the restated goal's own count]")
note("P-291", "[S300, B1833: its draft (integrity.py, 2026-10-22) lives only in the gitignored audit room — P-656]")
note("P-437", "[S300, B1833: stage 2a lives only in the gitignored audit room — P-656]")
note("P-617", "[S300, B1833: L189's eight dispositions (the audit-room draft of 2026-10-23) re-checked by the web-era reader: item (1) U_e split out as P-638; (2) the quasinormal channel covered by P-287 and B1090/B1704; (3) the Verlinde continuation numerology; (4) L(1, χ₅) answered (B1737, B1832); (5) the ζ₅ base point retired by B728's theorem; (6) the two-input framing subsumed (B1750); (7) s = 1/48 answered (B382, B386, B775, B778, B1199); (8) the Fibonacci-word children classical (Wythoff) — closures for main to confirm here]")
note("P-597", "[S300 (B1832's S300 section): in any two-Higgs reading tan β absorbs y_b/y_t, so it is held out only in a declared one-Higgs reading with shared normalisation; the card fixes the singular values (σ_max per sector), the reading (FR-FIB (S̃, S, S) at a₀ = 0, or FR-COV with a₀ = ∓b₁₀), L, the relative kinetic normalisation and the scale; no sealed region forces a scale; y_τ/y_b on an order-10 line moves at first order with the same h_I as D − 9, so its independence from D must be argued (z₃ against z₁, z₂); a candidate second quantity: U_e and the PMNS (P-638)]")
note("P-355", "**[S300 (B1832's S300 section, the firewalled reader's check re-run on main): S297's \"for EVERY Higgs exactly\" was scanned at a₀ = 0; with a₀ ≠ 0 read with one sign in both sectors the coincidence holds on the plain d = e points (orders 2, 4) and the order-10 half-lifts and fails on the transposed points (order 5) and the order-8 half-lifts, where opposite signs restore it — exactly Y_e(a₀, h) = λ·Y_d(−a₀, h)ᵀ on the transposed points (10⁻¹⁴); a QI admixture moves the third-generation lepton/down relation at FIRST order (no census direction cancels it, 0 of 312); RETRACTIONS; the loop lift P-637 bears on D]**")
note("P-624", "[S300: step (1) DONE — the value-free mathematics extracted through the mask and verified on main (B1832's S300 section; verification/sealed_mask/); nothing firewalled reached main; steps (2), (3) stand]")
def set_disp(pid, disp, where):
    row_edit(pid, lambda c: (c.__setitem__(4, disp), c.__setitem__(5, where + " [was: " + c[5][:300] + "…]"), c.__setitem__(6, D)))
set_disp("P-625", "OWNER",
         "**ANSWERED (S300; B1832's S300 section; the channel-exponent law verified on main):** (1) the value-free conditions do not single out 2/5 — the within-sector hierarchy holds on α = 1/5 as on 2/5 (gaps 1/20 in every sector on 1/5; 3/20 up, 1/20 down = lepton on 2/5); what singles out 2/5 is the bottom/top ordering, the cross-sector exponent that sets y_b/y_t (not computed by main), so adopting the selection spends P-585's last clean held-out target; (2) y_τ/y_b on the half-lift lines moves at first order with the same QI component as D, so it is a second target only with an argued independence and a forced scale (P-574; none in any sealed region). **ASKED OF THE OWNER:** adopt the slope selection (pays P-384's discrete input; P-585 then has no clean target unless P-638 or a forced-scale y_τ/y_b supplies one), or keep 2/5 a priced choice and y_b/y_t held out — main recommends keeping it held out now and revisiting if P-597 finds no second target (then the target cannot confirm anyway). Its 2026-11-04 correction stands: RI-1's sign is a relabelling")
row_edit("P-628", lambda c: (c.__setitem__(4, "DONE"), c.__setitem__(5, "frontier/B1833_the_brainstorms_reread/FINDINGS.md (S300): eight readers over five sources (about 530 ideas: about 340 worked, 80 partly, 45 stalled, 65 with no carrier, each confirmed by main's verify_forgotten.py); twelve mechanisms of loss; the forgotten re-rowed as P-629–P-660; the mechanism put to the owner (P-659), the direction (P-660) [was: " + c[5][:200] + "…]"), c.__setitem__(6, D)))

NEW = [
 ("P-629", "BS, OW", "THE MISSING DYNAMICS AND THE SELECTION OF THE POINT — ONE ROW (B1833 § 3.1): what holds τ and selects the line and the Higgs, named in at least six vocabularies (P-073 the field, THE_WEAVE l. 927 \"no effective action of the joint action has been computed\", B1823's honest limit, P-466 \"no potential on record\", P-475, FL-05/P-572) and split across eleven rows with no owner (P-139 unmoved 10-14 → 11-04): children P-073, P-130, P-139, P-572, P-419, P-411, P-422, P-366, P-373, P-384, P-327, P-466, P-475, P-625, and the handles P-630–P-633", "QUEUED", "[LEAD] Q1 (the umbrella; under P-659's M2 it would not close while a child is open): THE_WEAVE's functional card — from W154/W155 (every admissible content gives V = −(A·E(τ,3) + B·E(τ,2)), running to the cusp) state what the next term must supply, and which coefficients the weave forces"),
 ("P-630", "BS, MA", "THE DEVIATION SPECTRUM AROUND THE CRITICAL OBJECT (main, 2026-07-08: \"masses live in the flow away from criticality … computable, and never computed as a spectrum\"; with the 2026-07-06 Blume–Capel reading of the tricritical point): no row, arc or document since", "QUEUED", "[LEAD] Q1 (with P-629): linearise the trace map at B181's critical locus along the banked deviation directions (B471, B434's CS against slope, chirality per rung) and test whether B1788's exponent set lies in the spectrum; positive control: the tricritical Ising thermal dimensions 1/10 and 3/5 from the golden chain (B220, B222)"),
 ("P-631", "BS", "BEYOND ONE LOOP FOR τ (the chronicle archive (web era), 2026-07-15: at one loop the vacuum sits at the symmetric point and the values live at the next order — never translated when the frame changed): the τ potential on record is one-loop only (B1704, W154), the band needs a 13% content window (P-380) and P-373 asks for a principle for Im τ stated before its check", "QUEUED", "[LEAD] Q1 (with P-629, P-373): inventory, data-free, whether a two-loop vacuum term on the fibre carries τ-dependence outside E(τ,3), E(τ,2); price the couplings' circularity (they enter at two loops); seal the principle before looking at Im τ"),
 ("P-632", "BS", "SELECTION BY THE INSTABILITY SPECTRUM (the chronicle archive (web era), 2026-07-01: selection by the fastest-growing unstable mode, a scale from the ratio of two coupled flows; its in-chat negative on the old circulant frame — the fastest mode is the democratic one — never landed)", "QUEUED", "[LEAD] Q1 (with P-629, P-437): on B1813's s-family of counting rules, or on the frame's flow on τ, the linear-stability spectrum of perturbations; does the fastest-growing or marginal mode pick a τ-locus by itself (e.g. B852's s = 1 transition)? control: the democratic-mode case"),
 ("P-633", "BS, MA", "THE INTERACTING WEAVE'S SWITCH (main, 2026-10-15: all threads sourcing one field; a critical c = 6πh, set by the weave's volume entropy, as the switch between thread and surface phases — called \"the decisive computation\" and \"a breakthrough attempt\"; the sweep main promised and the computation never recorded; P-132 closed piecewise)", "QUEUED", "[LEAD] Q1 (with P-629, P-132, P-488): the sweep (has anyone stated it), then the critical c on the weave's sum, data-free"),
 ("P-634", "BS, MA", "ANGLE A — THE RIGID OBJECT AS THE COMPACTIFICATION (main, 2026-10-28: \"the rigid route was never tried as physics\"): zero modes as automorphic forms, couplings as L-values or overlap integrals on the object, the generation count as a dimension of cuspidal cohomology; the meditation's angle table omits it and \"cuspidal cohomology\" is in no tracked file; P-405, P-416, P-458 and B1794, B1801 touch its edges", "QUEUED", "[LEAD] Q1: dim H¹_cusp of m004's group and of its congruence covers (and with the local systems the frame uses), data-free, with the classical tables for PSL(2, O₋₃) as control; then what a nonzero class would couple to"),
 ("P-635", "BS, MA", "THE POSITIVE-DIMENSIONAL CLASSES (main, 2026-07-08: \"the only continuous degrees of freedom anywhere\"): never computed; its consequence sits in FL-02 and FL-08", "QUEUED", "[LEAD] Q2 (with P-567): dim H¹(fibre, ad) for the frame's flat Q₈ bundle; if positive, price the restriction to finite-order lines as an FL-08 choice and check, data-free, whether moving along the family moves the CKM corner"),
 ("P-636", "BS, OW, MA", "DERIVING THE 3 — THE ROUTES NEVER RUN: (a) 3 as the minimal n at which self-reference is structurally stable, one criterion across arenas (the chronicle archive (web era), 2026-06-29; the owner: \"mark that\"); (b) S₃ on the ends against the hands — what in the genesis selects tr = 5 (L³R, the unique state with three fixed points) other than \"it has three\" (main, 2026-10-07, \"the next sealed cells I propose\"); (c) FK7, the deck gauged or kept (\"one or three\"), a GENESIS fork with no row; (d) the FK11 curvature cell — doublets as K^{±½} sections feel the fibre's curvature (main, 2026-10-28, promised into P-403, left in an untracked note)", "QUEUED", "[LEAD] Q1 (with P-397, P-403, P-460, B1496): (a) state one stability criterion (e.g. the minimal hyperbolic trace) and test whether the record's generation index (dim T given the cusp unit; the Lefschetz count ∣2 − tr∣ = 3) is its minimum, killed if the 3 has an unrelated origin; (b) the sealed cell; (c) FK7's two branches' counts; (d) copy the cell into P-403"),
 ("P-637", "BS", "THE LOOP LIFT OF THE RANK-≤2 YUKAWA (the chronicle archive (web era), 2026-07-01: a radiative flavour ladder — third generation at tree, second at one loop, first at two — run in chat; its result and its owed null test never landed): B1653 proves the point coupling has rank ≤ 2 with a massless left state shared by up and down; a loop lift is sector-dependent (QCD acts on quarks only), so it acts where D fails (P-355) and where P-406's order-one first-generation coefficients are undelivered; P-590's \"D scale-free at one loop\" concerns running, not thresholds", "QUEUED", "[LEAD] Q1 (with P-355, P-406, P-415): sealed and data-free — at B1644's Y_unit, with only the frame's own gauge and Higgs content, is the null direction lifted at one loop or only at two, does the lift break the shared up/down state, and what quark–lepton pattern does it force; the gauge couplings counted as inputs"),
 ("P-638", "BS", "U_e AND THE PMNS IN B1656's FRAME — A CANDIDATE SECOND HELD-OUT QUANTITY (the chronicle archive (web era), 2026-07-15: \"nobody has computed U_e\"; L189 item (1), starred as one of the record's two genuine physics-adjacent gaps; lost by merge into P-283, which B1799 closed without building U_e; B1713 still reads \"PMNS (no neutrino sector)\"): P-597 says the candidate's confirmation is one clean target short", "QUEUED", "[LEAD] Q1 (with P-597, P-611, P-585): data-free — control B1728's consequence U_e^L = (U_d^R)* on the order-5 lines; at the strip (order-10 lines (2/5, b), Im τ ≈ 3, c = 3) and at B1726's rows compute Y_e's left diagonaliser and U_ν with B1799's Dirac pairing (ν^c right charge 0); commit U_PMNS unread; then rule its admissibility (outside the 19), charge the independent lane's unsealed PMNS look (harvest row 1550, LOOK_LEDGER) in m_V, run P-611's budget and seal before any comparison; the neutrino sector's own choices counted (B1616, B1799)"),
 ("P-639", "BS, OW", "THE MIRROR IN MATTER (the owner, 2026-07-04: \"an atom is the self-referential object … it should look for its mirror in matter\"; with 07-21's pre-force patterns in the chord between the object and its negative and 08-19's \"the whole has its own negative branch\"): the substance came back on 2026-11-03 as the adjugate — the leptons see the down quarks through the adjugate and one sector sees the Higgs mirrored (S290, S291) — which the record types a construction choice (FL-06)", "QUEUED", "[LEAD] Q1 (with P-566, P-583, P-627): data-free — the action of B1821's mirror (Y((α, −b), −τ̄) = P·conj(Y)·P, B1832) and of the amphichiral involution on the three sectors' twist data: if it singles out exactly the pair the adjugate links, FL-06's choice is forced and leaves the framing ledger; if not, the choice stays CHOSEN with this as its reason"),
 ("P-640", "BS, MA", "L246's PHASE 2/3 (the η step; the chiral continuous carrier; o10_150709): the record's only route from the proved spin-swap theorems (Theorem A) to a four-dimensional chiral spectrum; main's \"I'd put (a) first\" (2026-10-04) never run; ESCALATED 2026-10-27 to Review 71 with no register row", "QUEUED", "[LEAD] Q2 (with L246): Phase 2's η step on the 34 amphichiral word states (B1481's phase as input), or a dated decline scoped against the weave frame"),
 ("P-641", "BS, MA", "THE EVEN-TRACE THREADS NOT CARRIED INTO THE FIELD STAGE (main, 2026-10-15: they split the triplet (W4) and are studied in B1609, but the field stage reads the odd ones only — half the weave): P-176 listed it and closed on a pointer that does not carry it", "QUEUED", "[LEAD] Q2 (with P-176, P-629): B1656's frame on an even-trace thread's line and τ, data-free: what the triplet split does to the channel norms"),
 ("P-642", "BS", "THE LAUNDERING GROUP (HINT_LEDGER H114, TASK OPEN since 2026-07-08; the chronicle archive (web era)): the conjecture that the observable algebra's character lattice is ℤ/2 — a theorem of what any frame on the object can output, the recognition question of FRAMING_LEDGER § G; with the orphans √3/√35 and the half-chain quasi-invariant", "QUEUED", "[LEAD] Q2: the group the banked launder exhibits generate (the thermodynamic campaign's F's, K020's Galois-orbit moves) on a finite model; test the ℤ/2 conjecture"),
 ("P-643", "BS", "THE FINAL ATTACK's PRE-REGISTERED SUCCESSORS NEVER TAKEN: l. 106 makes the towers' meeting the next frame on NO SUPPORT (B1825 NO SUPPORT 2026-10-31; P-495 closed DONE without a successor; P-415 unmoved since 10-30); l. 137 defers the gauge couplings, the Higgs and θ \"until the nine are decided\" — decided, nothing reopened", "QUEUED", "[DEBT] Q2 (with P-415, P-419): the document states a plan the record did not follow — take each successor (P-419's E₆ meeting-point card; a row for the gauge couplings) or amend THE_FINAL_ATTACK with a dated decline"),
 ("P-644", "BS", "THE FRAMING LEDGER's UNROWED FINDINGS: § G's triggers that would reshape the foundations (main concurred with Q1; Review 74, the \"next review cycle\", silent; Q1 cannot fire while P-418 is unbuilt); FL-04 and Meditation 3 I.5 (the object's identity left the value frame — m004 from 26% to 2% of claim lines; no object-against-rival test); FL-27 (the weave principle against thread tests; only partly in P-582)", "QUEUED", "[LEAD] Q2 (with P-578, P-582, P-579): a row per trigger with its firing condition; one object-against-rival null (the frame on a rival object) as FL-04's test"),
 ("P-645", "BS, MA", "THE UNROWED DOORS: Meditation 3 report B's angle 8 (a measure over (τ, line) with the hyperbolic measure) and angle 14 (a compact hyperbolic internal space, volume ≫ diameter); reader A4's H-06 (the index under the mirror's swap of spin structures, B1480's hatch) and H-08 (non-perturbative or flux potentials for τ, named only inside P-373); THE_CLOCK's door C (the initial law, owed as two frame cards; P-439's note only); door (c), a canonical degree from the record's E₆/E₈ data (main, 2026-10-28; B1794 leaves the degree chosen); Angle B's cheap graviweak test on B1148's carrier (\"deprioritised\", never run)", "QUEUED", "[LEAD] Q3: each gets its first step or a dated decline"),
 ("P-646", "BS, MA", "B1000's THREE BRIDGE ARTIFACTS \"NAMED AND OWED\" (2026-08-09; main: \"reducible in principle, and nobody has tried\"): the filling slope and P5 completeness never reduced (B1410 still consumes P5), the 6d type only partly paid by B1123; with the closing-against-artifact classification never applied to FL-01–FL-18 and P-328's five unruled inputs", "QUEUED", "[DEBT] Q3 (with P-328): apply B1000's classification by referent (does the choice close a named deficit of the object, or is it ours?) to each; every ARTIFACT becomes a reduction attempt"),
 ("P-647", "BS, MA", "THE WHY CAMPAIGN's SIDE CELLS, NEVER RUN (2026-08-11; \"not silently dropped\"): II-2 (why the cascade stops, at mechanism level — what makes \"not any other configuration\" a theorem; B863 proves only that it stops), II-3, II-4/II-5 (\"ledgers before probes\"), III-3 (L81(c): \"the θ-even channel is the sister-difference\"; L145a, the child at depth 5), the Lane II backlog X3–X7", "QUEUED", "[LEAD] Q3: II-2 — from B994 (registerability does the landing) the lemma that every proper descent below the SM kills registerability, run on P-613's SO(10) chains; L81(c) — B1656's channel kernels with the −LR lift (B585) in place of LR, testing for the sector-odd piece P-566 needs"),
 ("P-648", "BS, MA", "THE TERMINAL ERA's SMALLER UNROWED ITEMS (main, 2026-06-26 → 08-12): B477's sterile obstruction classes (OPEN since 07-08, no law, no row); the +j two-world transport cell; the (k, κ) plane (\"second choice\", 07-29); the certified orbits' multipliers; the twist-knot family's Jacobian conductor; the charge tower eₙ's closed form; the child(p) slope→field law; transcendental spectral ratios (B853 \"carried forward\"); forbidding pattern against forbidding pattern (the frame's exact zeros against B1674's anomaly set); the renormalisation fixed-locus reading of the metallic family; L159's Deligne–Milne reading; B433's deferred one-loop leg, which B800 computed (√−3, its square the torsion −3) without a dated note; L86/L87 GATED since 07-16", "QUEUED", "[LEAD] Q7: translate each into today's frame or decline it with a dated reason (the forbidding-pattern comparison first: two incidence structures, a morphism?)"),
 ("P-649", "BS", "THE WEB ERA's SMALLER UNROWED ITEMS (the chronicle archive, 2026-05-19 → 08-19; topics only): the E₆ level-3 TQFT pair invariant on the non-abelian seam; the two-loop E₆ Chern–Simons term (translated in P-631); hearing at n = 4, 6; the class-S second leg (a 4d bulk with T[4₁] as boundary); T[4₁; E₆] (Gate B, specialist-gated, never expiring); the Dirac–Laplace near-coincidences (\"dropped for no reason\"); Turaev–Viro; the anyon and Bianchi-Maass bridges; p-adic regulators, mock modular forms and McKay at roots of unity; the Deligne product; v/M_Pl as an order-40 exponent; the fresh-instance genesis test (3–4 cold instances given only the question); the cost-of-a-closing note's Dehn-slope lead; the 4₁(5,1) ≅ 5₂(5,1) collision as a family; the SL(n) multichannel operator; the many-unit metric question (\"need DMRG\")", "QUEUED", "[LEAD] Q7: translate or decline each with a dated reason; the Dirac–Laplace check first (B940's instrument on m003 as control), since a shared cusp expansion would undercut P-330's instrument"),
 ("P-650", "BS, MA", "MAIN'S SEPTEMBER–OCTOBER SMALLER UNROWED ITEMS: B1466's remainder (the source question — the mixing quartic d — and \"the count is the order\" at the other points and levels); the codex question map's first row REFUTED (minimal description does not select a unique seed independent of encoding — a selection claim bearing on GENESIS, alive only inside L231); the early era's four exact reproductions and two geometric selections absent from the outside-facing record; the L_μ − L_τ pattern's sealed look; the breath as one rhythm (the owner's standing directive); an outside reader's fresh-reader checklist; the Lynn and Sanz Perl re-read; the orbifold holomorphic index of T against T̄ (\"neither seat has run it\"); the abandoned-never-refuted list (E15, E16, E18, the CS-level question, the empirical gates, the DESI fit, the Bell test); the adversarial seat's selection-functional kill test and its \"near, not at\" demand; the web seat's two-point term between threads (closed with no outcome)", "QUEUED", "[LEAD] Q7: translate or decline each with a dated reason; the question map's REFUTED row first (does any GENESIS sentence rely on minimal description selecting the seed?)"),
 ("P-651", "BS, OW", "THE OWNER's PHYSICAL-INTUITION QUESTIONS WITHOUT A FIRST COMPUTABLE STEP (terminal era, 2026-07-04 → 08-19): atoms, cells and the periodic table (\"simulate one atom up to its roots\"); \"i fail to map the process our chain explains to any process in nature\"; where only our object can contribute (map THEOREM_REGISTRY's PROVED rows to named open problems — the certified Maass eigenvalue on a cusped hyperbolic 3-manifold has no paper); measured physics' cycles to infer the bridge; scale and length as the coupling; SM parameters as S-matrix elements; \"why do you persist\"; chaos filtered by the golden at the cusp; the imaginary observer (in substance the orientation torsor)", "QUEUED", "[LEAD] Q3: each gets a first computable step or a dated decline; the nature-process question as a FRAMING_LEDGER row first; the open-problems map next"),
 ("P-652", "BS, OW", "THE OWNER's DEFERRED STRUCTURAL CALLS: the repository split into a lab repository and a clean-argument repository (2026-08-13, \"we need to discuss it\", never discussed); a CLI or API (2026-07-16, 07-29, deferred, never revisited); L86/L87 (object-scale couplings, composites; GATED behind an owner directive since 2026-07-16, never put back, likely superseded by the frame era)", "OWNER", "asked of the owner (S300, B1833): discuss the split; keep or drop the CLI; retire L86/L87 as superseded or reopen"),
 ("P-653", "BS, OW", "L240 (g) AND (h) DROPPED FROM THE CARRY (the foundation lock's last two items, the owner's 2026-10-02 \"lock once for all our genesis work … can we identify our naivities and ignorance\"): (g) Stage 6, the swept page of what the record holds and lacks on dynamics, time, scale, selection, values and the physical vacuum; (h) the test of the whole — a fresh reader with only GENESIS and the README, against sealed questions; Review 70 carried them \"as one item\" with (c), (f); R71-5 and P-428 carried only (c), (f)", "QUEUED", "[DEBT] Q2 (with P-428, P-629): (h) guards GENESIS — write the sealed questions and run one fresh reader; (g) — the swept page, which P-629's children feed"),
 ("P-654", "BS", "L241's ESCALATED NOTE MISLABELS ITEM (b): it says \"its item (b), the Higgs's own twist, answered by B1744\", but L241's item (b) is \"an instrument that keeps the marking: the index of a based or framed module\", never built; the measurer lead's one instrument was marked answered by another question's answer", "DONE", "docs/OPEN_LEADS.md (L241, dated note 2026-11-04); the instrument stays owed under L241 (the measurer lead, standing at the owner's word)"),
 ("P-655", "BS", "THE FIELD-GENESIS SPECULATION SAYS THE PF4 DERIVATION WAS \"ATTEMPTED\": the owner asked (2026-10-14) to state \"what exists is read\" and attempt its derivation from PF1 and PF2 in parallel; no attempt exists on the record", "DONE", "speculations/S_THE_FIELDS_GENESIS.md (dated note 2026-11-04); the attempt stays owed in P-130 (joined under P-629)"),
 ("P-656", "BS", "WORK THAT LIVES ONLY IN THE GITIGNORED AUDIT ROOM OR OUTSIDE THE REPOSITORY, INVISIBLE TO A CLONE: P-291's integrity.py (2026-10-22, the owner's math-integrity check); P-437's stage 2a (2026-10-29, \"not refereed, not landed\"); P-465's computation (in a briefing only); the FK11 curvature design note (2026-10-28); L189's eight dispositions (2026-10-23); a visual artifact of the object built outside the repository (2026-07-02)", "QUEUED", "[PROCESS] Q2 (with P-618, P-291, P-437): land each (refereed, with its instrument) or decline it with a dated reason"),
 ("P-657", "BS, OW", "THE RETRIEVAL TOOLS' BLIND SPOTS: topic_sweep reads none of docs/handoffs/, HINT_LEDGER, OPEN_LEADS, LEAD_REGISTER, speculations/, so items parked there show 0 hits; its eight alias groups cannot join renamed ideas (the object's own scale 07-15 → P-570; the anchored crossing 08-11 → the held-out rule; the mirror in matter 07-04 → the adjugate; the compatible field 06-22 → L254); τ is used for three things with no TERMINOLOGY entry; cross-arc seed reuse (main, 2026-10-23: \"my preregistration's 'fresh seeds' was wrong\") has no rule or error class; and the owner's 2026-08-19 \"4000+ tests … carry the order … retrieve lost breakthroughs\" was never built", "QUEUED", "[PROCESS] Q2: extend topic_sweep's sources and aliases (with a planted control); the TERMINOLOGY entry; the seed rule and its ERROR_LEDGER class; a script listing each lock's first commit and the arc it locks, flagging locks whose claim has no LAW_MAP or THEOREM_REGISTRY row, oldest first"),
 ("P-658", "BS, SE", "THE SEALED EXHIBITS' VALUE-FREE MATHEMATICS BANKED (P-624 step 1): the channel-exponent law (LAW_MAP); the a₀ table and the transposed-point identity Y_e(a₀, h) = λ·Y_d(−a₀, h)ᵀ (S297's scope corrected); the QI admixture at first order (the lane's O(∣h_i∣²) refuted); B1832 § 2's compensators only projective (Z₄ ⋊ Z₄ in SO(10), Q₈ in PSO(10)); the intertwiner as SU(2) covariance; T² not T at the residue level; P-625 answered", "DONE", "frontier/B1832_the_agy_lanes_digested/FINDINGS.md (S300 section; verification/sealed_mask/); docs/RETRACTIONS.md (+2); docs/LAW_MAP.md"),
 ("P-659", "BS, OW", "THE MECHANISM, SO THAT A BRAINSTORM's CONCLUSIONS AGE AND ARE WORKED (P-628's ask; B1833 § 5): M1 direction leads age at 21 days (first step, dated decline, or put to the owner; point_debt rule 7); M2 one owner row per central question, unclosable while a child is open; M3 a merged item keeps its own acceptance cell; M4 every brainstorm, meditation, framing pass and review ends with a carry list rowed the same day, and a FINDINGS \"owed / carried forward / not computed / next\" line needs a row citing its arc; M5 a review's ranked leads become action items under carry-age; M6 OWNER rows printed in every report to the owner, and an audit-room draft cited by a row lands or is declined within seven days; M7 a retired frame's open ideas translated or declined, and a frame card whose free continuous data outnumber the object-fixed invariants graded fit-capacity up front, not the main line without the owner's word", "OWNER", "asked of the owner (S300): adopt M1–M7, some, or none; the rules change what is worked first, so they are the owner's; main's tool repairs proceed under P-657"),
 ("P-660", "BS, OW", "THE DIRECTION: WHICH RECOVERED LEAD FIRST (B1833 § 3's ranked list: P-629 the dynamics and selection, P-638 U_e and the PMNS, P-637 the loop lift, P-639 the mirror in matter, P-634 Angle A, P-636 deriving the 3, P-418 the scoreboard, P-635, P-640–P-642, P-643)", "OWNER", "asked of the owner (S300): main recommends P-638's data-free first step first (it decides P-597, the sixth debt and the candidate's only route off 0 of 19), with P-639 and P-637's one-loop pattern alongside (both data-free and cheap), then P-629's functional card"),
]
ls = text.split("\n"); last = max(i for i, l in enumerate(ls) if re.match(r"^\| P-\d{3} \|", l)); assert ls[last].startswith("| P-628 |")
for pid, origin, body, disp, where in NEW:
    for cell in (body, where): assert "|" not in cell, pid
    ls.insert(last + 1, "| %s | %s | %s | %s | %s | %s | %s |" % (pid, D, origin, body, disp, where, D)); last += 1
text = "\n".join(ls)
# sources legend
old = "**R66** Review 66 (2026-10-21: its reliance census and repairs)."
assert text.count(old) == 1
text = text.replace(old, old + " **BS** the brainstorms re-read (P-628, B1833, 2026-11-04: the chat history and the brainstorm documents); **MA** main's own stated idea or promise.")
# the ranked list: P-625 leaves (OWNER); the three new debts join at the end
ls = text.split("\n"); h = [i for i, l in enumerate(ls) if l.startswith("## The debts, by load")][0]
end = [i for i in range(h + 1, len(ls)) if ls[i].startswith("## ")][0]
ls = [l for i, l in enumerate(ls) if not (h < i < end and re.match(r"^\d+\. P-625 ", l))]
end -= 1
k = h; n = 0
for i in range(h + 1, end):
    m = re.match(r"^(\d+)\. (P-\d+ .*)$", ls[i])
    if m:
        n += 1; ls[i] = "%d. %s" % (n, m.group(2)); k = i
add = ["", "*added by B1833 (S300; the brainstorms re-read):*", "",
       "%d. P-653 — GENESIS's foundation lock has never been tested as a whole (L240 (h)); its swept page of what the record lacks (g) dropped from the carry." % (n + 1),
       "%d. P-643 — THE_FINAL_ATTACK states pre-registered successors (the towers on NO SUPPORT; the gauge couplings after the nine) the record did not take." % (n + 2),
       "%d. P-646 — B1410 consumes P5 completeness, one of B1000's three bridge artifacts named and owed since 2026-08-09." % (n + 3)]
ls[k + 1:k + 1] = add
text = "\n".join(ls)
REG.write_text(text, encoding="utf-8")
fp = ROOT / "scripts/checks/point_debt.py"; s = fp.read_text(encoding="utf-8"); assert "FLOOR = 628" in s
fp.write_text(s.replace("FLOOR = 628", "FLOOR = 660", 1), encoding="utf-8")
print("applied S300")
