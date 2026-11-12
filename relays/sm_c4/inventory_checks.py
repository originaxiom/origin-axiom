#!/usr/bin/env python3
"""SM-C4: the inventory table's own checks, and three planted errors that each must catch.

Checks on relays/SM_C4_INVENTORY.md, § 1's table:
 (a) the rows by sector and kind equal the count from the field content (relays/sm_c4/parameter_count.json): masses,
     mixing angles and CP phases, and the totals with massless, Dirac and Majorana neutrinos;
 (b) no definition cell holds a figure: no ASCII digit (a reference to another row, such as S16, is removed first) and
     no unit of mass or energy;
 (c) no id and no symbol stands twice.
The checks are run on the page as it is (the control: they must pass), then on three planted copies, each of which
must fail: a sector's row deleted; a figure written into a definition; one parameter entered again under another name.
Usage (from the repository's root): inventory_checks.py OUT.json"""
import json
import re
import sys
from pathlib import Path

PAGE = Path("relays/SM_C4_INVENTORY.md").read_text(encoding="utf-8")
COUNT = json.loads(Path("relays/sm_c4/parameter_count.json").read_text(encoding="utf-8"))
MASSLESS = {"gauge", "Higgs", "vacuum angle", "quark masses", "lepton masses", "quark mixing"}


def rows_of(page):
    out = []
    for line in page.split("\n"):
        if re.match(r"^\| S\d\d \|", line):
            cells = [c.strip() for c in re.split(r"(?<!\\)\|", line.strip())[1:-1]]
            out.append(dict(zip(("id", "name", "sector", "kind", "dimension", "definition", "lagrangian", "coordinate", "record"), cells)))
    return out


def check(page):
    rows = rows_of(page)
    sectors = {"massless neutrinos": [r for r in rows if r["sector"] in MASSLESS]}
    sectors["Dirac neutrinos"] = sectors["massless neutrinos"] + [r for r in rows if r["sector"] == "neutrino (Dirac or Majorana)"]
    sectors["Majorana neutrinos"] = sectors["Dirac neutrinos"] + [r for r in rows if r["sector"] == "neutrino (Majorana only)"]
    res = {}
    for name, rs in sectors.items():
        k = lambda *kinds: sum(r["kind"] in kinds for r in rs)
        want = COUNT["by_kind_the_table_must_match"][name]
        got = {"masses": k("fermion mass", "neutrino mass"), "mixing angles": k("quark mixing angle", "lepton mixing angle"),
               "CP phases": k("CP phase", "Majorana phase")}
        res[f"(a) {name}: by kind"] = got == want
        res[f"(a) {name}: in all"] = len(rs) == COUNT["flavour"][name]["all"]
    res["(a) gauge 3, Higgs 2, vacuum angle 1"] = ([r["kind"] for r in rows].count("gauge coupling"), [r["kind"] for r in rows].count("Higgs-sector parameter"),
                                                [r["kind"] for r in rows].count("strong vacuum angle")) == (COUNT["gauge_couplings"], COUNT["higgs_potential"], COUNT["vacuum_angles"])
    # a reference to another row (P16) is an id, not a figure, and is removed before the test
    res["(b) no figure in a definition"] = not any(re.search(r"[0-9]|\b(?:k|M|G|T)?eV\b", re.sub(r"\bS\d\d\b", "", r["definition"])) for r in rows)
    ids = [r["id"] for r in rows]
    syms = [r["name"].split(",")[-1].strip() for r in rows if "," in r["name"]]
    res["(c) no id twice"] = len(ids) == len(set(ids))
    res["(c) no symbol twice"] = len(syms) == len(set(syms))
    return len(rows), res


n, control = check(PAGE)
out = {"rows": n, "control_passes": all(control.values()), "control": control, "plants": {}}
row17 = next(l for l in PAGE.split("\n") if l.startswith("| S17 |"))
row09 = next(l for l in PAGE.split("\n") if l.startswith("| S09 |"))
plants = {
    "a sector's row deleted (S17)": PAGE.replace(row17 + "\n", ""),
    "a figure written into a definition (S09)": PAGE.replace(row09, row09.replace("| the pole mass or the MS-bar mass,", "| the pole mass, near 173 GeV, or the MS-bar mass,")),
    "one parameter entered again under another name (the Cabibbo angle, beside S16)": PAGE.replace(
        row17, "| S29 | the Cabibbo angle, θ_C | quark mixing | quark mixing angle | dimensionless | the angle of the first two families | as S16 | \\|V_us\\| | as S16 |\n" + row17),
}
for name, text in plants.items():
    assert text != PAGE, name
    _, res = check(text)
    out["plants"][name] = {"caught": not all(res.values()), "failed_checks": [k for k, v in res.items() if not v]}
out["all_plants_caught"] = all(v["caught"] for v in out["plants"].values())
out["all_hold"] = out["control_passes"] and out["all_plants_caught"]
Path(sys.argv[1]).write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps(out, indent=1, ensure_ascii=False))
