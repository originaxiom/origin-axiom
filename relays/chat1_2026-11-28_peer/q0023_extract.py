#!/usr/bin/env python3
"""Input for the peer check of Q0023 (q0023_check.py): the census presentations, extracted by this seat. Not a test.

Writes q0023_presentations.json beside itself: for every orientable one-cusped manifold of SnapPy's cusped census, in
census order, up to and including six ideal tetrahedra, its name, number of tetrahedra, and SnapPy's simplified
fundamental-group presentation (generators as lower-case letters, inverses as upper-case, relators as words). The
card under review extracted its own copy the same way; this script does not open it. SnapPy is not among the
packages the sandbox allows, so this script is run once, here, and its output committed; the check itself uses the
standard library only.

    python3 relays/chat1_2026-11-28_peer/q0023_extract.py
"""
import json
import pathlib
import warnings

warnings.filterwarnings("ignore")
import snappy  # noqa: E402

rows = []
for M in snappy.OrientableCuspedCensus(num_cusps=1):
    if M.num_tetrahedra() > 6:
        break
    G = M.fundamental_group()
    rows.append({"name": M.name(), "tets": M.num_tetrahedra(), "generators": G.generators(),
                 "relators": G.relators()})
out = {"note": "SnapPy %s, OrientableCuspedCensus(num_cusps=1), tetrahedra <= 6, fundamental_group() as simplified"
               % snappy.__version__, "count": len(rows), "manifolds": rows}
pathlib.Path(__file__).with_name("q0023_presentations.json").write_text(json.dumps(out, indent=0) + "\n",
                                                                         encoding="utf-8")
print(len(rows), sum(1 for r in rows if len(r["generators"]) == 2), sum(1 for r in rows if len(r["generators"]) == 3))
