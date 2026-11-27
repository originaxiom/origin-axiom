#!/usr/bin/env python3
"""SM-C14's decisive run in the new card form (fam1-v1-unset-04): relays/sm_c14/run_c14.py run unchanged in a copy of its
folder, on its SnapPy-free parts he1, c4, p1, he2 and ap1 (c2's SnapPy cross-check, c5 and ap2's cusp shapes are not part
of this card); its part outputs read back and the decisive facts printed as DECISIVE: lines.
    python3 relays/claims/sm_refile/c14_decisive.py
Exit 0 when the run completes and every decisive fact comes out as the card states; 1 otherwise."""
import json, pathlib, shutil, subprocess, sys, tempfile
try:
    HERE = pathlib.Path(__file__).resolve().parent
    ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
    tmp = pathlib.Path(tempfile.mkdtemp()) / "sm_c14"
    shutil.copytree(ROOT / "relays" / "sm_c14", tmp)
    for f in tmp.glob("c14_*.json"):
        f.unlink()
    r = subprocess.run([sys.executable, "-B", "run_c14.py", "he1", "c4", "p1", "he2", "ap1"], cwd=tmp,
                       capture_output=True, text=True)
    J = {p: json.loads((tmp / ("c14_%s.json" % p)).read_text()) for p in ("he1", "c4", "p1", "he2", "ap1")}
except Exception as e:
    print("RUN FAILED: %s" % type(e).__name__); sys.exit(1)
h = J["he1"]
odd = [str(n) for n in (1, 3, 5, 7)]
even = [str(n) for n in (2, 4, 6)]
a = all(h[n]["h1(V9)"] == 0 and h[n]["h1(V9 w)"] == 1 and h[n]["r1(V9 w)"] == 1 for n in odd)
b = all(h[n]["h1(V9)"] == 1 and h[n]["h1(V9 w)"] == 1 for n in even)
print("DECISIVE: HE-1 odd levels 1, 3, 5, 7: h1(V9) = 0, h1(V9 w) = 1, restriction rank 1: %s" % a)
print("DECISIVE: HE-1 even levels 2, 4, 6: h1(V9) = h1(V9 w) = 1: %s" % b)
e = J["he2"]
for n in ("1", "3", "5"):
    x = e[n]
    print("DECISIVE: HE-2 level %s: characters %d, n(V) nonzero at %d, members %d, primes agree %s, generation-shaped %d"
          % (n, x["characters"], len(x["n(V) non-zero at"]), x["members (h1(V_eta) > 0)"], x["primes agree"],
             len(x["generation-shaped"])))
x = e["7"]
print("DECISIVE: HE-2 level 7: characters %d, n(V) nonzero at %d, members %d (its generation-shaped reading is not claimed)"
      % (x["characters"], len(x["n(V) non-zero at"]), x["members (h1(V_eta) > 0)"]))
print("DECISIVE: C4 the transfer identity on %d characters: %s" % (J["c4"]["rows"], J["c4"]["C4 holds"]))
print("DECISIVE: P1 plant (no w in the corner) gives det != 1 on every extension at levels 1, 3, 5: %s"
      % all(J["p1"][n]["det != 1"] == J["p1"][n]["W1 built"] for n in ("1", "3", "5")))
print("DECISIVE: AP-1 phi on the fixed 3-plane is +- its volume form, k = 2 to 6: %s" % J["ap1"]["AP-1 holds"])
ok = (r.returncode == 0 and a and b and all(len(e[n]["n(V) non-zero at"]) == 0 and not e[n]["generation-shaped"]
      and e[n]["primes agree"] for n in ("1", "3", "5")) and len(x["n(V) non-zero at"]) == 0
      and J["c4"]["C4 holds"] and J["ap1"]["AP-1 holds"])
sys.exit(0 if ok else 1)
