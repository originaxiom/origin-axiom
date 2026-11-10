"""The tracked-deps gate, second scope (E94; Review 77, 2026-11-10): a lock may not read a file git does not have.

B1671's three logs (Review 73) and B1854's three (Review 77) were read by their locks through `HERE / "name.log"`, ignored by
the repository's `*.log` rule, and so absent from every fresh clone.  The gate read only tests/ and scripts/ and only
repo-root paths; it now also reads each tracked lock's own-directory paths.  The plant is a synthetic lock handed to the gate
as text: no tracked file is touched.
"""
import importlib.util
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = "frontier/B1854_the_tubes_tau_beyond_k1_on_main/verification"
LOCK = "import pathlib\nHERE = pathlib.Path(__file__).resolve().parent\nx = (HERE / \"%s\").read_text()\n"


def _gates():
    spec = importlib.util.spec_from_file_location("gates_for_e94", ROOT / "scripts" / "gates" / "gates.py")
    g = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(g)
    return g


def test_the_gate_is_green_on_the_tree():
    ok, why = _gates().gate_tracked_deps()
    assert ok, why


def test_a_lock_that_reads_an_untracked_file_is_refused(tmp_path):
    g = _gates()
    # an untracked file beside a real arc's locks; removed whatever happens
    plant = ROOT / ARC / "_e94_planted_untracked_output.txt"
    assert not plant.exists()
    try:
        plant.write_text("planted: must never be tracked\n", encoding="utf-8")
        ok, why = g.gate_tracked_deps(_plant=(ARC + "/test_e94_planted_lock.py", LOCK % plant.name))
        assert not ok and plant.name in why, why
        # the same file read by a generator, not a lock, is not this gate's business
        ok2, why2 = g.gate_tracked_deps(_plant=(ARC + "/make_e94_planted.py", LOCK % plant.name))
        assert ok2, why2
    finally:
        if plant.exists():
            plant.unlink()
    # a tracked file read the same way passes
    ok3, why3 = g.gate_tracked_deps(_plant=(ARC + "/test_e94_planted_lock.py", LOCK % "driver_k2_run.txt"))
    assert ok3, why3


def test_the_own_directory_reader_resolves_parent_and_parents():
    g = _gates()
    txt = ("import pathlib\nHERE = pathlib.Path(__file__).resolve().parent\nA = pathlib.Path(__file__).resolve().parents[1]\n"
           "ROOT = pathlib.Path(__file__).resolve().parents[3]\n"
           "a = HERE / \"runs\" / \"k1.txt\"\nb = A / \"FINDINGS.md\"\nc = ROOT / \"docs\" / \"X.md\"\n")
    refs = g._file_relative_refs("frontier/B1_x/verification/test_t.py", txt)
    assert refs == {"frontier/B1_x/verification/runs/k1.txt", "frontier/B1_x/FINDINGS.md", "docs/X.md"}


def test_b1854s_lock_reads_only_tracked_files():
    tracked = set(subprocess.run(["git", "-C", str(ROOT), "ls-files", ARC], capture_output=True, text=True).stdout.split())
    for name in ("driver_k1_control_run.txt", "driver_k2_run.txt", "driver_k3_run.txt"):
        assert ARC + "/" + name in tracked
