"""B1802 -- Witten's doublet-triplet topology on the figure-eight's even fillings.  The committed runs: the explicit branch links
(each Sigma_2 isometric to the filling; two components exactly when p is even); the period's fixed circles and lifts; the order-2
torsion 5/4 and the 2-fold covers' |H1| = 5p/2; Witten's conditions enumerated (Z/2 alone has no full solution; Z/2 x Z/2 has)."""
import pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1802_witten_splitting_from_the_figure_eights_strong_inversion" / "verification"


def test_the_branch_links():
    text = "".join((V / "referee" / f).read_text(encoding="utf-8") for f in ("r3_run.txt", "r3_run_13.txt", "r3_run_14.txt"))
    hits = set(re.findall(r"m004\((\d+), (\d+)\): L = (\S+)\s+components (\d)\s+orbifold vol [0-9.]+\s+Sigma_2\(L\) isometric to Q: True", text))
    assert len(hits) >= 7
    for p, q, name, comps in hits:
        assert int(comps) == (2 if int(p) % 2 == 0 else 1), (p, q, name, comps)



def test_the_branch_links_on_main():
    run = (V / "branch_links_run.txt").read_text(encoding="utf-8")
    rows = re.findall(r"m004\((\d+), (\d+)\): H1 Z/(\d+), vol/2 ([0-9.]+); (\S+)\s+components (\d), orbifold vol ([0-9.]+); double branched cover isometric to Q: \[True\]", run)
    assert len(rows) == 7 and "branch_links exit 0" in run
    for p, q, h, half, name, comps, v in rows:
        assert int(h) == int(p) and half == v
        assert int(comps) == (2 if int(p) % 2 == 0 else 1), (p, q, name)

def test_the_period_and_the_lifts():
    r5 = (V / "referee" / "r5_run.txt").read_text(encoding="utf-8")
    assert "m004(6,1): |Hom(H1^orb, Z/2)| = 4; rho nontrivial on pi1(Q): local actions [(0, 1), (1, 0)]" in r5
    assert "m004(8,1): |Hom(H1^orb, Z/2)| = 4; rho nontrivial on pi1(Q): local actions [(0, 0), (1, 1)]" in r5
    r7 = (V / "referee" / "r7_run.txt").read_text(encoding="utf-8")
    assert "m004(6,1), P, Z/3 lines (restriction of order 3): (rho(m_A), rho(m_C), relative rho(m_A^-1 m_C)) = [(0, 0, 0)]" in r7


def test_the_torsion_and_witten_conditions():
    run = (V / "checks_run.txt").read_text(encoding="utf-8")
    assert re.search(r"order-2 torsion 5/4 and the cover orders 5p/2 on all \d+ listed fillings: True", run)
    r8 = (V / "referee" / "r8_run.txt").read_text(encoding="utf-8")
    assert "F' = Z/2: solutions {'full': 0" in r8 and "F' = Z/2 x Z/2: solutions {'full': 6" in r8
