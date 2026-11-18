"""B1957: the left unitaries of B1953's covariance law, read out (the web seat's section 13.2, item 3; 2026-11-18).  Main's own
code only: B1953's weyl_operator.py fits Y(g tau, w) = c phi U_L Y(tau, w g) U_R^dagger for g = T and S at the 24 points.  It
did not print U_L's form.  Here, for the down and up sectors, both readings and both base points: |U_L(T)| and |U_L(S)| as
permutations of the three blocks; the projective orders of U_L(T), U_L(S) and their product; the order of the group they
generate up to phases; whether U_L(T) is a real signed permutation up to one phase; and U_L against U_R.
The web seat's note W-A2 states these (its lines 110 to 116 and 187) as its referee's algebra, not computed on the frame."""
import sys, itertools, pathlib, numpy as np
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1953_*")) / "verification")); import weyl_operator as WO
def proj_order(U, nmax=24):
    P = np.eye(3, dtype=complex)
    for n in range(1, nmax + 1):
        P = P @ U
        d = P / P[np.unravel_index(np.argmax(abs(P)), P.shape)]
        if np.abs(d - np.diag(np.diag(d))).max() < 1e-8 and np.abs(np.abs(np.diag(d)) - 1).max() < 1e-8 and np.abs(np.diag(d) - d[0, 0]).max() < 1e-8: return n
    return None
def group_order(gens):
    key = lambda M: tuple(np.round(M / (M.flat[np.flatnonzero(abs(M) > 1e-6)[0]] / abs(M.flat[np.flatnonzero(abs(M) > 1e-6)[0]])), 5).flatten().tolist())
    seen = {key(np.eye(3, dtype=complex)): np.eye(3, dtype=complex)}; todo = [np.eye(3, dtype=complex)]
    while todo and len(seen) < 500:
        g = todo.pop()
        for h in gens:
            n = g @ h; k = key(n)
            if k not in seen: seen[k] = n; todo.append(n)
    return len(seen)
rows = []
for (tx, ty) in WO.BASES:
    for sec in ("down", "up"):
        Ys, _ = WO.images(tx, ty, sec)
        for rd in ("S", "St"):
            lt, ls = WO.law(Ys["t"][rd], Ys["T"][rd], "T"), WO.law(Ys["t"][rd], Ys["S"][rd], "S")
            UT, US = lt["UL"], ls["UL"]; A = np.abs(UT).round(3); B = np.abs(US).round(3)
            perm = lambda M: all(sorted(r) == [0, 0, 1] for r in M.tolist()) and all(sorted(c) == [0, 0, 1] for c in M.T.tolist())
            ph = UT[np.abs(UT) > 0.5]; real_signed = np.abs((ph / ph[0]).imag).max() < 1e-8        # up to one phase, the entries are +-1
            lr = lambda l: min(np.abs(l["UL"] - c * l["UR"]).max() for c in [np.vdot(l["UR"].flatten(), l["UL"].flatten()) / 3])
            rows.append((tx, sec, rd, max(lt["residual"], ls["residual"]), perm(A), perm(B), [int(np.argmax(r)) for r in A], [int(np.argmax(r)) for r in B], proj_order(UT), proj_order(US), proj_order(US @ UT), group_order([UT, US]), bool(real_signed), max(lr(lt), lr(ls))))
for r in rows: print("base %s %-4s %-2s: law residual %.1e; |U_L(T)|, |U_L(S)| permutations: %s, %s (rows -> columns %s, %s); projective orders of T, S, ST: %s, %s, %s; group generated, up to phases: %d; U_L(T) real signed up to one phase: %s; |U_L - c U_R| at most %.1e" % r)
print("all eight cases: orders (4, 2, 3): %s; group order 24: %s" % (all(r[8:11] == (4, 2, 3) for r in rows), all(r[11] == 24 for r in rows)))


# ---- ADDED 2026-11-18 (the web seat's section 15.2, item 1): the first read-out tested reality for U_L(T) only, and for S only
# that |U_L(S)| is a permutation, which cannot tell a real U_L(S) from a complex one.  Here: U_L(S) too is a real signed
# permutation up to one phase; with the phases removed U_L and U_R are ONE real matrix R (one sign for both); and, with that
# one R on both sides, the constant phase the law leaves under T at the points a = 0, where the level-5 phase is 1.
def realise(U):
    ph = U[np.abs(U) > 0.5]; R = U / (ph[0] / abs(ph[0])); return R, float(np.abs(R.imag).max())
more = []
for (tx, ty) in WO.BASES:
    for sec in ("down", "up"):
        Ys, _ = WO.images(tx, ty, sec)
        for rd in ("S", "St"):
            got = {}
            for gen in ("T", "S"):
                l = WO.law(Ys["t"][rd], Ys[gen][rd], gen); RL, imL = realise(l["UL"]); RR, imR = realise(l["UR"])
                if np.abs(RL - RR).max() > 1e-6: RR = -RR
                tr = next(t for t in WO.TRANS[gen] if (lambda Zm, Y: np.abs(Y - (np.vdot(Zm, Y) / np.vdot(Zm, Zm)) * Zm).max() / np.abs(Y).max() < 1e-8)(RL @ Ys["t"][rd][t(*WO.PTS[0])] @ RR.T, Ys[gen][rd][WO.PTS[0]]))
                turns = sorted({round(float(np.angle(np.vdot(RL @ Ys["t"][rd][tr(*w)] @ RR.T, Ys[gen][rd][w])) / (2 * np.pi)) % 1, 6) % 1 for w in WO.PTS if w[0] == 0})
                got[gen] = (max(imL, imR), float(np.abs(RL - RR).max()), RL.real.round(0).astype(int).tolist(), turns, bool(np.abs(np.abs(RL.real) - np.abs(RL.real).round(0)).max() < 1e-8))
            more.append((tx, sec, rd, got))
for tx, sec, rd, g in more:
    print("base %s %-4s %-2s: after one phase is removed, U_L(T) = %s and U_L(S) = %s, imaginary parts at most %.1e, entries 0 and +-1: %s, %s; U_R is the same real matrix to %.1e; with it on both sides the constant under T at the points a = 0 is %s of a turn"
          % (tx, sec, rd, g["T"][2], g["S"][2], max(g["T"][0], g["S"][0]), g["T"][4], g["S"][4], max(g["T"][1], g["S"][1]), ", ".join("%.4f" % t for t in g["T"][3])))
print("all eight cases: U_L(S) a real signed permutation up to one phase: %s; U_L = U_R = one real R: %s" % (all(g["S"][0] < 1e-8 and g["S"][4] for *_, g in more), all(max(g["T"][1], g["S"][1]) < 1e-8 for *_, g in more)))
print("the constant under T with one real R on both sides: reading S %s, reading St %s (turns; the web seat's note W-A2, line 110, has one eighth, from its referee's algebra with the Higgs direction moving)"
      % (sorted({t for _, _, rd, g in more if rd == "S" for t in g["T"][3]}), sorted({t for _, _, rd, g in more if rd == "St" for t in g["T"][3]})))


# ---- ADDED 2026-11-18, later (the web seat's section 17.2): the constant under T is one statement.  The Higgs triplet has its
# own T-law; main's constant above keeps the Higgs's phase inside the coupling, the seat's line 110 moves the Higgs with it.
#  H1  on main's own Higgs triplet (B1945's frame, te.B[1]): c3(tau + 1) = M c3(tau), fitted at six moduli; M = h Q with h a phase
#      and Q real orthogonal of determinant 1: h, Q's eigenphases.
#  H2  in the reading S-tilde = eps conj(S) eps^T the triplet is conjugated, so its phase is conj(h); main's constant under T in
#      each of the eight cases divided by the Higgs's own phase in that reading.
#  H3  R's determinant, and its eigenphases (line 113 of the note).
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1945_*")) / "verification")); import determinant_law as DLW
mpw, tew = DLW.mp, DLW.te
taus = [mpw.mpc("0.13", "1.7"), mpw.mpc("0.31", "1.2"), mpw.mpc("-0.2", "1.4"), mpw.mpc("0.05", "2.1"), mpw.mpc("0.4", "1.1"), mpw.mpc("-0.35", "1.6")]
c3 = lambda t: np.array([complex(tew.ev(cc, t)) for cc in tew.B[1]])
A3 = np.array([c3(t) for t in taus]); B3 = np.array([c3(t + 1) for t in taus]); Mh = np.linalg.lstsq(A3, B3, rcond=None)[0].T
fit = max(np.abs(B3[i] - Mh @ A3[i]).max() for i in range(len(taus)))
h = min([np.linalg.det(Mh) ** (1 / 3) * np.exp(2j * np.pi * k / 3) for k in range(3)], key=lambda x: np.abs((Mh / x).imag).max()); Qh = (Mh / h).real
turn = lambda z: round(float((np.angle(z) / (2 * np.pi)) % 1), 6) % 1
print("H1: the Higgs triplet under tau + 1: c3(tau + 1) = h Q c3(tau) at six moduli to %.1e; h = %.4f of a turn; |Im(M/h)| %.1e; Q orthogonal to %.1e with determinant %.4f; Q's eigenphases %s (a convention: with -Q, of determinant -1, h is %.4f of a turn)"
      % (fit, turn(h), np.abs((Mh / h).imag).max(), np.abs(Qh @ Qh.T - np.eye(3)).max(), np.linalg.det(Qh), sorted(round(float(x), 4) for x in (np.angle(np.linalg.eigvals(Qh)) / (2 * np.pi)) % 1), turn(-h)))
hph = {"S": turn(h), "St": turn(np.conj(h))}
over = sorted({round((t - hph[rd]) % 1, 6) % 1 for _, _, rd, g in more for t in g["T"][3]})
print("H2: the Higgs's own phase: %s of a turn in S and %s in S-tilde; main's constant under T divided by it, over the eight cases: %s of a turn: the channels' part. So the coupling's constant (i in S, 1 in S-tilde) is the channels' eighth times the Higgs's own phase; the web seat's line 110 had the Higgs's eighth as the coupling's constant and is withdrawn by the seat (its section 17.2, corrected)" % (hph["S"], hph["St"], over))
Rm = np.array(more[0][3]["T"][2], float)
print("H3: R = %s has determinant %d; its eigenphases %s of a turn (the note's line 113: 0, 1/4 and 3/4); -R would have determinant %d and eigenphases %s"
      % (Rm.astype(int).tolist(), round(np.linalg.det(Rm)), sorted(round(float(x), 4) for x in (np.angle(np.linalg.eigvals(Rm)) / (2 * np.pi)) % 1), round(np.linalg.det(-Rm)), sorted(round(float(x), 4) for x in (np.angle(np.linalg.eigvals(-Rm)) / (2 * np.pi)) % 1)))
#  H4  (added 2026-11-18, at the web seat's section 18.2, item 1: main had computed the quotient of its constant by the Higgs's own
#      phase, not the channels' law itself) THE CHANNELS' LAW WITH A FREE HIGGS INPUT, on main's own code: with the channels'
#      matrix Mw of B1945's determinant_law.parts and an arbitrary Higgs input x in place of the triplet (S = x . (QI, QJ, QK) in
#      the reading S, eps conj(S) eps^T in S-tilde), Y(tau + 1; Q x) = c R Y(tau; x) R^T at the points with a = 0 (which tau + 1
#      fixes), both base points, both sectors, five random complex x; the constant c, and with -Q in place of Q.
from fractions import Fraction as FrH
FMh = DLW.FM; _, QIh, QJh, QKh, EPSh, _, _, BLKh = FMh.setup()
def y_free(Mw, x, rd):
    S = mpw.mpc(x[0]) * QIh + mpw.mpc(x[1]) * QJh + mpw.mpc(x[2]) * QKh
    if rd == "St": S = EPSh * mpw.matrix([[mpw.conj(S[i, j]) for j in range(2)] for i in range(2)]) * EPSh.T
    return np.array([[complex(sum(((Ca.T * EPSh * S * Cb)[m, n] * Mw[m, n] for m in range(2) for n in range(2)), mpw.mpc(0))) for Cb in BLKh] for Ca in BLKh])
rngh = np.random.default_rng(5); xs = [rngh.normal(size=3) + 1j * rngh.normal(size=3) for _ in range(5)]
law4 = {"S": set(), "St": set()}; law4m = {"S": set(), "St": set()}; res4 = 0.0; n4 = 0
for (tx, ty) in WO.BASES:
    for sec in ("down", "up"):
        for j5 in range(1, 5):
            Mw0 = DLW.parts(tx, ty, FrH(0), FrH(j5, 5), sec)[1]; Mw1 = DLW.parts(mpw.nstr(mpw.mpf(tx) + 1, 30), ty, FrH(0), FrH(j5, 5), sec)[1]
            for x in xs:
                for rd in ("S", "St"):
                    for sgn, store in ((1, law4), (-1, law4m)):
                        Z = Rm @ y_free(Mw0, x, rd) @ Rm.T; Y1 = y_free(Mw1, sgn * (Qh @ x), rd); c = np.vdot(Z, Y1) / np.vdot(Z, Z)
                        res4 = max(res4, float(np.abs(Y1 - c * Z).max() / np.abs(Y1).max())); store[rd].add(turn(c)); n4 += 1
print("H4: the channels' law with a free Higgs input x (Q of determinant 1 from H1, R from H3): Y(tau + 1; Q x) = c R Y(tau; x) R^T over %d cases (two base points, two sectors, the four points with a = 0, five x, both readings, Q and -Q): worst residual %.1e; c = %s of a turn in S and %s in S-tilde with Q; %s and %s with -Q (determinant -1). With the Higgs's own phase (H1: an eighth in S, minus an eighth in S-tilde) the coupling's constant is the product: a quarter turn in S and none in S-tilde, main's constants"
      % (n4, res4, sorted(law4["S"]), sorted(law4["St"]), sorted(law4m["S"]), sorted(law4m["St"])))
