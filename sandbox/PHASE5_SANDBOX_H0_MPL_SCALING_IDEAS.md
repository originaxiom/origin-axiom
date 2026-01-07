# Phase 5 Sandbox: H₀/Mₚₗ Scaling and Vacuum-Energy Numerology

**Status:** Sandbox only — not a claim, not part of Phases 0–4, and not used
in any current corridor, mechanism, or FRW-facing diagnostic.

This note records a set of exploratory ideas where the enormous hierarchy
between the Hubble scale \(H_0\) and the Planck scale \(M_\mathrm{Pl}\)
was used to construct small dimensionless parameters, which were then
combined with \(M_\mathrm{Pl}\) to guess formulas for the vacuum-energy
density \(\rho_\Lambda\) or the dark-energy fraction \(\Omega_\Lambda\).
These were numerical experiments, not derivations from the non-cancellation
mechanism of Phase 3.

## 1. Core idea: small parameters from the Hubble–Planck hierarchy

The underlying intuition was:

- The ratio \(H_0 / M_\mathrm{Pl}\) is extremely small.
- Any physically meaningful vacuum-energy scale might plausibly be built
  from \(M_\mathrm{Pl}\) and \(H_0\) in a dimensionally consistent way.
- The observed \(\rho_\Lambda\) is tiny compared to \(M_\mathrm{Pl}^4\), so
  powers of \(H_0 / M_\mathrm{Pl}\) could, in principle, generate the right
  suppression.

In various sessions, we experimented with definitions of a small parameter
\(\varepsilon\) such as:
- \(\varepsilon \sim H_0 / M_\mathrm{Pl}\);
- \(\varepsilon \sim (H_0 / M_\mathrm{Pl})^{3/2}\);
- other variants chosen to make dimensional bookkeeping convenient.

## 2. Prototype scaling ansätze for \(\rho_\Lambda\)

Using such \(\varepsilon\), we then considered schematic ansätze of the form

- \(\rho_\Lambda \sim M_\mathrm{Pl}^4 \, \varepsilon^p\), for various powers
  \(p\), or
- \(\rho_\Lambda \sim c \, M_\mathrm{Pl}^2 H_0^2\),

where:
- \(p\) was chosen or tuned so that the resulting \(\rho_\Lambda\) landed
  near the observed value;
- \(c\) was treated as an \(\mathcal{O}(1)\) coefficient (sometimes
  decorated with simple rational factors motivated by other heuristic
  ideas, such as counting arguments or generation numbers).

Several specific exponents (including values like \(p = 2\) or fractional
powers) were tried.  Some of them led to numerically “interesting”
proximity to the observed vacuum-energy density when evaluated with
realistic values for \(H_0\) and \(M_\mathrm{Pl}\).  However, these matches
were **not** derived from first principles; they depended strongly on the
chosen exponent and prefactor and thus carry a high risk of numerology.

## 3. Relationship to the current Phase 3–4 pipeline

It is important to stress that:

- The Phase 3 toy mechanism, as presently implemented, defines a
  dimensionless amplitude observable \(A_0(\theta)\) and a floor
  \(\varepsilon\) that are *internal* to that toy ensemble.
- The Phase 4 F1 mapping constructs a *structural* energy-like quantity
  \(E_\mathrm{vac}(\theta) = \alpha \, A(\theta)^\beta\) and then feeds it
  into FRW-inspired diagnostics.  \(\alpha\) and \(\beta\) are tunable
  mapping parameters, not physically derived constants.

The H₀/Mₚₗ scaling ideas documented here did **not** arise from that
pipeline.  Instead, they attempted to jump directly from cosmological
scales to \(\rho_\Lambda\) using dimensional analysis and heuristic choice
of exponents.  There is currently:

- no derivation that connects the Phase 3 non-cancellation floor to
  \(H_0/M_\mathrm{Pl}\);
- no code path in the repository that implements these scaling formulas
  as part of the Phase 4 diagnostics.

Consequently, these ideas are explicitly quarantined from the main ladder.

## 4. Risks and limitations

The main reasons to keep these constructions in a sandbox are:

1. **Post hoc tuning**

   The choice of exponent \(p\) and coefficient \(c\) can easily be tuned
   until the output \(\rho_\Lambda\) lands near the observed value.  Without
   independent theoretical justification, such matches are not evidence of
   explanatory power.

2. **Ambiguity in the definition of \(\varepsilon\)**

   There is no unique, physically mandated way to define a dimensionless
   small parameter from \(H_0\) and \(M_\mathrm{Pl}\).  Different choices
   (e.g. \(H_0/M_\mathrm{Pl}\) vs. \((H_0/M_\mathrm{Pl})^{3/2}\)) lead to
   different scaling properties and may require different exponents \(p\).

3. **Disconnection from the non-cancellation mechanism**

   The Origin Axiom program is, by design, centered on a specific kind of
   non-cancellation principle implemented at the level of amplitudes and
   floors.  The scaling games here do not yet bridge that mechanism to
   cosmic scales in a principled way.

4. **No corridor or data impact**

   These scaling ideas are not used to define corridors, to select
   \(\theta\), or to interpret any current FRW or data-facing diagnostics.
   Treating them as anything more than numerology at this stage would
   overstate what the program has achieved.

## 5. Conditions for future rehabilitation

If future work suggests that an H₀/Mₚₗ-based scaling should re-enter the
main ladder, it should satisfy at least the following criteria:

- **Derived linkage:** The appearance of \(H_0/M_\mathrm{Pl}\) (or any
  related small parameter) should be derived from a concrete mechanism
  tied to the non-cancellation floor, not merely posited on dimensional
  grounds.
- **End-to-end integration:** The scaling should be expressed in terms of
  quantities produced by the existing Phase 3–4 pipeline (e.g.
  distributions of \(A(\theta)\), properties of corridors, etc.), and
  implemented as actual code in the repository.
- **Robustness and falsifiability:** The proposal should make testable
  predictions about how changes in model assumptions (e.g. mapping
  exponents, ensemble structure, or external cosmological parameters)
  affect the inferred \(\rho_\Lambda\), and these predictions should be
  checked against negative controls.
- **Clear separation from pure numerology:** Any numerical agreement with
  observed values should be accompanied by a careful accounting of the
  number of free choices made (exponents, coefficients, definitions of
  \(\varepsilon\)) so that the explanatory power, if any, can be honestly
  assessed.

Until such a mechanism is in place, all H₀/Mₚₗ scaling experiments remain
here as a record of useful intuition pumps rather than as components of
the main Origin Axiom program.
