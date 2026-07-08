#!/usr/bin/env python3
"""B470 — identify the volume-per-letter constant c (Chat-1's lit-search assignment):
compute c to high precision (ManifoldHP on tower rungs + the additivity acceleration),
then PSLQ against a Bloch-Wigner/Lobachevsky basis."""
import snappy, mpmath as mp
mp.mp.dps = 30

def fib_word(n):
    s = {0:"L", 1:"R"}
    a, b = "b", "a"
    seq = {0:"b", 1:"a"}
    for k in range(2, n+1): seq[k] = seq[k-1] + seq[k-2]
    return "".join("R" if c=="a" else "L" for c in seq[n])

vols = {}
for n in (10, 11, 12, 13):
    w = fib_word(n)
    M = snappy.ManifoldHP("b++" + w)
    vols[n] = mp.mpf(str(M.volume()))
    print(f"n={n} len={len(w)} vol={vols[n]}", flush=True)

F = {0:1, 1:1}
for k in range(2, 16): F[k] = F[k-1] + F[k-2]
# additivity defect + the incremental constant
for n in (11, 12, 13):
    defect = vols[n] - vols[n-1] - (vols[n-2] if n-2 in vols else 0)
    print(f"defect(n={n}) = vol(n)-vol(n-1)-vol(n-2) = {defect if n-2 in vols else 'n/a'}", flush=True)
c1 = (vols[13] - vols[12]) / F[11]
c2 = (vols[12] - vols[11]) / F[10]
print(f"incremental c estimates: {c1}\n                         {c2}", flush=True)
c = c1
print(f"\nc = {c}", flush=True)

# PSLQ basis: Lobachevsky/Bloch-Wigner values + standard constants
L = lambda th: mp.re(mp.polylog(2, mp.e**(2j*th)))/2  # Lobachevsky-ish: Λ(θ) = -∫log|2sin| = ½ Im Li2(e^{2iθ})
Lob = lambda th: mp.im(mp.polylog(2, mp.e**(2j*th)))/2
v3 = 2*Lob(mp.pi/6)*3/2  # v3 = 2Λ(π/6)? standard: v3 = 3Λ(π/3)... use both directly
cands = {
    "Lob(pi/5)": Lob(mp.pi/5), "Lob(2pi/5)": Lob(2*mp.pi/5),
    "Lob(pi/3)": Lob(mp.pi/3), "Lob(pi/6)": Lob(mp.pi/6),
    "Catalan": mp.catalan, "pi*logphi": mp.pi*mp.log((1+mp.sqrt(5))/2),
    "zeta2/phi": mp.zeta(2)/((1+mp.sqrt(5))/2),
}
print("\nPSLQ attempts (c vs single candidates with small rational multiples):", flush=True)
for name, v in cands.items():
    r = mp.pslq([c, v], maxcoeff=1000, maxsteps=10000)
    if r: print(f"  {name}: relation {r}  -> c = {mp.mpf(-r[1])/r[0]} * {name}", flush=True)
# multi-term
basis = [c] + list(cands.values())
r = mp.pslq(basis, maxcoeff=100, maxsteps=50000)
print("multi-term PSLQ:", r, flush=True)
print("basis order:", ["c"] + list(cands.keys()), flush=True)
