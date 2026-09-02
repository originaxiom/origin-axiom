"""Is the silver bundle (b++RRLL = m136) arithmetic?  Maclachlan-Reid criterion for a non-cocompact
Kleinian group: invariant trace field imaginary quadratic AND invariant traces (tr g^2) algebraic integers.
Recomputed here, not cited: every tr(g^2) for all words of length <= 6 in the holonomy generators, at
high precision, against the Gaussian integers; plus Vol against 4*Catalan (B147) and 12 x covol(PSL2 Z[i])."""
import snappy, itertools
from mpmath import mp, mpc, catalan, pi, zeta
mp.dps = 60
M = snappy.Manifold("m136")
G = M.fundamental_group()
rho = M.polished_holonomy(bits_prec=400, lift_to_SL2=False)
gens = {g: rho(g) for g in G.generators()}
inv = {g.upper(): rho(g.upper()) for g in G.generators()}
mats = {**gens, **inv}
def tr(A): return A[0,0] + A[1,1]
bad = []; seen = set(); n = 0
for L in range(1, 7):
    for w in itertools.product(mats.keys(), repeat=L):
        A = mats[w[0]]
        for c in w[1:]: A = A * mats[c]
        t = tr(A * A)            # invariant trace of the word
        re, im = float(t.real), float(t.imag)
        key = (round(re, 8), round(im, 8))
        if key in seen: continue
        seen.add(key); n += 1
        if abs(re - round(re)) > 1e-30 or abs(im - round(im)) > 1e-30:
            bad.append((''.join(w), key))
print(f"distinct invariant traces tr(g^2), words <= 6: {n}; NOT Gaussian integers: {len(bad)}")
print("sample:", sorted(seen)[:8])
covol = mp.mpf(4)**mp.mpf(1.5) * zeta(2) * catalan / (4*pi**2)   # |D|^{3/2} zeta_K(2)/(4 pi^2), zeta_{Q(i)}(2)=zeta(2)*G
V = mp.mpf(str(M.volume(bits_prec=200)))
print(f"Vol(m136) = {V}   4G = {4*catalan}   12*covol(PSL2 Z[i]) = {12*covol}")
print("SILVER ARITHMETIC (invariant field Q(i), integral invariant traces, Bianchi volume ratio 12):",
      len(bad) == 0 and abs(V - 4*catalan) < mp.mpf(10)**-50 and abs(V - 12*covol) < mp.mpf(10)**-50)
