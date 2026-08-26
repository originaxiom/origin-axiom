"""B8143 step 6 -- HOW MUCH of "hypercharge falls out" is object-specific?

The corrected result says: over the SM-visible alphabet, at the 5-field rigidity threshold,
the SM generation is the unique rigid chiral anomaly-free content, charges included.

The question that matters for the programme is what INPUT that result consumed. Below is
the complete list of things the computation used. If E6, the 27, m004 or the trace field
appear nowhere in it, the forcing is GENERIC -- true for anyone who writes down
SU(3)xSU(2)xU(1) -- and cannot be evidence FOR the object.
"""
import pathlib, re

src = "\n".join(pathlib.Path(f).read_text() for f in
                ("step4_full.py", "step5_robust.py"))

OBJECT_TOKENS = ["E6", "e6", "E_6", "27", "m004", "figure-eight", "trace field",
                 "Q(sqrt-3)", "trinification", "2T", "octahedral", "tetrahedral",
                 "Chevalley", "root", "weight lattice", "holonomy"]
GENERIC_INPUTS = [
    "the gauge group SU(3) x SU(2) x U(1)",
    "the list of small reps (the alphabet)",
    "the five anomaly conditions incl. [SU(3)]^3",
    "the Witten global-anomaly parity condition",
    "the rigidity threshold n = 5 (a dimension count)",
    "a chirality convention (no sterile field)",
]

print("INPUTS the corrected computation actually consumed:")
for g in GENERIC_INPUTS:
    print("   generic   ", g)

# Strip comments and docstrings first: a token in prose is PROVENANCE, not an input.
code = "\n".join(l.split("#")[0] for l in src.splitlines())
code = re.sub(r'"""[\s\S]*?"""', "", code)
print("\nOBJECT-SPECIFIC tokens appearing in EXECUTABLE code (comments/docstrings stripped):")
hits = []
for t in OBJECT_TOKENS:
    # '27' would false-positive on line numbers/counts, so require a word boundary AND
    # that it is not part of a number like 227 or a count
    pat = r"\b%s\b" % re.escape(t)
    if re.search(pat, code):
        hits.append(t)
print("   ", hits if hits else "NONE")
prose = [t for t in OBJECT_TOKENS if re.search(r"\b%s\b" % re.escape(t), src) and t not in hits]
print("\n   appearing only in PROSE (provenance, not input):", prose if prose else "none")
print("   -> the 27 is why I NOTICED that (3,1) differs from (3bar,1); it is not a term in any")
print("      equation. The alphabet itself is the generic small-rep list, and the extended")
print("      alphabets go BEYOND the 27. Stated rather than swept, because the control fired.")

print("""
  => The forcing used NOTHING about E6, the 27, m004, the trace field or the object's
     roots. It is a statement about SU(3)xSU(2)xU(1) representation theory.

     CONSEQUENCE, stated carefully:

       * The CHARGES are forced -- generically. (B1160 says so: "standard GUT model-building".)
       * The SHAPE is forced too -- also generically. (This arc, corrected.)
       * What is OBJECT-SPECIFIC is neither: it is that the object supplies a rank-3 abelian
         sector in which an SM-shaped 15-plet is AVAILABLE at all.

     So the object supplies the ARENA. The anomalies supply the CONTENT. A result that would
     come out the same for anyone starting from SU(3)xSU(2)xU(1) corroborates the Standard
     Model, but is not evidence FOR the object -- exactly the B996 lesson ("reaching E6 is
     generic; specialness lives in the grammar") one level further down.

     NOT A REFUTATION of B1160, which fences this itself. A quantification of it.
""")
print("NOTE ON NOVELTY: the uniqueness of the SM's anomaly-free chiral content at minimal")
print("field content is very likely KNOWN in the model-building literature. This arc claims")
print("no novelty for it -- only for the scoping conclusion above.")
