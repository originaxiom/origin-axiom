# Claims as units (GOVERNANCE §14; instituted 2026-07-16)

One file per claim, frontmatter + statement. **Forward rule:** every new
promotion into the layer-1 ledger creates its file here alongside its
`CLAIMS.md` row; existing claims convert opportunistically (lazy backfill,
never big-bang). File creation only — nothing moves (§12). When the
backfill completes, `CLAIMS.md` becomes a generated index over these
files.

## The frontmatter schema

```yaml
id:            P12            # the CLAIMS.md id (P/E/C/D-series)
label:         proven         # GOVERNANCE §3: proven|conditional|open|dead
strength:      THEOREM        # LAW_MAP class where applicable
layer:         1              # GOVERNANCE §13
locks:         [tests/test_gluing_equation.py]
uses:          [P6, P11]      # upstream claims/toolkits this rests on
provenance:    internal       # always internal (PROVENANCE.md §0)
superseded_by: null           # a claim id, for dead/replaced claims
```

The statement body follows the frontmatter, verbatim from the ledger.
Three exemplars accompany this spec: a proven claim with dependencies
(`P15.md`), a proven arithmetic identity (`P12.md`), and a dead claim
showing the terminal state (`D4.md`).
