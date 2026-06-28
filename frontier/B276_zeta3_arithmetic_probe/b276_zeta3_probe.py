"""B276 -- T[4_1] Rung 3: the zeta_3 ramified-prime arithmetic probe (the wall-#2 computable test).
FIREWALLED (quantum topology / arithmetic, not physics). Nothing to CLAIMS.md.

THE QUESTION (wall #2, the one computable test): does the figure-eight's quantum invariant Z[T[4_1]] -- the
colored Jones / state integral -- "know about" the arithmetic that selects E6 (B266: trace field Q(sqrt-3) ->
ramified prime 3 -> residue field F_3 -> SL(2,F_3) = 2T = McKay-E6)? This is the E6-end companion to B261, which
found the E8-end signature at zeta_5 (-> Q(sqrt5) -> 2I = E8, period 5 = det).

WHAT IS COMPUTED (reuses B261's verified colored_jones(N,q)):
  * Evaluate J_N(4_1; q) at the roots that generate the figure-eight's OWN trace field Q(sqrt-3) -- zeta_3 and
    zeta_6 = e^{i pi/3} (the Riley t / regular-ideal-tetrahedron shape, B264/B269). The colored-Jones recursion
    DEGENERATES (q-holonomic -> finite/periodic), exactly as B261 found at zeta_5:
        q = zeta_3:  [N]-period 3,  J_N = 1,1,13, 1,1,13, ...        all in Z[zeta_3] = O_{Q(sqrt-3)}
        q = zeta_6:  period 6,      J_N = 1,-1,1,-1,1,89, ...         all in Z[zeta_3]
    (period = order of the root, the E6-end analog of B261's zeta_5 period-5; values are algebraic integers in the
    trace-field ring of integers.)
  * The trace field is Q(sqrt-3) (SnapPy: 4_1 trace field = x^2-2x+4, root 1+i sqrt3); its UNIQUE ramified prime is
    3, with the explicit ramification (1-zeta_3)(1-zeta_3^2) = 3 (so (3) = (1-zeta_3)^2 up to a unit). The residue
    field at that prime is F_3, and SL(2,F_3) = 2T -> McKay-E6 (B266). The state-integral SADDLE sits at
    z = e^{i pi/3} in Q(sqrt-3) (B269) -- Z's geometric data lives in the same field.

THE TWO ENDS, side by side (B258's two-field structure, now from the quantum invariant):
    E6 end:  q in {zeta_3, zeta_6}  ->  trace field Q(sqrt-3)  ->  ramified prime 3  ->  F_3  ->  2T  ->  E6
    E8 end:  q = zeta_5 (B261)      ->  Q(sqrt5)               ->  det = 5            ->  F_5  ->  2I  ->  E8

HONEST SCOPE (PARTIAL by design): this is a COHERENCE -- Z's degeneration locus and saddle field are exactly the
field whose ramified prime yields 2T = McKay-E6. It does NOT exhibit SL(2,F_3) = 2T *acting on* any structure
inside Z, so it does NOT settle the input-E6 = output-E6 conjecture (wall #2); it SHARPENS it. (Matches B266's
guardrail and B269's stated residual.)

Run: python b276_zeta3_probe.py  (pyenv; mpmath + sympy; reuses B261).
"""
import importlib.util
import pathlib

import mpmath as mp

mp.mp.dps = 60

_b261_path = pathlib.Path(__file__).resolve().parents[1] / "B261_golden_root_aj" / "golden_root_aj.py"
_spec = importlib.util.spec_from_file_location("b261", _b261_path)
_b261 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_b261)
colored_jones = _b261.colored_jones                      # the verified Habiro colored-Jones of 4_1

TRACE_FIELD_POLY = "x^2 - 2*x + 4"                        # SnapPy: 4_1 trace field = Q(sqrt-3)
RAMIFIED_PRIME = 3                                        # unique ramified prime of Q(sqrt-3) (disc -3)


def in_ring_of_integers(x, tol=mp.mpf(10) ** -20):
    """Is x in Z[zeta_3] = O_{Q(sqrt-3)}? Returns (bool, a, b) with x = a + b*zeta_3, a,b in Z."""
    b = 2 * x.imag / mp.sqrt(3)
    a = x.real + b / 2
    ai, bi = mp.nint(a), mp.nint(b)
    return (abs(a - ai) < tol and abs(b - bi) < tol), int(ai), int(bi)


def jones_sequence(order, n_terms=15):
    """J_N(4_1; q) at q = a primitive `order`-th root of unity, N=1..n_terms, as (a,b) in Z[zeta_3]."""
    q = mp.e ** (2j * mp.pi / order)
    return [in_ring_of_integers(colored_jones(N, q))[1:] for N in range(1, n_terms + 1)]


def detect_period(seq):
    for P in range(1, len(seq) // 2 + 1):
        if all(seq[i] == seq[i + P] for i in range(len(seq) - P)):
            return P
    return None


def all_integral(order, n_terms=15):
    q = mp.e ** (2j * mp.pi / order)
    return all(in_ring_of_integers(colored_jones(N, q))[0] for N in range(1, n_terms + 1))


def ramification_holds():
    """(1 - zeta_3)(1 - zeta_3^2) = 3 exactly => 3 ramifies in Q(sqrt-3)."""
    z = mp.e ** (2j * mp.pi / 3)
    return abs((1 - z) * (1 - z ** 2) - 3) < mp.mpf(10) ** -40


# ---- verdict (computed; encoded for the test) ----
ZETA3 = {"order": 3, "period": 3, "integral": True, "seq6": [(1, 0), (1, 0), (13, 0), (1, 0), (1, 0), (13, 0)]}
ZETA6 = {"order": 6, "period": 6, "integral": True, "seq6": [(1, 0), (-1, 0), (1, 0), (-1, 0), (1, 0), (89, 0)]}


def verdict():
    return (all_integral(3) and detect_period(jones_sequence(3)) == 3 and
            all_integral(6) and detect_period(jones_sequence(6)) == 6 and
            ramification_holds())


if __name__ == "__main__":
    print("=== B276: the zeta_3 ramified-prime arithmetic probe (E6-end companion to B261) ===\n")
    for order in (3, 6):
        seq = jones_sequence(order)
        print(f"q=zeta_{order}: J_N(4_1) as (a,b)=a+b*zeta_3, N=1..15 = {seq}")
        print(f"          all in Z[zeta_3]=O_Q(sqrt-3): {all_integral(order)}; period = {detect_period(seq)}")
    print(f"\ntrace field of 4_1 = Q(sqrt-3) ({TRACE_FIELD_POLY}); unique ramified prime = {RAMIFIED_PRIME}")
    print(f"ramification (1-zeta_3)(1-zeta_3^2) = 3 exactly: {ramification_holds()}  => residue F_3 -> SL(2,F_3)=2T -> E6 (B266)")
    print("\nTwo ends:  zeta_3/zeta_6 -> Q(sqrt-3) -> prime 3 -> 2T -> E6   vs   zeta_5 -> Q(sqrt5) -> det 5 -> 2I -> E8 (B261)")
    print("PARTIAL by design: a COHERENCE (Z's arithmetic = the 2T field's), NOT 2T acting; does not settle input=output-E6.")
    assert verdict()
    print("\nverdict (degeneration in O_Q(sqrt-3) at the trace-field roots + ramification):", verdict())
