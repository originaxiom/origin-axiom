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


def test_manifest_is_current():
    """regenerating the manifest changes nothing but the timestamp and the commit."""
    import tempfile
    before = _manifest()
    with tempfile.TemporaryDirectory() as tmp:   # regenerate into a temp dir: the test never writes into the tree
        r = subprocess.run([sys.executable, str(PKG / "build_manifest.py"), "--out", tmp], capture_output=True, text=True, cwd=str(PKG))
        assert r.returncode == 0, r.stdout + r.stderr
        after = json.loads((Path(tmp) / "MANIFEST.json").read_text(encoding="utf-8"))
    strip = lambda m: {k: v for k, v in m.items() if k not in ("built", "environment")}
    assert strip(before) == strip(after), "MANIFEST.json is stale: run build_manifest.py"


def test_seal_check_passes():
    r = subprocess.run([sys.executable, str(PKG / "run_package.py"), "--seals"], capture_output=True, text=True, cwd=str(PKG))
    assert r.returncode == 0, r.stdout + r.stderr


@pytest.mark.skipif(not os.environ.get("OA_SLOW"), reason="runs every lock the manifest names (a few minutes)")
def test_lock_run_passes():
    r = subprocess.run([sys.executable, str(PKG / "run_package.py"), "--locks"], capture_output=True, text=True, cwd=str(PKG), timeout=3600)
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
