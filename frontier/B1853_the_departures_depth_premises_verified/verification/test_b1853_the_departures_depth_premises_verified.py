"""B1853 -- the committed run of main's re-derivation holds the explore seat's claims (the full run, explore_facts.py, takes
about two minutes: HL3 enumerates R1 u R2; the cheap sections are re-run here)."""
import itertools, pathlib
HERE = pathlib.Path(__file__).resolve().parent


def test_the_committed_run_holds_the_claims():
    t = (HERE / "explore_facts_run.txt").read_text(encoding="utf-8")
    for s in ("R1: 42768 defects, 643 rung-invisible", "C5(LR) = <LR> (which contains -I): True",
              "N = 2, 3, 4, 5: [True, True, True, True]", "least (6,) at 1.5714462325", "2.1955011599", "gap 0.6241",
              "symmetry at 5:         least length (2, 1, 1, 1, 2)", "charge at 5:           least length (6,)",
              "charge at 4, 5:        least length (21,)", "charge at 2, 3, 4, 5:  least length (61,)",
              "5: [(1, 2)]", "least excess volume (2, 1, 1, 1, 2)", "dV(2,2,2) = 2.3592", "= 0.117"):
        assert s in t, s


def test_the_centraliser_and_the_fixed_point_recomputed():
    mul = lambda A, B: ((A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]), (A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]))
    md = lambda A, n: tuple(tuple(x % n for x in r) for r in A)
    LR = ((2, 1), (1, 1))
    G = [((a, b), (c, d)) for a, b, c, d in itertools.product(range(5), repeat=4) if (a * d - b * c) % 5 == 1]
    cent = [A for A in G if md(mul(A, LR), 5) == md(mul(LR, A), 5)]
    assert len(G) == 120 and len(cent) == 10
    assert [(a, b) for a, b in [(1, 2)] if ((2 * a + b) * 2 - (a + b)) % 5 == 0] == [(1, 2)]      # LR (1, 2) = 4 (1, 2) mod 5
