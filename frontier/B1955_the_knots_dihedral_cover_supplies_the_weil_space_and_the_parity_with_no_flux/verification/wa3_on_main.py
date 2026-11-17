"""B1955: main's own recomputation of the web seat's W-A3 (harvest row 1866), with the dihedral cover's facts main found first.
No data; the web seat's scripts are not run or imported.
A  the figure-eight's group (SnapPy's presentation): homomorphisms onto the dihedral group of order 2p, p = 3..31 odd, and 25.
B  at p = 5: the meridian, the longitude, the cusp's preimages; the centraliser of the image in S5 (the deck group of the
   5-sheeted cover) and of its index-2 rotation subgroup (the deck group over the double cover).
C  the covers' homology (SnapPy): the 3-cusped 5-sheeted cover.
D  the two Weil classes c = 1, 2 on C^5: the group generated, det = 1 on all 120 elements, rho_c(-I) = P, rho_c(LR) against
   scalar multiples of P; the T-spectrum of the exterior powers; the trace signature r = tr R(T^2) / tr R(T)^2 on
   rho_c (x) conj(rho_c') and on the frame's 25 lines.
E  the knot's quadratic form: q = x^2/5; B1951's class is 2x^2/5.
F  level 25: roots of x^2 - 3x + 1 mod 5 and mod 25; the up sector's phases (from B1953's stored output: order 25)."""
import itertools, json, pathlib
from fractions import Fraction as Fr
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
OUT = {}
import snappy
M = snappy.Manifold("m004"); G = M.fundamental_group(); gens = G.generators(); rels = G.relators(); mer, lon = G.peripheral_curves()[0]


def dihedral(p):
    """homomorphisms onto the dihedral group of order 2p acting on Z/p; returns [(image of a, of b, meridian, longitude)]"""
    els = [tuple((s * x + c) % p for x in range(p)) for s in (1, -1) for c in range(p)]
    mul = lambda f, g: tuple(f[g[x]] for x in range(p)); idt = tuple(range(p))
    inv = lambda f: tuple(sorted(range(p), key=lambda x: f[x]))
    def word(w, img):
        r = idt
        for ch in w: r = mul(r, img[ch] if ch.islower() else inv(img[ch.lower()]))
        return r
    out = []; sizes = set()
    for fa in els:
        for fb in els:
            img = dict(zip(gens, (fa, fb)))
            if all(word(r, img) == idt for r in rels):
                grp = {idt}; fr = [idt]
                while fr:
                    nx = []
                    for h in fr:
                        for k in (fa, fb):
                            n = mul(h, k)
                            if n not in grp: grp.add(n); nx.append(n)
                    fr = nx
                sizes.add(len(grp))
                if len(grp) == 2 * p: out.append((fa, fb, word(mer, img), word(lon, img), grp))
    return out, sorted(sizes)


primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
has = {p: len(dihedral(p)[0]) for p in primes}
OUT["A_dihedral_primes"] = [p for p in primes if has[p]]
r25, sizes25 = dihedral(25)
OUT["A_onto_D25"] = len(r25); OUT["A_image_sizes_mod_25"] = sizes25
print("A: homomorphisms onto the dihedral group of order 2p exist at p in %s among %s; onto the dihedral group of order 50: %d (image sizes found mod 25: %s)" % (OUT["A_dihedral_primes"], primes, len(r25), sizes25))
reps5, _ = dihedral(5); fa, fb, m, l, grp = reps5[0]; idt = tuple(range(5))
orbs = []; seen = set()
for x in range(5):
    if x not in seen:
        o = {x}; fr = [x]
        while fr:
            y = fr.pop()
            for f in (m, l):
                if f[y] not in o: o.add(f[y]); fr.append(f[y])
        seen |= o; orbs.append(len(o))
S5 = list(itertools.permutations(range(5))); mul = lambda f, g: tuple(f[g[x]] for x in range(5))
cent_full = [s for s in S5 if all(mul(s, g) == mul(g, s) for g in grp)]
rot = [g for g in grp if all(g[x] == (g[0] + x) % 5 for x in range(5))]
cent_rot = [s for s in S5 if all(mul(s, g) == mul(g, s) for g in rot)]
OUT["B"] = {"count": len(reps5), "longitude_trivial": l == idt, "meridian_fixed_sheets": sum(1 for x in range(5) if m[x] == x), "meridian_order": 2 if mul(m, m) == idt else 0,
            "cusp_degrees": sorted(orbs), "deck_group_over_m004": len(cent_full), "rotations": len(rot), "deck_group_over_the_double_cover": len(cent_rot)}
print("B: at p = 5: %d homomorphisms; the longitude acts trivially: %s; the meridian is an involution fixing %d sheet; the cusp's preimages have degrees %s; the centraliser of the image in S5 has order %d (no deck transformations over m004); of its %d rotations, order %d (the shifts, over the double cover)"
      % (len(reps5), l == idt, OUT["B"]["meridian_fixed_sheets"], sorted(orbs), len(cent_full), len(rot), len(cent_rot)))
c5 = [(c.num_cusps(), str(c.cover_info()["type"]), str(c.homology())) for c in M.covers(5)]
c2 = [(c.num_cusps(), str(c.homology())) for c in M.covers(2)]
three = [c for c in M.covers(5) if c.num_cusps() == 3][0]
OUT["C"] = {"degree_5": sorted(c5), "degree_2": c2, "three_cusped": [three.volume() / M.volume(), str(three.homology()), [str(x) for x in three.identify()[:3]]]}
print("C: covers of degree 2: %s; of degree 5: %s; the 3-cusped one: volume ratio %.6f, homology %s, identified as %s" % (c2, sorted(c5), three.volume() / M.volume(), three.homology(), [str(x) for x in three.identify()[:3]]))
z = np.exp(2j * np.pi / 5); psi = lambda x: z ** (x % 5)
P = np.array([[1.0 if (x + y) % 5 == 0 else 0.0 for y in range(5)] for x in range(5)])
F = np.array([[psi(x * y) for y in range(5)] for x in range(5)]) / np.sqrt(5)
def weil(c):
    T = np.diag([psi(c * x * x) for x in range(5)])
    for k in (1, 2, 3, 4):                                             # the Fourier kernel psi(k x y) and the scalar that make (ST)^3 = S^2
        Fk = np.array([[psi(k * x * y) for y in range(5)] for x in range(5)]) / np.sqrt(5)
        for s in (1, -1, 1j, -1j):
            S = s * Fk
            if np.abs(np.linalg.matrix_power(S @ T, 3) - S @ S).max() < 1e-12 and np.abs(np.linalg.matrix_power(S, 4) - np.eye(5)).max() < 1e-12: return T, S
key = lambda A: tuple(np.round(A.flatten(), 8))
OUT["D"] = {}
RH = {}
for c in (1, 2):
    T, S = weil(c); RH[c] = (T, S)
    Gp = {key(np.eye(5)): np.eye(5, dtype=complex)}; fr = [np.eye(5, dtype=complex)]
    while fr:
        nx = []
        for A in fr:
            for g in (T, S):
                N = A @ g
                if key(N) not in Gp: Gp[key(N)] = N; nx.append(N)
        fr = nx
    dets = max(abs(np.linalg.det(A) - 1) for A in Gp.values())
    # LR = [[2, 1], [1, 1]] as a word in S, T: try the candidates and keep those inducing LR on the labels (a, b)
    Ti = T.conj().T; Si = S.conj().T
    X = np.roll(np.eye(5), 1, axis=0).astype(complex); Z = np.diag([psi(x) for x in range(5)])
    Wop = lambda a, b: np.linalg.matrix_power(X, a % 5) @ np.linalg.matrix_power(Z, b % 5)
    def induced(U):
        def im(a, b):
            Mm = U @ Wop(a, b) @ U.conj().T
            return max(itertools.product(range(5), repeat=2), key=lambda v: abs(np.trace(Wop(*v).conj().T @ Mm)))
        return (im(1, 0), im(0, 1))
    acts = {}
    for wd in itertools.product(range(4), repeat=4):
        U = np.eye(5, dtype=complex)
        for i in wd: U = U @ (T, Ti, S, Si)[i]
        ind = induced(U); tr = (ind[0][0] + ind[1][1]) % 5; dt = (ind[0][0] * ind[1][1] - ind[0][1] * ind[1][0]) % 5
        if tr == 3 and dt == 1 and ind not in (((1, 0), (0, 1)), ((4, 0), (0, 4))): acts.setdefault(ind, U)      # minus the identity also has trace 3 mod 5: excluded, it is P itself
    dist = min(min(np.abs(U - s * P).max() for s in [np.exp(2j * np.pi * t / 360) for t in range(360)]) for U in acts.values())
    sq = np.abs(S @ S - P).max()
    lam = {}
    ev = np.linalg.eigvals(T)
    for k in range(6):
        for idx in itertools.combinations(range(5), k):
            lam[k] = max(lam.get(k, 0), abs(np.prod(ev[list(idx)]) ** 5 - 1))
    OUT["D"][str(c)] = {"group_order": len(Gp), "det_minus_one": float(dets), "S2_is_P": float(sq), "words_inducing_trace_3": len(acts), "LR_distance_to_scalar_P": float(dist), "exterior_T_spectrum_fifth_roots": float(max(lam.values())),
                        "T_phases_even": sorted({(c * x * x) % 5 for x in range(5)})}
    print("D: class %d (T = diag psi(%d x^2)): the group has %d elements; det = 1 on all (%.0e); rho(-I) = P (%.0e); an element inducing a non-central map of trace 3 on the labels (the act's class) is never a scalar times P (least distance %.3f over %d such maps); every exterior power's T-spectrum is in fifth roots (%.0e); T-phases x5: %s"
          % (c, c, len(Gp), dets, sq, dist, len(acts), max(lam.values()), OUT["D"][str(c)]["T_phases_even"]))
def sig(c1, c2):
    t1 = lambda n: np.trace(np.linalg.matrix_power(RH[c1][0], n)) * np.conj(np.trace(np.linalg.matrix_power(RH[c2][0], n)))
    return (t1(2) / t1(1) ** 2).real, t1(1).real
lines_tr = lambda n: sum(1 for a in range(5) for b in range(5) if (a, (b - n * a) % 5) == (a, b))        # the frame's lines: T moves (a, b) to (a, b - a) with a phase that is 1 on its fixed lines a = 0
OUT["D"]["signature"] = {"same_1": sig(1, 1)[0], "same_2": sig(2, 2)[0], "mixed": sig(1, 2)[0], "frame_lines": lines_tr(2) / lines_tr(1) ** 2}
print("D: the trace signature tr R(T^2) / tr R(T)^2: same class %.3f and %.3f, mixed classes %.3f; on the frame's 25 lines %.3f (tr R(T) = %d)" % (sig(1, 1)[0], sig(2, 2)[0], sig(1, 2)[0], lines_tr(2) / lines_tr(1) ** 2, lines_tr(1)))
V = np.array([[1, 1], [0, -1]]); A = V + V.T
Ai = [[Fr(-2, -5), Fr(-1, -5)], [Fr(-1, -5), Fr(2, -5)]]
qs = [str((n * n * Ai[0][0] / 2) % 1) for n in range(5)]; bs = [str((n * n * Ai[0][0]) % 1) for n in range(5)]
OUT["E"] = {"q": qs, "b": bs, "signature": int(np.sign(np.linalg.eigvalsh(A)).sum()), "det": int(round(np.linalg.det(A)))}
print("E: the knot's form V + V^T = %s (det %d, signature %d): q(n g) = %s (x^2/5, a residue); b(n g, n g) = %s (2x^2/5); B1951's rho(T) = diag psi(2 x^2) is the other class" % (A.tolist(), OUT["E"]["det"], OUT["E"]["signature"], qs, bs))
r5 = [x for x in range(5) if (x * x - 3 * x + 1) % 5 == 0]; r25 = [x for x in range(25) if (x * x - 3 * x + 1) % 25 == 0]
B53 = json.loads((HERE.parents[1] / "B1953_frame_cs_down_coupling_is_the_symbol_of_one_covariant_operator_on_families_times_the_weil_space" / "verification" / "weyl_operator.json").read_text())
up_orders = sorted({B53[k][g]["phase_order"] for k in B53 if " up " in k for g in "TS"}); dn_orders = sorted({B53[k][g]["phase_order"] for k in B53 if " down " in k for g in "TS"})
OUT["F"] = {"roots_mod_5": r5, "roots_mod_25": r25, "up_phase_orders": up_orders, "down_phase_orders": dn_orders, "q2_sums_mod_5": {"down": (1 + 4) % 5, "lepton": (9 + 36) % 5, "up": (1 + 16) % 5}}
print("F: x^2 - 3x + 1 has roots %s mod 5 and %s mod 25; frame C's phases (B1953's stored output): up of order %s, down of order %s; q_L^2 + q_R^2 mod 5: down %d, lepton %d, up %d"
      % (r5, r25, up_orders, dn_orders, (1 + 4) % 5, (9 + 36) % 5, (1 + 16) % 5))
(HERE / "wa3_on_main.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")
