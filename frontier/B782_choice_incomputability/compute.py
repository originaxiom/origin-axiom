"""B782 -- C22, the choice-incomputability wall: the measurement torsor admits no
equivariant section (a free (Z/2)^3-action has no fixed point)."""
import itertools
import json

G = list(itertools.product([0, 1], repeat=3))          # (Z/2)^3 = (c, theta, gamma5)
torsor = list(itertools.product([0, 1], repeat=3))       # the 8 closings (the regular G-set)
act = lambda g, x: tuple(a ^ b for a, b in zip(g, x))    # translation action

free = all(act(g, x) != x for g in G if g != (0, 0, 0) for x in torsor)
transitive = all(any(act(g, x) == y for g in G) for x in torsor for y in torsor)
# an equivariant section = a G-fixed closing (fixed by ALL of G); a free action has none
G_fixed = [x for x in torsor if all(act(g, x) == x for g in G)]
has_equivariant_section = len(G_fixed) > 0

print(f"closing group (Z/2)^3 |G|={len(G)}; torsor size={len(torsor)}")
print(f"action FREE (no non-identity g fixes a closing): {free}")
print(f"action TRANSITIVE (a torsor): {transitive}")
print(f"G-fixed closings (equivariant sections): {G_fixed}  -> exists: {has_equivariant_section}")
verdict = "RESOLVED-A" if (free and transitive and not has_equivariant_section) else "RESOLVED-B"
print(f"\nVERDICT: {verdict}  -- C22 [NO-GO]: the free measurement torsor admits NO equivariant")
print("section; no symmetry-respecting process internal to the object selects a closing;")
print("the choice must be broken from outside. (Interpretation firewalled to C18.)")

json.dump({
    "arc": "B782", "chain_link": "C22", "verdict": verdict,
    "action_free": bool(free), "action_transitive": bool(transitive),
    "equivariant_sections": G_fixed, "no_equivariant_section": not has_equivariant_section,
    "headline": ("C22 [NO-GO]: the measurement torsor (C20) is a free transitive (Z/2)^3-action; "
                 "a free action has no G-fixed point, so no equivariant section selects a closing; "
                 "the choice is not computable by any symmetry-respecting internal process -- it is "
                 "broken from outside. Math-only; the observer/Born reading is the priced C18 bridge."),
}, open(__file__.replace("compute.py", "results.json"), "w"), indent=1)
