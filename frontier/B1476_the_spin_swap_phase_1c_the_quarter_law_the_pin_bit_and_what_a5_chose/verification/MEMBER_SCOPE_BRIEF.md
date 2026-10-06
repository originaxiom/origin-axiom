# Reader brief — member scope of every kill (the owner's rule, 2026-10-04)

The record studied one hyperbolic 3-manifold, m004 (the figure-eight knot complement), and later widened its object to a
FAMILY of 112 census manifolds sharing its shape field (and the commensurability class). Many negatives were written as
"the object cannot ..." when the computation was on m004 alone. For each kill, from its text ONLY, decide:
- `member_scope`: M004 (the computation or argument concerns m004 / the figure-eight / 4_1 / its covers or fillings
  only), FAMILY (it concerns the family, the class, several members, or "every member"), GENERAL (it is independent of
  which manifold: a theorem about the construction, a frame, a literature fact, an instrument), UNCLEAR.
- `says_object`: YES if the text phrases its negative as about "the object" / "the object cannot" / "impossible on the
  object" (or equivalent) while `member_scope` is M004; otherwise NO.
- `quote`: at most 15 words verbatim from the text supporting member_scope.
Output a JSON list to the path you are given, in order: {"id":..., "member_scope":..., "says_object":"YES|NO", "quote":...}.
Every entry exactly once; no prose outside the JSON.
