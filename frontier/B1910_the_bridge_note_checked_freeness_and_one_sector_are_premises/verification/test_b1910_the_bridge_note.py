"""B1910's lock. It loads the script (its write is under a main guard), requires every check to hold, and runs three
planted wrong claims that must come out false. It writes nothing."""
import importlib.util, io, contextlib, pathlib, json
import sympy as sp
HERE = pathlib.Path(__file__).resolve().parent
PAGE = (HERE.parent / "FINDINGS.md").read_text(encoding="utf-8")
LINE = json.loads((HERE.parent / "arc_verdict.json").read_text(encoding="utf-8"))["claim_one_line"]

def _load():
    spec = importlib.util.spec_from_file_location("b1910", HERE / "the_bridge_note_on_main.py")
    before = sorted(p.name for p in HERE.iterdir())
    with contextlib.redirect_stdout(io.StringIO()):
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    assert sorted(p.name for p in HERE.iterdir()) == before
    return m

M = _load()

def test_every_check_holds_and_the_page_counts_them():
    assert M.CHECKS and all(c["holds"] for c in M.CHECKS), [c["check"] for c in M.CHECKS if not c["holds"]]
    n = len(M.CHECKS)
    assert "%d checks, none failing" % n in PAGE and "%d checks, none failing" % n in LINE

def test_planted_wrong_claims_come_out_false():
    X, Z, z = M.heisenberg(3)
    lam = M.central_character(Z, X, 3)
    assert sp.simplify(M.central_character(Z, Z * X, 3) - sp.conjugate(lam)) != 0      # a det +1 move does not conjugate
    a, b = M.moves["swap (a,b) -> (b,a)"](Z, X)
    assert sp.simplify(M.central_character(a, b, 3) - lam) != 0                          # at p = 3 one sector is not kept
    D1, D2 = sp.diag(2, sp.Rational(1, 2)), sp.diag(3, sp.Rational(1, 3))
    assert M.comm(D1, D2).trace() != -2                                                 # the abelian carrier gives +2, never -2
