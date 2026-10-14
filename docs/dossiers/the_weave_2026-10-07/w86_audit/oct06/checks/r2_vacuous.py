"""Audit demo: r2_r3_primes.py's R2 verdict depends only on the traces having a non-zero omega-part; it never uses the deck.
Re-use its own helpers (imported unchanged) and run the same per-prime verdict on (i) Riley's pair, (ii) a pair unrelated
to m004 and its deck (X=[[1,omega],[0,1]], Y=[[1,0],[1,1]])."""
import sys, io, contextlib, importlib.util
spec = importlib.util.spec_from_file_location('r2', sys.argv[1])
with contextlib.redirect_stdout(io.StringIO()):
    r2 = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2)
src = open(sys.argv[1]).read()
print('mentions of the deck/beat/tau in r2_r3_primes.py:', sum(src.count(k) for k in ('deck', 'beat', 'tau', 'BEAT')))
def verdict(Xf, Yf):
    ok = True; rows = []
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
        typ = 'ramified' if p == 3 else ('inert' if p % 3 == 2 else 'split')
        mm, mi, I, add, mulr, neg = r2.mats(p)
        Xp, Yp = Xf(p), Yf(p)
        c = lambda A: tuple(tuple(tuple(v % p for v in r2.conj_entry(A[i][j])) for j in range(2)) for i in range(2))
        Xc, Yc = c(Xp), c(Yp)
        tr = lambda A: add(A[0][0], A[1][1])
        if typ == 'split':
            roots = [r for r in range(p) if (r*r + r + 1) % p == 0]
            evr = lambda u, r: (u[0] + u[1]*r) % p
            diff = [evr(tr(r2.mat_word(w, Xp, Yp, mm, mi, I)), roots[0]) != evr(tr(r2.mat_word(w, Xp, Yp, mm, mi, I)), roots[1]) for w in r2.WORDS]
            ok &= any(diff)
        else:
            diff = []
            for w in r2.WORDS:
                a = tr(r2.mat_word(w, Xp, Yp, mm, mi, I)); b = tr(r2.mat_word(w, Xc, Yc, mm, mi, I))
                if typ == 'ramified': a = (a[0] + a[1]) % 3; b = (b[0] + b[1]) % 3
                diff.append(a != b)
            ok &= (not any(diff)) if typ == 'ramified' else any(diff)
        rows.append((p, sum(diff)))
    return ok, rows
riley = (lambda p: (((1, 0), (1, 0)), ((0, 0), (1, 0))), lambda p: (((1, 0), (0, 0)), ((0, p - 1), (1, 0))))
other = (lambda p: (((1, 0), (0, 1)), ((0, 0), (1, 0))), lambda p: (((1, 0), (0, 0)), ((1, 0), (1, 0))))
print("Riley's pair      :", verdict(*riley))
print("an unrelated pair :", verdict(*other))
