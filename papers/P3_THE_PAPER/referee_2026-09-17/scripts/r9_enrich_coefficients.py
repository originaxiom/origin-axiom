"""Does ENRICHING THE COEFFICIENTS raise the count?  The one lead with a number attached.

r7 showed the generation count is a corank bounded by b1, and m004's b1 is 1.  But that bound was
computed with RANK-ONE coefficients (characters).  The obvious enrichment of the first step is to
carry a bigger bundle: replace the character by Sym^m of the geometric SL(2,C) representation --
which is exactly the coefficient system the record's own index instrument uses.

So: does dim H^1(pi_1(m004); Sym^m) grow with m, and does it reach 3?

Everything exact over Q(u), u^2 - u + 1 = 0 (= Q(sqrt -3), the figure-eight's invariant trace
field).  Field arithmetic, Sym^m, Fox calculus and ranks are reused from r3_m010_index.py, which
implements them from the definitions; the geometric representation, its relator and the Alexander
cross-check are this script's own.
"""
import io, os, sys, contextlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
with contextlib.redirect_stdout(io.StringIO()):
    import r3_m010_index as R          # importing runs its own report; silence it
K, mk, mat, eye, mmul, minv = R.K, R.mk, R.mat, R.eye, R.mmul, R.minv
msub, smul, rank, nullity = R.msub, R.smul, R.rank, R.nullity
stack_h, sym, ZERO, ONE, U = R.stack_h, R.sym, R.ZERO, R.ONE, R.U


def word_eval(w, rho):
    M = eye(len(rho['a']))
    for ch in w:
        M = mmul(M, rho[ch.lower()] if ch.islower() else rho[ch.lower() + "i"])
    return M


def rho_of(A, B):
    return {'a': A, 'b': B, 'ai': minv(A), 'bi': minv(B)}


def is_id(M):
    n = len(M)
    return all(M[i][j] == (ONE if i == j else ZERO) for i in range(n) for j in range(n))


def find_relator(rho, maxlen=8):
    """search for a word w with w a w^-1 = b; the relator is then  w a w^-1 b^-1."""
    import itertools
    A, Bi = rho['a'], rho['bi']
    for L in range(1, maxlen + 1):
        for tup in itertools.product("abAB", repeat=L):
            w = "".join(tup)
            W = word_eval(w, rho)
            if is_id(mmul(mmul(mmul(W, A), minv(W)), Bi)):
                return w
    return None


def alexander_from_relator(rel):
    """Delta(t) from the abelianised Fox derivatives of rel, with phi(a) = phi(b) = t."""
    import sympy as sp
    t = sp.symbols('t')
    P, D = sp.Integer(1), {'a': sp.Integer(0), 'b': sp.Integer(0)}
    for ch in rel:
        g = ch.lower()
        if ch.islower():
            D[g] = D[g] + P
            P = P * t
        else:
            P = P / t
            D[g] = D[g] - P
    out = {}
    for g in 'ab':
        e = sp.cancel(sp.together(sp.expand(D[g]) * t ** 12))
        cs = sp.Poly(sp.numer(e), t).all_coeffs() if sp.simplify(D[g]) != 0 else [0]
        while cs and cs[-1] == 0:
            cs.pop()
        if cs and cs[0] < 0:
            cs = [-c for c in cs]
        out[g] = sp.Poly(cs, t).as_expr() if cs else sp.Integer(0)
    return out, t


def h1(rel, rho):
    """a0 = dim H^0, a1 = dim H^1 for <a,b | rel> with coefficients rho."""
    n = len(rho['a'])
    I = eye(n)
    Mbig = [msub(rho['a'], I)[i] for i in range(n)] + [msub(rho['b'], I)[i] for i in range(n)]
    a0 = nullity(Mbig, n)
    Da, Db = R.fox(rel, rho)
    dimZ = 2 * n - rank(stack_h(Da, Db))
    return a0, dimZ - (n - a0)


def main():
    print("=" * 78)
    print("the geometric representation of the figure-eight knot group over Q(u)")
    print("=" * 78)
    A = mat([[1, 1], [0, 1]])
    print("   A = [[1,1],[0,1]],  B = [[1,0],[w,1]]  parabolic; search w over Q(u) for a relator")
    # Accept only the solution whose group really is the figure-eight: Delta = t^2 - 3t + 1.
    # (w = -1 also solves the relator search, but gives the TREFOIL, Delta = t^2 - t + 1.)
    import sympy as sp
    rel, B, om = None, None, None
    seen = []
    for p in range(-2, 3):
        for q in range(-2, 3):
            cand = K(p, q)
            if cand.is0():
                continue
            Bc = [[ONE, ZERO], [cand, ONE]]
            r = find_relator(rho_of(A, Bc), maxlen=6)
            if r is None:
                continue
            w = r + "a" + r.swapcase()[::-1] + "B"
            al, tt = alexander_from_relator(w)
            d = [v for v in al.values() if v != 0]
            seen.append((str(cand), r, str(d[0]) if d else "0"))
            if d and sp.simplify(d[0] - (tt ** 2 - 3 * tt + 1)) == 0:
                rel, B, om = r, Bc, cand
                break
        if rel:
            break
    print("   parabolic solutions found (w, relator word, Alexander polynomial):")
    for s in seen:
        mark = "   <-- FIGURE-EIGHT" if s[2].replace(" ", "") == "t**2-3*t+1" else (
               "   (trefoil)" if s[2].replace(" ", "") == "t**2-t+1" else "")
        print(f"      w = {s[0]:<10s} w-word = {s[1]:<8s} Delta = {s[2]}{mark}")
    if rel is None:
        print("   NO FIGURE-EIGHT SOLUTION FOUND -- abort"); return
    rho = rho_of(A, B)
    print(f"   using w = {om}   (w^2 - w + 1 = 0 ? {(om*om - om + ONE).is0()};"
          f"  w^2 + w + 1 = 0 ? {(om*om + om + ONE).is0()})")
    print(f"   det A = {R.det2(A)}   det B = {R.det2(B)}   (both must be 1)")
    print(f"   relator:  w a w^-1 b^-1  with w = {rel!r}")
    relator = rel + "a" + rel.swapcase()[::-1] + "B"
    print(f"   full relator word: {relator}")
    print(f"   relator evaluates to I ?  {is_id(word_eval(relator, rho))}")

    alex, t = alexander_from_relator(relator)
    print(f"   abelianised Fox derivatives -> {dict((g, str(v)) for g, v in alex.items())}")
    ok = any(str(v).replace(' ', '') in ("t**2-3*t+1",) for v in alex.values())
    print(f"   Alexander polynomial is t^2 - 3t + 1 (so this IS the figure-eight group): {ok}")

    print()
    print("=" * 78)
    print("does enriching the coefficients raise dim H^1 ?")
    print("=" * 78)
    print("   m   dim Sym^m   a0 = dim H^0   a1 = dim H^1      reaches 3 ?")
    rows = []
    for m in range(1, 15):
        Am, Bm = sym(A, m), sym(B, m)
        r = rho_of(Am, Bm)
        if not is_id(word_eval(relator, r)):
            print(f"   {m:>2}   relator fails in Sym^{m} -- skipped")
            continue
        a0, a1 = h1(relator, r)
        rows.append((m, m + 1, a0, a1))
        print(f"   {m:>2}   {m+1:>7}   {a0:>10}   {a1:>11}      {'YES' if a1 == 3 else ''}")

    print()
    hits = [r for r in rows if r[3] >= 3]
    print(f"   coefficient systems reaching dim H^1 >= 3: "
          f"{[f'Sym^{r[0]}' for r in hits] if hits else 'NONE in m = 1..14'}")
    print(f"   dim H^1 values seen: {sorted(set(r[3] for r in rows))}")
    print()
    print("   READING.  This is the honest test of 'enrich the first step': keep the object, keep")
    print("   the one-cusped bound, and make the BUNDLE bigger instead.  If dim H^1 climbs with m,")
    print("   the corank bound of r7 is a statement about rank-one coefficients only, and the")
    print("   count is not capped at one after all.  If it does not climb, the cap survives the")
    print("   enrichment and the obstruction is about the object rather than the instrument.")


if __name__ == "__main__":
    main()
