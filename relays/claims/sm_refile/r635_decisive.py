#!/usr/bin/env python3
"""The decisive lines of the SM seat's P-635 card (the boundary-free classes of H^1(fibre, ad Q8)).

Copies the sealed folder relays/sm_r635/ to a fresh temporary directory, runs its run.py there UNCHANGED with the
repo root as the main-checkout argument (the script reads only the frame's Q8 constants from main's b1656_funcs
module), reads r635_results.json from the copy, and prints the values the claim decides on, each on a line beginning
"DECISIVE: ".
Then it checks them against the claim:
  - the closed torus: H^1 = 0;
  - the punctured fibre: H^1 = 3 with the boundary free; H^1_par = 0 with it held (restriction rank 3);
  - the lines (centre): H^1 = 2, restriction to the boundary rank 0;
  - the family: Jacobian rank 3, tangents rank 3 modulo B^1, zero gradient of kappa, positive-definite Hessian, the
    sampled (kappa + 2)/|s|^2 positive;
  - the monodromy: dim ker(phi* - 1) = 1 by both routes.
Exit 0 when the run completes and every claimed value comes out; 1 otherwise. Nothing is written into the repo.

    python3 relays/claims/sm_refile/r635_decisive.py
Depends on the standard library and sympy (the sealed script), numpy and mpmath (main's module it imports)."""
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile


def repo_root():
    for d in [pathlib.Path(__file__).resolve().parent, *pathlib.Path(__file__).resolve().parents]:
        if (d / "frontier").is_dir() and (d / "GENESIS.md").is_file():
            return d
    return None


def run_sealed(main_root):
    """(results dict or None, message): the sealed script run in a temp copy, against `main_root`"""
    root = repo_root()
    if root is None:
        return None, "the repo root (frontier/ and GENESIS.md) was not found"
    sealed = root / "relays" / "sm_r635"
    tmp = tempfile.mkdtemp(prefix="r635_")
    try:
        work = pathlib.Path(tmp) / "sm_r635"
        shutil.copytree(sealed, work)
        for f in ("r635_results.json", "r635_run.txt"):
            if (work / f).exists():
                (work / f).unlink()
        env = dict(os.environ, OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1")
        r = subprocess.run([sys.executable, "-B", str(work / "run.py"), str(main_root), "run"], cwd=str(work),
                           capture_output=True, text=True, env=env)
        if r.returncode != 0 or not (work / "r635_results.json").exists():
            return None, "the sealed run did not complete (exit %d)" % r.returncode
        return json.loads((work / "r635_results.json").read_text(encoding="utf-8")), "ok"
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def decisive(R):
    """(lines, holds): the decisive values and whether each claimed value comes out"""
    f1, f23, f4, f5 = R["F1_closed_torus"], R["F2_F3_punctured"], R["F4_per_character"], R["F5_centre_lines"]
    f6, fx, ft = R["F6_family"], R["F7_monodromy_fox"], R["F7_monodromy_traces"]
    import sympy as sp
    hess_pd = bool(sp.Matrix(sp.sympify(f6["kappa_hessian"])).is_positive_definite)
    grad0 = all(g == "0" for g in f6["kappa_grad_at_0"])
    smin = f6["sample_min_kappa_plus_2_over_s2"]
    vals = [
        ("closed torus H1", f1["H1"], f1["H1"] == 0),
        ("punctured fibre, boundary free H1", f23["H1"], f23["H1"] == 3),
        ("punctured fibre, boundary held H1_par", f23["H1_par"], f23["H1_par"] == 0),
        ("restriction to the boundary loop, rank", f23["restriction_rank"], f23["restriction_rank"] == 3),
        ("per axis character H1 free (I, J, K)", [f4[k]["H1_free"] for k in "IJK"],
         [f4[k]["H1_free"] for k in "IJK"] == [1, 1, 1]),
        ("lines (centre) H1 closed, punctured", [f5["closed"]["H1"], f5["punctured"]["H1"]],
         [f5["closed"]["H1"], f5["punctured"]["H1"]] == [2, 2]),
        ("lines restriction to the boundary, rank", f5["punctured"]["restriction_rank"],
         f5["punctured"]["restriction_rank"] == 0),
        ("family Jacobian rank", f6["jacobian_rank"], f6["jacobian_rank"] == 3),
        ("family tangents rank modulo B1", f6["tangent_rank_mod_B1"], f6["tangent_rank_mod_B1"] == 3),
        ("kappa gradient at 0", f6["kappa_grad_at_0"], grad0),
        ("kappa Hessian at 0", f6["kappa_hessian"], hess_pd),
        ("sampled min (kappa + 2)/|s|^2, 3 decimals", round(smin, 3), smin > 0),
        ("Fricke identity residual below 1e-30", float(f6["fricke_identity_residual"]) < 1e-30,
         float(f6["fricke_identity_residual"]) < 1e-30),
        ("monodromy ker(phi* - 1), Fox route, per conjugator", fx["ker_dims"],
         bool(fx["ker_dims"]) and set(fx["ker_dims"]) == {1}),
        ("monodromy characteristic polynomial", fx["charpolys"], True),
        ("monodromy ker(D phi - 1), trace route", ft["ker_dim"], ft["ker_dim"] == 1),
    ]
    lines = ["DECISIVE: %s = %s" % (name, v) for name, v, _ in vals]
    return lines, all(ok for _, _, ok in vals), [name for name, _, ok in vals if not ok]


def main():
    try:
        root = repo_root()
        R, msg = run_sealed(root)
        if R is None:
            print("NOT DECIDED: " + msg)
            return 1
        lines, holds, bad = decisive(R)
        for l in lines:
            print(l)
        if not holds:
            print("NOT AS CLAIMED: " + "; ".join(bad))
            return 1
        return 0
    except Exception as e:                       # no traceback escapes
        print("NOT DECIDED: the wrapper raised %s" % type(e).__name__)
        return 1


if __name__ == "__main__":
    sys.exit(main())
