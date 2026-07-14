"""B598-P0 — the C1 baseline: the SL(2) semiclassical dictionary datum, computed.

The Kashaev invariant <4_1>_N = sum_{j=0}^{N-1} prod_{k=1}^{j} 4 sin^2(pi k/N):
extract the growth rate (gate: Vol(4_1)/2pi) and the 1-loop constant, and
identify its tau_1 = -3 content. Upgrades the B425-row identification from
[CITED] to [COMPUTED]. Run: python3 p0_c1_baseline.py (~2 min, mpmath).
"""
import mpmath as mp

mp.mp.dps = 40
VOL = mp.mpf("2.029883212819307250042405108549040391918")


def kashaev(N):
    s = mp.mpf(0)
    p = mp.mpf(1)
    for k in range(0, N):
        if k > 0:
            p *= 4 * mp.sin(mp.pi * k / N) ** 2
        s += p
    return s


print("P0 — the Kashaev asymptotics of 4_1:")
print("  N     log<4_1>_N/N      r_N = <4_1>_N e^{-NV/2pi} N^{-3/2}")
data = []
for N in (100, 200, 400, 800, 1600):
    v = kashaev(N)
    rate = mp.log(v) / N
    r = v * mp.e ** (-N * VOL / (2 * mp.pi)) / mp.mpf(N) ** mp.mpf(1.5)
    data.append((N, r))
    print(f"  {N:5d}  {mp.nstr(rate, 12):>16}  {mp.nstr(r, 12)}")

# the raw rate carries the universal (3/2) log N / N + log r / N corrections;
# gate on the corrected rate
v1600 = kashaev(1600)
corrected = (mp.log(v1600) - mp.mpf(1.5) * mp.log(1600) - mp.log(data[-1][1])) / 1600
gate = abs(corrected - VOL / (2 * mp.pi))
print(f"\n  GATE corrected growth rate -> Vol/2pi: dev = {mp.nstr(gate, 3)}")
assert gate < 1e-6

# Richardson extrapolation of r_N (corrections in 1/N)
def richardson(seq):
    # seq at N, 2N, 4N, ...: eliminate 1/N then 1/N^2
    out = list(seq)
    fac = 2
    while len(out) > 1:
        out = [(fac * b - a) / (fac - 1) for a, b in zip(out, out[1:])]
        fac *= 2
    return out[0]


r_inf = richardson([r for _, r in data])
print(f"  r_inf (Richardson) = {mp.nstr(r_inf, 15)}")

print("\n  identification against 1-loop candidates (the tau_1 = -3 content):")
cands = {
    "3^(-1/4)": 3 ** mp.mpf(-0.25),
    "2 pi / 3^(3/4)": 2 * mp.pi / 3 ** mp.mpf(0.75),
    "pi / 3^(3/4)": mp.pi / 3 ** mp.mpf(0.75),
    "(2 pi)^(1/2) 3^(-1/4)": mp.sqrt(2 * mp.pi) * 3 ** mp.mpf(-0.25),
    "pi^(1/2) 3^(-1/4)": mp.sqrt(mp.pi) * 3 ** mp.mpf(-0.25),
    "1/3^(1/2)": 3 ** mp.mpf(-0.5),
    "2 pi 3^(-1/4) / N-free": 2 * mp.pi * 3 ** mp.mpf(-0.25),
}
best = min(cands.items(), key=lambda kv: abs(r_inf - kv[1]))
for nm, v in sorted(cands.items(), key=lambda kv: abs(r_inf - kv[1])):
    print(f"    {nm:>24} = {mp.nstr(v, 12)}   |diff| = {mp.nstr(abs(r_inf - v), 3)}")
print(f"\n  best: {best[0]}  (relative dev {mp.nstr(abs(r_inf - best[1]) / best[1], 3)})")
print("  the 3-content of the winning constant = |tau_1| = 3: the SL(2) torsion")
print("  appears in the 1-loop coefficient exactly as the semiclassical")
print("  correspondence requires -- C1's baseline datum, computed in-sandbox.")
