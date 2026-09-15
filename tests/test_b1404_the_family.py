"""B1404 -- the object's family is Minsky's punctured-torus groups.

Independent re-derivations, not a re-run of the arc script: every number the
relay attached to the citation is recomputed here from the matrices, and the
two corrections (the object is the FIBRE group; the numbers are a MARKING)
are asserted as facts that can fail.

Two regression guards lock the bugs found while writing the arc -- the
float-truncated control and the subs-on-a-simplified-radical -- by asserting
that the BROKEN form is broken. Without them the fixes are invisible.
"""
import subprocess
from pathlib import Path

import pytest

sp = pytest.importorskip("sympy")
from sympy.ntheory.continued_fraction import continued_fraction_periodic as cfp

ROOT = Path(__file__).resolve().parents[1]
Z = sp.Symbol('z')
R = sp.Matrix([[1, 1], [0, 1]])
L = sp.Matrix([[1, 0], [1, 1]])
RL = R * L
PHI = (1 + sp.sqrt(5)) / 2
PHI_BAR = (1 - sp.sqrt(5)) / 2
W = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2          # primitive cube root


def _fixed_eq(M, z=Z):
    return sp.expand((M[0, 0] * z + M[0, 1]) - z * (M[1, 0] * z + M[1, 1]))


# ----------------------------------------------------------- the end invariants
def test_monodromy_is_RL_trace_three():
    assert RL == sp.Matrix([[2, 1], [1, 1]])
    assert RL.det() == 1 and sp.trace(RL) == 3


def test_fixed_points_are_phi_and_its_galois_conjugate():
    assert sp.simplify(_fixed_eq(RL) + (Z**2 - Z - 1)) == 0
    roots = sorted(sp.solve(sp.Eq(_fixed_eq(RL), 0), Z), key=lambda r: -sp.re(r))
    assert sp.simplify(roots[0] - PHI) == 0
    assert sp.simplify(roots[1] - PHI_BAR) == 0
    # conjugate and reciprocal, both exactly
    assert sp.simplify(PHI + PHI_BAR - 1) == 0 and sp.simplify(PHI * PHI_BAR + 1) == 0
    assert sp.simplify(PHI_BAR + 1 / PHI) == 0


def test_attracting_and_repelling_settled_by_the_derivative():
    c, d = RL[1, 0], RL[1, 1]
    dphi = sp.simplify(1 / (c * PHI + d) ** 2)
    dbar = sp.simplify(1 / (c * PHI_BAR + d) ** 2)
    assert sp.simplify(dphi - 1 / PHI**4) == 0 and dphi < 1          # attracting
    assert sp.simplify(dbar - PHI**4) == 0 and dbar > 1              # repelling


def test_dilatation_is_phi_squared():
    lam = max(RL.eigenvals().keys(), key=lambda e: sp.re(e))
    assert sp.simplify(lam - PHI**2) == 0


# --------------------------------------------- correction (b): it is a MARKING
def test_the_pair_moves_under_a_change_of_marking_while_the_manifold_does_not():
    P = sp.Matrix([[1, 1], [0, 1]])
    Mc = P * RL * P.inv()
    assert sp.trace(Mc) == sp.trace(RL)                       # same mapping class
    mob = lambda X, x: sp.simplify((X[0, 0] * x + X[0, 1]) / (X[1, 0] * x + X[1, 1]))
    pair = (mob(P, PHI), mob(P, PHI_BAR))
    assert sp.simplify(_fixed_eq(Mc, pair[0])) == 0           # still fixed points
    assert sp.simplify(pair[0] - PHI) != 0                    # but different numbers
    assert sp.simplify(pair[0] - PHI**2) == 0


def test_every_marked_value_is_noble():
    assert cfp(1, 2, 5) == [[1]]                              # phi
    assert cfp(3, 2, 5) == [2, [1]]                           # phi^2
    assert cfp(-1, 2, 5) == [0, [1]]                          # phi - 1


# ------------------------------------------------- the two kappas / the family
def test_fricke_identity_is_proved_not_recalled():
    p = sp.symbols('p1:9')
    A = sp.Matrix([[p[0], p[1]], [p[2], (1 + p[1] * p[2]) / p[0]]])
    B = sp.Matrix([[p[4], p[5]], [p[6], (1 + p[5] * p[6]) / p[4]]])
    C = A * B * A.inv() * B.inv()
    x, y, z = sp.trace(A), sp.trace(B), sp.trace(A * B)
    assert sp.simplify(sp.trace(C) - (x**2 + y**2 + z**2 - x * y * z - 2)) == 0


def test_banked_fibre_triple_satisfies_the_family_defining_condition():
    x, y, z = 2 + W, 1 - W, 1 - W
    assert sp.simplify(sp.expand(x**2 - 3 * x + 3)) == 0                    # E72's datum
    kappa = sp.simplify(sp.expand(x**2 + y**2 + z**2 - x * y * z - 2))
    assert kappa == -2                                                      # Minsky
    assert sp.simplify(sp.expand(x**2 + y**2 + z**2 - x * y * z)) == 0      # Markov
    assert sp.simplify(sp.Abs(kappa - 2)) == 4


def test_m004_knot_group_is_NOT_a_punctured_torus_group():
    mp = pytest.importorskip("mpmath")
    snappy = pytest.importorskip("snappy")
    with mp.workdps(60):
        G = snappy.Manifold("m004").high_precision().fundamental_group()

        def hp(v):
            f = lambda t: mp.mpf(str(t).replace(" ", ""))
            return mp.mpc(f(v.real()), f(v.imag()))

        def gen(n):
            g = G.SL2C(n)
            return mp.matrix([[hp(g[i, j]) for j in range(2)] for i in range(2)])

        def inv2(X):
            det = X[0, 0] * X[1, 1] - X[0, 1] * X[1, 0]
            return mp.matrix([[X[1, 1] / det, -X[0, 1] / det],
                              [-X[1, 0] / det, X[0, 0] / det]])

        A, B = gen('a'), gen('b')
        C = A * B * inv2(A) * inv2(B)
        kappa = C[0, 0] + C[1, 1]
        u = kappa - 2
        assert abs(abs(u) - 1) < mp.mpf(10) ** -40          # Jorgensen's attained 1
        assert abs(u**3 - 1) < mp.mpf(10) ** -40            # a cube root of unity
        assert abs(u**2 + u + 1) < mp.mpf(10) ** -40        # a PRIMITIVE one
        # the decisive negative: the commutator is NOT parabolic
        assert abs(kappa + 2) > mp.mpf("3.6")


# --------------------------------------------------------------- the ladder
@pytest.mark.parametrize("m", list(range(1, 9)))
def test_metallic_end_invariant_and_shadow_modulus(m):
    Am = sp.Matrix([[1 + m**2, m], [m, 1]])
    Xm = sp.Matrix([[m, 1], [1, 0]])
    assert sp.expand(R.subs(1, 1) * 1) is not None            # keep sympy imported
    assert sp.expand(Xm * Xm) == Am and Xm.det() == -1
    assert sp.simplify(sp.expand(_fixed_eq(Am) + m * (Z**2 - m * Z - 1))) == 0
    assert sp.discriminant(Z**2 - m * Z - 1, Z) == m**2 + 4   # the shadow modulus
    mu = sp.nsimplify((m + sp.sqrt(m**2 + 4)) / 2)
    mub = (m - sp.sqrt(m**2 + 4)) / 2
    assert sp.simplify(_fixed_eq(Am, mu)) == 0
    assert sp.simplify(mu + mub - m) == 0                     # Vieta, form-free
    assert sp.simplify(sp.expand(mu * mub) + 1) == 0
    assert sp.simplify(max(Am.eigenvals().keys(), key=lambda e: sp.re(e)) - mu**2) == 0
    assert cfp(m, 2, m**2 + 4) == [[m]]                       # purely periodic


# ------------------------------------------------------- the regression guards
def test_guard_complex_truncation_would_break_the_identification():
    """E75 instance #9: the control was built with complex(sp.N(...)), which
    truncates 50 exact digits to 16. Assert the BROKEN form is broken."""
    mp = pytest.importorskip("mpmath")
    with mp.workdps(60):
        exact = mp.mpc(mp.mpf(-1) / 2, mp.sqrt(3) / 2)
        truncated = mp.mpmathify(complex(sp.N(W, 50)))
        assert abs(exact - truncated) > mp.mpf(10) ** -20     # loses ~34 digits
        assert abs(exact - truncated) < mp.mpf(10) ** -16


def test_guard_subs_on_a_simplified_radical_silently_does_nothing():
    """E75, third mechanism: nsimplify turns (2+sqrt(8))/2 into 1+sqrt(2), so
    subs(sqrt(8) -> -sqrt(8)) matches nothing and EVEN m failed a true claim."""
    m = 2
    mu = sp.nsimplify((m + sp.sqrt(m**2 + 4)) / 2)
    naive = mu.subs(sp.sqrt(m**2 + 4), -sp.sqrt(m**2 + 4))
    assert naive == mu                                        # the substitution no-ops
    mub = (m - sp.sqrt(m**2 + 4)) / 2
    assert sp.simplify(naive - mub) != 0                      # so it gives the wrong root
    assert sp.simplify(mu + mub - m) == 0                     # while Vieta is fine


# ------------------------------------------------------------- absence audit
# PINNED to the commit B1404 started from. These tests lock what the arc CLAIMED,
# about the state it claimed it about -- and pinning is itself the finding: run
# against the working tree, they all pass trivially, because the arc's own prose
# now names Minsky, Marden, Maskit and Bromberg on eight doc surfaces. E78.
BASE = "d08d1f98"
ARC = "frontier/B1404_the_family_has_a_name/"


def _grep(term):
    cmd = ["git", "grep", "-I", "-n", "-E", "-i", "--", term, BASE,
           "--", "*.md", "*.py", "*.json", "*.tex"]
    out = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True).stdout
    rows = []
    for line in out.splitlines():
        parts = line.split(":", 3)
        if len(parts) < 4 or parts[1].startswith(ARC):
            continue
        rows.append((parts[1], parts[3]))
    return rows


# PORTABILITY GUARD (2026-09-16, main's pre-merge suite): BASE is reachable from this lane's
# history and NOT from main's own head, so every BASE-dependent test below failed on main's
# checkout. An absence audit pinned to a revision is a claim about a HISTORICAL state: if that
# state is not in the checkout the claim is UNVERIFIABLE, not false, and the honest outcome is a
# SKIP with a reason -- never a silent pass, which is what `test_the_base_revision_exists` was
# written to prevent. So the skip covers every BASE-dependent test at once: nothing below can
# pass vacuously, and a checkout without this lane's history no longer reds the suite. The
# assertion stays where it belongs -- inside the guard, for checkouts that DO have the commit.
_BASE_PRESENT = subprocess.run(["git", "cat-file", "-e", BASE + "^{commit}"],
                               cwd=ROOT, capture_output=True).returncode == 0
_needs_base = pytest.mark.skipif(
    not _BASE_PRESENT,
    reason=f"{BASE} is not reachable from this checkout -- B1404's absence audit is a claim about "
           f"that revision, so it is unverifiable here rather than false (it resolves once this "
           f"lane's history is merged)")


@_needs_base
def test_the_base_revision_exists():
    """Without this, every absence test below passes by returning nothing."""
    r = subprocess.run(["git", "cat-file", "-e", BASE + "^{commit}"], cwd=ROOT)
    assert r.returncode == 0, f"{BASE} is gone -- B1404's audit is unreproducible"
    assert len(_grep("Markov")) > 500, "the pinned revision greps empty -- wrong path spec?"


@pytest.mark.parametrize("term", ["Minsky", "Marden", "Maskit", "Bromberg",
                                  "ending lamination"])
@_needs_base
def test_the_genuinely_absent_half_of_the_literature(term):
    assert _grep(term) == [], f"{term} was not absent at {BASE} -- B1404 sect. 6 is wrong"


@pytest.mark.parametrize("term,least", [("Gu.ritaud", 18), ("Futer", 58), ("Floyd", 25),
                                        ("Hatcher", 25), ("Lackenby", 5),
                                        ("J.rgensen", 93), ("Farey", 47)])
@_needs_base
def test_the_relay_was_wrong_about_these_they_are_present(term, least):
    """The relay said 'not one of them is in the record'. Counts at BASE."""
    assert len(_grep(term)) == least, f"{term}: B1404 sect. 6 tabulates {least} lines"


@_needs_base
def test_epstein_is_present_only_as_the_zeta_function():
    """Absent, but MASKED: a bare grep reports 15 lines and none is Epstein-Penner."""
    lines = _grep("Epstein")
    assert len(lines) == 15, "the homonym count moved -- recheck B1404 sect. 6"
    zeta = [l for l in lines if any(k in l[1].lower() for k in
                                    ("zeta", "bessel", "eisenstein", "davenport",
                                     "epstein sum", "lattice"))]
    assert zeta == lines, f"a non-zeta Epstein appeared: {set(lines) - set(zeta)}"


@_needs_base
def test_the_scale_of_the_unnamed_family_condition():
    """The arc's headline number: the defining condition, banked without the name.

    Counted across EVERY spelling and by full alternatives, never by a character
    class: the Unicode minus is three bytes and a class matches one, which
    under-counted 442 as 215 (E75 #11).
    """
    minus, kappa = "\u2212", "\u03ba"
    pat = "|".join(k + " ?= ?" + d + "2" for k in ("kappa", kappa) for d in ("-", minus))
    assert len(_grep(pat)) == 442
    assert len({f for f, _ in _grep(pat)}) == 187
    assert len(_grep("Markov")) == 930


@_needs_base
def test_guard_a_bracket_expression_makes_the_count_locale_dependent():
    """E75 #11. The SAME pattern, corpus and git return 215 or 442 depending on
    the process locale, because a bracket expression is byte-oriented outside a
    UTF-8 locale and the Unicode minus is three bytes. The full-alternative form
    is locale-independent. Nothing errors; the wrong number is simply plausible.

    Python sets LC_CTYPE=C.UTF-8 for its children (PEP 538), so the bug is
    invisible from a script and visible from a plain shell -- which is exactly
    how it was found, and why the locale is now pinned rather than inherited.
    """
    import os
    minus, kappa = "\u2212", "\u03ba"
    klass = "kappa ?= ?[-" + minus + "]2|" + kappa + " ?= ?[-" + minus + "]2"
    alt = "|".join(k + " ?= ?" + d + "2" for k in ("kappa", kappa) for d in ("-", minus))

    def count(pat, loc):
        env = {**os.environ}
        for v in ("LC_ALL", "LC_CTYPE", "LANG"):
            env.pop(v, None)
        if loc:
            env["LC_ALL"] = loc
        cmd = ["git", "grep", "-I", "-n", "-E", "-i", "--", pat, BASE,
               "--", "*.md", "*.py", "*.json", "*.tex"]
        return len(subprocess.run(cmd, cwd=ROOT, capture_output=True,
                                  text=True, env=env).stdout.splitlines())

    # PORTABILITY (2026-09-16, main's macOS worktree): this pinned the locale NAME "C.UTF-8",
    # which exists on glibc and NOT on macOS -- there git falls back to byte-oriented C and the
    # count came back 215, reading as a failed assertion when the only thing wrong was the name.
    # A test about UTF-8 SEMANTICS must select a locale by semantics, not by name.
    #
    # The detector is the bug itself and needs no pinned number: under UTF-8 semantics the
    # bracket form and the full-alternative form agree; under byte semantics they cannot, because
    # the Unicode minus is three bytes and the bracket matches one of them. So the first candidate
    # where klass == alt IS a UTF-8 locale, established rather than assumed.
    utf8 = next((loc for loc in ("C.UTF-8", "en_US.UTF-8", "UTF-8")
                 if count(klass, loc) == count(alt, loc)), None)
    if utf8 is None:
        import pytest as _pt
        _pt.skip("no locale on this machine gives git UTF-8 semantics (tried C.UTF-8, "
                 "en_US.UTF-8, UTF-8) -- the locale-dependence this guard documents is real "
                 "but cannot be exhibited here")

    assert count(klass, "C") == 215          # byte-oriented: under-counts by half
    assert count(klass, utf8) == 442         # same pattern, different answer
    assert count(alt, "C") == 442            # the fix is locale-independent
    assert count(alt, utf8) == 442


def test_the_ladder_arithmetic_was_already_banked():
    """Sect. 5 is citation, not extension -- lock the source it was found in."""
    src = ROOT / "papers" / "metallic_one_object" / "SYNTHESIS.md"
    text = src.read_text()
    assert "fundamental unit" in text and "m^2+4" in text
    assert "banked K002" in text
    assert "Markov surface" in text and "\\kappa=-2" in text
