#!/usr/bin/env python3
"""B1380's carrier theorem in the new card form (fam1-v1-unset-04): the sealed relays/sm_b1380/verification/puncture.py,
copied unchanged from this seat's earlier branch, run through a small driver in a temporary copy, steps S1 to S6 only
(S7 and S8 need SnapPy and are not part of this card). The decisive facts are printed as DECISIVE: lines.
    python3 relays/claims/sm_refile/b1380_decisive.py
Exit 0 when every step completes with the card's result; 1 otherwise."""
import pathlib, shutil, subprocess, sys, tempfile
DRIVER = '''import puncture as P
ok1 = P.s1_automorphisms()
s1, s2, good, dets = P.s2_orientation()
closed = P.s3_closed_surfaces()
found, classes = P.s4_the_four()
no_root, verdict, ctrl = P.s5_realizability()
rows, i2, iz, nw, nz, freq = P.s6_word_against_shadow()
print("DECISIVE: S1 sigma and sigma^2 are automorphisms of F2: %s; abelianizations %s and %s" % (ok1[0], ok1[1].tolist(), ok1[2].tolist()))
print("DECISIVE: S2 sigma([a,b]) conjugate to [a,b]^-1: %s; sigma^2([a,b]) conjugate to [a,b]: %s" % (s1, s2))
print("DECISIVE: S2 Nielsen control: %d of 300 seeded automorphisms send [a,b] to a conjugate of [a,b]^det" % good)
print("DECISIVE: S3 closed surfaces checked, none with pi1 = F2: %d rows" % len(closed))
print("DECISIVE: S4 compact surfaces with chi = -1 and boundary: %s" % sorted(found))
print("DECISIVE: S5 sigma^ab has no root-of-unity eigenvalue: %s" % no_root)
print("DECISIVE: S5 surfaces realizing sigma: %s" % sorted(k for k, v in verdict.items() if v.startswith("sigma realizable")))
print("DECISIVE: S5 controls (the criterion does not fire on realized swaps): %s" % (ctrl,))
print("DECISIVE: S6 Fibonacci word, all n <= 60: n+1 factors and 2 letter-count images: %s"
      % all(p == n + 1 and q == 2 for n, p, q in rows))
'''
try:
    HERE = pathlib.Path(__file__).resolve().parent
    ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
    tmp = pathlib.Path(tempfile.mkdtemp())
    shutil.copy(ROOT / "relays" / "sm_b1380" / "verification" / "puncture.py", tmp / "puncture.py")
    (tmp / "driver.py").write_text(DRIVER)
    r = subprocess.run([sys.executable, "-B", "driver.py"], cwd=tmp, capture_output=True, text=True)
except Exception as e:
    print("RUN FAILED: %s" % type(e).__name__); sys.exit(1)
print(r.stdout, end="")
want = "DECISIVE: S5 surfaces realizing sigma: ['S(1,1) once-punctured torus']"
sys.exit(0 if r.returncode == 0 and want in r.stdout.splitlines() else 1)
