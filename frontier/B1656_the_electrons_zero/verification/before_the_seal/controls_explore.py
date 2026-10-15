"""C2 exploration (main, unsealed): do the controls bite? (b) a 9-torsion line whose 3w is NOT omega-fixed; (c) a
fictitious lepton charge pair with difference -8 (L = -3, e = 5)."""
import numpy as np, importlib, sys, io, contextlib
with contextlib.redirect_stdout(io.StringIO()): T = importlib.import_module("twisted_D_explore")
OM = T.OM
def sector(w, t, ql, qr):
    x = T.twist_of(ql*w, t); y = T.twist_of(qr*w, t); R = T.residues(x, y, t); n2 = sum(abs(R[s])**2 for s in R)
    c = T.cnorms(x, y, t, R); D = sum(c[s]*R[s]**2 for s in T.UNITS if c[s] is not None)
    return abs(D)/n2, abs(R["1"])/np.sqrt(n2), {s: (None if c[s] is None else round(c[s], 4)) for s in "1ijk"}
for (p1, p2) in [(1/9, 2/9), (1/9, 0), (4/9, 1/9)]:
    w = T.line_w(p1, p2, OM); w3 = 3*w
    fixed = abs(np.round((OM*w3 - w3)/1) - 0) # placeholder
    # is 3w omega-fixed mod the lattice Z + OM Z?  solve OM*w3 - w3 = m + n*OM
    d = OM*w3 - w3; n = d.imag/OM.imag; m = d.real - n*OM.real
    isfixed = abs(m - round(m)) < 1e-9 and abs(n - round(n)) < 1e-9
    D, r1, c = sector(w, OM, -3, 6)
    print(f"(b) line ({p1:.3f},{p2:.3f}): 3w omega-fixed? {isfixed}; lepton |D|/|R|^2 {D:.4f}, |R1|/|R| {r1:.1e}, c {c}")
w = T.line_w(1/9, 1/9, OM)
D, r1, c = sector(w, OM, -3, 5)
print(f"(c) W59 line (1/9,1/9), fictitious leptons (-3, 5): |D|/|R|^2 {D:.4f}, |R1|/|R| {r1:.3f}")
D, r1, c = sector(w, OM, -3, 6)
print(f"    the same line, true leptons (-3, 6): |D|/|R|^2 {D:.2e}, |R1|/|R| {r1:.1e}")
