"""B1957: the agy audit lane's P-753 note as revised after main's B1866 (its head d1c71f255): the claim that on the
'actual half-form bundles' the three channels induced over the three backgrounds have groups of order 96 (equivalent
to the weave's triplet T, its partner to conj T), 288 and 72, where the one-form proxy has 24.  Tested by main as
algebra, with B1866's own code (join_scrutiny.py is imported; it reruns B1866's parts): a line induced from the
stabiliser of one background, twisted by the character chi_m of the Dedekind eta's power (L -> zeta_24^m,
R -> zeta_24^-m).  WHICH mode of the lane's operator carries which line and which power of eta is the lane's
analysis and is not checked here.  Data-free."""
import sys, pathlib, io, contextlib, functools
import numpy as np
print = functools.partial(print, flush=True)
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1866_*")) / "verification"))
with contextlib.redirect_stdout(io.StringIO()): import join_scrutiny as J


def study(psi, m):
    r = J.induced(*psi); a, b = J.z24 ** m * r[0], J.z24 ** (-m) * r[1]; G = J.group([a, b], 3, cap=20000); centre = [g for g in G if J.is_scalar(g)]
    S = a @ np.linalg.inv(b) @ a; s4 = "+1" if np.abs(np.linalg.matrix_power(S, 4) - np.eye(3)).max() < 1e-9 else ("-1" if np.abs(np.linalg.matrix_power(S, 4) + np.eye(3)).max() < 1e-9 else "other")
    return len(G), len(centre), len(G) // len(centre), s4, J.equivalent(J.TL, J.TR, a, b)[0], J.equivalent(J.TL.conj(), J.TR.conj(), a, b)[0]


if __name__ == "__main__":
    print("the weave's triplet T: order %d" % len(J.GT))
    for psi, name in (((-1, 1), "the one-form line (signs -1 on L^2, +1 on S)"), ((1, 1), "the line with signs (+1, +1)"), ((1, -1), "the line with signs (+1, -1)"), ((-1, -1), "the line with signs (-1, -1)")):
        if J.induced(*psi) is None: print("%s: not a character of the stabiliser" % name); continue
        for m, why in ((0, "no twist (the proxy)"), (3, "eta^3"), (21, "conj eta^3"), (23, "conj eta"), (1, "eta"), (9, "chi_9, B1866's twist"), (15, "chi_15")):
            o, z, pr, s4, eT, eTb = study(psi, m); print("  %-46s twisted by chi_%-2d (%s): order %d, centre %d, modulo scalars %d, S^4 = %s; equivalent to T: %s; to conj T: %s" % (name, m, why, o, z, pr, s4, eT, eTb))
