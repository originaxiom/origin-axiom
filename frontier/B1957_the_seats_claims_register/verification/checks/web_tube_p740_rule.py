"""B1957: the web seat's three more words for B1852's even-run pattern (its note on the tube's tau, section 7 item 3;
register row P-740), and the rule behind the pattern, PROVED here for every cyclic word with a reversal.  Data-free; exact.

THE RULE (P-740's per-centre form).  A cyclic word w in L, R that reads the same backwards has, for each such reading,
two centres on its circle, each either between two letters (the middle of an even run) or on a letter (the middle
letter of an odd run).  The bundle's reversing involution sigma fixes the fibre over each centre, and acts on that
fibre's lattice by an involution Z of determinant -1.  CLAIM: Z = 1 modulo 2 at a centre between letters, and Z != 1
modulo 2 at a centre on a letter.  (An involution of determinant -1 in GL(2, Z) is conjugate to diag(1, -1) exactly
when it is 1 modulo 2, and the fibre's modulus then has real part 0; otherwise it is conjugate to the swap and the
real part is 1/2.  Standard.)

PROOF.  Write F = diag(-1, 1); F L F = L^-1, F R F = R^-1, so F M(u) F = M(reverse u)^-1 for every word u.
 (a) A centre between letters: read the word from there, W = M(u), u a palindrome.  Then F W F = W^-1, so Z = F,
     and F = 1 modulo 2.
 (b) A centre on a letter x: read the word from x, W = x P with P a palindrome.  Then Z = F x^-1 satisfies Z^2 = 1 and
     Z W Z^-1 = F P x F = P^-1 x^-1 = W^-1.  Modulo 2, Z = x, and L and R are not 1 modulo 2.
 (c) The other centre of the same reading carries Z W (the reversers of W are the coset Z <W>, in two classes under
     conjugation by W).  Modulo 2 the letters are involutions, so a palindrome of even length is 1 and one of odd
     length is a conjugate of its middle letter: Z W is 1 modulo 2 exactly when the other centre is between letters,
     which is (a) and (b) again.                                                                                 QED
So the two fixed fibres are in opposite classes exactly when one centre is between letters and the other on a letter.
The two centres are half the word's length apart, so that is every reading of a word of odd length and no reading of a
word of even length (there the centres are both between letters or both on letters).

CHECKS.
 T1  the seat's three words L^6 R (LR)^k, k = 6, 7, 8: every X with entries in [-14, 14], X^2 = 1, X A X^-1 = A^-1 is
     +-((-1, 6), (0, 1)) = +-L^3 F L^-3; X = 1 and X A != 1 modulo 2 (opposite classes).  For this family the same holds
     for EVERY k by the proof: A = R (LR)^k modulo 2, R has order 2 and LR order 3 in GL(2, Z/2), so A != 1.
 T2  every primitive cyclic word of length 2 to 14 with both letters that reads the same backwards: at each centre the
     Z of the proof is an integer involution of determinant -1 that reverses W (exact), its class modulo 2 is as claimed,
     and the two centres of a reading carry Z and a conjugate of Z W (checked through the class modulo 2).
 T3  a brute-force search on the words of length up to 7: every reversing involution with entries in [-6, 6] has the
     class modulo 2 of Z or of Z W.
 T4  the control: the rule with the two kinds of centre exchanged fails."""
import itertools, functools
print = functools.partial(print, flush=True)
Lm = ((1, 1), (0, 1)); Rm = ((1, 0), (1, 1)); F = ((-1, 0), (0, 1)); ONE = ((1, 0), (0, 1))
mul = lambda X, Y: tuple(tuple(sum(X[i][k] * Y[k][j] for k in range(2)) for j in range(2)) for i in range(2))
det = lambda X: X[0][0] * X[1][1] - X[0][1] * X[1][0]
inv = lambda X: (lambda d: ((X[1][1] * d, -X[0][1] * d), (-X[1][0] * d, X[0][0] * d)))(det(X))        # det = +-1
M = lambda u: functools.reduce(mul, [Lm if c == "L" else Rm for c in u], ONE)
one2 = lambda X: all((X[i][j] - ONE[i][j]) % 2 == 0 for i in range(2) for j in range(2))


def reversers_in_box(A, box):
    """every integer X with entries in [-box, box], X^2 = 1 and X A = A^-1 X"""
    Ai = inv(A); out = []
    for a, b, c, d in itertools.product(range(-box, box + 1), repeat=4):
        if a * d - b * c not in (1, -1): continue
        X = ((a, b), (c, d))
        if mul(X, X) == ONE and mul(X, A) == mul(Ai, X): out.append(X)
    return out


def centres(w):
    """the readings of the cyclic word w that are reversals: for each c with w[i] = w[(c - i) mod n] for all i, the two
    centres as ('between', j) (between letters j - 1 and j) or ('on', j)"""
    n = len(w); out = []
    for c in range(n):
        if all(w[i] == w[(c - i) % n] for i in range(n)):
            pair = []
            for twice in (c, c + n):                         # the centres sit at c/2 and c/2 + n/2
                pair.append(("on", (twice // 2) % n) if twice % 2 == 0 else ("between", ((twice + 1) // 2) % n))
            out.append(tuple(pair))
    return out


def Z_at(w, centre):
    """the proof's involution at a centre, with the monodromy read from that centre: returns (Z, W)"""
    kind, j = centre; u = w[j:] + w[:j]; W = M(u)
    if kind == "between": return F, W
    x = Lm if u[0] == "L" else Rm
    return mul(F, inv(x)), W


if __name__ == "__main__":
    # T1
    for k in (6, 7, 8):
        A = M("L" * 6 + "R" + "LR" * k); X0 = ((-1, 6), (0, 1)); found = reversers_in_box(A, 14)
        print("T1: k = %d: reversing involutions with entries to 14: %d, and they are +-((-1, 6), (0, 1)): %s; L^3 F L^-3 is that matrix: %s; X = 1 mod 2: %s; X A = 1 mod 2: %s; A = R (LR)^k mod 2 is not 1: %s" % (
            k, len(found), sorted(found) == sorted([X0, tuple(tuple(-v for v in r) for r in X0)]), mul(mul(M("LLL"), F), inv(M("LLL"))) == X0, one2(X0), one2(mul(X0, A)), not one2(M("R" + "LR" * k))))
    print("T1: for every k: A mod 2 = R (LR)^k; R^2 = 1 mod 2: %s, (LR)^3 = 1 mod 2: %s, and R is none of 1, LR, (LR)^2 mod 2: %s" % (one2(M("RR")), one2(M("LRLRLR")), all(not one2(mul(Rm, inv(M(p)))) for p in ("", "LR", "LRLR"))))
    # T2
    def primitive_cyclic(n):
        seen = set()
        for t in itertools.product("LR", repeat=n):
            w = "".join(t)
            if "L" not in w or "R" not in w: continue
            rots = [w[i:] + w[:i] for i in range(n)]
            if len(set(rots)) < n: continue                                  # a proper power
            m = min(rots)
            if m not in seen: seen.add(m); yield m
    tally = {"both between": 0, "one of each": 0, "both on": 0}; words = readings = 0; ok = True; swapped_ok = True; relation = True
    for n in range(2, 15):
        for w in primitive_cyclic(n):
            cs = centres(w)
            if not cs: continue
            words += 1
            for pair in cs:
                readings += 1; classes = []
                for centre in pair:
                    Z, W = Z_at(w, centre)
                    ok &= det(Z) == -1 and mul(Z, Z) == ONE and mul(mul(Z, W), inv(Z)) == inv(W) and (one2(Z) == (centre[0] == "between"))
                    swapped_ok &= one2(Z) == (centre[0] == "on"); classes.append(one2(Z))
                Z1, W1 = Z_at(w, pair[0]); relation &= one2(mul(Z1, W1)) == classes[1]
                kinds = sorted(c[0] for c in pair); tally["both between" if kinds == ["between", "between"] else "both on" if kinds == ["on", "on"] else "one of each"] += 1
    print("T2: primitive cyclic words of length 2 to 14 with both letters that read the same backwards: %d, with %d readings; at every centre Z is an involution of determinant -1 reversing W, 1 mod 2 exactly at a centre between letters: %s; the other centre's class is that of Z W: %s" % (words, readings, ok, relation))
    print("T2: the readings by their two centres: %s (opposite classes exactly in the middle case)" % tally)
    print("T4: the control (the two kinds of centre exchanged): %s" % swapped_ok)
    # T3
    bf = True; nb = 0
    for n in range(2, 8):
        for w in primitive_cyclic(n):
            cs = centres(w)
            if not cs: continue
            Wm = M(w); want = set()
            for pair in cs:
                for centre in pair: want.add(one2(Z_at(w, centre)[0]))
            got = {one2(X) for X in reversers_in_box(Wm, 6) if det(X) == -1}; nb += 1
            bf &= got <= want and bool(got)
    print("T3: on the %d such words of length 2 to 7, every reversing involution of determinant -1 with entries to 6 has a class modulo 2 that the proof's centres give: %s" % (nb, bf))
