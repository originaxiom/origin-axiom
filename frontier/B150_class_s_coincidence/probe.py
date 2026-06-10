"""B150 -- class-S coincidence: CHARACTERIZE the object, tag every comparison FORCED / PERMITTED / RHYME.

L14 (scoping pass, NOT a verdict-of-match): does the SL(2,Z) trace-map / mapping-class action on the once-punctured-
torus character variety (B148's object) COINCIDE with the S-duality / mapping-class action on the Coulomb branch of the
class-S theory of the once-punctured torus? This module is a CHARACTERIZATION + a tagged comparison, from a focused
read of the primary literature -- it does NOT declare a coincidence and fabricates NO sandbox "match". The sandbox here
only RE-ASSERTS the B148 anchor data (the comparison's verifiable left-hand side, imported from B148); the right-hand
side and the FORCED/PERMITTED/RHYME tags are cited prose, held to the actual anchor data.

THE BINDING DISTINCTION (two different spaces). The class-S SL(2,Z) acts on TWO spaces:
  (i) the UV gauge coupling tau (the complex-structure modulus of the punctured torus) -- the well-known S-duality
      modularity; this is NOT the trace-map dynamics, it is a HOMONYM -> RHYME;
  (ii) the Coulomb-branch / Fricke CHARACTER VARIETY -- where the trace-map action lives. A coincidence is FORCED only if
      the action ON THE CHARACTER VARIETY reproduces the B148 anchors (hyperbolic classes, lambda_m^2, Q(sqrt(m^2+4))
      fixed slopes, the kappa cubic, the kappa=-2 Markov fiber).
Every tag below is adjudicated against THIS distinction.

WHAT THE LITERATURE SAYS (primary sources, read for this stage):
  * Allegretti-Shan, arXiv:2411.17378 "Dualities of K-theoretic Coulomb branches from a once-punctured torus":
    M_flat(S_{1,1}, SL2C) = the Fricke cubic  a^2+b^2+c^2+abc = 2 + lambda + lambda^-1  (a,b,c = -traces of alpha,beta,
    alpha*beta); the mapping class group SL2(Z) = Mod(S_{1,1}) = <sigma,tau_+ | sigma^4=1,(sigma tau_+)^3=sigma^2> acts
    by the Dehn twists tau_+, tau_-; three Z2-invariant subalgebras of the quantized skein algebra are quantized
    K-theoretic Coulomb branches of the 4d N=2* theories (SL2 / PGL2, Langlands-dual), PERMUTED by the MCG; and
    explicitly "SL2(Z) is the S-duality group of the N=2* theories" with the duality acting "on the character variety
    itself through mapping class group transformations, not merely on the coupling tau."
  * Cantat-Loray, AIF 59 (2009) 2927 / arXiv:0711.1579 (+ "Bers and Henon, Painleve and Schroedinger", 0711.1727): a
    mapping class acts BOTH as a GL(2,Z) matrix (on homology) AND as a polynomial automorphism of the cubic (the trace
    map / Markov surface); its dynamical degree / topological entropy = log(spectral radius of the GL(2,Z) matrix);
    hyperbolic / pseudo-Anosov elements; the Markov surface and trace maps; the quasiperiodic-Schrodinger connection.
  * Gaiotto-Moore-Neitzke, arXiv:0907.3987 "Wall-crossing, Hitchin Systems, and the WKB Approximation": the class-S
    Coulomb branch (on S^1) = the rank-2 Hitchin moduli space of the surface (= the character variety by nonabelian
    Hodge).

CONVENTION MATCH (verified): B148's kappa = x^2+y^2+z^2-xyz-2 = tr[A,B] = the boundary/puncture holonomy trace; with
a=-x,b=-y,c=-z, Allegretti-Shan's a^2+b^2+c^2+abc = x^2+y^2+z^2-xyz, so kappa = lambda+lambda^-1 EXACTLY, and kappa=-2
<=> lambda=-1. Same cubic, same level sets.

OUTCOME = MIXED (per the two-space distinction; report the table, not a single global label):
  FORCED at the character-variety / MCG level (the genuine bridge: the SL(2,Z) trace-map action on the Fricke character
  variety IS the N=2* S-duality MCG action, reproducing the B148 anchor data); RHYME at the tau-modularity level (the
  homonym) and at the physical-magnitude / gauge-content level (the gauge group is free input; no scale is fixed; N=2* is
  non-chiral -- the firewall, L15's separate question). EVEN THE FORCED PART IS MATHEMATICS: it identifies the tower's
  symmetry with a known duality action; it does NOT cross to physical magnitude. MATH tier; firewalled; nothing to
  CLAIMS.md.
"""
from __future__ import annotations

from frontier.B148_kappa_fricke_metallic.probe import (
    metallic_trace_fields,
    verify_dehn_twists_preserve_kappa,
    verify_eigenvalue_is_metallic_squared,
    verify_fixed_slopes,
    verify_markov_slice_and_two_states,
    verify_metallic_trace_symbolic,
)

TAGS = {"FORCED", "PERMITTED", "RHYME"}


def anchor_data():
    """Re-assert the B148 invariant data (the comparison's verifiable LHS) -- the standard a FORCED coincidence must meet."""
    tr_ok, det_ok = verify_metallic_trace_symbolic()
    a_ok, b_ok = verify_dehn_twists_preserve_kappa()
    markov_ok, k333, k000 = verify_markov_slice_and_two_states()
    return {
        "RmLm_hyperbolic_tr_m2plus2": bool(tr_ok and det_ok),
        "eigenvalue_is_metallic_squared": bool(verify_eigenvalue_is_metallic_squared()),
        "fixed_slopes_t2_plus_mt_minus_1": bool(verify_fixed_slopes()),
        "dehn_twists_preserve_kappa": bool(a_ok and b_ok),
        "kappa_minus2_is_markov": bool(markov_ok and k333 == -2 and k000 == -2),
        "trace_fields": metallic_trace_fields(),
    }


# The tagged comparison. Each row: the unit side (B148), the class-S side (cited), the tag, the source, the reason.
COMPARISON = [
    {"point": "The space",
     "unit_side": "kappa level sets of the SL(2,C) character variety of S_{1,1}; coords (tr A, tr B, tr AB); "
                  "kappa = tr[A,B] = x^2+y^2+z^2-xyz-2 (the Fricke cubic)",
     "classS_side": "Allegretti-Shan: M_flat(S_{1,1},SL2C) = the Fricke cubic a^2+b^2+c^2+abc = 2+lambda+lambda^-1 "
                    "(a,b,c=-traces); GMN: the class-S Coulomb branch on S^1 = the rank-2 Hitchin moduli of the surface "
                    "= this character variety (nonabelian Hodge). Convention match: kappa = lambda+lambda^-1 exactly.",
     "tag": "FORCED",
     "source": "arXiv:2411.17378 (Fricke cubic); arXiv:0907.3987 (Coulomb=Hitchin)",
     "reason": "literally the same cubic surface in the same trace coordinates; kappa = the puncture-holonomy trace"},

    {"point": "The group",
     "unit_side": "SL(2,Z) = Out+(F_2) = MCG(S_{1,1}), generated by the two Dehn twists tau_a, tau_b",
     "classS_side": "Allegretti-Shan: SL2(Z) = Mod(S_{1,1}) = <sigma,tau_+ | sigma^4=1,(sigma tau_+)^3=sigma^2>, "
                    "generated by the Dehn twists tau_+, tau_-, = the N=2* S-duality group",
     "tag": "FORCED",
     "source": "arXiv:2411.17378",
     "reason": "the same mapping class group with the same Dehn-twist generators"},

    {"point": "The action ON THE CHARACTER VARIETY (not on tau)",
     "unit_side": "the trace map: tau_a, tau_b act on (x,y,z) preserving kappa (B148)",
     "classS_side": "Allegretti-Shan: the MCG acts on the skein/character algebra by the same Dehn twists, permuting "
                    "the three Coulomb-branch subalgebras; explicitly the S-duality acts 'on the character variety "
                    "itself through mapping class group transformations, not merely on the coupling tau'",
     "tag": "FORCED",
     "source": "arXiv:2411.17378",
     "reason": "the physics N=2* duality IS realized as the MCG / trace-map action on the character variety -- the same "
               "action as B148 (Coulomb branches are MCG-permuted subalgebras inside that variety)"},

    {"point": "Dynamical content: lambda_m^2 (top eigenvalue)",
     "unit_side": "(metallic mean)^2 = spectral radius of R^m L^m on homology (B148)",
     "classS_side": "Cantat-Loray: a mapping class acts as a GL(2,Z) matrix AND as a polynomial automorphism of the "
                    "cubic; its dynamical degree / entropy = log(spectral radius of the homology matrix). For R^m L^m "
                    "that spectral radius is lambda_m^2.",
     "tag": "FORCED",
     "source": "Cantat-Loray AIF 59 (2009) 2927; arXiv:0711.1579 / 0711.1727",
     "reason": "lambda_m^2 is the dynamical degree of the metallic mapping class -- an invariant of the SAME action. "
               "(The literature does not single out the metallic family; its data are reproduced because it is the same "
               "group acting the same way -- FORCED at the framework level, automatic for the specific elements.)"},

    {"point": "Fixed slopes (roots of t^2+m t-1) and field Q(sqrt(m^2+4))",
     "unit_side": "boundary fixed points on RP^1 + eigenvalue field of R^m L^m in SL(2,Z) (B148)",
     "classS_side": "the same SL(2,Z) element's homology action (Cantat-Loray's GL(2,Z) matrix = the mapping class)",
     "tag": "FORCED",
     "source": "arXiv:0711.1579",
     "reason": "intrinsic invariants of the same group element acting in the same action"},

    {"point": "kappa = -2 (the Markov surface)",
     "unit_side": "B148: kappa=-2 <=> p^2+q^2+r^2 = 3pqr",
     "classS_side": "the central fiber lambda=-1 (lambda+lambda^-1=-2) of the Fricke family; the Markov/Cayley cubic of "
                    "Cantat-Loray's trace-map dynamics",
     "tag": "FORCED",
     "source": "arXiv:2411.17378; arXiv:0711.1727",
     "reason": "the same distinguished fiber of the same cubic family"},

    {"point": "SL(2,Z) modularity on the UV coupling tau",
     "unit_side": "(NOT the B148 object -- the character variety, not the coupling)",
     "classS_side": "the standard S-duality modular action on tau = the complex-structure modulus of the punctured torus",
     "tag": "RHYME",
     "source": "standard class-S (Gaiotto 0904.2715)",
     "reason": "HOMONYM: same group NAME, different SPACE (the coupling, not the character variety); carries none of the "
               "metallic eigenvalue/field data. This is the rhyme the binding distinction rules out."},

    {"point": "A physical SCALE / gauge-coupling magnitude / the Standard Model",
     "unit_side": "-- (kappa is scale-free; B148 sec 0)",
     "classS_side": "the duality permutes Coulomb branches and fixes NO scale; the gauge group (SU(2), N=2*) is INPUT, "
                    "not selected; N=2* is non-chiral (no SM generations)",
     "tag": "RHYME",
     "source": "knowledge/K006; OPEN_LEADS L15 (separate, out of scope)",
     "reason": "the bridge is mathematical (a symmetry identification), not physical-magnitude; gauge group free input "
               "(the kill condition); MB9/MB10 structure != gauge content. The physical-magnitude boundary is L15."},
]


def verdict():
    forced = [c["point"] for c in COMPARISON if c["tag"] == "FORCED"]
    rhyme = [c["point"] for c in COMPARISON if c["tag"] == "RHYME"]
    return {
        "overall": "MIXED",
        "forced_level": "the SL(2,Z) trace-map action on the Fricke CHARACTER VARIETY IS the N=2* S-duality MCG action, "
                        "reproducing the B148 anchor data (points: %s)" % "; ".join(forced),
        "rhyme_level": "tau-modularity (homonym) and physical-magnitude/gauge-content (firewall, L15) (points: %s)"
                       % "; ".join(rhyme),
        "firewall": "even the FORCED part is mathematics (symmetry = a known duality action); it does NOT cross to "
                    "physical magnitude -- that is L15.",
    }


def main():
    print("B150 -- class-S coincidence (L14): CHARACTERIZE + tag FORCED/PERMITTED/RHYME (the unit's widest reach)\n")
    a = anchor_data()
    print("[anchor data re-asserted from B148 -- the standard a FORCED coincidence must meet]")
    for k, v in a.items():
        if k != "trace_fields":
            print(f"    {k:36} : {v}")
    print("    trace_fields (m -> reduced field Q(sqrt .)):",
          {r["m"]: r["field_radicand"] for r in a["trace_fields"]})
    print("\n[tagged comparison, against the tau-vs-character-variety distinction]")
    for c in COMPARISON:
        print(f"  [{c['tag']:9}] {c['point']}")
        print(f"             class-S: {c['classS_side'][:96]}{'...' if len(c['classS_side'])>96 else ''}")
        print(f"             why {c['tag']}: {c['reason'][:96]}{'...' if len(c['reason'])>96 else ''}  [{c['source']}]")
    v = verdict()
    print(f"\nVERDICT: {v['overall']}")
    print(f"  FORCED -- {v['forced_level']}")
    print(f"  RHYME  -- {v['rhyme_level']}")
    print(f"  FIREWALL -- {v['firewall']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
