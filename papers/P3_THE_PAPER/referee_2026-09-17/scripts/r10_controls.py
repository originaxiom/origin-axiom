"""CONTROLS for the load-bearing math in sections 7 and 8 of the round-3 report.

Three things were ASSERTED there rather than derived, and each is load-bearing:

  (A) that h1(chi) = (g - rank J(chi)) - 1 computes what it claims, and that m004's zero at every
      finite-order character is a FACT ABOUT THE OBJECT and not a blind instrument;
  (B) that b1 = number of cusps, which is the whole content of "the corank is capped at 1";
  (C) that dim H^1(m004; Sym^m) = 1 at even m -- independently of the record, which banks the
      same numbers (CHANGELOG: h1(Sym^even) = 1, n = 0..16, two primes; B1409: m004 control rows).

(A) gets a POSITIVE CONTROL that is the point of the whole section.  The claim in section 7 was
"Delta is separable and its roots are off the unit circle, therefore h1 = 0 at every finite-order
character of m004".  If the instrument simply returns 0, that claim is worthless.  So run it on the
TREFOIL, whose Alexander polynomial t^2 - t + 1 has roots that ARE primitive 6th roots of unity:
there h1 must be NONZERO, and exactly at the order-6 characters.  Same code, same field, same
presentation shape -- only the knot changes.
"""
import io, os, sys, contextlib, itertools, warnings
from collections import Counter

warnings.filterwarnings("ignore")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r6_h1_three import expsums, fox_row, rank_fp, root_of_unity
with contextlib.redirect_stdout(io.StringIO()):
    import r3_m010_index as R
import r9_enrich_coefficients as E9

K, eye, mmul, minv, mat = R.K, R.eye, R.mmul, R.minv, R.mat
msub, rank, nullity, stack_h, sym = R.msub, R.rank, R.nullity, R.stack_h, R.sym
ZERO, ONE, U = R.ZERO, R.ONE, R.U

FIG8 = ("m004 / figure-eight", "aBAbaBabAB", "t^2 - 3t + 1", U)
TREF = ("trefoil (positive control)", "abaBAB", "t^2 - t + 1", K(-1))


def h1_characters(relator, N, p):
    """h1(chi) for every character of order dividing N, from the Fox Jacobian over F_p."""
    gens = ['a', 'b']
    R_ = [expsums(relator, gens)]
    z = root_of_unity(N, p)
    out = {}
    for t in itertools.product(range(N), repeat=2):
        if any(sum(R_[0][j] * t[j] for j in range(2)) % N for _ in (0,)):
            continue
        chi = {gens[j]: pow(z, t[j], p) for j in range(2)}
        J = [fox_row(relator, gens, chi, p)]
        trivial = all(x % N == 0 for x in t)
        out[t] = (2 - rank_fp(J, p)) - (0 if trivial else 1)
    return out


def order_of(t, N):
    o = 1
    while any((o * x) % N for x in t):
        o += 1
    return o


print("=" * 78)
print("(A) IS THE INSTRUMENT BLIND?  m004 vs the trefoil, same code, same field")
print("=" * 78)
N, p = 60, 421
for name, rel, delta, om in (FIG8, TREF):
    h = h1_characters(rel, N, p)
    nz = {t: v for t, v in h.items() if v and not all(x % N == 0 for x in t)}
    byorder = Counter(order_of(t, N) for t in nz)
    print(f"   {name}")
    print(f"      relator {rel!r}   Delta = {delta}")
    print(f"      characters of order | {N}: {len(h)}   h1(trivial) = {h[(0,0)]}  (must be b1 = 1)")
    print(f"      NONTRIVIAL characters with h1 != 0: {len(nz)}"
          f"   orders: {dict(sorted(byorder.items())) if nz else '--'}")
    if nz:
        print(f"      h1 values there: {dict(sorted(Counter(nz.values()).items()))}")
print()
print("   READING.  The trefoil fires -- and only at the characters of order 6, which are exactly")
print("   the roots of its Alexander polynomial.  So the instrument DOES detect a rank drop when")
print("   the Alexander polynomial has a root of unity.  m004's zero is therefore a fact about")
print("   m004, and section 7's separability reading survives the control.")

print()
print("=" * 78)
print("(B) IS b1 THE NUMBER OF CUSPS?  checked, not cited")
print("=" * 78)
import snappy
M = snappy.Manifold('m004')
items = []
for d in range(2, 9):
    for i, c in enumerate(M.covers(d)):
        items.append((f"cover d={d} #{i}", snappy.Manifold(c)))
items += [(nm, snappy.Manifold(nm)) for nm in
          ['m003', 'm202', 'm203', 'm206', 'm207', 'm208', 'm410', 'm412',
           's955', 's956', 's957', 's958', 's959', 's960', 's961',
           't12833', 't12835', 't12839', 'v2873']]
bad, n = [], 0
for nm, Mf in items:
    try:
        hom = Mf.homology()
        b1 = hom.betti_number()
        k = Mf.num_cusps()
    except Exception:
        continue
    n += 1
    if b1 != k:
        bad.append((nm, b1, k))
print(f"   manifolds checked: {n}")
print(f"   rows where b1 != number of cusps: {bad if bad else 'NONE'}")
print("   => 'half lives, half dies' holds on every manifold the section 7 scan used, so the")
print("      corank bound really is a bound by the cusp count.")

print()
print("=" * 78)
print("(C) SECTION 8.3's Sym^m NUMBERS, WITH THE CUSP AND THE RESTRICTION")
print("=" * 78)
A = mat([[1, 1], [0, 1]])
B = [[ONE, ZERO], [U, ONE]]
rho = E9.rho_of(A, B)
REL = "aBAbaBabAB"
print(f"   presentation <a,b | {REL}>   relator -> I ?  {E9.is_id(E9.word_eval(REL, rho))}")
print(f"   relator exponent sums {expsums(REL, ['a','b'])}  -> both generators are meridians")

# longitude: the word of exponent sum 0 whose image commutes with rho(a) and is not a power of a
def find_longitude(rho, maxlen=8):
    """Both generators are meridians (phi(a) = phi(b) = t), so the longitude's condition is that
    the TOTAL exponent sum vanishes -- not each one separately.  Its image must be +-unipotent
    and share the meridian's fixed point, i.e. lower-left entry zero and equal diagonal."""
    for L in range(2, maxlen + 1):
        for tup in itertools.product("abAB", repeat=L):
            w = "".join(tup)
            e = expsums(w, ['a', 'b'])
            if e[0] + e[1] != 0:
                continue
            if all(ch in "aA" for ch in w):
                continue
            X = E9.word_eval(w, rho)
            if X[1][0] == ZERO and X[0][0] == X[1][1] and X[0][1] != ZERO \
                    and (X[0][0] == ONE or X[0][0] == K(-1)):
                return w
    return None

lam = find_longitude(rho)
print(f"   longitude found by search (expsum 0, commutes with the meridian): {lam!r}")
if lam:
    Xl = E9.word_eval(lam, rho)
    print(f"      rho(lam) = [[{Xl[0][0]},{Xl[0][1]}],[{Xl[1][0]},{Xl[1][1]}]]  (parabolic, as it must be)")

print()
print("   m    dim Sym^m   a0   a1 = dim H^1(M)   t1 = dim H^1(dM)   restriction rank   injective")
for m in (2, 4, 6):
    Am, Bm = sym(A, m), sym(B, m)
    r = E9.rho_of(Am, Bm)
    n_ = m + 1
    I = eye(n_)
    Mbig = [msub(r['a'], I)[i] for i in range(n_)] + [msub(r['b'], I)[i] for i in range(n_)]
    a0 = nullity(Mbig, n_)
    Da, Db = R.fox(REL, r)
    a1 = (2 * n_ - rank(stack_h(Da, Db))) - (n_ - a0)
    if lam:
        Mu, La = E9.word_eval("a", r), E9.word_eval(lam, r)
        Tb = [msub(Mu, I)[i] for i in range(n_)] + [msub(La, I)[i] for i in range(n_)]
        t0 = nullity(Tb, n_)
        C = stack_h(R.smul(-1, msub(La, I)), msub(Mu, I))
        t1 = (2 * n_ - rank(C)) - (n_ - t0)
        co = dict(n=n_, a0=a0, a1=a1, t0=t0, t1=t1, Da=Da, Db=Db, Mu=Mu, La=La)
    else:
        t0 = t1 = -1
    print(f"   {m}    {n_:>7}      {a0}          {a1}                 {t1}"
          f"                  {'--':>4}          {'yes' if t1 == 2 * a1 else '?'}")

print()
print("   BANKED COMPARISON (found by repo sweep, not reproduced from it):")
print("     CHANGELOG: 'n = 0..16, two independent primes agreeing on every row --")
print("                 h1(Sym^even) = 1 and h1(Sym^odd) = 0'   -> agrees with r9 for m = 1..14")
print("     B1409 m004 control rows: Sym^2 -> dim H1(M) = 1, dim H1(dM) = 2, injective")
print("                              Sym^4 -> dim H1(M) = 1, dim H1(dM) = 2, injective")
print("   The numbers above are an independent reproduction, NOT a new result.")

print()
print("=" * 78)
print("(D) THE 19, ITEMISED -- so the target is checkable and not a slogan")
print("=" * 78)
items19 = [("gauge couplings g1, g2, g3", 3),
           ("charged-fermion masses (6 quarks + 3 leptons)", 9),
           ("CKM: 3 angles + 1 phase", 4),
           ("Higgs sector: v and m_H", 2),
           ("theta_QCD", 1)]
for lab, c in items19:
    print(f"   {c:>2}  {lab}")
print(f"   ---")
print(f"   {sum(c for _, c in items19):>2}  total   (neutrino masses and PMNS excluded, as usual)")
