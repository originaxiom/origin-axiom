HERE = __file__.rsplit("/", 1)[0]
src = open(HERE + '/r15_types_modp.py').read().split("# ---------------- run at banked prime")[0]
src = src.replace('__file__.rsplit("/", 1)[0]', repr(HERE))
exec(src)
from flint import nmod_mat
for p in (40039, 40639):
    rs, _ = poly_roots_modp(MU, p)
    s2, _ = poly_roots_modp(SEXT2, p)
    s6, _ = poly_roots_modp(SEXT6, p)
    print(f"p={p}: mu roots {rs}; sext2 {s2}; sext6 {s6}")
    grid = {}
    for r in rs:
        for s in s2:
            nul, _ = joint_nullity(p, r, s)
            grid[(r, s)] = nul
    print("  sext2 grid:", {v: sum(1 for x in grid.values() if x == v) for v in set(grid.values())})
    r, s = [(r, s) for (r, s), v in grid.items() if v == 14][0]
    first_measurement_type(p, rs[0])
    analyze(p, r, s, "SMT wall")
    g6 = {}
    for r0 in rs:
        for s0 in s6:
            nul, _ = joint_nullity(p, r0, s0)
            g6[(r0, s0)] = nul
    print("  sext6 grid:", {v: sum(1 for x in g6.values() if x == v) for v in set(g6.values())})
    break
p = 40123
rs, _ = poly_roots_modp(MU, p)
r = rs[0]
M1 = [[(AD[8][i][j] + r * AD[16][i][j]) % p for j in range(DIM)] for i in range(DIM)]
M2 = [[AD[16][i][j] % p for j in range(DIM)] for i in range(DIM)]
Mat = nmod_mat(M1 + M2, p)
print("z(x1, g16) [slope-infinity endpoint] dim =", DIM - Mat.rank())
M3 = [[AD[14][i][j] % p for j in range(DIM)] for i in range(DIM)]
Mat = nmod_mat(M1 + M3, p)
print("z(x1, g14) [slope-0 endpoint] dim =", DIM - Mat.rank())
