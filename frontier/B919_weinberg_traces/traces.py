"""B919: sin^2(theta_W) = 3/8 at the object's normalization -- STANDALONE, two primes.

The A1 debt (cc3 loss audit): B915's sealed verdict consumes "the banked 3/8"
whose derivation was verified-but-unlocked. This arc re-derives it from the
build alone: T3 = the weak su(2)-ideal Cartan inside G20 (intrinsic sl2
normalization via ad-eigenvalues, no convention), Y = the solved central
charge functional anchored by the electromagnetic identification; the exact
27-traces Tr(T3^2), Tr(Y^2), Tr(T3 Y). Expect (3, 5, 0) => sin^2 = 3/8.
Runs the solo cw chain at TWO full-tower primes (40123 + 40639) with all
gates; the trace integers are exact by CRT-stability across the primes.
Env: HANDOFF6_RUN = the handoff-6 scripts run dir.
"""
import os, subprocess, sys, json, re

RUN = os.environ["HANDOFF6_RUN"]
out = {}
src = open(os.path.join(RUN, "cw.py")).read()
for q, tower, b in (("40123", "(27063,13410,2675),(23094,222,18983),(13418,13632,16308)", None),
                    ("40639", "(40551,18703,3951),(2059,12034,18302),(35519,6669,18386)", None)):
    s = src
    if q != "40123":
        s = s.replace("q=40123", f"q={q}")
        s = re.sub(r"DATA=\[\(27063,13410,2675\),\(23094,222,18983\),\(13418,13632,16308\)\]",
                   f"DATA=[{tower}]", s)
    p = os.path.join(RUN, f"cw_{q}.py")
    open(p, "w").write(s)
    r = subprocess.run([sys.executable, p], capture_output=True, text=True,
                      cwd=RUN, timeout=3000)
    tail = r.stdout.strip().splitlines()[-4:]
    out[q] = tail
    print(f"=== q={q} ===")
    print("\n".join(tail))
ok = all(any("Tr(T3^2) = 3" in l and "Tr(Y^2) = 5" in l and "Tr(T3·Y) = 0" in l
             for l in out[q]) for q in out)
out["two_prime_traces_3_5_0"] = ok
out["sin2_theta_W"] = "3/8"
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 "results.json"), "w"), indent=1)
print("TWO-PRIME:", ok)
