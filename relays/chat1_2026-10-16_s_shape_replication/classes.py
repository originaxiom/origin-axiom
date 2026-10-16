"""Configuration classes under word reversal and the L <-> R mirror (pure algebra, no mass).

A configuration is (Lyndon word, line (a, b) of exact order N fixed up to sign), in tlow_enum.py's convention:
u = (b, a) is a left eigenvector of M = mat(word) mod N. The mirror L <-> R is M -> J M J (J = [[0,1],[1,0]]),
taking the line to (b, a); reversal-with-mirror is M -> M^T, taking it to (-b, a) (M^T Omega M = Omega). Both images
are carried to the Lyndon rotation (u -> u P, P = mat(prefix)). The orbit of the order-4 group is the class.
Usage: python3 -B classes.py   (checks that every image is a closing configuration of T-low and counts the classes)"""
import math, json, os, sys
def mat(w):
    A, B, C, D = 1, 0, 0, 1
    for ch in w:
        if ch == "L": A, B, C, D = A + B, B, C + D, D
        else: A, B, C, D = A, A + B, C, C + D
    return A, B, C, D
def lyndon_rot(w):
    rots = [(w[k:] + w[:k], k) for k in range(len(w))]
    return min(rots)
def canon_line(a, b, N):
    return min((a % N, b % N), ((-a) % N, (-b) % N))
def carry(word, k, line, N):
    """the line (a, b) of `word` carried to the rotation word[k:] + word[:k]: u = (b, a) is a left eigenvector of
    mat(word); for the rotation P^-1 M P (P = mat(word[:k])) the left eigenvector is u P"""
    a, b = line
    A, B, C, D = mat(word[:k])
    u0, u1 = b, a
    v0, v1 = u0 * A + u1 * C, u0 * B + u1 * D
    return canon_line(v1, v0, N)
def mirror(word, line, N):
    w = word.translate(str.maketrans("LR", "RL")); a, b = line
    return w, canon_line(b, a, N)
def revmirror(word, line, N):            # transpose: mat(reverse(mirror(w))) = mat(w)^T
    w = word.translate(str.maketrans("LR", "RL"))[::-1]; a, b = line
    return w, canon_line(-b, a, N)
def to_lyndon(word, line, N):
    w, k = lyndon_rot(word)
    return w, carry(word, k, line, N)
def orbit(word, line, N):
    out = set()
    for f in (lambda w, l: (w, l), lambda w, l: mirror(w, l, N), lambda w, l: revmirror(w, l, N),
              lambda w, l: revmirror(*mirror(w, l, N), N)):
        out.add(to_lyndon(*f(word, tuple(line)), N))
    return frozenset(out)
if __name__ == "__main__":
    # sanity: the carried / mapped lines are fixed lines of the new matrices
    def fixed(word, line, N):
        A, B, C, D = mat(word); a, b = line
        return any(((a * D + b * B) - e * a) % N == 0 and ((a * C + b * A) - e * b) % N == 0 for e in (1, -1))
    cfg = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "chat1_2026-10-15_route",
                                      "twisted_units", "tlow_configurations.json")))
    allc = {(int(N), w, tuple(key)) for N in cfg for w, h, key, eps in cfg[N]}
    bad = 0; cls = {}
    for (N, w, l) in allc:
        orb = orbit(w, l, N)
        for (w2, l2) in orb:
            bad += (not fixed(w2, l2, N)) + ((N, w2, l2) not in allc)
        cls.setdefault((N, orb), []).append((w, l))
    sizes = {}
    for (N, orb), mem in cls.items(): sizes.setdefault(N, []).append(len(orb))
    print("T-low: images not fixed or not in the set:", bad, "| classes:", len(cls), {N: sorted(v) for N, v in sizes.items()})
