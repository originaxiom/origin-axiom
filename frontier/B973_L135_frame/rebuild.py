#!/usr/bin/env python3
"""B973 / L135 -- THE REBUILD: frame, floor, M12 constructed on this bench.

Mandate: import frontier/B961_frame_instrument/frame.py (do NOT reimplement e6);
construct the frame, the floor and M12; then VALIDATE against banked numbers.
If validation fails: STOP and report. No tuning.

Definitional source (all in-repo, bench-owned):
  - the four charges  : B854_centralizer_exact/e6_centralizer.py  INV[8,14,16,22]
  - the frame         : B911_cmt_document/CMT_DRAFT.md:23-25  (Killing Gram, sig (2,2))
  - core / floor      : CMT_DRAFT.md:32-34, ingredient table row 3
  - kappa, walls, M12 : CMT_DRAFT.md:62-69, 117-127, table rows 5/12

Everything below is COMPUTED here. Banked comparison values are quoted from the
above files and are labelled CITED at the point of comparison.

REPRESENTATION (house rule 3): g8,g14,g16,g22 are ADJOINT-sector elements -- they
live in e6 itself, not in the 27. Every centralizer taken below is therefore a
rank-preserving construction. No 27 VEV appears anywhere in this file.

Stage A/B are exact over Q. Stage C is mod p at TWO primes never used on this
bench before (record: 40009 40013 40037 40039 40063 40123 40639 40829; the B973
scout added 40883). Bound direction, stated once: mod-p nullity >= char-0
nullity, mod-p rank <= char-0 rank. So Stage C is EVIDENCE, not a char-0
certificate.
"""
import sys, json, time, random
sys.path.insert(0, "/Users/dri/origin-axiom/frontier/B961_frame_instrument")
import sympy as sp
import frame

T0 = time.time()
def log(m): print(f"[{time.time()-T0:7.1f}s] {m}", flush=True)

DIM, N = frame.DIM, frame.N
BB, ROOTS, C = frame.BB, frame.ROOTS, frame.C
INV = frame._G["INV"]
NS = [8, 14, 16, 22]
CH = {n: INV[n] for n in NS}
R = {}

# ============================================================ STAGE A (exact Q)
log("STAGE A -- exact over Q")
AD = {n: frame.ad(CH[n]) for n in NS}

# A0. the frame is abelian: all 6 brackets vanish.
br_zero = [bool((AD[NS[i]] * AD[NS[j]] - AD[NS[j]] * AD[NS[i]]).is_zero_matrix)
           for i in range(4) for j in range(i + 1, 4)]
R["A0_frame_abelian_6_of_6"] = all(br_zero)
random.seed(1973)
_au = frame.ad([sp.Rational(random.randrange(-5, 6)) for _ in range(DIM)])
_av = frame.ad([sp.Rational(random.randrange(-5, 6)) for _ in range(DIM)])
R["A0_control_random_pair_commutes"] = bool((_au * _av - _av * _au).is_zero_matrix)
log(f"A0 frame abelian: {R['A0_frame_abelian_6_of_6']}  "
    f"(CONTROL random pair commutes = {R['A0_control_random_pair_commutes']}, must be False)")

# A1. THE FRAME := the ordered 4-tuple (g8,g14,g16,g22) together with its Killing Gram.
Gm = sp.zeros(4, 4)
for i in range(4):
    for j in range(i, 4):
        t = (AD[NS[i]] * AD[NS[j]]).trace()
        Gm[i, j] = t; Gm[j, i] = t
diag = [Gm[i, i] for i in range(4)]
R["A1_gram_diagonal"] = all(Gm[i, j] == 0 for i in range(4) for j in range(4) if i != j)
R["A1_gram_diag_entries"] = [str(d) for d in diag]
R["A1_gram_signs"] = [int(sp.sign(d)) for d in diag]
R["A1_signature"] = [R["A1_gram_signs"].count(1), R["A1_gram_signs"].count(-1)]
log(f"A1 frame Gram diagonal={R['A1_gram_diagonal']} signs={R['A1_gram_signs']} "
    f"signature={tuple(R['A1_signature'])}")
log(f"   norms = {R['A1_gram_diag_entries']}")
_rad = [frame.ad([sp.Rational(random.randrange(-3, 4)) for _ in range(DIM)]) for _ in range(4)]
_rg = sp.Matrix(4, 4, lambda i, j: (_rad[i] * _rad[j]).trace())
R["A1_control_random_gram_diagonal"] = all(_rg[i, j] == 0 for i in range(4)
                                           for j in range(4) if i != j)
log(f"   CONTROL random 4-tuple Gram diagonal = {R['A1_control_random_gram_diagonal']} "
    "(must be False)")

# A2. THE CORE := z(g8).
core = AD[8].nullspace()
Bc = sp.Matrix.hstack(*core)
cdim = Bc.shape[1]
R["A2_dim_core"] = cdim
R["A2_ad16_kills_core"] = bool((AD[16] * Bc).is_zero_matrix)
log(f"A2 core = z(g8): dim {cdim}; ad(g16) kills it: {R['A2_ad16_kills_core']} "
    "(=> z(g8)=z(g16)=z(g8,g16))")

# A3. THE FLOOR := z(all four charges) = ker(ad g14 | core).
P = (Bc.T * Bc).inv() * Bc.T
C14 = P * AD[14] * Bc
assert (Bc * C14 - AD[14] * Bc).is_zero_matrix, "core is not ad(g14)-invariant"
fl = C14.nullspace()
Bf = Bc * sp.Matrix.hstack(*fl)
fdim = Bf.shape[1]
floor = [[Bf[i, j] for i in range(DIM)] for j in range(fdim)]
R["A3_dim_floor"] = fdim
R["A3_floor_killed_by_g22"] = bool((AD[22] * Bf).is_zero_matrix)
R["A3_floor_killed_by_g16"] = bool((AD[16] * Bf).is_zero_matrix)
_st = sp.Matrix.hstack(Bf, sp.Matrix([[sp.Rational(CH[n][i].numerator, CH[n][i].denominator)
                                       for n in NS] for i in range(DIM)]))
R["A3_charges_inside_floor"] = bool(_st.rank() == fdim)
log(f"A3 floor = z(g8,g14,g16,g22): dim {fdim}; killed by g22={R['A3_floor_killed_by_g22']}, "
    f"g16={R['A3_floor_killed_by_g16']}; charges inside: {R['A3_charges_inside_floor']}")

# A4. type the floor.
dfl = frame.derived([[sp.Rational(x) for x in v] for v in floor])
R["A4_dim_derived_floor"] = int(frame.dim_of(dfl))
R["A4_floor_centre"] = fdim - R["A4_dim_derived_floor"]
R["A4_derived_is_perfect"] = int(frame.dim_of(frame.derived(dfl))) == R["A4_dim_derived_floor"]
Ad = [frame.ad(v) for v in dfl]
Bd = sp.Matrix([[sp.Rational(x) for x in v] for v in dfl]).T
rows = []
for j in range(len(dfl)):
    rows.extend(sp.Matrix.hstack(*[Ad[a] * Bd[:, j] for a in range(len(dfl))]).tolist())
R["A4_centre_of_derived_floor"] = len(sp.Matrix(rows).nullspace())
log(f"A4 [floor,floor] dim {R['A4_dim_derived_floor']}, floor centre {R['A4_floor_centre']}, "
    f"perfect {R['A4_derived_is_perfect']}, centre of derived {R['A4_centre_of_derived_floor']}")
log("   => floor = (8-dim perfect, centre 0) + u(1)^4; the unique 8-dim simple is A2 = su(3)")

# ============================================================ STAGE B (exact Q)
log("STAGE B -- kappa, exact over Q")
Bfl = sp.Matrix.hstack(*fl)
piv = list(sp.Matrix(Bfl.T).rref()[1])
comp = [i for i in range(cdim) if i not in piv][: cdim - fdim]
Tm = sp.Matrix.hstack(Bfl, sp.eye(cdim)[:, comp])
Ti = Tm.inv()
C22 = P * AD[22] * Bc
M14 = Ti * C14 * Tm; M22 = Ti * C22 * Tm
assert M14[:, :fdim].is_zero_matrix and M22[:, :fdim].is_zero_matrix, "floor not pencil-killed"
Q14 = M14[fdim:, fdim:]; Q22 = M22[fdim:, fdim:]
qd = Q14.shape[0]
R["B_quotient_dim"] = qd
# DEGREE BOUND STRUCTURAL, NOT ASSUMED: a qd x qd matrix with entries affine in s.
s = sp.symbols('s')
def detat(x): return (Q14 + sp.Rational(x) * Q22).det()
nu = sp.expand(sp.interpolate(list(zip(range(qd + 1), [detat(x) for x in range(qd + 1)])), s))
R["B_nu_degree"] = int(sp.degree(nu, s))
R["B_nu_surplus_node_checks"] = bool(all(sp.simplify(nu.subs(s, x) - detat(x)) == 0
                                         for x in range(-6, 0)))
kap = None
for f_, m_ in sp.factor_list(sp.Poly(nu, s))[1]:
    if m_ == 6 and sp.degree(f_, s) == 3:
        kap = sp.Poly(sp.primitive(f_)[1], s)
R["B_nu_is_c_times_cubic_to_the_6"] = kap is not None
kco = [int(kap.as_expr().coeff(s, i)) for i in range(4)]
R["B_kappa_coeffs_asc"] = kco
R["B_kappa_irreducible"] = bool(kap.is_irreducible)
R["B_kappa_const_is_minus_19_cubed"] = bool(kco[0] == -19 ** 3)
_fi = sp.factorint(sp.discriminant(kap.as_expr(), s))
R["B_kappa_disc_squarefree_kernel"] = sorted(int(q) for q in _fi if _fi[q] % 2 == 1)
log(f"B quotient dim {qd}; nu degree {R['B_nu_degree']} (structural bound {qd}); "
    f"surplus checks {R['B_nu_surplus_node_checks']}; nu=c*kappa^6 "
    f"{R['B_nu_is_c_times_cubic_to_the_6']}")
log(f"  kappa = {kap.as_expr()}")
log(f"  irreducible {R['B_kappa_irreducible']}; const=-19^3 "
    f"{R['B_kappa_const_is_minus_19_cubed']}; disc squarefree kernel "
    f"{R['B_kappa_disc_squarefree_kernel']}")

# ============================================================ STAGE C (mod p)
log("STAGE C -- walls, span, M12; TWO fresh primes")

# exact Killing matrix on the Chevalley basis, from BB alone:
#   K[i][j] = tr(ad e_i . ad e_j) = sum_{q,k} BB[i][q][k] * BB[j][k][q]
SP = []
for i in range(DIM):
    ent = []
    for q in range(DIM):
        row = BB[i][q]
        for kk in range(DIM):
            if row[kk]:
                ent.append((q, kk, row[kk]))
    SP.append(ent)
K = [[0] * DIM for _ in range(DIM)]
for i in range(DIM):
    for j in range(i, DIM):
        t = 0
        for (q, kk, c) in SP[i]:
            d = BB[j][kk][q]
            if d:
                t += c * d
        K[i][j] = t; K[j][i] = t
random.seed(7)
R["C_killing_formula_matches_ad_traces"] = all(
    (frame.ad(frame._unit(i)) * frame.ad(frame._unit(j))).trace() == K[i][j]
    for i, j in [(random.randrange(DIM), random.randrange(DIM)) for _ in range(12)])
log(f"C Killing matrix from BB cross-checked vs ad-traces, 12 random pairs: "
    f"{R['C_killing_formula_matches_ad_traces']}")

denoms = {c.denominator for n in NS for c in CH[n] if c}
USED = {40009, 40013, 40037, 40039, 40063, 40123, 40639, 40829, 40883}
def split_primes(start, want):
    out = []; q = start
    while len(out) < want:
        q = int(sp.nextprime(q))
        if q in USED or any(d % q == 0 for d in denoms) or kco[3] % q == 0:
            continue
        rts = {x for x in range(q) if sum(c * pow(x, i, q) for i, c in enumerate(kco)) % q == 0}
        if len(rts) == 3:
            out.append(q)
    return out
PRIMES = split_primes(41000, 2)
log(f"C fresh split primes: {PRIMES}  (disjoint from the record's {sorted(USED)})")
R["C_primes"] = PRIMES


def stage_c(p):
    r = {}
    def rd(x):
        x = sp.Rational(x); return x.p % p * pow(x.q % p, p - 2, p) % p
    def mp(M): return [[rd(M[i, j]) for j in range(M.shape[1])] for i in range(M.shape[0])]
    def rref(rows):
        rows = [x[:] for x in rows]; n = len(rows[0]) if rows else 0; wh = {}; rk = 0
        for c in range(n):
            pv = next((i for i in range(rk, len(rows)) if rows[i][c]), None)
            if pv is None: continue
            rows[rk], rows[pv] = rows[pv], rows[rk]
            iv = pow(rows[rk][c], p - 2, p); rows[rk] = [v * iv % p for v in rows[rk]]
            for i in range(len(rows)):
                if i != rk and rows[i][c]:
                    f = rows[i][c]
                    rows[i] = [(a - f * b) % p for a, b in zip(rows[i], rows[rk])]
            wh[c] = rk; rk += 1
        return rows, wh, rk
    def rank(vs): return 0 if not vs else rref([list(x) for x in zip(*vs)])[2]
    def basis(vs): return [x[:] for x in rref(vs)[0] if any(x)]
    def null(rows):
        n = len(rows[0]) if rows else DIM
        rr, wh, _ = rref(rows)
        out = []
        for fc in [c for c in range(n) if c not in wh]:
            v = [0] * n; v[fc] = 1
            for c, rw in wh.items(): v[c] = (-rr[rw][fc]) % p
            out.append(v)
        return out
    def inter_dim(A, B):
        if not A or not B: return 0
        return len(basis(A)) + len(basis(B)) - rank(A + B)
    def inter_basis(A, B):
        """basis of span(A) ^ span(B): nullspace of [A^T | -B^T] -> A-combinations."""
        if not A or not B: return []
        na, nb = len(A), len(B)
        M = [[A[j][i] for j in range(na)] + [(-B[j][i]) % p for j in range(nb)]
             for i in range(DIM)]
        out = []
        for v in null(M):
            w = [0] * DIM
            for j in range(na):
                if v[j]:
                    w = [(w[t] + v[j] * A[j][t]) % p for t in range(DIM)]
            if any(w): out.append(w)
        return basis(out)

    ADp = {n: mp(AD[n]) for n in NS}
    Kp = [[K[i][j] % p for j in range(DIM)] for i in range(DIM)]
    r["killing_rank"] = rank([list(x) for x in zip(*Kp)])
    corep = [[rd(Bc[i, j]) for i in range(DIM)] for j in range(cdim)]
    floorp = [[rd(Bf[i, j]) for i in range(DIM)] for j in range(fdim)]
    def kperp(V):
        return null([[sum(v[i] * Kp[i][j] for i in range(DIM) if v[i]) % p
                      for j in range(DIM)] for v in V])

    r["kappa_roots"] = sorted(x for x in range(p)
                              if sum(c * pow(x, i, p) for i, c in enumerate(kco)) % p == 0)
    W = [null([[(ADp[14][i][j] + r0 * ADp[22][i][j]) % p for j in range(DIM)]
               for i in range(DIM)]) for r0 in r["kappa_roots"]]
    r["wall_dims"] = [len(w) for w in W]
    # pairwise + TRUE triple intersection (generic value would be 0 -- discriminating)
    I01 = inter_basis(W[0], W[1])
    r["pairwise_inters"] = [len(I01), inter_dim(W[0], W[2]), inter_dim(W[1], W[2])]
    r["triple_inter"] = inter_dim(I01, W[2])
    r["triple_inter_equals_floor"] = (r["triple_inter"] == fdim and
                                      rank(inter_basis(I01, W[2]) + floorp) == fdim)
    r["floor_inside_every_wall"] = all(rank(w + floorp) == len(w) for w in W)
    r["span"] = rank(W[0] + W[1] + W[2])

    # M12 := Killing-perp of the 66-span
    M12 = kperp(W[0] + W[1] + W[2])
    r["M12_dim"] = len(M12)
    r["M12_cap_core"] = inter_dim(M12, corep)
    inv_ok, ranks = [], []
    for n in NS:
        img = [[sum(ADp[n][i][kk] * v[kk] for kk in range(DIM) if v[kk]) % p
                for i in range(DIM)] for v in M12]
        inv_ok.append(rank(M12 + img) == len(M12))
        ranks.append(rank(img))
    r["M12_torus_invariant"] = all(inv_ok)
    r["M12_charge_ranks"] = ranks

    # --- CONTROLS that the "cap core = 0" routine CAN return nonzero ---
    # (a) a 66-dim span deliberately built so that its K-perp lies inside the core
    span66 = kperp(corep[:12])
    r["control_dim_span66"] = len(span66)
    r["control_perp_cap_core"] = inter_dim(kperp(span66), corep)
    # (b) [M12,M12] -- basis-reduce BEFORE any dimension formula (scout's recorded bug)
    BBp = [[[(kk, int(cv) % p) for kk, cv in enumerate(BB[a][b]) if cv]
            for b in range(DIM)] for a in range(DIM)]
    br12 = []
    for a in range(len(M12)):
        for b in range(a + 1, len(M12)):
            u, v = M12[a], M12[b]; w = [0] * DIM
            for pp in range(DIM):
                if not u[pp]: continue
                for qq in range(DIM):
                    if not v[qq]: continue
                    cc = u[pp] * v[qq] % p
                    for kk, cv in BBp[pp][qq]:
                        w[kk] = (w[kk] + cc * cv) % p
            br12.append(w)
    Bb = basis(br12)
    r["dim_bracket_M12"] = len(Bb)
    r["bracket_M12_cap_core"] = inter_dim(Bb, corep)
    r["bracket_M12_cap_M12"] = inter_dim(Bb, M12)

    # --- the mu-walls DERIVED FROM M12 ITSELF (no external cubic enters) ---
    Bm = [list(x) for x in zip(*M12)]                       # DIM x 12
    m = len(M12)
    def restrict(A):
        img = [[sum(A[i][kk] * v[kk] for kk in range(DIM) if v[kk]) % p for i in range(DIM)]
               for v in M12]
        aug = [[Bm[i][j] for j in range(m)] + [img[t][i] for t in range(m)]
               for i in range(DIM)]
        rr2, wh2, rk2 = rref(aug)
        assert rk2 == m, "ad does not preserve M12 -- restriction inconsistent"
        return [[rr2[wh2[c]][m + t] for t in range(m)] for c in range(m)]
    X8, X16 = restrict(ADp[8]), restrict(ADp[16])
    def det12(t0):
        A2 = [[(X8[i][j] + t0 * X16[i][j]) % p for j in range(m)] for i in range(m)]
        d = 1
        for c in range(m):
            pv = next((i for i in range(c, m) if A2[i][c]), None)
            if pv is None: return 0
            if pv != c: A2[c], A2[pv] = A2[pv], A2[c]; d = (-d) % p
            d = d * A2[c][c] % p; iv = pow(A2[c][c], p - 2, p)
            A2[c] = [v * iv % p for v in A2[c]]
            for i in range(c + 1, m):
                if A2[i][c]:
                    f = A2[i][c]; A2[i] = [(a - f * b) % p for a, b in zip(A2[i], A2[c])]
        return d % p
    # deg <= 12 is STRUCTURAL (12x12, entries affine in rho): 13 nodes + 6 surplus
    xs = list(range(13)); ys = [det12(x) for x in xs]
    co = [0] * 13
    for i in range(13):
        num = [1]; den = 1
        for j in range(13):
            if j == i: continue
            num = [((([0] + num)[t] if t < len(num) + 1 else 0)
                    + (-xs[j]) % p * ((num + [0])[t])) % p for t in range(len(num) + 1)]
            den = den * (xs[i] - xs[j]) % p
        di = pow(den % p, p - 2, p)
        for t in range(len(num)): co[t] = (co[t] + ys[i] * di % p * num[t]) % p
    r["det12_degree"] = max(t for t, c in enumerate(co) if c)
    r["det12_surplus_checks"] = all(
        sum(c * pow(t0 % p, t, p) for t, c in enumerate(co)) % p == det12(t0 % p)
        for t0 in range(-6, 0))
    mroots = sorted(x for x in range(p)
                    if sum(c * pow(x, t, p) for t, c in enumerate(co)) % p == 0)
    r["mu_walls_derived_from_M12"] = mroots
    lead = co[r["det12_degree"]]
    random.seed(31)
    okm = True
    for _ in range(8):
        t0 = random.randrange(p)
        lhs = sum(c * pow(t0, t, p) for t, c in enumerate(co)) % p
        rhs = lead
        for ri in mroots: rhs = rhs * pow((t0 - ri) % p, 4, p) % p
        if lhs != rhs: okm = False
    r["det12_is_c_times_cubic_to_the_4"] = okm
    r["M12_kernel_at_mu_walls"] = [
        len(null([[(X8[i][j] + ri * X16[i][j]) % p for j in range(m)] for i in range(m)]))
        for ri in mroots]
    gen = random.randrange(p)
    while gen in mroots: gen = random.randrange(p)
    r["M12_kernel_at_generic_rho"] = len(
        null([[(X8[i][j] + gen * X16[i][j]) % p for j in range(m)] for i in range(m)]))
    # CITED comparison target: solo-normalization mu, CMT_DRAFT.md:57 / table row 4
    mu_solo = [2197, -4769856, -2075673600, 500716339200]
    r["mu_solo_roots_cited"] = sorted(
        x for x in range(p)
        if sum(c * pow(x, t, p) for t, c in enumerate(mu_solo)) % p == 0)
    r["derived_walls_equal_cited_mu_roots"] = (mroots == r["mu_solo_roots_cited"])
    return r


for p in PRIMES:
    log(f"  --- p = {p} ---")
    rp = stage_c(p)
    R[f"C_p{p}"] = rp
    log(f"    Killing rank {rp['killing_rank']}; wall dims {rp['wall_dims']}; "
        f"pairwise inters {rp['pairwise_inters']}; triple {rp['triple_inter']} "
        f"(= floor: {rp['triple_inter_equals_floor']})")
    log(f"    span {rp['span']}; M12 dim {rp['M12_dim']}; M12 cap core {rp['M12_cap_core']}; "
        f"torus-inv {rp['M12_torus_invariant']}; charge ranks {rp['M12_charge_ranks']}")
    log(f"    det12 deg {rp['det12_degree']} surplus {rp['det12_surplus_checks']}; "
        f"= c*cubic^4 {rp['det12_is_c_times_cubic_to_the_4']}; kernels at mu-walls "
        f"{rp['M12_kernel_at_mu_walls']} vs generic {rp['M12_kernel_at_generic_rho']}")
    log(f"    mu-walls DERIVED from M12 == cited mu roots: "
        f"{rp['derived_walls_equal_cited_mu_roots']}")
    log(f"    CONTROLS: perp-of-perp cap core = {rp['control_perp_cap_core']} (must be > 0); "
        f"[M12,M12] dim {rp['dim_bracket_M12']}, cap core {rp['bracket_M12_cap_core']}, "
        f"cap M12 {rp['bracket_M12_cap_M12']}")

# ============================================================ VALIDATION GATE
log("VALIDATION GATE -- against banked numbers (targets CITED from CMT_DRAFT.md)")
G = []
def gate(name, got, want):
    ok = (got == want)
    G.append({"check": name, "got": got, "want": want, "pass": bool(ok)})
    log(f"  [{'PASS' if ok else 'FAIL'}] {name}: got {got}, banked {want}")
    return ok

gate("MANDATED floor dim == 12", R["A3_dim_floor"], 12)
for p in PRIMES:
    gate(f"MANDATED M12 dim == 12 (p={p})", R[f"C_p{p}"]["M12_dim"], 12)
    gate(f"MANDATED M12 cap core == 0 (p={p})", R[f"C_p{p}"]["M12_cap_core"], 0)
gate("frame Gram diagonal", R["A1_gram_diagonal"], True)
gate("frame signature (2,2)", R["A1_signature"], [2, 2])
gate("frame norms (CMT_DRAFT.md:26-31)", R["A1_gram_diag_entries"],
     ["241532928", "-317708697600", "988843239014400/13", "-889958915112960000/19"])
gate("frame abelian, 6/6 brackets", R["A0_frame_abelian_6_of_6"], True)
gate("core dim == 30", R["A2_dim_core"], 30)
gate("ad(g16) kills the core", R["A2_ad16_kills_core"], True)
gate("floor killed by g22", R["A3_floor_killed_by_g22"], True)
gate("the four charges lie in the floor", R["A3_charges_inside_floor"], True)
gate("derived(floor) dim == 8", R["A4_dim_derived_floor"], 8)
gate("floor centre == 4", R["A4_floor_centre"], 4)
gate("derived(floor) perfect", R["A4_derived_is_perfect"], True)
gate("centre of derived(floor) == 0", R["A4_centre_of_derived_floor"], 0)
gate("nu degree == 18", R["B_nu_degree"], 18)
gate("nu = c * kappa^6", R["B_nu_is_c_times_cubic_to_the_6"], True)
gate("kappa coeffs asc (CMT_DRAFT.md table row 5)", R["B_kappa_coeffs_asc"],
     [-6859, -56402640, 3033676800, 2771822592000])
gate("kappa irreducible", R["B_kappa_irreducible"], True)
gate("kappa const == -19^3", R["B_kappa_const_is_minus_19_cubed"], True)
gate("kappa disc squarefree kernel == {7,11}", R["B_kappa_disc_squarefree_kernel"], [7, 11])
for p in PRIMES:
    rp = R[f"C_p{p}"]
    gate(f"Killing rank == 78 (p={p})", rp["killing_rank"], 78)
    gate(f"wall dims [30,30,30] (p={p})", rp["wall_dims"], [30, 30, 30])
    gate(f"pairwise inters == 12 (p={p})", rp["pairwise_inters"], [12, 12, 12])
    gate(f"triple inter == the floor (p={p})", rp["triple_inter_equals_floor"], True)
    gate(f"floor inside every wall (p={p})", rp["floor_inside_every_wall"], True)
    gate(f"span == 66 (p={p})", rp["span"], 66)
    gate(f"M12 torus-invariant (p={p})", rp["M12_torus_invariant"], True)
    gate(f"M12 charge ranks [12,12,12,12] (p={p})", rp["M12_charge_ranks"], [12, 12, 12, 12])
    gate(f"det12 = c*cubic^4 (p={p})", rp["det12_is_c_times_cubic_to_the_4"], True)
    gate(f"M12 kernel 4 at each mu-wall (p={p})", rp["M12_kernel_at_mu_walls"], [4, 4, 4])
    gate(f"derived mu-walls == cited mu roots (p={p})",
         rp["derived_walls_equal_cited_mu_roots"], True)
gate("CONTROL random pair does NOT commute", R["A0_control_random_pair_commutes"], False)
gate("CONTROL random 4-Gram NOT diagonal", R["A1_control_random_gram_diagonal"], False)
for p in PRIMES:
    rp = R[f"C_p{p}"]
    gate(f"CONTROL K-perp CAN meet the core (p={p})", rp["control_perp_cap_core"] > 0, True)
    gate(f"CONTROL M12 kernel at generic rho == 0 (p={p})", rp["M12_kernel_at_generic_rho"], 0)

R["GATE"] = G
R["GATE_ALL_PASS"] = all(g["pass"] for g in G)
R["GATE_FAILURES"] = [g for g in G if not g["pass"]]
log(f"GATE: {sum(1 for g in G if g['pass'])}/{len(G)} pass; ALL PASS = {R['GATE_ALL_PASS']}")
if not R["GATE_ALL_PASS"]:
    log("!!! VALIDATION FAILED -- STOPPING. No tuning. Failures:")
    for g in R["GATE_FAILURES"]:
        log(f"    {g['check']}: got {g['got']}, banked {g['want']}")

json.dump(R, open("/Users/dri/origin-axiom/frontier/B973_L135_frame/rebuild_results.json", "w"),
          indent=1, sort_keys=True, default=str)
log("DONE")
