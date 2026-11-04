"""P-628: main's own check of every item a reader graded FORGOTTEN (no row, no arc, no tracked document).

Each item is searched with two or more vocabularies over (1) the point register, (2) OPEN_LEADS, (3) every tracked
text file. Hits are listed so main can read them; an item is CONFIRMED FORGOTTEN only if no hit carries it as work
(a hit that merely names the topic is read by hand). Data-free; no values are read.
"""
import re, subprocess, pathlib, json, sys
ROOT = pathlib.Path(__file__).resolve().parents[3]
files = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True).stdout.split("\n")
files = [f for f in files if f.endswith((".md", ".json", ".py", ".txt", ".tex")) and not f.startswith("CC_TO")]
TEXT = {}
for f in files:
    try:
        TEXT[f] = (ROOT / f).read_text(errors="ignore")
    except Exception:
        pass
REG = TEXT.get("docs/POINT_REGISTER.md", "")
OL = TEXT.get("docs/OPEN_LEADS.md", "")

ITEMS = {
 "L240gh":   [r"L240 \(g\)", r"L240 \(h\)", r"fresh reader with only GENESIS", r"Stage 6"],
 "Ue":       [r"\bU_e\b", r"charged-lepton diagonali", r"left diagonaliser of Y_e", r"U_PMNS"],
 "deviation":[r"spectrum of deviations", r"deviation spectrum", r"away from criticality", r"linearis\w+ (the )?trace map at"],
 "BlumeCapel":[r"Blume", r"multicritical", r"tricritical .{0,40}phase diagram"],
 "B477":     [r"B477", r"sterile (obstruction )?class"],
 "B1000art": [r"bridge artifact", r"filling slope.{0,80}owed", r"P5 completeness"],
 "B853trans":[r"B853", r"transcendental spectral ratio"],
 "kkappa":   [r"\(k, ?κ\) plane", r"\(k,κ\)"],
 "WHY_II2":  [r"termination-WHY", r"II-2", r"why the cascade stops"],
 "L81c":     [r"L81 ?\(c\)", r"L81c", r"sister-difference", r"sister.{0,20}trace −3"],
 "posdim":   [r"positive-dimensional class", r"dim H¹\(fib", r"only continuous degrees of freedom"],
 "L159":     [r"L159", r"gerbe"],
 "L151":     [r"L151", r"anchor budget"],
 "AngleA":   [r"cuspidal cohomology", r"rigid (object|route).{0,60}compactification", r"Angle A", r"overlap integrals"],
 "doorC_deg":[r"canonical degree", r"door \(c\)"],
 "FK11curv": [r"FK11.{0,80}curvature", r"K\^\{?[±+-]?½", r"curvature cell"],
 "seedreuse":[r"seed reuse", r"fresh seeds.{0,40}wrong", r"seeds overlap", r"correlated calibration"],
 "tauvocab": [r"τ.{0,10} used for (three|several)", r"three (different )?things.{0,30}τ", r"τ's two roles"],
 "WEAVE927": [r"no effective action", r"effective action of the joint"],
 "FA106":    [r"towers.{0,40}next frame", r"on NO SUPPORT.{0,80}tower"],
 "FA137":    [r"until the nine are decided", r"gauge couplings.{0,60}deferred"],
 "FLGtrig":  [r"§G trigger", r"FRAMING_LEDGER.{0,40}trigger", r"triggers? that would reshape"],
 "Med3I5":   [r"identity left the (value|physics)", r"26% to 2%", r"object's identity"],
 "FL27":     [r"FL-27"],
 "FL04":     [r"FL-04"],
 "clockC":   [r"door C", r"initial law"],
 "angle8":   [r"hyperbolic measure.{0,40}\(τ, ?line\)", r"measure over \(τ"],
 "angle14":  [r"compact hyperbolic internal", r"volume ≫ diameter", r"volume >> diameter"],
 "H06":      [r"H-06", r"index under the mirror's swap"],
 "H08":      [r"H-08", r"flux potential.{0,30}τ", r"non-perturbative.{0,40}τ"],
 "ccrit":    [r"c_crit", r"6π·?h", r"critical c"],
 "eventrace":[r"even-trace thread", r"even trace thread"],
 "PF4":      [r"PF4", r"what exists is read"],
 "L241b":    [r"L241.{0,10}\(b\)", r"marking-keeping instrument", r"instrument that keeps the marking"],
 "L246ph2":  [r"L246.{0,30}Phase 2", r"Phase 2.{0,20}η", r"Phase 3.{0,40}chiral"],
 "nonsplit": [r"sourced non-split", r"non-split configuration"],
 "FK7":      [r"FK7", r"deck (is )?gauged"],
 "codexmap": [r"question map", r"minimal description does not select"],
 "S3hands":  [r"S3 on the ends", r"three fixed points", r"selects tr ?= ?5", r"L3R"],
 "level5":   [r"McKay ladder", r"level 5.{0,40}icosahedral", r"icosahedral read"],
 "goldconv": [r"golden converse", r"metallic family of laws"],
 "nearfixed":[r"near-fixed-point hierarch", r"near fixed point hierarch"],
 "abandoned":[r"abandoned.{0,10}never refuted", r"E15", r"E16", r"Bell test"],
 "orbindex": [r"orbifold holomorphic index", r"holomorphic index of T"],
 "S2E6":     [r"two-loop", r"S₂ of E₆", r"next order.{0,40}vacuum"],
 "DiracLap": [r"Dirac eigenvalues? .{0,40}Laplac", r"Dirac.{0,20}Laplace coincidence"],
 "classS":   [r"class[- ]S.{0,40}(leg|bulk)", r"4d bulk with T\["],
 "E6lvl3":   [r"level-3 TQFT", r"20×20 pair", r"E₆ level 3"],
 "selfcopy": [r"adversarial seat.{0,60}kill test", r"near, not at"],
 "P070":     [r"P-070"],
 "twopoint": [r"two-point term", r"two-point alternative"],
 # chat B
 "radiative":[r"radiative (flavour|flavor|mass)", r"loop[- ]level lift", r"one loop.{0,40}(null direction|massless (left )?state)", r"first generation at two loops"],
 "fastmode": [r"fastest[- ]growing", r"Turing", r"instability spectrum", r"linear[- ]stability spectrum"],
 "min3stab": [r"minimal n .{0,40}self-reference", r"structurally stable.{0,40}3", r"self-reference is structurally stable"],
 "launder":  [r"laundering group", r"H114"],
 "vMpl":     [r"v/M_Pl", r"exponent of order 40", r"transmutation exponent"],
 "coldinst": [r"cold instance", r"fresh[- ]instance", r"from-zero test"],
 "collision":[r"4₁\(5, ?1\)", r"5₂\(5, ?1\)", r"filling collision"],
}
out = {}
for k, pats in ITEMS.items():
    rec = {"register": [], "open_leads": [], "files": {}}
    for p in pats:
        rx = re.compile(p)
        rec["register"] += [m.group(0) for m in rx.finditer(REG)][:3]
        rec["open_leads"] += [m.group(0) for m in rx.finditer(OL)][:3]
        hits = [f for f, t in TEXT.items() if rx.search(t)]
        rec["files"][p] = (len(hits), hits[:6])
    out[k] = rec
    print("%-10s reg=%-3d OL=%-3d  %s" % (k, len(rec["register"]), len(rec["open_leads"]),
          "; ".join("%s:%d" % (p[:22], n) for p, (n, _) in rec["files"].items())))
pathlib.Path(__import__("os").environ.get("VERIFY_FORGOTTEN_OUT", str(pathlib.Path(__file__).parent / "verify_forgotten_after_rows.json"))).write_text(json.dumps(out, indent=1, ensure_ascii=False))
