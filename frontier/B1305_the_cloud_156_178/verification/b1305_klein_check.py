"""B1305 Q2(f) -- memo 170's 'fusion that must not be made', checked on main (DESIGN sealed 7e1a7420): does any main surface identify
B1174's legs / B730's faces (V4 = Gal(Q(sqrt-3, sqrt5)/Q): subfields sqrt-3, sqrt5, sqrt-15) with B1182's frame <c, r> / Gal(Q(zeta12)/Q)
(subfields sqrt-3, sqrt3, sqrt-1)? Scan docs/*.md and frontier/*/FINDINGS.md for sentences that contain a 'faces/legs' token AND a
'zeta12 / <c,r> / frame' token AND an equality/identity verb. Prediction: none asserts the identity. Every hit is printed for reading."""
import os, re, glob, json, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
files = sorted(glob.glob(os.path.join(ROOT, "docs", "*.md")) + glob.glob(os.path.join(ROOT, "frontier", "*", "FINDINGS.md")))
A = re.compile(r"B730|three faces|B1174's legs|legs are|√−15|sqrt\(-15\)|√5\)/ℚ|sqrt5\)/Q|being.hearing.meeting", re.I)
B = re.compile(r"ζ₁₂|zeta_?12|ζ_12|⟨c, ?r⟩|<c, ?r>|frame V₄|frame V4|B1182", re.I)
V = re.compile(r"\b(is|are|=|≅|same|one|identical|equals?|fuse[sd]?|join(ed|s)?)\b", re.I)
hits = []
for f in files:
    t = open(f, encoding="utf-8", errors="replace").read()
    for s in re.split(r"(?<=[.!?])\s+|\n\n", t):
        if A.search(s) and B.search(s) and V.search(s):
            hits.append((os.path.relpath(f, ROOT), " ".join(s.split())[:400]))
print(f"scanned {len(files)} files; sentences with a faces/legs token AND a zeta12/frame token AND an identity verb: {len(hits)}")
for f, s in hits: print(f"  {f} | {s}")
# the arithmetic fact behind the caution, computed: the quadratic subfields of the two V4-extensions
import sympy as sp
def quad_subfields(gens):
    """squarefree parts of products of the generators' radicands (the three quadratic subfields of a biquadratic field)"""
    from sympy.ntheory.factor_ import core
    a, b = gens
    return sorted((1 if d > 0 else -1) * int(core(abs(d))) for d in (a, b, a * b))
faces = quad_subfields((-3, 5)); z12 = quad_subfields((-3, -1))
print(f"  quadratic subfields: B730/B1174/B1276's V4 = Q(sqrt-3, sqrt5): {faces};  B1182's Gal(Q(zeta12)/Q) = Q(sqrt-3, i): {z12};  shared: {sorted(set(faces) & set(z12))}")
json.dump(dict(hits=hits, faces=faces, z12=z12), open("b1305_klein_check.json", "w"), indent=1)
print("Q2(f): every hit above is a READ item; the verdict is written in FINDINGS after reading (the scan cannot judge an identity claim).")
