"""AXIS 0 strengthening -- the forward direction, tested hard.

The claim is a biconditional.  The sweep gave 5 split primes, all with mu splitting
completely.  This targets the FORWARD direction: at primes where mu splits completely,
do pure spinors ALWAYS appear?  A single counterexample kills the biconditional.

No silent skipping (rule 5): every prime gets an outcome.
"""
import os, subprocess, sys
import sympy as sp
HERE = os.path.dirname(os.path.abspath(__file__))
X = sp.Symbol('X'); MU = X**3 - 12*X - 5
targets = [p for p in sp.primerange(700, 4000)
           if p % 3 == 1 and 6237 % p and len(sp.ground_roots(MU, modulus=p)) == 3]
print(f"primes where mu splits completely (and p = 1 mod 3): {len(targets)}")
print(f"  {targets}\n")
ok = bad = noans = 0
for p in targets:
    try:
        out = subprocess.run([sys.executable, os.path.join(HERE, "cell6_pure.py"), str(p)],
                             capture_output=True, text=True, timeout=1200)
        line = [l for l in out.stdout.splitlines() if "omega  " in l]
        if not line:
            noans += 1
            print(f"  p={p:5d}  NO-ANSWER  {(out.stderr or '').strip().splitlines()[-1][:50] if out.stderr.strip() else ''}", flush=True)
            continue
        n = int(line[0].split("pure points")[1].split("at")[0].strip())
        if n == 2: ok += 1
        else: bad += 1
        print(f"  p={p:5d}  pure points = {n}  {'OK' if n==2 else '*** COUNTEREXAMPLE ***'}", flush=True)
    except subprocess.TimeoutExpired:
        noans += 1; print(f"  p={p:5d}  NO-ANSWER  timeout", flush=True)
print(f"\nFORWARD DIRECTION: {ok} confirmed, {bad} counterexamples, {noans} no-answer")
print(f"  biconditional survives: {bad == 0 and ok > 0}")
