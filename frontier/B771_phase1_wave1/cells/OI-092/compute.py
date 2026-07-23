"""OI-092 -- B771 Phase-1 Wave-1 closure batch: genus-2 CS numeric re-run.

TARGET (docs/OPEN_LEADS.md:205, "Genus-2 CS numeric (B140 soft spot)"; source
frontier/B140_compute_reconciliation/probe.py, function genus_general_live(), Item 1):

    g2 = snappy.twister.Surface("S_2").bundle("a*B*c*d*E")
    g2.complex_volume()   # <-- previously failed / was recorded as a soft spot (cs_numeric_rendered=False)

B140's load-bearing claim (the general orientation-reversal theorem: mirror M-bar of an oriented
hyperbolic 3-manifold M has SAME volume, OPPOSITE Chern-Simons, conjugate trace field) was banked on
the THEOREM plus genus-1 numeric confirmation; the genus-2 illustration was an honest soft spot because
SnapPy's complex_volume() raised on the raw twister output. This cell diagnoses and re-runs it.

DIAGNOSIS (in-sandbox): the twister bundle is delivered as a Dehn-FILLED triangulation (one torus cusp,
filling (1,0), closing up the mapping torus). snappy.Manifold.chern_simons()'s own docstring states the
exact mechanism: for a closed manifold, chern_simons()/complex_volume() need SnapPea's internal CS
"fudge factor" initialized on the UNFILLED cusped triangulation BEFORE the filling is (re)applied --
skipping that step is exactly what raises `ValueError: The Chern-Simons invariant isn't currently known.`
(confirmed verbatim in-sandbox below). This is a usage/retriangulation issue, not a non-existence of the
invariant -- the manifold IS hyperbolic (solution_type = all tetrahedra positively oriented once a
positively-oriented triangulation is reached).

FIX / RE-RUN PROTOCOL:
  1. copy the manifold, dehn_fill((0,0)) to expose the cusp,
  2. call chern_simons() on the unfilled cusped manifold (initializes SnapPea's CS internals),
  3. dehn_fill back to the original filling,
  4. complex_volume() now succeeds.

TWO INDEPENDENT TRIANGULATIONS (the two seeds, per house method):
  - seed 1: the native twister triangulation (as constructed by Surface.bundle), retriangulated via the
    fix above until a positively-oriented solution is reached (randomize() until solution_type flips, if
    the native one isn't already positive -- recorded either way).
  - seed 2: an independently randomized retriangulation (M.randomize(), a different tetrahedron count),
    same fix applied.
Agreement between the two seeds to double-precision (~1e-10) is the discriminating numeric fact.

MIRROR CHECK: apply the same protocol to the orientation-reversed manifold (reverse_orientation()) at
both seeds, and check volume-same / CS-opposite -- this is the actual banked B140 structural claim,
now confirmed numerically at genus 2 (previously only asserted via the general theorem + existence).

Gate 5/5-Q: structural language only; no SM values; nothing to CLAIMS.md; MATH tier.
Env: pyenv python3 (NOT sage) -- snappy + snappy.twister.
"""
from __future__ import annotations

import cmath
import sys

import snappy
import snappy.twister as twister


TOL = 1e-9  # matches the tolerance already used in B140's own genus-1/knot checks


def raw_attempt_reproduces_the_original_failure():
    """Reproduce the ORIGINAL failure mode exactly, before any fix, as the discriminating fact
    that something was actually broken (not just previously un-run)."""
    g2 = twister.Surface("S_2").bundle("a*B*c*d*E")
    info = {
        "num_tetrahedra": g2.num_tetrahedra(),
        "solution_type": g2.solution_type(),
        "num_cusps": g2.num_cusps(),
        "cusp_filling": g2.cusp_info()[0]["filling"],
    }
    try:
        cv = g2.complex_volume()
        info["raw_complex_volume"] = str(cv)
        info["raw_failed"] = False
    except Exception as e:
        info["raw_error"] = repr(e)
        info["raw_failed"] = True
    return info


def geometrize(M, max_tries=200):
    """Randomize until a positively-oriented (geometric) solution is reached, or give up."""
    M = M.copy()
    if "positively oriented" in M.solution_type():
        return M, 0
    for i in range(max_tries):
        M.randomize()
        if "positively oriented" in M.solution_type():
            return M, i + 1
    return None, max_tries


def cs_initialized_complex_volume(M, filling):
    """The fix: initialize SnapPea's CS internals on the UNFILLED manifold, then refill."""
    M2 = M.copy()
    M2.dehn_fill((0, 0))
    unfilled_solution_type = M2.solution_type()
    cs_unfilled = M2.chern_simons()  # initializes internals; raises if this manifold isn't geometric unfilled
    M2.dehn_fill(filling)
    refilled_solution_type = M2.solution_type()
    cv = M2.complex_volume()
    return {
        "unfilled_solution_type": unfilled_solution_type,
        "cs_unfilled": float(cs_unfilled),
        "refilled_solution_type": refilled_solution_type,
        "complex_volume": complex(cv.real(), cv.imag()) if hasattr(cv, "real") else complex(cv),
        "cv_str": str(cv),
    }


def two_seed_run(word="a*B*c*d*E", label="genus-2 twister bundle"):
    base = twister.Surface("S_2").bundle(word)
    filling = base.cusp_info()[0]["filling"]

    out = {"label": label, "word": word, "filling": tuple(filling)}

    # seed 1: native triangulation, geometrized if necessary (retriangulation only if needed)
    seed1_M, seed1_tries = geometrize(base)
    if seed1_M is None:
        out["seed1"] = {"failed": True, "reason": "no positively-oriented triangulation found"}
    else:
        r1 = cs_initialized_complex_volume(seed1_M, filling)
        r1["num_tetrahedra"] = seed1_M.num_tetrahedra()
        r1["randomize_tries"] = seed1_tries
        out["seed1"] = r1

    # seed 2: independently randomized retriangulation (different tetrahedron count / combinatorics)
    seed2_base = base.copy()
    seed2_base.randomize()
    seed2_M, seed2_tries = geometrize(seed2_base)
    if seed2_M is None:
        out["seed2"] = {"failed": True, "reason": "no positively-oriented triangulation found"}
    else:
        r2 = cs_initialized_complex_volume(seed2_M, filling)
        r2["num_tetrahedra"] = seed2_M.num_tetrahedra()
        r2["randomize_tries"] = seed2_tries
        out["seed2"] = r2

    # cross-seed agreement (the discriminating numeric fact for THIS manifold)
    if not out["seed1"].get("failed") and not out["seed2"].get("failed"):
        cv1, cv2 = out["seed1"]["complex_volume"], out["seed2"]["complex_volume"]
        out["seed_agreement"] = {
            "abs_diff": abs(cv1 - cv2),
            "agree_within_tol": abs(cv1 - cv2) < TOL,
            "tol": TOL,
        }

    # mirror (orientation-reversed) manifold, same two-seed protocol
    mirror = base.copy()
    mirror.reverse_orientation()
    m_seed1_M, m_seed1_tries = geometrize(mirror)
    if m_seed1_M is None:
        out["mirror_seed1"] = {"failed": True}
    else:
        rm1 = cs_initialized_complex_volume(m_seed1_M, filling)
        rm1["num_tetrahedra"] = m_seed1_M.num_tetrahedra()
        out["mirror_seed1"] = rm1

    mirror_seed2_base = mirror.copy()
    mirror_seed2_base.randomize()
    m_seed2_M, m_seed2_tries = geometrize(mirror_seed2_base)
    if m_seed2_M is None:
        out["mirror_seed2"] = {"failed": True}
    else:
        rm2 = cs_initialized_complex_volume(m_seed2_M, filling)
        rm2["num_tetrahedra"] = m_seed2_M.num_tetrahedra()
        out["mirror_seed2"] = rm2

    if not out["mirror_seed1"].get("failed") and not out["mirror_seed2"].get("failed"):
        cv1, cv2 = out["mirror_seed1"]["complex_volume"], out["mirror_seed2"]["complex_volume"]
        out["mirror_seed_agreement"] = {
            "abs_diff": abs(cv1 - cv2),
            "agree_within_tol": abs(cv1 - cv2) < TOL,
        }

    # the actual B140 structural claim: vol(M) == vol(Mbar), CS(M) == -CS(Mbar)
    if not out["seed1"].get("failed") and not out["mirror_seed1"].get("failed"):
        cv = out["seed1"]["complex_volume"]
        cvm = out["mirror_seed1"]["complex_volume"]
        out["orientation_reversal_check"] = {
            "M_complex_volume": cv,
            "Mbar_complex_volume": cvm,
            "vol_abs_diff": abs(cv.real - cvm.real),
            "vol_equal_within_tol": abs(cv.real - cvm.real) < TOL,
            "cs_sum": cv.imag + cvm.imag,
            "cs_opposite_within_tol": abs(cv.imag + cvm.imag) < TOL,
            "cs_nonzero_chiral": abs(cv.imag) > TOL,
        }

    return out


def symmetry_group_chirality(word="a*B*c*d*E"):
    g2 = twister.Surface("S_2").bundle(word)
    sg = g2.symmetry_group()
    is_full = sg.is_full_group()
    amph = sg.is_amphicheiral() if is_full else None
    return {"is_full_group": is_full, "is_amphicheiral": amph, "symmetry_group_str": str(sg)}


def main():
    print("=" * 110)
    print("OI-092 -- genus-2 twister complex_volume re-run (B771 Phase-1 Wave-1)")
    print("snappy version:", snappy.version() if hasattr(snappy, "version") else "?")
    print("python:", sys.version)
    print("=" * 110)

    print("\n[Step 0] Reproduce the original failure verbatim (before any fix)")
    raw = raw_attempt_reproduces_the_original_failure()
    for k, v in raw.items():
        print(f"    {k}: {v}")

    print("\n[Step 1] Chirality check (symmetry group) -- confirms this genus-2 example is chiral")
    chir = symmetry_group_chirality()
    for k, v in chir.items():
        print(f"    {k}: {v}")

    print("\n[Step 2] Two-seed re-run with the CS-initialization fix (unfill -> chern_simons() -> refill)")
    res = two_seed_run()
    print(f"    word: {res['word']}, filling: {res['filling']}")

    for tag in ("seed1", "seed2"):
        r = res[tag]
        if r.get("failed"):
            print(f"    {tag}: FAILED -- {r.get('reason')}")
        else:
            print(f"    {tag}: num_tet={r['num_tetrahedra']} randomize_tries={r['randomize_tries']}")
            print(f"        unfilled_solution_type = {r['unfilled_solution_type']}")
            print(f"        cs_unfilled (init)     = {r['cs_unfilled']}")
            print(f"        refilled_solution_type = {r['refilled_solution_type']}")
            print(f"        complex_volume         = {r['cv_str']}")

    if "seed_agreement" in res:
        sa = res["seed_agreement"]
        print(f"    seed1 vs seed2 |diff| = {sa['abs_diff']:.3e}  (tol {sa['tol']:.0e})  agree: {sa['agree_within_tol']}")

    print("\n[Step 3] Mirror manifold, same two-seed protocol")
    for tag in ("mirror_seed1", "mirror_seed2"):
        r = res[tag]
        if r.get("failed"):
            print(f"    {tag}: FAILED")
        else:
            print(f"    {tag}: num_tet={r['num_tetrahedra']}  complex_volume = {r['cv_str']}")
    if "mirror_seed_agreement" in res:
        ma = res["mirror_seed_agreement"]
        print(f"    mirror seed1 vs seed2 |diff| = {ma['abs_diff']:.3e}  agree: {ma['agree_within_tol']}")

    print("\n[Step 4] Orientation-reversal structural check (the B140 claim, now numeric at genus 2)")
    if "orientation_reversal_check" in res:
        c = res["orientation_reversal_check"]
        print(f"    M    complex_volume = {c['M_complex_volume']}")
        print(f"    Mbar complex_volume = {c['Mbar_complex_volume']}")
        print(f"    |vol(M) - vol(Mbar)| = {c['vol_abs_diff']:.3e}   vol_equal (tol {TOL:.0e}): {c['vol_equal_within_tol']}")
        print(f"    CS(M) + CS(Mbar)     = {c['cs_sum']:.3e}   cs_opposite (tol {TOL:.0e}): {c['cs_opposite_within_tol']}")
        print(f"    CS(M) nonzero (chiral, consistent with Step 1): {c['cs_nonzero_chiral']}")

        all_pass = (
            c["vol_equal_within_tol"]
            and c["cs_opposite_within_tol"]
            and c["cs_nonzero_chiral"]
            and chir["is_amphicheiral"] is False
            and res.get("seed_agreement", {}).get("agree_within_tol", False)
            and res.get("mirror_seed_agreement", {}).get("agree_within_tol", False)
        )
        print(f"\n    ALL CHECKS PASS: {all_pass}")
    else:
        print("    FAILED to compute -- see seed1/mirror_seed1 failure reasons above.")
        all_pass = False

    print("\n" + "=" * 110)
    print("VERDICT INPUTS:")
    print(f"    raw_call_failed_as_recorded: {raw.get('raw_failed')}")
    print(f"    fix_resolves_and_confirms_banked_structure: {all_pass}")
    print("=" * 110)


if __name__ == "__main__":
    main()
