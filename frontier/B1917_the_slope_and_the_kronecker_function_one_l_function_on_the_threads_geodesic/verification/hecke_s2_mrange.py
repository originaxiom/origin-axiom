"""Review 82 (agy-exp's finding F3 on this arc): the one kept row of hecke_s2.json above 1e-7 is the character with no
phase in n, level (+LR, 3), (i, j) = (1, 0), rel 2.03e-4 at the default m-range |m| <= 60. The page said it "converges
to 1.6e-7 as the m-range grows", a figure no committed run produced. This run grows the m-range on that row with
hecke_s2.py's own lhs and rhs (unchanged) and writes what it finds. It also computes a planted control for the lock:
the same left side against the right side of the transposed character (j, i), which must not agree.
Main's code; nothing of any seat's is read or run."""
import io, contextlib, json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import hecke_s2 as H

if __name__ == "__main__":
    SL = H.B._sl()
    with contextlib.redirect_stdout(io.StringIO()):
        N, F, S = SL.exact_slopes(1, "LR", 3)
    M = H.B.abel_M(SL, 1, "LR", 3)
    R, n = H.rhs(M, 1, 0, N, X=8000.0)
    out = {"level": ["+LR", 3], "ij": [1, 0], "N": N, "rhs X": 8000.0, "orbit reps": n, "runs": []}
    for Mmax, Nmax in [(60, 4000), (120, 4000), (240, 8000)]:
        L = H.lhs(M, (1 / N, 0.0), Mmax=Mmax, Nmax=Nmax)
        rel = abs(L - H.H(2) * R) / abs(L)
        out["runs"].append({"Mmax": Mmax, "Nmax": Nmax, "rel": rel})
        print("Mmax %d Nmax %d rel %.2e" % (Mmax, Nmax, rel), flush=True)
    # the planted control on the golden level: the transposed character's right side against (1, 2)'s left side
    with contextlib.redirect_stdout(io.StringIO()):
        N2, F2, S2 = SL.exact_slopes(1, "LR", 2)
    M2 = H.B.abel_M(SL, 1, "LR", 2)
    L2 = H.lhs(M2, (1 / N2, 2 / N2), Mmax=40, Nmax=1500)
    Rt, _ = H.rhs(M2, 2, 1, N2, X=4000.0)
    Rr, _ = H.rhs(M2, 1, 2, N2, X=4000.0)
    out["plant golden (1,2) vs (2,1)"] = {"rel right": abs(L2 - H.H(2) * Rr) / abs(L2), "rel transposed": abs(L2 - H.H(2) * Rt) / abs(L2)}
    print("golden level: right character rel %.2e, transposed character rel %.2e" % tuple(out["plant golden (1,2) vs (2,1)"].values()))
    (HERE / "hecke_s2_mrange.json").write_text(json.dumps(out, indent=1))
