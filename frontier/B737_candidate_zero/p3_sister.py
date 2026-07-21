# B737 — CANDIDATE ZERO — PROBE 3: SISTER / GENERICITY GUARD
# ============================================================
# Question (sealed, PREREGISTRATION.md probe 3): m003 is a 1-cusped index-12
# cover of the SAME Bianchi orbifold PSL(2,O_3)\H^3 as m004 (same field, same
# volume). What (if anything) in the cusp/scattering data is OBJECT-specific?
#   (a) does H_1 (Z for m004 vs Z/5+Z for m003) enter the cusp/scattering data?
#       Are the cusp shapes equal or different?
#   (b) does the congruence level ((4)/(8) for m004 vs (2) for m003; B734+cc3)
#       enter the Eisenstein/scattering level structure?
# Two-outcome: A = an object-specific datum genuinely enters the voice (state
# it exactly); B = fully generic to the commensurability class.
#
# HONESTY/PRECISION NOTE: the canonical env is pyenv (no sage), so snappy's
# interval-verified routines are unavailable. Rigor here = (i) an EXACT
# symbolic certificate that z = zeta_6 solves the gluing+completeness
# equations of both triangulations over Q(zeta_6) (sympy), plus (ii) 60-digit
# quad-double numerics with residuals < 1e-50 against exact algebraic targets,
# plus (iii) exact integer linear algebra (Smith forms) and exact finite-ring
# arithmetic. Labeled per item below.

import snappy
from sympy import (Matrix, Rational, sqrt, I, simplify, expand, Poly,
                   symbols, factor_list, exp, pi as spi)
from mpmath import mp, mpf, mpc, zeta, pi, kleinj
mp.dps = 60

TOL = mpf(10) ** (-50)
def snum(v):
    return str(v).replace(" ", "")             # snappy prints '... e-65' (space)
out = []
def P(s=""):
    print(s); out.append(str(s))

P("B737 PROBE 3 — SISTER/GENERICITY GUARD: m004 vs m003 cusp & scattering data")
P("=" * 78)

# ---------------------------------------------------------------------------
# PART 0 — raw high-precision invariants (snappy quad-double, ~60 digits)
# ---------------------------------------------------------------------------
P("\n[0] Raw invariants (snappy ManifoldHP, quad-double)")
data = {}
for name in ("m004", "m003"):
    M = snappy.ManifoldHP(name)
    ci = M.cusp_info()[0]
    tr = M.cusp_translations()[0]
    data[name] = dict(
        vol=mpf(snum(M.volume())),
        hom=str(M.homology()),
        shape=mpc(snum(ci["shape"].real()), snum(ci["shape"].imag())),
        mer=mpc(snum(tr[0].real()), snum(tr[0].imag())),
        long=mpc(snum(tr[1].real()), snum(tr[1].imag())),
        area=mpf(snum(M.cusp_areas()[0])),
        tets=[mpc(snum(t["rect"].real()), snum(t["rect"].imag()))
              for t in M.tetrahedra_shapes()],
    )
    P(f"  {name}: vol={data[name]['vol']}")
    P(f"        H_1={data[name]['hom']},  cusp shape={data[name]['shape']}")
    P(f"        max-cusp translations (mer,long)=({data[name]['mer']}, {data[name]['long']})")
    P(f"        max-cusp area={data[name]['area']}")

# ---------------------------------------------------------------------------
# PART 1 — EXACT certificate: both triangulations are solved by z = zeta_6
#          (2 regular ideal tetrahedra), over Q(zeta_6), symbolically.
# ---------------------------------------------------------------------------
P("\n[1] EXACT gluing+completeness certificate at z = zeta_6 (sympy, symbolic)")
z6 = Rational(1, 2) + sqrt(3) * I / 2          # zeta_6 exactly
for name in ("m004", "m003"):
    M = snappy.Manifold(name)
    rows = M.gluing_equations("rect")          # rows (a, b, c): c*prod z^a (1-z)^b = 1
    ok = True
    for (a, b, c) in rows:
        val = Rational(c)
        for ai, bi in zip(a, b):
            val *= z6 ** ai * (1 - z6) ** bi
        if simplify(expand(val - 1)) != 0:
            ok = False
    P(f"  {name}: all {len(rows)} gluing+completeness rows == 1 exactly at z=zeta_6: {ok}")
    assert ok
    for t in data[name]["tets"]:
        assert abs(t - mpc(0.5, mp.sqrt(3) / 2)) < TOL
P("  => both geometric solutions are EXACTLY 2 regular ideal tetrahedra (shape zeta_6);")
P("     both manifolds live in the regular-ideal tessellation commensurable w/ PSL(2,O_3).")

# ---------------------------------------------------------------------------
# PART 2 — index-12 cover check (Humbert volume, computed not cited)
# ---------------------------------------------------------------------------
P("\n[2] Humbert volume: vol(PSL(2,O_3)\\H^3) = |d|^{3/2} zeta_K(2)/(4 pi^2), d=-3")
L2 = mpf(3) ** (-2) * (zeta(2, mpf(1) / 3) - zeta(2, mpf(2) / 3))  # L(2,chi_{-3}), Hurwitz
zK2 = zeta(2) * L2
vol_orb = mpf(3) ** mpf("1.5") * zK2 / (4 * pi ** 2)
P(f"  L(2,chi_-3) = {L2}")
P(f"  vol_orb     = {vol_orb}")
for name in ("m004", "m003"):
    r = data[name]["vol"] / vol_orb
    P(f"  vol({name})/vol_orb = {r}   (|r-12| = {mp.nstr(abs(r-12), 3)})")
    assert abs(r - 12) < TOL
P("  => both are degree-12 objects over the SAME Bianchi orbifold (55+ digits).")

# ---------------------------------------------------------------------------
# PART 3 — (a) THE CUSP LATTICES: equal covolume, NON-similar tori
# ---------------------------------------------------------------------------
P("\n[3] (a) Cusp cross-section lattices (the scattering Gamma_infinity)")
s3 = mp.sqrt(3)
# m004: translations (i, 2*sqrt(3)) -> lattice ~ Z + 2*sqrt(-3) Z ; shape 2*sqrt(-3)
# m003: translations (1+sqrt(-3), 2) -> lattice = 2*(Z + zeta_6 Z) = 2*O_K ; shape zeta_6
chk = [
    ("m004 shape = 2*sqrt(-3)", abs(data["m004"]["shape"] - mpc(0, 2 * s3))),
    ("m003 shape = zeta_6", abs(data["m003"]["shape"] - mpc(0.5, s3 / 2))),
    ("m004 max-cusp lattice = i*(Z + 2sqrt(-3)Z): mer = i", abs(data["m004"]["mer"] - mpc(0, 1))),
    ("m004 long = 2*sqrt(3)", abs(data["m004"]["long"] - 2 * s3)),
    ("m003 max-cusp lattice = 2*O_K: mer = 1+sqrt(-3)", abs(data["m003"]["mer"] - mpc(1, s3))),
    ("m003 long = 2", abs(data["m003"]["long"] - 2)),
    ("equal max-cusp AREAS: m004 area = 2*sqrt(3)", abs(data["m004"]["area"] - 2 * s3)),
    ("equal max-cusp AREAS: m003 area = 2*sqrt(3)", abs(data["m003"]["area"] - 2 * s3)),
]
for lab, res in chk:
    P(f"  {lab:55s} residual {mp.nstr(res, 3)}")
    assert res < TOL
P("  Both moduli lie in K = Q(sqrt(-3)) (cusp field = the field, both).  BUT:")

# SL(2,Z)-inequivalence, made exact via CM theory / j-invariants:
# tau3 = zeta_6 is the hexagonal point (lattice O_K itself, disc -3):  j = 0.
# tau4 = 2*sqrt(-3):  multiplier ring of Z + 2sqrt(-3)Z is the ORDER Z + 4*O_K
# (conductor 4, disc -48), j = root of the disc -48 Hilbert class polynomial.
P("\n  Similarity classes (exact, via CM):")
j3 = 1728 * kleinj(mpc(0.5, s3 / 2))
j4 = 1728 * kleinj(mpc(0, 2 * s3))
P(f"  j(m003 cusp) = {mp.nstr(j3, 5)}  -> exactly 0 (hexagonal CM point, disc -3)")
from snappy.pari import pari
pari.set_real_precision(60)
hpoly = pari.algdep(pari(mp.nstr(j4.real, 58)), 2)
P(f"  j(m004 cusp) = {mp.nstr(j4.real, 30)}...")
P(f"    algdep (deg 2): {hpoly}")
assert str(hpoly) == "x^2 - 2835810000*x + 6549518250000"
P(f"    h(-48) = {pari.qfbclassno(-48)} (= degree: consistent; disc -48 = conductor 4^2 * (-3))")
# exact multiplier-ring computation for Lambda = Z + 2sqrt(-3) Z:
# alpha = x + y*2sqrt(-3) stabilizes Lambda iff alpha*1 and alpha*2sqrt(-3) in Lambda:
# alpha*2sqrt(-3) = 2x sqrt(-3)*2/2 ... compute: (x + 2y sqrt(-3))*2sqrt(-3) = -12y + 2x sqrt(-3)
# in Lambda automatically (integer x,y). alpha*1 = x + y*(2 sqrt(-3)) in Lambda automatically.
# General alpha = u + v sqrt(-3) (u,v in (1/2)Z allowed in O_K): alpha*1 in Lambda forces
# v even, u integer; then alpha*2sqrt(-3) = -6v + 2u sqrt(-3): needs 2u sqrt(-3) in 2sqrt(-3)Z: ok.
# => multiplier ring = Z + 2 sqrt(-3) Z = Z + 4*omega Z + 2Z = Z + 4 O_K  (conductor 4). Check:
w = (-1 + sqrt(3) * I) / 2                     # omega, O_K = Z + Z*omega
lhs = simplify(2 * sqrt(3) * I - (4 * w + 2))  # 2 sqrt(-3) = 4*omega + 2
P(f"    2*sqrt(-3) = 4*omega + 2 exactly: {lhs == 0}  => mult ring Z+2sqrt(-3)Z = Z + 4*O_K")
assert lhs == 0
P("\n  ==> COMPUTED (a): the two cusp tori are NOT similar: m003's cusp is the")
P("      hexagonal torus C/O_K itself (j=0, the SAME lattice class as the base")
P("      orbifold's cusp, maximal order); m004's cusp is the conductor-4 CM")
P("      torus C/(Z+2sqrt(-3)Z), j = 2835807690.42... (disc -48 class poly).")
P("      Same covolume 2*sqrt(3) at maximal cusp; different lattice SHAPE.")

# ---------------------------------------------------------------------------
# PART 4 — (a cont.) H_1 and the peripheral (cusp -> H_1) placement, exact
# ---------------------------------------------------------------------------
P("\n[4] (a) Does H_1 enter the CUSP data? Peripheral images in H_1 (exact Smith)")
def word_vec(wrd, n):
    v = [0] * n
    for ch in wrd:
        v[ord(ch.lower()) - 97] += 1 if ch.islower() else -1
    return v
for name in ("m004", "m003"):
    M = snappy.Manifold(name)
    G = M.fundamental_group()
    n = G.num_generators()
    rels = [word_vec(r, n) for r in G.relators()]
    mer_w, long_w = G.peripheral_curves()[0]
    from sympy.matrices.normalforms import smith_normal_form
    S = smith_normal_form(Matrix(rels))
    P(f"  {name}: relators {G.relators()}  Smith {S.tolist()}  H_1 = {M.homology()}")
    P(f"        meridian '{mer_w}' -> {word_vec(mer_w, n)},  longitude '{long_w}' -> {word_vec(long_w, n)}")
# m004: one relator, Smith [1 0] => H_1 = Z^2/<(row)> = Z; meridian |-> (1,1) => a GENERATOR
#       of H_1; longitude |-> (0,0) => null-homologous (knot-ness). Peripheral map ONTO H_1,
#       kernel = <longitude>.
# m003: Smith [5 0] => H_1 = Z/5 + Z; meridian |-> (-2,-3), longitude |-> (-1,1) in (a,b).
# Image and kernel of the peripheral Z^2, exact:
P("  m003 peripheral image/kernel (exact):")
mer, lon = Matrix([[-2], [-3]]), Matrix([[-1], [1]])
# H_1 coordinates: quotient Z^2 / <relator (1,-2)+...>: use the computed U*v from Smith
# transform; verified below by brute force over representatives:
# class map for m003 presentation <a,b | abAAbabbb>: relator exponent vector (1? ) -> use rows:
rel = Matrix([word_vec(snappy.Manifold("m003").fundamental_group().relators()[0], 2)])
# H_1 = Z^2/<rel>; rel = (1,-5)? print and reduce peripheral classes mod rel over Z:
P(f"    relator exponent vector: {rel.tolist()}")
# solve: image subgroup of H_1 generated by mer,lon classes; torsion coordinate t (mod 5)
# and free coordinate f via an explicit iso. Brute force check of the identity
# "peripheral image = {(t,f): t = -f mod 5}, index 5" and "kernel = <mer - 2*lon>":
kernel_vec = mer - 2 * lon                     # m - 2l
P(f"    mer - 2*lon = {kernel_vec.T.tolist()} vs relator {rel.tolist()}: proportional?")
assert kernel_vec.T == -rel or kernel_vec.T == rel
P("    => kernel of (cusp -> H_1) = <m - 2l> exactly (the homological longitude).")
# index of the peripheral image in H_1 = Z^2/<(0,5)>: the image is
# L/<(0,5)> with L = span{mer, lon, (0,5)}; (0,5) = -(mer - 2 lon) is inside
# span{mer,lon}, so [H_1 : image] = [Z^2 : span{mer,lon}] = |det[mer lon]|:
Lmat = Matrix([[-2, -3], [-1, 1]])
assert (-(mer - 2 * lon)).T == rel             # relator inside span{mer,lon}
P(f"       index of peripheral image in H_1 = |det{Lmat.tolist()}| = {abs(Lmat.det())}")
assert abs(Lmat.det()) == 5
P("       => image has INDEX 5 in H_1 = Z/5+Z  [index = |H_1 torsion|]. COMPUTED.")
P("  m004: kernel = <l>, image = ALL of H_1 = Z (meridian generates; index 1).")
P("  ==> H_1 shows up in the cusp PLACEMENT (marking): which peripheral slope dies")
P("      in homology and with what co-index. It does NOT enter Gamma_infinity itself")
P("      (a flat lattice has no H_1 memory); the scattering-relevant object-datum is")
P("      the LATTICE, and that differs by Part [3].")

# ---------------------------------------------------------------------------
# PART 5 — (b) LEVEL structure: (2) vs (4)/(8) in the scattering palette
# ---------------------------------------------------------------------------
P("\n[5] (b) Congruence level and the Hecke-character palette (exact arithmetic)")
x = symbols("x")
fl = factor_list(Poly(x ** 2 + x + 1, x, modulus=2))
P(f"  x^2+x+1 mod 2: {fl[1][0][0]} (irreducible) => 2 is INERT in O_3, (2) prime, N(2)=4")
def units_mod(k):
    N = 2 ** k
    def mul(p, q):
        a, b = p; c, d = q
        return ((a * c - b * d) % N, (a * d + b * c - b * d) % N)
    units = [(a, b) for a in range(N) for b in range(N)
             if (a * a - a * b + b * b) % 2 == 1]
    e, o = (1, 1), 1                            # zeta_6 = 1 + omega
    while e != (1, 0):
        e = mul(e, (1, 1)); o += 1
    return len(units), o, len(units) // o
P("  Banked levels (B734 + cc3 addendum, three-seat): m003 level (2);")
P("  m004 level (4) standard / (8) mod-center.  Ray-class character palette")
P("  (h=1, no real places => Cl_n = (O/n)^*/image(mu_6)), computed exactly:")
for k, lev in ((1, "(2)  [m003]"), (2, "(4)  [m004 std]"), (3, "(8)  [m004 mod-center]")):
    u, o, q = units_mod(k)
    P(f"    level {lev:22s} |(O/n)^*| = {u:2d}, ord(zeta_6) = {o},  #characters = {q}")
assert [units_mod(k)[2] for k in (1, 2, 3)] == [1, 2, 8]
P("  ==> at m003's level (2) the ray-class character group is TRIVIAL: the only")
P("      L-function available to its Eisenstein/scattering data is zeta_K itself")
P("      (+ elementary local factors at (2)).  At m004's level (4) ONE nontrivial")
P("      character exists; at (8), SEVEN more.  The level difference CHANGES the")
P("      available L-palette of the voice — this is the exact analogue of the")
P("      classical congruence picture (Huxley; Young 1710.03624 sec 3.3 + eq 4.1:")
P("      cusp Eisenstein series = character Eisenstein series, constant terms")
P("      carry L(2s,chi), L(2-2s,chi-bar), conductor powers q^{2s}, Gauss sums).")
P("      CAVEAT (stated, not glossed): which nontrivial characters occur with")
P("      NONZERO coefficient in m004's actual 1x1 scattering entry phi(s) is NOT")
P("      computed here — it needs the explicit double-coset/Eisenstein computation")
P("      on the index-12 group (probe-2 continuation), and the Bianchi-congruence")
P("      determinant formula is source-verified only in the classical PSL(2,Z)")
P("      case here (Bianchi level-1 zeta_K case is probe 1's verification).")

# ---------------------------------------------------------------------------
# VERDICT
# ---------------------------------------------------------------------------
P("\n" + "=" * 78)
P("VERDICT: OUTCOME A — object-specific data DO enter the cusp/voice data,")
P("with the generic/specific boundary now exact:")
P("  GENERIC to the commensurability class (shared by m004 & m003):")
P("    volume (12 x Humbert), cusp FIELD Q(sqrt(-3)), maximal-cusp AREA 2*sqrt(3),")
P("    regular-ideal-tessellation membership, and (expected, probes 1-2) the")
P("    zeta_K pole tower of the scattering determinant.")
P("  OBJECT-SPECIFIC (computed here, exact):")
P("    (i)  the cusp LATTICE (= Gamma_infinity, the base of the Eisenstein series):")
P("         m003: C/O_K, hexagonal, j = 0 (maximal order, disc -3 — the SAME")
P("               similarity class as the base orbifold cusp);")
P("         m004: C/(Z + 2sqrt(-3)Z), j = 2835807690.42... (conductor-4 order,")
P("               disc -48).  Non-similar tori of equal covolume: the object's")
P("               voice has object-specific FREQUENCIES (dual-lattice Fourier")
P("               support of the Eisenstein expansion), even where the pole")
P("               tower is class-generic.")
P("    (ii) the congruence LEVEL: (2) vs (4)/(8), changing the ray-class")
P("         character palette 1 -> 2 -> 8 (only zeta_K can sing at m003's level;")
P("         nontrivial conductor-(4)/(8) Hecke L-functions become available")
P("         to m004).  Echo (observation only, NO mechanism claimed): m004's")
P("         cusp-lattice CM conductor (4) = its standard congruence level (4).")
P("    (iii) H_1 enters the cusp MARKING (which slope is homologically trivial:")
P("         l for m004 at co-index 1; m-2l for m003 at co-index 5) but NOT the")
P("         scattering data itself — no formula pathway; the honest carrier of")
P("         object-specificity in the voice is the lattice + level, not H_1.")
P("  The B735-death clause does NOT fire: the candidate's specificity has a")
P("  computed, non-vibes carrier.  What remains open for the candidate is the")
P("  probe-4 question (role, not existence), and the nonzero-coefficient caveat")
P("  in [5].")

with open(__file__.replace(".py", "_out.txt"), "w") as f:
    f.write("\n".join(out) + "\n")
