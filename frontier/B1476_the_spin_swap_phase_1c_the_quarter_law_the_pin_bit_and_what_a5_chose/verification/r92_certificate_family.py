#!/usr/bin/env python3
"""The coverage-free certificate on the family's thirteen amphichiral rank-one members, read from the tables already on
the record (B1475's spin_quantity.json for ten members, this arc's C1 for three): for every spin structure, is the odd
twisted Alexander function real (or imaginary -- the lenient reading) at real t?  The same test as r92_certificate.py;
no new torsion is computed here."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
FR = next(p for p in HERE.parents if p.name == "frontier")
sq = json.load(open(FR / "B1475_the_spin_swap_phase_1b_does_the_swap_carry_a_quantity/verification/spin_quantity.json"))
c1 = json.load(open(HERE / "phase_1c.json"))["C1"]
CS = {k: v["cls"] for k, v in json.load(open(HERE / "phase_1c.json"))["C2"].items()}

def is_real(z):
    z = complex(z.replace(" ", ""))
    return min(abs(z.imag), abs(z.real)) <= 1e-9 * max(1, abs(z))

out = {}
for src, table in (("B1475", sq), ("B1476/C1", c1)):
    for nm, v in table.items():
        rows = []
        for s in v["spin"]:
            vals = [s[k][t] for k in ("R1", "R3") if k in s for t in s[k]]
            rows.append(dict(chi=s["chi"], real=all(is_real(z) for z in vals), n_values=len(vals)))
        s0 = [r for r in rows if all(x == 1 for x in r["chi"])][0]
        out[nm] = dict(source=src, cs=CS.get(nm), n_spin=len(rows), torsion_real=sum(r["real"] for r in rows),
                       s0_real=s0["real"], rows=rows)
        print("%-11s CS %-8s spin %d, torsion-real %d, s0 real: %s  (%s)" % (nm, CS.get(nm), len(rows), out[nm]["torsion_real"], s0["real"], src))
json.dump(out, open(HERE / "r92_certificate_family.json", "w"), indent=1)
