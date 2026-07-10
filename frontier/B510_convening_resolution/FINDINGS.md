# B510 — THE CONVENING RESOLVED: 40a3 IS the Jacobian of 40a1's branch cover (verified, corrected)
**Twelfth handoff verified by this seat (2026-07-11). The flag is DISCHARGED as a theorem.**
- **Repo model confirmed:** y²=x(x−1)(x−5) is Cremona **40a1**, j=148176/25 ✓ (the handoff's model
  correction §5 validated; no downstream damage).
- **THE MECHANISM, verified in corrected form:** the genus-1 double cover **d²=(c²−1)(c²−5)** — the
  square-time condition, whose quartic IS 40a1's branch polynomial — has Jacobian **exactly 40a3**
  (classical I,J invariants → minimal model → isomorphism True). The square-time question is a
  covering question about the character variety; the Rationality Theorem is a statement about that
  cover's rational points; the three arithmetic ends are the branch points {0,1,5}.
- **CORRECTION to the handoff (sixth caught error of the arc):** 40a3 is **NOT a quadratic twist**
  of 40a1 — twists preserve j, and j differs (148176/25 vs 55296/5); no small-d twist exists
  (scanned). The correct statement: **40a3 = Jac(the branch double-cover), 2-isogenous to 40a1**
  (three prime-2 isogenies in class 40a). The structural reading SURVIVES and is cleaner: the
  object's curve governs square time through its covering geometry, not through a twist.
- **Verdict:** neither signal nor coincidence — a THEOREM. The unification sentence is earned at
  covering-geometry level: the program's two independently-found elliptic curves are the character
  variety and the Jacobian of its own branch cover. The 283-airlock remains armed and independent.
  Lock: tests/test_b509.py extended.
