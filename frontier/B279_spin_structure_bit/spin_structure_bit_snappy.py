"""B279 -- the checkable topological inputs for "does the amphicheiral tau fix or swap the 2 spin structures of 4_1?"
(the Chat-2 headline reduction). Run with sage-python (needs SnapPy).

This verifies the THREE inputs the FIX proof rests on (the proof itself is in FINDINGS.md):
  (1) H_1(4_1;Z) = Z  =>  H^1(4_1;Z/2) = Z/2  =>  EXACTLY 2 spin structures.
  (2) the full symmetry group of the complement is D4 (order 8), and 4_1 is hyperbolic, so by Mostow rigidity +
      Gordon-Lueke every complement-isometry is AMBIENT (extends to a symmetry of the pair (S^3, 4_1)).
  (3) every isometry's action on the cusp (meridian, longitude) is by +-1 entries, i.e. TRIVIAL mod 2 -- so the
      action on H^1(.;Z/2) is the identity (forced; Aut(Z/2)=1), and the fix/swap bit is a framing-level invariant
      NOT visible from homology alone. The S^3-bounding spin structure resolves it (see FINDINGS): FIX.
"""
import snappy


def inputs():
    M = snappy.Manifold("m004")                       # = 4_1, the figure-eight complement
    H1 = str(M.homology())
    sg = M.symmetry_group()
    cusp_actions = []
    for iso in sg.isometries():
        m = iso.cusp_maps()[0]
        cusp_actions.append(((int(m[0, 0]), int(m[0, 1])), (int(m[1, 0]), int(m[1, 1]))))
    trivial_mod2 = all(all(abs(x) % 2 == (1 if (i == j) else 0) for i, row in enumerate(a) for j, x in enumerate(row))
                       for a in cusp_actions)          # every cusp map == identity mod 2
    return {
        "manifold": "m004 = 4_1",
        "H1": H1,                                       # 'Z'
        "n_spin_structures": 2,                         # H^1(;Z/2)=Z/2
        "symmetry_group": str(sg),                      # 'D4'
        "order": sg.order(),                            # 8
        "is_full_group": sg.is_full_group(),            # True => isometries are ambient (hyperbolic)
        "all_cusp_actions_trivial_mod2": trivial_mod2,  # True => homological action on H^1(;Z/2) is identity
    }


if __name__ == "__main__":
    d = inputs()
    for k, v in d.items():
        print(f"  {k}: {v}")
    assert d["H1"] == "Z" and d["symmetry_group"] == "D4" and d["order"] == 8
    assert d["is_full_group"] and d["all_cusp_actions_trivial_mod2"]
    print("\nInputs verified. The homological tau-action on H^1(;Z/2) is trivial; FIX follows from the")
    print("S^3-bounding spin structure being ambient-symmetry-invariant (FINDINGS.md). => the bit is FIX.")
