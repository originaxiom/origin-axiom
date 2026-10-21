"""B1683 -- GENESIS v1.50. The amendment reproduces v1.50 from the hash-pinned v1.49: the root file while it was at v1.50,
and B1685's received copy since (GENESIS moved to v1.51, so the check reads the pinned copy, as B1681's does). In v1.50
GM1 reads POSTULATED in an equivalent form, GM5b's "only" is scoped, and the log keeps the v1.50 entry."""
import hashlib, importlib.util, pathlib, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1683_genesis_v1_50_gm1_characterised"
V150 = ROOT / "frontier" / "B1685_genesis_v1_51_reliance_tagged" / "received" / "GENESIS_v1_50_main.md"


def test_the_amendment_reproduces_v1_50():
    r = subprocess.run([sys.executable, str(A / "adoption" / "amend.py"), "--check"], capture_output=True)
    assert r.returncode == 0
    spec = importlib.util.spec_from_file_location("am", A / "adoption" / "amend.py"); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    v = V150.read_text(encoding="utf-8")
    assert hashlib.sha256(v.encode("utf-8")).hexdigest() == "98a8dda5ee926d1943b6dd801fb2fb770fa665d1c793c37e17bd34392659ca12"
    assert m.build() == v


def test_gm1_gm5b_and_the_log_in_v1_50():
    v = V150.read_text(encoding="utf-8")
    assert "| GM1 | Two records: updates act on a pair of integer counts, ℤ² | **POSTULATED, in an equivalent form [v1.50]**" in v
    assert "of the two readings B1662 compared, only this one never settles" in v
    g = (ROOT / "GENESIS.md").read_text(encoding="utf-8")
    assert "- **v1.50 · 2026-10-21 · main B1683.**" in g and "| GM5b | Inverse moves are legal | **ADOPTED [v1.48]**" in g
