"""THE PAPER's verification package: the manifest is current and consistent with the repository (every record found, every
record locked, every seal matching), the seal check passes, and under OA_SLOW the lock run passes."""
import hashlib, json, os, subprocess, sys
from pathlib import Path
import pytest
ROOT = Path(__file__).resolve().parents[1]; PKG = ROOT / "papers" / "P3_THE_PAPER" / "verification_package"


def _manifest():
    return json.loads((PKG / "MANIFEST.json").read_text(encoding="utf-8"))


def test_package_files_exist():
    for f in ("build_manifest.py", "run_package.py", "README.md", "MANIFEST.json", "MANIFEST.md"):
        assert (PKG / f).exists(), f


def test_manifest_is_consistent_with_the_repository():
    m = _manifest()
    assert m["totals"]["claims"] >= 21
    for c in m["claims"]:
        assert c["support"] in ("settled", "computed")
        for r in c["records"]:
            assert "error" not in r, (c["claim"], r)
            assert (ROOT / r["dir"]).is_dir() and r["locks"], (c["claim"], r["arc"])
            for l in r["locks"]: assert (ROOT / l).exists(), l
            for s in r["seals"]:
                cur = hashlib.sha256((ROOT / s["sealed_file"]).read_bytes()).hexdigest()
                assert any(cur in line for line in s["recorded"]), (r["arc"], s["seal_file"])


def _drop_absent_paths(node):
    """Prune, from every list in the manifest, string entries naming a repo path this
    checkout does not have.  Used only to tell an incomplete checkout from a stale manifest."""
    if isinstance(node, dict):
        return {k: _drop_absent_paths(v) for k, v in node.items()}
    if isinstance(node, list):
        return [_drop_absent_paths(v) for v in node
                if not (isinstance(v, str) and "/" in v and not v.split()[1:]
                        and not (ROOT / v).exists())]   # path-shaped only: no prose, no seal comments
    return node


def test_manifest_is_current():
    """regenerating the manifest changes nothing but the timestamp and the commit."""
    import tempfile
    before = _manifest()
    with tempfile.TemporaryDirectory() as tmp:   # regenerate into a temp dir: the test never writes into the tree
        r = subprocess.run([sys.executable, str(PKG / "build_manifest.py"), "--out", tmp], capture_output=True, text=True, cwd=str(PKG))
        assert r.returncode == 0, r.stdout + r.stderr
        after = json.loads((Path(tmp) / "MANIFEST.json").read_text(encoding="utf-8"))
    strip = lambda m: {k: v for k, v in m.items() if k not in ("built", "environment")}
    b, a = strip(before), strip(after)
    if b != a:
        # Distinguish a STALE manifest from an INCOMPLETE checkout.  build_manifest.py globs
        # the filesystem, and .gitignore's LaTeX rule `*.out` also matches every
        # frontier/*/verification/*.out, so a fresh clone lacks artifacts the manifest cites
        # and rebuilds a strictly smaller manifest.  Running build_manifest.py there would
        # DELETE those entries -- the opposite of the repair.  Only the residue after
        # dropping absent paths may be called staleness.
        assert _drop_absent_paths(b) == a, "MANIFEST.json is stale: run build_manifest.py"
        pytest.skip("manifest cites artifacts absent from this checkout (gitignored *.out); "
                    "not stale -- rebuild only on a bench that holds them")


def test_seal_check_passes():
    r = subprocess.run([sys.executable, str(PKG / "run_package.py"), "--seals"], capture_output=True, text=True, cwd=str(PKG))
    assert r.returncode == 0, r.stdout + r.stderr


@pytest.mark.skipif(not os.environ.get("OA_SLOW"), reason="runs every lock the manifest names (a few minutes)")
def test_lock_run_passes():
    r = subprocess.run([sys.executable, str(PKG / "run_package.py"), "--locks"], capture_output=True, text=True, cwd=str(PKG), timeout=3600)
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
