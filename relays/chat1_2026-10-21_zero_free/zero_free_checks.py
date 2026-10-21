#!/usr/bin/env python3
"""chat1, 2026-10-21 -- the zero-free layer: the strong angle's census read as "where a quark is massless", and the
end's dressing.  The rule is ZERO_FREE_RULE.md, committed and pushed before this script (48e2105f4).  One run; its
output (zero_free_checks.json, zero_free_checks_run.txt) is committed before it is read.

The SM seat's code is imported unchanged: the_strong_angle.py (W113) and the_tuned_fit.py (W114), read from
docs/dossiers/the_weave_2026-10-07/ at c9f001d9d into a temporary directory, their sha256 checked before import.
Every cell value is computed with mpmath at 50 digits.  Pre-run: this script was only compiled (py_compile); no part
of it was run before the run.

Cells (the rule's): Z0 the control; Z1 impossible = massless at i; Z2 a generic tuned member's massless point on a CP
locus; Z3 tuned members zero-free; Z4 the end's dressing; read-outs R1 (psi on F) and R2 (the leptons' feasibility).
"""
import hashlib
import json
import subprocess
import sys
import tempfile
import time
from fractions import Fraction
from pathlib import Path

import numpy as np
import mpmath as mp

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
COMMIT = "c9f001d9ded23c059fae7d4475c98231404fec45"
SRC = "docs/dossiers/the_weave_2026-10-07/"
PINS = {"the_strong_angle.py": "a9c4b15b82739289b4698a388da117d4c517380826fcacfc16c6065221028622",
        "the_tuned_fit.py": "21f979beccd96c5470109d91579eff17af289c6951ed7485822a84e2149c713b",
        "the_strong_angle.json": None}
T0 = time.time()
OUT = {"rule": "ZERO_FREE_RULE.md (48e2105f4)", "script": "zero_free_checks.py", "sm_commit": COMMIT}


def log(*a):
    print(f"[{time.time() - T0:8.1f}s]", *a, flush=True)


# ------------------------------------------------------------------------------------------- the seat's code, pinned
TMP = Path(tempfile.mkdtemp(prefix="zf_sm_"))
for name, pin in PINS.items():
    blob = subprocess.check_output(["git", "-C", str(REPO), "show", f"{COMMIT}:{SRC}{name}"])
    h = hashlib.sha256(blob).hexdigest()
    if pin is not None and h != pin:
        raise SystemExit(f"hash mismatch for {name}: {h}")
    (TMP / name).write_bytes(blob)
    OUT.setdefault("sha256", {})[name] = h
sys.path.insert(0, str(TMP))
import the_strong_angle as SA  # noqa: E402
import the_tuned_fit as TF  # noqa: E402

mp.mp.dps = 50
RNG = np.random.default_rng(20261021)
I = mp.mpc(0, 1)
OMEGA = mp.mpc(-0.5, mp.sqrt(3) / 2)
GEN = [mp.mpc(t.real, t.imag) for t in SA.GENERIC5]
W113 = json.loads((TMP / "the_strong_angle.json").read_text())


def mpc(t):
    return mp.mpc(t)


def j_of(tau):
    tau = mpc(tau)
    return SA.eis_mp(tau, 4) ** 3 / SA.eta_mp(tau) ** 24


def basis_mats(rb, m, tau):
    tau = mpc(tau)
    u, eta = SA.u_mp(tau), SA.eta_mp(tau)
    return [SA.Y_mp(B, m, tau, u, eta) for B in rb], eta


def member(mats, c):
    Y = mp.matrix(3, 3)
    for M, x in zip(mats, c):
        Y += x * M
    return Y


def rmeasure(Y):
    s = mp.svd_c(Y, compute_uv=False)
    s = [abs(s[i]) for i in range(3)]
    return min(s) / max(s) if max(s) > 0 else mp.mpf(0)


def frac_vec(x):
    return [mp.mpf(Fraction(float(v)).numerator) / Fraction(float(v)).denominator for v in x]


def sector(typ, k):
    basis, d = SA.space(typ[0], typ[1], k)
    closed, rb = SA.real_basis(basis, d)
    return basis, d, closed, rb


def locate(j0, steps=230):
    """the point of F-bar with j = j0 (real), by bisection on the CP locus where j takes real values"""
    j0 = mp.mpf(j0)
    if j0 >= 1728:
        lo, hi = mp.mpf(1), mp.mpf(2)
        while mp.re(j_of(mp.mpc(0, hi))) < j0:
            hi *= 2
        for _ in range(steps):
            mid = (lo + hi) / 2
            if mp.re(j_of(mp.mpc(0, mid))) < j0:
                lo = mid
            else:
                hi = mid
        return mp.mpc(0, (lo + hi) / 2), "Re tau = 0"
    if j0 >= 0:
        lo, hi = mp.pi / 2, 2 * mp.pi / 3   # j decreases from 1728 at i to 0 at omega along the arc
        for _ in range(steps):
            mid = (lo + hi) / 2
            if mp.re(j_of(mp.expjpi(mid / mp.pi))) > j0:
                lo = mid
            else:
                hi = mid
        return mp.expjpi(((lo + hi) / 2) / mp.pi), "|tau| = 1"
    lo, hi = mp.sqrt(3) / 2, mp.mpf(2)
    while mp.re(j_of(mp.mpc(-0.5, hi))) > j0:
        hi *= 2
    for _ in range(steps):
        mid = (lo + hi) / 2
        if mp.re(j_of(mp.mpc(-0.5, mid))) > j0:
            lo = mid
        else:
            hi = mid
    return mp.mpc(-0.5, (lo + hi) / 2), "Re tau = -1/2"


def f(x):
    return float(x) if x is not None else None


# ------------------------------------------------------------------------------------------- Z0 the control
log("Z0")
SECT = {}
z0_rows, z0_ok = {}, True
for typ in SA.TYPES:
    for k in SA.WEIGHTS[typ]:
        basis, d, closed, rb = sector(typ, k)
        label = f"{SA.NAME[typ]} k={k}"
        w = 3 * k - SA.A_CHAR[typ] // 2
        rec_dim = W113["dims"].get(label)
        rec_class = W113["F2"]["rows"].get(label, {}).get("class")
        cls = SA.classify(typ[0], typ[1], k)
        ok = (len(basis) == rec_dim) and (w % 6 == 0) and (rec_class is None or rec_class == cls) and closed
        z0_ok &= ok
        z0_rows[label] = {"dim": len(basis), "recorded_dim": rec_dim, "w": w, "class": cls,
                          "recorded_class": rec_class, "real_basis": closed, "holds": ok}
        SECT[(typ, k)] = (rb, SA.M_ETA[typ])
        log(" ", label, z0_rows[label])
OUT["Z0"] = {"rows": z0_rows, "holds": bool(z0_ok)}

# ------------------------------------------------------------------------------------------- Z1 impossible = massless at i
log("Z1")
IMPOSSIBLE = [(typ, k) for typ in SA.TYPES for k in SA.WEIGHTS[typ]
              if (3 * k - SA.A_CHAR[typ] // 2) > 0 and (3 * k - SA.A_CHAR[typ] // 2) % 12 == 6]
z1, z1_ok = {}, True
for typ, k in IMPOSSIBLE:
    rb, m = SECT[(typ, k)]
    mi, _ = basis_mats(rb, m, I)
    mw, _ = basis_mats(rb, m, OMEGA)
    mg = [basis_mats(rb, m, t)[0] for t in GEN[:3]]
    r_i, r_w, r_g = [], [], []
    for _ in range(10):
        c = frac_vec(RNG.standard_normal(len(rb)))
        r_i.append(rmeasure(member(mi, c)))
        r_w.append(rmeasure(member(mw, c)))
        r_g.append(min(rmeasure(member(M, c)) for M in mg))
    ok = max(r_i) < mp.mpf(10) ** -25 and min(r_w) > mp.mpf(10) ** -12 and min(r_g) > mp.mpf(10) ** -12
    z1_ok &= bool(ok)
    lab = f"{SA.NAME[typ]} k={k}"
    z1[lab] = {"w": 3 * k - SA.A_CHAR[typ] // 2, "max r(i)": f(max(r_i)), "min r(omega)": f(min(r_w)),
               "min r(generic)": f(min(r_g)), "holds": bool(ok)}
    log(" ", lab, z1[lab])
OUT["Z1"] = {"sectors": z1, "count": len(IMPOSSIBLE), "holds": bool(z1_ok)}

# ------------------------------------------------------------------------------------------- Z2 the tuned layer's massless point
log("Z2")
TUNED = [(typ, SA.K_TUNED[typ]) for typ in SA.TYPES]
CHECK_T = [GEN[2], GEN[3], GEN[4], mp.mpc(-0.284, 2.173)]
z2, z2_ok = {}, True
JV = {}
for t in GEN[:5] + [CHECK_T[3]]:
    JV[str(t)] = j_of(t)
for typ, k in TUNED:
    rb, m = SECT[(typ, k)]
    pts = GEN[:2] + CHECK_T
    mats = {str(t): basis_mats(rb, m, t) for t in pts}
    rows = []
    for _ in range(10):
        c = frac_vec(RNG.standard_normal(len(rb)))

        def G(t):
            M, eta = mats[str(t)]
            return mp.det(member(M, c)) / eta ** (6 * k)

        g1, g2 = G(GEN[0]), G(GEN[1])
        j1, j2 = JV[str(GEN[0])], JV[str(GEN[1])]
        al = (g1 - g2) / (j1 - j2)
        be = g1 - al * j1
        res = max(abs(G(t) - (al * JV[str(t)] + be)) / abs(G(t)) for t in CHECK_T)
        im_al, im_be = abs(mp.im(al)) / abs(al), abs(mp.im(be)) / abs(be)
        j0 = -mp.re(be) / mp.re(al)
        tau0, locus = locate(j0)
        M0, _ = basis_mats(rb, m, tau0)
        r0 = rmeasure(member(M0, c))
        ok = res < mp.mpf(10) ** -25 and im_al < mp.mpf(10) ** -25 and im_be < mp.mpf(10) ** -25 and r0 < mp.mpf(10) ** -20
        rows.append({"linear_residual": f(res), "Im/abs alpha": f(im_al), "Im/abs beta": f(im_be), "j0": f(j0),
                     "tau0": [f(mp.re(tau0)), f(mp.im(tau0))], "locus": locus, "r(tau0)": f(r0), "holds": bool(ok)})
        z2_ok &= bool(ok)
    lab = f"{SA.NAME[typ]} k={k}"
    z2[lab] = {"members": rows, "holds": all(r["holds"] for r in rows),
               "loci": sorted({r["locus"] for r in rows})}
    log(" ", lab, "holds", z2[lab]["holds"], "max r(tau0)", max(r["r(tau0)"] for r in rows),
        "max residual", max(r["linear_residual"] for r in rows), "loci", z2[lab]["loci"])
OUT["Z2"] = {"sectors": z2, "holds": bool(z2_ok)}

# ------------------------------------------------------------------------------------------- Z3 tuned members zero-free
log("Z3")
Z3_T = GEN[:3] + [mp.mpc(0, 1.01), OMEGA + mp.mpc(0, 0.01), mp.mpc(0, 2.5)]
z3, z3_ok, rank2_total = {}, True, 0
for typ, k in TUNED:
    sp = TF.SectorParam(typ, k, RNG)
    rb, m = sp.rb, SA.M_ETA[typ]
    mats = {str(t): basis_mats(rb, m, t) for t in Z3_T + [I, OMEGA]}
    rows = []
    for _ in range(10):
        v = RNG.standard_normal(sp.dim)
        c = sp.coeffs_mp(v)
        Gs, scales = [], []
        for t in Z3_T:
            M, eta = mats[str(t)]
            Y = member(M, c)
            mx = max(abs(Y[a, b]) for a in range(3) for b in range(3))
            Gs.append(mp.det(Y) / eta ** (6 * k))
            scales.append(abs(mp.det(Y)) / mx ** 3)
        if max(scales) < mp.mpf(10) ** -30:
            rows.append({"rank_two": True, "max |det|/max|Y|^3": f(max(scales))})
            rank2_total += 1
            continue
        spread = max(abs(g - Gs[0]) for g in Gs) / abs(Gs[0])
        rs = [rmeasure(member(mats[str(t)][0], c)) for t in Z3_T + [I, OMEGA]]
        ok = spread < mp.mpf(10) ** -20 and min(rs) > mp.mpf(10) ** -15 and abs(Gs[0]) > 0
        rows.append({"rank_two": False, "G spread": f(spread), "min r (incl. i, omega)": f(min(rs)),
                     "r(i)": f(rs[-2]), "r(omega)": f(rs[-1]), "holds": bool(ok)})
    good = [r for r in rows if not r["rank_two"]]
    ok_s = all(r["holds"] for r in good)
    z3_ok &= ok_s
    lab = f"{SA.NAME[typ]} k={k}"
    z3[lab] = {"members": rows, "holds": bool(ok_s), "tensor_check": sp.check}
    log(" ", lab, "holds", ok_s, "rank-two", sum(r["rank_two"] for r in rows),
        "max spread", max((r["G spread"] for r in good), default=None),
        "min r", min((r["min r (incl. i, omega)"] for r in good), default=None))
z3_ok = z3_ok and rank2_total <= 2
OUT["Z3"] = {"sectors": z3, "rank_two_total": rank2_total, "holds": bool(z3_ok)}

# ------------------------------------------------------------------------------------------- Z4 the end's dressing
log("Z4")
e4w = abs(SA.eis_mp(OMEGA, 4))
nie = {}
for N, name in [(0, "Leech"), (1104, "D24+")]:
    tau0, locus = locate(720 - N)
    val = abs(j_of(tau0) - 720 + N)
    nie[name] = {"N": N, "zero at": [f(mp.re(tau0)), f(mp.im(tau0))], "locus": locus, "|Theta_L/Delta| there": f(val)}
mult = {}
t = GEN[0]
for cc in (8, 12, 16, 24):
    ratio = (SA.eta_mp(t + 1) / SA.eta_mp(t)) ** cc
    mult[str(cc)] = {"|ratio - 1|": f(abs(ratio - 1)), "|ratio - e^(2 pi i c/24)|": f(abs(ratio - mp.expjpi(mp.mpf(cc) / 12)))}
z4_ok = (e4w < mp.mpf(10) ** -40 and all(v["|Theta_L/Delta| there"] < 1e-30 for v in nie.values())
         and all(mult[str(c)]["|ratio - e^(2 pi i c/24)|"] < 1e-40 for c in (8, 12, 16, 24))
         and all(mult[str(c)]["|ratio - 1|"] > 1e-3 for c in (8, 12, 16)) and mult["24"]["|ratio - 1|"] < 1e-40)
OUT["Z4"] = {"|E4(omega)|": f(e4w), "Niemeier": nie, "eta^c multiplier at T": mult, "holds": bool(z4_ok)}
log(" ", OUT["Z4"])

# ------------------------------------------------------------------------------------------- R1 psi on F-bar
log("R1")
xs = np.linspace(-0.5, 0.5, 201)
best = (-1.0, None)
for x in xs:
    y0 = np.sqrt(max(1 - x * x, 0.75))
    ys = np.linspace(y0, 3.0, 600)
    tau = x + 1j * ys
    _, eta = SA.u_eta_np(tau)
    psi = np.sqrt(ys) * np.abs(eta) ** 2
    n = int(np.argmax(psi))
    if psi[n] > best[0]:
        best = (float(psi[n]), complex(tau[n]))
psi_mp = {lab: f(mp.sqrt(mp.im(t)) * abs(SA.eta_mp(t)) ** 2) for lab, t in [("omega", OMEGA), ("i", I), ("1.5i", mp.mpc(0, 1.5))]}
OUT["R1"] = {"grid max": best[0], "at": [best[1].real, best[1].imag], "psi": psi_mp,
             "max at omega (within grid step)": bool(abs(abs(best[1].real) - 0.5) < 0.006 and abs(best[1].imag - np.sqrt(3) / 2) < 0.01)}
log(" ", OUT["R1"])

# ------------------------------------------------------------------------------------------- R2 the leptons' feasibility
log("R2")
from sympy import Matrix, Rational  # noqa: E402


def sym_basis(rb, d):
    """a rational basis (coefficient vectors in rb) of the symmetric members"""
    mons = SA.normal_monomials(d)
    idx = {mon: n for n, mon in enumerate(mons)}
    nm = len(mons)
    cols = []
    for B in rb:
        BT = [[B[j][i] for j in range(3)] for i in range(3)]
        v = [Rational(0)] * (9 * nm)
        for i in range(3):
            for jj in range(3):
                for mon, x in B[i][jj].items():
                    v[(3 * i + jj) * nm + idx[mon]] += Rational(x.numerator, x.denominator)
                for mon, x in BT[i][jj].items():
                    v[(3 * i + jj) * nm + idx[mon]] -= Rational(x.numerator, x.denominator)
        cols.append(v)
    A = Matrix(cols).T
    return [[Fraction(int(z.p), int(z.q)) for z in vec] for vec in A.nullspace()]


r2 = {}
for typ, ks in [((1, 1), (1, 5)), ((-1, -1), (3, 7))]:
    for k in ks:
        tuned = (k == SA.K_TUNED[typ])
        basis, d = SA.space(typ[0], typ[1], k)
        _, rb = SA.real_basis(basis, d)
        S = sym_basis(rb, d)
        row = {"dim": len(rb), "sym_dim": len(S), "w": 3 * k - SA.A_CHAR[typ] // 2, "tuned": tuned}
        if tuned and len(S) >= 1:
            sp = TF.SectorParam(typ, k, RNG)
            Bm = np.array([[float(x) for x in vec] for vec in S]).T   # n x s
            As = np.einsum("ijk,ia,jb,kc->abc", sp.As, Bm, Bm, Bm)
            row["restricted cubic max |coef|"] = float(np.max(np.abs(As)))
            row["automatic on the symmetric part"] = bool(float(np.max(np.abs(As))) < 1e-12 * max(1.0, float(np.max(np.abs(sp.As)))))
            nondeg, roots_found = 0, 0
            m = SA.M_ETA[typ]
            mats = basis_mats(sp.rb, m, GEN[0])[0]
            mats2 = basis_mats(sp.rb, m, GEN[1])
            for _ in range(10):
                vv, ee = RNG.standard_normal(len(S)), RNG.standard_normal(len(S))
                a3 = np.einsum("abc,a,b,c->", As, ee, ee, ee)
                a2 = 3 * np.einsum("abc,a,b,c->", As, vv, ee, ee)
                a1 = 3 * np.einsum("abc,a,b,c->", As, vv, vv, ee)
                a0 = np.einsum("abc,a,b,c->", As, vv, vv, vv)
                rts = [x.real for x in np.roots([a3, a2, a1, a0]) if abs(x.imag) < 1e-9 * max(1, abs(x))]
                if not rts:
                    continue
                roots_found += 1
                s_ = min(rts, key=abs)
                cfull = Bm @ (vv + s_ * ee)
                c = [mp.mpf(float(x)) for x in cfull]
                Y1 = member(mats, c)
                Y2 = member(mats2[0], c)
                g1 = mp.det(Y1) / basis_mats(sp.rb, m, GEN[0])[1] ** (6 * k)
                g2 = mp.det(Y2) / mats2[1] ** (6 * k)
                if rmeasure(Y1) > 1e-8 and abs(g1 - g2) / abs(g1) < 1e-6:
                    nondeg += 1
            row["lines with a real root"] = roots_found
            row["non-degenerate, G constant to 1e-6 (float root)"] = nondeg
        r2[f"{SA.NAME[typ]} k={k}"] = row
        log(" ", SA.NAME[typ], k, row)


def nfree(dim, tuned):
    return dim - 1 - int(tuned)


CH = {+1: [((1, 1), 1), ((1, 1), 5), ((1, -1), 0), ((1, -1), 4)],
      -1: [((-1, -1), 3), ((-1, -1), 7), ((-1, 1), 0), ((-1, 1), 4)]}
WB = {+1: [((1, 1), 1), ((1, 1), 5)], -1: [((-1, -1), 3), ((-1, -1), 7)]}
table = []
for sL in (+1, -1):
    for (ct, ck) in CH[sL]:
        cdim = len(SECT[(ct, ck)][0])
        ctuned = ck == SA.K_TUNED[ct]
        cn = nfree(cdim, ctuned)
        note = ""
        if ct[0] != ct[1] and ck == 0:
            note = "identity: degenerate charged leptons"
        if ct == (1, 1) and ck == 1:
            note = "dim 1: B1636's sum rule, m2/m1 >= 1/2"
        for (wt, wk) in WB[sL]:
            wrow = r2[f"{SA.NAME[wt]} k={wk}"]
            wtuned = (wk == SA.K_TUNED[wt]) and not wrow.get("automatic on the symmetric part", False)
            if wtuned and not wrow.get("non-degenerate, G constant to 1e-6 (float root)"):
                wn = None
            else:
                wn = nfree(wrow["sym_dim"], wtuned) if wrow["sym_dim"] >= 1 else None
            p = None if wn is None else cn + wn
            table.append({"L hand": sL, "charged": f"{SA.NAME[ct]} k={ck}", "charged free": cn,
                          "Weinberg": f"sym {SA.NAME[wt]} k={wk}", "Weinberg free": wn, "total at fixed tau": p,
                          "over seven observables": None if p is None else 7 - p, "note": note})
OUT["R2"] = {"symmetric parts": r2, "pairs": table,
             "assumption": "Weinberg coupling in the symmetric part of the (s_L, s_L) space at weight k; chat1's"}
for row in table:
    log(" ", row)

OUT["seconds"] = time.time() - T0
(HERE / "zero_free_checks.json").write_text(json.dumps(OUT, indent=1, default=str))
log("cells", {c: OUT[c]["holds"] for c in ("Z0", "Z1", "Z2", "Z3", "Z4")})
log("written zero_free_checks.json")
