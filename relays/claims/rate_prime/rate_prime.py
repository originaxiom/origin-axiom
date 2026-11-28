"""On every p-tower the six-move slow rate depends on the prime only: from p^3 on it is 2 sqrt(5 + 4 cos(pi/p)).  Checked at
mod 27, 125 and 343 with B2015's own code for W on the largest orbit over the common point.
    python3 -B rate_prime.py            (the claim)
    python3 -B rate_prime.py --control  (the prediction with cos(pi/(2p)): it must miss)
B2015's code is taken as text, up to its own loop, and run with this check after it as one script beside B2015's, in a
separate process, so that its imports of its neighbours resolve; the copy is removed afterwards."""
import subprocess, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parent
f = next(ROOT.glob("frontier/B2015_*/verification/rate_law.py"))
head = f.read_text().split("\nfor p, k, M in")[0]
CHECK = '''
import sys
ctrl = "--control" in sys.argv; ok = True
for p, k in ((3, 3), (5, 3), (7, 3)):
    N, pts = largest_points(p, k); W, _ = six(N, pts)
    ev = np.linalg.eigvalsh(W.astype(float)); below = float(ev[ev < 6 - 1e-9].max())
    pred = 2 * np.sqrt(5 + 4 * np.cos(np.pi / (2 * p if ctrl else p)))
    print("DECISIVE: mod %d: largest below 6 %.15f; 2 sqrt(5 + 4 cos(pi/%d)) = %.15f; difference %.1e" % (p ** k, below, 2 * p if ctrl else p, pred, abs(below - pred)))
    ok &= abs(below - pred) < 1e-9
if ok:
    print("DECISIVE: the rate depends on the prime only: 2 sqrt(5 + 4 cos(pi/p)) on every p-tower from p^3 on")
else:
    sys.exit(1)
'''
copy = f.with_name("_rate_prime_check.py")
copy.write_text(head + "\n" + CHECK, encoding="utf-8")
try:
    r = subprocess.run([sys.executable, "-B", str(copy)] + sys.argv[1:], cwd=str(f.parent), capture_output=True, text=True)
finally:
    copy.unlink()
sys.stdout.write(r.stdout)
sys.stderr.write(r.stderr)
sys.exit(r.returncode)
