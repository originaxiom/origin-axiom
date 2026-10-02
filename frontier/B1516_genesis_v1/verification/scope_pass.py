"""B1516 -- the scope tag made data: write a `scope` field into this seat's kill-graph entries (B1369 on).

python3 scope_pass.py            -> report what would change
python3 scope_pass.py --write    -> write frontier/B738_pathfinder_compiler/kill_graph.json (idempotent)

Each scope follows GENESIS.md v1.0 section 6: frame (F-FC, F-CI, F-HE, F-AP or "none"), object, reach ("single",
"class" or "general") and hypotheses. A `note` is added where an entry's own wording reached further than its
computation; the entry's text is left as written. Nothing here changes a verdict.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
KG = ROOT / "frontier" / "B738_pathfinder_compiler" / "kill_graph.json"

FC_CLASS = "B1186's 112-member family (shape field in Q(sqrt-3); its 99 arithmetic members are m004's class's census part)"

SCOPES = {
    "B1369": dict(frame="F-FC", object=FC_CLASS, reach="class",
                  hypotheses=["bulk matter with the Standard Model unbroken (B1368's sectors)",
                              "B1351 (ii)'s whole-torus and annular conventions, with R23's scoping",
                              "four cusps left open (B1370)"],
                  note="The free-cusp theorem itself is general in F-FC; the census closes 108 of the 112."),
    "B1372": dict(frame="F-FC", object="any free cusp of any member: the doublet reading of a generation (10 from the "
                  "78's SL(2)_beta doublets, 5bar from the 27's)", reach="general",
                  hypotheses=["a non-unitary peripheral eigenvalue (Theorem B)",
                              "the unitary order-4 residual is B1373's"]),
    "B1373": dict(frame="F-FC", object="the 35 members of B1186's family with a free cusp", reach="class",
                  hypotheses=["the real cone-manifold path of the hyperbolic structure only (fillings (2p, 0) or (0, 2p))",
                              "34 of the 166 pairs degenerate before the point"]),
    "B1385": dict(frame="F-FC", object="all orientable word states (joins checked to length 8), and the pilot's "
                  "Eisenstein cusps in m004's class", reach="general",
                  hypotheses=["the free-cusp frame's requirement of a free cusp",
                              "the pilot's cusps are class-wide; B1386 found an open member, cube~3.24"],
                  note="'The word states never can' holds in F-FC only. In F-CI, 95 of the 758 word states to length 12 "
                  "carry a generation-shaped background at their own level (main B1439)."),
    "B1388": dict(frame="F-FC", object="cube~3.24, a degree-9 cover of o10_150725 in m004's class", reach="single",
                  hypotheses=["the relative index at a cusp cut, as sealed",
                              "the mathematics stands; the physical reading is what was retired"]),
    "B1389": dict(frame="F-FC", object="any member with a cuspidal Higgs class (computed on cube~3.24)",
                  reach="general",
                  hypotheses=["7d E6 super-Yang-Mills with the 78's broken roots in the frame",
                              "the frame's rule sign(<H, mu>) N"]),
    "B1390": dict(frame="F-FC", object="the arithmetic members of m004's commensurability class (isometries in "
                  "PGL(2, Q(sqrt-3)))", reach="class",
                  hypotheses=["arithmeticity (Skolem-Noether); the non-arithmetic o10_143602 of B1186's family has "
                              "closed order-3 curves"]),
    "B1391": dict(frame="F-FC", object="cube~3.24 (isometry group D3)", reach="single",
                  hypotheses=["the symmetric point of D3", "tree-level textures covariant under D3"],
                  note="A statement about cube~3.24's isometry group; members with other isometry groups are not read."),
    "B1392": dict(frame="F-FC", object="any member and any Higgs class (the deformed problem on the complete manifold)",
                  reach="general", hypotheses=["the frame's deformed operator; a class alive on a cusp seals it"]),
    "B1393": dict(frame="F-FC", object="the rank-one Higgs twist on any member (cube~3.24's cuspidal twist computed)",
                  reach="general",
                  hypotheses=["rank-one twist only: a non-semisimple V against V* evades it (R27; main B1418; sm:B1374)",
                              "off isolated couplings"]),
    "B1394": dict(frame="F-FC", object="acyclic invariant order-3 characters on the arithmetic census of m004's class "
                  "and cube~3.24", reach="class",
                  hypotheses=["sources symmetric under an order-3 rotation",
                              "acyclic characters (54 non-acyclic pairs are unbalanced: P3)"]),
    "B1395": dict(frame="F-FC", object="any free cusp", reach="general",
                  hypotheses=["finite-energy, normalizable data in 7d super-Yang-Mills"]),
    "B1396": dict(frame="F-FC", object="rotated Eisenstein cusps of members of m004's class (213 pairs, 444 rows)",
                  reach="class", hypotheses=["a Z/3-symmetric flux cap", "an acyclic bulk character"]),
    "B1397": dict(frame="F-FC", object="any capped cusp torus", reach="general",
                  hypotheses=["a U(1) flux cap of degree n", "E6, E7 and E8 frames",
                              "bulk-flux caps sum to zero in total (B1397 section 7)"]),
    "B1398": dict(frame="F-FC", object="m004's commensurability class: the frame's verdict on three", reach="general",
                  hypotheses=["the record's menu of completions", "an abelian Higgs field Y w1 + gamma w2 of any rank",
                              "78 matter: with 27 matter one family survives, tested by B1399"]),
    "B1399": dict(frame="F-FC", object="degree-2 and degree-3 covers of the 99 arithmetic members with cuspidal "
                  "dimension at least 2 (109 up to isometry)", reach="class",
                  hypotheses=["27 matter with a rank-two abelian Higgs field", "7 members unresolved"]),
    "B1500": dict(frame="F-AP", object="any member's free cusps completed as cone points (ten members computed)",
                  reach="general", hypotheses=["the one-point completion", "Cheeger's ideal boundary conditions"]),
    "B1501": dict(frame="F-AP", object="G2 cones over the four homogeneous nearly Kaehler 6-manifolds modulo their "
                  "listed finite automorphisms (694 classes of order at most 12)", reach="class",
                  hypotheses=["the listed automorphisms", "order at most 12"]),
    "B1502": dict(frame="F-AP", object="B1501's torus-linked quotients", reach="class",
                  hypotheses=["B1501's census"]),
    "B1503": dict(frame="F-AP", object="G2 cone points over finite quotients of compact nearly Kaehler links",
                  reach="general", hypotheses=["global quotients of smooth links; orbifold links are B1505's"]),
    "B1504": dict(frame="F-AP", object="B1500's cusp-point choice: the order bit and symmetry (every member), and the "
                  "root's own data (m004)", reach="general",
                  hypotheses=["B1500's one-point completion",
                              "T1 and T3 hold for every member; T2 reads m004's isometries only"],
                  note="'What the architecture itself fixes' was computed from m004's own data (T2) and from symmetry; "
                  "other states' own data are not read, and completions supplied by physics are outside it."),
    "B1505": dict(frame="F-AP", object="known G2 cones over orbifold links that are not global quotients (AW sections 2 "
                  "and 3, and isometric quotients)", reach="class", hypotheses=["the known families only"]),
    "B1506": dict(frame="F-CI", object="m004's cyclic levels (s961 and M6): B1378's deck triplet", reach="single",
                  hypotheses=["one background's count (Shapiro, pullback)",
                              "the deck gauged; keeping it is the open bit (sL-5, GENESIS FK7)"],
                  note="About the root's levels; other states' levels (main B1434: ten of twelve three-fold levels carry "
                  "orbits of three) are not read."),
    "B1509": dict(frame="F-HE", object="m004's convex-projective family (the audit lane's harmonic vacuum A + 1, "
                  "A = mu rho_q)", reach="single",
                  hypotheses=["determinant-one rank-five extensions of a character", "q != 1 (T1)",
                              "the end condition decides the 10' count"]),
    "B1510": dict(frame="F-HE", object="m004's harmonic vacuum A + 1 with both singlet directions", reach="single",
                  hypotheses=["deformations over F[[eps]] with no invariant vector or covector"]),
    "B1511": dict(frame="F-HE", object="m004's cyclic levels M_n with the projective vacuum, any character twist",
                  reach="single",
                  hypotheses=["q != 1: at q = 1 the Lambda^2 sector meets the cusp, and B1515 finds non-zero 5bar' "
                              "counts there"],
                  note="'On every level' holds for q != 1 only."),
    "B1513": dict(frame="F-HE", object="B1511's projective triplet on s961 and B1509's join on m004", reach="single",
                  hypotheses=["tree-level relative triple products", "each member's own Higgs classes"]),
    "B1514": dict(frame="F-HE", object="B1511's case-(b) orbits on M4, M5 and M6 (184 members)", reach="single",
                  hypotheses=["through level 6", "tree level"]),
    "B1515": dict(frame="F-HE", object="m004's harmonic family at q = 1 (the complete hyperbolic structure), levels 1 "
                  "to 6", reach="single", hypotheses=["through level 6", "the sealed rule for I(W) and I(Lambda^2 W)"]),
}

FRAMES = {"F-FC", "F-CI", "F-HE", "F-AP", "none"}
REACH = {"single", "class", "general"}


def main():
    kg = json.loads(KG.read_text(encoding="utf-8"))
    ids = [e["id"] for e in kg]
    missing = sorted(set(SCOPES) - set(ids))
    assert not missing, missing
    changed = 0
    for e in kg:
        s = SCOPES.get(e["id"])
        if s is None:
            continue
        assert s["frame"] in FRAMES and s["reach"] in REACH and s["object"] and s["hypotheses"]
        if e.get("scope") != s:
            e["scope"] = s
            changed += 1
    print(f"{len(SCOPES)} scopes; {changed} entries to change")
    if "--write" in sys.argv and changed:
        KG.write_text(json.dumps(kg, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        print("written")


if __name__ == "__main__":
    main()
