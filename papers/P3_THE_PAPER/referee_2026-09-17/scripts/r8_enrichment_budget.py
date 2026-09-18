"""What does ENRICHING THE FIRST STEP actually buy, in dimensions?

The obstruction: the construction is one variational step (Jorgensen minimality picks m004) followed
by pure invariant extraction, and an equivariant machine cannot emit a non-invariant number.  To
carry parameters, the first step must range over a space that CONTAINS them as coordinates.

So: count the coordinates each candidate enrichment actually supplies, for THIS object.

  (0) the bare object                      -- discrete, 0 continuous coordinates
  (1) its own moduli (Dehn surgery space)  -- Thurston: #cusps complex = 2 real for m004
  (2) flat G-connections (character var.)  -- (rank G) * #cusps complex  [Thurston; Menal-Ferrer-Porti]
  (3) matter: modes on the object          -- not a dimension count; an exponential scale question

For (3) the only known geometric mechanism for a Yukawa HIERARCHY is exponentially suppressed
overlap, exp(-distance).  Necessary condition: does the object's own geodesic length spectrum span
the range the observed hierarchy needs?  That is computable, and it is computed here.

Nothing below is evidence FOR anything.  A necessary condition that fails kills a direction; a
necessary condition that passes leaves it merely alive.
"""
import snappy, warnings, math
warnings.filterwarnings("ignore")

M = snappy.Manifold('m004')

print("=" * 78)
print("the object")
print("=" * 78)
print(f"   m004   volume {float(M.volume()):.10f}   cusps {M.num_cusps()}   homology {M.homology()}")
try:
    S = M.symmetry_group()
    print(f"   symmetry group: {S}   order {S.order()}")
    print(f"   is amphichiral: {S.is_amphicheiral()}")
except Exception as e:
    print(f"   symmetry group: {type(e).__name__}")

print()
print("=" * 78)
print("(1)+(2) the parameter budget: how many real coordinates each enrichment supplies")
print("=" * 78)
c = M.num_cusps()
print(f"   cusps = {c},  so b1 = {c}")
print()
print("   enrichment                                     complex dim   REAL dim   vs 19 needed")
print(f"   bare object (complete structure, Mostow)             0            0        short by 19")
print(f"   Dehn surgery space  (Thurston: dim = cusps)          {c}            {2*c}        short by {19-2*c}")
for name, rank in [("SU(2)", 1), ("SM: SU(3)xSU(2)xU(1)", 4), ("SU(5)", 4), ("SO(10)", 5),
                   ("E6", 6), ("E8", 8), ("E8 x E8", 16)]:
    d = rank * c
    print(f"   flat {name:<24s} rank {rank:<2d}        {d:<2d}           {2*d:<2d}"
          f"       {'short by ' + str(19 - 2*d) if 2*d < 19 else 'ENOUGH (' + str(2*d) + ')'}")
print()
print("   => with ONE cusp, no flat-connection moduli space for a group of rank <= 9 has room")
print("      for 19 real numbers.  And the SM's own gauge group has rank 4: eight real")
print("      coordinates, all of them gauge-sector.  The nine Yukawas are not in there at all.")

print()
print("=" * 78)
print("(3) the hierarchy: does the object's length spectrum span what Yukawas need?")
print("=" * 78)
counts = {}
lens = []
for cut in (2.0, 3.0, 4.0, 5.0):
    got = []
    for g in M.length_spectrum(cut):
        try:
            L = float(g.length.real())
        except Exception:
            L = float(complex(g.length).real)
        got.append(L)
    got.sort()
    counts[cut] = len(got)
    if len(got) > len(lens):
        lens = got
print("   geodesic counts N(L) (SnapPy length_spectrum, real part of complex length):")
for cut in sorted(counts):
    print(f"      L <= {cut:>4.1f}:  N = {counts[cut]:>6d}")
# least-squares fit of log N = log C + s L over the measured window
xs = sorted(counts)
ys = [math.log(counts[c]) for c in xs]
n = len(xs)
mx_, my_ = sum(xs) / n, sum(ys) / n
s = sum((xs[i] - mx_) * (ys[i] - my_) for i in range(n)) / sum((x - mx_) ** 2 for x in xs)
logC = my_ - s * mx_
print(f"      fit over this window:  N(L) ~ {math.exp(logC):.3f} * exp({s:.3f} L)"
      f"   (exponential growth, as it must be: entropy = 1)")
print()
print(f"   systole: {lens[0]:.9f}      exp(-systole) = {math.exp(-lens[0]):.6e}")
print("   first eight lengths and their suppressions exp(-L):")
for L in lens[:8]:
    print(f"      L = {L:.9f}    exp(-L) = {math.exp(-L):.6e}")

print()
print("   what the observed hierarchy needs (PDG central values, one scale):")
masses = {"electron": 0.511e-3, "muon": 0.10566, "tau": 1.77686,
          "up": 2.16e-3, "down": 4.67e-3, "strange": 93.4e-3,
          "charm": 1.27, "bottom": 4.18, "top": 172.69}
mx, mn = max(masses.values()), min(masses.values())
need = math.log(mx / mn)
print(f"      top / electron = {mx/mn:.6g}   ->   needs a length gap dL = {need:.4f}")
print(f"      the spectrum is infinite and L -> infinity, so a gap of {need:.2f} trivially exists.")
print()
print("   THE REAL NUMBER: how much fitting freedom does that gap contain?")
Lmax = need + lens[0]
est = math.exp(logC + s * Lmax)
print(f"      geodesics with L <= systole + {need:.2f} = {Lmax:.2f}:"
      f"  extrapolating the fit, N ~ {est:,.0f}")
print(f"      (an extrapolation from a window ending at L = {max(counts):.0f}, not a count)")
print(f"      parameters to be explained by choosing among them: 9 Yukawas")
print()
print("   VERDICT.  The magnitude range is available -- that necessary condition passes, so an")
print("   exponential-overlap mechanism is not killed on scale grounds.  But the enrichment")
print("   supplies on the order of {0:,.0f} candidate lengths to fit 9 numbers.  An enrichment that".format(est))
print("   offers more freedom than the data constrains can FIT the parameters; it cannot PREDICT")
print("   them.  That is the criterion any enrichment of the first step has to meet, and it is")
print("   the criterion Jorgensen minimality meets perfectly: zero choices in, one object out.")
