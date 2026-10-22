#!/usr/bin/env python3
"""COMPUTED, no data: main's fibre frame (B1720's instrument at 3412bf09d, through two_ingredients_census.evaluate) reads
each field's 6Y only mod N on a line of order N.  At an off-grid tau, on lines of order 4, 5, 7 and 10, the six ratios
of every sector and reading and the CKM moduli are compared between the record's charges and the same charges shifted by
multiples of N (two shift vectors); and the down and lepton ratios are compared on each line (B1703: d = e for N | 4, 5).
Ratios below 1e-8 (an exactly massless state) are compared in absolute value, the rest in log.
    python3 -B mod_n_check.py      # writes mod_n_check_run.txt"""
import importlib.util, math, pathlib

HERE = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("tic", HERE / "two_ingredients_census.py")
tic = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(tic)
B = tic.B; BASE = dict(B.SIXY); TAU = (0.37, 2.71); LOG = []


def say(s):
    LOG.append(s); print(s, flush=True)


def frame(a, b, six):
    B.SIXY.clear(); B.SIXY.update(six)
    try:
        return tic.evaluate(TAU[0], TAU[1], a, b)
    finally:
        B.SIXY.clear(); B.SIXY.update(BASE)


def diff(p, q):
    out = 0.0
    for x, y in zip(p, q):
        out = max(out, abs(x - y) if min(x, y) < 1e-8 else abs(math.log(x / y)))
    return out


say(f"tau = {TAU[0]} + {TAU[1]}i; charges 6Y = {BASE}")
for a, b, N in [(1 / 4, 3 / 4, 4), (2 / 5, 1 / 5, 5), (2 / 7, 3 / 7, 7), (2 / 5, 1 / 10, 10)]:
    r0 = frame(a, b, BASE)
    for vec in [(1, -2, 3, -1, 2), (-2, 1, 1, 2, -1)]:
        six = dict(BASE); six.update({k: BASE[k] + N * s for k, s in zip(("Q", "d", "L", "e", "u"), vec)})
        r1 = frame(a, b, six)
        dm = max(diff(r0[k], r1[k]) for k in r0 if not k.startswith("ckm"))
        dv = max(diff(r0[k][:3], r1[k][:3]) for k in r0 if k.startswith("ckm"))
        say(f"line ({a:.4g}, {b:.4g}), order {N}: charges + {N} x {vec}: masses {dm:.1e}, |V| {dv:.1e}")
    de = max(diff(r0[f"down|{h}|{rd}"], r0[f"lep|{h}|{rd}"]) for h in ("L_max", "L_2") for rd in ("S", "St", "conjS"))
    m1 = min(r0[f"down|{h}|S"][1] for h in ("L_max", "L_2"))
    say(f"   down vs leptons on this line: {de:.1e} (down m1/m3 at S: {m1:.2e})")
(HERE / "mod_n_check_run.txt").write_text("\n".join(LOG) + "\n")
