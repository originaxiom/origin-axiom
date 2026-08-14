#!/usr/bin/env python3
"""B911 -- independent recomputation cell for the COMPACT MEASUREMENT THEOREM draft.

Recomputes, on the banked B854 exact e6 build (exec'd, credited), the parts of the
solo ledger's compact campaign (sections LV-LVIII) that this seat can reach:

  STAGE 1  exact centralizer-lattice dims: z(g8)=z(g16)=core (30), z(g14)=z(g22)=
           floor-track (12), floor = z(torus) (12), floor c core.
  STAGE 2  the compact pencil g14 + s*g22 on core/floor (18-dim quotient):
           exact determinant nu(s) by interpolation with a PROVEN degree bound
           (18x18 matrix, entries affine in s => deg <= 18; 19 nodes + 6 check
           nodes -- the section-LIV retraction lesson, applied);
           factor nu = c * kappa^6, kappa an irreducible cubic; disc kernel;
           one-field check: kappa factors [1,2] over the banked noncompact cubic's
           field; rational rescale map to the ledger's kappa.
  STAGE 3  ledger-data-only exact checks (no build needed): mu and kappa
           irreducible, constants 13^3 / -19^3, disc squarefree kernels {7,11},
           discs non-square (S3); one-field over Q[rho]/mu; the exact s*(rho)
           root check (ledger section LVII SST).
  STAGE 4  fresh-prime mod-p replication (a split prime NOT in {40013, 40039,
           40123, 40639}): compact-wall centralizers dim 30 / derived 28 /
           center 2 / cap core 18 at all three walls; noncompact walls dim 46;
           the 3x3 pairing table (diag 30 / off-diag 18) with the matching;
           the 18-typing (derived 15, center 3); GEO (pairwise/triple cap =
           floor, span 66); the invisible-12 Killing-perp block and its
           advertised properties.
  STAGE 5  semisimple-uniqueness import enumerations (dim 28 rank<=4,
           dim 15 rank<=3, dim 45 rank<=5, dim 11).

Everything char-0 is exact (Fraction/sympy Rational); mod-p is exact arithmetic
in F_p. No floats anywhere. Output: cmt_recompute_results.json + stdout log.
"""
import json
import os
import sys
import time
from fractions import Fraction as Fr

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
B854 = os.path.normpath(os.path.join(HERE, "..", "B854_centralizer_exact",
                                     "e6_centralizer.py"))
RESULTS = {}
T0 = time.time()


def log(msg):
    print(f"[{time.time()-T0:8.1f}s] {msg}", flush=True)


def save():
    json.dump(RESULTS, open(os.path.join(HERE, "cmt_recompute_results.json"), "w"),
              indent=1, sort_keys=True, default=str)


# ============================================================ STAGE 0: the build
log("STAGE 0: exec of the banked B854 build (exact e6 + the four charges) ...")
src = open(B854, encoding="utf-8").read()
g = {"__file__": os.path.join(HERE, "b854_rerun.py"), "__name__": "b854"}
exec(compile(src, B854, "exec"), g)
DIM, N = g["DIM"], g["N"]
ROOTS, BB, INV = g["ROOTS"], g["BB"], g["INV"]
br, hvec, evec = g["br"], g["hvec"], g["evec"]
C_cartan = g["C"]
# b854's own results.json regenerates into HERE; rename to keep provenance clear
if os.path.exists(os.path.join(HERE, "results.json")):
    os.replace(os.path.join(HERE, "results.json"),
               os.path.join(HERE, "b854_rerun_results.json"))
banked = json.load(open(os.path.join(
    os.path.dirname(B854), "results.json")))
rerun = json.load(open(os.path.join(HERE, "b854_rerun_results.json")))
RESULTS["stage0_build_reproduces_banked_results"] = (banked == rerun)
log(f"  b854 rerun results == banked results.json : {banked == rerun}")

# sparse triple table: BB[p][q] has coefficient c at slot r
triples = {}
for p in range(DIM):
    for q in range(DIM):
        for r, c in enumerate(BB[p][q]):
            if c:
                triples.setdefault(p, []).append((q, r, int(c)))

CH = {n: INV[n] for n in (8, 14, 16, 22)}   # Fractions, length 78


def admat_rat(vec):
    """ad(vec) as a sympy Rational DIMxDIM matrix (columns = [vec, b_q])."""
    A = sp.zeros(DIM, DIM)
    for p, vp in enumerate(vec):
        if not vp:
            continue
        vps = sp.Rational(vp.numerator, vp.denominator)
        for q, r, c in triples.get(p, []):
            A[r, q] += vps * c
    return A


log("  building the four exact ad matrices ...")
AD = {n: admat_rat(CH[n]) for n in (8, 14, 16, 22)}
save()

# ============================================================ STAGE 1: lattice dims
log("STAGE 1: exact centralizer-lattice dimensions ...")
ns8 = AD[8].nullspace()
dim_z8 = len(ns8)
Bc = sp.Matrix.hstack(*ns8)                       # 78 x dim_z8, candidate core
z16_kills_core = (AD[16] * Bc).is_zero_matrix     # z(g8) subset z(g16)?
log(f"  dim z(g8) = {dim_z8}   ad16 * basis(z(g8)) == 0 : {z16_kills_core}")
ns16 = AD[16].nullspace()
dim_z16 = len(ns16)
log(f"  dim z(g16) = {dim_z16}")
# core = z(g8) cap z(g16); if ad16 kills z(g8) and dims agree, core = z(g8) = z(g16)
core_dim = dim_z8 if z16_kills_core and dim_z16 == dim_z8 else None
rank14 = AD[14].rank()
rank22 = AD[22].rank()
log(f"  dim z(g14) = {DIM - rank14}   dim z(g22) = {DIM - rank22}")
# floor = z(torus): kernel of ad14 restricted to core (all four then annihilate)
P = (Bc.T * Bc).inv() * Bc.T                      # exact left inverse of Bc
C14 = P * AD[14] * Bc
C22 = P * AD[22] * Bc
assert (Bc * C14 - AD[14] * Bc).is_zero_matrix, "core not ad14-invariant"
assert (Bc * C22 - AD[22] * Bc).is_zero_matrix, "core not ad22-invariant"
fl = C14.nullspace()                              # floor in core coordinates
Fc = sp.Matrix.hstack(*fl)                        # 30 x 12 expected
floor_dim = Fc.shape[1]
c22_kills_floor = (C22 * Fc).is_zero_matrix
Bf = Bc * Fc                                      # floor in e6 coordinates
zg14_eq_floor = (DIM - rank14 == floor_dim)
log(f"  floor = ker(ad14|core): dim {floor_dim}; ad22 kills it: {c22_kills_floor};"
    f" z(g14) dim == floor dim: {zg14_eq_floor}")
RESULTS["stage1_lattice"] = dict(
    dim_z_g8=dim_z8, dim_z_g16=dim_z16, core_dim=core_dim,
    dim_z_g14=DIM - rank14, dim_z_g22=DIM - rank22,
    floor_dim=floor_dim, ad22_kills_floor=c22_kills_floor,
    z_g14_equals_floor_dim=zg14_eq_floor)
save()

# ============================================================ STAGE 2: the pencil
log("STAGE 2: exact compact-pencil determinant on core/floor ...")
# complement coordinates: pivot rows of Fc give floor-coords; complement = rest
_, FcT_piv = Fc.T.rref()
piv_rows = set(FcT_piv)
comp = [i for i in range(core_dim) if i not in piv_rows][: core_dim - floor_dim]
Ecols = sp.Matrix(core_dim, len(comp),
                  lambda i, j: 1 if i == comp[j] else 0)
T = sp.Matrix.hstack(Fc, Ecols)
assert T.rank() == core_dim, "complement choice failed"
Tinv = T.inv()
M14 = Tinv * C14 * T
M22 = Tinv * C22 * T
# floor invariance in the new basis: first floor_dim columns must vanish for
# the pencil (ad14 and ad22 both kill floor)
assert M14[:, :floor_dim].is_zero_matrix and M22[:, :floor_dim].is_zero_matrix
Q14 = M14[floor_dim:, floor_dim:]
Q22 = M22[floor_dim:, floor_dim:]
qdim = Q14.shape[0]
log(f"  quotient dim = {qdim} (expect 18); degree bound deg nu <= {qdim} PROVEN"
    f" (det of {qdim}x{qdim}, entries affine in s)")
s = sp.symbols('s')
nodes = list(range(qdim + 1))            # 19 nodes: enough for deg <= 18
vals = []
for s0 in nodes:
    vals.append((Q14 + s0 * Q22).det())
nu_poly = sp.Poly(sp.interpolate(list(zip(nodes, vals)), s), s)
extra_ok = all(nu_poly.eval(s0) == (Q14 + s0 * Q22).det()
               for s0 in range(-6, 0))
log(f"  nu interpolated: degree {nu_poly.degree()}; 6 extra-node checks: {extra_ok}")
fac = sp.factor_list(nu_poly.as_expr())
log(f"  factorization: {fac}")
# expect one cubic to the 6th power
kappa_mine = None
for base, mult in fac[1]:
    pb = sp.Poly(base, s)
    if pb.degree() == 3 and mult == 6:
        kappa_mine = pb
if kappa_mine is None:
    log("  !! nu is NOT c * cubic^6 -- record and continue")
else:
    kint = sp.Poly(sp.primitive(kappa_mine.as_expr())[1], s)
    disc_k = sp.discriminant(kint.as_expr(), s)
    kern = sp.factorint(sp.Integer(disc_k))
    kernel = sorted(p_ for p_, e_ in kern.items() if e_ % 2 == 1 and p_ > 0)
    fl_k = sp.factor_list(kint.as_expr())[1]
    irr = (len(fl_k) == 1 and fl_k[0][1] == 1
           and sp.Poly(fl_k[0][0], s).degree() == 3)
    log(f"  kappa (this build, primitive) = {kint.as_expr()}")
    log(f"  irreducible cubic: {irr}")
    log(f"  disc = {disc_k}; squarefree kernel primes = {kernel}"
        f"  (expect [7, 11] -> Q(sqrt 77)); disc square? {sp.sqrt(disc_k).is_integer}")
    RESULTS["stage2_pencil"] = dict(
        quotient_dim=qdim, nu_degree=int(nu_poly.degree()),
        extra_node_checks=bool(extra_ok),
        nu_is_c_times_cubic_pow6=kappa_mine is not None,
        kappa_this_build=str(kint.as_expr()),
        kappa_irreducible=bool(irr),
        disc=str(disc_k), disc_squarefree_kernel=[int(x) for x in kernel],
        disc_is_square=bool(sp.sqrt(disc_k).is_integer))
save()

# banked noncompact cubic (B880 normalization, on this same build)
CUBIC = sp.Poly([500716339200, -159667200, -28224, 1], sp.symbols('t'))
# ledger polynomials (solo normalization)
rho = sp.symbols('rho')
mu_ledger = sp.Poly(500716339200 * rho**3 - 2075673600 * rho**2
                    - 4769856 * rho + 2197, rho)
kappa_ledger = sp.Poly(2771822592000 * s**3 + 3033676800 * s**2
                       - 56402640 * s - 6859, s)

if kappa_mine is not None:
    log("  one-field check: factoring kappa_mine over Q[t]/CUBIC (banked field) ...")
    try:
        alpha = sp.RootOf(CUBIC.as_expr(), 0)
        fl_ext = sp.factor_list(kint.as_expr(), extension=alpha)
        degs = sorted(sp.Poly(b, s).degree() for b, m in fl_ext[1])
        log(f"    factor degrees over the noncompact cubic field: {degs}"
            f" (expect [1, 2])")
        RESULTS["stage2_pencil"]["one_field_factor_degrees_this_build"] = \
            [int(d) for d in degs]
    except Exception as exc:  # record honestly; the rescale route still decides
        log(f"    extension factoring failed ({exc!r}) -- relying on the"
            f" rescale-proportionality route below")
        RESULTS["stage2_pencil"]["one_field_factor_degrees_this_build"] = \
            f"FAILED: {exc!r}"
    # rescale map to the ledger kappa: kappa_ledger(s) ~ kappa_mine(lam * s)?
    a3, a2, a1, a0 = [kint.as_expr().coeff(s, k) for k in (3, 2, 1, 0)]
    b3, b2, b1, b0 = [kappa_ledger.as_expr().coeff(s, k) for k in (3, 2, 1, 0)]
    # kappa_mine(lam s) = a3 lam^3 s^3 + a2 lam^2 s^2 + a1 lam s + a0
    # proportional to ledger: (a2 lam^2)/(a3 lam^3) = b2/b3  => lam = (a2 b3)/(a3 b2)
    lam = sp.Rational(a2 * b3, a3 * b2)
    scaled = sp.Poly(kint.as_expr().subs(s, lam * s), s)
    # proportionality check
    ratios = {scaled.as_expr().coeff(s, k) / kappa_ledger.as_expr().coeff(s, k)
              for k in (3, 2, 1, 0)}
    prop = len(ratios) == 1
    log(f"    rescale lambda = {lam}; kappa_mine(lam s) proportional to"
        f" kappa_ledger: {prop}")
    RESULTS["stage2_pencil"]["rescale_lambda_to_ledger"] = str(lam)
    RESULTS["stage2_pencil"]["proportional_to_ledger_after_rescale"] = bool(prop)
    save()

# ============================================================ STAGE 3: ledger-only
log("STAGE 3: ledger-data-only exact checks ...")
res3 = {}
res3["mu_irreducible"] = len(sp.factor_list(mu_ledger.as_expr())[1]) == 1
res3["mu_constant_is_13cubed"] = (mu_ledger.as_expr().coeff(rho, 0) == 13**3)
dmu = sp.discriminant(mu_ledger.as_expr(), rho)
kmu = sorted(p_ for p_, e_ in sp.factorint(sp.Integer(dmu)).items()
             if e_ % 2 == 1 and p_ > 0)
res3["mu_disc"] = str(dmu)
res3["mu_disc_squarefree_kernel"] = [int(x) for x in kmu]
res3["mu_disc_is_square"] = bool(sp.sqrt(dmu).is_integer)
res3["kappa_irreducible"] = len(sp.factor_list(kappa_ledger.as_expr())[1]) == 1
res3["kappa_constant_is_minus_19cubed"] = (
    kappa_ledger.as_expr().coeff(s, 0) == -(19**3))
dka = sp.discriminant(kappa_ledger.as_expr(), s)
kka = sorted(p_ for p_, e_ in sp.factorint(sp.Integer(dka)).items()
             if e_ % 2 == 1 and p_ > 0)
res3["kappa_disc"] = str(dka)
res3["kappa_disc_squarefree_kernel"] = [int(x) for x in kka]
res3["kappa_disc_is_square"] = bool(sp.sqrt(dka).is_integer)
log(f"  mu: irred {res3['mu_irreducible']}, const 13^3 "
    f"{res3['mu_constant_is_13cubed']}, disc kernel {kmu}, square "
    f"{res3['mu_disc_is_square']}")
log(f"  kappa: irred {res3['kappa_irreducible']}, const -19^3 "
    f"{res3['kappa_constant_is_minus_19cubed']}, disc kernel {kka}, square "
    f"{res3['kappa_disc_is_square']}")
# banked-vs-solo mu normalization: mu_solo(rho) == 13^3 * CUBIC(rho/13)
t_ = sp.symbols('t')
lhs = sp.expand(13**3 * CUBIC.as_expr().subs(t_, rho / 13))
res3["mu_solo_equals_13cubed_CUBIC_rho_over_13"] = sp.expand(
    mu_ledger.as_expr() - lhs) == 0
log(f"  mu_solo(rho) == 13^3 * banked_CUBIC(rho/13): "
    f"{res3['mu_solo_equals_13cubed_CUBIC_rho_over_13']}")
# one-field on ledger polynomials (belt; the SST identity below is the proof)
try:
    rt = sp.RootOf(mu_ledger.as_expr(), 0)
    fl_led = sp.factor_list(kappa_ledger.as_expr(), extension=rt)
    degs_led = sorted(sp.Poly(b, s).degree() for b, m in fl_led[1])
    res3["one_field_factor_degrees_ledger"] = [int(d) for d in degs_led]
    log(f"  kappa_ledger factor degrees over Q[rho]/mu: {degs_led}"
        f" (expect [1, 2])")
except Exception as exc:
    res3["one_field_factor_degrees_ledger"] = f"FAILED: {exc!r}"
    log(f"  extension factoring failed ({exc!r}); SST identity below still"
        f" proves the [1,2] split (root in the field + irreducibility over Q)")
# SST: exact wall bijection s*(rho) is a root of kappa_ledger in the field
sstar = (sp.Rational(-4997, 1257360)
         - sp.Rational(198911, 68107) * rho
         + sp.Rational(560387520, 885391) * rho**2)
val = sp.rem(sp.expand(kappa_ledger.as_expr().subs(s, sstar)),
             mu_ledger.as_expr(), rho)
res3["sst_kappa_of_sstar_rho_is_zero_mod_mu"] = (sp.simplify(val) == 0)
log(f"  kappa_ledger(s*(rho)) mod mu == 0 : "
    f"{res3['sst_kappa_of_sstar_rho_is_zero_mod_mu']}")
RESULTS["stage3_ledger_exact"] = res3
save()

# ============================================================ STAGE 4: fresh prime
log("STAGE 4: fresh-prime mod-p replication ...")

# ---- tiny GF(p) kit -------------------------------------------------------


def redp(x, p):
    if isinstance(x, Fr):
        return x.numerator % p * pow(x.denominator % p, p - 2, p) % p
    xr = sp.Rational(x)
    return int(xr.p) % p * pow(int(xr.q) % p, p - 2, p) % p


def mat_redp(M, p):
    return [[redp(M[i, j], p) for j in range(M.shape[1])]
            for i in range(M.shape[0])]


def rankp(rows, p):
    rows = [r[:] for r in rows]
    m = len(rows)
    n = len(rows[0]) if m else 0
    rank = 0
    col = 0
    for col in range(n):
        piv = None
        for i in range(rank, m):
            if rows[i][col] % p:
                piv = i
                break
        if piv is None:
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        inv = pow(rows[rank][col], p - 2, p)
        rows[rank] = [x * inv % p for x in rows[rank]]
        for i in range(m):
            if i != rank and rows[i][col]:
                f = rows[i][col]
                rows[i] = [(a - f * b) % p for a, b in zip(rows[i], rows[rank])]
        rank += 1
        if rank == m:
            break
    return rank


def nullspacep(rows, p):
    """Kernel basis (as column vectors) of the matrix given by rows over F_p."""
    m = len(rows)
    n = len(rows[0]) if m else 0
    R = [r[:] for r in rows]
    pivots = []
    rank = 0
    for col in range(n):
        piv = None
        for i in range(rank, m):
            if R[i][col] % p:
                piv = i
                break
        if piv is None:
            continue
        R[rank], R[piv] = R[piv], R[rank]
        inv = pow(R[rank][col], p - 2, p)
        R[rank] = [x * inv % p for x in R[rank]]
        for i in range(m):
            if i != rank and R[i][col]:
                f = R[i][col]
                R[i] = [(a - f * b) % p for a, b in zip(R[i], R[rank])]
        pivots.append(col)
        rank += 1
    free = [c for c in range(n) if c not in pivots]
    basis = []
    for fc in free:
        v = [0] * n
        v[fc] = 1
        for r_i, pc in enumerate(pivots):
            v[pc] = (-R[r_i][fc]) % p
        basis.append(v)
    return basis


def polyrootsp(coeffs, p):
    """Roots in F_p of a polynomial given by int coeff list (low..high)."""
    return [x for x in range(p)
            if sum(c * pow(x, k, p) for k, c in enumerate(coeffs)) % p == 0]


# ---- pick the prime -------------------------------------------------------
used = {40009, 40013, 40037, 40039, 40123, 40639}
denoms = set()
for n_ in (8, 14, 16, 22):
    for c in CH[n_]:
        if c:
            denoms.add(c.denominator)
kint_c = [int(kint.as_expr().coeff(s, k)) for k in (0, 1, 2, 3)]
cubic_c = [int(CUBIC.as_expr().coeff(t_, k)) for k in (0, 1, 2, 3)]
found = None
q_ = sp.nextprime(40639)
while found is None:
    q_ = int(sp.nextprime(q_))
    if q_ in used:
        continue
    if any(d % q_ == 0 for d in denoms):
        continue
    if int(dka) % q_ == 0 or int(dmu) % q_ == 0:
        continue
    if kint_c[3] % q_ == 0 or cubic_c[3] % q_ == 0:
        continue
    rk = polyrootsp(kint_c, q_)
    rc = polyrootsp(cubic_c, q_)
    if len(set(rk)) == 3 and len(set(rc)) == 3:
        found = q_
p = found
log(f"  fresh split prime p = {p} (splits both cubics; not in {sorted(used)})")
res4 = {"prime": p}

AD8p = mat_redp(AD[8], p)
AD14p = mat_redp(AD[14], p)
AD16p = mat_redp(AD[16], p)
AD22p = mat_redp(AD[22], p)
corep = [[redp(Bc[i, j], p) for j in range(Bc.shape[1])] for i in range(DIM)]
floorp = [[redp(Bf[i, j], p) for j in range(Bf.shape[1])] for i in range(DIM)]
core_cols = [[corep[i][j] for i in range(DIM)] for j in range(Bc.shape[1])]
floor_cols = [[floorp[i][j] for i in range(DIM)] for j in range(Bf.shape[1])]

CHp = {n_: [redp(c, p) for c in CH[n_]] for n_ in (8, 14, 16, 22)}


def brp(u, v):
    out = [0] * DIM
    for pi, up in enumerate(u):
        if not up:
            continue
        for q, r, c in triples.get(pi, []):
            vq = v[q]
            if vq:
                out[r] = (out[r] + up * vq * c) % p
    return out


def addmat(A, B, t0):
    return [[(A[i][j] + t0 * B[i][j]) % p for j in range(DIM)]
            for i in range(DIM)]


def colspace_rank(cols):
    return rankp([list(r) for r in zip(*[c for c in cols])], p) if cols else 0


def stack_cols_rank(*groups):
    cols = []
    for gcols in groups:
        cols.extend(gcols)
    return rankp([list(r) for r in zip(*cols)], p)


def inter_dim(colsU, colsV):
    return len(colsU) + len(colsV) - stack_cols_rank(colsU, colsV)


def inter_basis(colsU, colsV):
    """Basis (columns) of span(U) cap span(V) over F_p."""
    nU, nV = len(colsU), len(colsV)
    rows = []
    for i in range(DIM):
        rows.append([colsU[j][i] for j in range(nU)]
                    + [(-colsV[j][i]) % p for j in range(nV)])
    ker = nullspacep(rows, p)
    out = []
    for kv in ker:
        vec = [0] * DIM
        for j in range(nU):
            if kv[j]:
                for i in range(DIM):
                    vec[i] = (vec[i] + kv[j] * colsU[j][i]) % p
        out.append(vec)
    # independent subset
    if not out:
        return []
    rows2 = [v[:] for v in out]
    # reduce to independent set via elimination bookkeeping
    keep = []
    acc = []
    for v in out:
        if rankp(acc + [v], p) > len(keep):
            keep.append(v)
            acc.append(v)
    return keep


def derived_center(cols):
    """(derived dim, center dim) of the subalgebra spanned by cols (mod p)."""
    k = len(cols)
    bracks = []
    for i in range(k):
        for j in range(i + 1, k):
            bracks.append(brp(cols[i], cols[j]))
    dd = rankp(bracks, p) if bracks else 0
    rows = []
    for j in range(k):          # constraints: sum_a x_a [w_a, w_j] = 0
        cols_ij = [brp(cols[a], cols[j]) for a in range(k)]
        for i in range(DIM):
            row = [cols_ij[a][i] for a in range(k)]
            if any(row):
                rows.append(row)
    cd = len(nullspacep(rows, p)) if rows else k
    return dd, cd


# ---- compact walls --------------------------------------------------------
s_roots = sorted(set(polyrootsp(kint_c, p)))
t_roots = sorted(set(polyrootsp(cubic_c, p)))
log(f"  kappa_mine roots mod p: {s_roots}; banked noncompact cubic roots: {t_roots}")
W = []
wall_data = []
for sr in s_roots:
    Ap = addmat(AD14p, AD22p, sr)
    ker = nullspacep(Ap, p)
    dz = len(ker)
    dd, cd = derived_center(ker)
    capc = inter_dim(ker, core_cols)
    capf = inter_dim(ker, floor_cols)
    wall_data.append(dict(s=sr, dim=dz, derived=dd, center=cd,
                          cap_core=capc, cap_floor=capf))
    W.append(ker)
    log(f"    compact wall s={sr}: dim z = {dz} (30), derived = {dd} (28), "
        f"center = {cd} (2), cap core = {capc} (18), cap floor = {capf} (12)")
res4["compact_walls"] = wall_data

# generic pencil point control
import random as _rnd
_rnd.seed(7)
while True:
    sg = _rnd.randrange(p)
    if sg not in s_roots:
        break
ker_g = nullspacep(addmat(AD14p, AD22p, sg), p)
log(f"    generic compact-pencil point s={sg}: dim z = {len(ker_g)} (expect 12)")
res4["compact_generic_dim"] = len(ker_g)

# ---- noncompact walls -----------------------------------------------------
Z = []
nc_data = []
for tr in t_roots:
    Ap = addmat(AD8p, AD16p, tr)
    ker = nullspacep(Ap, p)
    Z.append(ker)
    nc_data.append(dict(t=tr, dim=len(ker)))
    log(f"    noncompact wall t={tr}: dim z = {len(ker)} (46)")
while True:
    tg = _rnd.randrange(p)
    if tg not in t_roots:
        break
ker_gnc = nullspacep(addmat(AD8p, AD16p, tg), p)
log(f"    generic noncompact point t={tg}: dim z = {len(ker_gnc)} (expect 30)")
res4["noncompact_walls"] = nc_data
res4["noncompact_generic_dim"] = len(ker_gnc)

# ---- the 3x3 pairing table ------------------------------------------------
table = [[inter_dim(Z[i], W[j]) for j in range(3)] for i in range(3)]
log(f"  pairing table dim(z_nc_i cap z_c_j) = {table} (expect one 30 per row/col,"
    f" 18 elsewhere)")
res4["pairing_table"] = table
matching = []
for i in range(3):
    hits = [j for j in range(3) if table[i][j] == 30]
    matching.append(hits)
perm_ok = (sorted(sum(matching, [])) == [0, 1, 2]
           and all(len(h) == 1 for h in matching))
res4["pairing_is_perfect_matching"] = perm_ok
log(f"  matched pairs (i -> j): {matching}; perfect matching: {perm_ok}")
# nesting: matched implies W_j subset Z_i (dims 30 = 30)
# the 18: type an off-diagonal intersection
off = None
for i in range(3):
    for j in range(3):
        if table[i][j] == 18:
            off = (i, j)
            break
    if off:
        break
ib = inter_basis(Z[off[0]], W[off[1]])
dd18, cd18 = derived_center(ib)
log(f"  off-diagonal 18 at (i,j)={off}: dim {len(ib)}, derived = {dd18} (15), "
    f"center = {cd18} (3)")
res4["cross_shadow_18"] = dict(pair=list(off), dim=len(ib),
                               derived=dd18, center=cd18)
# core-shadow identity: 18-space == z(compact wall) cap core?
shadow = inter_basis(W[off[1]], core_cols)
same = (len(shadow) == len(ib)
        and stack_cols_rank(shadow, ib) == len(ib))
log(f"  core-shadow identity: (z_nc_i cap z_c_j) == (z_c_j cap core): {same}")
res4["core_shadow_identity"] = same
save()

# ---- GEO: pairwise/triple, span, invisible 12 -----------------------------
geo = {}
pair_caps = []
for i in range(3):
    for j in range(i + 1, 3):
        d = inter_dim(W[i], W[j])
        ibij = inter_basis(W[i], W[j])
        eqf = (d == len(floor_cols)
               and stack_cols_rank(ibij, floor_cols) == len(floor_cols))
        pair_caps.append(dict(pair=[i, j], dim=d, equals_floor=eqf))
        log(f"  compact walls cap({i},{j}): dim {d} (12), == floor: {eqf}")
span_dim = stack_cols_rank(W[0], W[1], W[2])
log(f"  triple span dim = {span_dim} (66); invisible complement = {DIM - span_dim}")
geo["pairwise"] = pair_caps
geo["triple_span"] = span_dim
res4["geo"] = geo

# Killing form (exact integers on the Chevalley basis), then mod p
log("  building the exact Killing Gram on the Chevalley basis ...")
K = [[0] * DIM for _ in range(DIM)]
for i in range(N):
    for j in range(N):
        K[i][j] = sum((sum(r[k] * C_cartan[i][k] for k in range(N)))
                      * (sum(r[k] * C_cartan[j][k] for k in range(N)))
                      for r in ROOTS)
for ri, r in enumerate(ROOTS):
    mr = tuple(-x for x in r)
    mi = ROOTS.index(mr)
    # tr(ad e_r ad e_mr) computed sparsely
    tr = Fr(0)
    for k in range(DIM):
        w = BB[N + mi][k]
        # u = [e_r, w]
        acc = Fr(0)
        for pdx, wp in enumerate(w):
            if wp:
                acc += wp * BB[N + ri][pdx][k]
        tr += acc
    assert tr.denominator == 1
    K[N + ri][N + mi] = int(tr)
Kp = [[K[i][j] % p for j in range(DIM)] for i in range(DIM)]
log(f"  Killing rank mod p = {rankp(Kp, p)} (must be 78)")
# M12 = Killing-perp of span(W1,W2,W3)
span_cols = W[0] + W[1] + W[2]
rows = []
for cvec in span_cols:
    row = [sum(cvec[i] * Kp[i][j] for i in range(DIM)) % p for j in range(DIM)]
    rows.append(row)
M12 = nullspacep(rows, p)
log(f"  invisible block M12 = Killing-perp of the compact span: dim {len(M12)} (12)")
i12 = {"dim": len(M12)}
i12["cap_core"] = inter_dim(M12, core_cols)
log(f"    M12 cap core = {i12['cap_core']} (0)")
inv_ok, fr_ok = [], []
for nm, A in (("g8", AD8p), ("g14", AD14p), ("g16", AD16p), ("g22", AD22p)):
    img = [[sum(A[i][k] * v[k] for k in range(DIM)) % p for i in range(DIM)]
           for v in M12]
    definv = stack_cols_rank(M12, img) == len(M12)
    frk = rankp(img, p)
    inv_ok.append(definv)
    fr_ok.append(frk)
    log(f"    [{nm}, M12] subset M12: {definv};  rank({nm}|M12) = {frk}")
i12["torus_invariant"] = all(inv_ok)
i12["charge_ranks_on_M12"] = fr_ok
# ker((A8 + t A16)|M12) = 4 at a noncompact wall
t1 = t_roots[0]
Ap = addmat(AD8p, AD16p, t1)
img = [[sum(Ap[i][k] * v[k] for k in range(DIM)) % p for i in range(DIM)]
       for v in M12]
kdim = len(M12) - rankp(img, p)
log(f"    ker((ad8 + t*ad16)|M12) at wall t={t1}: {kdim} (4)")
i12["pencil_kernel_on_M12_at_wall"] = kdim
res4["invisible_12"] = i12
RESULTS["stage4_fresh_prime"] = res4
save()

# ============================================================ STAGE 5: imports
log("STAGE 5: semisimple-uniqueness enumerations (char 0, exhaustive) ...")
simples = []
for n_ in range(1, 7):
    simples.append((f"A{n_}", n_, n_ * (n_ + 2)))
for n_ in range(2, 7):
    simples.append((f"B{n_}", n_, n_ * (2 * n_ + 1)))
for n_ in range(3, 7):
    simples.append((f"C{n_}", n_, n_ * (2 * n_ + 1)))
for n_ in range(4, 7):
    simples.append((f"D{n_}", n_, n_ * (2 * n_ - 1)))
simples += [("G2", 2, 14), ("F4", 4, 52), ("E6", 6, 78)]


def semis(target_dim, max_rank):
    out = []

    def rec(i, dim_left, rank_left, acc):
        if dim_left == 0:
            out.append(sorted(acc))
            return
        if i >= len(simples) or dim_left < 3:
            return
        name, r, d = simples[i]
        rec(i + 1, dim_left, rank_left, acc)
        if d <= dim_left and r <= rank_left:
            rec(i, dim_left - d, rank_left - r, acc + [name])
    rec(0, target_dim, max_rank, [])
    return sorted(set(tuple(x) for x in out))


enum = {
    "dim28_rank_le4": [list(x) for x in semis(28, 4)],
    "dim15_rank_le3": [list(x) for x in semis(15, 3)],
    "dim45_rank_le5": [list(x) for x in semis(45, 5)],
    "dim11_rank_le6": [list(x) for x in semis(11, 6)],
}
for k_, v_ in enum.items():
    log(f"  {k_}: {v_}")
RESULTS["stage5_enumerations"] = enum

# bookkeeping identities
RESULTS["stage6_bookkeeping"] = dict(
    chain_dims=[12, 18, 30, 46, 78],
    semisimple_plus_abelian=[(8, 4), (15, 3), (28, 2), (45, 1), (78, 0)],
    sums_ok=all(a + b == c for (a, b), c in
                zip([(8, 4), (15, 3), (28, 2), (45, 1), (78, 0)],
                    [12, 18, 30, 46, 78])),
    inclusion_exclusion_3x30_minus_3x12_plus_12=3 * 30 - 3 * 12 + 12,
    invisible=78 - 66, corank_bookkeeping_3x6=18)
save()
log("DONE.")
