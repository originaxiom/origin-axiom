"""P-290 refile, decisive run (SM seat; data-free). Copies the sealed folder relays/sm_r290/ to a fresh temporary
directory, runs its sealed script run.py there UNCHANGED (`python3 -B run.py <repo root> run`), reads the
r290_results.json it writes, and prints the values the claim decides on, one per line, each beginning "DECISIVE: ".
Run from the repository root:  python3 relays/claims/sm_refile/r290_decisive.py
Exit 0 when the run completes and the decisive values come out; 1 otherwise. Nothing is written into the repository."""
import sys as _sys, os as _os, traceback as _tb


def _crash(et, ev, tb):
    _tb.print_exception(et, ev, tb)
    print("DECISIVE RUN FAILED: the script raised")
    _sys.stdout.flush()
    _os._exit(1)


_sys.excepthook = _crash
import json, pathlib, shutil, subprocess, sys, tempfile


def find_root():
    for s in (pathlib.Path(__file__).resolve().parent, pathlib.Path.cwd().resolve()):
        for d in [s, *s.parents]:
            if (d / "frontier").is_dir() and (d / "GENESIS.md").is_file():
                return d
    return None


def run_sealed(root, edit=None):
    """Copy relays/sm_r290 to a temp dir, optionally apply one (old, new) text edit to run.py, run it.
    Returns (returncode, results dict or None, stdout, stderr)."""
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="r290_"))
    try:
        dst = tmp / "sm_r290"
        shutil.copytree(root / "relays" / "sm_r290", dst)
        for f in ("r290_run.txt", "r290_results.json"):      # the copy's outputs are regenerated, never reused
            (dst / f).unlink(missing_ok=True)
        if edit:
            src = (dst / "run.py").read_text()
            if src.count(edit[0]) != 1:
                return -2, None, "", "edit did not apply"
            (dst / "run.py").write_text(src.replace(edit[0], edit[1]))
        env = dict(_os.environ, PYTHONDONTWRITEBYTECODE="1", OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1")
        p = subprocess.run([sys.executable, "-B", "run.py", str(root), "run"], cwd=dst, capture_output=True,
                           text=True, env=env)
        res = dst / "r290_results.json"
        return p.returncode, (json.loads(res.read_text()) if res.is_file() else None), p.stdout, p.stderr
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def decisive_lines(R):
    A, B, C, D, E = R["A"], R["B"], R["C"], R["D"], R["E"]
    i31, vec = A["I31"], A["vectorial"]
    out = [
        "A I-31 anomaly exponents mod 24: SU3 %d, SU2 %d, grav %d, grav without nu^c %d; m %d; K_W mod 4 %s" % (
            i31["SU3"], i31["SU2"], i31["grav"], i31["grav_no_nu"], i31["m"], i31["KW_mod4"]),
        "A vectorial anomaly exponents mod 24: SU3 %d, SU2 %d, grav %d; m %d; K_W mod 4 %s" % (
            vec["SU3"], vec["SU2"], vec["grav"], vec["m"], vec["KW_mod4"]),
        "B nu^c states in the 16: %d; two distinct doublets serve up and down/leptons: %s" % (
            B["nu_in_16"], B["two_distinct"]),
        "B Standard Model gauge group, uniform scalars realised: I-31 %s, vectorial %s" % (
            B["SM_realised"]["I-31"], B["SM_realised"]["vectorial"]),
        "C det exponents (chi_eta^e): rho_T %s, rho_H %s; rho_H = rho_T (x) chi^j for j in %s; = conj for j in %s" % (
            C["det_exp_T"], C["det_exp_H"], C["same"], C["conj"]),
        "D scalar subgroup Z of rho_T's image (phases r): %s; image order %d" % (D["Z"], D["image_T"]),
        "D F_c restricted phases trivial for I-31: SU3 %s, SU2 %s, grav %s; every s_u != s_d fails SU3: %s" % (
            D["restricted_I31"]["SU3"], D["restricted_I31"]["SU2"], D["restricted_I31"]["grav"],
            D["mixed_fail_SU3"]),
        "D F_S SU(3)_F^3 cubic: I-31 %d, vectorial %d; anomaly-free assignments %s" % (
            D["FS_cubic_I31"], D["FS_cubic_vect"], D["FS_free"]),
        "E invariant (Q, u^c, Higgs (x) chi^j) couplings by j: %s; determinant law at j = 3 below 1e-9: %s" % (
            {int(k): v for k, v in E["inv_dims"].items()}, float(E["law_residual"]["3"]) < 1e-9),
    ]
    return ["DECISIVE: " + s for s in out]


def main():
    root = find_root()
    if root is None:
        print("DECISIVE RUN FAILED: repository root (frontier/ and GENESIS.md) not found")
        return 1
    rc, R, so, se = run_sealed(root)
    if rc != 0 or R is None:
        print("DECISIVE RUN FAILED: the sealed script exited %d: %s" % (rc, (se.strip().splitlines() or [""])[-1]))
        return 1
    try:
        lines = decisive_lines(R)
    except Exception as e:                 # a missing value: the decisive values did not come out
        print("DECISIVE RUN FAILED: a decisive value is missing (%s)" % type(e).__name__)
        return 1
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())
