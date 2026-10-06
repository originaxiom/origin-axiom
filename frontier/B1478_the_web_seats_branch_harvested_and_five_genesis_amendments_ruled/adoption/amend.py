#!/usr/bin/env python3
"""B1478 -- GENESIS v1.11 (main's, B1476) -> GENESIS v1.12 (main's): the web seat's five proposed amendments of 2026-10-06,
each verified on main and ruled; B1477's location of the bit recorded.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.12 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_11_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_11 = "68fadf5b9ef1587a4f9f1dbdbdb22024826928ccb644c03d73e4bfc1729ad964"

CHANGES = [
 ("**Version 1.11 · 2026-10-04 · canonical.**", "**Version 1.12 · 2026-10-06 · canonical.**"),
 # A2 -- moduli, not values
 ("So the flat frame reaches DISCRETE data (counts, bits, signs) through the boundary and cannot reach CONTINUOUS\n"
  "  values (a mass, a coupling): the record's value-negatives are theorems about flat moduli and bound the frame, not\n"
  "  physics (lead L247; the census of 173 value-kills, 107 on flat premises).",
  "So the flat frame reaches DISCRETE data (counts, bits, signs) through the boundary and cannot reach CONTINUOUS\n"
  "  MODULI (a mass, a coupling that the construction leaves free): the record's value-negatives are theorems about flat\n"
  "  moduli and bound the frame, not physics (lead L247; the census of 173 value-kills, 107 on flat premises). **[v1.12]**\n"
  "  The v1.11 wording said \"continuous values\" and over-reached the other way (the web seat's A2): a rigid flat point is\n"
  "  not a modulus and fixes continuous numbers exactly — on m004 the volume (3√3/2)·L(2,χ₋₃) and the Kashaev\n"
  "  expansion (B598, B722; the dilogarithm atom verified in B1476). Those are numbers of a member, fixed; none is a\n"
  "  Standard-Model parameter, and the count of §7 does not move."),
 # A1 -- the parity rule; B1477's location
 ("  What remains of the gap: the continuous values; and the step from the boundary's η to a physical count (B279's\n"
  "  unbanked link, L246 Phase 2).",
  "  What remains of the gap: the continuous moduli; and the step from the boundary's η to a physical count (B279's\n"
  "  unbanked link, L246 Phase 2). **[v1.12] \"A frame with curvature\" is necessary, not sufficient (the web seat's A1,\n"
  "  derived):** on a smooth closed bulk of dimension n the Dirac index ∫Â·ch(V) takes ch_k only with n − 2k ≡ 0 (mod 4),\n"
  "  and ch_k(V̄) = (−1)^k ch_k(V); so ind(V) ≠ ind(V̄) is possible only for n ≡ 2 (mod 4). A four-dimensional bulk, curved\n"
  "  or not, cannot tell 27 from 27̄; a six-dimensional one can. No frame of the right parity is on the record (§8).\n"
  "  **[v1.12] Where the bit is decided (B1477):** a mirror that acts on an invariant cusp torus by a rhombic involution\n"
  "  fixes no spin structure whose longitude has trace −2 (Theorem A, proved); every one-cusped amphichiral census\n"
  "  manifold at Chern–Simons class ¼ is of that kind (75 of 75). The bit is a parity of the boundary torus' lattice."),
 # A3 -- one referent for "the family"
 ("**[v1.2]** A count over states names its unit, word states or manifolds: a word and its reverse are two states and one manifold\n"
  "(§3).",
  "**[v1.2]** A count over states names its unit, word states or manifolds: a word and its reverse are two states and one manifold\n"
  "(§3). **[v1.12] \"The family\" names its set (the web seat's A3, adopted as a naming rule).** At least five sets have been\n"
  "called \"the family\" on the record and in the seats' reports: the word states X_gen (§3); m004's commensurability class;\n"
  "B1186's 112; the regular-tetrahedral class; the amphichiral members of B1474–B1477. A statement true on one is false on\n"
  "another — measured: on X_gen's primitive word states to length 8 (74 hyperbolic realisations) the Chern–Simons class is\n"
  "rational on 18 and irrational on 56, and 16 are amphichiral with class 0 or ¼ (reproduced on main, B1478), whereas the\n"
  "1/24 lattice of B1476 is a fact of B1186's 112. From v1.12 a scope tag's `object` names the set, and the bare phrase is\n"
  "not used in a verdict line. Which set the owner's rule of 2026-10-04 means is fork FK13 (§8); main does not rule on it."),
 # FK13 and the frontier items (A1, A4, A5)
 ("\n\n**Computed nowhere yet** (the frontier, not a list of failures):",
  "\n| FK13 **[v1.12]** | Which set \"the family as object\" names (the owner's rule of 2026-10-04) | OPEN — the owner's | the owner's word: X_gen (§3's word states, the web seat's reading), m004's commensurability class, or B1186's 112 (the set main's B1474–B1477 computed on). Until then every statement names its set (§6) |\n"
  "\n**Computed nowhere yet** (the frontier, not a list of failures):"),
 ("- **[v1.6]** the fixed loci of the metallic trace maps component by component (B130's question with isolated components\n"
  "  allowed; the audit lane's AR4).",
  "- **[v1.6]** the fixed loci of the metallic trace maps component by component (B130's question with isolated components\n"
  "  allowed; the audit lane's AR4);\n"
  "- **[v1.12]** a frame of the right parity for GAP6 (§7): a bulk of dimension ≡ 2 (mod 4) with a bundle that is not flat.\n"
  "  One candidate is named and unbuilt — the six-dimensional frame bundle Γ\\PSL(2,ℂ) of a closed filling (the web seat's A1);\n"
  "- **[v1.12]** F-MC's two extra abelian factors, on any state other than the root. They are two objects and are named\n"
  "  apart (the web seat's A4, verified on main's record): **U1-η**, left by the flat closing Y₃ — the η direction of the\n"
  "  rank-five E₆ breaking, family-universal, both E₆-charged singlets of the 27 carrying the same charge so that no field\n"
  "  of the 27 or the 78 gives ν^c a Majorana mass (the paper); and **U1-Z′₉**, left by the ninth closing's tree-level\n"
  "  vacuum — (5ψ − 3χ)/2 with a family part (−10, 5, 5), family-non-universal, the VEV'd generation's singlets neutral\n"
  "  (sm:B1283, B1303). Charges 4, −2, 10, −8, −2, 10 on one 27 with Σq = Σq³ = 0 (recomputed, B1478) — a check that\n"
  "  cannot fail on full 27s (B1340). What can fail is the cube of the family part, and it does: Σf³ = −750 for (−10, 5, 5).\n"
  "  **On a chiral spectrum U1-Z′₉ is not gaugeable as it stands** (B1340; FALSIFIER P9: the programme cannot hold both the\n"
  "  observed chirality and this Z′ — the web seat's A4 did not carry this, main's ruling adds it). Neither factor has a\n"
  "  mass, a coupling or a range on the record — B1303 gives a regime and a fork, not a value — and neither is a statement\n"
  "  about any state but the root;\n"
  "- **[v1.12]** dark-matter stability on any state other than the root (the cloud seat's memo 122 is NEGATIVE for the\n"
  "  root's forced gauge 2-torsion only; the web seat's A5);\n"
  "- **[v1.12]** Dirac against Majorana: decided by the discrete symmetry left when the extra abelian factor is broken,\n"
  "  which no arc computes (A5)."),
 # version log
 ("    A5 (SE2's torsion-free tie-break) selects a member; the page's object is the family (B1418), and this page's statements\n"
  "    about m004 are statements about one member unless they say otherwise.",
  "    A5 (SE2's torsion-free tie-break) selects a member; the page's object is the family (B1418), and this page's statements\n"
  "    about m004 are statements about one member unless they say otherwise.\n"
  "- **v1.12 · 2026-10-06 · main B1478.** The web seat's five proposed amendments, each verified on main and ruled; one fork.\n"
  "  - A1 ADOPTED: a curved bulk tells 27 from 27̄ only in dimension ≡ 2 (mod 4) (GAP6); the six-dimensional frame bundle\n"
  "    entered as an unbuilt candidate, not a claim.\n"
  "  - A2 ADOPTED: GAP6's \"continuous values\" becomes \"continuous moduli\"; rigid flat invariants are fixed numbers of a member.\n"
  "  - A3 ADOPTED as a naming rule (§6): \"the family\" names its set. Its last clause — that the owner's rule means X_gen —\n"
  "    is NOT ruled by main: fork FK13, the owner's.\n"
  "  - A4 ADOPTED: the two extra abelian factors named apart, U1-η (Y₃) and U1-Z′₉ (the ninth closing), both root-only.\n"
  "  - A5 ADOPTED: dark-matter stability and Dirac-against-Majorana listed as computed on the root only / nowhere.\n"
  "  - B1477 recorded in GAP6: the bit is decided at the cusp (Theorem A; the ¼ class is the rhombic class on the census).\n"
  "  - The web seat has its own branch from this date (`chat1/web-seat`); its relays are rowed and its pin set in B1478."),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_11, "the received v1.11 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.12 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.12, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
