# Main's review of P210's code and check design (read-only reviewer, 2026-10-27; static, the package not run)
VERDICT: ACCEPT WITH NAMED CAVEATS — no blocking defect; every re-derived assertion holds; the wrapper is fail-closed.
- Custody: SPECIFICATION.json f3334814…f948 at 39ce620a8; all 39 pins and the design identical at the seal and the head
  8a4fdc411; SEAL_LEDGER rows for the design and specification on the audit branch, not on origin/main — run from an
  audit-branch fresh clone with origin/main fetched.
- What P210 asks: DESIGN.md (lines 18-22) says some checks cannot fail for correct code (instrument verification); none of
  the ten can select a domain; P-210 stays open whatever the outcome.
- The ten methods (checks.py at 39ce620a8; definitions and expected values typed in, matched by eye to the sources):
  (1) Y = -2 I3 correct, controls M = I2 and M = eps fire; no dagger control (dagger gives diag(-2, 2, 2)).
  (2) commutant dimension 9 a real computation; basis/rank assertions by construction.
  (3) nullness and unitarity hold for any Hermitian h; b = U a by definition; the wrong-graph control works.
  (4) cannot fire where it matters: Gamma-commutation holds for any block-diagonal 12x12; counts are binomial bookkeeping;
      Q8 preservation never asserted.
  (5) discriminating: joined rank 6 against 12.
  (6) covariance for any unitary g, |alpha| = 1 (fails for non-unitary SL(2,C)); the family permutation decorative; the
      frozen-state rejection checks a constant; the lifts' source note (COHERENT_WORD_LIFTS_AND_LOCAL_BOUNDARY.md) not pinned.
  (7) the projector built from the direction; the shared symmetric endpoint never asserted.
  (8) the sign of the sigma-2 K term not discriminated (+sigma-2 K passes every assertion).
  (9) the decay orientation hard-coded by index parity, not derived from (8); flipping the sigma-2 sign moves the decaying
      mode from PLUS to MINUS; the source's promised controls (wrong Green sign, wrong orientation, omitted MINUS) absent.
  (10) the conjugation identity holds for any weight; the spin-connection term typed in; the wrong-exponent control fires;
      the bump ratio 12 correct.
- Wrapper and gates: the P210 run_checks.py hash-checks the frozen v3 runner and rebinds HERE, ENTRY, EXPECTED; the runner
  checks runtime, environment and versions, strict tracked state, the exact command and output set, the pins before import,
  the exact test population, a strict pass, custody before and after; no bypass found. Caveats: tracked_state.py is imported
  before any pin is checked (hash the wrapper chain externally); untracked or ignored files are invisible to it and the script
  directory is on sys.path (run from a fresh clone); prospective.py checks independence only as strings and booleans (main's
  acceptance is what makes it real); failfast stops at the first failure (the log keeps the traceback).
- The lane's own review (523821858): its algebra correct; it overstated the orientation checks ("consistent", both slots
  "retained"), called the weight "the true cusp weight", argued a dagger control the code lacks, said S_t tends to I where the
  code asserts nothing, and did not flag the unpinned lift source; its independence self-attested.
