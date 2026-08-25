#!/usr/bin/env python3
"""Hostile extension of outside-bench C-P1 over all eleven odd rows.

Usage:
    python3 verify_cp1_all_odd.py /path/to/outside_bench/certificates/cp1_strata.py

The source must be the exact certificate from Origin Axiom commit 22a8a1a4.
The upstream script reconstructs the E6/27 machinery and its 20 accepted
characteristics. This wrapper then applies its own semilinear-matrix test to
every odd row, rather than only the one odd distinguished row checked there.

This does not repair the upstream completeness dependency on the standard
20-orbit E6 classification, and it does not turn internal A1 parity into a
four-dimensional spinor or chirality statement.
"""

from __future__ import annotations

import hashlib
import runpy
import sys
from pathlib import Path


EXPECTED_SOURCE_SHA256 = (
    "8d3e7092d65803529ca68ef2c01b270d01f61871d84d9d7d606c9f1e63b71c46"
)


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {Path(sys.argv[0]).name} CP1_STRATA_PY")

    source = Path(sys.argv[1]).resolve()
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    assert digest == EXPECTED_SOURCE_SHA256, (
        f"unexpected cp1_strata.py digest: {digest}"
    )

    ns = runpy.run_path(str(source))

    chars = ns["chars"]
    rho27_Q = ns["rho27_Q"]
    toF = ns["toF"]
    nilexp = ns["nilexp"]
    wordmat = ns["wordmat"]
    eye = ns["eye"]
    mmul = ns["mmul"]
    galM = ns["galM"]
    fneg = ns["fneg"]
    ONE = ns["ONE"]
    QQ = ns["QQ"]

    checked = []
    for characteristic in sorted(chars):
        e, _, f = chars[characteristic]
        h27 = rho27_Q(ns["Hc"](characteristic))
        weights = [int(h27[i][i]) for i in range(27)]
        if not any(weight % 2 for weight in weights):
            continue

        e27 = toF(rho27_Q(e))
        f27 = toF(rho27_Q(f))
        a27 = nilexp(e27, ONE)
        b27 = nilexp(f27, QQ)
        a27_inv = nilexp(e27, fneg(ONE))
        b27_inv = nilexp(f27, fneg(QQ))
        generators = {
            "a": a27,
            "A": a27_inv,
            "b": b27,
            "B": b27_inv,
        }

        relator = wordmat("abABaBAbaB", generators)
        omega = nilexp(e27, QQ)
        omega_inv = nilexp(e27, fneg(QQ))
        omega_sq = mmul(omega, galM(omega))
        intertwines_a = mmul(omega, mmul(galM(a27), omega_inv)) == a27
        intertwines_b = (
            mmul(omega, mmul(galM(b27), omega_inv))
            == wordmat("BabAb", generators)
        )

        verdict = (
            relator == eye(27),
            omega_sq == a27,
            intertwines_a,
            intertwines_b,
        )
        print(f"odd characteristic {characteristic}: {verdict}")
        assert all(verdict), (characteristic, verdict)
        checked.append(characteristic)

    assert len(checked) == 11, checked
    print("ALL 11 ODD ACCEPTED CHARACTERISTICS PASS THE SELECTED-BEAT IDENTITIES")


if __name__ == "__main__":
    main()
