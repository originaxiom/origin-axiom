"""Bounded rechecks of already-banked claims; NOT new scientific discoveries.

Loads the pinned, inspected producers unchanged from Git into memory. Checks
are non-exhaustive and reuse upstream algorithms; not independent rederivation.
Assertions are explicit because a producer's printed PASS is not an exit status.
"""
import contextlib
import hashlib
import io
import json
import pathlib
import subprocess
import sys
import types
from fractions import Fraction as F

import snappy
import sympy as sp

PIN = "987c0c8fdb07f7f79beccd6c82c1154e3e75fa47"
SOURCES = {}


def load(name, path):
    code = subprocess.check_output(["git", "show", f"{PIN}:{path}"])
    SOURCES[path] = hashlib.sha256(code).hexdigest()
    module = types.ModuleType(name)
    module.__file__ = str(pathlib.Path(path).resolve())
    sys.modules[name] = module
    exec(compile(code, f"{PIN}:{path}", "exec"), module.__dict__)
    return module


def main(output):
    r = load("c2_reducible_index", "frontier/B1418_the_family_as_the_object/verification/c2_reducible_index.py")
    tet = load("tet_index", "frontier/B1431_the_index_separates_the_sibling/verification/tet_index.py")
    idx = load("idx", "frontier/B1431_the_index_separates_the_sibling/verification/idx.py")
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        K = r.NF([1, -1, 1])
        M, gens, rels, mu, lam = r.presentation("m010")
        u = K.alpha()
        chi = {"a": u, "b": K.const(-1)}
        c, h1 = r.nonsplit_cocycle(K, gens, rels, {g: K.mul(chi[g], chi[g]) for g in gens})
        assert c is not None and h1 == 1
        triple = {}
        for label, psi, wanted in [
            ("untwisted", {g: K.const(1) for g in gens}, 0),
            ("order_six", chi, 1),
            ("order_two", {g: K.pw(chi[g], 3) for g in gens}, 0),
        ]:
            value = r.run_module(K, "m010", gens, rels, mu, lam, chi, c, 3, psi, label)
            assert value["I"] == wanted and value["I_ss"] == 0, value
            triple[label] = value
    # Check the elementary determinant identity independently of the rank code.
    a,b,c0,d = sp.symbols("a b c d")
    A = sp.Matrix([[a,b],[c0,d]])
    J = sp.Matrix([[0,1],[-1,0]])
    assert sp.simplify(A.T*J*A - A.det()*J) == sp.zeros(2)
    witnesses = {}
    for name, cls, wanted in [
        ("m004", (1,0), [-2,-2,2,8,16,16,10,-14]),
        ("m003", (0,1), [-1,-1,2,7,11,11,3,-17]),
    ]:
        v = idx.index_class(name, cls, Xmax=16, box=100)
        assert v == idx.index_class(name, cls, Xmax=16, box=160)
        assert [v.get(2*i,0) for i in range(1,9)] == wanted
        witnesses[name] = v
    assert idx.index_class("m004", (0,0), Xmax=16, box=100) == idx.index_class("m003", (0,0), Xmax=16, box=100)
    mapping_count = 0
    for x in range(-2,3):
        for y in range(-2,3):
            lhs = idx.index_class("m003", (x,y), Xmax=16, box=100)
            rhs = idx.index_class("m004", (-(2*x+y),F(-y,2)), Xmax=16, box=100)
            assert lhs == rhs, (x,y)
            mapping_count += 1
    lattice_map = sp.Matrix([[-2,-1],[0,sp.Rational(-1,2)]])
    assert lattice_map.det() == 1
    assert any(v.q != 1 for v in lattice_map[:,1])
    fixed = [F(i,12) for i in range(6) if (2*F(i,12)) % F(1,2) == 0]
    assert fixed == [F(0),F(1,4)]
    result = {
        "kind": "bounded upstream-algorithm reproduction plus elementary identity checks",
        "pin": PIN, "source_sha256": SOURCES,
        "versions": {"python": sys.version, "snappy": snappy.__version__, "sympy": sp.__version__},
        "m010": triple, "m010_log": buf.getvalue(), "index_witnesses_in_sqrt_q": witnesses,
        "index_mapping_checks_through_q8": mapping_count,
        "cs_inversion_fixed_classes_mod_half": [str(x) for x in fixed],
        "not_verified": ["all-class index-series exclusion", "all parameter or module censuses",
                         "physical admissibility", "physical chirality", "full repository test suite"],
        "all_explicit_assertions_passed": True,
    }
    pathlib.Path(output).write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"pass": True, "m010_I": {k:v["I"] for k,v in triple.items()},
                      "series_witnesses": witnesses, "mapping_checks": mapping_count}, indent=2))


if __name__ == "__main__":
    main(sys.argv[1])
