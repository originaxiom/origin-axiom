"""B1050 locks — the projective quotient is natural and still not a selector.

Locks MATHEMATICS (WORKING_RULES §7), recomputed here rather than read from the arc's JSON.
"""
import glob
import json
import pathlib
import re

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[1]
x, y, z, c = sp.symbols("x y z c")
V = (x, y, z)

# The trace map, the central sign action, and the Fricke-Vogt invariant in the TRACE-MAP
# normalisation. The Markov form x^2+y^2+z^2-xyz is a DIFFERENT normalisation of the same name and
# is NOT preserved by T -- pinned below so the collision cannot be reintroduced silently.
T = (z, x, sp.expand(2 * x * z - y))
S = lambda sa, sb: (sa * x, sb * y, sa * sb * z)
I = x ** 2 + y ** 2 + z ** 2 - 2 * x * y * z - 1
SIGNS = [(a, b) for a in (1, -1) for b in (1, -1)]


def _read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def _body(bid):
    return pathlib.Path(glob.glob(str(ROOT / "frontier" / f"{bid}_*" / "FINDINGS.md"))[0]
                        ).read_text(encoding="utf-8")


def _sub(F, e):
    return sp.expand(e.subs(dict(zip(V, F)), simultaneous=True))


def _jac(F):
    return sp.Matrix([[sp.diff(f, v) for v in V] for f in F])


def _nambu(f, g):
    gI = sp.Matrix([sp.diff(I, t) for t in V])
    return sp.expand(gI.dot(sp.Matrix([sp.diff(f, t) for t in V]).cross(
        sp.Matrix([sp.diff(g, t) for t in V]))))


def test_all_checks_pass():
    R = json.loads(_read("frontier/B1050_the_projective_wall/results.json"))
    bad = [k for k, v in R["checks"].items() if not v["pass"]]
    assert bad == [] and R["all_pass"] is True, bad
    assert len(R["checks"]) >= 66


def test_which_invariant_the_trace_map_preserves():
    """The convention collision, pinned in both directions so it cannot come back."""
    assert sp.expand(_sub(T, I) - I) == 0
    markov = x ** 2 + y ** 2 + z ** 2 - x * y * z
    assert sp.expand(_sub(T, markov) - markov) != 0


def test_the_quotient_is_legitimate_and_the_antipodal_control_fails():
    for sa, sb in SIGNS:
        lhs = [_sub(S(sa, sb), t) for t in T]
        rhs = [_sub(T, e) for e in S(sa * sb, sa)]
        assert all(sp.expand(a - b) == 0 for a, b in zip(lhs, rhs)), (sa, sb)
        assert sp.expand(_sub(S(sa, sb), I) - I) == 0
    assert sp.expand(I.subs({x: -x, y: -y, z: -z}, simultaneous=True) - I) != 0


def test_the_polynomial_descent_and_the_period_3_orbit():
    u, v, w, r = x ** 2, y ** 2, z ** 2, x * y * z
    img = [sp.expand(e) for e in T]
    assert sp.expand(img[0] ** 2 - w) == 0
    assert sp.expand(img[1] ** 2 - u) == 0
    assert sp.expand(img[2] ** 2 - (4 * u * w - 4 * r + v)) == 0
    assert sp.expand(img[0] * img[1] * img[2] - (2 * u * w - r)) == 0
    step = lambda q: (q[2], q[0], sp.expand(4 * q[0] * q[2] - 4 * q[3] + q[1]),
                      sp.expand(2 * q[0] * q[2] - q[3]))
    o = (0, 0, c ** 2, 0)
    assert step(step(step(o))) == o


def test_the_half_step_is_anti_poisson_and_its_square_is_poisson():
    """B21's mechanism: for a map preserving I the bracket transforms by det(DF)."""
    T2 = tuple(_sub(T, e) for e in T)
    assert sp.simplify(_jac(T).det()) == -1
    assert sp.simplify(_jac(T2).det()) == 1
    for f, g in ((x, y), (y, z), (z, x)):
        assert sp.expand(_nambu(_sub(T, f), _sub(T, g)) + _sub(T, _nambu(f, g))) == 0
        assert sp.expand(_nambu(_sub(T2, f), _sub(T2, g)) - _sub(T2, _nambu(f, g))) == 0
    for sa, sb in SIGNS:
        assert sp.simplify(_jac(S(sa, sb)).det()) == 1
        for f, g in ((x, y), (y, z), (z, x)):
            assert sp.expand(_nambu(_sub(S(sa, sb), f), _sub(S(sa, sb), g))
                             - _sub(S(sa, sb), _nambu(f, g))) == 0


def test_the_sign_action_has_order_three_over_F2():
    f2 = lambda s: ((s[0] + s[1]) % 2, s[0])
    nz = [(0, 1), (1, 0), (1, 1)]
    assert all(f2(f2(f2(s))) == s for s in nz)
    assert {f2(s) for s in nz} == set(nz) and f2((0, 0)) == (0, 0)


def test_the_exchange_generator_is_exactly_plus_minus_P():
    L = sp.Matrix([[1, 1], [0, 1]]); Rm = sp.Matrix([[1, 0], [1, 1]]); A = L * Rm
    P = sp.Matrix([[0, 1], [1, 0]]); E = sp.eye(2)

    def box(pred, B=2):
        out = set()
        for a in range(-B, B + 1):
            for b in range(-B, B + 1):
                for d in range(-B, B + 1):
                    for e in range(-B, B + 1):
                        X = sp.Matrix([[a, b], [d, e]])
                        if X.det() != 0 and pred(X):
                            out.add(sp.ImmutableMatrix(X))
        return out

    s1 = box(lambda X: X * X == E and sp.simplify(X * L * X.inv() - Rm) == sp.zeros(2, 2))
    s2 = box(lambda X: X * X == E and sp.simplify(X * A * X.inv() - Rm * L) == sp.zeros(2, 2))
    s3 = box(lambda X: sp.simplify((L * X) ** 2 - A) == sp.zeros(2, 2))
    assert s1 == s2 == s3 == {sp.ImmutableMatrix(P), sp.ImmutableMatrix(-P)}
    assert len(box(lambda X: sp.simplify(X * L * X.inv() - Rm) == sp.zeros(2, 2))) > 2


def test_the_wall_is_proved_not_sampled():
    """The whole point: the return is symbolic in c, so the quotient cannot see I's value."""
    step = lambda q: (q[2], q[0], sp.expand(4 * q[0] * q[2] - 4 * q[3] + q[1]),
                      sp.expand(2 * q[0] * q[2] - q[3]))
    assert step(step(step((0, 0, c ** 2, 0)))) == (0, 0, c ** 2, 0)
    line = sp.expand(I.subs({x: 0, y: 0, z: c}))
    assert sp.expand(line - (c ** 2 - 1)) == 0
    assert sp.solve(sp.Eq(line, sp.Rational(1, 4)), c ** 2) == [sp.Rational(5, 4)]


def test_the_six_carry_their_own_STALLED_and_B21_is_kept_separate():
    for b in ("B19", "B21", "B28", "B30", "B34", "B35"):
        assert "**`STALLED`**" in _body(b), b
    flat = lambda s: re.sub(r"\s+", " ", s)
    assert "the physical spacetime dictionary does not" in flat(_body("B21"))
    assert "does not derive the selector" not in flat(_body("B21"))
    row = [ln for ln in _read("docs/LAW_MAP.md").splitlines()
           if "THE PROJECTIVE QUOTIENT IS FULLY NATURAL AND STILL NOT A SELECTOR" in ln]
    assert len(row) == 1 and "**WALL**" in row[0] and "STALLED" in row[0]
    assert "spacetime" in row[0].lower() and "no selector exists" in row[0]
    assert "B27" not in row[0]          # STALLED too, but tower material — not this wall


def test_L166_is_fourteen_contradictions_not_twenty_four():
    """The count the registry publishes, re-derived from the anchored extractor."""
    def token(d):
        b = pathlib.Path(d, "FINDINGS.md").read_text(encoding="utf-8", errors="ignore")
        m = re.search(r"^##\s*Verdict\s*$", b, re.M)
        if not m:
            return None
        w = b[m.end():m.end() + 400]
        m2 = (re.search(r"```(?:text)?\s*\n([A-Z][A-Z0-9_\-]+)", w)
              or re.search(r"\*\*`([A-Z][A-Z0-9_\-]+)`\*\*", w))
        return m2.group(1) if m2 else None

    neg, pos, seen = [], [], set()
    for d in sorted(glob.glob(str(ROOT / "frontier" / "B*"))):
        m = re.match(r"B(\d+)_", pathlib.Path(d).name)
        if not m or not pathlib.Path(d, "arc_verdict.json").is_file() \
           or not pathlib.Path(d, "FINDINGS.md").is_file():
            continue
        n = int(m.group(1))
        if n in seen:
            continue
        seen.add(n)
        if json.loads(pathlib.Path(d, "arc_verdict.json").read_text()).get("verdict") != "PROVED":
            continue
        t = token(d)
        if t is None or t == "PROVED":
            continue
        (neg if t in ("STALLED", "NEEDS_VALIDATION") else pos).append(n)
    assert sorted(neg) == [13, 14, 16, 18, 19, 21, 27, 28, 30, 33, 34, 35, 48, 50], sorted(neg)
    assert all(n < 100 for n in neg)
    assert len(pos) == 9, sorted(pos)      # positive vocabulary is NOT contradiction
    assert "FOURTEEN ARCS SAY `PROVED`" in _read("docs/OPEN_LEADS.md")


def test_the_band_stays_firewalled():
    claims = _read("CLAIMS.md")
    for b in ("B19", "B21", "B28", "B30", "B34", "B35"):
        assert not re.search(rf"\b{b}\b", claims), b
