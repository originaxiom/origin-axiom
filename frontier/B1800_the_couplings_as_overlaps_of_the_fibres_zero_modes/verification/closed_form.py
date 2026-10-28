"""L251: the overlaps' closed forms.  theta[a1,b1](z,t) theta[a2,b2](z,t) = sum_m theta[s_m, b1+b2](2z,2t) C_m with
s_m = (a1+a2+m)/2 and C_m = theta[(a1-a2+m)/2, b1-b2](0,2t) (m = 0, 1; exact).  A flux-two mode chi has characteristic
(c_a, c_b); theta[s, b'] equals theta[c_a, c_b] times e^{2 pi i s db} when s - c_a = da and b' - c_b = db are integers
(theta[a+da, b] = theta[a, b]; theta[a, b+db] = e^{2 pi i a db} theta[a, b]), and is orthogonal to it otherwise.  So every
periodic overlap is K(t) C_m e^{2 pi i s_m db} for its matching m, with one constant K(t) (magnetic translations preserve
the norm).  Checked against the quadrature."""
import numpy as np
import overlaps as O
def thc(a, b, t): return complex(O.theta(a, b, np.array([0j]), t)[0])
def main():
    worst = 0.0
    for t in [complex(a, b) for a, b in ((0.37, 1.2), (0.11, 0.9), (0.0, 1.0), (0.25, 1.5), (-0.3, 1.1), (0.45, 2.0), (0.2, 0.8))]:
        per, ip, ortho, Y = O.run(t, n=96)
        Ks = []; zero_ok = True
        for (p, q, a, b, k), v in Y.items():
            if ip[(p, q, a, b, k)] > 1e-8: continue
            (a1, b1), (a2, b2) = O.CH[p], O.CH[q]
            ca, cb = (k + a) / 2, b
            pred = 0j
            for m in (0, 1):
                s = (a1 + a2 + m) / 2; da, db = s - ca, (b1 + b2) - cb
                if abs(da - round(da)) < 1e-12 and abs(db - round(db)) < 1e-12:
                    pred += thc((a1 - a2 + m) / 2, b1 - b2, 2 * t) * np.exp(2j * np.pi * s * round(db))
            if abs(pred) < 1e-12:
                zero_ok = zero_ok and abs(v) < 1e-9
                continue
            Ks.append(v / pred)
        Ks = np.array(Ks); spread = float(np.max(np.abs(Ks / Ks[0] - 1)))
        worst = max(worst, spread)
        print("tau %-18s periodic overlaps matched %d; K(t) = %.6f%+.6fi; spread %.1e; predicted zeros vanish: %s" % (t, len(Ks), Ks[0].real, Ks[0].imag, spread, zero_ok))
    print("worst spread %.1e" % worst); print("closed_form exit 0")


if __name__ == "__main__":
    main()
