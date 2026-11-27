"""Failing control for Card A2-P629-VEFF-MODULUS (P-885 mechanical intake, 0 of 19).

Imports the sibling decisive module `a2_p629_veff_modulus_decisive` and verifies:
  (a) Unperturbed baseline checks PASS (confirming the harness works);
  (b) Four deliberate mathematical falsifications FAIL the decisive predicates cleanly:
      1. Dropping the non-holomorphic -3/(pi y) term from E2_hat breaks SL(2,Z) S-invariance;
      2. Replacing critical SUGRA n = 3 with subcritical n = 1 in V_{FILQ,n} + 70 V_CW(1) at 1/2 + 4i
         restores exponential cusp runaway (V < -1e9 instead of cusp wall > 4e9);
      3. Testing Re(tau) = 0 instead of Re(tau) = 1/2 at y* = 3.380451106 yields a saddle
         (V_xx(0, y*) < 0 instead of local minimum V_xx > 0);
      4. Perturbing the Branco/CE UV D-term l4_D -> l4_D / 2 breaks exact UV D-flat saturation
         (l3_D + l4_D + sqrt(l1_D l2_D) != 0) and perturbing the 2-loop Type-II hypercharge
         coefficient -41/240 -> -29/240 breaks the primary arXiv:1503.08216 benchmark (> 1e-10).

Exit codes (P-885 / rerun.py):
  1  control FAILS as it must (baseline passed, deliberate mathematical falsifications failed cleanly
     with zero traceback on stderr);
  0  control did NOT fail (decisive predicates survived the mathematical falsifications);
  3  control INVALID (unexpected exception, AST float/complex literal, or baseline failure).
"""

import ast
import os
import pathlib
import sys
import traceback


def _crash_handler(et, ev, tb):
    traceback.print_exception(et, ev, tb)
    print("CONTROL INVALID: unexpected exception; a crash is not a failing control")
    sys.stdout.flush()
    os._exit(3)


sys.excepthook = _crash_handler
sys.dont_write_bytecode = True

import mpmath as mp
import a2_p629_veff_modulus_decisive as prod


def _check_ast_clean(path: pathlib.Path) -> bool:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)):
            return False
    return True


def main() -> int:
    if not _check_ast_clean(pathlib.Path(__file__).resolve()):
        print("CONTROL INVALID: float or complex literal in control script")
        return 3

    mp.mp.dps = 40
    I = prod.iu()
    pairs288 = prod.build_E288_pairs()
    tau_gen = mp.mpc(prod.mp_rat(3, 10), prod.mp_rat(13, 10))
    tau_cusp = mp.mpc(prod.mp_rat(1, 2), mp.mpf(4))
    y_star = prod.mp_rat(3380451106, 1000000000)
    h_2d = prod.mp_rat(1, 50)

    # (a) Unperturbed baseline checks MUST PASS
    v_ok_0 = prod.V_FILQ(tau_gen, 1, dps=40, drop_nonhol=False)
    v_ok_S = prod.V_FILQ(-1 / tau_gen, 1, dps=40, drop_nonhol=False)
    base_s_err = abs(v_ok_S - v_ok_0) / max(mp.mpf(1), abs(v_ok_0))

    fv_cusp = prod.eval_all288_fermion_pot(tau_cusp, pairs288, dps_use=24)
    base_wall_n3 = prod.V_FILQ(tau_cusp, 3, dps=32) + 70 * fv_cusp["VCW_1"]

    g_uv = prod.mp_rat(1, 2)
    g12, g22 = g_uv * g_uv, g_uv * g_uv
    gy2 = prod.mp_rat(3, 5) * g12
    l1_ok = (g22 + gy2) / 4
    l2_ok = l1_ok
    l3_ok = (g22 - gy2) / 4
    l4_ok = -g22 / 2
    base_dflat_err = abs(l3_ok + l4_ok + mp.sqrt(l1_ok * l2_ok))

    if not (base_s_err < prod.mp_pow10(-32) and base_wall_n3 > mp.mpf(4 * (10 ** 9)) and base_dflat_err < prod.mp_pow10(-38)):
        print(
            "CONTROL INVALID: unperturbed baseline failed "
            f"(s_err={prod.mp_str(base_s_err, 6)}, wall_n3={prod.mp_str(base_wall_n3, 8)}, dflat={prod.mp_str(base_dflat_err, 6)})"
        )
        return 3

    # (b1) Deliberate falsification 1: drop non-holomorphic -3/(pi y) term from E2_hat
    v_bad_0 = prod.V_FILQ(tau_gen, 1, dps=40, drop_nonhol=True)
    v_bad_S = prod.V_FILQ(-1 / tau_gen, 1, dps=40, drop_nonhol=True)
    bad_s_err = abs(v_bad_S - v_bad_0) / max(mp.mpf(1), abs(v_bad_0))
    c1_fails = bad_s_err > prod.mp_rat(1, 10)

    # (b2) Deliberate falsification 2: subcritical n = 1 instead of n = 3 restores cusp runaway
    bad_wall_n1 = prod.V_FILQ(tau_cusp, 1, dps=32) + 70 * fv_cusp["VCW_1"]
    c2_fails = bad_wall_n1 < mp.mpf(-10 ** 9)

    # (b3) Deliberate falsification 3: test x = 0 instead of x = 1/2 at y* = 3.380451106 (saddle V_xx < 0)
    def eval_vtot70(t_in):
        fv = prod.eval_all288_fermion_pot(t_in, pairs288, dps_use=28)
        return prod.V_FILQ(t_in, 3, dps=32) + 70 * fv["VCW_1"]

    v0_c = eval_vtot70(mp.mpc(0, y_star))
    v0_xp = eval_vtot70(mp.mpc(h_2d, y_star))
    vxx_zero = (2 * v0_xp - 2 * v0_c) / (h_2d * h_2d)
    c3_fails = vxx_zero < mp.mpf(-100)

    # (b4) Deliberate falsification 4: corrupt UV D-term l4_D -> l4_D / 2 (breaks UV D-flat saturation == 0)
    #      and test corrupted -29/240 (instead of primary arXiv:1503.08216 -41/240) directly against prod.rhs_coupled_2hdm_soft
    l4_bad = -g22 / 4
    bad_dflat_err = abs(l3_ok + l4_bad + mp.sqrt(l1_ok * l2_ok))

    yt_v, yb_v, ytau_v = prod.mp_rat(9, 10), prod.mp_rat(4, 10), prod.mp_rat(2, 10)
    g1_v, g2_v, g3_v = prod.mp_rat(45, 100), prod.mp_rat(65, 100), prod.mp_rat(11, 10)
    l1_v, l2_v, l3_v, l4_v = prod.mp_rat(1, 10), prod.mp_rat(15, 100), prod.mp_rat(5, 100), prod.mp_rat(-3, 100)
    out_b = prod.rhs_coupled_2hdm_soft(
        g1_v, g2_v, g3_v,
        mp.diag([0, 0, yt_v]), mp.diag([0, 0, yb_v]), mp.diag([0, 0, ytau_v]),
        l1_v, l2_v, l3_v, l4_v,
        prod.mp_rat(7, 10), prod.mp_rat(9, 10),
        mp.diag([0, 0, prod.mp_rat(11, 10)]), mp.diag([0, 0, prod.mp_rat(13, 10)]),
        mp.diag([0, 0, prod.mp_rat(15, 10)]), mp.diag([0, 0, prod.mp_rat(17, 10)]),
        mp.diag([0, 0, prod.mp_rat(19, 10)]),
    )
    inv1 = 1 / (16 * (mp.pi ** 2))
    inv2 = inv1 * inv1
    gy2_v = prod.mp_rat(3, 5) * (g1_v ** 2)
    b1_yt = yt_v * (prod.mp_rat(9, 2) * yt_v ** 2 + prod.mp_rat(1, 2) * yb_v ** 2 - prod.mp_rat(17, 12) * gy2_v - prod.mp_rat(9, 4) * g2_v ** 2 - 8 * g3_v ** 2)
    b2_yt_corrupted = yt_v * (
        -12 * yt_v ** 4 - prod.mp_rat(5, 2) * yt_v ** 2 * yb_v ** 2 - prod.mp_rat(5, 2) * yb_v ** 4 - prod.mp_rat(3, 4) * yb_v ** 2 * ytau_v ** 2
        + (prod.mp_rat(131, 16) * gy2_v + prod.mp_rat(225, 16) * g2_v ** 2 + 36 * g3_v ** 2) * yt_v ** 2
        + (-prod.mp_rat(29, 144) * gy2_v + prod.mp_rat(33, 16) * g2_v ** 2 + prod.mp_rat(16, 3) * g3_v ** 2) * yb_v ** 2
        + prod.mp_rat(1267, 216) * gy2_v ** 2 - prod.mp_rat(3, 4) * gy2_v * g2_v ** 2 + prod.mp_rat(19, 9) * gy2_v * g3_v ** 2
        - prod.mp_rat(21, 4) * g2_v ** 4 + 9 * g2_v ** 2 * g3_v ** 2 - 108 * g3_v ** 4
        - 6 * l2_v * yt_v ** 2 + (-2 * l3_v + 2 * l4_v) * yb_v ** 2
        + prod.mp_rat(3, 2) * l2_v ** 2 + l3_v ** 2 + l3_v * l4_v + l4_v ** 2
    )
    bad_ce_err = abs(out_b[3][2, 2] - (inv1 * b1_yt + inv2 * b2_yt_corrupted))
    c4_fails = (bad_dflat_err > prod.mp_rat(1, 20)) and (bad_ce_err > prod.mp_pow10(-10))

    print(
        "CONTROL SUMMARY: baseline_ok=True "
        f"c1_nonhol_S_err={prod.mp_str(bad_s_err, 6)} "
        f"c2_n1_cusp_4i={prod.mp_str(bad_wall_n1, 8)} "
        f"c3_Vxx_zero={prod.mp_str(vxx_zero, 6)} "
        f"c4_dflat_err={prod.mp_str(bad_dflat_err, 6)} "
        f"c4_ce_err={prod.mp_str(bad_ce_err, 6)}"
    )

    if c1_fails and c2_fails and c3_fails and c4_fails:
        print(
            "CONTROL FAILS: as required, all four deliberate mathematical falsifications "
            "(holomorphic E2, subcritical n=1, x=0 saddle, and corrupted D-term/2-loop coefficients) "
            "violate the decisive claim predicates cleanly."
        )
        return 1

    print("CONTROL DID NOT FAIL: one or more falsifications failed to trip the decisive claim predicates")
    return 0


if __name__ == "__main__":
    sys.exit(main())
