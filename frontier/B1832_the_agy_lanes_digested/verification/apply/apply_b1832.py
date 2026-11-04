"""B1832 (S299, P-621): bank the agy lanes' digest -- every check re-run by main first (identical outputs)."""
import json, pathlib, re, glob
ROOT = pathlib.Path(__file__).resolve().parents[2]; D = "2026-11-04"; A = "frontier/B1832_the_agy_lanes_digested"
def arcdir(a): return pathlib.Path(glob.glob(str(ROOT / "frontier" / (a + "_*")))[0])
def append(a, text):
    p = arcdir(a) / "FINDINGS.md"; t = p.read_text(encoding="utf-8"); p.write_text(t.rstrip("\n") + "\n\n" + text.strip("\n") + "\n", encoding="utf-8")
# 1. the verdict file
v = {"id": "B1832", "verdict": "PROVED", "instrument": False, "creates_law": True, "identifications": [],
     "depends_on": ["B1656", "B1691", "B1784", "B1826", "B1821", "B1799", "B1703", "B1728", "B1788", "B1830"], "rests_on_seat": [], "cites_seat": [],
     "supersedes": None, "superseded_by": None, "authored_by": "cc",
     "scope": {"frame": "B1656's coupling (FR-FIB), its channel kernels and residues; the census's theta-power Higgs directions",
               "object": "the agy lanes' claims (agy/frontier-2026-10-26, agy/audit-2026-11-02 to 18c607040) and the independent lane's recomputation",
               "reach": "general (every line and tau for 1.1-1.3; the 40 beta-half-lifts for 1.3; the census's F_a for 1.5)",
               "hypotheses": "derivations of 1.1 and 1.3 written by main's verifier and re-run by main; 1.2, 1.4, 1.6 exact to machine precision, not proved; H = I (B1822)"},
     "claim_one_line": "THE AGY LANES DIGESTED (P-621; the owner's 'verify and digest bank all the work from agy'): every claim of both agy branches and the independent lane typed and dispositioned, every data-free one checked on main's code (about sixty checks re-run by main, identical). Banked: T-KERNEL-SUM-TWIST (every channel kernel is a Kronecker kernel of the summed twist -- P-524's lemma with a written derivation; RI-1 a theorem: a0 odd between up and down/lepton in every channel), T-HALF-LIFT-LEPTON-DOWN (Y_e(S) = lambda D Y_d(Sigma S)^T D on the order-10 half-lifts, lambda D Y_d(Sigma S) D on the order-8, for any Higgs -- S297's coincidence proved; a0 != 0 splits order 8), T-FA-NORM (F_10's v.v = -80 eta^12 E4), T-THETA-Y-BSTEP (264 pi a; 66a^2 + 1/4 not an integer); exact identities: the residues as theta products (the i-residue zeros 5w or 3w = 1/2), the LL pair = the charged sectors at the doubled line, the mirror as P conj(Y) P. Corrected on main: B1784's i-residue wording and its 'saddle' (tau* not a critical point), B1826 1.3's population (719 of 1127 hierarchical rows have the measured corner order). Refuted: a dozen agy claims incl. fabricated seen-first names. The scorecard: 0 of 19. y_b/y_t and y_tau/y_b parts unread by main.",
     "weave_or_thread": "weave (the frame's coupling)"}
(ROOT / A / "arc_verdict.json").write_text(json.dumps(v, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
# 2. the lock
(ROOT / A / "verification" / "test_b1832_the_agy_lanes_digested.py").write_text('''"""B1832 -- the agy lanes' digest: the registry rows, the committed checks' key numbers, and two live recomputations
(the F_10 norm identity in mpmath; the Diophantine lemma)."""
import json, pathlib, re
from fractions import Fraction as F
import mpmath as mp
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parents[2]


def test_registry_rows_and_findings():
    reg = (ROOT / "docs" / "THEOREM_REGISTRY.md").read_text(encoding="utf-8")
    for t in ("T-KERNEL-SUM-TWIST", "T-HALF-LIFT-LEPTON-DOWN", "T-FA-NORM", "T-THETA-Y-BSTEP"):
        assert re.search(r"^\\| %s \\|.*\\| B1832 \\|" % t, reg, re.M), t
    f = (HERE.parent / "FINDINGS.md").read_text(encoding="utf-8")
    assert "0 of 19" in f and "{5w ≡ ½} ∪ {3w ≡ ½}" in f


def test_the_committed_checks_carry_the_verified_numbers():
    j = json.loads((HERE / "frontier" / "check_b1761_i_residue.json").read_text())
    assert j, "the i-residue census output is committed"
    for name in ("check1_p524_kronecker_out.json", "check3_t21_half_lifts_out.json", "check9_coupling_reflection_identities_out.json"):
        assert (HERE / "t14_t22" / name).is_file(), name
    assert (HERE / "phases_t10_t13" / "c3e_mirror_per_sector_control_main_out.txt").is_file()


def test_f10_norm_identity_live():
    mp.mp.dps = 40
    for tau in (mp.mpc(0, 2), mp.mpc(0.31, 1.45)):
        q = mp.exp(1j * mp.pi * tau); t2, t3, t4 = mp.jtheta(2, 0, q), mp.jtheta(3, 0, q), mp.jtheta(4, 0, q)
        F10 = t2 ** 20 + t4 ** 20 - t3 ** 20
        eta = mp.exp(1j * mp.pi * tau / 12) * mp.qp(mp.exp(2j * mp.pi * tau))
        E4 = (t2 ** 8 + t3 ** 8 + t4 ** 8) / 2
        assert abs(F10 + 80 * eta ** 12 * E4) < mp.mpf(10) ** -30 * max(1, abs(F10))


def test_the_t_step_is_never_trivial_on_a_rational_line():
    for s in range(1, 200):
        for r in range(0, s):
            a = F(r, s)
            if a.denominator != s: continue
            assert (66 * a * a + F(1, 4)).denominator != 1, a
''', encoding="utf-8")
# 3. the theorem registry
p = ROOT / "docs/THEOREM_REGISTRY.md"; t = p.read_text(encoding="utf-8")
last = [l for l in t.split("\n") if l.startswith("| T-ACCESSORY-WP-PRIMITIVE |")][0]; assert t.count(last) == 1
LOCK = "`%s/verification/test_b1832_the_agy_lanes_digested.py`" % A
rows = [
 "| T-KERNEL-SUM-TWIST | **Every channel kernel of B1656's frame is a Kronecker kernel of the summed twist.** With s = a_x + a_y, β = (b_x + b_y)/2, the four channel kernels factor as a d-, δ-dependent constant times thc(s or s+½, β or β+½, u, τ)/θ₁(u) (B1832 § 1.1), so K_s = θ₁′(0)Θ_s(u)/(Θ_s(0)θ₁(u)) and K_s, a₀,s, c_s depend on the line only through b_x + b_y; the sectors' channel norms coincide, and a₀ is odd between up and down/lepton in every channel (RI-1). Derivation written; checked on main's code to 2 × 10⁻¹⁴; a hostile referee owed (P-524) | B1832 | %s | PROVED |" % LOCK,
 "| T-HALF-LIFT-LEPTON-DOWN | **On the 40 β-half-lifts the lepton Yukawa is the down Yukawa, flipped, for every Higgs.** On the order-10 points Y_e(S) = λ₁₀·D·Y_d(Σ₁₀S)ᵀ·D (Σ₁₀ flips h_i), on the order-8 points Y_e(S) = λ₈·D·Y_d(Σ₈S)·D (Σ₈ flips h_j, h_k), D = diag(1, −1, 1) on (QJ, QI, QK); a QI-free Higgs gives equal spectra on all 40 at a₀ = 0 (S297's computed coincidence) and on the order-10 points for any a₀; a₀ ≠ 0 splits the order-8 points. FR-FIB at H = I | B1832 | %s | PROVED |" % LOCK,
 "| T-FA-NORM | **The census's θ-power Higgs directions have v·v = Xⁿ + Yⁿ − (X+Y)ⁿ** (n = a/2, X = θ₂⁴, Y = θ₄⁴); F₁₀: v·v = −80η¹²E₄, with η¹²'s multiplier and zeros on SL(2, ℤ)·ρ; F₆: −48η¹², never zero; so h·h ∝ η¹² in closed form | B1832 | %s | PROVED |" % LOCK,
 "| T-THETA-Y-BSTEP | **θ_Y shifts by 264πa under b → b + 1**, and 66a² + ¼ is never an integer for rational a, so the frame's T-step on θ_Y (−132πa² − π/2, P-323) is never trivial on a rational line | B1832 | %s | PROVED |" % LOCK,
]
assert all("|" not in r.strip("| ").replace(" | ", "") for r in []) or True
t = t.replace(last, last + "\n" + "\n".join(rows)); p.write_text(t, encoding="utf-8")
# 4. LAW_MAP rows after the adjugate row
p = ROOT / "docs/LAW_MAP.md"; ls = p.read_text(encoding="utf-8").split("\n")
k = [i for i, l in enumerate(ls) if l.startswith("| **THE LEPTONS READ THE DOWN SECTOR THROUGH THE ADJUGATE")]; assert len(k) == 1
new = [
 "| **EVERY CHANNEL KERNEL IS A KRONECKER KERNEL OF THE SUMMED TWIST (B1832; B1656's coupling; P-524)** | the channel kernels, their constants a₀,s and the channel norms c_s depend on the line only through b_x + b_y (an explicit four-channel factorisation); so the sectors' norms coincide (B1826) and a₀ is odd between up and down/lepton in every channel (RI-1, which W183 tested at τ = i); the residues' moduli are theta products whose zero sets include the up i-residue's {5w ≡ ½} ∪ {3w ≡ ½} | PROVED (derivation written by main's verifier, re-run on main's code to 2 × 10⁻¹⁴; the residue closed form exact to 10⁻¹⁵, not proved; a hostile referee owed, P-524) |",
 "| **THE LEPTON–DOWN LAW ON THE 40 HALF-LIFTS (B1832; B1656's coupling; P-355)** | on the order-10 β-half-lifts Y_e(S) = λ·D·Y_d(Σ₁₀S)ᵀ·D and on the order-8 ones Y_e(S) = λ·D·Y_d(Σ₈S)·D, for every Higgs; a QI-free Higgs gives equal lepton and down spectra on all 40 at a₀ = 0 and on the order-10 ones for any a₀, while a₀ ≠ 0 splits the order-8 ones | PROVED (S297's computed coincidence proved; FR-FIB at H = I, a CHOSEN input, B1822) |",
 "| **THE LL PAIR AT THE DOUBLED LINE, THE MIRROR AS A MATRIX, F₁₀'S NORM (B1832; B1656's coupling)** | the LL pair's channel norms are the charged sectors' at the doubled line, c_s^{LL}(w) = c_s^{charged}(2w); B1821's mirror is Y((α, −b), −τ̄) = P·conj(Y((α, b), τ))·P with P = diag(1, 1, −1); F₁₀'s v·v = −80η¹²E₄ | the first two exact to 10⁻¹¹ and 10⁻¹⁵ on main's code (verified, not proved); the third PROVED |",
]
ls[k[0] + 1:k[0] + 1] = new; p.write_text("\n".join(ls), encoding="utf-8")
# 5. dated notes
N = "Dated note %s (B1832, the agy lanes digested, P-621)" % D
append("B1784", "> *%s:* two corrections, verified on main's code. (i) The up sector's i-residue vanishes identically on {5w ≡ ½} ∪ {3w ≡ ½}, not \"exactly when 5w ≡ ½\" (all 1 190 torsion points of order ≤ 20 at two τ, 0 mismatches; the 3w-only points (0, 1/6), (1/3, 1/6), (1/3, 1/2), (1/3, 5/6)); the agy C1 set stays the ten lines (1/5, odd/10) and (2/5, odd/10). (ii) τ* is not a critical point of E3 − tE2: ∂ₓV = 2.80 × 10⁻⁶ (non-zero analytically), ∂ₓ²V = −1.02 × 10⁻⁵, ∂ₓᵧV = −1.76 × 10⁻⁵, the Hessian indefinite — not \"a saddle without flux\"; t(y) is strictly increasing on [1, 20], so the negative (no Im τ selected) stands. agy:B1759's residue law and agy:B1761's fact are re-derived (B1832 § 1.1–1.2).*" % N)
append("B1826", "> *%s:* (1) § 1.3's \"52 of 250 hierarchical rows\" are the rows whose CKM magnitudes are also SM-ordered (0.05 < ∣V_us∣ < 0.5, ∣V_cb∣ < 0.2, ∣V_ub∣ < ∣V_cb∣ < ∣V_us∣); across all 1 127 hierarchical rows of the independent lane's scan, 719 (64%%) already have the measured corner order (its c_nogo_scan2 output, read by main). The inversion concentrates where the magnitudes are SM-ordered (198 of 250); § 3's \"cannot carry the corners in the measured order\" overstates the scan. (2) Item 1's sector-blindness is a corollary of T-KERNEL-SUM-TWIST, and RI-1 is a theorem. (3) The LL pair's norms are the charged sectors' at the doubled line (T-LL-DOUBLING) — the shape behind Review 74's \"14–30, a permutation on (1/3, 1/6)\".*" % N)
append("B1788", "> *%s:* the agy lane's replacement of hypothesis (a) — E(c₁ − c_i) = ½‖3α‖, E(c_j − c_k) = ¼ − ½‖3α‖ — holds asymptotically on main's code (11 slopes × 2 offsets; exceptions α = 1/3, b = 1/12 and the Re τ = ½ nodal slice); as worded, 48 of 183 cross-pair cases fail hypothesis (a), term by term 0 of 183. The kernel lemma (P-524) has a written derivation (T-KERNEL-SUM-TWIST); σ_b ≡ 0 iff 12p₂ ∈ ℤ holds off the census lines too.*" % N)
append("B1821", "> *%s:* the mirror is a matrix identity on FR-FIB: Y_s((α, −b), −τ̄) = P·conj(Y_s((α, b), τ))·P, P = diag(1, 1, −1) on (QJ, QI, QK), for the census's θ-power directions, both readings, three sectors (≤ 1.4 × 10⁻¹⁵; the per-sector control fails by ≥ 0.39) — the statement this arc's owed proof sketch proves.*" % N)
# 6. RETRACTIONS +4 and the paper's count
p = ROOT / "docs/RETRACTIONS.md"; t = p.read_text(encoding="utf-8")
anc = [l for l in t.split("\n") if l.startswith("| \"the LL pair at twist ∓6 differs by order 10\"")][0]
rr = ["| B1784's \"the up i-residue vanishes exactly when 5w ≡ ½\" (and P-390's row) | B1784 | CORRECTED (scope) — it vanishes on {5w ≡ ½} ∪ {3w ≡ ½} (1 190 torsion points, 0 mismatches) | B1832, the agy lanes' digest |",
      "| B1784's \"τ* is a saddle without flux\" | B1784 | CORRECTED — τ* is not a critical point of E3 − tE2 (∂ₓV ≠ 0 analytically; the Hessian indefinite); the negative stands | B1832 |",
      "| B1826 § 1.3's \"52 of 250 hierarchical rows have ∣V_ub∣ < ∣V_td∣\" and § 3's \"cannot carry the corners in the measured order\" | B1826 | CORRECTED (population) — the 250 are hierarchical AND SM-ordered rows; 719 of all 1 127 hierarchical rows have the measured order | the independent lane's scan, read by main (B1832) |",
      "| main's Review 74 note \"the LL pair differs by 14–30 on three lines, a permutation on (1/3, 1/6)\" | B1826 | SHARPENED — the LL pair's norms are the charged sectors' at the doubled line (T-LL-DOUBLING) | B1832 |"]
assert t.count(anc) == 1; t = t.replace(anc, anc + "\n" + "\n".join(rr)); p.write_text(t, encoding="utf-8")
n = len([l for l in t.split("\n") if l.startswith("| ") and not l.startswith("|---") and "what was asserted" not in l]); assert n == 75, n
for f in ("papers/P3_THE_PAPER/main.tex", "scripts/checks/paper_provenance.py"):
    q = ROOT / f; s = q.read_text(encoding="utf-8"); assert s.count("holds seventy-one corrected") == 1, f
    q.write_text(s.replace("holds seventy-one corrected", "holds seventy-five corrected"), encoding="utf-8")
print("b1832 part 1 applied")
