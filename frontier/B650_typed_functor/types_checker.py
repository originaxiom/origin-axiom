"""The mechanical typing checker (TYPES.md v1, frozen 306d6cde).

Instances are DESCRIPTORS (construction facts only, no conclusions);
the checker applies R1-R6 verbatim. The held-out battery: B593, B626,
B632/B637 typed here AFTER the freeze.
"""

def type_of(desc):
    """desc: dict with construction facts:
    eig_multiset_fn, contraction_against (None | 'listener' | 'partner-object' | 'stage-section'),
    scalar_arith (tr/det/disc/membership of single element), word (str|None),
    core_coupled (bool), dimensionless (bool),
    x_independence_theorem (bool)."""
    matches = []
    if desc.get("eig_multiset_fn") and not desc.get("contraction_against"):
        matches.append("T_spec")
    if desc.get("scalar_arith") and not desc.get("contraction_against"):
        matches.append("T_field")
    if desc.get("contraction_against"):
        t = "T_coup^inv" if desc.get("x_independence_theorem") else \
            f"T_coup({desc['contraction_against']})"
        matches.append(t)
    if len(matches) != 1:
        return ("ILL-TYPED (R6)", matches)
    base = matches[0]
    flags = ("W(%s)" % desc["word"] if desc.get("word") else "F",
             "core" if desc.get("core_coupled") else "dressed",
             "dimless" if desc.get("dimensionless") else "dimful")
    return (base, flags)


FREEZE = {
    "B584 antiphase-listener coefficient": dict(
        contraction_against="listener", word="RL", core_coupled=True,
        dimensionless=True),
    "B613 closure predicate": dict(eig_multiset_fn=True, word=None,
                                   core_coupled=True, dimensionless=True),
    "B611 trace-layer exemplar (trace of B_odd)": dict(
        scalar_arith=True, word="RL", core_coupled=True,
        dimensionless=True),
}

HELD_OUT = {
    "B593 displaced-ear amplitude": dict(
        contraction_against="listener", word=None, core_coupled=True,
        dimensionless=True),
    "B626 Jacobian reality quantity J = mu + 1/mu": dict(
        scalar_arith=True, word="mu", core_coupled=True,
        dimensionless=True),
    "B632/B637 chord cubic Y": dict(
        contraction_against="partner-object", word=None,
        core_coupled=True, dimensionless=True),
    # v0 is a CARRIER (R0, the disclosed revision); its quantity:
    "B632 dim h0(M;27) = 1 (v0's quantity per R0)": dict(
        eig_multiset_fn=True, word=None, core_coupled=True,
        dimensionless=True),
}

print("== FREEZE set (must reproduce the bank) ==")
for nm, d in FREEZE.items():
    print(f"  {nm}: {type_of(d)}")
print("\n== HELD-OUT battery (mechanical, post-freeze) ==")
for nm, d in HELD_OUT.items():
    print(f"  {nm}: {type_of(d)}")
