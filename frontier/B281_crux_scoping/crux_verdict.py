"""B281 verdict (pyenv-safe; heavy probe in crux_geom_probe.py).

Scoping of the CRUX (the load-bearing conjecture of the E6 bridge): does the 3d-3d/class-S INPUT type equal the
arithmetic McKay OUTPUT type (= E6)? Decomposed into four levels, each tagged by where it can be settled.
FIREWALLED; nothing to CLAIMS.md.
"""
# Level 2 result (computed, crux_geom_probe.py): every simple type gives dim H^1 = rank on 4_1.
EVERY_TYPE_GIVES_RANK = True          # E6 NOT geometrically distinguished; 3d-3d input geometrically FREE

# the four-level decomposition and where each is settleable
LEVELS = {
    "combinatorial (do both E6's share Lie data?)":
        ("YES but TAUTOLOGICAL", "in-sandbox (B267); both ARE E6 so agreement is automatic (B272). Not evidence."),
    "geometric (does the char variety distinguish E6?)":
        ("NO", "in-sandbox SETTLED (B264 + this probe + Falbel-Guilloux): every G gives dim H^1=rank => input free."),
    "arithmetic (is E6 selected?)":
        ("YES, output-only", "in-sandbox (B266): McKay reduction pi_1->SL(2,F_3)=2T, McKay(2T)=E6. A finite-quotient "
         "fact, independent of the character variety / the 3d-3d input."),
    "physics forcing (does 3d-3d force input=output?)":
        ("UNSETTLED", "NOT in-sandbox: needs T[4_1;E6] (the type-E6 3d-3d theory / state integral), which has no "
         "constructive Lagrangian/quiver for exceptional types. Specialist/tool gate = the R6 'arithmetic-selection "
         "overlay' novel kernel."),
}

# the only candidate TRUE-route, = the R6 NEEDS-SPECIALIST kernel:
CANDIDATE_FORCING_PRINCIPLE = "impose G = McKay(arithmetic reduction); E6 is the unique type with McKay(2T)=G"
SETTLEABLE_IN_SANDBOX = False          # CRUX cannot be settled TRUE in-sandbox; geometry evidence leans FALSE/unforced


def verdict():
    # the scope's bottom line: geometry settled (input free), physics-forcing is the specialist gate
    return EVERY_TYPE_GIVES_RANK and not SETTLEABLE_IN_SANDBOX


if __name__ == "__main__":
    for lvl, (ans, how) in LEVELS.items():
        print(f"[{ans}] {lvl}\n      {how}")
    print("\ncandidate TRUE-route:", CANDIDATE_FORCING_PRINCIPLE)
    print("settleable in-sandbox?", SETTLEABLE_IN_SANDBOX, "| verdict:", verdict())
