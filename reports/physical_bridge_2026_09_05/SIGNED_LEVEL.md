# R78 — signed powers were lost at the state/level interface

October 2, 2026. Sealed, pushed and server-confirmed at
`64a96ea6d81d651a95341dfb8f4aee8d76ea11b4` before execution.
**Reconstruction defect verified; named geometry certified.** This is a
path-local audit publication, not a fully banked B-arc or physical theory.

## The concrete correction

Put A=LR=[[2,1],[1,1]]. The signed word -LRLR gives U=-A²,
not the cyclic double cover of -LR. The latter has monodromy
(-A)²=+A². Their traces (-7,+7) and homology differ.

| monodromy | certified census carrier | exact H1 |
|---|---|---|
| A² | m206 | Z + C5 |
| -A² | m207 | Z + C3 + C3 |
| A⁴=(-A²)² | t12839 | Z + C3 + C15 |

Each is complete, orientable and one-cusped. Hyperbolicity passed interval
checks at both 100 and 160 bits, on all three bundle triangulations and
all three named census triangulations. Each named identification was
verified by equality of complete-cusped isometry signatures: respectively
`eLMkbcdddhxqdu`, `eLMkbcdddhxqlm`, `iLMzMPcbcdefghhhhxqqxhhep`.
identify() alone was not treated as certification. Method reference:
[SnapPy verification documentation](https://snappy.computop.org/verify.html).
Sage 10.7, SnapPy 3.3.2; a Sage version deprecation warning is preserved.

The exact common-cover relation is not inferred from matching fields or
volumes: U²=A⁴. Thus m207 and m206 have the same degree-two cyclic cover
t12839 under the assumed once-punctured-torus realization. This does not
say m207 is a cyclic cover of m004. The authored matrix-power proof in
[the frozen proof](SIGNED_LEVEL_PROOF.md) shows U has no proper root in
GL(2,Z). Its independent analytic review remains pending.

## What was wrong, exactly

B1516 C9 at commit e1bc9c36 reduces B to eps A(w), extracts the primitive
UNSIGNED root w=u^k, and labels B as level k of (eps,u). But that level
has (eps A(u))^k=eps^k A(u)^k, rather than eps A(u)^k. Negative sign
and even k are silently changed. C9 checks the first conjugacy, not this
second reconstruction.

Replaying its preserved byte-identical producer reproduces C9's success
on all 168 hyperbolic SL(2,Z) matrices in entries [-5,5]. Adding the
reconstruction predicate finds four failures, all negative trace-seven
matrices with even unsigned exponent two. They are four matrix entries
of this window, NOT four new inequivalent manifolds or a universal count.
U is one of them. The correction is not to reject C9's positive-word
factorization: it is to withdraw that factorization's untested promotion
to a signed primitive-seed/ordinary-level decomposition.

There is no workaround by a different primitive seed. S3's matrix-root
proof rules out levels >=2. S4's trace >= word length+1 proof bounds every
possible unsigned trace-seven representative by length six. Exhaustive
enumeration has two cyclic/swap classes: LLLLLR (primitive, negative
homology C9) and LRLR (nonprimitive unsigned word, negative homology
C3+C3). Homology rules out level-one primitive representatives even up
to GL conjugacy. This proof combines an all-length bound with a finite
complete window; it is not a finite search claimed to be universal.

## Preserve what was already achieved

The 758 signed-primitive-positive-word census at lengths 2..12 replays
unchanged. B1434/B1439 explicitly use that family and ordinary cyclic
levels; their scoped numerical/coefficient conclusions are not refuted
by this audit. They do not exhaust the full signed word grammar by the
primitive-root argument in C9.

**m207 was already in the record.** SM B1385 §2 S4 explicitly lists
±(LR)² as m206/m207. Main B1418's class census has m207, its H1, one
cusp and the reported amphichiral/non-three frame outcomes. B1224 also
lists it in the amphichiral CS census, with its numerical/certification
caveat. These source bodies/selected record were read, not their full
scientific probes rerun. We recover a lost interface, not claim a new
manifold, a global omission or a new chirality breakthrough. In particular
m207 does not evade the one-cusp b1=1 free-cusp obstruction in that frame.

For U, all nine C3-valued fibre characters are fixed, eight nontrivial;
the positive double-cover control fixes only zero modulo three. This
is exact potential coefficient data native to this member. It is not
three generations, an E6/E8 representation, a nonsplit module, a selected
vacuum or a physical spectrum. None of those was computed here.

## Repair without choosing another root

Use (u,k,eps) to mean eps A(u)^k, keeping the sign after the unsigned
power. A cyclic cover of degree n is then (u,kn,eps^n). Alternatively
admit signed-power-primitive seeds, including negative even unsigned
powers. 3,328 exact finite cover-identity controls pass on the preregistered
window. No canonical form up to every mapping-class conjugacy is proved.
Signing is conditional on its legality; the audit cannot turn the
positive monoid into an inverse-closed group without a stated premise.

This correction retains the LR positive minimum and SE1's conditional
selector. It does not select m207 or widen a physical model covertly.
GENESIS v1 should distinguish its complete conditional grammar from the
758-family experiment, and test reconstruction after each reduction.

## Execution and mission status

[Receipts](SIGNED_LEVEL_RECEIPTS.json) preserve the first exact run, full
geometric stdout and both test invocations. The first test command failed
BEFORE collection because Apple's system Python has no pytest. Unchanged
tests via the installed pytest environment then passed **14/14**. No
science file was repaired; all seven frozen hashes and HEAD remained
unchanged. No full scientific-suite-green or independent review claim.
Older governance/raw-custody debts are not cured by these new receipts.

The first publication-governance pass also caught a table header and two
new law-map rows without the required prior-arc reference. Their source
contexts were added explicitly as CONTEXT/audit target, not attributed
as the authors of the new proof. That failed output is retained; no
frozen science path changed. Final governance status is recorded with
[publication checks](SIGNED_LEVEL_PUBLICATION_CHECKS.json), not advertised
as a fully green bank. Final staged pass: 26 gates PASS, four existing
categories FAIL (attribution, test-vacuity, seal-provenance, relay-debt).
All 19 source pins, seven frozen science paths, four embedded science/test
captures and 1,150 then-latest artifact digests match. Review is due;
the source-core drafts are excluded. These are bounded custody checks,
not proof acceptance or permission to merge through failing bank gates.

The latest SM currency commit 6da934c0 changes headlines/docs, not this
producer or GENESIS specification. Other branches are untouched.
The [sender relay](relays/CODEX_TO_CC_AND_SM_2026-10-02_SIGNED_LEVEL_R78.md)
requests review and propagation; recipient acknowledgement is pending.

Next reconcile legal signed closure and the state/level schema, then
continue the faithful-F2/carrier dependency audit. The new positive
coefficient data must not be promoted to physics without the SAME
coefficient, admissible background, action, operator domain and
interaction/source construction. Full Standard Model/TOE remains ACTIVE
and unachieved; R77 drafts remain unsealed/unrun.
