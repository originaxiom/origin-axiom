"""Guard test (portability): no committed *.py file may hardcode an absolute machine path. Sibling
imports must resolve via Path(__file__)-relative paths. This locks the §2 cleanup permanently.

The forbidden prefixes are assembled from fragments so this test file does not trip itself."""
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
# assembled so the literal strings do not appear in this file's own source
_FORBIDDEN = ("/Us" + "ers/", "/ho" + "me/")
# legacy/ is checked-in history (incl. a vendored virtualenv); site-packages/venvs are third-party.
# audit/ and .tmpwork/ are gitignored scratch workspaces (never committed) -- out of scope for a guard
# that, per its docstring, governs *committed* .py files; they hold one-off probes with absolute paths.
_SKIP_DIRS = {".git", "__pycache__", ".venv", "venv", "node_modules", ".mypy_cache", ".pytest_cache",
              "legacy", "site-packages", "phi_env", "dist-packages", "audit", ".tmpwork",
              "cc2_packets"}  # archived cross-seat packet records (B646+): history, not live code


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


def test_no_absolute_machine_paths_in_tracked_text(  # R28-9 (the fourth-pass audit)
):
    """Extends the guard to tracked text artifacts (.md/.txt/.json/.log). Sealed and
    frozen records are exempt BY NAME (their bytes are hash-pinned); everything else
    must use repo-relative, ~/, or <seat>/ placeholder forms."""
    import re
    import subprocess
    tracked = subprocess.run(["git", "ls-files"], capture_output=True, text=True,
                             cwd=_ROOT).stdout.splitlines()
    sealed_pat = re.compile(r"PREREG|SEALED|ARTIFACT_HASHES|SEALS\.txt|REDACTION_RECORD"
                            r"|FORENSIC_SEAL")
    frozen_prefixes = ("frontier/B742_negatives_hunt_p1/reviews/", "legacy/")
    offenders = []
    for rel in tracked:
        if not rel.endswith((".md", ".txt", ".json", ".log")):
            continue
        if rel.startswith(frozen_prefixes) or sealed_pat.search(rel):
            continue
        if rel == "PROGRESS_LOG.md" or rel.startswith("docs/progress/PROGRESS_"):
            continue          # append-only records: historical bytes outrank path hygiene
        if "cc2_packets" in rel:
            continue                                  # archived packet records: history
        try:
            text = (_ROOT / rel).read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for frag in _FORBIDDEN:
            if frag in text:
                offenders.append(rel)
                break
    assert not offenders, "absolute paths in tracked text:\n" + "\n".join(offenders[:20])
