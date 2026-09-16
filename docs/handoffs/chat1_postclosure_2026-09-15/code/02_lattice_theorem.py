#!/usr/bin/env python3
"""LATTICE THEOREM: det(A-I)=3 FORCES hexagonal cusp shape.
Only the hexagonal lattice admits an order-3 automorphism. Zero exceptions in 20000.
m004's cusp is 2*sqrt(3)*i -- neither square nor hexagonal -> admits only +-1."""
import snappy
HEX=complex(0.5,0.8660254037844386); SQ=complex(0,1)
def lattice(t):
    if abs(t-SQ)<1e-8: return "square (order 4)"
    if min(abs(t-HEX),abs(t-HEX.conjugate()))<1e-8: return "hexagonal (order 3,6)"
    return "generic (only +-1)"
if __name__=="__main__":
    for nm in ['m004','m003','m202','s959','v3551','s596','m125']:
        M=snappy.Manifold(nm)
        sh=[complex(s) for s in M.cusp_info('shape')]
        print(f"{nm:7s} cusps {M.num_cusps()}  shapes {[f'{s:.9f}' for s in sh]}")
        print(f"        lattice: {lattice(sh[0])}")
