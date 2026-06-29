"""B283 verdict (pyenv) -- scoping the "arithmetic self-generation" vein (path-a / the metallic WRT tower).

Result: it COLLAPSES, like the E6 vein (B282). The WRT-period <-> trace-field link is PROVEN (B204), GENERIC to all
torus bundles (metallic = the diagonal a=b; confirmed here for irregular words too), and KNOWN prior art (Jeffrey
1992). The path-a conjectures (period = order of fundamental unit; absent when m^2+4 prime) are superseded/falsified
by B204. FIREWALLED; nothing to CLAIMS.md.
"""
# scoping decomposition of the self-generation vein:
LEVELS = {
    "WRT period reflects the trace-field arithmetic (the core 'self-generation')":
        ("PROVEN + GENERIC + KNOWN", "B204 proved per|Z(a,b)| = lcm(a,b)(4+ab)/gcd(4+ab,4) via Gauss reciprocity; "
         "general for ALL once-punctured-torus bundles (metallic = diagonal a=b); = Jeffrey 1992 (V199 audit). "
         "B283 probe: period governed by det(phi+I) for metallic, non-metallic, AND irregular monodromies."),
    "path-a conjecture: period = order of the fundamental unit":
        ("SUPERSEDED", "replaced by the exact closed form P(m)=m(m^2+4)/gcd(m^2+4,4) (B204)."),
    "path-a conjecture: period absent when m^2+4 is prime":
        ("FALSIFIED", "a search-bound artifact (B204): m=1 (disc 5, prime) has the SMALLEST period."),
    "trace map / Fibonacci self-generation (kappa = 2 + lambda^2)":
        ("KNOWN", "= the Fibonacci-Hamiltonian trace map (banked K007/K010/B107/B148); quasicrystal-bridge-status."),
    "metallic family generates Q(sqrt(m^2+4))":
        ("ELEMENTARY", "trace(R^m L^m) = m^2+2 => trace field Q(sqrt(m^2+4)); immediate, not deep."),
}

METALLIC_IS_SPECIAL = False         # the metallic family is the diagonal of a general law, not distinguished
OBJECT_SPECIFIC_NOVEL_SIGNAL = False  # no object-specific novel arithmetic survives scoping

# the meta-conclusion (both veins scoped):
META = ("Both the E6-physics vein (B282) and the arithmetic-self-generation vein (B283) collapse to: generic "
        "structure + known prior art + the SAME two NEEDS-SPECIALIST kernels (arithmetic-McKay-selection, "
        "tau=outer-automorphism) + Reid's unique-arithmetic-knot theorem. The in-sandbox program is exhausted of "
        "new object-specific signal.")


def verdict():
    return not METALLIC_IS_SPECIAL and not OBJECT_SPECIFIC_NOVEL_SIGNAL


if __name__ == "__main__":
    for lvl, (ans, how) in LEVELS.items():
        print(f"[{ans}] {lvl}\n      {how}")
    print("\nmetallic special?", METALLIC_IS_SPECIAL, "| object-specific novel signal?", OBJECT_SPECIFIC_NOVEL_SIGNAL)
    print("META:", META)
    print("verdict (vein collapses):", verdict())
