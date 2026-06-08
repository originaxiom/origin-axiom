# B131 — two-seed gluing creates an internal discrete fork: heterogeneity makes a choice (S032-B)

The arc after B130 (verify-don't-trust, in-sandbox). B130: a single metallic seed is **internally fork-free** (κ free;
deterministic word) — the only discrete fork is the external seed `m`. **S032-B:** does combining two distinct seeds
create an *internal* fork? **Yes — and it is heterogeneity, not multiplicity, that does it.**

`probe.py` verifies:
- **The mechanism** — each seed's boundary data `(κ, trT)` is an A-polynomial curve; gluing matches the curves:
  **same seed → same curve → continuum** (no fork); **distinct seeds → distinct curves → 0-dim intersection** (a
  discrete fork).
- **The A-poly curves**, validated against banked work: m=1 `κ=trT⁴−5trT²+2` (B67), m=2 `κ=trT²−6` (B69/V33); m=3's is
  irrational (B69 double cover). Also re-derived from explicit SL(2,ℂ) matrices here (residual ~1e-14).
- **The forks:** (1,2) **exact** `{−4,−2}`; (1,3) 6 values, (2,3) 4 values (numerical). All κ≠2 → all **irreducible**.
  `κ=−2` (complete-cusp) is shared; the others are genuine.

```
python frontier/B131_two_seed_fork/probe.py
python -m pytest tests/test_b131_two_seed_fork.py -q
```

Exact (1,2) fork + same-seed continuum + irreducibility run unconditionally; the matrix re-derivation is numpy-guarded.

**The reading:** a single seed is a **moduli space** (parametrizes, doesn't choose, B130); two **distinct** seeds glued
create **discreteness** — a choice born from **heterogeneity**. "Minimal multiplicity to become more" = two distinct
seeds. Emergent aperiodic-order / 3-manifold **mathematics**, **not** a physics bridge.

**Tier.** MATH + a firewalled reading (POSTULATED). Resolves `speculations/S032` Target B (YES). Nothing to
`CLAIMS.md`; P1–P16, B85, B124–B130 untouched. See `FINDINGS.md`; ledger **V120**.
