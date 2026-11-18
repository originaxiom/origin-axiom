"""B1957: agy-exp's X-ENDGAME campaign (five result notes, read in full through the mask): the exact facts under its
statements that main's other checks do not already hold.  Nothing of the seat's is run.  (The carrier's cohomology,
the 45 points and their orbits, the level-three pair, the three-term Majorana matrix, the mixed products and the
figure-eight's shape are in physical_endgame_review.py and physical_endgame_outputs.py.)
 H1  M = T S^-1 T^-1 S with T = [[1, 1], [0, 1]], S = [[0, -1], [1, 0]]; M^2 + 1 = 3M; det(M - 1), det(M + 1) and
     det(3M) are -1, 5, 9, so |det(M^4 - 1)| = 45; M^2 - 1 has determinant -5 and its fixed points have order 1 or 5.
 H2  the trace normalisation: with Y = diag(-1/3, -1/3, -1/3, 1/2, 1/2), (3/5) tr Y^2 = 1/2, the same as a
     generator of SU(2) or SU(3) in the five; so k_2/k_1 = 3/5.
 H3  on the six two-forms of a four-space the Hodge star squares to -1 in signature (1, 3) and to +1 in signature
     (4, 0); (1 - i star)/2 is a projector in the first case and in the second misses by sqrt(6)/2.
 H4  W(u) = (u - 1)(u^2 - 5u + 1) has W'(1) = -3."""
import functools, itertools, math
import numpy as np
import sympy as sp
print = functools.partial(print, flush=True)

def star(eta):
    """the Hodge star on two-forms e^i ^ e^j (i < j) for a diagonal metric eta"""
    pairs = list(itertools.combinations(range(4), 2)); S = np.zeros((6, 6))
    for a, (i, j) in enumerate(pairs):
        k, l = [x for x in range(4) if x not in (i, j)]; sign = sp.LeviCivita(i, j, k, l)
        S[pairs.index((k, l)), a] = float(sign) * eta[i] * eta[j]
    return S

if __name__ == "__main__":
    M = sp.Matrix([[2, 1], [1, 1]]); T = sp.Matrix([[1, 1], [0, 1]]); S = sp.Matrix([[0, -1], [1, 0]]); I2 = sp.eye(2)
    fix2 = [(a, b) for a in range(15) for b in range(15) if ((sp.Matrix([[a, b]]) * (M ** 2 - I2)).applyfunc(lambda x: x % 15)).is_zero_matrix]
    print("H1: T S^-1 T^-1 S = M: %s; M^2 + 1 = 3M: %s; det(M - 1), det(M + 1), det(3M): %s, %s, %s; det(M^4 - 1) = %s; det(M^2 - 1) = %s, with %d fixed points on the 15-torsion, of orders %s"
          % (T * S.inv() * T.inv() * S == M, M ** 2 + I2 == 3 * M, (M - I2).det(), (M + I2).det(), (3 * M).det(), (M ** 4 - I2).det(), (M ** 2 - I2).det(), len(fix2), sorted({math.lcm(15 // math.gcd(a, 15), 15 // math.gcd(b, 15)) for a, b in fix2})))
    Y = sp.diag(-sp.Rational(1, 3), -sp.Rational(1, 3), -sp.Rational(1, 3), sp.Rational(1, 2), sp.Rational(1, 2)); t3 = sp.diag(0, 0, 0, sp.Rational(1, 2), -sp.Rational(1, 2)); l3 = sp.diag(sp.Rational(1, 2), -sp.Rational(1, 2), 0, 0, 0)
    print("H2: (3/5) tr Y^2 = %s; tr of a weak and of a colour generator squared: %s, %s" % (sp.Rational(3, 5) * (Y ** 2).trace(), (t3 ** 2).trace(), (l3 ** 2).trace()))
    SL, SE = star([1, -1, -1, -1]), star([1, 1, 1, 1]); PL, PE = (np.eye(6) - 1j * SL) / 2, (np.eye(6) - 1j * SE) / 2
    print("H3: star^2 in signature (1, 3): %s; in (4, 0): %s; |P^2 - P| for P = (1 - i star)/2: %.3e and %.6f (sqrt(6)/2 = %.6f)"
          % ("-1" if np.allclose(SL @ SL, -np.eye(6)) else "?", "+1" if np.allclose(SE @ SE, np.eye(6)) else "?", np.linalg.norm(PL @ PL - PL), np.linalg.norm(PE @ PE - PE), math.sqrt(6) / 2))
    u = sp.Symbol("u"); W = (u - 1) * (u ** 2 - 5 * u + 1); print("H4: W'(1) = %s" % sp.diff(W, u).subs(u, 1))
