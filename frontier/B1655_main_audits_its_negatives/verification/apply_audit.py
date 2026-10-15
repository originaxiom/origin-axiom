#!/usr/bin/env python3
"""B1655 -- apply main's audit of its own negatives (P-152) to the verdict files, the governed pages, the public
refresh blocks, the outside-review page, the kill graph and the audited arcs' FINDINGS. Each edit asserts its anchor is
present exactly once and refuses to apply twice. `--dry` checks every anchor and writes nothing.

    python3 apply_audit.py [ROOT] [--dry]
"""
import glob, json, os, sys
ARGS = [a for a in sys.argv[1:] if not a.startswith("--")]
ROOT = ARGS[0] if ARGS else "."
DRY = "--dry" in sys.argv
TAG = "[Audited by main (P-152, B1655, 2026-10-15):"
PAGE = "*(Audited 2026-10-15, B1655:"
PROBLEMS = []


def _p(*parts):
    return os.path.join(ROOT, *parts)


def verdict(b):
    return glob.glob(_p("frontier", "%s_*" % b, "arc_verdict.json"))[0]


def _save_json(p, d, raw):
    if not DRY:
        open(p, "w", encoding="utf-8").write(json.dumps(d, indent=1) + ("\n" if raw.endswith("\n") else ""))


def claim(b, text):
    p = verdict(b); raw = open(p, encoding="utf-8").read(); d = json.loads(raw); c = d["claim_one_line"]
    if TAG in c or c.count(" 0 of 19.") != 1:
        PROBLEMS.append(("claim", b)); return
    d["claim_one_line"] = c.replace(" 0 of 19.", " " + TAG + " " + text + "] 0 of 19.", 1); _save_json(p, d, raw)


def hypotheses(b, text):
    p = verdict(b); raw = open(p, encoding="utf-8").read(); d = json.loads(raw); h = d["scope"]["hypotheses"]
    if "B1655" in json.dumps(h):
        PROBLEMS.append(("hyp", b)); return
    if isinstance(h, list):
        d["scope"]["hypotheses"] = h + [text]
    else:
        d["scope"]["hypotheses"] = h.rstrip() + " " + text
    _save_json(p, d, raw)


def page(path, anchor, insert, where="after"):
    p = _p(*path.split("/")); s = open(p, encoding="utf-8").read()
    if s.count(anchor) != 1 or insert.strip() in s:
        PROBLEMS.append((path, anchor[:60], s.count(anchor))); return
    s = s.replace(anchor, anchor + insert if where == "after" else insert + anchor, 1)
    if not DRY:
        open(p, "w", encoding="utf-8").write(s)


def swap(path, old, new):
    p = _p(*path.split("/")); s = open(p, encoding="utf-8").read()
    if s.count(old) != 1:
        PROBLEMS.append((path, old[:60], s.count(old))); return
    if not DRY:
        open(p, "w", encoding="utf-8").write(s.replace(old, new, 1))


def findings_pointer(b, grade):
    p = glob.glob(_p("frontier", "%s_*" % b, "FINDINGS.md"))[0]; s = open(p, encoding="utf-8").read()
    if "Audited 2026-10-15 by main (P-152, B1655)" in s:
        PROBLEMS.append(("findings", b)); return
    head, rest = s.split("\n", 1)
    s = head + "\n\n> *Audited 2026-10-15 by main (P-152, B1655): " + grade + " The grades, the corrected wording and the " \
        "checks are in `frontier/B1655_main_audits_its_negatives/FINDINGS.md`.*\n" + rest
    if not DRY:
        open(p, "w", encoding="utf-8").write(s)


# ---------------------------------------------------------------- the verdict files' claim lines
CLAIMS = {
 "B1602": "the exclusivity's failure was the -LLRLRLRR noise, withdrawn (B1604 2b); B1605 certifies the +-LR exclusivity on odd trace at order two; on even trace 'carries' means on some candidate kernel, the forced kernel being unidentified (16 of 42 on some, 26 on none); the NEGATIVE is a failed expectation of generic even-trace content, not a physical negative",
 "B1603": "the readings are pooled over candidate kernels (the even-trace forced kernel unidentified); 120 generation-shaped readings with +LR's 24 after B1604 and B1605, six kinds on certified covers; the NEGATIVE marks a failed expectation of the root's exclusivity, which the weave rule does not need",
 "B1604": "the theorem: no twisted Euler characteristic, and not B1492's class index, carries n_5bar = n_10 on a thread or cover; 'no characteristic class' means no formula I(L2E) = f(I(E)) fits the reliable data; other indices (eta-invariants, L2) are not addressed; not every length-eight odd-trace cover is unreliable (b++LLLLLLLR is certified); the lock's vacuous clause ('or True') repaired",
 "B1606": "+-3 holds when the end condition keeps the parity grading, with dim Lambda_+ - 3 taken as stated; W23 and W24 are the seat's, registered at headline level and not verified on main; the weave's object = M_{1,2} is the seat's reading; 'the hand forced at the puncture' means that a hand exists, not which",
 "B1615": "with one Higgs irreducible at a time and a vacuum fixed by RL, L, R or RRL; with several irreducibles the masses are free (C5; B1620); the exact sum rule m1 + m2 = m3 is structure (B1636's golden spectrum obeys it), not a failure",
 "B1616": "for the four elements RL, L, R, RRL, in the frame where the central phases are physical (RRL carries e^{i pi/4}, so Sym^2 T has no fixed content there); B1620 finds 16 Sym^2-viable subgroups",
 "B1617": "the residual of order 48 includes the inner automorphisms, which on the ruled branch are not moves (there the residual at omega is cyclic of order 12, B1634); the near-omega clause has no cell -- no spectrum near omega was computed -- and the near-fixed-point mechanism's input, distinct residual charges, is what Z4 found; tau = omega is retired only as 'no hierarchy found at omega' (B1640)",
 "B1618": "the headline holds where the inner automorphisms act; on the ruled branch no hierarchy was found in samples and the near-omega regime is not computed; the JSON flag every_spectrum_degenerate on the empty Majorana set is vacuous",
 "B1620": "'reduces none' means none compatible with the data: 2916 of 3249 T-bar(x)T pairs have a family below four parameters, none reaching the CKM, and the PMNS reaches the data at two; the decisive clauses are post-seal (A3 as sealed computed a minimal freedom of 0, which cannot fail); exact residuals, one tensor per pair; the tau-only clause holds where the inner automorphisms act",
 "B1628": "the NEGATIVE marks main's failed expectation that the global fit excludes TM2 at 3 sigma; TM1 passes (0.85 sigma on NuFIT 6.0, 1.04 on JUNO's first measurement); it is not a failure of the relation",
 "B1633": "the closing sentence is wider than computed: one coupling kind (the zero-mode projector) under one measure (uniform words); B1635-B1636 found a value-fixing coupling (golden masses on the tick's geodesic) days later",
 "B1635": "'every coupling degenerate at omega' is false for T-bar(x)T and mixed T(x)T by this arc's own K5 read-outs (booked: E53 #31); every single piece of T(x)T is degenerate at omega for k <= 11; the NEGATIVE marks a failed threshold and a failed prediction, and the failure is the golden-spectrum discovery",
 "B1641": "'exactly the golden pattern' is the support (zero diagonal) only: the symmetric c and the antisymmetric epsilon both obey the parity rule, and B1642 shows the zero modes give epsilon",
 "B1642": "a feature booked as a failure: the coupling is rank two with an exact massless direction along the theta-triplet, the pattern a light first generation needs (B1644-B1653); what fails is the preregistration's symmetric assumption (E1) and the golden pattern; 'the zero modes give no flavour structure' (the addendum, B1643's C6) is withdrawn",
 "B1643": "not exhaustive: B1075 (a sealed crossing, a MISS), B1126 and the 0.15-sigma near-match of sin^2 theta12 to 1/(2 phi) disclosed in B856 and B1075 are absent; 'three independent routes' is two (the audit lane's was sealed from B1642's public preregistration); C6 inherits B1642's withdrawn sentence; the lock's bite is tautological",
 "B1644": "a feature booked as a failure: the NEGATIVE is S3b's failed |q| prediction (an uncomputed second-order step); the exact zero it found is the leading-order structure a light first generation needs; 'golden impossible' is for the leading-order adjoint-Higgs coupling at one tau; the sealed rule 'the adjoint Higgs is excluded as the flavour source' was never applied, and B1645-B1654 build on M",
 "B1645": "m is a mass ratio given a kinetic metric proportional to the identity on the three zero modes (T-NORM, by hand at B1654 1.11)",
 "B1646": "'never between' holds for a quartic potential: one octic invariant, or the zero modes' own one-loop term, puts minima between the cone and the real locus (the audit's check, reproduced on main: B1655 verification/check_potential.py); only real units were tested as vacua; 'nothing on the record fixes the direction' leaves the SM seat's cusp reading (P-113, isotropic eigenlines) unexamined",
 "B1648": "its declared coverage of B1642 and B1644-B1646 is now applied to their scope hypotheses (B1655)",
 "B1649": "the frame dependence (the surface frame's W72; E8's flavon) is in its addendum, not FINDINGS; 'the zeros are Jacobi's' is superseded by B1653 (a twist makes R.R non-zero and the zero persists): the zero is a point coupling's",
 "B1651": "'the puncture is not forced' holds for a point or density Higgs (premise P1, tested by no cell); a smooth (0, 1) Higgs carrying a parity couples at the puncture, forced at the price of one framed datum per parity (its addendum of 2026-10-14), the typing B1654 adopts",
 "B1652": "no frame is SHOWN to satisfy every demand: D3, D4 and D8 are open, untested or failing in every column, so outcome 2 could not have come out otherwise; F1/D5 is graded FAIL where the demand is 'a hierarchy possible'; F2's 'forbids CP violation' rests on W74 alone, and its hypercharge is UNTESTED in the table",
 "B1653": "'this explains the frame dependence' is withdrawn (its own S129 correction): W72's lift is this arc's two-point mechanism carried in tau, not a fibre profile, and where R is a matter mode the tau-integral cannot lift the zero (the web seat's step 3a)",
 "B1654": "the first clause rests on the SM seat's C0; P4's exact equality of the three channels' amplitudes is fine-tuned: at tau = i, L = 40 a 1% error in one channel doubles m1/m3 (4.9e-4 to 1.07e-3) and 10% multiplies it by 15 (the audit's check, reproduced on main)",
}
for b, t in CLAIMS.items():
    claim(b, t)
B1648_COND = "B1648's conditions, applied by B1655: the record's hand; the lifts' agreement with the ruled moves checked at Delta^4 alone (Gate 12 owed); M_{1,2} as the weave's surface, the SM seat's reading."
for b in ("B1642", "B1644", "B1645", "B1646"):
    hypotheses(b, B1648_COND)

# ---------------------------------------------------------------- the public refresh blocks (six pages, one text)
OMEGA = (" " + PAGE + " computed where the inner automorphisms act; on the ruled branch τ = ω is retired only as \"no "
         "hierarchy found at ω\" (B1640), and the near-ω regime is uncomputed.)*")
NONE13 = (" " + PAGE + " none compatible with the data, under exact residuals with one tensor per pair; 2916 of 3249 "
          "T̄ ⊗ T pairs do reduce the count, none reaching the CKM; the τ-only clause holds where the inner automorphisms act.)*")
NOFLAV = (" " + PAGE + " withdrawn — the coupling is rank two with an exact massless direction, the pattern a light first "
          "generation needs (B1644–B1653); it gives no 2–3 hierarchy and no golden pattern.)*")
for f in ("README.md", "ROADMAP.md", "docs/MASTERPLAN.md", "docs/OPEN_PROBLEMS.md", "docs/LEAD_REGISTER.md", "docs/PRICED_DOORS.md"):
    page(f, "(B1617, B1618) and is retired as tested (GENESIS v1.35).", OMEGA)
    page(f, "parity grading (B1620).\n", NONE13.strip() + "\n", where="after")
    page(f, "the SM seat and the audit lane found independently.", NOFLAV)

# ---------------------------------------------------------------- the outside-review page
DS = "docs/THE_DERIVED_STRUCTURE_FOR_REVIEW.md"
page(DS, "The postulate is retired as tested (GENESIS v1.35).",
     " " + PAGE + " this paragraph was computed where the inner automorphisms are symmetries. On the owner's ruled branch "
     "they are not moves; there the residual at ω is cyclic of order 12 with three distinct charges, only the single "
     "pieces of T ⊗ T are degenerate at ω, and no spectrum near ω has been computed. τ = ω is retired only as \"no "
     "hierarchy found at ω\" (B1640, GENESIS v1.46).)*")
page(DS, "  - **The weave's symmetry reduces none of the 13.**",
     " " + PAGE + " none compatible with the data; under exact residuals, one tensor per pair.)*")
page(DS, "and couplings in τ alone give permutation mixing (B1620).",
     " " + PAGE + " where the inner automorphisms act.)*")

# ---------------------------------------------------------------- the crossings census
CC = "docs/THE_CROSSINGS_CENSUS_2026-10-13.md"
page(CC, "but antisymmetric or degenerate: no flavour structure (three routes agree).",
     " " + PAGE + " withdrawn: rank two with an exact massless direction; no 2–3 hierarchy, no golden pattern; two routes are independent.)*")
page(CC, "the audit lane's residue audit). The hierarchy needs a datum acting on the multiplicity M (P-105).",
     " " + PAGE + " \"no flavour structure\" is withdrawn — the coupling is rank two with an exact massless direction "
     "(B1644–B1653); two of the three routes are independent; the census also omits B1075, B1126 and the near-match "
     "disclosed in B856.)*")

# ---------------------------------------------------------------- THE_WEAVE
W = "docs/THE_WEAVE.md"
swap(W, "NEGATIVES — no index on a thread (B1604);",
     "NEGATIVES — no index on a thread (B1604: no twisted Euler characteristic and not the class index; B1655);")
page(W, "the charged leptons' hierarchy is out of reach.",
     " " + PAGE + " with one Higgs irreducible at a time along RL, L, R or RRL; with several the masses are free.)*")
page(W, "with B1611, B1612, B1615, no flavour value at all.",
     " " + PAGE + " along the four elements tested, where the central phases are physical; B1620 finds 16 Sym²-viable subgroups.)*")
page(W, "quasi-degenerate, not the\n  observed hierarchy.",
     " " + PAGE + " this near-ω clause has no cell — no spectrum near ω was computed; on the ruled branch the residual at "
     "ω is cyclic of order 12 and τ = ω is retired only as \"no hierarchy found at ω\".)*")
page(W, "**The weave's symmetry reduces none of the 13 flavour parameters.**",
     " " + PAGE + " none compatible with the data — 2916 of 3249 T̄ ⊗ T pairs have a family below four parameters, none "
     "reaching the CKM; exact residuals, one tensor per pair; the decisive clauses are post-seal.)*")
page(W, "is (k+1)/2^k at every length, with no atom.",
     " " + PAGE + " the limit, within 2.4% at n = 10, under the uniform word measure, which is not the geodesic flow's.)*")
page(W, "among the genuine rescalings it is 0 for five and 1 for one.",
     " " + PAGE + " refuted in part by B1634: the helper's sign on S̃; the lifts form a genuine representation of Mp2(ℤ).)*")
page(W, "and none\n  fixes one.",
     " " + PAGE + " one coupling kind under one measure; B1635–B1636 found a value-fixing coupling days later.)*")
page(W, "mixing at a generic τ, every coupling degenerate at\n  ω.",
     " " + PAGE + " single pieces of T ⊗ T only; T̄ ⊗ T and mixed T ⊗ T are not degenerate at ω — B1640 cell A.)*")
page(W, "This is an instance of B990's law that an invariant cannot pick a\n    point on its orbit.",
     " " + PAGE + " for a quartic potential; an octic invariant or the zero modes' own one-loop term gives minima "
     "between; only real units were tested as vacua.)*")
page(W, "**Every structure that fits needs 21 or more parameters for 13 numbers.**",
     " " + PAGE + " the fits near Im τ 6.6–7.1 are most likely artifacts (the 2026-10-14 addendum); 25 in the reliable region; P-144.)*")
page(W, "## Main's addition: where a Higgs can couple (B1651, PROVED) — Step 4 answered: the puncture is not forced\n",
     "\n" + PAGE + " for a point or density Higgs, B1651's premise P1. A smooth (0, 1) Higgs carrying a parity couples at "
     "the puncture, forced at the price of one framed datum per parity — B1651's addendum, the typing B1654 adopts.)*\n")
page(W, "This explains W72's rank 3 (an overlap) against B1649's zero (a point).",  # retracted phrases, quoted to lock or bracket them
     " " + PAGE + " withdrawn by B1653's own S129 correction — W72's lift is the two-point mechanism carried in τ, not a "
     "fibre profile, and where R is a matter mode the τ-integral cannot lift the zero.)*")
page(W, "## Main's addition: the frame tribunal (B1652) — no frame survives on its own; the parent is a specification\n",
     "\n" + PAGE + " no frame is SHOWN to satisfy every demand; D3, D4 and D8 are not computed positively for any frame, "
     "so outcome 2 could not have come out otherwise.)*\n")

# ---------------------------------------------------------------- LAW_MAP and THEOREM_REGISTRY
LM = "docs/LAW_MAP.md"; TR = "docs/THEOREM_REGISTRY.md"
swap(LM, "W46's index table n(|Λ₊| − 3) verified on", "W46's index table n(∣Λ₊∣ − 3) verified on")
swap(LM, "| PROVED (B1641; T-FIBRE-LOOPS-PARITY) |",
     "| PROVED (B1641; T-FIBRE-LOOPS-PARITY); audited (B1655): \"exactly the golden pattern\" is the support (zero diagonal) only |")
swap(LM, "| PROVED (B1606; the grade a ruling under THE_BAR) |",
     "| PROVED (B1606; the grade a ruling under THE_BAR); audited (B1655): ±3 when the end condition keeps the parity grading; W23 and W24 registered, not verified on main; M₁,₂ the seat's reading |")
swap(LM, "never between; the units give m ≥ ½",
     "never between (for a quartic potential: an octic invariant or the zero modes' own one-loop term gives minima between, B1655); the units give m ≥ ½")
swap(LM, "| PROVED (B1651; T-PUNCTURE-NOT-FORCED) |",
     "| PROVED (B1651; T-PUNCTURE-NOT-FORCED); scoped (B1655): for a point or density Higgs (premise P1); a (0, 1) Higgs carrying a parity couples at the puncture, forced at one framed datum per parity (B1651's addendum) |")
swap(LM, "| PROVED as a compiled verdict (B1652) |",
     "| PROVED as a compiled verdict (B1652); audited (B1655): no frame is SHOWN to satisfy the demands; D3, D4 and D8 are computed positively for none, so outcome 2 was foregone |")
swap(LM, "this explains the surface frame's lift (W72) against the fibre frame's zero",
     "W72's lift is this two-point mechanism carried in τ, and where R is a matter mode the τ-integral cannot lift the zero (B1653's S129 correction; B1655)")
swap(TR, "he four-dimensional index is n(|Λ₊| − 3) on main", "he four-dimensional index is n(∣Λ₊∣ − 3) on main")
swap(TR, "Y = [v]× with |v_r| = |θ_r²/(2πη³)|,", "Y = [v]× with ∣v_r∣ = ∣θ_r²/(2πη³)∣,")
swap(TR, "| NEGATIVE as sealed (R4); the identities PROVED numerically to 10⁻⁴⁰ |",
     "| NEGATIVE as sealed (R4); the identities PROVED numerically to 10⁻⁴⁰; audited (B1655): a feature — rank two with an exact massless direction; \"no flavour structure\" withdrawn |")
swap(TR, "across the eight kinds)", "across the eight kinds; six on certified covers, B1605, B1655)")
swap(TR, "or on the real locus (λ₂ < 0, m ∈ [½, 1]), never between. | B1646",
     "or on the real locus (λ₂ < 0, m ∈ [½, 1]), never between — for this quartic potential (an octic invariant or the zero modes' own one-loop term gives minima between; B1655). | B1646")
swap(TR, "at χ² ≤ 13, the smallest P = 21. An optimizer's minimum is an upper bound. | B1637",
     "at χ² ≤ 13, the smallest P = 21. An optimizer's minimum is an upper bound. [The 2026-10-14 addendum, carried by B1655: the fits near Im τ 6.6–7.1 are most likely numerical artifacts of the forms' truncation; F2 is suspended; in the reliable region the smallest P is 25; F4 and F5 are to be re-graded, P-144.] | B1637")
swap(TR, "| PROVED (every cell as sealed; the exact law to 2·10⁻¹⁶; a swapped-matrix control fails) |",
     "| PROVED (every cell as sealed; the exact law to 2·10⁻¹⁶; a swapped-matrix control fails); scoped (B1655): for a point or density Higgs (premise P1, tested by no cell); a (0, 1) Higgs carrying a parity couples at the puncture (B1651's addendum) |")

# ---------------------------------------------------------------- the kill graph's printed sealed text (CLOSED_DOORS)
KG = _p("frontier", "B738_pathfinder_compiler", "kill_graph.json")
KILL = {
 "B1632": " [Audited, B1655: refuted in part by B1634 -- the helper's sign on S~; the lifts form a genuine representation of Mp2(Z).]",
 "B1635": " [Audited, B1655: 'at omega for every k' holds for the single pieces of T(x)T only; the failed cell is the golden-spectrum discovery.]",
 "B1642": " [Audited, B1655: a feature -- rank two with an exact massless direction, the pattern a light first generation needs.]",
 "B1644": " [Audited, B1655: a feature -- the exact zero is the leading-order structure a light first generation needs; 'golden impossible' is for the leading-order adjoint-Higgs coupling at one tau.]",
 "B1629": " [Audited, B1655: 'not dynamical' for forced data and bounded observables under the uniform word measure, which is not the geodesic flow's.]",
}
raw = open(KG, encoding="utf-8").read(); g = json.loads(raw)
for r in g:
    if r.get("id") in KILL:
        if "B1655" in r["kill_form"]:
            PROBLEMS.append(("kill", r["id"])); continue
        r["kill_form"] = r["kill_form"] + KILL[r["id"]]
if not DRY:
    open(KG, "w", encoding="utf-8").write(json.dumps(g, indent=1, ensure_ascii=False) + ("\n" if raw.endswith("\n") else ""))

# ---------------------------------------------------------------- pointers on the audited arcs' FINDINGS
GRADES = {
 "B1602": "WRONG AS WORDED for the exclusivity (withdrawn: B1604, B1605); the rest STANDS ONLY AS SCOPED (candidate kernels).",
 "B1603": "STANDS ONLY AS SCOPED (candidate kernels; six kinds; 120 readings with +LR's).",
 "B1604": "STANDS ONLY AS SCOPED (Euler characteristics and the class index); a real obstacle within that scope; its lock's vacuous clause repaired.",
 "B1606": "the cells HOLD; the grade STANDS ONLY AS SCOPED (the parity grading kept; W23, W24 unverified on main).",
 "B1615": "STANDS ONLY AS SCOPED (one irreducible at a time, four elements); the sum rule is structure.",
 "B1616": "STANDS ONLY AS SCOPED (four elements, the frame where the central phases are physical).",
 "B1617": "STANDS ONLY AS SCOPED (the inner automorphisms act, exactly at ω); the near-ω clause has no cell.",
 "B1618": "STANDS ONLY AS SCOPED (the inner automorphisms act); the headline is wrong on the ruled branch; near ω not computed.",
 "B1620": "a REAL OBSTACLE for the CKM against exact residual patterns; STANDS ONLY AS SCOPED (exact residuals, one tensor per pair); the decisive clauses are post-seal.",
 "B1628": "HOLDS AS WORDED; the NEGATIVE label marks main's failed expectation, not a failure of TM1.",
 "B1629": "STANDS ONLY AS SCOPED; \"not dynamical\" is wrong as worded on this page (the claim line carries the scope).",
 "B1630": "STANDS ONLY AS SCOPED (the inner automorphisms act; B1648).",
 "B1632": "WRONG AS WORDED in the headline (refuted in part by B1634); the calibrations stand.",
 "B1633": "the computation HOLDS; the closing sentence is wider than computed.",
 "B1635": "STANDS ONLY AS SCOPED; one sentence wrong as worded (booked); the failed cell is the golden-spectrum discovery.",
 "B1637": "STANDS ONLY AS SCOPED (P ≥ 25 in the reliable region; T ⊗ T, odd weights {3, 5, 7}³, Im τ ≤ 10, search-bounded).",
 "B1641": "STANDS ONLY AS SCOPED (\"exactly the golden pattern\" is the support only).",
 "B1642": "a FEATURE PRESENTED AS FAILURE: rank two with an exact massless direction; \"no flavour structure\" withdrawn.",
 "B1643": "STANDS ONLY AS SCOPED (the rows read; not exhaustive; two independent routes).",
 "B1644": "a FEATURE PRESENTED AS FAILURE: the exact zero is the pattern a light first generation needs; \"golden impossible\" is leading order at one τ.",
 "B1646": "STANDS ONLY AS SCOPED: \"never between\" holds for a quartic potential; wrong as worded where carried unqualified.",
 "B1651": "STANDS ONLY AS SCOPED: \"not forced\" holds for a point or density Higgs (premise P1).",
 "B1652": "STANDS ONLY AS SCOPED: no frame is shown to satisfy the demands; outcome 2 was foregone.",
 "B1653": "HOLDS AS WORDED, except \"explains W72\", withdrawn by its own S129 correction.",
}
for b, gr in GRADES.items():
    findings_pointer(b, gr)

if PROBLEMS:
    print("PROBLEMS:"); [print(" ", x) for x in PROBLEMS]; sys.exit(1)
print("dry run: every anchor once" if DRY else "applied")
