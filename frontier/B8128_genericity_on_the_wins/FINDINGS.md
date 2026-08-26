# B8128 — genericity on the wins

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

THE GENERICITY CONTROL, TURNED ON THE WINS: OF SEVEN ELEMENTARY PROPERTIES EXACTLY ONE SEPARATES
m004 FROM ITS SHAPE-FIELD FAMILY, AND IT IS H_1 = Z. Rebuilt B8118's 14-manifold family (shape
field Q(sqrt-3)) and tabulated volume, tetrahedron count, cusp count, torsion-freeness, H_1 = Z,
amphichirality and CS = 0. SHARED, hence properties of the FAMILY and not of the object: the
volume 2.029883212819307 (with m003 -- so B680's identity Vol = (3sqrt3/2)L(chi_-3,2) is not
m004-specific); the tetrahedron count 2 (with m003); the cusp count (with nine); torsion-
freeness (with m202, m203); AMPHICHIRALITY (with ALL THIRTEEN -- every member is amphichiral);
and CS = 0 (with m203, m206, m208, s595, s596). SEPARATING, hence genuinely the object's: H_1 =
Z EXACTLY -- which is precisely the knot-complement-in-S^3 condition B955 identified as making
rank preservation structural. FOR THE CHAIN: the paper's two manifold-touching steps split
cleanly. Selection I uses H_1, the separating property, so selecting m004 is object-level. The
entrance prop:mod3 uses the TRACE FIELD, which DEFINES the family, so all fourteen members give
the same 2T and the same E6 -- the entrance's input is a FAMILY input. NOT DAMAGING: Selection I
does the separating work before the entrance is reached, and nothing in the paper is
contradicted; but the honest statement is sharper than the paper makes it, and a referee who
runs this census will ask. TWO SELF-CAUGHT BUGS, both found by re-reading the run's own table:
comparing Chern-Simons by FLOAT EQUALITY made m004's 9e-17 differ from other members' 0.0 and
reported CS as the one separator, which it is not; and the first pass tested torsion-freeness
rather than H_1 = Z, conflating m202/m203's Z+Z with m004's Z. Elementary invariants of the 14
orientable cusped census manifolds whose tetrahedron shape field is Q(sqrt-3). Tests which
properties SEPARATE m004. Does NOT test every banked result -- it tests the invariants those
results rest on. Gate 5 untouched.

## Law created

This arc creates a law. **The statement of record is the `B8128` row in `docs/LAW_MAP.md`**, not this file.

## What the arc recorded

### `verdict`

THE GENERICITY CONTROL, TURNED ON THE WINS: OF SEVEN ELEMENTARY PROPERTIES EXACTLY ONE SEPARATES
m004 FROM ITS SHAPE-FIELD FAMILY, AND IT IS H_1 = Z. Rebuilt B8118's 14-manifold family (shape
field Q(sqrt-3)) and tabulated volume, tetrahedron count, cusp count, torsion-freeness, H_1 = Z,
amphichirality and CS = 0. SHARED, hence properties of the FAMILY and not of the object: the
volume 2.029883212819307 (with m003 -- so B680's identity Vol = (3sqrt3/2)L(chi_-3,2) is not
m004-specific); the tetrahedron count 2 (with m003); the cusp count (with nine); torsion-
freeness (with m202, m203); AMPHICHIRALITY (with ALL THIRTEEN -- every member is amphichiral);
and CS = 0 (with m203, m206, m208, s595, s596). SEPARATING, hence genuinely the object's: H_1 =
Z EXACTLY -- which is precisely the knot-complement-in-S^3 condition B955 identified as making
rank preservation structural. FOR THE CHAIN: the paper's two manifold-touching steps split
cleanly. Selection I uses H_1, the separating property, so selecting m004 is object-level. The
entrance prop:mod3 uses the TRACE FIELD, which DEFINES the family, so all fourteen members give
the same 2T and the same E6 -- the entrance's input is a FAMILY input. NOT DAMAGING: Selection I
does the separating work before the entrance is reached, and nothing in the paper is
contradicted; but the honest statement is sharper than the paper makes it, and a referee who
runs this census will ask. TWO SELF-CAUGHT BUGS, both found by re-reading the run's own table:
comparing Chern-Simons by FLOAT EQUALITY made m004's 9e-17 differ from other members' 0.0 and
reported CS as the one separator, which it is not; and the first pass tested torsion-freeness
rather than H_1 = Z, conflating m202/m203's Z+Z with m004's Z.

### `scope`

Elementary invariants of the 14 orientable cusped census manifolds whose tetrahedron shape field
is Q(sqrt-3). Tests which properties SEPARATE m004. Does NOT test every banked result -- it
tests the invariants those results rest on. Gate 5 untouched.

### `self_caught_bugs`

```json
[
 "the first run compared Chern-Simons by FLOAT EQUALITY, so m004's 9e-17 differed from other members' 0.0 and CS was reported as the ONE separating property. It is not: five other family members also have CS = 0. Caught by re-reading the run's own printed table.",
 "the first run tested TORSION-FREENESS, which is not the knot-complement condition. m202 and m203 are torsion-free with H_1 = Z+Z. The condition is H_1 = Z EXACTLY."
]
```

### `method`

vary the manifold within the shape field; a property shared by other members is the family's

### `is_this_damaging`

NO, and the reason is that Selection I has already done the separating work before the entrance
is reached: H_1 = Z picks m004 out of the family, and only then is the trace field used. Nothing
in the paper is contradicted. But the honest statement is sharper than the paper makes it -- the
entrance is a FAMILY entrance -- and a referee who runs this census will ask.

### `what_it_means_for_the_chain`

The paper's chain has two manifold-touching steps. SELECTION uses H_1 -- the one separating
property -- so the selection of m004 is genuinely object-level. THE ENTRANCE (prop:mod3) uses
the TRACE FIELD, which defines the family: all 14 members share it, so all 14 would give the
same 2T and the same E6. The entrance's input is a FAMILY input. The paper already says nothing
after the entrance uses the manifold (rem:consumes); what this adds is that the arithmetic the
entrance consumes is not m004's either.

## Depends on

`B8118`, `B955`, `B680`, `B8111`

## Scope

As recorded above. Nothing in this reconstruction adds a claim the arc did not bank, and where
the arc recorded a limit, a flag or a self-caught error, that text is reproduced rather than
summarised away.
