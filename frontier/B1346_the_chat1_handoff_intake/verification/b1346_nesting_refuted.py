"""B1346 -- Chat-2's structural finding 3a REFUTED: drilling m004 does not give the silver bundle.

Chat-2's handoff (HANDOFF_FRESH_EYES_SESSION.md, section 3a), verbatim:
   "Drilling the shortest geodesic from M(A1) = m004 produces M(A2) -- the silver bundle.
    Volume match: 3.6638623767 to 10^-10. The two metallic bundles are geometrically
    contained in each other ... Previously unrecorded in the programme."

The volume match is REAL. The identification is FALSE, and the control that catches it is in
chat1's OWN handoff: verify_all.py's NEG.2, "TRAP: s958 and s961 share volume, differ".
"""
import warnings; warnings.filterwarnings("ignore")
import snappy

fails = []
def check(tag, label, ok):
    print(f"   [{'PASS' if ok else 'FAIL'}] {tag}: {label}")
    if not ok: fails.append(tag)

M = snappy.Manifold("m004")
w = M.length_spectrum_alt(count=1)[0]["word"]
D = M.drill_word(w)
m136, m129 = snappy.Manifold("m136"), snappy.Manifold("m129")
print(f"   shortest geodesic of m004: word {w}")
print(f"   drill(m004):  cusps {D.num_cusps()}  vol {float(D.volume()):.13f}")
print(f"   m136 (silver bundle): cusps {m136.num_cusps()}  vol {float(m136.volume()):.13f}")
print(f"   m129 (Whitehead link): cusps {m129.num_cusps()}  vol {float(m129.volume()):.13f}")

check("Q1", "the VOLUME match Chat-2 reports is real, to 1e-13",
      abs(float(D.volume()) - float(m136.volume())) < 1e-12)
check("Q2", "but the drilled manifold has TWO cusps and the silver bundle has ONE -- a "
            "once-punctured-torus bundle has exactly one cusp, so the identification cannot hold "
            "whatever the volume", D.num_cusps() == 2 and m136.num_cusps() == 1)
check("Q3", "and SnapPy's isometry test agrees: drill(m004) is NOT isometric to m136",
      not D.is_isometric_to(m136))
check("Q4", "what it IS: m129, the Whitehead link complement (5^2_1 / L5a1) -- isometric",
      D.is_isometric_to(m129))
print(f"   identify(): {D.identify()}")
check("Q5", "so m136 and m129 are a VOLUME-SHARING PAIR that differ -- exactly the trap chat1's "
            "own NEG.2 control flags for s958/s961, in the other seat's handoff",
      abs(float(m136.volume()) - float(m129.volume())) < 1e-12 and not m136.is_isometric_to(m129))

print("\nB1346-nesting:", "PASS" if not fails else f"FAIL ({fails})")
raise SystemExit(0 if not fails else 1)
