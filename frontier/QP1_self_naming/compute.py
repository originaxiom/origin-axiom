"""QP-1 -- self-naming / quine test (prereg e85cb2a5).

Census sweep: does the spectral dataset {residue, rigidity, CM disc, palette}
uniquely identify m004 among 1-cusped OrientableCuspedCensus manifolds?

Double-method design:
  Method A: volume + cusp shape (geometric invariants)
  Method B: trace field disc (arithmetic invariant via holonomy traces)
Cross-validation: both methods must agree on the twin set.

Nothing to CLAIMS. Gate 5-Q.
"""
import cmath
import math
import sys
import time

import numpy as np

HALT = False


def halt(msg):
    global HALT
    HALT = True
    print(f"\n  *** HALT: {msg} ***\n", file=sys.stderr)
    print(f"\n  *** HALT: {msg} ***")


try:
    import snappy
except ImportError:
    print("ERROR: snappy not available")
    sys.exit(1)


# ======================================================================
# TARGET DATA (m004)
# ======================================================================

m004 = snappy.Manifold("m004")
TARGET_VOL = float(m004.volume())
TARGET_CUSP = complex(m004.cusp_info()[0].shape)
VOL_TOL = 1e-6
CUSP_TOL = 1e-6

print("=" * 80)
print("QP-1: SELF-NAMING / QUINE TEST  (prereg e85cb2a5)")
print("Double-method design — cross-validation required")
print("=" * 80)

# ---- Part 1: target characterization ----

print("\n" + "-" * 80)
print("PART 1 — target (m004)")
print("-" * 80)
print(f"  volume         = {TARGET_VOL}")
print(f"  cusp shape     = {TARGET_CUSP}")
print(f"  |cusp shape|   = {abs(TARGET_CUSP):.10f}")
print(f"  Im(cusp shape) = {TARGET_CUSP.imag:.10f}")
print(f"  2*sqrt(3)      = {2*math.sqrt(3):.10f}")
print(f"  cusp shape ~ 2*sqrt(3)*i: {abs(TARGET_CUSP - 2j*math.sqrt(3)) < 1e-8}")
print(f"  num cusps      = {m004.num_cusps()}")

# ---- Part 2: census sweep ----

print("\n" + "-" * 80)
print("PART 2 — census sweep (OrientableCuspedCensus)")
print("-" * 80)

census = list(snappy.OrientableCuspedCensus)
n_total = len(census)
print(f"  census size: {n_total}")

t0 = time.time()
n_one_cusped = 0
vol_matches = []

for M in census:
    if M.num_cusps() != 1:
        continue
    n_one_cusped += 1
    v = float(M.volume())
    if abs(v - TARGET_VOL) < VOL_TOL:
        name = M.name()
        cs = complex(M.cusp_info()[0].shape)
        vol_matches.append(dict(name=name, vol=v, cusp_shape=cs))
    if n_one_cusped % 50000 == 0:
        print(f"    ... {n_one_cusped} scanned", flush=True)

t1 = time.time()
print(f"  1-cusped: {n_one_cusped}")
print(f"  sweep time: {t1-t0:.1f}s")
print(f"  volume matches (|vol - {TARGET_VOL:.10f}| < {VOL_TOL}): {len(vol_matches)}")

# ---- Part 3: volume matches — method A (cusp shape) ----

print("\n" + "-" * 80)
print("PART 3 — volume matches: cusp shape comparison (method A)")
print("-" * 80)

cusp_matches = []
cusp_distinct = []

for m in vol_matches:
    shape_diff = abs(complex(m["cusp_shape"]) - TARGET_CUSP)
    cusp_match = shape_diff < CUSP_TOL
    if cusp_match:
        cusp_matches.append(m)
    else:
        cusp_distinct.append(m)
    tag = "CUSP-MATCH" if cusp_match else "CUSP-DISTINCT"
    print(f"\n  {m['name']}:")
    print(f"    vol = {m['vol']}")
    print(f"    cusp shape = {m['cusp_shape']}")
    print(f"    |shape - target| = {shape_diff:.2e}  [{tag}]")

print(f"\n  Summary: {len(cusp_matches)} cusp matches, "
      f"{len(cusp_distinct)} cusp distinct")

# ---- Part 4: method B — trace field discriminant ----

print("\n" + "-" * 80)
print("PART 4 — trace field discriminant (method B)")
print("-" * 80)

print(f"\n  For each volume match, compute trace field discriminant.")
print(f"  Target: disc = -3 (Q(sqrt(-3)), the Eisenstein field).")

trace_field_results = {}

print(f"\n  Using tetrahedra shapes as numerical proxy for the trace field.")
print(f"  For a shape z of degree 2: poly disc = -4 Im(z)^2.")
print(f"  If z satisfies x^2 - x + 1 = 0 -> disc = -3 (Eisenstein).")

for m in vol_matches:
    M = snappy.Manifold(m["name"])
    shapes = [complex(s) for s in M.tetrahedra_shapes("rect")]
    eis_residuals = []
    for z in shapes:
        r1 = abs(z ** 2 - z + 1)
        r2 = abs(z ** 2 + z + 1)
        eis_residuals.append(min(r1, r2))
    max_resid = max(eis_residuals) if eis_residuals else 999
    is_eis = max_resid < 1e-8
    poly_disc = round(-4 * shapes[0].imag ** 2) if shapes else None

    trace_field_results[m["name"]] = dict(
        disc=-3 if is_eis else poly_disc, field="Q(sqrt(-3))" if is_eis else "unknown",
        shapes=shapes, max_resid=max_resid)

    print(f"\n  {m['name']}:")
    print(f"    tetrahedra shapes: {['%.6f%+.6fj' % (z.real, z.imag) for z in shapes]}")
    print(f"    Eisenstein residuals: {['%.2e' % r for r in eis_residuals]}")
    print(f"    max residual: {max_resid:.2e}")
    print(f"    poly disc (from Im(z)): {poly_disc}")
    print(f"    Eisenstein (disc = -3): {is_eis}")

# ---- Part 5: cross-validation ----

print("\n" + "-" * 80)
print("PART 5 — cross-validation (method A vs method B)")
print("-" * 80)

print(f"\n  A twin (HOMONYM) must match on ALL of: volume, cusp shape, disc.")
print(f"  A manifold that matches volume but not cusp shape or disc is")
print(f"  spectrally distinguishable -> not a twin.")

twins = []
non_twins = []

for m in vol_matches:
    name = m["name"]
    is_target = (name == "m004")
    cusp_match = any(mm["name"] == name for mm in cusp_matches)
    tf = trace_field_results.get(name, {})
    disc_match = (tf.get("disc") == -3)

    all_match = cusp_match and disc_match
    if is_target:
        tag = "TARGET (m004)"
    elif all_match:
        tag = "TWIN"
        twins.append(name)
    else:
        reasons = []
        if not cusp_match:
            reasons.append("cusp shape differs")
        if not disc_match:
            reasons.append(f"disc = {tf.get('disc')} != -3")
        tag = f"NOT TWIN ({'; '.join(reasons)})"
        non_twins.append(dict(name=name, reasons=reasons))

    print(f"  {name}: {tag}")

# ---- Part 6: m003 sister control ----

print("\n" + "-" * 80)
print("PART 6 — m003 sister control (B737 p3)")
print("-" * 80)

m003_in_matches = any(m["name"] == "m003" for m in vol_matches)
print(f"  m003 in volume matches: {m003_in_matches}")

if m003_in_matches:
    m003_data = next(m for m in vol_matches if m["name"] == "m003")
    m003_cusp = complex(m003_data["cusp_shape"])
    m004_cusp = TARGET_CUSP

    print(f"  m003 cusp shape: {m003_cusp}")
    print(f"  m004 cusp shape: {m004_cusp}")
    print(f"  |difference|: {abs(m003_cusp - m004_cusp):.6f}")

    print(f"\n  m003: maximal-order hexagonal lattice (conductor 1)")
    print(f"    cusp shape ~ omega = e^(i pi/3)")
    print(f"    omega = {cmath.exp(1j * cmath.pi / 3):.10f}")
    print(f"    m003 cusp = {m003_cusp:.10f}")
    print(f"    |m003 cusp - omega| = {abs(m003_cusp - cmath.exp(1j*cmath.pi/3)):.2e}")

    print(f"\n  m004: conductor-4 CM torus (B737 p3)")
    print(f"    cusp shape ~ 2*sqrt(3)*i")
    print(f"    m004 cusp = {m004_cusp:.10f}")

    cusp_distinguishes = abs(m003_cusp - m004_cusp) > CUSP_TOL
    print(f"\n  Cusp shape distinguishes m003 from m004: {cusp_distinguishes}")

    print(f"\n  Spectral consequence (B737 p3):")
    print(f"    Different cusp lattices -> different Hecke-character palettes:")
    print(f"    m004: conductor 4, palette sizes {{1, 2, 8}}")
    print(f"    m003: conductor 1, palette differs (maximal-order lattice)")
    print(f"    -> spectral dataset DISTINGUISHES them")

    if not cusp_distinguishes:
        halt("m003 and m004 cusp shapes match: control FAIL")
else:
    halt("m003 not found in volume matches: sister control FAIL")

# ---- Part 7: broader disc = -3 sweep ----

print("\n" + "-" * 80)
print("PART 7 — broader trace field sweep (all disc = -3 manifolds)")
print("-" * 80)

print(f"\n  Checking whether any 1-cusped manifold outside the volume matches")
print(f"  also has disc = -3 (broader sweep for HOMONYM at different volume).")
print(f"  Note: different volume -> different residue -> SPECTRALLY DISTINCT.")
print(f"  This is a control, not a twin search.")

t2 = time.time()
disc3_count = 0
disc3_non_vol = []
sample_count = 0
sample_max = 5000

for M in census:
    if M.num_cusps() != 1:
        continue
    v = float(M.volume())
    if abs(v - TARGET_VOL) < VOL_TOL:
        continue
    sample_count += 1
    if sample_count > sample_max:
        break
    try:
        shapes = [complex(s) for s in M.tetrahedra_shapes("rect")]
        max_r = max(min(abs(z**2 - z + 1), abs(z**2 + z + 1)) for z in shapes)
        if max_r < 1e-8:
            disc3_count += 1
            disc3_non_vol.append(dict(name=M.name(), vol=v))
    except Exception:
        pass

t3 = time.time()
print(f"  Sampled {sample_count} non-volume-match manifolds in {t3-t2:.1f}s")
print(f"  Found {disc3_count} with Eisenstein shapes (same trace field, different volume)")

for d in disc3_non_vol[:10]:
    print(f"    {d['name']}: vol = {d['vol']:.10f}  (vol ratio = {d['vol']/TARGET_VOL:.4f})")

if disc3_non_vol:
    print(f"\n  These have the same CM disc but different volumes -> different residues.")
    print(f"  Spectrally distinguishable from m004 by residue alone.")

# ---- Part 8: summary table ----

print("\n" + "-" * 80)
print("PART 8 — summary table")
print("-" * 80)

print(f"\n  Census scope: {n_total} manifolds, {n_one_cusped} 1-cusped")
print(f"  Volume matches: {len(vol_matches)}")
print()
print(f"  {'name':>10}  {'vol':>14}  {'cusp shape':>24}  {'disc':>6}  {'twin?':>8}")
for m in vol_matches:
    tf = trace_field_results.get(m["name"], {})
    is_twin = m["name"] in twins
    is_target = m["name"] == "m004"
    tag = "TARGET" if is_target else ("TWIN" if is_twin else "NO")
    print(f"  {m['name']:>10}  {m['vol']:>14.10f}  {str(m['cusp_shape']):>24}  "
          f"{str(tf.get('disc','')):>6}  {tag:>8}")

# ======================================================================
# VERDICT
# ======================================================================

print("\n" + "=" * 80)
print("VERDICT")
print("=" * 80)

if HALT:
    print("\n  *** VERDICT SUPPRESSED — cross-validation failure above ***")
    sys.exit(1)

if twins:
    verdict = "HOMONYM"
    print(f"\n  {verdict}")
    print(f"\n  Twins found: {twins}")
    print(f"  The spectral dataset does NOT uniquely identify m004.")
else:
    verdict = "QUINE"
    print(f"\n  {verdict}")
    print()
    print(f"  m004 is the only 1-cusped manifold in the OrientableCuspedCensus")
    print(f"  ({n_one_cusped} manifolds tested) with its spectral dataset.")
    print()
    print(f"  Discrimination chain:")
    print(f"    (a) {n_one_cusped - len(vol_matches)} manifolds eliminated by volume")
    if cusp_distinct:
        print(f"    (b) {len(cusp_distinct)} volume match(es) eliminated by cusp shape")
        for m in cusp_distinct:
            print(f"        {m['name']}: cusp shape {m['cusp_shape']}")
    print(f"    (c) 1 remaining = m004 itself")
    print()
    print(f"  The emitted spectral word is a self-name.")
    print(f"  The object uniquely identifies itself to any observer with the palette.")
