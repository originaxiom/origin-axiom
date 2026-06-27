"""B234 locks -- the verified arithmetic from the chat1/chat2 handoff. The two overclaims caught
(H12-Conway-generic, chat2's one-wall) are documented in FINDINGS; here we lock the EXACT facts.
Firewall: pure arithmetic / rep-theory / fusion-category data; nothing to CLAIMS.md."""
import importlib.util
import pathlib

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B234_handoff_verification" / "handoff_verify.py"
_spec = importlib.util.spec_from_file_location("b234_handoff", _PATH)
b234 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b234)


def test_trace1_congruence_law():
    """H27: disc=1-4det is always ==1 mod 4; E8(5)/E6(-3) reachable, E7's sqrt2 (disc 8) is NOT."""
    assert b234.trace1_disc(-1) == 5 and b234.trace1_disc(1) == -3      # E8 (monodromy), E6 (cusp)
    assert all(b234.trace1_disc(d) % 4 == 1 for d in range(-30, 30))    # always 1 mod 4
    assert not any(b234.trace1_disc(d) in (2, 8) for d in range(-200, 200))  # sqrt2 unreachable
    assert b234.trace1_disc(2) == -7                                    # next imaginary rung: Q(sqrt-7)


def test_mckay_congruence_bound():
    """H29: 2T=SL(2,F3), 2I=SL(2,F5), 2O never SL(2,Fp); McKay primes {3,5}, 5 largest."""
    out, mp, too_big = b234.verify_mckay_congruence_bound()
    assert mp == [3, 5] and out["E7 (2O binary octahedral)"] is None and too_big


def test_field_vs_coincidence_vs_susy():
    """H25: E8 field at squarefree(n)=5 (m=1,4,11..); n==5 only m=1; SUSY only m=1."""
    rows = b234.field_vs_coincidence_vs_susy(12)
    assert [r["m"] for r in rows if r["E8_field"]][:3] == [1, 4, 11]
    assert [r["m"] for r in rows if r["n_eq_5"]] == [1]
    assert [r["m"] for r in rows if r["susy"]] == [1]


def test_metallic_field_ladder_silver_is_E7_field():
    """H23: golden -> Q(sqrt5); silver (m=2) -> Q(sqrt2) = E7's (2O) character field."""
    assert b234.metallic_field(1)[1] == 5
    assert b234.metallic_field(2)[1] == 2


def test_primality_overlap_only_at_five():
    """Path2 push: primality + SUSY-overlap co-occur only at m=1 (n=5), over m=1..200."""
    _, susy, cooccur = b234.primality_overlap_cooccurrence(200)
    assert susy == [1] and cooccur == [1]


def test_fibonacci_F_unique_makes_H19_circular():
    """H26: the Fibonacci F-matrix is unitary, det=-1, F^2=I (unique pentagon soln) -> H19 match forced."""
    uni, detm1, invol = b234.verify_fibonacci_unique()
    assert uni and detm1 and invol


def test_cusp_field_is_Qsqrtm3():
    """H22: z=e^{i pi/3} solves z^2-z+1=0; disc -3 -> Q(sqrt-3) (the hyperbolic/E6 field)."""
    zero, disc = b234.verify_cusp_field()
    assert zero and disc == -3
