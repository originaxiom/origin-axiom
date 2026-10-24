"""B1754 -- GENESIS v1.58.  The amendment reproduces the root file from the hash-pinned v1.57 (--check bites); every status
cell as it was; F-MC's merged ladder wording and R2's hypothesis in place; the log entry above an unrewritten v1.57 entry;
THE WEAVE carries the qualifier, the lane's second sentence as a gloss, and the merged wording."""
import importlib.util, pathlib, re, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1754_genesis_v1_58"


def _m():
    spec = importlib.util.spec_from_file_location("am58", A / "adoption" / "amend.py"); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def test_the_amendment_reproduces_the_root_file():
    r = subprocess.run([sys.executable, str(A / "adoption" / "amend.py"), "--check"], capture_output=True)
    assert r.returncode == 0
    g = (ROOT / "GENESIS.md").read_text(encoding="utf-8")
    if "**Version 1.58 · 2026-10-24 · canonical.**" in g:
        assert _m().build() == g


def test_the_changes():
    src = (A / "received" / "GENESIS_v1_57_main.md").read_text(encoding="utf-8"); out = _m().build()
    cells = lambda t: re.findall(r"^\| (GM\d\w?|PF\d|FK\d+|SE\d) \|[^|]*\| \*{0,2}([A-Z][A-Z ,]+)", t, re.M)
    assert cells(src) == cells(out)
    assert "Γ/⟨⟨T^N⟩⟩ = Δ(2, 3, N)" in out and "PSL(2, 𝔽₇) is a quotient of the infinite Δ(2, 3, 7)" in out
    assert "a composition requirement adopted by the ruling" in out and "one scalar holomorphic theta series" in out
    i58, i57 = out.find("- **v1.58 · 2026-10-24 · main B1754.**"), out.find("- **v1.57 · 2026-10-24 · main B1752.**")
    assert 0 < i58 < i57
    fmc = [l for l in out.splitlines() if l.startswith("| F-MC ")][0]
    assert "|" not in fmc.replace(" | ", "\x00").strip("|\x00 ").replace("\x00", "")


def test_the_companions_b1754():
    w = (ROOT / "docs" / "THE_WEAVE.md").read_text(encoding="utf-8")
    assert "Choosing a representative is a\n> convention only when the declared equivalence preserves the full relational observables" in w
    assert "recorded here as its gloss" in w and "The merged wording (adopted 2026-10-24 at the owner's ruling on P-385" in w
    assert "what the ruling adopts is E₈ as the single container" in w          # B1752's clause kept
    r = (ROOT / "WORKING_RULES.md").read_text(encoding="utf-8")
    assert "including the reference/measuring sector (the audit lane's qualifier" in r
    assert "| P-385 | 2026-10-24 | SE |" in (ROOT / "docs" / "POINT_REGISTER.md").read_text(encoding="utf-8")
