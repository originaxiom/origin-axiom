#!/usr/bin/env python3
"""SM-R290 (P-290, M53): C11 re-read against B1970 and B1974. Does the two-doublet dictionary fix the K datum
(C11's frame datum K_F, or B1674's coupling-weight sum K_W), so that I-31 is earned, excluded or still priced?

Card: relays/cards/SM_R290_c11-two-doublets-and-the-k-datum.md (sealed before any run on the cases).
Data-free. No measured value is read or printed.

  python3 -B run.py <main checkout> run     # the sealed run: writes r290_run.txt and r290_results.json here
  python3 -B run.py <main checkout> smoke   # toy inputs only (outside the test population); prints 'smoke ok'

Parts: A B1674's character layer (exact, mod 24); B the dictionary (main's B1253 code) and K_F's realisability by
the Standard Model gauge group (exact rationals); C frame C's Higgs triplet representation (main's B1945/B1940 frame
code, 40 digits, snapped to exact roots of unity); D B1674's characters restricted to each frame's K; E the
determinant law with a triplet Higgs (numerical consistency check). Plants P1 to P6 as in the card.
Depends on the standard library, numpy, mpmath (through main's modules) and main's own modules.
"""
import cmath
import contextlib
import io
import itertools
import json
import pathlib
import sys
from fractions import Fraction as F

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
LOG, OUT = [], {}


def say(*a):
    s = " ".join(str(x) for x in a)
    LOG.append(s)
    print(s, flush=True)


FIELDS = ["Q", "u", "d", "L", "e", "nu"]
W = {"SU3": dict(Q=2, u=1, d=1), "SU2": dict(Q=3, L=1), "grav": dict(Q=6, u=3, d=3, L=2, e=1, nu=1)}
DIM = dict(Q=6, u=3, d=3, L=2, e=1, nu=1)                         # colour x SU(2) multiplicity
SIXY = dict(Q=1, u=-4, d=2, L=-3, e=6, nu=0)                      # 6Y of the left-handed fields
COLOUR = dict(Q=1, u=-1, d=-1, L=0, e=0, nu=0)                    # +1 for a 3, -1 for a 3bar
DOUBLET = dict(Q=1, u=0, d=0, L=1, e=0, nu=0)
I31 = dict(Q=1, u=1, d=1, L=1, e=1, nu=1)
VECT = dict(Q=1, u=-1, d=-1, L=1, e=-1, nu=-1)
ASSIGN = [dict(zip(FIELDS, v)) for v in itertools.product((1, -1), repeat=6)]
key6 = lambda s: "".join("+" if s[f] > 0 else "-" for f in FIELDS)


# ---------------------------------------------------------------- A. B1674's character layer (exact)
def n_G(G, s, e=9, drop=()):
    return (e * sum(w * s[f] for f, w in W[G].items() if f not in drop)) % 24


def kw_classes(s):
    m = (-9 * (2 * s["Q"] + s["u"] + s["d"])) % 24
    return m, sorted({K % 4 for K in range(24) if (6 * K - m) % 24 == 0})


def part_A():
    rows = {}
    for s in ASSIGN:
        m, ks = kw_classes(s)
        rows[key6(s)] = dict(SU3=n_G("SU3", s), SU2=n_G("SU2", s), grav=n_G("grav", s),
                             grav_no_nu=n_G("grav", s, drop=("nu",)), m=m, KW_mod4=ks)
    su3 = [k for k, r in rows.items() if r["SU3"] == 0]
    say("A: SU(3)^2-free assignments:", len(su3), "of 64; all have s_u = s_d = -s_Q:",
        all(k[1] == k[2] != k[0] for k in su3))
    say("A: SU(2)^2 values:", sorted({r["SU2"] for r in rows.values()}))
    gf = [k for k in su3 if rows[k]["grav"] == 0]
    say("A: gravity^2-free among SU(3)^2-free:", len(gf), "; all with s_e = s_nu = -s_L:",
        all(k[4] == k[5] != k[3] for k in gf), "; any free without nu^c:",
        any(rows[k]["grav_no_nu"] == 0 for k in su3))
    for name, s in (("I-31", I31), ("vectorial", VECT)):
        say("A: %-9s" % name, rows[key6(s)])
    # plants
    p1 = dict(I31, d=-1)
    r1 = rows[key6(p1)]
    say("P1: mixed (s_Q, s_u, s_d) = (+, +, -): n_SU3 = %d (rejected: %s); K_W classes %s" % (
        r1["SU3"], r1["SU3"] != 0, r1["KW_mod4"]))
    r2 = rows[key6(VECT)]
    say("P2: vectorial without nu^c: gravity^2 exponent %d (rejected: %s)" % (r2["grav_no_nu"], r2["grav_no_nu"] != 0))
    OUT["A"] = dict(rows=rows, I31=rows[key6(I31)], vectorial=rows[key6(VECT)],
                    P1=dict(row=r1, rejected=r1["SU3"] != 0),
                    P2=dict(exp=r2["grav_no_nu"], rejected=r2["grav_no_nu"] != 0))


# ---------------------------------------------------------------- B. the dictionary, and K_F's realisability
def load_main_module(main_root, arc_glob, name):
    d = next((pathlib.Path(main_root) / "frontier").glob(arc_glob)) / "verification"
    sys.path.insert(0, str(d))
    with contextlib.redirect_stdout(io.StringIO()):
        return __import__(name)


def operator_states(Y, ten, sixteen, trip, higgs_ok):
    lab = {F(1, 6): "Q", F(-2, 3): "u", F(1, 3): "d", F(-1, 2): "L", F(1): "e", F(0): "nu"}
    ops = {}
    for t in trip:
        a = [i for i in t if i in ten]
        b = [i for i in t if i in sixteen]
        if len(a) == 1 and len(b) == 2 and a[0] in higgs_ok:
            ops.setdefault(tuple(sorted((lab[Y[b[0]]], lab[Y[b[1]]]))), set()).add(a[0])
    return ops


def two_distinct_doublets(ops):
    up, dn, le = ops.get(("Q", "u"), set()), ops.get(("Q", "d"), set()), ops.get(("L", "e"), set())
    return bool(up) and bool(dn) and bool(le) and not (up & dn)


def realised_scalars(s, charge, grid=720):
    """Phases r (zeta = e^{2 pi i r}) such that some gauge element acts by zeta^{s_f} on every field f.
    charge(f, a, b, x) gives the element's phase on f as a rational mod 1."""
    out = set()
    for a in range(3):
        for b in range(2):
            for j in range(grid):
                x = F(j, grid)
                ph = {f: charge(f, a, b, x) % 1 for f in FIELDS}
                r = (ph["Q"] * s["Q"]) % 1
                if all((ph[f] - s[f] * r) % 1 == 0 for f in FIELDS):
                    out.add(r)
    return sorted(out)


def sm_charge(f, a, b, x):
    return F(a * COLOUR[f], 3) + F(b * DOUBLET[f], 2) + x * SIXY[f]


def psi_charge(f, a, b, x):                       # U(1)_psi: charge 1 on every field of the 16 (P5)
    return x


def part_B(main_root):
    SM = load_main_module(main_root, "B1253_*", "sm_sector")
    with contextlib.redirect_stdout(io.StringIO()):
        Y, (one, ten, sixteen), wts = SM.hypercharges()
        trip = SM.cubic_triples(wts)
    tenY = sorted((str(y), c) for y, c in __import__("collections").Counter(Y[i] for i in ten).items())
    nu_in_16 = sum(1 for i in sixteen if Y[i] == 0)
    say("B: the 10's hypercharges:", tenY, "; Y = 0 states in the 16 (nu^c):", nu_in_16, "; in the 1:",
        sum(1 for i in one if Y[i] == 0))
    ops = operator_states(Y, ten, sixteen, trip, set(ten))
    opsY = {"%s %s" % k: sorted(str(Y[h]) for h in v) for k, v in ops.items() if k in
            (("Q", "u"), ("Q", "d"), ("L", "e"), ("L", "nu"))}
    say("B: operators and the Y of the 10-states they use:", opsY)
    ok2 = two_distinct_doublets(ops)
    say("B: two distinct doublets serve up and down/leptons:", ok2)
    one_dbl = {i for i in ten if Y[i] == F(1, 2)}                   # P3: only the Y = +1/2 doublet exists
    ops1 = operator_states(Y, ten, sixteen, trip, one_dbl)
    p3 = not two_distinct_doublets(ops1)
    say("P3: one-doublet dictionary (Y = +1/2 only): down/lepton operators lack a holomorphic Higgs, flagged:", p3)
    real = {}
    for name, s in (("I-31", I31), ("vectorial", VECT)):
        real[name] = [str(r) for r in realised_scalars(s, sm_charge)]
        say("B: Standard Model gauge group realises uniform scalars r (zeta = e^{2 pi i r}) on %s: %s" % (
            name, real[name]))
    psi = realised_scalars(I31, psi_charge)
    p5 = len(psi) == 720
    say("P5: U(1)_psi (charge 1 on the 16) realises %d of 720 grid phases on I-31 (all: %s)" % (len(psi), p5))
    OUT["B"] = dict(ten_Y=tenY, nu_in_16=nu_in_16, ops=opsY, two_distinct=ok2, P3_flagged=p3,
                    SM_realised=real, P5_all=p5)


# ---------------------------------------------------------------- C. the Higgs triplet's representation
Z24 = cmath.exp(2j * cmath.pi / 24)
CHI = {"t": Z24, "s": cmath.exp(-1j * cmath.pi / 4)}
A_U = np.array([[1j, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)        # theta^2 triplet under T
B_U = np.array([[0, 0, -1j], [0, -1j, 0], [-1j, 0, 0]], dtype=complex)    # under S, factor tau
RHO_T = {"t": CHI["t"] ** 21 * A_U, "s": CHI["s"] ** 21 * B_U}


def snap(M, n=8):
    roots = [0] + [cmath.exp(2j * cmath.pi * k / n) for k in range(n)]
    S = np.array([[min(roots, key=lambda r: abs(complex(z) - r)) for z in row] for row in M], dtype=complex)
    return S, float(np.max(np.abs(np.array(M, dtype=complex) - S)))


def higgs_rho(main_root):
    DL = load_main_module(main_root, "B1945_*", "determinant_law")
    mp, te = DL.mp, DL.FM.te
    mp.mp.dps = 40
    c3 = lambda t: [te.ev(cc, t) for cc in te.B[1]]
    taus = [mp.mpc(x, y) for x, y in ((0.11, 1.05), (-0.27, 0.95), (0.33, 1.6), (0.07, 2.1),
                                      (-0.41, 1.25),
                                      (0.21, 1.35))]
    def solve(gamma, factor):
        rows = [(c3(gamma(t)), [factor(t) * z for z in c3(t)]) for t in taus]
        A = mp.matrix([[r[1][j] for j in range(3)] for r in rows])
        R, res = np.zeros((3, 3), dtype=complex), 0
        for i in range(3):
            b = mp.matrix([r[0][i] for r in rows])
            x = mp.lu_solve(A.H * A, A.H * b)
            res = max(res, float(mp.norm(A * x - b) / mp.norm(b)))
            R[i] = [complex(x[j]) for j in range(3)]
        return R, res
    RT, rt = solve(lambda t: t + 1, lambda t: 1)
    RS, rs = solve(lambda t: -1 / t, lambda t: t ** mp.mpf(1.5) * mp.exp(-1j * mp.pi * 3 / 4))
    RTs, et = snap(RT)
    RSs, es = snap(RS)
    say("C: R_T, R_S solved (residuals %.1e, %.1e), snapped to eighth roots (distance %.1e, %.1e)" % (rt, rs, et, es))
    OUT.setdefault("C", {}).update(solve_residuals=[rt, rs], snap_distance=[et, es],
                                   R_T=[[str(complex(z)) for z in r] for r in RTs],
                                   R_S=[[str(complex(z)) for z in r] for r in RSs])
    return {"t": RTs, "s": cmath.exp(-3j * cmath.pi / 4) * RSs}


def relations(rho):
    s, t = rho["s"], rho["t"]
    I3 = np.eye(3)
    return dict(s2_st3=bool(np.allclose(s @ s, np.linalg.matrix_power(s @ t, 3))),
                s8=bool(np.allclose(np.linalg.matrix_power(s, 8), I3)))


def det_exponent(rho):
    es = [e for e in range(24) if abs(np.linalg.det(rho["t"]) - CHI["t"] ** e) < 1e-9
          and abs(np.linalg.det(rho["s"]) - CHI["s"] ** e) < 1e-9]
    return es


def closure(gens):
    """gens: dict name -> tuple of arrays/scalars. Returns the list of tuples generated (finite image)."""
    def k(g):
        return tuple(np.round(np.concatenate([np.ravel(np.asarray(x, dtype=complex)) for x in g]), 7).tolist())
    e = tuple(np.eye(3, dtype=complex) if np.ndim(x) else 1 + 0j for x in next(iter(gens.values())))
    seen = {k(e): e}
    front = [e]
    while front:
        nxt = []
        for g in front:
            for h in gens.values():
                x = tuple(a @ b if np.ndim(a) else a * b for a, b in zip(g, h))
                kk = k(x)
                if kk not in seen:
                    seen[kk] = x
                    nxt.append(x)
        front = nxt
        if len(seen) > 20000:
            raise RuntimeError("image too large")
    return list(seen.values())


def equivalences(rhoA, rhoB):
    """j such that rhoA = rhoB (x) chi^j, and j such that rhoA = conj(rhoB) (x) chi^j, by characters."""
    G = closure({g: (rhoA[g], rhoB[g], CHI[g]) for g in ("t", "s")})
    same = [j for j in range(24) if all(abs(np.trace(a) - c ** j * np.trace(b)) < 1e-8 for a, b, c in G)]
    conj = [j for j in range(24) if all(abs(np.trace(a) - c ** j * np.conj(np.trace(b))) < 1e-8 for a, b, c in G)]
    return len(G), same, conj


def t_exponents(M):
    return sorted(round((cmath.phase(z) / (2 * cmath.pi)) % 1 * 24) % 24 for z in np.linalg.eigvals(M))


def part_C(rho_H):
    C = OUT.setdefault("C", {})
    C.update(relations_T=relations(RHO_T), relations_H=relations(rho_H), det_exp_T=det_exponent(RHO_T),
             det_exp_H=det_exponent(rho_H), t_exp24_T=t_exponents(RHO_T["t"]), t_exp24_H=t_exponents(rho_H["t"]))
    say("C: relations rho_T %s, rho_H %s; det exponents (chi_eta^e): T %s, H %s; t-exponents x24: T %s, H %s" % (
        C["relations_T"], C["relations_H"], C["det_exp_T"], C["det_exp_H"], C["t_exp24_T"], C["t_exp24_H"]))
    n, same, conj = equivalences(rho_H, RHO_T)
    say("C: joint image of (rho_H, rho_T, chi) has %d elements; rho_H = rho_T (x) chi^j for j in %s; "
        "= conj(rho_T) (x) chi^j for j in %s" % (n, same, conj))
    n2, selfc, selfconj = equivalences(RHO_T, RHO_T)
    say("C: read-out, rho_T against itself: same %s, conjugate %s" % (selfc, selfconj))
    p4 = {g: np.conj(RHO_T[g]) for g in ("t", "s")}
    _, s4, c4 = equivalences(p4, RHO_T)
    say("P4: conj(rho_T) planted as the Higgs: conjugate list %s (j = 0 present: %s); same list %s" % (c4, 0 in c4, s4))
    C.update(joint_order=n, same=same, conj=conj, self_same=selfc, self_conj=selfconj,
             P4=dict(conj=c4, same=s4, ok=0 in c4))


# ---------------------------------------------------------------- D. characters restricted to each frame's K
def r_of(z, den=24):
    r = F(round((cmath.phase(z) / (2 * cmath.pi)) * den), den) % 1
    assert abs(z - cmath.exp(2j * cmath.pi * float(r))) < 1e-8, z
    return r


def part_D(rho_H):
    G = closure({g: (RHO_T[g], rho_H[g], CHI[g]) for g in ("t", "s")})
    Z = []
    for a, b, c in G:
        if np.allclose(a, a[0, 0] * np.eye(3), atol=1e-9):
            hs = np.allclose(b, b[0, 0] * np.eye(3), atol=1e-9)
            Z.append((r_of(a[0, 0]), r_of(b[0, 0]) if hs else None, r_of(c)))
    zetas = sorted({z[0] for z in Z})
    proj = len({tuple(np.round(a / a[0, np.argmax(np.abs(a[0]))], 6).ravel()) for a, _, _ in G})
    say("D: image of rho_T has %d elements; scalar phases r of Z: %s" % (len({tuple(np.round(a, 7).ravel())
                                                                                 for a, _, _ in G}),
                                                                          [str(z) for z in zetas]))
    restricted = {}
    for s in ASSIGN:
        ph = {}
        for Gn in ("SU3", "SU2", "grav"):
            tot = 3 * sum(w * s[f] for f, w in W[Gn].items())
            ph[Gn] = all((tot * z) % 1 == 0 for z in zetas)
        restricted[key6(s)] = ph
    say("D: F_c restricted phases trivial (SU3, SU2, grav): I-31 %s; vectorial %s" % (
        restricted[key6(I31)], restricted[key6(VECT)]))
    mixed_fail = all(not restricted[k]["SU3"] for k in restricted if not (k[1] == k[2]))
    say("D: every assignment with s_u != s_d fails the restricted SU(3)^2 phase:", mixed_fail)
    comp = sorted({(str(z), str(h), str((-2 * z) % 1) if h is not None else None) for z, h, _ in Z},
                  key=lambda t: t[0])
    say("D4 read-out: on Z, (r_T, r_H, -2 r_T):", comp)
    cubic = {key6(s): sum(s[f] * DIM[f] for f in FIELDS) for s in ASSIGN}
    free = sorted(k for k, v in cubic.items() if v == 0)
    ymix = sum(F(DIM[f]) * F(SIXY[f], 6) for f in FIELDS)
    say("D: F_S cubic SU(3)_F^3: I-31 %d, vectorial %d; free assignments (%d): %s; mixed SU(3)_F^2 U(1)_Y sum %s" % (
        cubic[key6(I31)], cubic[key6(VECT)], len(free), free, ymix))
    OUT["D"] = dict(image_T=len({tuple(np.round(a, 7).ravel()) for a, _, _ in G}), projective_classes=proj,
                    Z=[str(z) for z in zetas], restricted_I31=restricted[key6(I31)],
                    restricted_vect=restricted[key6(VECT)], mixed_fail_SU3=mixed_fail,
                    Z_higgs=comp, FS_cubic_I31=cubic[key6(I31)], FS_cubic_vect=cubic[key6(VECT)],
                    FS_free=free, FS_ymix=str(ymix))


# ---------------------------------------------------------------- E. the determinant law with a triplet Higgs
def part_E(rho_H, seed=290):
    rng = np.random.default_rng(seed)
    G = closure({g: (RHO_T[g], rho_H[g], CHI[g]) for g in ("t", "s")})
    dims, res = {}, {}
    for j in range(24):
        P = np.zeros((27, 27), dtype=complex)
        for a, b, c in G:
            P += np.kron(np.kron(a, a), b * c ** j)
        P /= len(G)
        dims[j] = int(round(np.real(np.trace(P))))
        if dims[j] and j not in res:
            Yt = (P.T @ (rng.normal(size=27) + 1j * rng.normal(size=27))).reshape(3, 3, 3)
            h = rng.normal(size=3) + 1j * rng.normal(size=3)
            Mof = lambda hh: np.einsum("ijk,k->ij", Yt, hh)
            worst = 0.0
            for a, b, c in G:
                d1 = np.linalg.det(Mof(c ** j * b @ h)) * np.linalg.det(a) ** 2
                worst = max(worst, abs(d1 - np.linalg.det(Mof(h))) / abs(np.linalg.det(Mof(h))))
            res[j] = worst
    say("E: invariant (Q, u^c, Higgs (x) chi^j) couplings, dimension by j:", {j: d for j, d in dims.items() if d})
    say("E: determinant law worst relative residual, by j with invariants:", {j: "%.1e" % v for j, v in res.items()})
    Yr = (rng.normal(size=27) + 1j * rng.normal(size=27)).reshape(3, 3, 3)
    h = rng.normal(size=3) + 1j * rng.normal(size=3)
    Mof = lambda hh: np.einsum("ijk,k->ij", Yr, hh)
    p6 = max(abs(np.linalg.det(Mof(b @ h)) * np.linalg.det(a) ** 2 - np.linalg.det(Mof(h))) / abs(np.linalg.det(Mof(h)))
             for a, b, c in G)
    say("P6: a non-covariant coupling: determinant law residual %.2e (broken: %s)" % (p6, p6 > 1e-3))
    OUT["E"] = dict(inv_dims={j: d for j, d in dims.items() if d}, law_residual=res, P6=dict(res=p6, broken=p6 > 1e-3))


# ---------------------------------------------------------------- smoke (toy inputs only)
def smoke():
    toy = {"t": np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex), "s": np.eye(3, dtype=complex)}
    assert len(closure({g: (toy[g],) for g in ("t", "s")})) == 3
    n, same, conj = equivalences(toy, toy)
    assert n >= 3 and isinstance(same, list)
    assert snap(np.array([[1.0000001, 0, 0], [0, 1j, 0], [0, 0, -1]]))[1] < 1e-5
    toy_s = dict(Q=1, u=1, d=1, L=1, e=1, nu=0)
    assert realised_scalars(toy_s, lambda f, a, b, x: x if f != "nu" else 0, grid=12)
    assert r_of(cmath.exp(2j * cmath.pi * 5 / 24)) == F(5, 24)
    print("smoke ok")


def main():
    if len(sys.argv) < 3 or sys.argv[2] not in ("run", "smoke"):
        sys.exit(__doc__)
    if sys.argv[2] == "smoke":
        smoke()
        return
    main_root = sys.argv[1]
    part_A()
    part_B(main_root)
    rho_H = higgs_rho(main_root)
    part_C(rho_H)
    part_D(rho_H)
    part_E(rho_H)
    (HERE / "r290_run.txt").write_text("\n".join(LOG) + "\n")
    (HERE / "r290_results.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")


if __name__ == "__main__":
    main()
