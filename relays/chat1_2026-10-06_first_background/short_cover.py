"""Level n as the n-fold cyclic cover of the root presentation <t, x, y | t x t^-1 = phi(x), t y t^-1 = phi(y)>
(Schreier, transversal t^k): generators 1 = T = t^n, x_k = t^k x t^-k (2+k), y_k = t^k y t^-k (2+n+k), k < n.
Relators (2n, each of length |phi| + 3): x_{k+1} = phi(x)_k, y_{k+1} = phi(y)_k for k < n-1; T x_0 T^-1 = phi(x)_{n-1},
T y_0 T^-1 = phi(y)_{n-1}.  Meridian T, longitude c_0 = [x_0, y_0].  Deck = conjugation by t:
T -> T, x_k -> x_{k+1}, x_{n-1} -> T x_0 T^-1 (same for y).  Same group as first_background's bundle of phi^n."""
import first_background as F
CC = F.CC
def short_cover(phi):
    def cover(n):
        X = lambda k: 2 + k; Y = lambda k: 2 + n + k
        def sub(word, k):
            return [(1 if L > 0 else -1) * (X(k) if abs(L) == 2 else Y(k)) for L in word]
        rels = []
        for k in range(n - 1):
            rels.append(F.red([X(k + 1)] + F.inv(sub(phi[2], k))))
            rels.append(F.red([Y(k + 1)] + F.inv(sub(phi[3], k))))
        rels.append(F.red([1, X(0), -1] + F.inv(sub(phi[2], n - 1))))
        rels.append(F.red([1, Y(0), -1] + F.inv(sub(phi[3], n - 1))))
        lam = [X(0), Y(0), -X(0), -Y(0)]
        tau = {1: [1]}
        for k in range(n):
            tau[X(k)] = [X(k + 1)] if k < n - 1 else [1, X(0), -1]
            tau[Y(k)] = [Y(k + 1)] if k < n - 1 else [1, Y(0), -1]
        return 2 * n + 1, rels, [1], lam, tau
    return cover
