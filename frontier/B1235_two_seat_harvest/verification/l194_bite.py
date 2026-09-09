"""L194 bite control: is any quarter-class amphichiral manifold itself an orientation double cover?
Quarter-class = amphichiral with CS = 1/4 (mod 1/2). A cover of N has vol = 2 vol(N); for each quarter-class
manifold X test every nonorientable census manifold N with vol(N) = vol(X)/2, build its orientation double cover
and test isometry (orientation-blind isometry is the right notion here: CS(cover) = 0 is a statement about the
manifold). Also the direct test: does X have a free orientation-reversing involution? -- read off from the
symmetry group when SnapPy exposes it; otherwise the cover search is the test."""
import json, snappy
fam = json.load(open("frontier/B1235_two_seat_harvest/verification/chirality_112.json"))
quarter = [r for r in fam if r["amphicheiral"] and abs(abs(r["cs"] % 0.5) - 0.25) < 1e-6]
print(f"quarter-class amphichiral members of the 112-family: {len(quarter)}")
# positive control (MB12): the search must FIND a genuine cover -- m004 is the Gieseking manifold m000's
# orientation double cover (CS 0), and its sibling m003 (CS 1/4, same volume) is not.
C0 = snappy.Manifold("m000").orientation_cover()
assert C0.is_isometric_to(snappy.Manifold("m004")) and not C0.is_isometric_to(snappy.Manifold("m003"))
print("positive control: m000's orientation double cover IS m004 (CS 0) and is NOT m003 (CS 1/4) -- the search discriminates")
nonor = list(snappy.NonorientableCuspedCensus())
print(f"nonorientable cusped census: {len(nonor)} manifolds")
vols = [(N.name(), float(N.volume())) for N in nonor]
hits, tested = [], 0
for r in quarter:
    X = snappy.Manifold(r["name"]); vx = float(X.volume())
    cands = [n for n, v in vols if abs(2*v - vx) < 1e-6]
    found = None
    for n in cands:
        N = snappy.Manifold(n)
        C = N.orientation_cover()
        tested += 1
        if C.is_isometric_to(X):
            found = n; break
    print(f"  {r['name']:12s} vol {vx:.6f}  half-volume nonorientable candidates: {len(cands):3d}  double cover? {found}")
    if found: hits.append((r["name"], found))
print(f"\ncover-isometry tests run: {tested}")
print("FENCE: quotients are searched in the nonorientable cusped census (1260); a quotient outside it is not excluded by this cell")
print("VERDICT:", "L194 REFUTED -- quarter-class manifold(s) that ARE orientation double covers: %s" % hits if hits
      else "L194 SURVIVES the bite -- none of the %d quarter-class members is an orientation double cover of any half-volume nonorientable census manifold" % len(quarter))
