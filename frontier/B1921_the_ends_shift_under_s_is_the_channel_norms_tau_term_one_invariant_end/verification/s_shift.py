"""B1921: under tau -> -1/tau the channel norm of the transported characteristic shifts by exactly -2 pi log|tau|.
Written before the run: S rescales the fibre by 1/|tau|; the kernel has weight one, so |K|^2 d^2u is unchanged; the
excised disc of radius eps becomes one of radius eps/|tau|, and the regularisation -2 pi log(1/eps) moves by
-2 pi log|tau|. So N(c', -1/tau) = N(c, tau) - 2 pi log|tau|, c' = (b, -a) (equally (-b, a): N(-c) = N(c)). B1724 found
the frame covariant under S with the end passed as L + log|tau|: the two cancel in 2 pi L + c_s. Main's code."""
import math, json, pathlib
import step3_norm as S
HERE = pathlib.Path(__file__).resolve().parent
if __name__ == "__main__":
    out = []
    for t in (complex(0.5, 1.1180339887498949), complex(0.13, 1.07), complex(-0.3, 0.9)):
        for c in [(0.3, 0.6), (0.7, 0.2), (0.1, 0.45)]:
            n = S.norm(c, t); nS = S.norm((c[1], -c[0]), -1 / t)
            d = nS + 2 * math.pi * math.log(abs(t)) - n
            out.append({"tau": [t.real, t.imag], "c": c, "N": n, "N_S": nS, "residual": d, "without the shift": nS - n})
            print("tau %.2f%+.2fi c %s: N(c',-1/tau) + 2 pi log|tau| - N(c,tau) = %.2e; without the shift %.3f" % (t.real, t.imag, c, d, nS - n), flush=True)
    (HERE / "s_shift.json").write_text(json.dumps(out, indent=1))
