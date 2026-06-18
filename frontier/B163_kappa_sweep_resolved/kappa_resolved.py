#!/usr/bin/env python3
"""B163 -- the kappa-sweep resolved: kappa<2 is a Cantor set; NO figure-eight encoding.

Resolves the two OPEN items B162 left (OPEN_LEADS L19), each with a built-in control / null-test.

(3a) Is the kappa<2 thin complex spectrum a TRUE Cantor set (totally disconnected), or a
     connected curve? "Thin / zero-2D-area" (B162) cannot decide -- a curve is also zero-area.
     DIAGNOSTIC = the largest spectral gap = max edge of the minimum spanning tree (MST),
     normalized by the spectrum diameter, vs chain length F_k:
        connected curve/band -> max-gap/diam -> 0 ;   Cantor (gaps at all scales) -> -> const>0.
     CONTROLS: kappa=2 (lambda=0, full AC band -> ->0) and kappa>2 Hermitian (lambda=1, KNOWN
     Cantor, Suto -> ->const). RESULT: both kappa<2 cases track the Cantor control (gap converges
     to a positive constant across F=144..1597) => the kappa<2 spectrum is TOTALLY DISCONNECTED
     (a Cantor set in C). [num, control-bracketed; not a theorem -- no ground truth off the real axis.]

(3b) Does the kappa=-2 spectrum ENCODE the figure-eight hyperbolic geometry? NULL-TEST: is any
     spectral feature non-analytic/extremal EXACTLY at kappa=-2 vs neighbors, and does any feature
     hit a figure-eight invariant (vol=2.029883, |sqrt(-3)|, 2/phi, ...) ONLY there? RESULT: all
     features are smooth through kappa=-2 (no kink at the cusp-opening), and no invariant matches
     specially (neighbors match equally/better). => NO encoding -- the figure-eight link is the
     boundary-trace value kappa=-2 alone (B160), NOT the spectrum. [num, negative + null-test.]
"""
import numpy as np

def fib_word(n):
    w = {1: "a", 2: "ab"}
    for j in range(3, n+1): w[j] = w[j-1] + w[j-2]
    return w[n]

def H_eig(word, lam, periodic=False):
    L = len(word); V = np.array([lam if c == "a" else 0.0 for c in word], dtype=complex)
    H = np.zeros((L, L), dtype=complex); np.fill_diagonal(H, V)
    i = np.arange(L-1); H[i, i+1] = 1.0; H[i+1, i] = 1.0
    if periodic: H[0, L-1] = 1.0; H[L-1, 0] = 1.0
    return np.linalg.eigvals(H)

def mst_max_edge(pts):
    """max edge of the Euclidean MST (Prim, O(N^2)) = the largest spectral gap."""
    P = np.c_[pts.real, pts.imag]; n = len(P)
    in_tree = np.zeros(n, bool); mind = np.full(n, np.inf); mind[0] = 0.0; edges = np.empty(n)
    for t in range(n):
        u = int(np.argmin(np.where(in_tree, np.inf, mind)))
        edges[t] = mind[u]; in_tree[u] = True
        d = np.sqrt(((P - P[u])**2).sum(1)); upd = (~in_tree) & (d < mind); mind[upd] = d[upd]
    return float(edges[1:].max())

def diam(pts):
    return float(np.hypot(pts.real.max()-pts.real.min(), pts.imag.max()-pts.imag.min()))

ok = True
def chk(n, c, x=""):
    global ok; ok = ok and bool(c); print(f"  [{'PASS' if c else 'FAIL'}] {n}" + (f"  {x}" if x else ""))

print("== (3a) total-disconnectedness: max-gap/diam vs F_k (Cantor: ->const>0 ; curve/band: ->0) ==")
sizes = [11, 13, 15, 16]                       # word lengths F = 144, 377, 987, 1597
res = {}
for name, lam in [("kappa=2 lam=0 [band control]", 0.0+0j), ("kappa=3 lam=1 [Cantor control]", 1.0+0j),
                  ("kappa=1 lam=1i", 1.0j), ("kappa=-2 lam=2i [fig-8 pt]", 2.0j)]:
    row = [mst_max_edge(ev := H_eig(fib_word(n), lam, False))/diam(ev) for n in sizes]
    res[name] = row
    print(f"   {name:32s} F=144/377/987/1597: " + "/".join(f"{v:.4f}" for v in row))
band, cantor = res["kappa=2 lam=0 [band control]"], res["kappa=3 lam=1 [Cantor control]"]
chk("control: kappa=2 band gap -> 0", band[-1] < 0.1*band[0] and band[-1] < 0.01)
chk("control: kappa>2 Cantor gap -> const>0", cantor[-1] > 0.05 and cantor[-1] > 0.5*cantor[0])
for nm in ("kappa=1 lam=1i", "kappa=-2 lam=2i [fig-8 pt]"):
    r = res[nm]
    chk(f"{nm}: gap converges to const>0 (Cantor, NOT band)", r[-1] > 0.02 and r[-1] > 0.5*r[0],
        x=f"gap={r[-1]:.4f} (vs band {band[-1]:.4f}->0)")

print("\n== (3b) figure-eight encoding null-test: smooth through kappa=-2? any special invariant match? ==")
fig8 = {"vol=2.0299": 2.029883, "|v-3|=1.7321": 3**0.5, "2/phi=1.2361": 2/((1+5**0.5)/2), "2cos(pi/3)=1": 1.0}
feats = {}
for kap in [-1.6, -1.8, -2.0, -2.2, -2.4]:
    mu = (2.0 - kap)**0.5
    ev = H_eig(fib_word(15), mu*1j, True)
    lo_r, lo_i = ev.real.min()-1e-6, ev.imag.min()-1e-6
    area = len(set(zip(np.floor((ev.real-lo_r)/0.02).astype(int).tolist(),
                       np.floor((ev.imag-lo_i)/0.02).astype(int).tolist())))*0.0004
    feats[kap] = (np.max(np.abs(ev.imag)), ev.real.max()-ev.real.min(), ev.imag.max()-ev.imag.min(), area)
    print(f"   kappa={kap:5.1f} (mu={mu:.4f}): max|Im|={feats[kap][0]:.4f} Re-ext={feats[kap][1]:.4f} "
          f"Im-ext={feats[kap][2]:.4f} area={feats[kap][3]:.4f}" + ("  <-- fig-8" if kap == -2.0 else ""))
ks = sorted(feats); i2 = ks.index(-2.0); names = ["max|Im|", "Re-ext", "Im-ext", "area"]
smooth = True
for j, nm in enumerate(names):
    v = [feats[k][j] for k in ks]
    d2 = abs(v[i2-1]-2*v[i2]+v[i2+1]); typ = np.mean([abs(v[i+1]-2*v[i]+v[i-1]) for i in range(1, len(v)-1)])
    if d2 > 3*typ + 1e-9: smooth = False
chk("(3b) all spectral features SMOOTH through kappa=-2 (no kink at the cusp-opening)", smooth)
special = False
for label, tgt in fig8.items():
    best = min(abs(np.array(feats[-2.0]) - tgt))
    nb = min(min(abs(np.array(feats[k]) - tgt)) for k in (-1.8, -2.2))
    if best < 0.02 and best < 0.5*nb: special = True
    print(f"   {label:16s}: best@-2={best:.4f} neighbor-best={nb:.4f} -> {'SPECIAL' if (best<0.02 and best<0.5*nb) else 'not special'}")
chk("(3b) NO figure-eight invariant matched specially at kappa=-2 (null-test)", not special)

print("\nVERDICT: (3a) kappa<2 spectrum is a CANTOR set (totally disconnected) -- both questions track the")
print("Cantor control, NOT the band control. (3b) NO spectral encoding of the figure-eight geometry -- smooth")
print("through kappa=-2, no special invariant; the figure-eight link is the boundary trace kappa=-2 alone (B160).")
print("\n" + ("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED"))
import sys; sys.exit(0 if ok else 1)
