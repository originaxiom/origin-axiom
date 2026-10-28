"""Referee B1803, b1: does Sym(Q) = Z/2 x Z/2 hold on the even fillings Q = m004(p,q), and which even fillings are
exceptional (the draft never says 'hyperbolic')?  For every p even in 2..40, q odd with |q| <= 13, gcd(p,q) = 1:
solution type, volume, H1, SnapPy's symmetry group, is_full_group, amphicheirality.  Exceptional slopes of the
figure-eight: 0, +-1, +-2, +-3, +-4 (Thurston); the even ones are (0,1), (+-2,1), (+-4,1)."""
import snappy, math
rows = []
bad = []
for p in range(2, 41, 2):
    for q in range(-13, 14, 2):
        if math.gcd(p, abs(q)) != 1:
            continue
        N = snappy.Manifold("m004"); N.dehn_fill((p, q))
        st = N.solution_type()
        hyp = st.startswith("all tetrahedra positively")
        try:
            S = N.symmetry_group()
            sym, full, amph = str(S), S.is_full_group(), S.is_amphicheiral()
        except Exception as e:
            sym, full, amph = "err:%s" % str(e)[:40], None, None
        vol = float(N.volume())
        tag = "" if (hyp and sym == "Z/2 + Z/2" and full and amph is False) else "  <-- CHECK"
        if tag:
            bad.append((p, q, st, sym, full, amph))
        rows.append((p, q))
        if tag or abs(q) == 1 or p <= 6:
            print("m004(%d,%d): %-34s vol %.6f H1 %-6s Sym %-12s full %s amph %s%s" % (p, q, st, vol, N.homology(), sym, full, amph, tag))
print("even fillings tested: %d; not (hyperbolic, Sym = Z/2+Z/2, full, chiral): %d" % (len(rows), len(bad)))
for b in bad:
    print("   ", b)
print("b1 exit 0")
