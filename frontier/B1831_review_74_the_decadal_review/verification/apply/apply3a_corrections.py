"""Review 74 (S299), apply 3a: corrections verified by main at source this session.
- B1809:129 (the web seat's relations relay; main's own check with B1821's evaluator: audit trail r74_b1809/null_m2.py);
- B1826's S298 claims: the sigma_b and LL-pair instruments now committed (verification/review74/, main's runs, identical to the
  P-086 reader's); 'the LL pair differs by order 10' corrected; the unscoped 'vanishing' bracketed on rows 1510 and 1512;
- the exact-end failure attributed to the web seat's sealed look (P-086 reader's (c) #4; S238's MAIN_VERIFICATION covered
  the data-free half only); row 1459's 'not recomputed on main' corrected."""
import pathlib, re, glob, json
ROOT = pathlib.Path(__file__).resolve().parents[3]; D = "2026-11-04"
def arcdir(a): return pathlib.Path(glob.glob(str(ROOT / "frontier" / (a + "_*")))[0])
def append(a, text):
    p = arcdir(a) / "FINDINGS.md"; t = p.read_text(encoding="utf-8"); p.write_text(t.rstrip("\n") + "\n\n" + text.strip("\n") + "\n", encoding="utf-8")
def rep(rel, old, new, n=1):
    p = ROOT / rel; t = p.read_text(encoding="utf-8"); assert t.count(old) == n, (rel, t.count(old), old[:70]); p.write_text(t.replace(old, new), encoding="utf-8")
def hrow(n, fn):
    p = ROOT / "docs/HARVEST_LEDGER.md"; ls = p.read_text(encoding="utf-8").split("\n")
    k = [i for i, l in enumerate(ls) if l.startswith("| %d |" % n)]; assert len(k) == 1, n
    c = [x.strip() for x in ls[k[0]].strip().strip("|").split(" | ")]; assert len(c) == 8, (n, len(c)); fn(c)
    assert all("|" not in x for x in c); ls[k[0]] = "| " + " | ".join(c) + " |"; p.write_text("\n".join(ls), encoding="utf-8")

# B1809:129
append("B1809", "> *Dated note " + D + " (Review 74; the web seat's THE RELATIONS THE FRAME FORCES, fe2f972cd, checked by main with "
 "B1821's evaluator):* \"Isotropic directions (R, η⁶R, t = −5/288): m₁ ≡ 0 at every L. m₂ ≡ 0 only at L = ∞\" fails on two "
 "classes of lines. On the order-4 lines m₂/m₃ ≤ 4 × 10⁻¹⁴ in every sector; on the order-12 lines it is so in the lepton "
 "sector. Main checked both radii, the eight readings and τ = 0.13 + 2.2i and 0.3 + 1.5i, with the order-5 and order-8 "
 "controls of order one (2 × 10⁻³ to 0.8). Elsewhere the statement stands. This is B1728's table read on the isotropic directions "
 "(rank one on null matter).*")
# B1826: the instruments and the LL pair
append("B1826", "> *Dated note " + D + " (Review 74, P-086's check of S298's 'verified on main'):* the two S298 checks had no "
 "committed instrument; they are now `verification/review74/sigma_b_order8.py` and `ll_pair_norms.py` with their outputs "
 "(main's runs, identical to the review reader's). σ_b on (1/4, odd/8) is ∓0.102 at 0.13 + 1.9i, ∓1.9 × 10⁻⁴ at 0.13 + 3.9i "
 "and ≤ 2 × 10⁻¹¹ at Re τ ∈ {0, 1}, in all three sectors, as S298 stated. **Corrected:** S298's \"the LL pair at twist ∓6 "
 "differs by order 10\" is not the shape. On three of the four lines checked, the LL pair's channel norms differ from the "
 "charged sectors' by 14 to 30. On (1/3, 1/6) at 0.2 + 2.3i they are the charged norms with the channels permuted (1 ↔ i, "
 "j ↔ k), within 0.03. The charged sectors agree to 1.3–4.5 × 10⁻¹² on all four. The title's, the claim line's and item "
 "2's \"the vanishing is exact at finite τ on these slopes\" holds where 12p₂ is an integer (this page's S298 note).*")
vp = arcdir("B1826") / "arc_verdict.json"; v = json.loads(vp.read_text(encoding="utf-8"))
assert "Review 74" not in v["claim_one_line"]
v["claim_one_line"] += " [Review 74: the vanishing on these slopes holds where 12p2 is an integer, not on (1/4, odd/8); the LL pair's norms are not the charged sectors' (verification/review74/)]"
vp.write_text(json.dumps(v, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
SC = "[Review 74: σ_b ≡ 0 only where 12p₂ ∈ ℤ; on (1/4, odd/8) it is non-zero off Re τ ∈ ℤ (RETRACTIONS; B1826's dated notes; instrument B1826 verification/review74/sigma_b_order8.py)]"
for n in (1510, 1512):
    hrow(n, lambda c: c.__setitem__(5, c[5] + " " + SC))
hrow(1510, lambda c: c.__setitem__(5, c[5] + " [Review 74: 'main's code: the read-out and its pulls' — the pulls are checked against B1825's own run.json and referee/node_pulls.py, not recomputed by B1826's scripts]"))
LL = ("[Review 74: the LL pair's instrument is B1826 verification/review74/ll_pair_norms.py; 'differs by order 10' corrected — "
      "it differs by 14–30 on three of four lines checked and is the charged norms with the channels permuted on (1/3, 1/6); "
      "B1826's dated note of 2026-11-04]")
for n in (1512, 1538): hrow(n, lambda c: c.__setitem__(5, c[5] + " " + LL))
hrow(1516, lambda c: c.__setitem__(5, c[5] + " [Review 74: the reproduction's instrument, uncommitted at S298, is B1826 verification/review74/sigma_b_order8.py with its output]"))
hrow(1459, lambda c: c.__setitem__(5, c[5] + " [Review 74: the data-free half (the exact norms 35–38% below the small-cut end) was REPRODUCED on main at S238 (its MAIN_VERIFICATION, the seat's exact_end.py rerun, exit 0); the sealed χ² look 5215f337a was not re-run on main — P-595]"))
# LAW_MAP: the exact-end failure attributed (rows 299, 322, 327, 329, 330, 335) and B1788's row cites the instrument
p = ROOT / "docs/LAW_MAP.md"; ls = p.read_text(encoding="utf-8").split("\n")
ATT = " [the web seat's sealed look, LOOK_LEDGER's THE EXACT END row; not re-run on main — P-595]"
for n in (299, 322, 327, 329, 330, 335):
    l = ls[n - 1]
    if n == 299:
        assert l.count("(they fail)") == 1; l = l.replace("(they fail)", "(they fail" + ATT + ")")
    else:
        assert l.count("the six fail") == 1, (n, l.count("the six fail")); l = l.replace("the six fail", "the six fail" + ATT)
    ls[n - 1] = l
k = [i for i, l in enumerate(ls) if "reproduced on main with B1826's own functions, S298)" in l]; assert len(k) == 1, k
ls[k[0]] = ls[k[0]].replace("reproduced on main with B1826's own functions, S298)", "reproduced on main with B1826's own functions, S298; the instrument committed at Review 74, B1826 verification/review74/sigma_b_order8.py)")
p.write_text("\n".join(ls), encoding="utf-8")
print("apply3a done")
