# A smooth connection for the existing cusp unit

2026-10-11. **Scoped positive realization; unit selection not derived.** Seal `cad6ef3ec` precedes the first run. All 136 exact safeguards passed, with no source change or scientific rerun. The hand proof supplies the all-integer and analytic statements; the finite checks are not an index certificate.

## Result

On the effective modular base B=PSL(2,Z)\H, the weight-12n Hodge line with its Petersson metric has

    F_n = -6in dA,     effective flux = n,
    E_n = 6pi n²/g².

The curvature is smooth on the open orbifold, has finite two-dimensional Yang–Mills action and obeys the source-free bulk equation. It minimizes that action in its fixed-flux sector. The weight 12 has trivial elliptic stabilizer characters and is the least positive integral weight with that property in this automorphic-line family.

This strengthens the analytic description of an already admitted cusp unit. It does not determine which line is coupled to matter. It also does not select the unit: n=0 has lower energy than n=1 for this action when both sectors are allowed. Only with nonzero integral flux imposed do the two minimal sectors have |n|=1.

## Why triviality does not rule out curvature

Conditional on the standard discriminant transformation law HDelta, Delta trivializes the weight-12 line on the open base, while the compactified extension is the cusp divisor line. The same open holomorphic line admits both a flat connection and the nonflat Chern connection above. An available flat trivialization or a torsion Picard class does not fix a connection.

The distinction is stronger than an integer-family example: the open trivial line supports the positive smooth metrics (y^12 |Delta|²)^s for every real s, with effective flux s and finite action. Quantization therefore uses an end-growth or compactification restriction, not just open smoothness and finite energy. This is a constructive witness, not a classification of every metric or physical action.

W47's flat-character table and its canonical-cusp normalizability results remain untouched. Its broader statement that no forcing can exist inside the weave does not follow from an enumeration of flat characters alone. Conversely, this packet does not provide such a forcing. If W47's word “source” denotes end data, those data are still present here; if read as requiring an added singular bulk source, this realization shows why that stronger reading is unwarranted on the modular base.

## Relation to the pole prescription

With the twisted metric, the section Fmod/Delta^n has exactly the norm of a weight-(k0+12n) section Fmod. Positive fractional cusp exponents then give square-integrable modes at the level of this local norm test. Keeping the original metric instead can make the pole non-normalizable. The change is exponential in the original cusp frame, not just a polynomial weight change, so it does not contradict W47's existing normalizability calculation.

This is a specified Hermitian change of description. It does not prove a self-adjoint/Fredholm realization or a four-dimensional Dirac index on the total surface M_1,2, and it does not turn a counted mode into a Standard-Model particle.

## Verification and surviving inputs

The run checks the differential and unitary-gauge curvature formulas, general Mobius metric descent plus its missing chart, elliptic characters over weights -36 through 36, the exact fundamental-region area, the flux and energy identities, the fixed-flux square identity, metric scaling, boundary orientation in Stokes' formula, effective versus stack integration, and the change-of-frame norm with decay controls. Zero-curvature and non-Yang–Mills local controls prevent vacuous success.

The core curvature/energy calculation uses the specified automorphic line and metric directly. Identifying the global Delta frame with W46 remains conditional on HDelta's transformation law, named rather than hidden. Product nonvanishing and leading cusp order are justified in the proof. The source's published modularity is not claimed to have been fully rederived on this bench.

Supplied inputs still include the geometric surface realization, coupling g, metric scale when interpreted physically, end sector, matter coupling and physical dictionary. Pullback to the total four-dimensional surface requires its own metric, action, field equations and domain verification. No Standard-Model parameter, unit selection or gravitational law is derived.

## Seen first

`VERDICT topic-sweep /Petersson metric|Chern connection|cusp.{0,25}unit|unit.{0,25}cusp/: 7 of 1408 arcs on pinned main; 19 other retained lanes match`.

The seven main FINDINGS, B1629's correcting addendum, W45–W47 producers, W27/W48 rules and the relevant physical-branch reports were read. The direct literature reading is Burgos Gil–Menares–Rivera-Letelier, *On the essential minimum of Faltings' height*, pp. 2430–2431, defining the Petersson metric and cusp line; the elementary curvature and variational proof here uses no external noncompact existence theorem. Detailed search/read scope and limitations are in SOURCE_SCOPE.md. No claim that this construction is absent from every historical branch, or mathematically novel, is made.

## Next obligation

Keep FK10 conditional. Before adding a proposed end selector, determine whether the already specified matter operator or its determinant/anomaly line actually requires this tensor power and its nonzero extension. That requires an explicit coupling map and boundary rule, not a match between the integer flux and the desired generation count. The present base solution is a useful ingredient for that test, not its answer.

LAW_MAP_PROPOSALS.md keeps the scoped lemmas visible pending independent review and normal banking. No shared B-number or canonical GENESIS status is changed. The packet is locally committed; the full-suite publication certificate remains pending, so it is not described as pushed.
