#!/usr/bin/env python3
"""B1530 post-run check E on m136 = +LLRR (written after the census and post_run_b.py had read m136's kappa = -1 members;
disclosed in FINDINGS): those members read exactly, in route E's arithmetic.

Why.  post_run_b.py reads every kappa = -1 member in routes N and W at 60 digits, and post_run_s.py reads m136 on SnapPy's
presentation, also at 60 digits.  m136 is commensurable with PSL(2, Z[i]) (volume 3.66386, the Whitehead link's), so its
holonomy can be read exactly, as sm:B1529's post_run_exact_m135.py read m135's: the cusp's fixed point and its images under
a and b sent to 0, 1 and infinity, each matrix scaled by its largest entry, every entry read as a Gaussian rational (an
assertion at 10^-50 fails if it is not one).  That reader is sm:B1529's function, run here with its sign set to +.
What this does, exactly over Q(zeta_24) (exact_lib):
  - the relators are checked on the exact four;
  - at every character nu of m136 with kappa = nu(t') in {1, -1} (four base points u, so eight characters): h^1 and the
    interior dimension of V = nu (x) rho, V_eta = nu^5 (x) rho and V (x) L;
  - at every member: W1 = [[V, c L], [0, L]] at each class of a basis of H^1(V_eta) and at their sum, and W2* at the dual
    classes, read by exact_lib.class_index (B1297's identity, the annihilator identity and Lemma E asserted at each reading);
  - at kappa = -1, Lemma N's mechanism: x cup c (Wang's test), recorded.
Writes post_run_e136.json and post_run_e136_log.txt."""
import json
import sys
import time
import warnings
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import exact_lib as E  # noqa: E402
import exact_states as S  # noqa: E402

SIGN, WORD = "+", "LLRR"
LOG = []


def say(s):
    print(s, flush=True)
    LOG.append(s)


def m136_sl2():
    P = S.load(S.B1529, "post_run_exact_m135", "b1529_post_run_exact_m135")
    saved = (P.SIGN, P.WORD)
    P.SIGN, P.WORD = SIGN, WORD
    try:
        g2 = P.exact_sl2()
    finally:
        P.SIGN, P.WORD = saved
    return {g: [[E.from_z8(x) for x in row] for row in g2[g]] for g in "abt"}, g2


def z8_str(x):
    """c0 + c1 z + c2 z^2 + c3 z^3, z = e^{i pi/4}, as sm:B1529's Z8 holds it"""
    return "(" + ", ".join(str(c) for c in x.c) + ")"


def classes_of(C):
    """a basis of H^1 (representatives) and, when there are two or more, their sum"""
    out = {f"basis {k}": C.reps[k] for k in range(C.h1)}
    if C.h1 >= 2:
        s = C.reps[0]
        for k in range(1, C.h1):
            s = [p + q for p, q in zip(s, C.reps[k])]
        out["the sum of the basis"] = s
    return out


def main():
    t0 = time.time()
    say(f"B1530 post-run check E on {SIGN}{WORD} (m136), {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}")
    sl2, g2 = m136_sl2()
    say("the exact holonomy (PGL(2, Q(i)), sm:B1529's reader with sign +): " +
        "; ".join(f"{g}: {[[z8_str(x) for x in row] for row in g2[g]]}" for g in "abt") +
        " (coefficients of 1, z, z^2, z^3 with z = e^{i pi/4})")
    G, img, chars, D = S.group(SIGN, WORD)
    rho = S.four_module(sl2)
    assert rho.check(G.rels)
    say(f"the four: the relators hold exactly; D = {D}, {len(chars)} base points u")
    phi_p, tp = S.phi_prime(SIGN, img), S.tprime(SIGN)
    rows = []
    for kturn, kname in ((Fraction(0), "1"), (Fraction(1, 2), "-1")):
        for u in chars:
            t1 = time.time()
            ch = S.nu(SIGN, u, kturn)
            V = rho.twist(ch)
            Lc = S.power_char(ch, -4)
            trivial_L = all(v == E.ONE for v in Lc.values())
            L = None if trivial_L else E.line(G.gens, Lc)
            Veta = rho.twist(S.power_char(ch, 5))
            VL = rho.twist(S.power_char(ch, -3))
            CV, CE, CQ = E.Cohomology(G, V), E.Cohomology(G, Veta), E.Cohomology(G, VL)
            row = {"u": [str(x) for x in u], "kappa": kname, "case": "(a)" if trivial_L else "(b)",
                   "h1": {"V": CV.h1, "V_eta": CE.h1, "V (x) L": CQ.h1},
                   "n (interior)": {"V": CV.n, "V_eta": CE.n, "V (x) L": CQ.n}, "W1": {}, "W2": {}, "mechanism": {}}
            if CE.h1 >= 1:
                cls = classes_of(CE)
                for name, c in cls.items():
                    W1 = E.extension(V, c, L)
                    assert W1.check(G.rels)
                    a, b = E.class_index(G, W1), E.class_index(G, W1.wedge2())
                    row["W1"][name] = {"I(W)": a["I"], "I(L2W)": b["I"],
                                       "c|P a coboundary": CE.coboundary_on_P(c) is not None}
                    if trivial_L:
                        row["mechanism"][f"x cup {name} = 0"] = E.cup_with_fibration_class_vanishes(V, c, phi_p, tp)[0]
                Vd = V.dual()
                Linv = None if trivial_L else E.line(G.gens, S.power_char(ch, 4))
                CEd = E.Cohomology(G, Veta.dual())
                for name, c in classes_of(CEd).items():
                    W2s = E.extension(Vd, c, Linv)
                    assert W2s.check(G.rels)
                    a, b = E.class_index(G, W2s), E.class_index(G, W2s.wedge2())
                    row["W2"][name] = {"I(W)": -a["I"], "I(L2W)": -b["I"]}
            row["seconds"] = round(time.time() - t1)
            rows.append(row)
            say(f"  u {row['u']}, kappa {kname}: case {row['case']}, h1 {row['h1']}, interior {row['n (interior)']}; W1 "
                f"{ {k: (v['I(W)'], v['I(L2W)']) for k, v in row['W1'].items()} }; W2 "
                f"{ {k: (v['I(W)'], v['I(L2W)']) for k, v in row['W2'].items()} }; {row['mechanism']} ({row['seconds']} s)")
    gen = [(r["u"], r["kappa"], k, (v["I(W)"], v["I(L2W)"])) for r in rows for k, v in r["W1"].items()
           if v["I(W)"] == v["I(L2W)"] != 0]
    out = {"state": SIGN + WORD, "holonomy (Gaussian rationals, as read; coefficients of 1, z, z^2, z^3, z = e^{i pi/4})": {g: [[z8_str(x) for x in row] for row in g2[g]]
                                                                          for g in "abt"},
           "rows": rows, "generation-shaped": gen, "seconds": round(time.time() - t0)}
    say(f"generation-shaped (exact): {gen} ({out['seconds']} s)")
    (HERE / "post_run_e136.json").write_text(json.dumps(out, indent=1, default=str))
    (HERE / "post_run_e136_log.txt").write_text("\n".join(LOG) + "\n")


if __name__ == "__main__":
    main()
