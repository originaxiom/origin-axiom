"""B1028 -- the global freedom ledger (Lane I-1, sealed e13d09a5 before compute).

The retroactive look-elsewhere audit over the WHOLE chain: A1-A7 -> the object -> kappa ->
Q(sqrt-3) -> 2T -> E6 -> the cascade -> the SM skeleton. Method as sealed: (1) every arrow
listed; (2) per link, every choice (rule, face, convention, selection) priced -- banked-forced
links price 0 WITH THE FORCING ARC CITED AND ITS DISCRIMINATING PHRASE MACHINE-CHECKED against
the arc's own banked verdict (compute-the-discriminating-fact, applied to a desk audit);
(3) outputs against ambient classes DECLARED IN THE ROW before counting; (4) bits-in vs
bits-out, links first, aggregate last.

CONSERVATIVE COUNTING RULES (declared before any number below):
  C-A  STRUCTURAL-grade outputs are EXCLUDED from bits-out (they are debts, not credits).
  C-B  Continuum pins (a continuous ambient pinned to a point) are NOTED, never counted.
  C-C  Pattern-combinatorics (e.g. the 11-of-286 Yukawa support) are EXCLUDED -- counting
       them would inflate the margin with rep-theory that is forced once the carrier is fixed.
  C-D  Ambient classes use FLOORS when the banked enumeration gives a lower bound only.
  C-E  Declared INPUTS (the hypothesis list) are a separate table -- they are the theorem's
       hypotheses, not retroactive freedom; retroactive freedom = choices made in BUILDING
       the chain whose alternatives would change the conclusion.
"""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def _claim(arc_dir: str) -> str:
    v = json.loads((ROOT / "frontier" / arc_dir / "arc_verdict.json").read_text("utf-8"))
    assert v["verdict"] == "PROVED", f"{arc_dir}: cited verdict not affirmative"
    return v["claim_one_line"]


def _cite(arc_dir: str, *phrases: str) -> str:
    """A cite is only usable if the banked claim line carries its discriminating phrase."""
    c = _claim(arc_dir)
    for p in phrases:
        assert p in c, f"{arc_dir}: discriminating phrase not found: {p!r}"
    return arc_dir.split("_")[0]


# ---------------------------------------------------------------- the links (bits-in)
def links():
    L = []

    L.append(dict(link="A1-A6 -> the object (up to orientation)", price=0.0,
        cite=_cite("B14_half_step_square_root_selector", "unique GL(2,Z) square root of A up to sign"),
        note="uniqueness chain; the leftover sign IS A7 = 1 input bit (hypothesis table)"))

    L.append(dict(link="object selection within its own family", price=0.0,
        cite=_cite("B997_golden_conductor_uniqueness", "UNIQUE METALLIC GRAMMAR", "INFINITE FAMILY"),
        note="scanned exhaustively as a control over the INFINITE metallic family; unique hit; "
             "the family is the object's own deformation axis (banked since the m-axis arcs), "
             "not a curated class -- FLAG: the family declaration is the residual soft spot, "
             "priced 0 because no live alternative family was ever on the table"))

    L.append(dict(link="object -> kappa -> Q(sqrt-3)", price=0.0,
        cite=_cite("B1010_consolidation_loss", "MATTER FACE"),
        note="kappa = tr[a,b] canonical (Fricke/reducibility discriminant); field by evaluation; "
             "the restored matter law's row (B1010) carries the lineage"))

    L.append(dict(link="Q(sqrt-3) -> 2T (the door)", price=0.0,
        cite=_cite("B266_arithmetic_selects_e6", "canonically selects E6"),
        note="the ramified prime selects; and the door is the grammar's OWN conductor -- "
             "no criterion was chosen: siblings have no door at all"))

    L.append(dict(link="door uniqueness across grammars (no criterion freedom)", price=0.0,
        cite=_cite("B1019_l149_silver_cascade", "THE SIBLINGS HAVE NO DOOR"),
        note="silver/bronze diverge AT THE ENTRY MAP; only the golden's own door opens onto ADE"))

    L.append(dict(link="2T -> E6 (McKay)", price=0.0,
        cite=_cite("B266_arithmetic_selects_e6", "McKay E6"),
        note="one ADE classification; a bijection consumes no freedom"))

    L.append(dict(link="carrier = the 27", price=0.0,
        cite=_cite("B884_yukawa_support", "nullspace dim exactly 1", "inherited not chosen"),
        note="CONDITIONAL ON THE CHIRALITY INPUT (declared, hypothesis table): Sym^2(27) has no "
             "invariant, Sym^3 exactly one, adjoint is real/vector-like -- the chirality bit "
             "forces the complex minuscule; 27 vs 27-bar identified by the object's own "
             "theta-symmetry; frame conventions inherited not chosen"))

    L.append(dict(link="the cascade rule", price=0.0,
        cite=_cite("B994_rule_variation", "ALL SIX END AT THE STANDARD MODEL",
                   "DOES NOT DO THE LANDING"),
        note="NAMED RISK 2 IN THE SEAL, RESOLVED BY THE BANKED RECORD: the assumed half "
             "('maximal residual symmetry') does not do the landing; registerability (the "
             "DERIVED half) does; every registerable selection function was enumerated (six) "
             "and all land at the SM. PATH freedom log2(6) = 2.585 bits exists and affects "
             "no output. Menu import (P5) flagged on the termination row"))

    L.append(dict(link="cascade termination", price=0.0,
        cite=_cite("B863_termination", "TERMINAL registerable algebra", "Menu import (P5)"),
        note="theorem; FLAG: the branching menu (P5) is a mathematical import (Lie branching "
             "data), stated not hidden -- an import, not a choice among live alternatives"))

    L.append(dict(link="generation reading", price=0.0,
        cite=_cite("B897_27_under_g20", "BEFORE compute", "three 9-blocks"),
        note="NAMED RISK 1 IN THE SEAL, RESOLVED: the cell was SEALED BEFORE COMPUTE "
             "(prereg e293f095) with the criterion verbatim -- retroactive freedom is 0 BY "
             "CONSTRUCTION; the grade debt is handled on the output side (rule C-A: its "
             "output is EXCLUDED from bits-out until Lane II upgrades it)"))

    L.append(dict(link="faces", price=0.0, cite="--",
        note="no face choice enters the STRUCTURAL chain; face choices exist only in the "
             "value-layer crossing lane, whose spent bits live in ITS ledger (2 bits + rows, "
             "a separate book, already maintained)"))

    return L


# ---------------------------------------------------------------- the inputs (hypotheses)
def inputs():
    _cite("B14_half_step_square_root_selector", "up to sign")
    return [
        dict(inp="A1-A6 (the axioms)", bits=None,
             note="motivated-not-laws (Layer 0's honest boundary); prices audited in B1003 "
                  "(five robust, two fragile); the hypothesis of the theorem"),
        dict(inp="A7 orientation", bits=1.0, note="the square root's sign (B14)"),
        dict(inp="time's arrow", bits=1.0, note="F2 bit"),
        dict(inp="chirality / conjugation (tau)", bits=1.0,
             note="F2 bit; does real work at the carrier link"),
        dict(inp="one unit (ell)", bits=None, note="dimensionful; not a bit"),
        dict(inp="acceptance: the 6d type J", bits=None,
             note="narrowed to accept-the-nomination (B1025); closer = S1"),
        dict(inp="acceptance: the VEV direction", bits=None,
             note="retyped by B1025 to a discrete act on canonical multiplicity-one lines + "
                  "weight-1 magnitudes; the one-trit retype (log2 3 = 1.585 bits, orbit order "
                  "3) is RELAYED AND NOT YET VERIFIED BY THIS SEAT -- recorded as pending, "
                  "not adopted"),
    ]


# ---------------------------------------------------------------- the outputs (bits-out)
def outputs():
    O = []
    O.append(dict(out="global form [SU(3)xSU(2)xU(1)]/Z6", bits=2.0,
        ambient="DECLARED: the four global forms the SM admits, Gamma in {1,Z2,Z3,Z6} (Tong)",
        cite=_cite("B862_global_form", "FORCES Z6", "{1,Z2,Z3,Z6}")))

    O.append(dict(out="the endpoint algebra su(3)+su(2)+u(1)^3", bits=math.log2(3),
        ambient="DECLARED (floor, rule C-D): distinct a-priori terminal algebras of the "
                "unrestricted menu tree; the banked enumeration names >= 3 (the SM; "
                "SU(4)xU(1); the Sp(8) branch) -- termination depth folded in, not "
                "double-counted",
        cite=_cite("B994_rule_variation", "Registerable options per step are [3, 2, 1]")
             + "+" + _cite("B892_second_measurement", "su(3)+su(2)+u(1)^3 EXACTLY")))

    O.append(dict(out="matter mass in the cubic; the doublet in the 10", bits=1.0,
        ambient="DECLARED (coarse, rule C-C): mass-from-cubic vs bare-quadratic -- the "
                "quadratic invariant does not exist and the SM has no bare masses; counted "
                "as ONE coarse bit; the 11-cell SM-refined support pattern EXCLUDED (C-C)",
        cite=_cite("B884_yukawa_support", "nullspace dim exactly 1")))

    O.append(dict(out="hypercharge direction (b = c = 0)", bits=0.0,
        ambient="CONTINUUM PIN (rule C-B, noted not counted): the solution cone of the "
                "anomaly system is EXACTLY ONE LINE in the 3-parameter dial space; the "
                "normalisation is convention by the homogeneity theorem (empty class)",
        cite=_cite("B864_anomaly_ledger", "forcing b = c = 0", "UNIQUE GAUGEABLE ABELIAN DIRECTION")
             + "+" + _cite("B991_X11_normalisation", "HOMOGENEOUS", "CONE")))

    O.append(dict(out="generation structure (three 9-blocks)", bits=0.0,
        ambient="EXCLUDED (rule C-A): STRUCTURAL grade -- a debt, not a credit, until the "
                "Lane II upgrade",
        cite=_cite("B897_27_under_g20", "three 9-blocks")))

    O.append(dict(out="CS = 0; no dimensionful quantity", bits=0.0,
        ambient="controls about the object, not SM-facing bits; not counted",
        cite=_cite("B303_clock_is_the_cp_sign", "CS=0 amphichiral")))

    return O


# ---------------------------------------------------------------- the verdict
def verdict():
    L, I, O = links(), inputs(), outputs()
    bits_in = sum(r["price"] for r in L)
    bits_out = sum(r["bits"] for r in O)
    declared_input_bits = sum(r["bits"] for r in I if r["bits"])
    assert bits_in == 0.0
    assert abs(bits_out - (2.0 + math.log2(3) + 1.0)) < 1e-12
    return dict(
        retroactive_bits_in=bits_in,
        conservative_bits_out=bits_out,
        declared_input_bits=declared_input_bits,
        uncounted=["hypercharge continuum pin (C-B)",
                   "generation triple, STRUCTURAL (C-A)",
                   "Yukawa 11-cell pattern (C-C)",
                   "path freedom log2(6): affects no output"],
        named_risks="BOTH RESOLVED BY THE BANKED RECORD: (1) the rule's assumed half does "
                    "not do the landing (B994); (2) the generation cell was sealed before "
                    "compute (B897) -- retroactive freedom 0 by construction",
        outcome="COMPRESSION",
        margin=f"{bits_out:.3f} conservative output bits (a deliberate FLOOR under rules "
               f"C-A..C-D) against 0.000 retroactive designer bits; the declared inputs "
               f"({declared_input_bits:.0f} discrete bits + one unit + two acceptances) are "
               f"the hypothesis, published, and separate",
    )


if __name__ == "__main__":
    print("LINKS (retroactive freedom, priced against the banked record):")
    for r in links():
        print(f"  [{r['price']:.3f} bits] {r['link']}  <- {r['cite']}")
        print(f"          {r['note']}")
    print("\nINPUTS (the hypothesis list -- declared, separate; NOT retroactive freedom):")
    for r in inputs():
        b = "--" if r["bits"] is None else f"{r['bits']:.3f} bits"
        print(f"  [{b}] {r['inp']}: {r['note']}")
    print("\nOUTPUTS (each against its DECLARED ambient class; conservative rules C-A..C-D):")
    for r in outputs():
        print(f"  [{r['bits']:.3f} bits] {r['out']}  <- {r['cite']}")
        print(f"          {r['ambient']}")
    print()
    v = verdict()
    for k, val in v.items():
        print(f"{k}: {val}")
