#!/usr/bin/env python3
"""T2_cp_bit — object-side computation of the CP bit (L192).

Computes Chern-Simons for m004, m003 (the discriminating amphichiral pair),
m208 (the chiral CS=0 control), and ~10 chiral orientable census controls.

CONVENTIONS (stated per E23 discipline):
- Orientation: SnapPy census orientation as loaded by Manifold(name); no
  reorientation applied. CS is orientation-odd (CS(-M) = -CS(M)); the 2-torsion
  classes {0, 1/4} are orientation-invariant, so the BIT is orientation-free.
- CS normalization: SnapPy's Manifold.chern_simons(), the Riemannian
  Chern-Simons invariant cs(M) normalized so that it is defined modulo 1/2
  for orientable cusped manifolds (value group R/(1/2)Z). This matches the
  repo's B1224 convention: 2-torsion elements of R/(1/2)Z are exactly {0, 1/4}.
- Representative interval: values reduced to [0, 1/2).
- Amphichirality test: symmetry_group().is_amphicheiral() (the authoritative
  call per B1226's methodological catch; is_isometric_to(mirror) is NOT a
  chirality test).
- Precision: standard (double) and high precision (Manifold with
  high_precision via verify/extended) cross-checked where available; we use
  chern_simons() on both the plain Manifold and its high-precision copy.

BIT-READING PROCEDURE (the object-side output):
  Input: an amphichiral cusped orientable hyperbolic manifold M.
  Step 1: verify amphichirality (forces 2-torsion: CS in {0, 1/4} mod 1/2).
  Step 2: compute cs = CS(M) mod 1/2, reduced to [0, 1/2).
  Step 3: if |cs - 0| < TOL       -> bit = CP-EVEN  (the identity of Z/2)
          if |cs - 1/4| < TOL     -> bit = CP-ODD   (the non-identity element)
          otherwise               -> NOT-2-TORSION  (contradiction with Step 1;
                                     the reading FAILS -> DEGRADED)
  For a NON-amphichiral manifold the bit is NOT DEFINED (2-torsion not forced);
  the procedure outputs UNDEFINED-CHIRAL. This is deliberate: m208 has CS = 0
  but chiral, so CS=0 alone does not make an object CP-even in the forced
  sense; the bit is the element of a symmetry-given Z/2, which only exists
  when the symmetry does.

MB12: the procedure can output either element (m004 -> CP-EVEN must hold,
m003 -> CP-ODD must hold as the bite control), and it can fail (NOT-2-TORSION
if numerics landed elsewhere; UNDEFINED-CHIRAL for the controls).

Gate 5: no measured Standard Model value appears anywhere in this script.
"""
import json
import sys

import snappy

TOL = 1e-6  # separation scale: |0 - 1/4| = 0.25, tolerance 6 orders below

AMPHICHIRAL_EXHIBITS = ["m004", "m003", "m136", "m135", "m206", "m207"]
CHIRAL_CS0_CONTROL = "m208"
# ~10 chiral orientable census controls (first orientable census entries,
# skipping the known amphichiral exhibits and m208):
CHIRAL_CONTROLS = ["m006", "m007", "m009", "m010", "m011", "m015",
                   "m016", "m017", "m019", "m022", "m023", "m026"]


def reduce_mod_half(x):
    """Reduce to the representative interval [0, 1/2) of R/(1/2)Z."""
    r = x % 0.5
    if r >= 0.5 - TOL:  # wrap values numerically at ~0.5 back to 0
        r -= 0.5
    return abs(r) if abs(r) < TOL else r


def cs_both_precisions(name):
    M = snappy.Manifold(name)
    cs_std = float(M.chern_simons())
    try:
        Mh = M.high_precision()
        cs_hp = float(Mh.chern_simons())
    except Exception as e:
        cs_hp = None
    return M, cs_std, cs_hp


def is_amphichiral(M):
    return bool(M.symmetry_group().is_amphicheiral())


def read_bit(name):
    """The bit-reading procedure. Returns a dict with all intermediate data."""
    M, cs_std, cs_hp = cs_both_precisions(name)
    amph = is_amphichiral(M)
    r = reduce_mod_half(cs_std)
    r_hp = reduce_mod_half(cs_hp) if cs_hp is not None else None
    if r_hp is not None and abs(r - r_hp) > TOL:
        precision_agree = False
    else:
        precision_agree = True

    if not amph:
        bit = "UNDEFINED-CHIRAL"
    elif abs(r) < TOL:
        bit = "CP-EVEN"
    elif abs(r - 0.25) < TOL:
        bit = "CP-ODD"
    else:
        bit = "NOT-2-TORSION"

    return {
        "manifold": name,
        "cs_raw_std": cs_std,
        "cs_raw_hp": cs_hp,
        "cs_mod_half": r,
        "cs_mod_half_hp": r_hp,
        "precision_agree": precision_agree,
        "amphichiral": amph,
        "bit": bit,
    }


def main():
    results = {"convention": "SnapPy chern_simons(), value group R/(1/2)Z, "
                             "representatives in [0,1/2), TOL=%g" % TOL,
               "exhibits": [], "chiral_cs0_control": None,
               "chiral_controls": [], "checks": {}}

    print("=== Amphichiral exhibits (bit defined) ===")
    for name in AMPHICHIRAL_EXHIBITS:
        row = read_bit(name)
        results["exhibits"].append(row)
        print(f"{name}: CS={row['cs_raw_std']:+.9f} -> mod 1/2 = "
              f"{row['cs_mod_half']:.9f}  amph={row['amphichiral']}  "
              f"bit={row['bit']}  (hp agree: {row['precision_agree']})")

    print("\n=== Chiral CS=0 control (bit must be UNDEFINED-CHIRAL) ===")
    row = read_bit(CHIRAL_CS0_CONTROL)
    results["chiral_cs0_control"] = row
    print(f"{CHIRAL_CS0_CONTROL}: CS={row['cs_raw_std']:+.9f} -> mod 1/2 = "
          f"{row['cs_mod_half']:.9f}  amph={row['amphichiral']}  bit={row['bit']}")

    print("\n=== Chiral controls (generic CS not in {0, 1/4}) ===")
    n_in_torsion = 0
    for name in CHIRAL_CONTROLS:
        row = read_bit(name)
        results["chiral_controls"].append(row)
        in_t = (abs(row["cs_mod_half"]) < TOL
                or abs(row["cs_mod_half"] - 0.25) < TOL)
        n_in_torsion += in_t
        print(f"{name}: CS={row['cs_raw_std']:+.9f} -> mod 1/2 = "
              f"{row['cs_mod_half']:.9f}  amph={row['amphichiral']}  "
              f"bit={row['bit']}  in{{0,1/4}}={in_t}")

    # ---- The named checks ----
    by_name = {r["manifold"]: r for r in results["exhibits"]}
    checks = results["checks"]
    checks["m004_cp_even"] = by_name["m004"]["bit"] == "CP-EVEN"
    checks["MB12_bite_m003_cp_odd"] = by_name["m003"]["bit"] == "CP-ODD"
    checks["m208_cs_zero"] = abs(results["chiral_cs0_control"]["cs_mod_half"]) < TOL
    checks["m208_chiral_so_bit_undefined"] = (
        results["chiral_cs0_control"]["bit"] == "UNDEFINED-CHIRAL")
    checks["generic_chiral_not_2torsion"] = (
        n_in_torsion <= 1 and len(CHIRAL_CONTROLS) >= 10)
    checks["n_chiral_controls"] = len(CHIRAL_CONTROLS)
    checks["n_chiral_in_torsion"] = n_in_torsion
    checks["all_exhibits_2torsion"] = all(
        r["bit"] in ("CP-EVEN", "CP-ODD") for r in results["exhibits"])
    checks["precision_agreement_everywhere"] = all(
        r["precision_agree"] for r in
        results["exhibits"] + [results["chiral_cs0_control"]]
        + results["chiral_controls"])

    print("\n=== CHECKS ===")
    for k, v in checks.items():
        print(f"  {k}: {v}")

    passed = (checks["m004_cp_even"] and checks["MB12_bite_m003_cp_odd"]
              and checks["m208_cs_zero"]
              and checks["m208_chiral_so_bit_undefined"]
              and checks["generic_chiral_not_2torsion"]
              and checks["all_exhibits_2torsion"])
    results["object_side_bit"] = {
        "m004": by_name["m004"]["bit"],
        "m003": by_name["m003"]["bit"],
    }
    results["verdict_half1"] = "PASS" if passed else "DEGRADED"
    print(f"\nHALF-1 VERDICT: {results['verdict_half1']}")
    print(f"OBJECT-SIDE BIT: m004 = {by_name['m004']['bit']}, "
          f"discriminating sibling m003 = {by_name['m003']['bit']}")

    out = __file__.rsplit("/", 1)[0] + "/results.json"
    with open(out, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nwrote {out}")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
