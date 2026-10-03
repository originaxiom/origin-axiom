#!/usr/bin/env python3
"""B1530 post-run structural check (written after the readings on m135 and m136; disclosed in FINDINGS, and not a sealed
quantity): are m135's kappa = 1 interior classes and m136's kappa = -1 classes one class on the two states' common double
cover?

Why.  -LLRR (m135) and +LLRR (m136) have monodromies -phi and +phi, phi = LLRR.  Their squares agree, so both contain the
bundle group of phi^2 = (LLRR)^2 with index two, Gamma_2 = <a, b, t^2>.  At u = (0, 1/2) both members have nu(a) = 1,
nu(b) = -1, nu(t) = -1 (m135: kappa = nu(abt) = 1; m136: kappa = nu(t) = -1), so both restrict to the character
(0, 1/2) with nu(t^2) = 1 on Gamma_2.  By the transfer, H^1(Gamma_2; nu (x) rho) = H^1(Gamma; nu (x) rho) +
H^1(Gamma; nu eps (x) rho), eps the deck character (eps(t) = -1, trivial on F).  On m135 the second summand is the kappa = -1
character at u, which carries nothing (route S); on m136 it is the kappa = 1 character at u, simple.  Both predict h^1 = 2
on Gamma_2 with one interior class.  This reads Gamma_2 exactly:
  - the group: family_lib.word_group('+', 'LLRRLLRR'), the bundle of phi^2 (not a census state: (LLRR)^2 is a proper power);
  - the point: m136's exact holonomy (post_run_e136.py) with t -> t^2.  The bundle of phi^2 covers m135 too (-I is central
    in SL(2, Z), so (-phi)^2 = phi^2), and by Mostow rigidity the hyperbolic structure is the same; but in the bundle
    presentation m135's t^2 may differ from t_2 by an element g of F, so m135's member restricts to nu(t_2) = nu(g)^-1,
    which this script does not identify.  So both nu(t_2) = 1 and nu(t_2) = -1 are read;
  - at u = (0, 1/2) and (1/2, 0), nu(t_2) = +-1: h^1 and the interior dimension of nu (x) rho, and W1 at the interior class
    and at a boundary-type class (exact_lib.class_index on W1 and Lambda^2 W1).
Writes post_run_cover.json and post_run_cover_log.txt."""
import itertools
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
import post_run_e136 as P136  # noqa: E402

LOG = []


def say(s):
    print(s, flush=True)
    LOG.append(s)


def main():
    t0 = time.time()
    say(f"B1530 post-run check: the common double cover of m135 and m136, "
        f"{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}")
    m136, _ = P136.m136_sl2()
    R6 = {"a": m136["a"], "b": m136["b"], "t": E.mmul(m136["t"], m136["t"])}
    G, img, chars, D = S.group("+", "LLRRLLRR")
    rho = S.four_module(R6)
    assert rho.check(G.rels)
    say(f"Gamma_2 = +LLRRLLRR: D = {D}, {len(chars)} base points; the relators hold exactly on m136's four with t -> t^2")
    rows = []
    for u, kt in itertools.product([(Fraction(0), Fraction(1, 2)), (Fraction(1, 2), Fraction(0))],
                                   [Fraction(0), Fraction(1, 2)]):
        assert u in chars
        ch = S.nu("+", u, kt)
        V = rho.twist(ch)
        CV = E.Cohomology(G, V)
        row = {"u": [str(x) for x in u], "nu(t_2)": "1" if kt == 0 else "-1", "h1": CV.h1, "interior": CV.n, "W1": {}}
        ints = CV.interior()
        cls = {}
        if ints and len(ints) < CV.h1:                              # interior and boundary-type classes
            cls["c_int"] = CV.combine(ints[0])
            cls["c_b"] = next(z for z in CV.reps
                              if E.rank_vectors(CV.Bvecs + [cls["c_int"], z], CV.d * CV.ng) == CV.dimB + 2)
        elif ints:                                                  # every class interior (an acyclic cusp)
            for k in range(len(ints)):
                cls[f"interior {k}"] = CV.combine(ints[k])
        else:
            for k in range(CV.h1):
                cls[f"basis {k}"] = CV.reps[k]
        for name, c in cls.items():
            W1 = E.extension(V, c, None)
            assert W1.check(G.rels)
            a, b = E.class_index(G, W1), E.class_index(G, W1.wedge2())
            row["W1"][name] = [a["I"], b["I"]]
        rows.append(row)
        say(f"  u {row['u']}, nu(t_2) = {row['nu(t_2)']}: h1 {CV.h1}, interior {CV.n}; W1 {row['W1']}")
    out = {"Gamma_2": "+LLRRLLRR", "D": D,
           "rows": rows, "seconds": round(time.time() - t0)}
    (HERE / "post_run_cover.json").write_text(json.dumps(out, indent=1, default=str))
    (HERE / "post_run_cover_log.txt").write_text("\n".join(LOG) + "\n")
    say(f"({out['seconds']} s)")


if __name__ == "__main__":
    main()
