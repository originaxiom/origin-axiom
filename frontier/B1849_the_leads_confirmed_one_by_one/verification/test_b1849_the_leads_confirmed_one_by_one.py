"""B1849 -- R76-1's register half: the two checks reproduce, every acted-on row carries its disposition, every merge's
host names it, and the ranked debts list no longer names P-527."""
import pathlib, re, subprocess, sys, importlib.util
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def _ap():
    spec = importlib.util.spec_from_file_location("ap", HERE / "apply_r76_1.py"); m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m); return m


def _rows():
    out = {}
    for ln in (ROOT / "docs" / "POINT_REGISTER.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"\| (P-\d{3}) \| ", ln)
        if m:
            out[m.group(1)] = ln.split(" | ")
    return out


def test_the_cyclic_texture_check_reproduces():
    out = subprocess.run([sys.executable, "-B", str(HERE / "p039_cyclic_texture.py")], capture_output=True, text=True,
                         check=True, timeout=120).stdout
    ref = (HERE / "p039_cyclic_texture_run.txt").read_text(encoding="utf-8")
    pat = (r"^200 random 3-cycle-covariant symmetric couplings in the charge basis: "
           r"entries with k \+ l != 0 mod 3 at most ([0-9.eE+-]+) of the largest; "
           r"entries \(0,0\), \(1,2\), \(2,1\) at least ([0-9.eE+-]+) -> the anti-diagonal texture\s*$")
    m_out, m_ref = re.match(pat, out), re.match(pat, ref)
    assert m_out and m_ref, (out, ref)
    err_out, min_out = float(m_out.group(1)), float(m_out.group(2))
    err_ref, min_ref = float(m_ref.group(1)), float(m_ref.group(2))
    assert err_out < 1e-12 and err_ref < 1e-12, (err_out, err_ref)
    assert abs(min_out - min_ref) < 1e-12 or (min_out > 1e-2 and abs(min_out - min_ref) / min_ref < 1e-2), (min_out, min_ref)
    assert "-> the anti-diagonal texture" in out


def test_the_whitehead_volumes_output():
    t = (HERE / "p476_whitehead_volumes_run.txt").read_text(encoding="utf-8")
    assert "volume 3.6638623767" in t
    vols = [float(m) for m in re.findall(r"vol\(L\^a R\) = ([0-9.]+)", t)]
    assert len(vols) == 9 and vols == sorted(vols) and all(v < 3.6638623767 for v in vols) and vols[-1] > 3.657


def test_every_acted_row_carries_its_disposition():
    ap, R = _ap(), _rows()
    for pid in list(ap.ANSWERED) + list(ap.PARTS):
        assert R[pid][4] == "DONE" and "R76-1, S306i" in R[pid][5], pid
    for pid, (host, _) in ap.MERGED.items():
        assert R[pid][4] == "DONE" and R[pid][5].startswith("merged into %s (R76-1" % host), pid
        assert R[host][4] in ("QUEUED", "LEAD") and pid in R[host][5], (pid, host)
    for pid in ap.KEPT:
        assert R[pid][4] in ("QUEUED", "LEAD") and "S306i, R76-1:" in R[pid][5], pid
    for pid in ap.RETYPE:
        assert R[pid][5].startswith("[PROCESS]") and "[was: (typed LEAD)" in R[pid][5], pid


def test_the_paid_debt_left_the_ranked_list_and_is_disclosed():
    reg = (ROOT / "docs" / "POINT_REGISTER.md").read_text(encoding="utf-8")
    ranked = reg[reg.index("## The debts, by load"):reg.index("## The queue")]
    assert "P-527 —" not in ranked
    nums = [int(n) for n in re.findall(r"^(\d+)\. P-\d{3} — ", ranked, re.M)]
    assert nums == list(range(1, len(nums) + 1))
    b1825 = next((ROOT / "frontier").glob("B1825_*")) / "FINDINGS.md"
    assert "The CM arm was dropped and not disclosed" in b1825.read_text(encoding="utf-8")
