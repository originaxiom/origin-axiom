"""B281 -- CRUX scoping probe: is E6 GEOMETRICALLY distinguished by 4_1's character variety? Run with sage-python.

For the principal embedding sl(2)->g, Ad = sum over exponents of Sym^{2m}, so
   dim H^1(Ad rho_prin) = sum_{m in exponents(g)} dim H^1(Sym^{2m}) = #exponents = rank(g),
provided dim H^1(Sym^{2k}) = 1 for all k (B264). This script verifies that for EVERY simple type the figure-eight
gives dim H^1 = rank -- i.e. the character variety does NOT single out E6. The 3d-3d INPUT type is geometrically
free; E6 is distinguished ONLY by the arithmetic (McKay output, B266). This is the load-bearing fact for the scope.
"""
import importlib.util
import pathlib

_P = pathlib.Path(__file__).resolve().parents[1] / "B264_e6_character_variety" / "e6_charvar_tangent.py"
_s = importlib.util.spec_from_file_location("b264", _P)
b264 = importlib.util.module_from_spec(_s)
_s.loader.exec_module(b264)

EXPONENTS = {
    "A2=SU(3)": [1, 2], "G2": [1, 5], "A3=SU(4)": [1, 2, 3], "B2/C2": [1, 3],
    "F4": [1, 5, 7, 11], "A4=SU(5)": [1, 2, 3, 4], "D4=SO(8)": [1, 3, 3, 5],
    "E6": [1, 4, 5, 7, 8, 11], "E7": [1, 5, 7, 9, 11, 13, 17],
}


def table():
    need = sorted({k for v in EXPONENTS.values() for k in v})
    h1 = {k: b264.H1_sym(k) for k in need}
    return h1, {G: (len(ex), sum(h1[k] for k in ex)) for G, ex in EXPONENTS.items()}


if __name__ == "__main__":
    h1, tab = table()
    print("dim H^1(Sym^{2k}) all == 1 ?", all(v == 1 for v in h1.values()), h1)
    print(f"{'group':12}{'rank':>5}{'dimH1':>7}  match")
    for G, (rank, d) in tab.items():
        print(f"{G:12}{rank:>5}{d:>7}  {'YES' if rank == d else 'NO'}")
    assert all(rank == d for rank, d in tab.values())
    print("\n=> every simple type gives dim H^1 = rank: E6 is NOT geometrically distinguished.")
