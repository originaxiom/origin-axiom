"""B390 session 3 -- the attribution: the exact sqrt(-15)-pairing and the dark-pair kills.

The bilinear form B: Q(zeta12) x Q(zeta20) -> Q,  B(x3, x5) = the sqrt(-15)-coefficient of
Pi_H(x3 * x5), computed on the power bases zeta12^r (r=0..3) x zeta20^s (s=0..7) as an exact
4x8 rational matrix. Then for each pair: the 3-side spectral vectors x3(a,b) (the DFT of T3)
and 5-side x5(a,b) (DFT of T5) in those bases; the s-content of t(a,b) = sum over the
convolution of B-pairings; a dark pair's kill is attributed:
  KILL-5: every x5 in the pair's spectrum lies in the RIGHT-kernel of B  (5-side dead)
  KILL-3: every x3 lies in the LEFT-kernel of B                          (3-side dead)
  KILL-C: neither kernel condition holds -- the convolution cancels (the subtle class)."""
import json, os, sys
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
sys.path.insert(0, os.path.join(HERE, "..", "B386_crt_closed_form"))
import cyclo_engine as E
import seam_certification as SC
from step0_exact_matrices import build_theta_W, matrix_order
from tensor_gate import local_partrace_table

# ---- the pairing matrix ----
B = [[Fr(0)]*8 for _ in range(4)]
for r in range(4):
    zr = E.zeta((5*r) % 60)          # zeta12^r
    for s in range(8):
        zs = E.zeta((3*s) % 60)      # zeta20^s
        sol = SC.solve_H(SC.H_avg(E.mul(zr, zs)))
        B[r][s] = sol[3] if sol else Fr(0)
print("pairing matrix B (rows zeta12^r, cols zeta20^s):")
for row in B: print("  ", [str(x) for x in row])

def rank(M):
    M = [row[:] for row in M]
    m, n = len(M), len(M[0]); r = 0
    for c in range(n):
        piv = next((i for i in range(r, m) if M[i][c] != 0), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][c]; M[r] = [v/pv for v in M[r]]
        for i in range(m):
            if i != r and M[i][c] != 0:
                f = M[i][c]; M[i] = [M[i][j]-f*M[r][j] for j in range(n)]
        r += 1
        if r == m: break
    return r
print("rank(B):", rank(B))

def in_left_kernel(x3):   # x3: 4-vector
    return all(sum(x3[r]*B[r][s] for r in range(4)) == 0 for s in range(8))
def in_right_kernel(x5):  # x5: 8-vector
    return all(sum(B[r][s]*x5[s] for s in range(8)) == 0 for r in range(4))

def field_coords(t, kind):
    """exact coordinates of an engine element known to lie in Q(zeta12) or Q(zeta20)."""
    basis = [E.zeta((5*r) % 60) for r in range(4)] if kind == 12 else [E.zeta((3*s) % 60) for s in range(8)]
    n = len(basis)
    # solve t = sum c_i basis_i over the 16-dim engine coords
    M = [[basis[c][row] for c in range(n)] + [t[row]] for row in range(E.DEG)]
    r = 0; piv_cols = []
    for c in range(n):
        piv = next((i for i in range(r, E.DEG) if M[i][c] != 0), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][c]; M[r] = [v/pv for v in M[r]]
        for i in range(E.DEG):
            if i != r and M[i][c] != 0:
                f = M[i][c]; M[i] = [M[i][j]-f*M[r][j] for j in range(n+1)]
        piv_cols.append(c); r += 1
    sol = [Fr(0)]*n
    for i, c in enumerate(piv_cols): sol[c] = M[i][n]
    for i in range(r, E.DEG):
        if M[i][n] != 0: return None
    return sol

PAIRS = [((1,3),"dark"),((1,4),"dark"),((3,5),"dark"),((1,5),"dark"),((4,5),"dark"),
         ((3,4),"bright"),((2,3),"bright")]
out = {"B": [[str(x) for x in row] for row in B], "rankB": rank(B)}
for (m1,m2), st in PAIRS:
    W1 = build_theta_W(m1); W2 = build_theta_W(m2)
    o1,_ = matrix_order(W1); o2,_ = matrix_order(W2)
    T3 = local_partrace_table(3, 2, m1, m2, o1, o2)
    T5 = local_partrace_table(5, 2, m1, m2, o1, o2)
    z1, z2 = 60//o1, 60//o2
    all3_left, all5_right = True, True
    bad = 0
    for a in range(o1):
        for b in range(o2):
            t3 = E.ZERO; t5 = E.ZERO
            for j in range(o1):
                za = E.zeta((-z1*j*a) % 60)
                for l in range(o2):
                    zb = E.zeta((-z2*l*b) % 60)
                    t3 = E.add(t3, E.mul(E.mul(za, zb), T3[(j,l)]))
                    t5 = E.add(t5, E.mul(E.mul(za, zb), T5[(j,l)]))
            c3 = field_coords(E.scal(Fr(1,o1*o2), t3), 12)
            c5 = field_coords(E.scal(Fr(1,o1*o2), t5), 20)
            if c3 is None or c5 is None: bad += 1; continue
            if any(x != 0 for x in c3) and not in_left_kernel(c3): all3_left = False
            if any(x != 0 for x in c5) and not in_right_kernel(c5): all5_right = False
    att = ("KILL-3 (3-side in left-kernel)" if all3_left else
           "KILL-5 (5-side in right-kernel)" if all5_right else
           "KILL-C (convolution cancellation)" if st == "dark" else "LIVE (bright)")
    out[f"{m1},{m2}"] = dict(status=st, all3_left=all3_left, all5_right=all5_right,
                             coord_fail=bad, attribution=att)
    print(f"({m1},{m2}) {st:7s}: 3-side all in left-ker: {all3_left}; 5-side all in right-ker: {all5_right}; -> {att}")
json.dump(out, open(os.path.join(HERE, "attribution.json"), "w"), indent=1)
print("DONE")
