#!/usr/bin/env python3
"""B1756 -- JUNO's second release against the falsifier register's P10 (a) and P10'.  B1628's sealed instrument
(two_relations.py) is loaded unchanged, its sha256 asserted, and pointed at this arc's data.json; it writes
two_relations.json here.  Then the register's own wordings, fixed before this release, are applied:
    P10 (a)  falsified by a theta12 measurement more than 3 sigma from 1 - 2/(3 cos^2 theta13)      (TM1)
    P10'     falsified by a global fit or a single precision measurement placing 1/(3 cos^2 theta13) beyond 3 sigma   (TM2)
    python3 -B grade.py      # writes two_relations.json and grade.json beside itself"""
import json, hashlib, pathlib, importlib.util
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
SRC = ROOT / "frontier" / "B1628_the_data_and_the_two_trimaximal_relations" / "verification" / "two_relations.py"
SRC_SHA = "e638ccb7c634acc770b835a146dbfed0b21202ccf80bdd5b4e247f9433bcf0dd"


def main():
    assert hashlib.sha256(SRC.read_bytes()).hexdigest() == SRC_SHA
    sp = importlib.util.spec_from_file_location("b1628_two_relations", SRC); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    m.HERE = HERE
    m.main()
    out = json.load(open(HERE / "two_relations.json"))
    g = {}
    for name, res in out["sets"].items():
        r = res["NO"]
        g[name] = {"TM1_pull_sigma": r["TM1"]["pull_sigma"], "TM2_pull_sigma": r["TM2"]["pull_sigma"],
                   "P10a_falsified": abs(r["TM1"]["pull_sigma"]) > 3, "P10prime_falsified": abs(r["TM2"]["pull_sigma"]) > 3}
    json.dump(g, open(HERE / "grade.json", "w"), indent=1)
    for k, v in g.items(): print(k, v)


if __name__ == "__main__":
    main()
