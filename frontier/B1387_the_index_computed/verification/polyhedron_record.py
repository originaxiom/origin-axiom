#!/usr/bin/env python3
"""B1387 -- the polyhedron's numbers, recorded (2026-10-02).

FINDINGS section 1 quotes the developed fundamental polyhedron's size (ideal tetrahedra, polyhedron vertices, face pairings) and
how well its matrices satisfy the relators. `harmonic_cusp_form.py` builds that polyhedron but never logged these numbers; main's
B1453 reader found them in no record. This script builds the same object with the arc's own code (`member()`, `Polyhedron`,
`cuspidal_class`) for the three chart seeds the five runs use, and records: the number of developed tetrahedra, of polyhedron
vertices, of generators of the unsimplified presentation (each pairs two faces), the face pairings themselves, and the worst
deviation of a relator word in the generator matrices from +-I.
Usage: python3 polyhedron_record.py  (writes polyhedron_record_run.txt beside it)"""
import importlib.util
import json
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("b1387_harmonic_cusp_form", HERE / "harmonic_cusp_form.py")
H = importlib.util.module_from_spec(spec)
spec.loader.exec_module(H)


def main():
    t0 = time.time()
    M = H.member()
    v, G, dim = H.cuspidal_class(M)
    rels = G.relators(as_int_list=True)
    out = {"member": M.name(), "decorated isosig (the arc's pin)": H.T.ISOSIG, "cuspidal line dimension": dim,
           "unsimplified presentation: generators": G.num_generators(), "relators": len(rels), "by chart seed": {}}
    for seed in (1, 2, 3):
        P = H.Polyhedron(M, seed=seed)
        worst = 0.0
        for rel in rels:
            A = np.eye(2, dtype=complex)
            for g in rel:
                A = A @ P.gen[g]
            worst = max(worst, min(np.abs(A - np.eye(2)).max(), np.abs(A + np.eye(2)).max()))
        gens = sorted(g for g in P.gen if g > 0)
        out["by chart seed"][str(seed)] = {
            "developed ideal tetrahedra": P.ntet,
            "polyhedron vertices": P.nvert,
            "face-pairing generators": len(gens),
            "paired faces": len(P.pairing),
            "generators equal the presentation's": gens == list(range(1, G.num_generators() + 1)),
            "worst relator deviation from +-I": float("%.2e" % worst)}
    out["seconds"] = round(time.time() - t0, 1)
    text = json.dumps(out, indent=1, ensure_ascii=False)
    (HERE / "polyhedron_record_run.txt").write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
