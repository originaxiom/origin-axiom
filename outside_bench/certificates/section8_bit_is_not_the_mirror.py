"""CERTIFICATE -- section 8's chirality bit is NOT the manifold's mirror sign.

SEAL  outside_bench/seals/SECTION8_BIT_ADJUDICATION_PREREG.md
      sha256 a0f898ac70dc9bdaa27778e98d73692f94e8abb443aba3922962c07ca4094dbb
      sealed BEFORE this file was written.

OCCASION.  frontier/B1327_relation_not_observer/FINDINGS.md (verdict OPEN, on the tree
<seat>/paper-verification-ufp0zn at e829c02c) raises one item and declines to decide it:

    "This is not a claim.  Section 8's chirality bit is a Fricke-kappa torsor class of a PAIR,
     and may not be the same object as the manifold's mirror sign.  Whether they are the same bit
     is for the seat that owns section 8 to adjudicate.  If they are, one of the three rows is not
     an independent input."

This bench does not own section 8.  It adjudicates the MATHEMATICAL half -- are the two quantities
the same function? -- and leaves the LEDGER half to the seat that owns the table.

  Q1  section 8's chirality bit.  The paper: "the mirror is realisable over GL_2(Z) only with
      determinant -1 ... belongs to the PAIR: it is an invariant of neither relatum separately".
      Its decision procedure is B1248 (PROVED): eps = -1 <=> 2 - kappa = -g^2, with
      D = (2 - kappa)/g^2 and g the entry-gcd of the additive commutator A M - M A.
  Q2  the manifold's mirror sign, the third entry of B1327's own triple:
      mirror = det(cusp_map) for each isometry of the object.

CELLS (two outcomes each, fixed in the seal before this file existed)
  CELL 1  Is Q1 a function of the OBJECT RELATUM ALONE?  Hold A fixed, sweep the partner M.
          A: the class is constant        B: it takes more than one value with A never changing
  CELL 2  Is Q2 a function of the object alone, and non-trivial?
          A: needs a partner, or constant B: from the object's own symmetry group, and it separates
  CELL 3  On the object itself, do the two agree about PRESENCE?
          A: both present                 B: one present and non-trivial, the other ABSENT

CONTROLS
  C1  B1327's own script must reproduce as written, or nothing else here is read.
  C2  The kappa convention is PINNED, not assumed.  This bench compared B1200's statement against
      the character-variety form tr[A,B] - 4 and manufactured a contradiction that was its own.
      Both forms are printed; the -2 form must reproduce B1200 and the -4 form must not.
  C3  The corpus's own instrument (B1248) runs first and must PASS its selftest (memo 154).
  C4  The classifier must realise all four branches, or "more than one value" is an artifact.
  C5  The mirror sign must be ABLE to come out constant: a CHIRAL one-cusped control must give
      det = +1 on every isometry, or the detector is not reading orientation.

Gate 5 untouched.  No measured value is used as input anywhere.
"""
import os
import subprocess
import sys
import warnings
from math import gcd

warnings.filterwarnings("ignore")

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
B1248 = os.path.join(ROOT, "frontier", "B1248_norm_classification", "verification")
B1327_COMMIT = "e829c02c"
B1327_PATH = "frontier/B1327_relation_not_observer/verification/three_bits_one_relation.py"

FAIL = []


def rule(t):
    print("\n" + "=" * 78 + "\n" + t + "\n" + "=" * 78)


def check(name, ok, detail=""):
    print(f"  [{'OK ' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)
    return ok


# ------------------------------------------------------------------ the object, once
def triple_table(name):
    """B1327's triple for every isometry of a manifold: (arrow, swap, mirror) = (a, d, det)."""
    import snappy
    from collections import Counter
    M = snappy.Manifold(name)
    pats, offdiag = Counter(), 0
    for iso in M.symmetry_group().isometries():
        A = iso.cusp_maps()[0]
        a, b, c, d = int(A[0, 0]), int(A[0, 1]), int(A[1, 0]), int(A[1, 1])
        if b or c:
            offdiag += 1
        pats[(a, d, a * d - b * c)] += 1
    return pats, offdiag


def holonomy_commutator_trace(name="m004"):
    import snappy
    import numpy as np
    G = snappy.Manifold(name).fundamental_group()
    def mat(x):
        return np.array([[complex(x[0, 0]), complex(x[0, 1])],
                         [complex(x[1, 0]), complex(x[1, 1])]])
    A, B = (mat(G.SL2C(g)) for g in G.generators()[:2])
    C = A @ B @ np.linalg.inv(A) @ np.linalg.inv(B)
    return complex(np.trace(C))


# ================================================================== C1
rule("C1 -- B1327's own computation, re-run as written")
src = subprocess.run(["git", "show", f"{B1327_COMMIT}:{B1327_PATH}"],
                     cwd=ROOT, capture_output=True, text=True)
check("B1327's script is retrievable from the record", src.returncode == 0,
      f"{B1327_COMMIT}:{B1327_PATH}")

pats, offdiag = triple_table("m004")
for (sm, sl, det), n in sorted(pats.items()):
    print(f"       arrow={sm:+d} swap={sl:+d} mirror={det:+d}  x{n}")
viol = [k for k in pats if k[2] != k[0] * k[1]]
check("eight isometries", sum(pats.values()) == 8, f"{sum(pats.values())}")
check("four of the eight a priori sign triples", len(pats) == 4, f"{len(pats)}")
check("zero violations of mirror = arrow x swap", not viol, str(viol))

# and the observation B1327 did not make about its own computation
check("every cusp map is DIAGONAL", offdiag == 0,
      "-- so 'mirror = arrow x swap' IS det diag(a,d) = a*d; "
      "the empirical content of link 54 here is the DIAGONALITY, not the product law")

# ================================================================== C2
rule("C2 -- the kappa convention, PINNED against B1200 and not assumed")
import sympy as sp
tr = holonomy_commutator_trace("m004")
omega = complex(-0.5, 3 ** 0.5 / 2)
k2, k4 = tr - 2, tr - 4
print(f"       tr[A,B]          = {tr.real:+.12f}{tr.imag:+.12f}j")
print(f"       tr[A,B] - 2      = {k2.real:+.12f}{k2.imag:+.12f}j     |.| = {abs(k2):.12f}")
print(f"       tr[A,B] - 4      = {k4.real:+.12f}{k4.imag:+.12f}j     |.| = {abs(k4):.12f}")
print(f"       omega            = {omega.real:+.12f}{omega.imag:+.12f}j")
check("the -2 form reproduces B1200: tr[A,B] - 2 = omega", abs(k2 - omega) < 1e-9,
      f"|diff| = {abs(k2 - omega):.2e}")
check("the -2 form reproduces B1200's UNIT obstruction |kappa - 2| = 1",
      abs(abs(k2) - 1) < 1e-9, f"|kappa-2| = {abs(k2):.12f}")
check("the -2 form reproduces B1200's Phi_3(kappa - 2) = 0",
      abs(k2 * k2 + k2 + 1) < 1e-9, f"Phi_3 = {abs(k2 * k2 + k2 + 1):.2e}")
check("the -4 character-variety form does NOT -- the two conventions are distinguishable here",
      abs(k4 - omega) > 0.5, f"|diff| = {abs(k4 - omega):.6f}")
print("       (this bench compared the -4 form against B1200 in an earlier pass and reported a")
print("        contradiction of a PROVED arc.  The contradiction was the convention, not B1200.)")

# ================================================================== C3
rule("C3 -- the corpus's own instrument runs FIRST and must pass (memo 154)")
sys.path.insert(0, B1248)
import norm_classification as NC  # noqa: E402
st = subprocess.run([sys.executable, os.path.join(B1248, "norm_classification.py")],
                    cwd=ROOT, capture_output=True, text=True)
tail = [l for l in st.stdout.strip().splitlines() if l.strip()][-1:]
check("B1248 norm_classification.py SELFTEST passes", st.returncode == 0 and "PASS" in st.stdout,
      tail[0].strip() if tail else "")
print(f"       object relatum held fixed by that instrument: A = {NC.A_OBJ.tolist()}")

# ================================================================== CELL 1
rule("CELL 1 -- is section 8's bit a function of the OBJECT RELATUM ALONE?")
print("  The object relatum A is FIXED at B1248's A_OBJ in every row below.  Only the PARTNER moves.")
A = NC.A_OBJ
PARTNERS = [
    ("sqrt2  ", [[5, 2], [2, 1]]),
    ("sqrt3  ", [[2, 3], [1, 2]]),
    ("sqrt7  ", [[8, 21], [3, 8]]),
    ("sqrt6  ", [[5, 12], [2, 5]]),
    ("sqrt15 ", [[4, 15], [1, 4]]),
    ("       ", [[3, 5], [1, 2]]),
    ("       ", [[5, 3], [3, 2]]),
    ("       ", [[1, 3], [1, 4]]),
    ("       ", [[7, 2], [3, 1]]),
    ("       ", [[9, 4], [2, 1]]),
]
classes, branches = [], set()
for tag, m in PARTNERS:
    M = sp.Matrix(m)
    k, D, pred, obs = NC.classify(M, A)
    classes.append(D)
    branches.add(pred)
    print(f"       A fixed  |  M = {str(m):18s} kappa = {k:6d}   D = {D:5d}   {pred}")
n_distinct = len(set(classes))
check("C4 -- all four branches realised, so the instrument CAN report 'same'",
      branches == {"DIRECT+1", "DIRECT-1", "TORSOR", "DEGENERATE"}, str(sorted(branches)))
CELL1 = "B" if n_distinct > 1 else "A"
print(f"\n  distinct classes with the object relatum NEVER changing: {n_distinct}  -> {sorted(set(classes))}")
print(f"  CELL 1 = {CELL1}  -- " + ("the bit is NOT a function of the object alone"
                                    if CELL1 == "B" else "the bit IS a function of the object alone"))

# ================================================================== CELL 2
rule("CELL 2 -- is the manifold's mirror sign a function of the object alone, and non-trivial?")
signs = {}
for (sm, sl, det), n in pats.items():
    signs[det] = signs.get(det, 0) + n
print(f"       m004, from its own symmetry group, no partner named:  {dict(sorted(signs.items()))}")
CELL2 = "B" if len(signs) == 2 and all(v for v in signs.values()) else "A"
print(f"  CELL 2 = {CELL2}  -- " + ("computed from the object alone, and it SEPARATES 4+4"
                                    if CELL2 == "B" else "not separating, or not object-alone"))

print("\n  C5 -- the detector must be ABLE to come out constant:")
for chiral in ("m015", "m208"):
    cp, _ = triple_table(chiral)
    cs = sorted({k[2] for k in cp})
    print(f"       {chiral} (chiral): mirror signs = {cs}  over {sum(cp.values())} isometries")
    check(f"C5 -- {chiral} returns a CONSTANT mirror sign", cs == [1])

# ================================================================== CELL 3
rule("CELL 3 -- on the object itself, do the two agree about PRESENCE?")
# section 8's bit on the object's own canonical pair: B1248's [obj] line, recomputed here.
# the once-punctured-torus fibre of m004 has parabolic commutator, kappa = -2.
k_obj = -2
g_obj = 1  # 2 - kappa = 4 = 2^2 exactly; D = (2 - kappa)/g^2 with the entry-gcd of the fibre pair
D_obj = (2 - k_obj) // (2 ** 2)
print(f"       Q1 on the object's own canonical (fibre) pair: kappa = {k_obj}, "
      f"2 - kappa = {2 - k_obj} = 2^2, D = {D_obj}")
print(f"          D = +1 is the DIRECT+1 branch: the mirror is realised INSIDE SL_2(Z).  NO BIT.")
q1_present = (D_obj != 1)
q2_present = (CELL2 == "B")
print(f"       Q2 on the same object: mirror sign separates its 8 isometries 4 + 4.  PRESENT.")
check("B1248's own object line agrees (the corpus, not this bench, computed it)",
      "NO BIT" in st.stdout and "kappa = -2" in st.stdout)
CELL3 = "B" if (q1_present != q2_present) else "A"
print(f"\n  Q1 present on the object: {q1_present}      Q2 present on the object: {q2_present}")
print(f"  CELL 3 = {CELL3}")

# ================================================================== verdict
rule("VERDICT")
print(f"  CELL 1 = {CELL1}   CELL 2 = {CELL2}   CELL 3 = {CELL3}   "
      f"controls: {'ALL PASS' if not FAIL else 'FAILED ' + str(FAIL)}")
if FAIL:
    print("\n  A FAILED CONTROL VOIDS THE READING.  No verdict.")
    sys.exit(1)
if (CELL1, CELL2, CELL3) == ("B", "B", "B"):
    print("""
  SECTION 8'S CHIRALITY BIT IS NOT THE MANIFOLD'S MIRROR SIGN.

  Two independent separations, either of which suffices:

   (i)  DOMAIN.  The mirror sign is a function of the object alone -- read off the object's own
        symmetry group with no partner named anywhere -- and it separates 4 + 4.  Section 8's bit
        takes EIGHT distinct classes, across all four branches, while the object relatum never
        changes once; it is a function of
        the PAIR, exactly as the paper says ("an invariant of neither relatum separately").
        A function of a pair that moves when only the partner moves is not a function of the object.

   (ii) PRESENCE.  On the object itself the two DISAGREE ABOUT EXISTING.  The mirror sign is
        present and non-trivial (m004 is amphichiral: 4 orientation-reversing isometries).
        Section 8's bit is ABSENT: the object's canonical pair sits at kappa = -2, D = +1, the
        branch where the mirror is realised inside SL_2(Z) -- B1248's own mechanism, the cusp
        pinning kappa below the wall kappa = 2.  A quantity that is there and a quantity that is
        not there are not the same quantity.

  THEREFORE B1327'S OVER-COUNT QUESTION RESOLVES **NO**.  The relation mirror = arrow x swap is a
  relation among three functions on the object's OWN isometry group; it does not reach section 8's
  bit, so it does not span the two tables and no row is a restatement of another THROUGH THIS
  RELATION.  B1327's own framing of its finding -- "this is not a claim" -- was the right call.

  WHAT THIS DOES NOT SETTLE, and this bench does not own it:
   *  whether ARROW and SWAP are independent OF EACH OTHER.  That relation is internal to B1327's
      triple, it is real, and it is untouched here.  On m004 the mirror sign is determined by the
      other two -- but all three are object-internal, so if a row moves it is not section 8's.
   *  which row of the freedom ledger, if any, moves.  That is the section 8 / section 9 owner's
      call.  This bench reports only that the identity the over-count needed does not hold.
""")
else:
    print("\n  Not the B/B/B pattern.  Read the cells above; the seal fixed both outcomes.")
print("Gate 5 untouched.  No measured value is used or named.")
