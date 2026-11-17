"""B1938's lock: the determinant identity re-run live (two seconds); the other identities and the gauge-class read-out
held in their kept runs, each with its plant caught; the page's figures are the runs' figures."""
import re, subprocess, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent


def _num(pat, text):
    return float(re.search(pat, text).group(1))


def test_the_determinant_identity_live_and_its_plant():
    out = subprocess.run([sys.executable, "-B", str(HERE / "residue_as_determinants.py")], capture_output=True, text=True, timeout=300).stdout
    diffs = [float(x) for x in re.findall(r"diff ([0-9.e+-]+)  \(neglected", out)]
    assert len(diffs) >= 6 and max(abs(d) for d in diffs) < 1e-12      # Review 83: the absolute value was missing
    assert _num(r"PLANT \(chi = c instead of c - \(1/2,1/2\)\): diff ([0-9.e+-]+)", out) > 0.1


def test_the_kernel_identity_kept_with_its_plant():
    t = (HERE / "kernel_is_kronecker_run.txt").read_text()
    for key in ("kernel_vs_bilinear", "kronecker_form", "R_as_Z", "sumR2_rel", "z_vs_Qw_minus_h", "up_R1_rel"):
        assert _num(r"%s\s+([0-9.e+-]+)" % key, t) < 1e-15, key
    assert _num(r"PLANT \(relative line used as the kernel's line\): rel\. diff ([0-9.e+-]+)", t) > 0.1


def test_the_second_route_kept_with_its_plant():
    t = (HERE / "kronecker_other_lines_run.txt").read_text()
    assert _num(r"Kronecker at z = Q w - h_s\) - 1 : max ([0-9.e+-]+)", t) < 1e-13
    assert _num(r"log\(2 pi \|eta\|\)\] : max ([0-9.e+-]+)", t) < 1e-13
    assert _num(r"PLANT \(channel i with delta's half period moved\): ([0-9.e+-]+)", t) > 0.05


def test_the_parseval_constant_kept_with_its_plant():
    t = (HERE / "parseval_constant_run.txt").read_text()
    assert _num(r"max \|c_s - C_heat - predicted\| = ([0-9.e+-]+)", t) < 1e-10
    assert _num(r"PLANT \(log y with the opposite sign\): min \|diff\| = ([0-9.e+-]+)", t) > 0.1


def test_the_gauge_classes_agree_and_the_control_is_caught():
    t = (HERE / "gauge_class_readout_run.txt").read_text()
    zs = [float(x) for x in re.findall(r"max \|z\| ([0-9.]+)", t)]
    assert len(zs) == 3 and max(zs) < 3.0 and "words per class: 3000" in t
    c = (HERE / "gauge_class_control_run.txt").read_text()
    assert "CAUGHT" in c and _num(r"max \|z\| ([0-9.]+)", c) > 3.0


def test_the_page_states_the_runs_figures():
    f = (HERE.parent / "FINDINGS.md").read_text()
    t = (HERE / "gauge_class_readout_run.txt").read_text()
    for line in t.splitlines():
        m = re.match(r"(\w+)\s+vs (\w+)\s*: max \|d ln\| ([0-9.]+), max \|z\| ([0-9.]+), rms z ([0-9.]+)", line)
        if m:
            assert "| %s | %s | %s |" % (m.group(3), m.group(4), m.group(5)) in f, line
