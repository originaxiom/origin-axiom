"""C8 (P-639, Theorem 55 Part 1): the lane's sector pairing (sum signs; mod-5 transposition) as a function of the line order N.
Charges (B1656/B1691 SIXY): up (1,-4), down (1,2), lepton (-3,6).  For each N: which sectors coincide mod N, which are
transposes mod N, which are self-transposed.  Pure arithmetic."""
import pathlib
S = {"up": (1, -4), "down": (1, 2), "lepton": (-3, 6)}
out = ["sum q_L + q_R: " + str({k: a + b for k, (a, b) in S.items()})]
for N in (2, 3, 4, 5, 6, 8, 10, 12):
    m = {k: (a % N, b % N) for k, (a, b) in S.items()}
    eq = [(x, y) for x in S for y in S if x < y and m[x] == m[y]]
    tr = [(x, y) for x in S for y in S if x < y and m[x] == m[y][::-1] and m[x] != m[y]]
    st = [x for x in S if m[x][0] == m[x][1]]
    out.append("N=%2d mod-pairs %s | equal %s | transposed %s | self-transposed %s" % (N, m, eq, tr, st))
print("\n".join(out)); pathlib.Path(__file__).with_name("c8_run.txt").write_text("\n".join(out) + "\n")
