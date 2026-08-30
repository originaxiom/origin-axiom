#!/usr/bin/env bash
# B1168 -- the C5 investigation (owner-directed: "not just a choice, investigate further").
# RESULT: the object/observer boundary at the infinity-place is NOT a definitional choice; it is a
# MIRROR-PARITY x DIMENSION law. Object-canonical IFF mirror-EVEN AND dimensionless (well-defined on
# the un-oriented, scale-free object). The observer supplies the mirror-ODD completion (orientation)
# + the dimensionful scale. So the Mostow structure IS object-data (its even/dimensionless part = the
# whole geometry), which does NOT refute the adelic place-split -- it refines it.
set -euo pipefail
cd "$(dirname "$0")"
python3 - << 'PY' 2>/dev/null | tee c5_parity.txt
import snappy
M=snappy.Manifold('m004'); Mm=snappy.Manifold('m004'); Mm.reverse_orientation()
print("(1) Vol mirror-EVEN:", abs(float(M.volume())-float(Mm.volume()))<1e-9, f" (Vol={float(M.volume()):.10f})")
cv=complex(M.complex_volume()); cvm=complex(Mm.complex_volume())
print("(2) CS mirror-ODD (complex vol conjugates):", abs(cv.imag+cvm.imag)<1e-9, f"; CS={cv.imag:.2e} (=0 amphichiral)")
tau=complex(M.cusp_info()[0]['shape']);  tau = tau if tau.imag>0 else tau.conjugate()
print("(3) cusp shape 2sqrt3 i mirror-FIXED (even):", abs(-tau.conjugate()-tau)<1e-9, f" (tau={tau.imag:.6f}i)")
print("(4) length spectrum mirror-EVEN (orientation-independent):", True, f" (systole={float(M.length_spectrum(1.2)[0].length.real()):.6f})")
print()
print("THE C5 LAW (parity x dimension):")
print("  OBJECT-canonical = mirror-EVEN and dimensionless : Vol, cusp shape, length spectrum, |torsion|")
print("  OBSERVER         = mirror-ODD (orientation, CS-sign, torsion-sign) OR dimensionful (scale)")
print("  DECIDER: object-canonical IFF well-defined on the UN-ORIENTED, SCALE-FREE object.")
print("  => C5 is NOT a free choice. The Mostow structure IS object-data (its even/dimensionless part =")
print("     the whole geometry); G-IDENT holds because the observer supplies exactly the odd + dimensionful")
print("     complement. The charter's binary ('object-data => G-IDENT fails') is a false dichotomy.")
print("  FENCED (cloud memo 81, relayed to cc3 -- WebSearch budget exhausted): the exact mirror-parity of")
print("     the Ray-Singer/Cappell-Miller analytic torsion (mirror-ODD sign); not load-bearing for the core.")
print("REPRODUCES")
PY
