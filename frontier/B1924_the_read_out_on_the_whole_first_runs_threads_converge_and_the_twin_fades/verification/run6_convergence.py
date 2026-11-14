"""The run of 6's thread (L^6 R LR, geodesic length 6.18): the frame's ratios averaged over one period at 128 and 192
trapezoid nodes, and at 128 in a second window. Structure printed; values to the json."""
import json, pathlib
import numpy as np
import convergence as CV
HERE = pathlib.Path(__file__).resolve().parent
w = "LLLLLLRLR"
S192 = CV.samples(w, 0.0, 192)
S128a = CV.samples(w, 0.0, 128)
S128b = CV.samples(w, 0.37, 128)
l192, _ = CV.averages(S192); l128a, _ = CV.averages(S128a); l128b, _ = CV.averages(S128b)
print("run of 6, ratios averaged: 128 vs 192 nodes %.1e; window spread at 128 %.1e" % (CV.spread(l128a, l192), CV.spread(l128a, l128b)), flush=True)
(HERE / "run6_convergence.json").write_text(json.dumps({"lin192": {k: v.tolist() for k, v in l192.items()}}, indent=1))
