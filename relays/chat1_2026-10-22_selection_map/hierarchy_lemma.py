#!/usr/bin/env python3
"""Lemma H (computed, no data): how many levels of hierarchy the weave's theta triplet gives near each special point,
in the SM seat's frame (W113/W114: u = (theta_2^2, theta_3^2, theta_4^2), types T(x)T, Tbar(x)Tbar and mixed, real
coefficients), for generic members and for the PF1-W ('tuned', zero-free determinant) members.

The seat's modules are imported unchanged from c9f001d9d (the_strong_angle.py sha256 a9c4b15b...028622,
the_tuned_fit.py 21f979be...49c713b), extracted with their two data files into a temporary directory.

For each space, 40 random real coefficient vectors (seed 20261022; tuned members on the seat's own variety
parametrisation, seed 7): the singular values s1 <= s2 <= s3 near
  - the cusp: tau = 0.137 + iY, Y = 1.5 .. 3.5; the slope of ln(s_i/s3) against Y, in units of pi/2 (|q|^(1/4));
  - omega and i: tau = p + d e^{i phi}, d = 0.004 .. 0.032; the slope of ln(s_i/s3) against ln d.
Also the residual-charge prediction at the cusp from the T matrices alone: the T-eigenvalues on the triplet.
    python3 -B hierarchy_lemma.py        # writes hierarchy_lemma.json and hierarchy_lemma_run.txt"""
import hashlib, json, math, subprocess, sys, tempfile, pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())
REV = "c9f001d9d"
DOS = "docs/dossiers/the_weave_2026-10-07"
SHA = {"the_strong_angle.py": "a9c4b15b82739289b4698a388da117d4c517380826fcacfc16c6065221028622",
       "the_tuned_fit.py": "21f979beccd96c5470109d91579eff17af289c6951ed7485822a84e2149c713b"}
LOG = []


def say(*a):
    s = " ".join(str(x) for x in a); LOG.append(s); print(s, flush=True)


tmp = pathlib.Path(tempfile.mkdtemp())
(tmp / "received").mkdir()
for f in SHA:
    b = subprocess.run(["git", "show", f"{REV}:{DOS}/{f}"], cwd=ROOT, capture_output=True, check=True).stdout
    assert hashlib.sha256(b).hexdigest() == SHA[f], f
    (tmp / f).write_bytes(b)
for f in ("HZ2021_running_masses_MZ.json", "B1612_data.json"):
    (tmp / "received" / f).write_bytes(
        subprocess.run(["git", "show", f"{REV}:{DOS}/received/{f}"], cwd=ROOT, capture_output=True, check=True).stdout)
sys.path.insert(0, str(tmp))
import the_strong_angle as sa  # noqa: E402
import the_tuned_fit as tf  # noqa: E402

OMEGA = complex(-0.5, math.sqrt(3) / 2)
YS = np.array([1.5, 2.0, 2.5, 3.0, 3.5])
DS = np.array([0.004, 0.008, 0.016, 0.032])


def sv(sec, taus, c):
    U, ETA = sa.u_eta_np(np.array(taus))
    return np.sort(np.linalg.svd(sec.Y(U, ETA, c), compute_uv=False), axis=1)


def slope(x, y):
    return float(np.linalg.lstsq(np.vstack([x, np.ones_like(x)]).T, y, rcond=None)[0][0])


def measure(sec, coeff_iter, rng):
    rows = []
    for c in coeff_iter:
        s = sv(sec, [complex(0.137, y) for y in YS], c)
        r = {"cusp": [slope(YS, np.log(s[:, 0] / s[:, 2])) / (-math.pi / 2),
                      slope(YS, np.log(s[:, 1] / s[:, 2])) / (-math.pi / 2)]}
        for p, key in ((OMEGA, "omega"), (1j, "i")):
            ph = rng.uniform(0, 2 * math.pi)
            ss = sv(sec, [p + d * complex(math.cos(ph), math.sin(ph)) for d in DS], c)
            r[key] = [slope(np.log(DS), np.log(ss[:, 0] / ss[:, 2])), slope(np.log(DS), np.log(ss[:, 1] / ss[:, 2]))]
        rows.append(r)
    out = {}
    for key in ("cusp", "omega", "i"):
        a = np.array([r[key] for r in rows])
        out[key] = {"m1_q10_med_q90": [float(np.quantile(a[:, 0], q)) for q in (.1, .5, .9)],
                    "m2_q10_med_q90": [float(np.quantile(a[:, 1], q)) for q in (.1, .5, .9)]}
    return out


OUT = {"rev": REV, "generic": {}, "tuned": {}}
# the residual charges at the cusp: T acts on the triplet by A_T (conjugated for T), eigenvalues
for lab, conj in (("T", True), ("Tbar", False)):
    A = np.array([[complex(sa.zc(x)) for x in row] for row in sa.amat("T", conj)])
    ev = np.linalg.eigvals(A)
    OUT[f"T_eigen_phases_over_2pi_{lab}"] = sorted(float((np.angle(e) / (2 * math.pi)) % 1) for e in ev)
say("T-eigenvalue phases on the triplet (units of 2 pi):", OUT["T_eigen_phases_over_2pi_T"], "(T);",
    OUT["T_eigen_phases_over_2pi_Tbar"], "(Tbar)")

rng = np.random.default_rng(20261022)
for typ in sa.TYPES:
    for k in sa.WEIGHTS[typ] + ([8, 9] if typ in [(1, 1), (-1, -1)] else [8]):
        basis, d = sa.space(typ[0], typ[1], k)
        if not basis:
            continue
        ok, rb = sa.real_basis(basis, d)
        if not rb:
            continue
        sec = sa.Sector(rb, sa.M_ETA[typ], f"{sa.NAME[typ]} k={k}")
        res = measure(sec, [rng.normal(size=len(rb)) for _ in range(40)], rng) | {"dim": len(rb)}
        OUT["generic"][sec.label] = res
        say(f"generic {sec.label:24s} dim {len(rb):2d} | cusp m1 {res['cusp']['m1_q10_med_q90'][1]:5.2f} "
            f"m2 {res['cusp']['m2_q10_med_q90'][1]:5.2f} (q^1/4 units) | omega m1 {res['omega']['m1_q10_med_q90'][1]:5.2f} "
            f"m2 {res['omega']['m2_q10_med_q90'][1]:5.2f} | i m1 {res['i']['m1_q10_med_q90'][1]:5.2f} "
            f"m2 {res['i']['m2_q10_med_q90'][1]:5.2f} (powers of d)")

rng2 = np.random.default_rng(7)
for typ in [tf.TT, tf.BB, tf.MQT, tf.MQB]:
    sp = tf.SectorParam(typ, sa.K_TUNED[typ], rng2)
    cs = []
    while len(cs) < 40:
        c = sp.coeffs(rng2.normal(size=sp.dim))
        if c is not None:
            cs.append(c)
    res = measure(sp.S, cs, rng2) | {"dim": sp.dim, "tensor_self_check": sp.check}
    OUT["tuned"][sp.label] = res
    say(f"tuned   {sp.label:24s} dim {sp.dim:2d} | cusp m1 {res['cusp']['m1_q10_med_q90'][1]:5.2f} "
        f"m2 {res['cusp']['m2_q10_med_q90'][1]:5.2f} (q^1/4 units) | omega m1 {res['omega']['m1_q10_med_q90'][1]:5.2f} "
        f"m2 {res['omega']['m2_q10_med_q90'][1]:5.2f} | i m1 {res['i']['m1_q10_med_q90'][1]:5.2f} "
        f"m2 {res['i']['m2_q10_med_q90'][1]:5.2f} (powers of d)")

(HERE / "hierarchy_lemma.json").write_text(json.dumps(OUT, indent=1) + "\n")
(HERE / "hierarchy_lemma_run.txt").write_text("\n".join(LOG) + "\n")
