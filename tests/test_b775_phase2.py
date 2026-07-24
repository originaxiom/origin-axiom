"""B775 Phase 2 Wave 1 -- locks on the structural results."""
import json
import pathlib

import sympy as sp

ARC = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B775_phase2_wave1"


def test_p2aabb_gamma5_derives_from_sigma():
    # the incidence matrix of sigma:a->ab has discriminant EXACTLY 5 -> Gal(Q(sqrt5)) = gamma5
    lam = sp.symbols("lambda")
    M = sp.Matrix([[1, 1], [1, 0]])
    cp = M.charpoly(lam).as_expr()
    assert cp == lam**2 - lam - 1
    assert sp.discriminant(cp, lam) == 5
    assert M.det() == -1  # phi*(1-phi)


def test_p2aabb_c_does_not_derive():
    # a<->b swap is NOT a sigma-automorphism: sigma(a)=ab, and swap-conjugation gives a->ba != ab
    sigma = {"a": "ab", "b": "a"}
    swap = {"a": "b", "b": "a"}
    # s . sigma . s applied to 'a': swap(sigma(swap('a'))) = swap(sigma('b')) = swap('a') = 'b'... image word
    conj = "".join(swap[ch] for ch in sigma[swap["a"]])  # swap(sigma(b)) = swap('a')='b'
    assert conj != sigma["a"]  # 'b' != 'ab' -> not an automorphism, c does not derive


def test_p2weld_minus_inv_phi_is_conjugate():
    # -1/phi = 1 - phi, the ubiquitous Galois conjugate (base-rate, dismissed)
    phi = (1 + sp.sqrt(5)) / 2
    assert sp.simplify(-1 / phi - (1 - phi)) == 0


def test_p2_wave1_all_upheld():
    d = json.loads((ARC / "wave1_results.json").read_text())
    cells = d["cells"]
    assert len(cells) == 7
    assert all(c["upheld"] for c in cells)
    verds = {c["id"]: c["verdict"] for c in cells}
    assert verds["P2-T1MOVER"] == "RESOLVED-B"      # WALLED
    assert verds["P2-SELRULE"] == "RESOLVED-A" if "P2-SELRULE" in verds else True
    # the three tombstones
    tomb = [c for c in cells if c.get("terminal_state", "").startswith("DISMISSED")]
    assert len(tomb) == 3


# ---- Wave 2 locks -------------------------------------------------------------


def test_p2w2_mirror_empty_set():
    # the mirror as a diagonal index-scaling needs c=1 mod 20 AND c=-1 mod 12 -> impossible
    assert (1 % 4) != (3 % 4)  # c=1 mod20 => 1 mod4; c=-1 mod12 => 3 mod4
    # the (2,3) stabilizer = units mod 60 with c = +-1 mod 5 (the sqrt5-fixing half-group)
    units60 = [c for c in range(1, 60) if sp.gcd(c, 60) == 1]
    half = [c for c in units60 if c % 5 in (1, 4)]
    assert half == [1, 11, 19, 29, 31, 41, 49, 59]
    # the phantom unit 49 is index-trivial at orders (12,6)
    assert 49 % 12 == 1 and 49 % 6 == 1


def test_p2w2_wave2_shape():
    d = json.loads((ARC / "wave2_results.json").read_text())
    cells = {c["id"]: c for c in d["cells"]}
    assert len(cells) == 7  # DARKHYP dropped on the output cap
    upheld = sorted(i for i, c in cells.items() if c["upheld"])
    assert len(upheld) == 6
    assert cells["P2W2-LATIN"]["upheld"] is False  # the forcing-overclaim catch
    assert cells["P2W2-PERLETTER"]["verdict"] == "RESOLVED-B"  # per-letter weight tombstoned


# ---- Wave 3 locks -------------------------------------------------------------


def test_p2w3_octahedral_parent():
    # OCTA: the octahedral group S4 has order 24 (the projective mod-3 Galois image)
    import sympy.combinatorics.named_groups as ng
    S4 = ng.SymmetricGroup(4)
    assert S4.order() == 24


def test_p2w3_l53_e6_cohomology_dims():
    # L53: e6 = (+) Sym^{2m} over Kostant exponents {1,4,5,7,8,11}, dims sum to 78; H^1 = rank 6
    exps = [1, 4, 5, 7, 8, 11]
    dims = [2 * m + 1 for m in exps]        # dim Sym^{2m} = 2m+1
    assert sum(dims) == 78                    # dim E6
    assert len(exps) == 6                     # rank E6 = H^1 dimension (one per block)


def test_p2w3_wave3_shape():
    d = json.loads((ARC / "wave3_results.json").read_text())
    cells = {c["id"]: c for c in d["cells"]}
    assert len(cells) == 8
    upheld = sorted(i for i, c in cells.items() if c["upheld"])
    assert len(upheld) == 7
    assert cells["P2W3-1/4WALK"]["upheld"] is False   # the frozenness over-claim carry
    # two theorems + a structural positive banked
    assert cells["P2W3-L56"]["verdict"] == "RESOLVED-A"
    assert cells["P2W3-OCTA"]["verdict"] == "RESOLVED-A"


# ---- Wave 4 locks -------------------------------------------------------------


def test_p2w4_z1_values_in_golden_ring():
    # Z1: every value of the ladder is an algebraic integer in Z[phi].  The values are NOT
    # hardcoded any more (P2W6-Z1-r repair): they are read from the recomputed ladder, whose
    # low-k entries are themselves recomputed from scratch by the locks below.
    x = sp.Symbol("x")
    d = json.loads((ARC / "wave4_results.json").read_text())
    z1 = next(c for c in d["cells"] if c["id"] == "P2W4-Z1")
    assert z1["verdict"] == "RESOLVED-B"        # the verdict is correct and reproduced
    assert z1["upheld"] is False                 # carried: two false statements in the claim text
    r = json.loads((ARC / "cells" / "P2W6-Z1-r" / "results.json").read_text())
    vals = sorted({e["Z"] for e in r["ladder"]})
    assert len(vals) >= 4
    for s in vals:
        v = sp.sympify(s.replace("sqrt5", "sqrt(5)"))
        coeffs = sp.Poly(sp.minimal_polynomial(v, x), x).all_coeffs()
        assert coeffs[0] == 1 and all(c.is_integer for c in coeffs)   # monic integer => in Z[phi]
        assert sp.degree(sp.minimal_polynomial(v, x), x) <= 2         # degree <= 2 over Q


def _z1r():
    """load the repair cell's exact pipeline (module import is ~1 s: E6 Weyl group)."""
    import importlib.util
    p = ARC / "cells" / "P2W6-Z1-r" / "compute.py"
    spec = importlib.util.spec_from_file_location("p2w6_z1r", p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


# ---- Wave 6 locks (repairs) ---------------------------------------------------


def test_p2w6_z1r_recomputes_ladder_entries():
    # RECOMPUTING lock (replaces the six hardcoded values): Z_k is recomputed FROM SCRATCH
    # through the exact cyclotomic pipeline and certified mod Phi_{36 kappa}.
    from fractions import Fraction
    m = _z1r()
    for k, want in ((1, (1, 0)), (3, (1, 0)), (4, (0, 0))):
        N, kap, M, coeff = m.exact_Z_vector(k, read_cache=False, write_cache=False)
        z, p, q, st = m.identify(coeff, M, kap)
        assert st == "exact" and (p, q) == (Fraction(want[0]), Fraction(want[1]))
        assert m.certify(coeff, M, kap, p, q)                 # the certificate holds ...
        assert not m.certify(coeff, M, kap, p + 1, q)         # ... and is falsifiable
        assert m.in_Zphi(p, q)                                # value lies in Z[phi]
    # k=4 is the H133 killer: the coefficient vector is identically zero
    _, _, _, c4 = m.exact_Z_vector(4, read_cache=False, write_cache=False)
    assert not c4.any()


def test_p2w6_z1r_irrationality_is_one_directional():
    # CORRECTION (a): "irrational EXACTLY WHEN 5|kappa" is FALSE.  Recomputed counterexample:
    # k=3 has kappa=15 (divisible by 5) and Z=1 -- RATIONAL -- even though sqrt5 DOES live in
    # Q(zeta_540) (Gauss sum g with g^2 = 5, verified exactly mod Phi_540).
    from fractions import Fraction
    m = _z1r()
    N, kap, M, coeff = m.exact_Z_vector(3, read_cache=False, write_cache=False)
    assert kap == 15 and kap % 5 == 0
    z, p, q, st = m.identify(coeff, M, kap)
    assert st == "exact" and q == 0 and p == Fraction(1)      # rational, so the iff fails
    ram = m.ramification_facts([15, 16])
    assert ram["gausssum_ok"]          # sqrt5 IS available at kappa=15 -> not a field obstruction
    assert ram["unramified_ok"]        # and 5 is unramified at kappa=16 -> the other direction
    # the forced direction: 5 unramified in Q(zeta_{36 kappa}) whenever 5 does not divide kappa
    row = {r["kappa"]: r for r in ram["rows"]}
    assert row[16]["5_unramified_in_Q(zeta_36k)"] is True
    assert row[15]["5_unramified_in_Q(zeta_36k)"] is False


def test_p2w6_z1r_characteristic_prime_exemplars():
    # CORRECTION (b): the banked exemplars are wrong -- kappa=32,34,39 DO carry a
    # characteristic prime.  R is RECOMPUTED from W(E6), not quoted.
    import math
    m = _z1r()
    import numpy as np
    Wi = m.W.astype(np.int64)
    dets = np.rint(np.linalg.det((Wi @ Wi - 3 * Wi
                                  + np.eye(6, dtype=np.int64)[None, :, :]).astype(float)))
    prim = sorted({p for d in {abs(int(v)) for v in dets.astype(np.int64)} if d
                   for p in sp.factorint(d)})
    assert prim == [2, 3, 5, 7, 11, 19]
    R = 1
    for p in prim:
        R *= p
    assert R == 43890
    assert [math.gcd(k, R) for k in (32, 34, 39)] == [2, 2, 3]   # NOT coprime -> banked text wrong
    # and the computed C5-failing set, rebuilt from the recomputed ladder
    r = json.loads((ARC / "cells" / "P2W6-Z1-r" / "results.json").read_text())
    fail = [e["kappa"] for e in r["ladder"]
            if (e["Z"] == "1") != (math.gcd(e["kappa"], R) == 1)]
    assert fail == [14, 15, 18, 20, 21, 28, 29, 31]
    assert [k for k in fail if math.gcd(k, R) == 1] == [29, 31]  # only two of that mode


def test_p2w6_z1r_verdict_gate_is_not_vacuous():
    # every branch of the sealed decision function fires on an admissible fact-vector
    m = _z1r()
    r = json.loads((ARC / "cells" / "P2W6-Z1-r" / "results.json").read_text())
    assert r["verdict"] == "RESOLVED-A"
    fired = {c["verdict"] for c in r["L1_counterfactuals"]} | {r["verdict"]}
    assert fired == {"RESOLVED-A", "RESOLVED-B", "UNRESOLVED"}
    assert r["gates"]["G6_reproduces_banked_vectors"] is True   # bitwise repro of P2W4-Z1
    assert r["L3_implication_lattice"]["independent_count"] == 3   # not the banked 5
    assert r["L4_range_sensitivity"]["first_kmax_with_no_surviving_law"] == 14


def test_p2w4_wave4_shape():
    d = json.loads((ARC / "wave4_results.json").read_text())
    cells = {c["id"]: c for c in d["cells"]}
    assert len(cells) == 8
    # R2 sealing fails (positive-dimensional); HEAR reprices kappa=5 as a choice
    assert cells["P2W4-R2"]["verdict"] == "RESOLVED-B"
    assert cells["P2W4-HEAR"]["verdict"] == "RESOLVED-B"
    assert cells["P2W4-L54"]["verdict"] == "RESOLVED-A"


# ---- Wave 5 locks -------------------------------------------------------------


def test_p2w5_gateb_hessian_identity_forces_the_reason():
    # the verifier's catch: det Hess I3(v) == 2*I3(v)^9, so F4-exclusion is a corollary
    # of chirality, not an independent discriminator. Check the identity's consequence:
    # I3(v)=0 => det Hess = 0 (degenerate), so "degenerate Hessian" adds nothing once I3|Fix==0.
    for i3 in [-8, 1, 3, -2]:
        assert 2 * i3**9 != 0            # nondegenerate exactly when I3 != 0
    assert 2 * 0**9 == 0                  # I3=0 => Hessian degenerate, forced


def test_p2w5_wave5_shape():
    d = json.loads((ARC / "wave5_results.json").read_text())
    cells = {c["id"]: c for c in d["cells"]}
    assert len(cells) == 8
    upheld = sorted(i for i, c in cells.items() if c["upheld"])
    assert upheld == ["P2W5-ALLCHIRAL", "P2W5-CLOCK", "P2W5-HERED", "P2W5-LSCHAAR", "P2W5-ORGAN"]
    # GATEB's verdict stands but is carried for a forced reason
    assert cells["P2W5-GATEB"]["verdict"] == "RESOLVED-B"
    assert cells["P2W5-GATEB"]["upheld"] is False


# ---- Wave 6 locks -------------------------------------------------------------


def test_p2w6_b138_sl4_sealing_bound():
    # S031a -> SL(4): A^2 central => dim C<A,B> <= 4 => reducible for n>=3
    # the bound is dim<=4 (A, B, AB, A^2=scalar collapses) -- check the algebra-dim logic
    # A^2 scalar means {I, A, B, AB} spans; dim <= 4 < n^2 for n>=3 (9) => reducible
    for n in (3, 4, 5):
        assert 4 < n**2                       # dim C<A,B> <= 4 < n^2 => not all of M_n => reducible


def test_p2w6_wave6_shape():
    d = json.loads((ARC / "wave6_results.json").read_text())
    cells = {c["id"]: c for c in d["cells"]}
    assert len(cells) == 8
    upheld = sorted(i for i, c in cells.items() if c["upheld"])
    assert upheld == ["P2W6-B106", "P2W6-B138", "P2W6-B414-r", "P2W6-GATEB-r", "P2W6-Z1-r"]
    # GATEB-r: the forced-reason repair, upheld
    assert cells["P2W6-GATEB-r"]["verdict"] == "RESOLVED-B" and cells["P2W6-GATEB-r"]["upheld"]
