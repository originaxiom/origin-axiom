"""B739 Stage-B recompute — TOMB-L34 (S021: "entanglement = holographic", tombstone L34).

THE DISCRIMINATING FACT (as banked, V37 / FAILURE_ATLAS D3 / TOMBSTONES.md S021):
  (a) The Fibonacci critical chain's entanglement entropy is LOGARITHMIC in subsystem
      size (generic 1D-CFT criticality) — NOT area-law (which, per the arc's own verdict
      logic in holo_arealaw.py, is the holographic-boundary signature) and NOT volume-law
      — and the periodic (known c=1 CFT) control is in the SAME class (genericity).
  (b) The emergent geometry d(i,j) = -log|C_ij| is AdS-like but GENERIC:
      Gromov delta/diam Fibonacci 0.381 ~ periodic 0.385 (random 0.265) — the geometry
      test cannot single out the quasicrystal. Together: "does not bridge".

E19 compute-not-cite, BOTH directions:
  Direction 1 (does the fact recompute?): re-derive (a) and (b) by an independent
      reimplementation from the arc's declared conventions (below).
  Direction 2 (is the fact discriminating?): verify the tests CAN discriminate —
      the strong-disorder control must come out area-law/flat (so "log" is a real
      finding, not what the test always says), and the periodic control must sit in
      the same log class as Fibonacci (so "generic" is earned, not asserted).

DECLARED CONVENTIONS (from the original arc's scripts holo_arealaw.py /
emergent_geometry2.py, frontier/physics_probes/, banked under V37):
  - Fibonacci word: substitution a->ab, b->a, start "a", truncate to N.
  - Hamiltonian: open 1D tight-binding chain, hopping t=1, on-site potential
    +1/2 on 'a', -1/2 on 'b' (periodic control: 0; random control: U(-3,3), seeded).
  - Free fermions; ground-state correlation matrix C = occ @ occ^T (exact method).
  - Entanglement leg: N=1597 (a Fibonacci number), half filling, random seed 0;
    L in {10,20,40,80,160,320,640}; one-cut interval [0,L) and bulk interval
    [N/2-L/2, N/2+L/2); von Neumann entropy in nats.
  - Geometry leg: N=987, filling 1/3, random seed 1; probe sites
    range(60, 60+22*16, 16) (22 sites); D_ij = -log|C_ij| (25.0 if |C_ij|<=1e-12);
    four-point Gromov delta = max over quadruples of (largest - middle)/2 of the
    three pairwise-sum combinations; report delta/diam.
E1 — conventions the arc left implicit, declared HERE:
  - Eigenvalue clipping for entropy: p in [1e-13, 1-1e-13] (as in the arc's script).
  - CFT normalization: for an OPEN chain, one-cut S(L) = (c/6) ln L + const and
    bulk two-cut S(L) = (c/3) ln L + const, so c_eff(one-cut) = 6*logslope and
    c_eff(two-cut) = 3*logslope. (The arc's inline comment said "c/3" for the
    one-cut fit — a factor-2 label slip; it does not affect the kill, which needs
    only log-vs-const-vs-linear. Checked here via the two-cut/one-cut slope ratio ~2.)
  - Model selection (quantifying the arc's qualitative call): fit S = a*lnL + b
    (LOG) and S = a*L + b (LIN) by least squares. AREA-LAW means S is BOUNDED
    (does not grow): logslope < 0.05 (nats per e-fold) AND |linslope| < 1e-3.
    LOG if logslope > 0.05 with R2_log > R2_lin; VOLUME if linslope > 1e-3 with
    R2_lin > R2_log. (First draft of this classifier used ptp(last3)<0.05 for
    AREA — recalibrated: a localized chain's bounded S oscillates with L, and
    "area law" is boundedness, not literal constancy. Recorded here per E1.)
  - "AdS-like" is the arc's Test-1 criterion (emergent_geometry2.py): bulk-averaged
    |C(r)| decays as a POWER LAW (R2 of log-log fit beats R2 of semilog fit) —
    power-law ⇒ AdS-like, exponential ⇒ localized/non-geometric. The delta/diam
    tag thresholds (<0.25 hyperbolic, <0.45 mildly curved) are reported as the
    arc's script prints them; note V37's OWN numbers (0.381/0.385) fall in the
    script's "mildly curved" band — the banked "AdS-like" clause rides on Test 1,
    the banked "generic" clause on delta/diam(fib) ~ delta/diam(per).
  - Genericity tolerance (the arc wrote "~"): |d/D(fib) - d/D(per)| < 0.05.
Deterministic: no wall-clock, no network; the only randomness is the disorder
control with fixed seeds (0 entanglement leg, 1 geometry leg) as in the arc.
"""
import itertools

import numpy as np

EPS = 1e-13


# ---------- shared machinery (independent reimplementation) ----------

def fibonacci_word(n):
    w, prev = "a", "b"
    while len(w) < n:
        w, prev = w + prev, w
    return w[:n]


def hamiltonian(kind, n, seed):
    if kind == "fibonacci":
        diag = np.array([0.5 if ch == "a" else -0.5 for ch in fibonacci_word(n)])
    elif kind == "periodic":
        diag = np.zeros(n)
    elif kind == "random":
        diag = np.random.default_rng(seed).uniform(-3.0, 3.0, n)
    else:
        raise ValueError(kind)
    h = np.diag(diag)
    off = np.ones(n - 1)
    h += np.diag(off, 1) + np.diag(off, -1)
    return h


def correlation_matrix(h, fill):
    _, vecs = np.linalg.eigh(h)
    nocc = int(round(fill * h.shape[0]))
    occ = vecs[:, :nocc]
    return occ @ occ.conj().T


def entropy(corr, idx):
    sub = corr[np.ix_(idx, idx)]
    p = np.clip(np.linalg.eigvalsh(sub), EPS, 1.0 - EPS)
    return float(-np.sum(p * np.log(p) + (1.0 - p) * np.log(1.0 - p)))


def fit_r2(x, y):
    a, b = np.polyfit(x, y, 1)
    resid = y - (a * np.asarray(x) + b)
    ss_res = float(np.sum(resid ** 2))
    ss_tot = float(np.sum((y - np.mean(y)) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0
    return a, b, r2


def classify(ls, s):
    logslope, _, r2_log = fit_r2(np.log(ls), s)
    linslope, _, r2_lin = fit_r2(np.asarray(ls, float), s)
    flat = float(np.ptp(s[-3:]))
    if logslope < 0.05 and abs(linslope) < 1e-3:
        cls = "AREA-LAW (bounded)"
    elif logslope > 0.05 and r2_log >= r2_lin:
        cls = "LOG (1D-CFT critical)"
    elif linslope > 1e-3 and r2_lin > r2_log:
        cls = "VOLUME (extensive)"
    else:
        cls = "UNCLASSIFIED"
    return logslope, linslope, r2_log, r2_lin, flat, cls


def gromov_delta(dist):
    n = dist.shape[0]
    worst = 0.0
    for x, y, z, w in itertools.combinations(range(n), 4):
        sums = sorted((dist[x, y] + dist[z, w],
                       dist[x, z] + dist[y, w],
                       dist[x, w] + dist[y, z]))
        worst = max(worst, (sums[2] - sums[1]) / 2.0)
    return worst


# ---------- Leg (a): entanglement scaling, N=1597, half filling ----------

N_ENT = 1597
LS = [10, 20, 40, 80, 160, 320, 640]
KINDS = ("fibonacci", "periodic", "random")

print("=" * 78)
print("LEG (a): entanglement scaling  (N=%d, half filling, open chain, t=1)" % N_ENT)
print("=" * 78)

leg_a = {}
for kind in KINDS:
    corr = correlation_matrix(hamiltonian(kind, N_ENT, seed=0), fill=0.5)
    s_one = [entropy(corr, list(range(l))) for l in LS]
    s_two = [entropy(corr, list(range(N_ENT // 2 - l // 2, N_ENT // 2 + l // 2)))
             for l in LS]
    leg_a[kind] = (s_one, s_two)

print("\nS(L), one boundary point (interval [0,L)):")
print("  L     " + "".join("%12s" % k for k in KINDS))
for i, l in enumerate(LS):
    print("  %-5d " % l + "".join("%12.4f" % leg_a[k][0][i] for k in KINDS))

print("\nOne-cut fits  (c_eff = 6 * logslope for an open-chain end interval):")
one_cut = {}
for kind in KINDS:
    ls_, lin, r2l, r2n, flat, cls = classify(LS, np.array(leg_a[kind][0]))
    one_cut[kind] = (ls_, lin, r2l, r2n, flat, cls)
    print("  %-10s logslope=%+.4f (R2=%.4f)  linslope=%+.6f (R2=%.4f)  "
          "ptp(last3)=%.4f  c_eff=%.3f  -> %s"
          % (kind, ls_, r2l, lin, r2n, flat, 6 * ls_, cls))

print("\nTwo-cut (bulk interval) fits  (c_eff = 3 * logslope):")
two_cut = {}
for kind in KINDS:
    ls_, lin, r2l, r2n, flat, cls = classify(LS, np.array(leg_a[kind][1]))
    two_cut[kind] = (ls_, lin, r2l, r2n, flat, cls)
    print("  %-10s logslope=%+.4f (R2=%.4f)  linslope=%+.6f (R2=%.4f)  "
          "ptp(last3)=%.4f  c_eff=%.3f  -> %s"
          % (kind, ls_, r2l, lin, r2n, flat, 3 * ls_, cls))

ratio_fib = two_cut["fibonacci"][0] / one_cut["fibonacci"][0]
ratio_per = two_cut["periodic"][0] / one_cut["periodic"][0]
print("\nRT/CFT consistency (two-cut slope / one-cut slope, expect ~2):")
print("  fibonacci: %.3f    periodic: %.3f" % (ratio_fib, ratio_per))


# ---------- Leg (b): emergent geometry, N=987, filling 1/3 ----------

N_GEO = 987
FILL = 1.0 / 3.0
SITES = list(range(60, 60 + 22 * 16, 16))

print()
print("=" * 78)
print("LEG (b): emergent geometry  (N=%d, filling 1/3, %d probe sites, "
      "D=-log|C|)" % (N_GEO, len(SITES)))
print("=" * 78)

print("\nTest 1 — bulk-averaged |C(r)| decay (power-law => AdS-like; exp => localized):")
decay = {}
for kind in KINDS:
    corr = np.abs(correlation_matrix(hamiltonian(kind, N_GEO, seed=1), FILL))
    rs = np.arange(2, 160)
    cr = np.array([np.mean([corr[i, i + r] for i in range(N_GEO // 4, 3 * N_GEO // 4 - r)])
                   for r in rs])
    good = cr > 1e-12
    lr, lc = np.log(rs[good]), np.log(cr[good])
    eta, _, r2_pow = fit_r2(lr, lc)
    invxi, _, r2_exp = fit_r2(rs[good].astype(float), lc)
    is_power = r2_pow > r2_exp
    decay[kind] = (-eta, r2_pow, -invxi, r2_exp, is_power)
    print("  %-10s power eta=%+.3f (R2=%.3f)   exp 1/xi=%+.4f (R2=%.3f)   -> %s"
          % (kind, -eta, r2_pow, -invxi, r2_exp,
             "POWER-LAW/AdS-like" if is_power else "EXP/localized"))

print("\nTest 2 — Gromov delta/diam of D_ij = -log|C_ij| on the 22 probe sites:")
geo = {}
for kind in KINDS:
    corr = np.abs(correlation_matrix(hamiltonian(kind, N_GEO, seed=1), FILL))
    n = len(SITES)
    dist = np.zeros((n, n))
    for a in range(n):
        for b in range(n):
            if a != b:
                c = corr[SITES[a], SITES[b]]
                dist[a, b] = -np.log(c) if c > 1e-12 else 25.0
    diam = float(dist.max())
    delta = gromov_delta(dist)
    geo[kind] = (delta, diam, delta / diam)
    tag = ("hyperbolic/AdS-like" if delta / diam < 0.25
           else "mildly curved" if delta / diam < 0.45 else "flat/non-geometric")
    print("  %-10s delta=%.3f  diam=%.3f  delta/diam=%.3f  -> %s"
          % (kind, delta, diam, delta / diam, tag))

gap = abs(geo["fibonacci"][2] - geo["periodic"][2])
print("\n  |delta/diam(fib) - delta/diam(per)| = %.3f  (genericity tolerance 0.05)"
      % gap)
print("  banked V37 values: fibonacci 0.381, periodic 0.385, random 0.265")


# ---------- Verdict assembly ----------

print()
print("=" * 78)
print("VERDICT CHECKS")
print("=" * 78)

fib_is_log = one_cut["fibonacci"][5].startswith("LOG") and \
    two_cut["fibonacci"][5].startswith("LOG")
per_is_log = one_cut["periodic"][5].startswith("LOG") and \
    two_cut["periodic"][5].startswith("LOG")
rnd_is_area = one_cut["random"][5].startswith("AREA")
fib_not_vol = abs(one_cut["fibonacci"][1]) < 1e-3 and abs(two_cut["fibonacci"][1]) < 2e-3

checks = [
    ("(a1) Fibonacci entanglement is LOG (not area, not volume)",
     fib_is_log and fib_not_vol),
    ("(a2) periodic control is in the SAME log class (genericity of 'log')",
     per_is_log),
    ("(a3) disorder control is AREA-LAW (the test CAN discriminate; E19 dir-2)",
     rnd_is_area),
    ("(b1) 'AdS-like': power-law |C(r)| decay for fib AND periodic; the localized"
     " control is EXP (Test 1 discriminates)",
     decay["fibonacci"][4] and decay["periodic"][4] and not decay["random"][4]),
    ("(b2) fib ~ periodic within 0.05 in delta/diam (the geometry does not"
     " single out fib)",
     gap < 0.05),
    ("(b3) recomputed delta/diam match the banked V37 numbers to 3 decimals"
     " (0.381 / 0.385 / 0.265)",
     abs(geo["fibonacci"][2] - 0.381) < 5e-4 and
     abs(geo["periodic"][2] - 0.385) < 5e-4 and
     abs(geo["random"][2] - 0.265) < 5e-4),
]
all_pass = True
for label, ok in checks:
    all_pass = all_pass and ok
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))

print()
if all_pass:
    print("RECOMPUTED VERDICT: RECONFIRMED — the entanglement is logarithmic"
          " (generic 1D-CFT criticality, shared with the periodic control; the"
          " holographic-boundary signature would be area-law and is exhibited"
          " only by the localized control), and the emergent geometry is"
          " AdS-like but generic (Fibonacci ~ periodic). S021 does not bridge.")
else:
    print("RECOMPUTED VERDICT: the banked discriminating fact did NOT fully"
          " recompute — see FAIL lines above.")
