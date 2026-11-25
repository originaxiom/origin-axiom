"""B2002, POST HOC (labelled; written after halving_run.txt showed every non-top neutral factor paired, with a multiplicity
count that did not check sufficiency). The exact identity suggested by the dimensions (neutral = charged sector + 3):
    p_neutral(2x) = 2^deg(p_neutral) * (x - 3) * (x + 3) * x * S(x),   S = one charged sector's polynomial (pC = S^2),
checked exactly in FLINT at mod 27 and mod 81, and shown to fail at mod 5 and 7.
    python3 -B identity_posthoc.py > identity_posthoc_run.txt"""
import importlib.util, pathlib
import flint
HERE = pathlib.Path(__file__).resolve().parent
src = (HERE / "halving.py").read_text().split("summary = {}")[0]
ns = {"__file__": str(HERE / "halving.py")}; exec(compile(src, "halving_head", "exec"), ns)
for N, start, lab in ((27, (3, 3, 3), "mod 27"), (81, (3, 3, 3), "mod 81"), (5, None, "mod 5"), (7, None, "mod 7")):
    n, k, sym, pQ, pC = ns["polys"](N, start)
    c, fs = pC.factor(); assert all(e % 2 == 0 for _, e in fs)
    S = flint.fmpz_poly([1])
    for f, e in fs: S = S * f ** (e // 2)
    lead = int(pC.coeffs()[-1]); assert S * S == pC
    d = pQ.degree()
    lhs = flint.fmpz_poly([int(cf) * 2 ** i for i, cf in enumerate(pQ.coeffs())])
    rhs = flint.fmpz_poly([0, -9, 0, 1]) * S * (2 ** d)
    print("%s: neutral degree %d, charged-sector degree %d; p_neutral(2x) == 2^%d (x^2 - 9) x S(x): %s" % (lab, d, S.degree(), d, lhs == rhs))
