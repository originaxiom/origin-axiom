"""PATH 1b -- the gap labeling theorem: a GENUINE topology->physics bridge, computable.
Bellissard: for the Fibonacci Hamiltonian the integrated density of states (IDOS = fraction of
states below energy E) takes QUANTIZED values inside spectral gaps, of the form {m + n*omega}
(mod 1), omega = (sqrt5-1)/2 = 1/phi. These labels are TOPOLOGICAL (K-theory of the operator
algebra / determined by the trace-map structure), yet the IDOS is a MEASURABLE physical quantity
(a filling fraction). So a topological invariant predicts a lab-measurable number. We verify the
labels fall on the predicted Z+Z*omega lattice. This is the cleanest real topology<->physics
crossing in the neighborhood -- but note: it is 1D condensed matter, NOT the thesis."""
import numpy as np

phi = (1+5**0.5)/2
omega = (5**0.5 - 1)/2     # = 1/phi = phi - 1

def fib_chain(VA, VB, m=1, depth=14):
    a,b = "a","b"
    for _ in range(depth): a,b = a*m+b, a
    word = a
    N = len(word)
    diag = np.array([VA if ch=="a" else VB for ch in word])
    H = np.diag(diag) + np.diag(np.ones(N-1),1) + np.diag(np.ones(N-1),-1)
    return np.sort(np.linalg.eigvalsh(H)), N

VA, VB = 1.0, -1.0
ev, N = fib_chain(VA, VB, depth=14)
# IDOS jumps at each eigenvalue by 1/N. Gaps = large jumps in E. The IDOS *value* in a gap is k/N.
gaps = np.diff(ev)
# find the big gaps and the IDOS (= index/N) at each
idx = np.argsort(gaps)[::-1][:12]
idx = np.sort(idx)
print(f"PATH 1b -- gap labeling (Fibonacci length {N}, omega=1/phi={omega:.6f}):")
print("   gap# | gap width | IDOS in gap (k/N) | best {m+n*omega} | integers (m,n) | error")
def best_label(val, mrange=8, nrange=8):
    best=None
    for n in range(-nrange, nrange+1):
        for m in range(-mrange, mrange+1):
            lab = (m + n*omega) % 1.0
            e = min(abs(lab-val), abs(lab-val-1), abs(lab-val+1))
            if best is None or e<best[0]:
                best=(e, lab, m, n)
    return best
hits=0
for gi in idx:
    if gaps[gi] < 0.05: continue
    idos = (gi+1)/N
    e,lab,m,n = best_label(idos)
    flag = "OK" if e<0.01 else "  "
    if e<0.01: hits+=1
    print(f"     {gi:5d}| {gaps[gi]:.4f}   |  {idos:.5f}        |  {lab:.5f}      |  ({m:+d},{n:+d})    | {e:.4f} {flag}")
print(f"   -> {hits} of the labeled gaps fall on the Z+Z*omega lattice (error<0.01): "
      f"{'GAP LABELING CONFIRMED' if hits>=4 else 'WEAK'}")
print("   MEANING: a topological invariant (K-theory label) fixes a measurable filling fraction.")
print("   HONEST SCOPE: genuine topology<->physics, but 1D condensed matter -- does NOT reach the thesis.\n")

# Now the n>=3 question, stated precisely and honestly:
print("PATH 1 -- the SL(n>=3) question (the actual open thing):")
print("   The SL(2) trace map = this 1D single-channel quasicrystal (solid physics above).")
print("   The SL(n) tower (the project's object) has NO established physical model. The honest")
print("   candidate: an n-channel / n-band tight-binding chain whose transfer matrices live in a")
print("   larger group reducing to the SL(n) trace map. WHETHER such a model exists and whether the")
print("   tower's char(M^k) multiplicities a_d control its spectrum/gap-labels is UNKNOWN and is a")
print("   clean, falsifiable computational target (Path 1-extended below).")
