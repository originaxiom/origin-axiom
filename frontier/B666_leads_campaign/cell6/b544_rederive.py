"""CELL 6 / ticket B544: re-derive chat-2's two headline figures that have no
in-repo reproducer (only FINDINGS.md was ever committed; commit f4ab206):
  (a) Frenkel-Kontorova ground state at golden winding 987/610, K = 0.5:
      "occupation word = Sturmian 610/610 exactly";
  (b) critical circle map tuned to winding 1/phi: "itinerary 99.95% Sturmian".

(a) METHOD: standard FK energy  E = sum_n [ (x_{n+1}-x_n)^2/2 + (K/(2pi)^2)(1-cos 2pi x_n) ]
with the rational-winding boundary x_{n+q} = x_n + p, (p,q) = (987,610) = (F_16,F_15),
K = 0.5. Equilibria solve x_{n+1}+x_{n-1}-2x_n = (K/2pi) sin(2pi x_n) (Newton, cyclic
tridiagonal + shift). Ground state = the lowest-energy equilibrium (Hessian min
eigenvalue reported: > 0 = minimum). The claim's word: hop word
h_n = floor(x_{n+1}) - floor(x_n) in {1,2}, n = 0..609, compared EXACTLY (integer
arithmetic) against all 610 intercepts of the mechanical/Sturmian word of slope
p/q: m_n(s) = floor(((n+1)p+s)/q) - floor((np+s)/q). Also reported: the
well-occupation reading (which of 987 consecutive wells are occupied) vs the
mechanical word of slope q/p = 610/987. Aubry-Mather predicts an exact match;
the computation decides.

(b) METHOD: critical sine circle map f(x) = x + Omega - sin(2pi x)/(2pi) (K=1),
Omega bisected (cc2's lock convention, mpmath) so the critical orbit closes:
f^q(0) = p at p/q = F_16/F_17 = 1597/2584 -- the same golden-mean tuning the
FINDINGS' own spot verification uses (Omega* ~ 0.60666). The orbit itinerary
s_n = floor(x_{n+1}) - floor(x_n) in {0,1} is then EXACTLY 2584-periodic; we
test (i) itinerary == mechanical word of slope 1597/2584 (some cyclic shift),
exact; (ii) itinerary vs the TRUE golden Sturmian of slope 1/phi at the best
intercept, over windows L = 1000, 2000, 2584, 5000, 10000 -- exact mismatch
counts, to locate what "99.95%" is a measurement of.
"""
import numpy as np
import mpmath as mp

p, q, K = 987, 610, 0.5

# ---------------------------------------------------------------- (a) FK
print("="*78)
print(f"(a) FK ground state: winding {p}/{q}, K = {K}")
print("="*78)


def fk_energy(x):
    dx = np.empty(q)
    dx[:-1] = x[1:] - x[:-1]
    dx[-1] = (x[0] + p) - x[-1]
    return float(np.sum(dx**2)/2 + (K/(2*np.pi)**2)*np.sum(1 - np.cos(2*np.pi*x)))


def fk_newton(beta, itmax=200):
    n = np.arange(q, dtype=float)
    x = n*p/q + beta
    for it in range(itmax):
        xp = np.roll(x, -1).copy(); xp[-1] += p     # x_{n+1}
        xm = np.roll(x, 1).copy();  xm[0] -= p      # x_{n-1}
        g = xp + xm - 2*x - (K/(2*np.pi))*np.sin(2*np.pi*x)
        if np.max(np.abs(g)) < 1e-13:
            break
        J = np.zeros((q, q))
        idx = np.arange(q)
        J[idx, idx] = -2 - K*np.cos(2*np.pi*x)
        J[idx, (idx+1) % q] += 1
        J[idx, (idx-1) % q] += 1
        x = x - np.linalg.solve(J, g)
    hess = np.zeros((q, q))
    hess[idx, idx] = 2 + K*np.cos(2*np.pi*x)   # d2E: diag 2 + V'', offdiag -1
    hess[idx, (idx+1) % q] -= 1
    hess[idx, (idx-1) % q] -= 1
    return x, np.max(np.abs(g)), float(np.min(np.linalg.eigvalsh(hess)))


sols = []
for beta in (0.0, 1/(2*q), 0.123456789, 0.25, 0.5):
    x, res, hmin = fk_newton(beta)
    E = fk_energy(x)
    sols.append((E, hmin, res, beta, x))
    print(f"  init beta={beta:<12.9f}: residual {res:.2e}, E = {E:.15f}, "
          f"Hessian min eig = {hmin:+.3e}")

sols.sort(key=lambda t: t[0])
E0, hmin0, res0, beta0, x0 = sols[0]
print(f"\nground state: E = {E0:.15f} (from beta={beta0}), Hessian min eig = {hmin0:+.3e}"
      f" ({'MINIMUM' if hmin0 > -1e-10 else 'SADDLE -- check'})")

# hop word, exact integer comparison against all 610 mechanical intercepts
h = np.floor(x0[1:]).astype(int).tolist() + [int(np.floor(x0[0] + p))]
hop = [h_next - h_cur for h_cur, h_next in
       zip(np.floor(x0).astype(int).tolist(),
           np.floor(np.append(x0[1:], x0[0]+p)).astype(int).tolist())]
margin = float(np.min(np.abs(x0 - np.rint(x0))))
print(f"floor-robustness: min distance of any x_n to an integer = {margin:.6f}")

best, best_s = -1, None
for s in range(q):
    mech = [((n+1)*p + s)//q - (n*p + s)//q for n in range(q)]
    m = sum(1 for a, b in zip(hop, mech) if a == b)
    if m > best:
        best, best_s = m, s
print(f"HOP WORD vs mechanical word slope {p}/{q}: best match = {best}/{q}"
      f" (at intercept s={best_s})   [banked claim: 610/610 exactly]")

# occupation word (which wells hold an atom), slope q/p reading
wells = sorted(int(np.floor(v)) for v in x0)
w0 = wells[0]
occ = [0]*p
for w in wells:
    occ[w - w0] = 1
bestw, bestw_s = -1, None
for s in range(p):
    mech = [((m_+1)*q + s)//p - (m_*q + s)//p for m_ in range(p)]
    m = sum(1 for a, b in zip(occ, mech) if a == b)
    if m > bestw:
        bestw, bestw_s = m, s
print(f"OCCUPATION WORD (987 wells) vs mechanical word slope {q}/{p}: "
      f"best match = {bestw}/{p} (at intercept s={bestw_s})")

# ---------------------------------------------------------------- (b) circle map
print()
print("="*78)
print("(b) critical circle map itinerary vs the golden Sturmian")
print("="*78)
mp.mp.dps = 30
P, Q = 1597, 2584  # F_16/F_17, the FINDINGS' own spot-verification level


def f(x, Om):
    return x + Om - mp.sin(2*mp.pi*x)/(2*mp.pi)


def orbit_end(Om, nsteps):
    x = mp.mpf(0)
    for _ in range(nsteps):
        x = f(x, Om)
    return x


lo, hi = mp.mpf(0), mp.mpf(1)
flo = orbit_end(lo, Q) - P
for _ in range(110):
    mid = (lo + hi)/2
    fm = orbit_end(mid, Q) - P
    if (flo < 0) == (fm < 0):
        lo, flo = mid, fm
    else:
        hi = mid
Omega = (lo + hi)/2
print(f"Omega (bisected, f^{Q}(0) = {P}) = {mp.nstr(Omega, 20)}")
print(f"closure residual f^Q(0) - P = {mp.nstr(orbit_end(Omega, Q) - P, 5)}")

# itinerary over 1.5 periods to confirm periodicity; letters from floors
NIT = Q + 200
xs = [mp.mpf(0)]
for _ in range(NIT):
    xs.append(f(xs[-1], Omega))
floors = [int(mp.floor(v)) for v in xs]
marg = min(abs(v - mp.nint(v)) for v in xs[1:])
itin = [floors[n+1] - floors[n] for n in range(NIT)]
print(f"floor-robustness: min distance of any orbit point to an integer = {mp.nstr(marg, 3)}")
print(f"itinerary periodic with period {Q}: "
      f"{itin[:200] == itin[Q:Q+200]} (first 200 letters of period 2 check)")

W = np.array(itin[:Q], dtype=np.int8)
# exact mechanical word slope P/Q, all cyclic intercepts via integer arithmetic
n_ = np.arange(Q, dtype=np.int64)
best_m, best_s = -1, None
for s in range(Q):
    mech = ((n_+1)*P + s)//Q - (n_*P + s)//Q
    m = int(np.sum(W == mech))
    if m > best_m:
        best_m, best_s = m, s
print(f"ITINERARY vs mechanical word slope {P}/{Q}: best match = {best_m}/{Q}"
      f" (intercept s={best_s})   [expect exact if rotation-ordered]")

# vs the TRUE golden Sturmian slope 1/phi, best intercept, several windows
alpha = (np.sqrt(5) - 1)/2
print(f"\nITINERARY (periodically extended) vs TRUE Sturmian slope 1/phi = {alpha:.15f}:")
for L in (1000, 2000, Q, 5000, 10000):
    ext = np.tile(W, L//Q + 2)[:L].astype(np.int64)
    nn = np.arange(L, dtype=np.float64)
    # candidate intercepts: midpoints between sorted breakpoints {-n alpha mod 1}
    bps = np.sort(np.concatenate([(-nn*alpha) % 1.0, (-(nn+1)*alpha) % 1.0]))
    cand = (bps + np.roll(bps, -1))/2
    cand[-1] = (bps[-1] + bps[0] + 1)/2
    best_L, worst_gap = -1, None
    for b in cand:
        st = np.floor((nn+1)*alpha + b) - np.floor(nn*alpha + b)
        m = int(np.sum(ext == st.astype(np.int64)))
        if m > best_L:
            best_L = m
    print(f"  L = {L:5d}: best match = {best_L}/{L}  = {100*best_L/L:.4f}%"
          f"   (mismatches: {L-best_L})")
print("\n[banked claim: 'itinerary 99.95% Sturmian' -- no window length specified]")
