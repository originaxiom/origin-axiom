"""Guard test (portability): no committed *.py file may hardcode an absolute machine path. Sibling
imports must resolve via Path(__file__)-relative paths. This locks the §2 cleanup permanently.

The forbidden prefixes are assembled from fragments so this test file does not trip itself."""
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
# assembled so the literal strings do not appear in this file's own source
_FORBIDDEN = ("/Us" + "ers/", "/ho" + "me/")
# legacy/ is checked-in history (incl. a vendored virtualenv); site-packages/venvs are third-party.
_SKIP_DIRS = {".git", "__pycache__", ".venv", "venv", "node_modules", ".mypy_cache", ".pytest_cache",
              "legacy", "site-packages", "phi_env", "dist-packages"}


def test_no_absolute_machine_paths_in_py():
    offenders = []
    for path in _ROOT.rglob("*.py"):
        if any(part in _SKIP_DIRS for part in path.parts):
            continue
        if path.resolve() == pathlib.Path(__file__).resolve():
            continue                                  # skip this guard file itself
        text = path.read_text(encoding="utf-8", errors="ignore")
        for frag in _FORBIDDEN:
            if frag in text:
                offenders.append(f"{path.relative_to(_ROOT)} contains {frag!r}")
    assert not offenders, "hardcoded absolute paths found:\n" + "\n".join(offenders)
