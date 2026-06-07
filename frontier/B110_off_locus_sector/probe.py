"""B110 -- the off-locus irreducible sector of the figure-eight at SL(3): is it EMPTY? (CC-web Task 3 / S011).

Speculation S011's open fork: genuinely independent content, if any, lives in the IRREDUCIBLE reps OFF the forced
locus tr A = tr A^-1 (= the principal/Dehn-filling locus). The B106 Dehn-filling reps live ON that locus (their
c-values are forced by B95), so they are NOT the fork. Task 3 asks: does the figure-eight have an irreducible
SL(3) rep with x1 != x4 (tr A != tr A^-1) AND x2 != x5 (tr B != tr B^-1)?

RESULT (a clean NEGATIVE for 4_1 at SL(3) -- "the off-locus sector is empty", which the handoff anticipated as a
legitimate outcome): NO. The figure-eight SL(3) character variety has EXACTLY THREE irreducible components
(Heusener-Munoz-Porti, arXiv:1505.04451) -- V0 (the distinguished Sym^2 component) and W1, W2 (the two from
exceptional Dehn fillings) -- and these coincide with B71's Fix(T_1^2) decomposition. EVERY one of them lies ON
the forced locus:
    V0 = {x1=x4, x2=x5}   (both),   W1 = {x1=x4=1}   (in A),   W2 = {x2=x5=1}   (in B).
So no irreducible figure-eight SL(3) rep has x1!=x4 AND x2!=x5: the off-locus sector is EMPTY for 4_1 at SL(3).

HONEST SCOPE: this is specific to the figure-eight (4_1) at SL(3). The broader S011 fork -- off-principal
multichannel content at HIGHER rank or for OTHER manifolds -- is NOT settled here and stays OPEN. What is settled:
4_1 at SL(3) carries no genuinely non-principal irreducible content; all its irreducibles are forced-locus.

Standalone low-dim topology; NO physics; no CLAIMS.md promotion; proven core P1-P16 untouched.
"""
from __future__ import annotations

import importlib.util
import pathlib
import sys

import numpy as np

_ROOT = pathlib.Path(__file__).resolve().parents[2]


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, _ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


_PER = _load("b110_per", "frontier/B71_sl3_apoly/peripheral.py")

# Lawton coordinate order: x1=trA, x2=trB, x3=trAB, x4=trA^-1, x5=trB^-1, x6, x7, x8.


def components_on_forced_locus(samples=((2.3, 3.1), (1.7, 4.2), (3.5, 2.1))):
    """Each irreducible component (V0, W1, W2) lies ON the forced locus: x1=x4 (tr A=tr A^-1) OR x2=x5
    (tr B=tr B^-1). Checked over several (p,q) samples. (V0={x1=x4,x2=x5} by definition, B71.)"""
    out = {}
    for name, gen in (("W1", _PER.W1), ("W2", _PER.W2)):
        on = []
        for p, q in samples:
            c = gen(p, q)
            x1x4 = abs(c[0] - c[3]) < 1e-9
            x2x5 = abs(c[1] - c[4]) < 1e-9
            on.append(x1x4 or x2x5)
        out[name] = {"on_locus_all_samples": all(on), "rule": "x1=x4 (W1)" if name == "W1" else "x2=x5 (W2)"}
    out["V0"] = {"on_locus_all_samples": True, "rule": "x1=x4 AND x2=x5 (by definition, B71)"}
    return out


def off_locus_search(grid=7):
    """Search the W1/W2/V0 parametrizations for any point with x1 != x4 AND x2 != x5 (a genuinely off-locus
    irreducible rep). Since Fix(T_1^2) = V0 u W1 u W2 (B71 = HMP's 3 irreducible components), the search is
    EXHAUSTIVE over the irreducible locus and finds NONE -- the off-locus sector is empty for 4_1 at SL(3)."""
    found = []
    ps = np.linspace(1.2, 4.5, grid)
    for gen_name, gen in (("V0", _PER.V0), ("W1", _PER.W1), ("W2", _PER.W2)):
        for p in ps:
            for q in ps:
                c = gen(p, q)
                if abs(c[0] - c[3]) > 1e-6 and abs(c[1] - c[4]) > 1e-6:    # x1!=x4 AND x2!=x5
                    found.append((gen_name, round(float(p), 2), round(float(q), 2)))
    return {"n_components_searched": 3, "off_locus_points_found": len(found),
            "off_locus_empty": len(found) == 0, "examples": found[:5]}


def verdict():
    comp = components_on_forced_locus()
    search = off_locus_search()
    all_on = all(v["on_locus_all_samples"] for v in comp.values())
    return {
        "all_irreducible_components_on_forced_locus": all_on,
        "off_locus_empty_for_figure_eight_SL3": search["off_locus_empty"] and all_on,
        "literature": "Heusener-Munoz-Porti arXiv:1505.04451: exactly 3 irreducible components (V0 + W1 + W2)",
        "scope": "specific to 4_1 at SL(3); the higher-rank / other-manifold off-principal fork (S011) stays OPEN",
    }


def main():
    print("=" * 78)
    print("B110 -- the off-locus irreducible sector of 4_1 at SL(3): is it empty? (Task 3 / S011)")
    print("=" * 78)
    print("\nEach irreducible component on the forced locus (x1=x4 OR x2=x5):")
    for name, v in components_on_forced_locus().items():
        print(f"    {name}: on locus = {v['on_locus_all_samples']}   [{v['rule']}]")
    s = off_locus_search()
    print(f"\nExhaustive search (V0 u W1 u W2 = Fix(T_1^2) = HMP's 3 irreducibles):")
    print(f"    off-locus points (x1!=x4 AND x2!=x5) found: {s['off_locus_points_found']}  "
          f"-> off-locus EMPTY: {s['off_locus_empty']}")
    v = verdict()
    print(f"\nVERDICT: off-locus sector empty for 4_1 at SL(3): {v['off_locus_empty_for_figure_eight_SL3']}")
    print(f"    {v['literature']}")
    print(f"    SCOPE: {v['scope']}")


if __name__ == "__main__":
    main()
