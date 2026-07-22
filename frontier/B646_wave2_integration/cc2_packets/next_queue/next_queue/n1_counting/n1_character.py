"""N1-D1: exact CHARACTERS of rho(A1) = T^2ST per parity sector, E6 k=1..7.
Power-trace DFT at dps 50 (prereg aa47092d). Levels 4..7 reconstruct from the
persisted exact counts (levelN_blocks.npz); 1..3 build fresh. Certificates:
sector order must divide the CSP bound ord(A1 mod ord T_k) (else FLAG — would
contradict congruence); multiplicities integer to 1e-30, nonneg, sum=dim;
character at j=1 must equal the banked sector traces."""
import sys, json
sys.path.insert(0, '<cc2-seat>/seat-work/level_ladder_campaign/scripts')
import numpy as np
import mpmath as mp
from engine import Level, enumerate_level_weights, theta_split, weyl_group, HVEE

mp.mp.dps = 50
OUTDIR = '<cc2-seat>/seat-work/next_queue/n1_counting'
NPZ = '<cc2-seat>/seat-work/level_ladder_campaign/outputs/level%d_blocks.npz'
BANKED_Z = {1: 1, 2: 1, 3: 1, 4: 0, 5: 1, 6: 1, 7: 2}
BANKED_SECT = {1: (1, 0), 2: (1, 0), 3: (0, 1), 4: (0, 0), 5: (0, 1), 6: (1, 0), 7: (1, 1)}
CSP_BOUND = {1: 12, 2: 24, 3: 60, 4: 12, 5: 36, 6: 36, 7: 36}   # ord(A1 mod ordT), n2 table

W, eps = weyl_group()

def get_level(k):
    if k <= 3:
        return Level(k, W, eps)
    z = np.load(NPZ % k)
    L = object.__new__(Level)
    L.k, L.K = k, k + HVEE
    L.M6 = 6 * L.K
    L.PRIM = enumerate_level_weights(k)
    L.N = len(L.PRIM)
    L.fixed_idx, L.pairs = theta_split(L.PRIM)
    L.W, L.eps = W, eps
    L.counts, L.T_expo = z['counts'], z['T_expo']
    return L

def sector_blocks(L):
    S, T = L.S_mp(50), L.T_mp(50)
    rho = T * T * S * T
    s2 = 1 / mp.sqrt(2)
    n_o, n_f = len(L.pairs), len(L.fixed_idx)
    odd = mp.matrix(L.N, n_o)
    even = mp.matrix(L.N, n_f + n_o)
    for j, (a, b) in enumerate(L.pairs):
        odd[a, j], odd[b, j] = s2, -s2
        even[a, n_f + j], even[b, n_f + j] = s2, s2
    for j, i in enumerate(L.fixed_idx):
        even[i, j] = 1
    return odd.T * rho * odd, even.T * rho * even

def character(B, cap, tag):
    n = B.rows
    if n == 0:
        return {"dim": 0, "ord": 1, "mult": {}, "trace": 0}
    I = mp.eye(n)
    traces = [mp.mpc(n)]
    P = B.copy()
    order = None
    for j in range(1, cap + 1):
        traces.append(mp.fsum(P[i, i] for i in range(n)))
        dev = max(abs(P[i, l] - I[i, l]) for i in range(n) for l in range(n))
        if dev < mp.mpf('1e-35'):
            order = j
            break
        P = P * B
    assert order is not None, f"{tag}: order exceeds CSP bound {cap} — FLAG (congruence!)"
    mult = {}
    for r in range(order):
        m = mp.fsum(traces[j] * mp.e ** (-2j * mp.pi * j * r / order)
                    for j in range(order)) / order
        mi = int(mp.nint(m.real))
        assert abs(m - mi) < mp.mpf('1e-30') and mi >= 0, f"{tag}: bad mult r={r}: {m}"
        if mi:
            mult[r] = mi
    assert sum(mult.values()) == n, f"{tag}: mult sum != dim"
    tr1 = complex(traces[1]) if order > 1 else complex(n)
    return {"dim": n, "ord": order, "mult": mult, "trace": round(tr1.real)}

results = {}
for k in range(1, 8):
    L = get_level(k)
    Bo, Be = sector_blocks(L)
    co = character(Bo, CSP_BOUND[k], f"k={k} odd")
    ce = character(Be, CSP_BOUND[k], f"k={k} even")
    assert (co["trace"], ce["trace"]) == BANKED_SECT[k], \
        f"k={k}: sector traces {(co['trace'], ce['trace'])} != banked {BANKED_SECT[k]}"
    assert co["trace"] + ce["trace"] == BANKED_Z[k]
    results[k] = {"odd": co, "even": ce}
    print(f"k={k}: odd dim {co['dim']:3d} ord {co['ord']:3d} | even dim {ce['dim']:3d} "
          f"ord {ce['ord']:3d} | sector traces {(co['trace'], ce['trace'])} GATE-OK", flush=True)
    print(f"   odd  mult: {co['mult']}", flush=True)
    print(f"   even mult: {ce['mult']}", flush=True)

with open(f"{OUTDIR}/characters.json", "w") as f:
    json.dump({str(k): {s: {"dim": v[s]["dim"], "ord": v[s]["ord"], "trace": v[s]["trace"],
                            "mult": {str(r): m for r, m in v[s]["mult"].items()}}
                        for s in ("odd", "even")} for k, v in results.items()}, f, indent=1)
print("DONE — characters.json written", flush=True)
