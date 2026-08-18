"""AXIS 0 -- the unbiased sweep.  Every prime accounted for; nothing silently dropped.

Rule 5 of the loop: no silent skipping.  cell8 carried `except: pass` and reported 36
primes in which #roots(mu) was NEVER 0 -- impossible for an S3 cubic.  This run records
an outcome for every prime, with a reason when the pipeline cannot produce an answer.
"""
import os, subprocess, sys
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
X = sp.Symbol('X'); MU = X**3 - 12*X - 5
LO, HI = int(sys.argv[1]), int(sys.argv[2])
primes = [p for p in sp.primerange(LO, HI) if p % 3 == 1 and 6237 % p]

rows = []
for p in primes:
    nr = len(sp.ground_roots(MU, modulus=p))
    l77 = int(sp.legendre_symbol(77 % p, p)) if 77 % p else 0
    try:
        out = subprocess.run([sys.executable, os.path.join(HERE, "cell6_pure.py"), str(p)],
                             capture_output=True, text=True, timeout=900)
        line = [l for l in out.stdout.splitlines() if "omega  " in l]
        if line:
            n = int(line[0].split("pure points")[1].split("at")[0].strip())
            status, why = ("SPLIT" if n == 2 else "inert"), ""
        else:
            err = (out.stderr or "").strip().splitlines()
            status, why = "NO-ANSWER", (err[-1][:60] if err else "no output")
    except subprocess.TimeoutExpired:
        status, why = "NO-ANSWER", "timeout"
    rows.append((p, nr, l77, status, why))
    print(f"  p={p:5d}  roots(mu)={nr}  L(77,p)={l77:+d}  {status:10s} {why}", flush=True)

print("\n" + "="*70)
tot = len(rows)
ans = [r for r in rows if r[3] != "NO-ANSWER"]
noans = [r for r in rows if r[3] == "NO-ANSWER"]
split = [r for r in ans if r[3] == "SPLIT"]
print(f"primes tested            : {tot}")
print(f"  answered               : {len(ans)}")
print(f"  NO-ANSWER (accounted)  : {len(noans)}   {[r[0] for r in noans][:12]}")
print(f"\nroot-count distribution over ALL primes tested:")
for k in (0, 1, 3):
    c = sum(1 for r in rows if r[1] == k)
    print(f"    #roots(mu) = {k} : {c:3d}  ({c/tot:.3f})   [S3 predicts {['1/3','1/2','1/6'][ (0,1,3).index(k) ]}]")
print(f"\nNO-ANSWER by root count  : "
      f"{ {k: sum(1 for r in noans if r[1]==k) for k in (0,1,3)} }")
print(f"   -> was the drop exactly the 0-root primes? "
      f"{all(r[1]==0 for r in noans) and len(noans)>0}")

print(f"\nsplit density over ANSWERED primes: {len(split)}/{len(ans)} = "
      f"{len(split)/len(ans):.3f}   (prereg predicted 0.250 if the predicate holds)")
print(f"split density over ALL primes     : {len(split)}/{tot} = {len(split)/tot:.3f}"
      f"   (1/6 = 0.167 if 'mu splits completely' is the true rule)")

print("\nPREDICATE TEST on the answered sample (prereg: zero misses, zero extras)")
for name, pred in (("#roots(mu) = 3", lambda r: r[1] == 3),
                   ("77 is a QR",     lambda r: r[2] == 1),
                   ("both",           lambda r: r[1] == 3 and r[2] == 1)):
    miss = [r[0] for r in ans if r[3] == "SPLIT" and not pred(r)]
    extra = [r[0] for r in ans if r[3] != "SPLIT" and pred(r)]
    print(f"  {name:16s} misses {len(miss)} {miss[:6]}  extras {len(extra)} {extra[:6]}"
          f"   EXACT: {not miss and not extra}")
