"""For a DEHN-FILLED manifold the shape field is generally larger than the invariant trace field,
which sits inside it. So:
  (1) the three claimed arithmetic slopes: is the claimed field a SUBFIELD of the shape field?
  (2) all 78 closed fillings: is Q(sqrt-3) a subfield of the shape field?  (If not, it is not in
      the invariant trace field either, since that is a subfield of the shape field.)
Control: the open object, whose shape field IS its invariant trace field Q(sqrt-3)."""
import snappy, warnings, math; warnings.filterwarnings("ignore")
from snappy import Manifold
from cypari import pari
pari.set_real_precision(60)
I = pari('I')

def shapes(M):
    return [pari(str(w.real())) + pari(str(w.imag())) * I
            for w in M.high_precision().tetrahedra_shapes('rect')]

def minpoly(z, maxdeg=10, maxcoeff=10**8, tol=1e-45):
    for d in range(2, maxdeg + 1):
        p = z.algdep(d)
        cf = [abs(int(p.polcoef(k))) for k in range(int(p.poldegree()) + 1)]
        if max(cf) > maxcoeff:
            continue
        try:
            if abs(complex(p.subst('x', z))) > tol:
                continue
        except Exception:
            continue
        return d, p
    return None, None

def subfield_discs(p):
    """discriminants of the proper subfields of Q[x]/(p), plus their degrees"""
    out = []
    try:
        subs = p.nfsubfields()
    except Exception:
        return None
    for k in range(len(subs)):
        f = subs[k][0]
        d = int(f.poldegree())
        if d <= 1:
            continue
        try:
            out.append((d, int(f.nfdisc()), f))
        except Exception:
            out.append((d, None, f))
    return out

print("=== CONTROL: open m004 ===", flush=True)
for z in shapes(Manifold('m004')):
    d, p = minpoly(z)
    print("   shape minpoly:", p, " disc", p.nfdisc(), flush=True)

print("\n=== (1) the three claimed arithmetic slopes ===", flush=True)
claims = {(5, 1): ('x^4-x-1', -283), (6, 1): ('x^3+2*x-1', -59), (8, 1): ('x^3+x-1', -31)}
for s, (poly, disc) in claims.items():
    N = Manifold('m004'); N.dehn_fill(s)
    z = shapes(N)[0]
    d, p = minpoly(z)
    subs = subfield_discs(p)
    hit = [t for t in (subs or []) if t[1] == disc]
    print("   m004%s: shape field degree %s (disc %s); proper subfields %s"
          % (s, d, p.nfdisc(), [(t[0], t[1]) for t in (subs or [])]), flush=True)
    print("      contains a field of discriminant %d (= %s)? %s"
          % (disc, poly, bool(hit)), flush=True)
    if hit:
        print("      and it is isomorphic to %s? %s"
              % (poly, str(pari('nfisisom(%s,%s)' % (hit[0][2], poly))) != '0'), flush=True)

print("\n=== (2) does ANY of the 78 closed fillings have Q(sqrt-3) inside its shape field? ===",
      flush=True)
slopes = [(a, b) for a in range(-8, 9) for b in range(0, 9)
          if math.gcd(abs(a), abs(b)) == 1 and not (b == 0 and a != 1)]
hyp = []
for s in slopes:
    N = Manifold('m004'); N.dehn_fill(s)
    if N.solution_type() == 'all tetrahedra positively oriented':
        hyp.append(s)
print("   closed hyperbolic fillings:", len(hyp), flush=True)
keeps, unresolved = [], []
for s in hyp:
    N = Manifold('m004'); N.dehn_fill(s)
    try:
        z = shapes(N)[0]
        d, p = minpoly(z)
        if p is None:
            unresolved.append(s); continue
        if int(p.poldegree()) == 2 and int(p.nfdisc()) == -3:
            keeps.append(s); continue
        subs = subfield_discs(p)
        if subs is None:
            unresolved.append(s); continue
        if any(t[1] == -3 for t in subs):
            keeps.append(s)
    except Exception:
        unresolved.append(s)
print("   fillings whose shape field CONTAINS Q(sqrt-3):", keeps, flush=True)
print("   unresolved at this precision/coefficient bound:", len(unresolved), unresolved, flush=True)
print("   paper: ZERO of the 78 keep Q(sqrt-3)", flush=True)
