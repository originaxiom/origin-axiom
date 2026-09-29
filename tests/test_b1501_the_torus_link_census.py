"""B1501 lock -- THE TORUS-LINK CENSUS, run as sealed.

In the cones over the four homogeneous nearly Kaehler 6-manifolds (S6, S3 x S3, CP3, F12), modulo finite groups of the sealed list of
automorphisms, an ADE locus that is a cone over a torus is always of A-type and the torus is always hexagonal (P1 YES, P2 YES).  There are
exactly two kinds: the diagonal torus U(1)^3/U(1) of S3 x S3, fixed by the 23 classes L_(q,q,q) with pointwise stabiliser the diagonal
U(1); and Kostant's Coxeter torus of F12, fixed by L_{diag(1,w,w^2)} R_P^{+-1}, with pointwise stabiliser Z/3 acting on the normal plane
by (w, w^2), an A2 locus.  S6 and CP3 give points and spheres only."""
import hashlib
import importlib.util
import json
from fractions import Fraction
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1501_the_torus_link_census"
VER = ARC / "verification"


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _census():
    return json.load(open(VER / "census.json"))


def test_the_seal_and_the_recorded_census():
    d = _census()
    assert hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest() == d["sealed sha256"] \
        == "51b6730bd362e34656d3dfb2697e46af91a9f6c95739986bb7885997e5ac345d"
    recs = d["records"]
    assert d["classes"] == len(recs) == 694 and not d["flags"]
    per = {}
    for r in recs:
        per.setdefault(r["link"], []).append(r)
    assert {k: len(v) for k, v in per.items()} == {"S6": 67, "S3xS3": 329, "CP3": 95, "F12": 203}
    s = d["summary"]
    assert s["P1 every torus locus A-type (all finite subgroups of H_F cyclic)"] == "YES"
    assert s["P2 every torus hexagonal"] == "YES"
    assert s["P3 links carrying torus loci"] == ["F12", "S3xS3"] and s["P3 F12 carries a torus locus"] is True
    tori = [(r, c) for r in recs for c in r["components"] if c["topology"]["type"] == "torus"]
    assert len(tori) == 25
    s3 = [(r, c) for r, c in tori if r["link"] == "S3xS3"]
    f12 = [(r, c) for r, c in tori if r["link"] == "F12"]
    assert len(s3) == 23 and len(f12) == 2
    for r, c in s3:                                            # L_(q,q,q): the diagonal torus, U(1) isotropy
        assert r["outer"] is None and len(set(r["q"])) == 1
        assert np.allclose(c["shape"]["Gram (units (2 pi)^2)"], np.array([[2, -1], [-1, 2]]) / 3, atol=1e-12)
        assert c["H_F"]["H_F"] == "continuous: U(1)" and c["H_F"]["every finite subgroup cyclic"]
    for r, c in f12:                                           # L_{c0} R_P^{+-1}: the Coxeter torus, Z/3 isotropy, A2
        assert r["q"] == ["0", "1/3"] and r["outer"] in ("R_P", "R_P^2") and r["order"] == 3
        assert np.allclose(c["shape"]["Gram (units (2 pi)^2)"], np.array([[2, -1], [-1, 2]]) / 6, atol=1e-12)
        assert c["shape"]["index of the integral image in the period lattice"] == 3
        assert c["H_F"]["H_F"] == "finite, order 3" and c["H_F"]["ADE"] == "A2"
    for r, c in tori:
        assert c["shape"]["hexagonal"] and c["shape"]["dist to e^{i pi/3} up to reflection"] < 1e-12
        assert c["H_F"]["SU(2)-type on the normal space"]
    # the lemma: no torus from a left translation on an equal-rank link
    assert not [r for r, c in tori if r["outer"] is None and r["link"] in ("S6", "CP3", "F12")]
    # every class with fixed points converged on all 400 seeds; the others stayed far from a solution
    assert all(r["converged"] == 400 for r in recs if r["components"])
    assert min(r["smallest residual of the other seeds"] for r in recs if not r["components"]) > 0.4


def test_the_post_run_checks():
    rec = json.load(open(VER / "post_run_checks.json"))
    assert rec["all pass"] and not rec["criteria disagreements"] and not rec["lefschetz failures"]
    assert rec["closed-form shapes agree"] and not rec["reproducibility mismatches"] and len(rec["rerun"]) >= 30
    P = _load("b1501_post_run_checks", VER / "post_run_checks.py")
    d = _census()
    for r in d["records"]:                                     # the independent criteria and Lefschetz, recomputed here
        assert P.comp_signature(r) == P.expected_signature(r), r["label"]
        L = P.LEFSCHETZ_LEFT[r["link"]] if r["outer"] is None else P.LEFSCHETZ_TWISTED[r["link"]]
        assert P.euler_char(r) == L, r["label"]
    M, L = P.sigma_on_H3()
    assert M.tolist() == [[-1, 1], [-1, 0]] and L == 3


def test_the_flag_manifold_torus_in_closed_form():
    P = _load("b1501_post_run_checks_cf", VER / "post_run_checks.py")
    Gr, tau, orth = P.f12_coxeter_torus_shape()
    assert orth < 1e-12                                        # Kostant: Ad_{g^-1} t is orthogonal to t
    assert np.allclose(Gr, np.array([[2, -1], [-1, 2]]) / 6, atol=1e-12)
    assert abs(tau - np.exp(2j * np.pi / 3)) < 1e-12


def test_the_structures_and_s6():
    T = _load("b1501_census_mod", VER / "torus_link_census.py")
    rng = np.random.default_rng(2)
    for name, L in T.LINKS.items():
        T.structure_checks(L(), rng)                           # asserts inside: J, the listed and the excluded elements
    link = T.S6()
    T.s6_cross_product_check(link, rng)
    for q in [(Fraction(1, 13), Fraction(3, 13)), (Fraction(1, 13), Fraction(12, 13))]:
        cls = {"link": "S6", "q": q, "outer": None, "order": 13}
        rec = T.run_class(link, cls)
        assert T.s6_agrees(rec, cls)[1]
