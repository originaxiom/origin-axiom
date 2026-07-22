"""N2 part (c): measure ord(B_odd) for SU(3)_13 (kappa=16). Gate: SU(3)_2 first
(banked clock 10, tr_odd = -1/phi). Word convention: A1 = T^2 S T (locked)."""
import sys, os
sys.path.insert(0, '<cc2-seat>/seat-work/veins/v7_conduit')
import mpmath as mp
from engine_v7 import An_Level

mp.mp.dps = 50

def odd_block_word(k):
    L = An_Level(3, k, name=f"SU(3)_{k}")
    S, T = L.build(verbose=False)
    fixed_idx, pairs = L.theta_split()
    N = S.rows
    odd = mp.matrix(N, len(pairs))
    s2 = 1 / mp.sqrt(2)
    for jj, (a, b) in enumerate(pairs):
        odd[a, jj], odd[b, jj] = s2, -s2
    Tm = odd.T * T * odd
    Sm = odd.T * S * odd
    A1 = Tm * Tm * Sm * Tm
    return A1, len(pairs)

def elt_order(M, cap=400):
    n = M.rows
    I = mp.eye(n)
    P = M.copy()
    for j in range(1, cap + 1):
        dev = max(abs(P[i, l] - I[i, l]) for i in range(n) for l in range(n))
        if dev < mp.mpf('1e-35'):
            return j, dev
        P = P * M
    return None, None

# gate: k=2
A1, d = odd_block_word(2)
o, dev = elt_order(A1)
tr = A1[0, 0] + A1[1, 1]
phi = (1 + mp.sqrt(5)) / 2
gate_ok = (o == 10) and abs(tr + 1/phi) < mp.mpf('1e-40')
print(f"GATE SU(3)_2: dim_odd={d} clock={o} (banked 10) dev={mp.nstr(dev,3)} "
      f"tr={mp.nstr(tr,25)} vs -1/phi ok={gate_ok}", flush=True)
assert gate_ok, "GATE FAILED"

# fresh rung: k=13
A1, d = odd_block_word(13)
o, dev = elt_order(A1)
tr = A1[0, 0] + A1[1, 1] if d == 1 else mp.fsum(A1[i, i] for i in range(A1.rows))
print(f"SU(3)_13: dim_odd={d} MEASURED clock={o} dev={mp.nstr(dev,3) if dev else dev} "
      f"(SEALED PREDICTION: 12)  tr(B_odd)={mp.nstr(tr, 30)}", flush=True)
