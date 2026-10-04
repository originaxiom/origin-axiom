#!/usr/bin/env python3
"""B1476 (THE SPIN SWAP, Phase 1c) cells C1-C4.
C1: the spin tables of m206, o10_150696 (on its shortest presentation), o10_150707 with B1475's instrument.
C2: Chern-Simons classes (HP, folded mod 1/2 into {0, 1/4, other}) of the 13 amphichiral rank-one members (and the 41 chiral).
C3: is m003 / m004 the orientation double cover of a non-orientable census manifold (SnapPy NonorientableCuspedCensus)?
C4: the Pin sign on m004: for each lift (rho, rho (x) eps) and each reversing tau with eta = 1, C conj(C) = c.1 (Schur), sign(c)."""
import sys, json, pathlib, warnings; warnings.filterwarnings("ignore")
HERE = pathlib.Path(__file__).resolve().parent
FRONTIER = next((p for p in HERE.parents if p.name == "frontier"), pathlib.Path.cwd() / "frontier")
for d in ("B1471_the_cancellation_is_a_theorem_of_amphichirality", "B1474_the_spin_swap_phase_1a_fix_or_swap_by_the_matrix_route", "B1475_the_spin_swap_phase_1b_does_the_swap_carry_a_quantity"):
    sys.path.insert(0, str(FRONTIER / d / "verification"))
import snappy, realness as R, spin_swap as SS, spin_quantity as SQ
from mpmath import mp, mpf, mpc, matrix, eye, inverse, norm, nstr, conj as cj
mp.dps = 50
B1474 = FRONTIER / "B1474_the_spin_swap_phase_1a_fix_or_swap_by_the_matrix_route" / "verification"
SWAP = ["m003", "m207", "s955", "s957", "s960", "t12838", "o10_150695"]; FIX = ["m004", "m206", "s961", "t12839", "o10_150696", "o10_150707"]


def fold(x, mod):
    x = float(x) % mod; return min(x, mod - x)


def cs_class(name):
    M = snappy.ManifoldHP(name); c = M.chern_simons(); f0 = fold(c, 0.5); f4 = fold(c - 0.25, 0.5)
    return dict(cs=str(c)[:24], cls=("zero" if f0 < 1e-20 else ("quarter" if f4 < 1e-20 else "other")), dist=min(f0, f4))


def conjm(M): return matrix([[cj(M[i, j]) for j in range(2)] for i in range(2)])


def pin_sign(nm, taus):
    """for each lift (rho and rho (x) eps for every sign character eps) and each tau with eta trivial: C conj(C) = c 1, sign(c)"""
    pk, _ = R.setup(nm); gens = pk["gens"]; chars = SQ.characters(pk); rows = []
    for chi in chars:
        rho = {g: chi[g] * pk["rho"][g] for g in gens}
        for T in taus:
            tau = T["tau"]
            # solve C for THIS lift: C conj(rho(g)) C^-1 = +- rho(tau g)
            Xs = [conjm(rho[g]) for g in gens]; Ys = [R.word_mat(tau[g], rho) for g in gens]
            r = SS.intertwiner_pm(Xs, Ys)
            if r is None: rows.append(dict(chi=tuple(chi[g] for g in gens), tau=tau, result="no intertwiner")); continue
            C, signs = r
            eta_triv = all(s == 1 for s in signs)
            CC = C * conjm(C); c = CC[0, 0]; scal = norm(CC - c * eye(2))
            rows.append(dict(chi=tuple(chi[g] for g in gens), tau=tau, eta=dict(zip(gens, signs)), eta_trivial=eta_triv,
                             C_conjC_scalar=nstr(c, 12), scalar_residual=nstr(scal, 3), pin=("Pin+" if (eta_triv and c.real > 0) else ("Pin-" if (eta_triv and c.real < 0) else "n/a (eta nontrivial: the mirror moves this lift)"))))
    return rows


def orientation_cover_of(name, limit=None):
    """non-orientable census manifolds whose orientation double cover is isometric to `name` (orientation-blind test suffices for identity)"""
    M = snappy.Manifold(name); hits = []
    for N in snappy.NonorientableCuspedCensus:
        try:
            if abs(N.volume() * 2 - M.volume()) > 1e-6: continue
            if N.orientation_cover().is_isometric_to(M): hits.append(N.name())
        except Exception: pass
    return hits


if __name__ == "__main__":
    out = {}
    # C1
    sw = json.load(open(B1474 / "spin_swap.json")); retri = json.load(open(B1474 / "o10_150696_retri.json"))
    c1 = {}
    for nm in ("m206", "o10_150707"):
        c1[nm] = SQ.run(nm, sw[nm]["solutions"][:6]); print("C1", nm, "spin", c1[nm]["n_spin"], "mirror-invariant", c1[nm]["mirror_invariant_any_tau"], flush=True)
    # o10_150696 on its shortest presentation: SQ.run uses R.setup(nm) default; build with randomize=1 via a thin wrapper
    pk, _ = R.setup("o10_150696", randomize=1)
    _setup = R.setup
    R.setup = lambda nm, randomize=0: _setup(nm, randomize=1) if nm == "o10_150696" else _setup(nm, randomize)
    c1["o10_150696"] = SQ.run("o10_150696", retri["solutions"][:6]); print("C1 o10_150696 (randomize=1) spin", c1["o10_150696"]["n_spin"], "mirror-invariant", c1["o10_150696"]["mirror_invariant_any_tau"], flush=True)
    R.setup = _setup
    out["C1"] = c1
    # C2
    fam = json.load(open(FRONTIER / "B1235_two_seat_harvest" / "verification" / "chirality_112.json"))
    rank1 = [v for v in sw.values() if "error" not in v]
    c2 = {}
    for v in rank1:
        nm = v["name"]; c2[nm] = dict(cs_class(nm), verdict=v["verdict"], amphichiral=v["amphichiral_snappy"]); print("C2", nm, c2[nm], flush=True)
    out["C2"] = c2
    law = {nm: (r["cls"], "SWAP" if nm in SWAP else ("FIX" if nm in FIX else "chiral")) for nm, r in c2.items()}
    out["C2_law_amphichiral"] = {nm: law[nm] for nm in SWAP + FIX}
    out["C2_holds"] = all(law[nm][0] == "quarter" for nm in SWAP) and all(law[nm][0] == "zero" for nm in FIX)
    print("C2 LAW swap <=> quarter:", out["C2_holds"], flush=True)
    # C2b (P6): the 1/24 lattice on all 112, the 41 chiral rank-one, and 40 outside controls; the dilogarithm atom
    from fractions import Fraction
    from mpmath import polylog, pi as PI, log as LOG, re as RE, im as IM, exp as EXP, mpc as MPC
    def lattice_row(name):
        try:
            M = snappy.ManifoldHP(name); c = float(M.chern_simons())
        except Exception as e:
            return dict(error=str(e)[:60])
        x = c % 0.5; k = round(x * 24); d = abs(x - k / 24)
        fr = Fraction(k, 24) if d < 1e-9 else None
        return dict(cs=c, dist_to_24th=d, on_lattice=bool(d < 1e-9), value=(str(fr) if fr is not None else None), denominator=(fr.denominator if fr is not None else None))
    c2b = dict(family={}, outside={})
    for r in fam: c2b["family"][r["name"]] = lattice_row(r["name"])
    famset = {r["name"] for r in fam}; n = 0
    for M in snappy.OrientableCuspedCensus:
        if M.num_cusps() != 1 or M.name() in famset: continue
        c2b["outside"][M.name()] = lattice_row(M.name()); n += 1
        if n >= 40: break
    fam_on = sum(1 for v in c2b["family"].values() if v.get("on_lattice")); out_on = sum(1 for v in c2b["outside"].values() if v.get("on_lattice"))
    import collections
    c2b["summary"] = dict(family_on_lattice=fam_on, family_total=len(c2b["family"]), family_denominators=dict(collections.Counter(v.get("denominator") for v in c2b["family"].values())),
                          outside_on_lattice=out_on, outside_total=len(c2b["outside"]), outside_nonzero_on_lattice=sum(1 for v in c2b["outside"].values() if v.get("on_lattice") and v.get("denominator") not in (None, 1)))
    z = EXP(MPC(0, 1) * PI / 3); L2 = polylog(2, z); Rz = L2 + LOG(z) * LOG(1 - z) / 2
    vol41 = mpf(str(snappy.ManifoldHP("4_1").volume()))
    # Rogers: R(z) = Li2(z) + log z log(1-z)/2 (standard; R(1) = pi^2/6); chat1's normalised form is R - pi^2/6 (so -pi^2/12 at z = e^{i pi/3})
    c2b["atom"] = dict(Re_R_standard=nstr(RE(Rz), 25), pi2_over_12=nstr(PI ** 2 / 12, 25), Re_R_normalised=nstr(RE(Rz) - PI ** 2 / 6, 25), Im_R=nstr(IM(Rz), 25), half_vol_4_1=nstr(vol41 / 2, 25),
                       Re_ok=bool(abs(RE(Rz) - PI ** 2 / 12) < mpf(10) ** -20), Im_ok=bool(abs(IM(Rz) - vol41 / 2) < mpf(10) ** -20),
                       note="each regular ideal tetrahedron contributes Re R = pi^2/12 (normalised: -pi^2/12) to the CS part; flattenings add multiples of pi^2/6; SnapPy's CS = CS_raw/(2 pi^2) lands in (1/24)Z")
    out["C2b"] = c2b; print("C2b", c2b["summary"], "| atom", c2b["atom"]["Re_ok"], c2b["atom"]["Im_ok"], flush=True)
    # C3
    out["C3"] = {nm: orientation_cover_of(nm) for nm in ("m003", "m004")}; print("C3", out["C3"], flush=True)
    # C4
    out["C4_m004"] = pin_sign("m004", sw["m004"]["solutions"][:6]);
    for r in out["C4_m004"]: print("C4 m004", r["chi"], r.get("eta"), r.get("C_conjC_scalar"), r.get("pin"), flush=True)
    out["C4_m003"] = pin_sign("m003", sw["m003"]["solutions"][:3])
    for r in out["C4_m003"]: print("C4 m003", r["chi"], r.get("eta"), r.get("pin"), flush=True)
    json.dump(out, open(HERE / "phase_1c.json", "w"), indent=1, default=str)
