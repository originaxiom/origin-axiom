"""Decisive run for the SM seat's P-384 claim (the line class (2/5, odd/10): one cusp, its offset forced, its slope one
Galois bit). Copies the sealed folder relays/sm_r384/ to a fresh temporary directory, runs the sealed run.py there
unchanged with the repository root as its main-checkout argument, reads the results it writes beside itself, and
prints the values the claim decides on lines beginning "DECISIVE: ". Writes nothing into the repository.
    python3 relays/claims/sm_refile/r384_decisive.py        # from the repository root
Exit 0 when the run completes and every decisive value is read; 1 otherwise. Data-free: an exact enumeration."""
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile

SEALED_SHA16 = "d0c30fbf62479829"
KEY_RULES = ("div5 (plant: the five-ality rule)", "5-part on the act's line", "order 10, 5-part on the act's line",
             "order 10, cusp sees the 5-part, not the 2-part", "unit twist (3a = +-1/5)",
             "PI: least level breaking the copy, unit twist", "PI_inv: least level breaking the copy, nonzero twist",
             "PI with h = 1 (plant)", "DESCRIPTION (control): order 10, a = +-2/5")


def find_root():
    for s in (pathlib.Path.cwd(), pathlib.Path(__file__).resolve().parent):
        for d in (s, *s.parents):
            if (d / "frontier").is_dir() and (d / "GENESIS.md").exists():
                return d
    raise SystemExit("repository root (with frontier/ and GENESIS.md) not found")


def run_sealed(root, edit=None):
    """Run the sealed script in a temp copy; edit, if given, is (old, new) applied to the copy's run.py only."""
    import hashlib
    src = root / "relays" / "sm_r384"
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="r384_"))
    try:
        dst = tmp / "sm_r384"
        shutil.copytree(src, dst, ignore=shutil.ignore_patterns("r384_results.json", "r384_run.txt", "__pycache__"))
        script = dst / "run.py"
        sha16 = hashlib.sha256(script.read_bytes()).hexdigest()[:16]
        if edit is not None:
            text = script.read_text(encoding="utf8")
            if text.count(edit[0]) != 1:
                raise RuntimeError("the planted edit did not apply")
            script.write_text(text.replace(edit[0], edit[1]), encoding="utf8")
        proc = subprocess.run([sys.executable, "-B", str(script), str(root)], cwd=str(dst), capture_output=True,
                              text=True, timeout=600)
        if proc.returncode != 0:
            raise RuntimeError("the sealed script exited %d" % proc.returncode)
        return sha16, json.loads((dst / "r384_results.json").read_text(encoding="utf8"))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def decisive_lines(sha16, res):
    R = res["rules"]
    inv_exact = [n for n, r in R.items() if r["unit_invariant"] and r["exactly_class"]]
    cusps = res["cusps_at_order_pq"]
    out = [
        "sealed script sha256[:16] = %s (expected %s)" % (sha16, SEALED_SHA16),
        "universe %d lines; order 5: %d; order 10: %d" % (res["universe"], res["order_p"], res["order_pq"]),
        "class K = %s; carriers in K: %s" % (", ".join(res["class"]), res["carriers_in_class"]),
        "K unit-invariant: %s; its unit closure has %d lines" % (res["class_unit_invariant"],
                                                                len(res["class_unit_closure"])),
        "order-10 cusps: %d; K is exactly one: %s; cusps seeing the 5-part: %d" % (
            len(cusps), sum(c["is_class"] for c in cusps) == 1, sum(c["sees_p_part"] for c in cusps)),
        "least level breaking the lepton copy: %d" % res["least_level"],
        "unit-invariant rules: %d; of them exactly K: %d" % (sum(r["unit_invariant"] for r in R.values()),
                                                             len(inv_exact)),
    ]
    for n in KEY_RULES:
        r = R[n]
        out.append("rule [%s]: selected %d, in K %d, carriers %d, exactly K %s, unit-invariant %s" % (
            n, r["selected"], r["in_class"], r["carriers_in"], r["exactly_class"], r["unit_invariant"]))
    return out


def main():
    try:
        root = find_root()
        sha16, res = run_sealed(root)
        lines = decisive_lines(sha16, res)
    except BaseException as exc:          # noqa: BLE001
        print("FAILED: %s" % (exc,))
        return 1
    for l in lines:
        print("DECISIVE: " + l)
    return 0 if sha16 == SEALED_SHA16 else 1


if __name__ == "__main__":
    sys.exit(main())
