"""xB032 T3/T4 -- the step B803 named and never took, and where it lands.

SEALED PREDICTION (988ca30d): "Fried's theorem requires the flat bundle to be ACYCLIC -- the same
h^1 = 0 condition that Friedmann-Witten buy with finite pi_1 -- so the thermodynamic route to T_lambda
hits THE SAME WALL as the topological one."

This cell does three things:
  (1) records the hypotheses, quoted;
  (2) CHECKS, on the record's own objects, whether they satisfy them;
  (3) states what that does and does not license.
"""
import json, os, sys, pathlib, warnings
warnings.filterwarnings("ignore")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] /
                       'B1418_the_family_as_the_object' / 'verification'))
from c2_reducible_index import *
from c2_run import characters

print("T3       FRIED'S THEOREM -- hypotheses, quoted")
print("         Source read at source: N. V. Dang, C. Guillarmou, G. Riviere, S. Shen,")
print("         'The Fried conjecture in small dimensions', arXiv:1807.01189v3, Invent. Math.")
print("         Fried himself (Invent. Math. 84 (1986) 523-540) is NOT read here; his theorem is")
print("         quoted THROUGH DGRS, so his row stays CITED-UNREAD and DGRS becomes READ-AT-SOURCE.")
print()
print('         DEFINITION, verbatim: "We say that the complex (or rho) is ACYCLIC if')
print('         H^k(M; rho) = 0 for each k."')
print('         FRIED\'S FORMULA, verbatim (their eq. 1.2, dim(M) = 2n_0 + 1):')
print('           "|zeta_{X,rho}(0)^{(-1)^{n_0}}| = tau_rho(M),')
print('            where rho is the lift to pi_1(M) of an ACYCLIC and UNITARY representation')
print('            rho_0 : pi_1(M) -> U(C^r)."')
print('         And: "If rho is unitary and acyclic and if X is the geodesic vector field on the')
print('         unit tangent bundle ... of a hyperbolic manifold M, Fried showed that zeta_{X,rho}')
print('         extends meromorphically ... Then he proved [Fr2] the remarkable formula".')
print()
print("         SO THE HYPOTHESES ARE TWO: ACYCLIC and UNITARY.  The seal predicted acyclicity;")
print("         unitarity is a SECOND hypothesis the seal did not name.")
print()

# ---- (2) do the record's own objects satisfy them?
print("T3       DO THE RECORD'S OWN MODULES SATISFY THEM?  Measured, not asserted.")
K = NF([1, 0, -1, 0, 1]); z = K.alpha()
S = [K.pw(z, k) for k in range(12)]
res = {}
for name in ('t12835', 'm004'):
    M, gens, rels, mu, lam = presentation(name)
    chars = characters(K, gens, rels, S)
    h1s = []
    for chi in chars:
        if all(K.is_zero(K.sub(chi[g], K.const(1))) for g in gens):
            continue
        chi2 = {g: K.mul(chi[g], chi[g]) for g in gens}
        c, h1 = nonsplit_cocycle(K, gens, rels, chi2)
        if c is not None:
            h1s.append(h1)
    res[name] = h1s
    print(f"         {name}: {len(h1s)} reducible non-split loci; h^1(chi^2) values "
          f"{sorted(set(h1s))}; minimum {min(h1s) if h1s else None}")
    print(f"           ACYCLIC requires H^k = 0 for EVERY k, in particular h^1 = 0.")
    print(f"           Every locus has h^1 >= 1 BY CONSTRUCTION -- nonsplit_cocycle() returns a")
    print(f"           cocycle only when h^1(chi^2) > 0.  So ZERO of {len(h1s)} loci are acyclic.")
print()
print("         UNITARY?  A unitary representation is completely reducible (semisimple).")
print("         The record's modules are REDUCIBLE NON-SPLIT by construction -- rho_chi =")
print("         [[chi, c],[0, chi^-1]] with c a NON-coboundary cocycle, i.e. the extension does")
print("         NOT split, i.e. rho_chi is NOT semisimple.  Hence NOT unitary.  And B1418's own")
print("         FINDINGS say so: 'not the geometric holonomy, not unitary'.")
print("         Independent corroboration from the record's own numbers: I^ss = 0 EVERYWHERE in")
print("         B1418's table -- the semisimplification, which is what a unitary rep would be,")
print("         gives index zero at every locus.  The index exists ONLY off the semisimple set.")
print()
allh1 = sum(res.values(), [])
acyclic = sum(1 for h in allh1 if h == 0)
print(f"         RESULT: loci examined {len(allh1)}; satisfying ACYCLIC: {acyclic}; "
      f"satisfying UNITARY: 0 (non-split by construction)")
print("         *** THE SEALED PREDICTION HOLDS, AND IS STRONGER THAN SEALED.")
print("         Fried needs ACYCLIC + UNITARY.  The record's chirality mechanism is defined on")
print("         the locus h^1 != 0 and fires only on NON-semisimple modules.  It lives exactly on")
print("         the set BOTH hypotheses exclude.  The thermodynamic route does not go around the")
print("         wall -- it requires STRICTLY MORE than the topological one.")
print()
print("T4       THE HONEST READING, AND ITS LIMITS")
print("         (a) T1 established log|Tor H_1(X_n)| = n * h_top(monodromy).  So Friedmann-Witten's")
print("             T_O term is an ENTROPY and their condition P_eff = 84 is an ENTROPY")
print("             REQUIREMENT on the three-cycle: 84 nats, i.e. n = 88 levels of this tower.")
print("             THIS IS A REFRAMING.  It changes no number and derives nothing.")
print("         (b) It does NOT make a hyperbolic Qhat admissible.  xB029 Addendum 1 stands:")
print("             FW assume FINITE pi_1 and the zero modes are real.")
print("         (c) DO NOT SLIDE BETWEEN THE TWO ENTROPIES.  h_top of the GEODESIC FLOW of any")
print("             hyperbolic 3-manifold is 2, universally -- it discriminates nothing.  The")
print("             entropy that carries information here is the MONODROMY's, log lambda, which")
print("             is a fibration datum and not a metric one.")
print("         (d) Gate 5 absolute.  No value.  Nothing to CLAIMS.md.")
json.dump({"fried_hypotheses": ["acyclic", "unitary"],
           "source_read_at_source": "Dang-Guillarmou-Riviere-Shen arXiv:1807.01189v3",
           "fried_himself": "CITED-UNREAD (quoted through DGRS)",
           "loci_h1_values": {k: sorted(set(v)) for k, v in res.items()},
           "loci_count": {k: len(v) for k, v in res.items()},
           "acyclic_loci": acyclic, "unitary_loci": 0,
           "sealed_prediction": "CONFIRMED, and stronger: unitarity is a second hypothesis"},
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "thermo_t3.json"),
               "w", encoding="utf-8"), indent=1, default=str)
print("\nT3/T4 PASS  (content is the verdict above)")
