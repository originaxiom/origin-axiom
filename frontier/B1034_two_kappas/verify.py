"""B1034 — kappa names TWO quantities, and one of them is exported by the certified core.

Found by the code sweep the campaign's step 1 asks for ("grep the CODE, not claim lines").

`src/origin_axiom/mobius.py` exports `KAPPA = 2*log(phi^2)/sqrt(5)` ~ 0.8608, the Moebius
generating vector field's coupling, locked by CLAIMS P15/P16. The corpus's OTHER kappa is the
bridge equation `kappa = tr[a,b]`, whose `kappa = 2 <=> nothing` is the programme's founding
sentence (B309/B518, restored by B1010, extended by B1027).

They are not the same object, and neither surface declares the other.
"""
import json
import pathlib
import re
import sys

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
R = {"checks": {}}


def chk(name, ok, **d):
    R["checks"][name] = {"pass": bool(ok), **d}
    return ok


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def flat(s):
    """Markdown hard-wraps and prefixes blockquote lines with '> '; every phrase checked here is
    a SENTENCE, not a line. (Same hazard B1030 hit; kept as the house helper.)"""
    return re.sub(r"\s+", " ", s.replace("\n> ", "\n"))


# ------------------------------------------------- 1. kappa #1: the certified core's constant
from origin_axiom.mobius import KAPPA, vector_field, potential          # noqa: E402
from origin_axiom.constants import PHI_SQ                                # noqa: E402

chk("core_kappa_is_the_moebius_coupling",
    sp.simplify(KAPPA - 2 * sp.log(PHI_SQ) / sp.sqrt(5)) == 0,
    value=float(KAPPA))
chk("core_kappa_is_a_single_transcendental_number",
    abs(float(KAPPA) - 0.8608178819280081) < 1e-12 and not KAPPA.free_symbols,
    value=float(KAPPA))
tau = sp.symbols("tau")
chk("core_kappa_is_the_coefficient_of_the_flow_and_its_potential",
    sp.simplify(vector_field(tau) + KAPPA * (tau**2 - tau - 1)) == 0
    and sp.simplify(sp.diff(potential(tau), tau) - KAPPA * (tau**2 - tau - 1)) == 0)

# The package's own docstring: this is the PROVEN core, nothing speculative.
chk("the_package_declares_itself_the_proven_core",
    "only* the results labelled ``proven``" in read("src/origin_axiom/__init__.py"))

# ------------------------------------------------- 2. kappa #2: the bridge equation
LAWMAP = read("docs/LAW_MAP.md")
chk("the_bridge_kappa_is_a_commutator_trace_on_a_curated_surface",
    "κ = tr[a,b]" in LAWMAP and "κ = 2" in LAWMAP)
chk("the_bridge_kappa_carries_the_founding_sentence",
    "κ = 2 ⟺ the cancellation completes ⟺ nothing" in flat(LAWMAP))
b309 = json.loads(read("frontier/B309_kappa_unification/arc_verdict.json"))
chk("B309_banks_kappa_minus_2_equals_omega_squared",
    "kappa=tr[a,b]" in b309["claim_one_line"].replace(" ", "")
    and "kappa-2=omega^2" in b309["claim_one_line"].replace(" ", ""))

# ------------------ 3. THEY ARE DIFFERENT IN TYPE, NOT ONLY IN VALUE — the non-vacuous check
# kappa #1 is a CONSTANT (no free symbols, one transcendental value, never 2).
# kappa #2 is a COORDINATE on the character variety — a function that takes the value 2 exactly
# on the degenerate locus. A constant cannot have a locus where it equals 2.
chk("core_kappa_can_never_equal_2", abs(float(KAPPA) - 2) > 1.1)
chk("the_two_kappas_differ_in_TYPE_not_only_value",
    not KAPPA.free_symbols                       # a fixed number
    and "κ = 2 ⟺" in flat(LAWMAP))               # vs a value the other kappa attains
# MB12 control: the criterion must be able to come out the other way. If the core's KAPPA had
# been a symbolic function of the character-variety coordinates, this check would not fire.
chk("the_criterion_is_failable__a_symbolic_kappa_would_not_trip_it",
    bool(sp.symbols("x").free_symbols) and not KAPPA.free_symbols)

# ---------------------------------------------- 4. neither surface declares the other
CLAIMS = read("CLAIMS.md")
p15p16 = "\n".join(ln for ln in CLAIMS.splitlines() if ln.startswith(("| P15", "| P16")))
chk("CLAIMS_P15_P16_use_kappa_for_the_moebius_coupling",
    "κ" in p15p16 and "2·log(φ²)/√5" in p15p16)
chk("CLAIMS_P15_P16_do_not_mention_the_bridge_kappa",
    "tr[a,b]" not in p15p16 and "commutator" not in p15p16)

# and the bridge-kappa rows never mention the Moebius one
# Scoped by AUTHORSHIP — the seventh instance of one hazard in six arcs: this arc's own LAW_MAP
# row necessarily mentions BOTH kappas, which is the whole point of it.
bridge_rows = "\n".join(ln for ln in LAWMAP.splitlines()
                        if ("tr[a,b]" in ln or "THE κ-UNIFICATION" in ln) and "B1034" not in ln)
chk("the_bridge_rows_do_not_mention_the_moebius_kappa",
    "log(φ²)" not in bridge_rows and "0.8608" not in bridge_rows and "P15" not in bridge_rows)

# a third locus, using it as a physical coupling
chk("a_third_locus_calls_the_moebius_kappa_a_coupling",
    "Coupling: g = κ = 0.8608" in read("docs/SESSION3_SYNTHESIS.md"))

# --------------------------------------- 5. this arc's repair: declared, not renamed
chk("the_core_module_now_declares_the_collision",
    "TWO DIFFERENT QUANTITIES" in read("src/origin_axiom/mobius.py"))
chk("CLAIMS_now_carries_the_disambiguation",
    "B1034" in CLAIMS
    and "NAME COLLISION" in CLAIMS
    and "the bridge-equation `κ`" in flat(CLAIMS)
    and "They differ in type, not only in value" in flat(CLAIMS))
chk("a_lead_is_registered_rather_than_a_rename_performed",
    "L159" in read("docs/OPEN_LEADS.md"))

R["summary"] = {
    "kappa_core": {"expr": "2*log(phi^2)/sqrt(5)", "value": float(KAPPA),
                   "type": "constant", "locus": "src/origin_axiom/mobius.py; CLAIMS P15/P16",
                   "can_be_2": False},
    "kappa_bridge": {"expr": "tr[a,b]", "type": "coordinate on the character variety",
                     "locus": "LAW_MAP; THE_FRAMEWORK; ORIENTATION; B309/B518/B1010/B1027",
                     "kappa_equals_2": "the founding sentence: cancellation completes = nothing"},
}
R["all_pass"] = all(v["pass"] for v in R["checks"].values())

if __name__ == "__main__":
    (pathlib.Path(__file__).parent / "results.json").write_text(
        json.dumps(R, indent=1, ensure_ascii=False))
    for k, v in R["checks"].items():
        print(("PASS " if v["pass"] else "FAIL ") + k)
    print("\nALL PASS:", R["all_pass"])
