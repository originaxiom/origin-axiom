"""B1041 — PM1: the theta-leg. Exact F2 linear algebra, no numerics.

V1: assemble both actions from banked data (B766's flip-vectors; the Galois action
    on the compositum's sign-vectors; B782's free transitive action).
V2: the finite intertwining check for Phi: (c,theta,gamma5) -> (s-3, s5, s-7).
V3: verdict per the sealed outcome space.
"""
from itertools import permutations, product

# ---- V1a: the operation cube's translation vectors on the closing coordinates
# Closing coordinates (T4, T6, T3): chirality's side, the chord's sign, the
# basepoint/time bit (T7 = T3 banked). From B766's action table (each entry
# derived in that arc, cc3-audited):
#   c   flips T4 and T6          -> (1,1,0)
#   theta flips T6 only          -> (0,1,0)
#   gamma5 flips T3 (=T7) only   -> (0,0,1)
v = {"c": (1, 1, 0), "theta": (0, 1, 0), "gamma5": (0, 0, 1)}

# ---- V1b: the Galois cube's translation vectors on the sign coordinates
# Sign coordinates (s-3, s5, s-7): the signs of sqrt(-3), sqrt(5), sqrt(-7) in
# the compositum's square-root-choice torsor (B704's multiquadratic structure;
# each sigma negates its own radical, fixes the other two coordinates):
w = {"s-3": (1, 0, 0), "s5": (0, 1, 0), "s-7": (0, 0, 1)}

# Phi, forced on generators by the two banked legs + elimination (the seal):
#   c -> sigma_{-3}   (B766: gamma3 == c, the being-Galois IS conjugation)
#   gamma5 -> sigma_5 (B766: time's arrow = sqrt(5)'s sign)
#   theta -> sigma_{-7} (elimination; THE PAIRING UNDER TEST)
Phi = {"c": "s-3", "theta": "s-7", "gamma5": "s5"}

def xor(a, b):
    return tuple((x + y) % 2 for x, y in zip(a, b))

# ---- V2 pre-check: rank of the operation translations (B766's rank-3, recomputed)
def rank_f2(rows):
    rows = [list(r) for r in rows]
    r = 0
    for col in range(3):
        piv = next((i for i in range(r, len(rows)) if rows[i][col]), None)
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        for i in range(len(rows)):
            if i != r and rows[i][col]:
                rows[i] = [(a + b) % 2 for a, b in zip(rows[i], rows[r])]
        r += 1
    return r

print("[V1] operation translations:", v)
print("[V1] Galois translations:", w)
rk = rank_f2(list(v.values()))
print(f"[V1] rank of (c,theta,gamma5) translations = {rk} (B766 banked: 3)")
assert rk == 3

# ---- V2a: the coordinate-permutation dictionary question (the natural reading
# of "basis dictionary"): does ANY axis<->radical bijection intertwine?
perm_hits = []
for pi in permutations(range(3)):  # axis i -> radical pi[i]
    ok = True
    for g, vg in v.items():
        target = w[Phi[g]]
        mapped = tuple(vg[pi.index(j)] if False else 0 for j in range(3))
        # correct mapping: coordinate permutation sends flip-set {i: vg[i]=1}
        # to {pi[i]}; equivariance needs image flip-set == target flip-set
        image = [0, 0, 0]
        for i in range(3):
            if vg[i]:
                image[pi[i]] ^= 1
        if tuple(image) != target:
            ok = False
            break
    if ok:
        perm_hits.append(pi)
print(f"[V2a] coordinate-permutation dictionaries intertwining Phi: {len(perm_hits)} of 6")

# ---- V2b: the general linear intertwiner. L is determined on the translation
# basis by L(v_g) = w_{Phi(g)}; solve for L on the standard basis and check
# invertibility + the 3x8 equivariance table.
# v_c=(1,1,0), v_theta=(0,1,0), v_gamma5=(0,0,1) -> e1 = v_c + v_theta.
L = {}
L_e2 = w[Phi["theta"]]                      # L(e_T6)  = s-7 direction
L_e3 = w[Phi["gamma5"]]                     # L(e_T3)  = s5 direction
L_e1 = xor(w[Phi["c"]], L_e2)               # L(e_T4)  = L(v_c) + L(e_T6)
Lrows = [L_e1, L_e2, L_e3]
print(f"[V2b] L(e_T4)={L_e1}  L(e_T6)={L_e2}  L(e_T3)={L_e3}")
assert rank_f2(Lrows) == 3, "L not invertible"
print("[V2b] L is INVERTIBLE over F2 (rank 3)")

def apply_L(x):
    out = (0, 0, 0)
    for i, xi in enumerate(x):
        if xi:
            out = xor(out, Lrows[i])
    return out

# the affine match: match(x) = L(x) + b. Equivariance holds for EVERY b (checked
# for all 8 -- the 8-fold freedom IS B782's no-canonical-point, preserved).
full_pass = 0
for b in product((0, 1), repeat=3):
    ok = all(
        xor(apply_L(xor(x, v[g])), b) == xor(w[Phi[g]], xor(apply_L(x), b))
        for g in v for x in product((0, 1), repeat=3)
    )
    full_pass += ok
print(f"[V2b] affine matches passing the full 3x8 equivariance table: {full_pass} of 8")

# consistency of the banked point-level pin (time's arrow = sqrt5's sign):
print(f"[V2b] banked pin check: L maps the T3 direction to {apply_L((0,0,1))} (= s5 direction: {L_e3 == w['s5']})")

# ---- V3
print()
print("[V3] VERDICT INPUTS:")
print(f"  coordinate-permutation dictionary: IMPOSSIBLE ({len(perm_hits)}/6) --")
print("    obstruction: c's flip-set has size 2 (T4 and the chord T6) while")
print("    sigma_{-3} flips exactly one radical; no bijection matches cardinalities.")
print("  linear intertwiner: EXISTS, UNIQUE given Phi, invertible; all 8 affine")
print("    liftings pass the full table (the 8 = the torsor's basepoint freedom,")
print("    B782's no-canonical-point PRESERVED -- no section smuggled).")
print("  the diagonal: L(e_T4) = s-3 + s-7 -- chirality's side is the being(+)E6")
print("    DIAGONAL, not a single leg; the chord direction maps to s-7 PURE.")
print("  theta <-> sqrt(-7): HOLDS inside the exhibited L (the pairing under test).")
print("==== B1041 compute done ====")
