"""B1379 lock -- THE GENESIS AND m004 LINKS, AUDITED.  Also the lock THE CHAIN's C2 never had (docs/THEOREM_LEDGER.md:
"F3 is a citation to a test that does not exist"): the golden slope is the all-ones continued fraction, the bottom of the
Lagrange spectrum (value sqrt5, every other tested quadratic irrational >= sqrt8), and the one alternative a broader Pisot
criterion would pick -- the plastic number -- needs a three-letter alphabet, which C1's minimal complexity p(1) = 2 excludes.
The rest: the founding-ratio ladder (symbolic in n), its manifolds, the m003/m004 common double cover, A7 at the unbased level,
the m010 coefficient chain (Sym^3 the first active power), the puncture's invisibility to the torsion axiom, the reachability
census, and the non-descent of the cusped covers' index backgrounds to the closed tower (E72)."""
import sys, subprocess, importlib.util
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1379_the_genesis_and_m004_links" / "verification"
_spec = importlib.util.spec_from_file_location("b1379_genesis", VER / "genesis_audit.py")
G = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(G)


def test_c2_golden_self_selection():
    cf, lg = G.s8_c2()
    assert cf == [1] * 8                                              # phi = [1; 1, 1, ...]
    assert abs(lg["phi"] - 5 ** 0.5) < 1e-3                          # the bottom of the Lagrange spectrum
    assert min(v for k, v in lg.items() if k != "phi") > 8 ** 0.5 - 1e-3
    r2, r3 = G.s7_golden_plastic()
    assert abs(r2[0] - (1 + 5 ** 0.5) / 2) < 1e-12 and len(r2[1]) == 2    # binary: phi
    assert r3[0] < r2[0] and len(r3[1]) == 3                               # the plastic number needs three letters


def test_the_ratio_ladder_and_its_manifolds():
    out, gate, first_ratio, first_pos = G.s1_ladder()
    assert (first_ratio, first_pos) == (3, 4)
    names = {r[1]: r[2] for r in G.s2_manifolds()}
    assert names["+LR"] == "m004" and names["-LR"] == "m003" and names["-LLR"] == "m010"
    assert G.s3_common_cover() == {"m004": [True], "m003": [True]}
    conj, same, pLR, pRL = G.s4_A7()
    assert conj and same and str(pLR) != str(pRL)


def test_the_m010_coefficient_chain():
    gens, rels, _, res = G.s5_m010()
    for p, table in res:
        assert all(I == 0 for (c, m, s), (I, I0) in table.items() if m <= 2)
        assert table[((1, 3), 3, (1, 3))][0] == +1 and table[((4, 0), 3, (4, 0))][0] == +1


def test_the_puncture_and_the_census():
    assert G.s6_puncture()[:2] == ("Z", "Z")
    assert G.s9_reachability() == [1, 2, 4, 6, 12, 18, 34, 58, 106, 186, 350]


def test_no_descent_to_the_closed_tower():
    out = subprocess.run([sys.executable, str(VER / "descent_check.py")], capture_output=True, text=True, timeout=600,
                         cwd=str(VER)).stdout
    assert "non-split loci (common to three primes): 89" in out and "descends to Y4): 0" in out
    assert out.count("descends to closed Y6: False") == 3 and "DONE" in out
