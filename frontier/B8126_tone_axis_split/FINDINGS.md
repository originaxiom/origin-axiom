# B8126 — tone axis split

**Arc dated:** 2026-08-22 · **Seat:** cc3 (audit) · **Lane:** MATHEMATICS.
**Gate 5:** no physical identification claimed in this arc.

> **RECONSTRUCTED 2026-08-26 from this arc's own banked record** (`arc_verdict.json`
> and `results.json`). **This seat stopped writing `FINDINGS.md` at B8110 and the
> omission ran unbroken through B8134 — sixteen arcs.** It went uncaught because the
> lock that detects it lives in a suite too slow to finish inside a session. **This
> document is faithful to the banked record but is NOT contemporaneous, and is marked
> so rather than backdated.**

## Verdict

**PROVED**

THE PAULI COMPONENTS SPLIT AGAINST THE TONE MENU, TRANSVERSELY TO THE LAW. cc's generalized
golden-meridian law h(R^2L^2,u) = -phi h(RL,u) - i phi n_y(u) is correct and its real part still
reduces to the identity phi*(1/(2phi)) = 1/2, so B8124's scoping point survives the
generalization: the tone component carries no golden content in either form. THE NEW FINDING: of
the four Pauli components, {tone, wy} land EXACTLY on B8111's five-tone 2I menu and {wx, wz}
land nowhere near it -- while the law's own structure splits them the other way, since {tone,
wx, wz} scale by -phi and wy does not, wy being exactly the component forcing the -i phi n_y
correction. Two exact structures on four numbers, transverse to each other. AND THE GOLDEN-
SPECIFIC CONTENT SITS IN wy: by B8111 only phi/2 and 1/(2phi) discriminate 2I from 2T and 2O,
and wy hits both of them (phi/2 -> 1/(2phi)) while tone hits one discriminating then one generic
(1/(2phi) -> 1/2). So the component the law must treat specially is the one carrying the golden
signature. PROCESS: third false negative of the day in the same class -- a 1e-25 tolerance
against 18-digit literals reported every menu member as a miss; caught by a positive control now
embedded in the check. Reads four already-computed Pauli components against B8111's menu and
against cc's law. Computes nothing new about the listener map and does not re-derive B1132,
whose verdict is untouched. The menu identifications are exact to the precision of the quoted
components (1e-15). Gate 5 untouched.

## Law created

This arc creates a law. **The statement of record is the `B8126` row in `docs/LAW_MAP.md`**, not this file.

## What the arc recorded

### `verdict`

THE PAULI COMPONENTS SPLIT AGAINST THE TONE MENU, TRANSVERSELY TO THE LAW. cc's generalized
golden-meridian law h(R^2L^2,u) = -phi h(RL,u) - i phi n_y(u) is correct and its real part still
reduces to the identity phi*(1/(2phi)) = 1/2, so B8124's scoping point survives the
generalization: the tone component carries no golden content in either form. THE NEW FINDING: of
the four Pauli components, {tone, wy} land EXACTLY on B8111's five-tone 2I menu and {wx, wz}
land nowhere near it -- while the law's own structure splits them the other way, since {tone,
wx, wz} scale by -phi and wy does not, wy being exactly the component forcing the -i phi n_y
correction. Two exact structures on four numbers, transverse to each other. AND THE GOLDEN-
SPECIFIC CONTENT SITS IN wy: by B8111 only phi/2 and 1/(2phi) discriminate 2I from 2T and 2O,
and wy hits both of them (phi/2 -> 1/(2phi)) while tone hits one discriminating then one generic
(1/(2phi) -> 1/2). So the component the law must treat specially is the one carrying the golden
signature. PROCESS: third false negative of the day in the same class -- a 1e-25 tolerance
against 18-digit literals reported every menu member as a miss; caught by a positive control now
embedded in the check.

### `scope`

Reads four already-computed Pauli components against B8111's menu and against cc's law. Computes
nothing new about the listener map and does not re-derive B1132, whose verdict is untouched. The
menu identifications are exact to the precision of the quoted components (1e-15). Gate 5
untouched.

### `and_the_discriminating_half`

By B8111's measurement only phi/2 and 1/(2phi) are golden-DISCRIMINATING; {0, 1/2, 1} are shared
by 2T, 2O and 2I alike. wy hits BOTH discriminating entries (phi/2 -> 1/(2phi)). tone hits one
discriminating entry then one generic one (1/(2phi) -> 1/2). So the golden-specific content sits
in wy -- precisely the component the law cannot scale.

### `context`

cc's B1132 generalized the phi-law to the full CP^1_odd: h(R^2L^2,u) = -phi h(RL,u) - i phi
n_y(u), banked as LAW_MAP + registry T-GOLDEN-MERIDIAN. B8124 had recommended SCOPING the
earlier real-circle version instead.

### `does_my_sharpening_survive`

YES. n_y is REAL (pauli_decompose returns all four components real for this M), so the -i phi
n_y term is purely imaginary and contributes nothing to the real part. The real part of the
GENERAL law therefore still reads tone(R^2L^2) = -phi tone(RL), and with tone(RL) = 1/(2phi) and
tone(R^2L^2) = -1/2 that is the identity phi*(1/(2phi)) = 1/2, true for any phi. The tone
component of the banked law carries no golden content even in its general form.

### `process_note`

THIRD FALSE NEGATIVE OF THE DAY, SAME CLASS. The first run of this check used a 1e-25 tolerance
against 18-digit decimal literals and reported EVERY menu member as a miss and every -phi ratio
as 'NOT -phi'. A tolerance tighter than the input precision manufactures a negative. Caught by a
positive control -- recognising 1/(2phi) itself -- which is now in the script.

### `recommendation`

The T-GOLDEN-MERIDIAN row is right to be general, and B8124's scoping point still applies to its
real part. Suggest the row carry one clause: that the real part reduces to phi*(1/(2phi)) = 1/2
and so is an identity, with the content in the imaginary part and the n_y correction. And
suggest the (tone,wy)-vs-(wx,wz) menu split be recorded -- it is free, it is exact, and it was
invisible until B8111's menu existed to test against.

### `the_new_finding`

THE FOUR PAULI COMPONENTS SPLIT CLEANLY AGAINST B8111'S TONE MENU, AND NOBODY HAS NOTICED.
{tone, wy} land EXACTLY on the five-tone 2I menu; {wx, wz} do not, at all.

### `why_it_matters`

The split is EXACTLY the split in the law's own structure. The three components that scale by
-phi are {tone, wx, wz}; the one that does NOT, and that forces the extra -i phi n_y correction
term, is wy. And the menu membership cuts the OTHER way: {tone, wy} are menu members, {wx, wz}
are not. So the component the law had to treat specially (wy) is a menu member, and the
components that scale cleanly are not. Those are two independent structures on the same four
numbers, and they are transverse.

## Depends on

`B8111`, `B8124`

## Scope

As recorded above. Nothing in this reconstruction adds a claim the arc did not bank, and where
the arc recorded a limit, a flag or a self-caught error, that text is reproduced rather than
summarised away.
