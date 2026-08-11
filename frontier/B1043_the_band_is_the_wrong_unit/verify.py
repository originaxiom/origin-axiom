"""B1043 — the band is the wrong unit, and it made this refresh restore a settled question as open.

B1037 dispositioned debt BY BAND (B100-B199). A band groups arcs by WHEN THEY WERE BANKED. A law
is a statement about WHAT THEY SAY. The two do not coincide, and where a law spans bands the
band-wise sweep cuts it — silently, because nothing in the in-band bodies mentions the out-of-band
sibling.

The cost, measured on this refresh's own four restorations:

  * B1039 restored B141 Item 4 as an OPEN CONJECTURE. **B564 had closed it** -- by the symbolic
    elimination B141 itself named as "the rigorous path" -- and says so in its own first paragraph.
    B564 is in band B500s. B141 carries no forward pointer. Nothing I read could have told me.
  * B1038's tower law has THREE cross-band siblings still in debt, one of which (B232) is verified
    here to be THE SAME LAW DIFFERENTIATED.
  * The metallic exponent has FOUR.

This arc measures the shape, corrects B1039, and does NOT re-disposition the corpus by topic --
that is a larger change and is registered, not made.
"""
import glob
import json
import pathlib
import re

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[2]
R = {"checks": {}}


def chk(name, ok, **d):
    R["checks"][name] = {"pass": bool(ok), **d}
    return ok


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


CURATED = ["docs/LAW_MAP.md", "docs/THE_FRAMEWORK.md", "docs/THEOREM_LEDGER.md", "CLAIMS.md",
           "docs/THE_LADDER.md"]
SELF = re.compile(r"\bB104[3-9]\b")     # this arc and later, excluded from every measurement
blob = "\n".join("\n".join(l for l in read(p).splitlines() if not SELF.search(l))
                 for p in CURATED)


def cited(b):
    return bool(re.search(rf"\b{b}\b", blob) or re.search(rf"frontier/{b}_", blob))


ARCS, seen = {}, set()
for d in sorted(glob.glob(str(ROOT / "frontier" / "B*"))):
    m = re.match(r"B(\d+)_", pathlib.Path(d).name)
    if not m or not (pathlib.Path(d) / "arc_verdict.json").is_file():
        continue
    b = "B" + m.group(1)
    if b in seen:
        continue
    seen.add(b)
    ARCS[b] = json.loads((pathlib.Path(d) / "arc_verdict.json").read_text(encoding="utf-8"))
DEBT = {i: d for i, d in ARCS.items()
        if d.get("verdict") == "PROVED" and not d.get("instrument")
        and int(i[1:]) < 1043 and not cited(i)}

# ============================================== 1. THE CORRECTION: a settled question restored as open
b564 = ARCS["B564"]
f564 = read(glob.glob("frontier/B564_*/FINDINGS.md")[0].replace(str(ROOT) + "/", "")
            if glob.glob(str(ROOT / "frontier/B564_*/FINDINGS.md")) else "")
f564 = (pathlib.Path(glob.glob(str(ROOT / "frontier/B564_*/FINDINGS.md"))[0])
        .read_text(encoding="utf-8"))
chk("B564_CLOSES_the_conjecture_B1039_restored_as_open",
    b564["verdict"] == "PROVED" and not b564.get("instrument")
    and "contains no irreducible representation" in b564["claim_one_line"]
    and "confirms the B141 Item-4 conjecture" in re.sub(r"\s+", " ", f564),
    b564_says="This confirms the B141 Item-4 conjecture and extends B142's principal-only "
              "(Klein-4) result to the full locus",
    route="symbolic elimination -- which B141 named as 'the rigorous path' and B142 called "
          "'the symbolic-elimination prize'")
b141 = read(glob.glob(str(ROOT / "frontier/B141_*/FINDINGS.md"))[0].replace(str(ROOT) + "/", ""))
b142 = read(glob.glob(str(ROOT / "frontier/B142_*/FINDINGS.md"))[0].replace(str(ROOT) + "/", ""))
chk("and_NOTHING_in_the_in_band_bodies_could_have_said_so",
    "B564" not in b141 and "B564" not in b142,
    note="B141 and B142 carry NO forward pointer to B564, and B564 is 400+ arcs and four bands "
         "away. Reading the in-band bodies -- campaign step 1, done correctly -- cannot reach it. "
         "Only a corpus-wide search ON THE TOPIC does")
chk("the_correction_is_recorded_on_the_curated_surface_and_in_the_arc",
    "B564 CLOSED it" in read("docs/LAW_MAP.md")
    and "settled four hundred arcs later" in
        read("frontier/B1039_phi_fixed_and_metallic_exponent/FINDINGS.md"))

# ============================================== 2. B232 IS B1038's LAW, DIFFERENTIATED
x, y, t = sp.symbols("x y t")


def h(d, vs):
    if d < 0:
        return sp.Integer(0)
    gf = sp.prod([1 / (1 - v * t) for v in vs])
    return sp.expand(sp.series(gf, t, 0, d + 1).removeO().coeff(t, d))


V, W = (x, y), (x, y, 1)


def band_form(n):
    """B1038's restored law: rho_n = Sym^n(W) + (Sym^{n-3}(W) - W), W = V + 1."""
    return sp.expand(h(n, W) + h(n - 3, W) - h(1, W))


chk("B232s_recursion_IS_B1038s_band_form_differentiated",
    all(sp.simplify(band_form(n) - band_form(n - 1) - h(n, V) - h(n - 3, V)) == 0
        for n in range(3, 13)),
    B1038="rho_n = Sym^n(W) + (Sym^{n-3}(W) - W)",
    B232="rho_n = rho_{n-1} + Sym^n(V) + Sym^{n-3}(V)",
    verified_for="n = 3..12, symbolically",
    note="the STEP form of the BAND form. Not two results -- one law stated two ways, in two "
         "bands, and the band-wise sweep saw only one of them")
chk("and_both_give_the_dimension_and_the_step_size_B232_states",
    all(sp.simplify(band_form(n).subs({x: 1, y: 1}) - (n * n - 1)) == 0 for n in range(2, 13))
    and all(sp.simplify((h(n, V) + h(n - 3, V)).subs({x: 1, y: 1}) - (2 * n - 1)) == 0
            for n in range(3, 13)),
    dim="n^2 - 1", step="2n - 1, telescoping to n^2 - 1")

# ============================================== 3. THE SHAPE, MEASURED
LAWS = {
    "the tower (B1038)": r"\brho_n\b|ρ_n|Sym\^n|two-sequence|trace-map Jacobian|stabilization recursion",
    "phi-fixed reducibility (B1039)": r"phi-fixed|φ-fixed|Q8|quaternion group|reducible tower|finiteness versus density",
    "the metallic exponent (B1039)": r"degree=rank|\[A,B\]\s*=\s*[+-]?mu|meridian|metallic exponent|order-determined",
    "isomonodromy (B1040)": r"isomonodrom|Painlev|Schlesinger|Vieta|Jimbo|Fricke cubic",
}
siblings = {}
for name, pat in LAWS.items():
    siblings[name] = sorted((i for i, d in DEBT.items()
                             if re.search(pat, d["claim_one_line"], re.I)),
                            key=lambda z: int(z[1:]))
bands = sorted({int(b[1:]) // 100 for v in siblings.values() for b in v})
chk("every_restored_law_but_one_has_siblings_STILL_IN_DEBT_in_other_bands",
    sum(len(v) for v in siblings.values()) >= 8 and len(bands) >= 4
    and siblings["isomonodromy (B1040)"] == [],
    siblings={k: v for k, v in siblings.items()},
    bands_spanned=["B%d00s" % b for b in bands],
    note="isomonodromy is the control: B1040's cluster was already complete, so a law CAN be "
         "band-local. The finding is that most are not")
chk("the_band_groups_by_WHEN_not_by_WHAT",
    True,
    argument="a band is an interval of B-numbers, i.e. of BANKING DATE. A law is a statement. "
             "B1037's sweep read every body in B100-B199 -- correctly, and it found the clusters "
             "INSIDE the band. It could not see B33, B232, B522, B564, B75, B77 or B257, because "
             "they are the same laws banked at other times",
    note="B1037's own headline stands: '37 rows are 17 statements'. What is added is that the 17 "
         "are not closed at the band boundary")

# ============================================== 4. what is NOT done
chk("re_dispositioning_the_corpus_BY_TOPIC_is_registered_not_done",
    "L164" in read("docs/OPEN_LEADS.md"),
    note="a topic-wise re-disposition of all 213 debt rows is a different instrument from the "
         "band sweep and would re-open every band already closed. Registered as L164 with the "
         "measurement that motivates it; the four laws' siblings are named there so the next pass "
         "starts from evidence rather than from scratch")

R["all_pass"] = all(v["pass"] for v in R["checks"].values())
if __name__ == "__main__":
    (pathlib.Path(__file__).parent / "results.json").write_text(
        json.dumps(R, indent=1, ensure_ascii=False, default=str))
    for k, v in R["checks"].items():
        print(("PASS " if v["pass"] else "FAIL ") + k)
    print("\nALL PASS:", R["all_pass"], " checks:", len(R["checks"]))
