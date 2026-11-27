"""Failing control for Card A2-LEG5-TOWER-MODULAR-BRIDGE (P-885 mechanical intake, 0 of 19).

Imports the sibling decisive module `a2_leg5_tower_modular_bridge_decisive` and verifies:
  (a) Unperturbed baseline checks PASS (confirming the harness works);
  (b) Four deliberate mathematical falsifications FAIL the decisive claim predicates cleanly:
      1. Replacing Leg(5) quadratic signs with trivial P^1(F_5) signs destroys the golden kernel
         ker(W6^2 - 3 W6 + I) (dim 0 instead of 4);
      2. Swapping R <-> R^-1 inside the chiral walk W_L breaks [W_L, W_R] = 0 on Leg(5);
      3. Testing the Re(tau) = 0 reflection R_0 instead of Re(tau) = +1/2 reflection R_{+1/2}
         breaks [M, W_6] = 0 and gives a saddle (I4_xx < 0) at y* = 2.27277 instead of a local minimum;
      4. Dropping the weight-2 factor (c tau + d)^2 in Phi^{wp}(-1/tau) breaks S-equivariance (> 0.5).

Exit codes (P-885 / rerun.py):
  1  control FAILS as it must (baseline passed, all four deliberate falsifications violated the
     decisive predicates cleanly with zero traceback on stderr);
  0  control did NOT fail;
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
import sympy as sp
import a2_leg5_tower_modular_bridge_decisive as prod


def _ast_clean(path: pathlib.Path) -> bool:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)):
            return False
    return True


def main() -> int:
    if not _ast_clean(pathlib.Path(__file__).resolve()):
        print("CONTROL INVALID: float or complex literal in control script")
        return 3

    mp.mp.dps = 38
    WL, WR, W6, C3M, TM = prod.build_leg5_operators(trivial_signs=False)
    MS = prod.leg5_sp_mat(prod.S_STD)
    MS_mp = prod.sp_mat_to_mp(MS, dps=38)

    # (a) Unperturbed baseline MUST PASS
    base_gold_dim = len((W6 * W6 - 3 * W6 + sp.eye(6)).nullspace())
    base_comm_ok = (WL * WR - WR * WL) == sp.zeros(6, 6)
    M_half = sp.simplify(MS * prod.leg5_sp_mat(((1, 0), (-1, -1))) * MS.inv())
    base_lock_ok = sp.simplify(M_half * W6 - W6 * M_half) == sp.zeros(6, 6)
    tau0 = mp.mpc(prod.mp_rat(3, 10), prod.mp_rat(13, 10))
    w0 = prod.phi_wp_col(tau0, MS_mp, dps=38)
    wS = prod.phi_wp_col(-1 / tau0, MS_mp, dps=38)
    base_wp_err = max(abs((wS - (tau0 ** 2) * MS_mp * w0)[i]) for i in range(6)) / max(abs(x) for x in wS)

    if not (base_gold_dim == 4 and base_comm_ok and base_lock_ok and base_wp_err < prod.mp_pow10(-30)):
        print("CONTROL INVALID: unperturbed baseline failed")
        return 3

    # (b1) Trivial P^1(F_5) signs kill golden kernel
    _, _, W6_triv, _, _ = prod.build_leg5_operators(trivial_signs=True)
    bad_gold_dim = len((W6_triv * W6_triv - 3 * W6_triv + sp.eye(6)).nullspace())
    c1_fails = bad_gold_dim == 0

    # (b2) Swapped R <-> R^-1 chiral walk breaks [W_L, W_R] = 0
    P3 = prod.mat2_mul(prod.C_OM, prod.mat2_mul(prod.mat2_inv(prod.R2), prod.mat2_inv(prod.C_OM)))
    WL_bad = prod.leg5_sp_mat(prod.L2) + prod.leg5_sp_mat(prod.R2) + prod.leg5_sp_mat(P3)
    WR_bad = W6 - WL_bad
    c2_fails = (WL_bad * WR_bad - WR_bad * WL_bad) != sp.zeros(6, 6)

    # (b3) Re(tau) = 0 reflection R_0 breaks [M, W_6] = 0 and gives saddle I4_xx(0, y*) < 0
    M_zero = sp.simplify(MS * prod.leg5_sp_mat(((1, 0), (0, -1))) * MS.inv())
    r0_breaks_w6 = sp.simplify(M_zero * W6 - W6 * M_zero) != sp.zeros(6, 6)
    y0 = prod.mp_rat(227277316, 100000000)
    hh = prod.mp_pow10(-4)
    f0 = prod.I4_I6_vec(prod.phi_siegel_col(mp.mpc(0, y0), MS_mp, dps=36))[0]
    fp = prod.I4_I6_vec(prod.phi_siegel_col(mp.mpc(hh, y0), MS_mp, dps=36))[0]
    fm = prod.I4_I6_vec(prod.phi_siegel_col(mp.mpc(-hh, y0), MS_mp, dps=36))[0]
    i4_xx_zero = (fp - 2 * f0 + fm) / (hh * hh)
    c3_fails = r0_breaks_w6 and (i4_xx_zero < -prod.mp_pow10(-5))

    # (b4) Dropping weight-2 factor breaks S-equivariance of Phi^{wp}
    bad_wp_err = max(abs((wS - MS_mp * w0)[i]) for i in range(6)) / max(abs(x) for x in wS)
    c4_fails = bad_wp_err > prod.mp_rat(1, 2)

    print(
        f"CONTROL SUMMARY: baseline_ok=True bad_gold_dim={bad_gold_dim} "
        f"swapped_comm_nonzero={c2_fails} r0_breaks_w6={r0_breaks_w6} "
        f"I4_xx_zero={prod.mp_str(i4_xx_zero, 6)} drop_wt2_err={prod.mp_str(bad_wp_err, 6)}"
    )

    if c1_fails and c2_fails and c3_fails and c4_fails:
        print(
            "CONTROL FAILS: as required, all four deliberate mathematical falsifications "
            "(trivial signs, swapped chiral walk, Re(tau)=0 reflection/saddle, and dropped weight-2 factor) "
            "violate the decisive claim predicates cleanly."
        )
        return 1

    print("CONTROL DID NOT FAIL: one or more falsifications survived the decisive predicates")
    return 0


if __name__ == "__main__":
    sys.exit(main())
