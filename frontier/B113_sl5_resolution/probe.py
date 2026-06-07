"""B113 -- the proved closed form RESOLVES the SL(5) sign sectors the eps-series could not (and localizes degree=rank).

The B112-proved opposition-involution closed form (mult char(M^h)=ceil((n-h)/2), char(-M^h)=floor((n-h)/2)) is
applied to n=5 and compared to the repo's SL(5) tower (B61: 22/24 resolved by the eps-series; B62: the 2
unresolved completed structurally as a second char(M^2)).

TWO findings:

  (1) WIN -- the closed form RESOLVES SL(5) above height 1. At heights 2,3,4 the proved closed form MATCHES the
      SL(5) tower EXACTLY, including the height-2 sector char(M^2)^2 . char(-M^2) -- i.e. it PREDICTS B62's two
      gauge-corrupted modes (the eps-series pinv could only resolve 22/24; B62 had to supply the last 2 by the
      opposition involution at height 2). B112 now supplies ALL heights structurally, so the SL(5) sign sectors
      are determined by a PROOF, not by the gauge-fragile numerics.

  (2) LOCALIZATION -- degree=rank touches only height 1 and the top power. The only place the closed form differs
      from the tower is HEIGHT 1 (closed (M:2,-M:2) vs tower (M:2,-M:1)) plus the extra char(M^5) (the longitude,
      L=c*M^5). So heights 2..n-1 are PURE bulk-theta (proved); degree=rank is confined to the height-1 / top-power
      interface. Moreover the promotion at n=5 consumes a char(-M^1), whereas at n=3,4 it consumed a char(+M^1):
      the degree=rank promotion is NOT a uniform char(M)->char(M^n) rule -- the power half is n-dependent and stays
      the genuinely-hard open piece (S022).

Standalone trace-map / Lie theory; NO physics; no CLAIMS.md promotion; the rho_n proof stays the prize; P1-P16
untouched.
"""
from __future__ import annotations

import importlib.util
import math
import pathlib
import sys

_ROOT = pathlib.Path(__file__).resolve().parents[2]


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, _ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


_B112 = _load("b113_b112", "frontier/B112_closed_form_proof/probe.py")


# The repo's SL(5) tower (B61 22/24 resolved + B62 structural for the 2), as (sign, height) -> mult, with
# char(M^-1) folded to char(-M^1) (det=-1 identity). Heights of |k|=1..5; the parity is (t-1)^2 (t+1)^2.
#   char(M^-1) char(M)^2 char(M^2)^2 char(M^3) char(M^4) char(M^5) char(-M^2) char(-M^3)
_SL5_TOWER = {("+", 1): 2, ("-", 1): 1, ("+", 2): 2, ("-", 2): 1,
              ("+", 3): 1, ("-", 3): 1, ("+", 4): 1, ("+", 5): 1}
_TOP_POWER = 5   # char(M^n) = char(M^5), the degree=rank longitude


def closed_form_vs_sl5():
    """Per-height comparison of the B112 closed form (bulk theta) against the SL(5) tower. Heights 2..4 match
    exactly (incl. B62's char(M^2)^2); height 1 differs by the degree=rank promotion."""
    rows = {}
    for h in range(1, 5):
        cf = _B112.closed_form(5, h)                 # (char(M^h), char(-M^h))
        tw = (_SL5_TOWER.get(("+", h), 0), _SL5_TOWER.get(("-", h), 0))
        rows[h] = {"closed_form": cf, "sl5_tower": tw, "match": cf == tw}
    return rows


def b62_modes_resolved():
    """The closed form predicts the height-2 sector char(M^2)^2 . char(-M^2) -- B62's two gauge-corrupted SL(5)
    modes (the 23rd/24th that the eps-series pinv could not resolve)."""
    cf_h2 = _B112.closed_form(5, 2)                   # should be (2, 1)
    tower_h2 = (_SL5_TOWER[("+", 2)], _SL5_TOWER[("-", 2)])
    return {"closed_form_h2": cf_h2, "sl5_tower_h2": tower_h2,
            "predicts_second_char_M2": cf_h2 == (2, 1) == tower_h2,
            "note": "char(M^2)^2 . char(-M^2): the closed form supplies B62's 2 gauge-corrupted modes by proof"}


def degree_rank_localization():
    """Heights 2..n-1 are pure bulk-theta (closed form); degree=rank is confined to height-1 + char(M^n)."""
    rows = closed_form_vs_sl5()
    heights_2_to_4_match = all(rows[h]["match"] for h in (2, 3, 4))
    h1 = rows[1]
    return {"heights_2_to_nminus1_pure_bulk_theta": heights_2_to_4_match,
            "height1_differs": not h1["match"],
            "degree_rank_confined_to": "height 1 + the top power char(M^5) (the longitude)",
            "top_power_present_in_tower": ("+", _TOP_POWER) in _SL5_TOWER,
            "promotion_consumes_at_n5": "char(-M^1)",      # n=5: closed -M:2 -> tower -M:1
            "promotion_consumes_at_n34": "char(+M^1)",     # n=3,4: closed +M excess
            "promotion_is_uniform": False,
            "note": "the degree=rank promotion is n-dependent (consumes -M at n=5, +M at n=3,4) -- the power half "
                    "stays the genuinely-hard open piece (S022)"}


def main():
    print("=" * 78)
    print("B113 -- the proved closed form (B112) resolves the SL(5) sign sectors + localizes degree=rank")
    print("=" * 78)
    print("\n[per-height] B112 closed form vs the SL(5) tower (B61 + B62):")
    for h, r in closed_form_vs_sl5().items():
        tag = "MATCH" if r["match"] else "differs (the promotion / degree=rank)"
        print(f"    h={h}: closed {r['closed_form']}  SL5 {r['sl5_tower']}  -> {tag}")
    print("\n[WIN] the closed form resolves B62's 2 gauge-corrupted modes:")
    b = b62_modes_resolved()
    print(f"    height-2: closed {b['closed_form_h2']} == SL5 {b['sl5_tower_h2']} == char(M^2)^2.char(-M^2): "
          f"{b['predicts_second_char_M2']}")
    print(f"    {b['note']}")
    print("\n[LOCALIZATION] degree=rank is confined to height 1 + the top power:")
    d = degree_rank_localization()
    print(f"    heights 2..n-1 pure bulk-theta (proved): {d['heights_2_to_nminus1_pure_bulk_theta']}")
    print(f"    degree=rank confined to: {d['degree_rank_confined_to']}")
    print(f"    the promotion is n-dependent (consumes {d['promotion_consumes_at_n5']} at n=5, "
          f"{d['promotion_consumes_at_n34']} at n=3,4) -> uniform: {d['promotion_is_uniform']}")
    print("\nVERDICT: the proved closed form determines the SL(5) sign sectors at heights 2,3,4 by proof (resolving")
    print("the gauge-corrupted eps-series modes); degree=rank is localized to height-1 + char(M^n); the promotion")
    print("rule (the power half) is n-dependent and stays open (S022). NO physics.")


if __name__ == "__main__":
    main()
