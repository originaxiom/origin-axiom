"""B1872 -- the four facts recomputed with this file's own code; the sealed run says what the findings quote."""
import itertools
import pathlib

import pytest

HERE = pathlib.Path(__file__).resolve().parent
RUN = (HERE / "together_facts_run.txt").read_text(encoding="utf-8")
L, R, ONE = ((1, 0), (1, 1)), ((1, 1), (0, 1)), ((1, 0), (0, 1))


def _mul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def _word(w):
    M = ONE
    for c in w:
        M = _mul(M, L if c == "L" else R)
    return M


def _keeps(M, v=(1, 3)):
    img = ((M[0][0] * v[0] + M[0][1] * v[1]) % 5, (M[1][0] * v[0] + M[1][1] * v[1]) % 5)
    return img in (v, ((-v[0]) % 5, (-v[1]) % 5))


def test_the_marked_line_and_the_counts():
    LR = _word("LR")
    assert _keeps(LR) and not _keeps(_word("L"))                       # LR keeps its line; one letter alone does not
    pos = ["".join(t) for n in range(1, 13) for t in itertools.product("LR", repeat=n)]
    keep = [w for w in pos if _keeps(_word(w))]
    assert len(keep) == 694
    assert all(_keeps(_word(w), (2, 1)) for w in keep)                 # the twin line is kept by every one of them
    neck = lambda w: min(w[s:] + w[:s] for s in range(len(w)))
    cyc = {neck(w) for w in pos if len(w) >= 2 and "L" in w and "R" in w}
    tr2 = [w for w in cyc if (_word(w)[0][0] + _word(w)[1][1]) % 5 in (2, 3)]
    none = sorted((w for w in tr2 if not any(_keeps(_word(w[s:] + w[:s])) for s in range(len(w)))), key=lambda u: (len(u), u))
    assert (len(tr2), len(none), none[0]) == (330, 23, "LLLRLRRR")


def test_one_thread_from_two_base_points_keeps_no_line():
    def group(gens):
        m5 = lambda M: tuple(tuple(x % 5 for x in r) for r in M)
        seen, fr = {m5(ONE)}, [m5(ONE)]
        while fr:
            nx = []
            for a in fr:
                for g in gens:
                    x = m5(_mul(a, g))
                    if x not in seen:
                        seen.add(x)
                        nx.append(x)
            fr = nx
        return seen
    assert len(group([_word("LR"), _word("RL")])) == 120
    assert len(group([_word("LR")])) == 10                             # the control: LR alone generates the line's stabiliser


def test_the_index_in_the_modular_group():
    fg = pytest.importorskip("sympy.combinatorics.free_groups")
    fp = pytest.importorskip("sympy.combinatorics.fp_groups")
    F, s, u = fg.free_group("s, u")
    G = fp.FpGroup(F, [s ** 2, u ** 3])
    r, l = s * u, s * u * u                                             # R = s u and L = s u u, up to sign (checked in the arc's script)
    def elt(w):
        out = F.identity
        for c in w:
            out = out * (l if c == "L" else r)
        return out
    def index(words):
        C = G.coset_enumeration([elt(w) for w in words], max_cosets=20000)
        C.compress()
        return len(C.table)
    assert index(["L", "R"]) == 1 and index(["LL", "R"]) == 3           # the instrument on two known answers
    assert index(["LLLLLLRLR", "LLLLLLRLRLR", "LRRRRRRLR", "LRRRRRRLRLR"]) == 12


def test_the_sealed_run_and_the_findings_agree():
    for s in ("keep the line: 694", "followed by golden periods: 204", "with trace +-2 mod 5: 330", "keeps the marked line: 23 (first: LLLRLRRR)",
              "has 120 elements", "generate a subgroup of index 12", "< L, R > has index 1; < L^2, R > has index 3"):
        assert s in RUN, s
    f = (HERE.parent / "FINDINGS.md").read_text(encoding="utf-8")
    for s in ("The repo sweep:", "the definition is done and the read-out is not", "None of the three is ruled", "derives nothing and selects nothing"):
        assert s in f, s
