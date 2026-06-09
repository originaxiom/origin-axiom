# B132 — the quantum layer: SU(2)_k field content, quantum selection criteria, Lee–Yang (CORRECTED by B133)

Internalizes a cross-session "Chat-1" handoff (verify-don't-trust, in-sandbox). The genuinely new content is the
**quantum layer** on the metallic once-punctured-torus bundles: the SU(2)_k WRT data `Z_k`.

> **⚠ CORRECTION (B133):** the original headline "chirality shifts the eigenvalue arithmetic" is **withdrawn** — a
> sampling artifact. The field content is **quantum-group arithmetic** (word spin-content mod 4), present in achiral
> words too (control: achiral `RRLL`→ℚ(ζ₁₂), `RRRLLL`→ℚ(√−3), `RLRLRL`→ℚ span all three). S7 + S5 withdrawn; tombstone
> `K-H`, guard `MB6`. See `knowledge/K015`.

**One-line (corrected):** the SU(2)_k eigenvalue **field content is quantum-group arithmetic** (word composition mod 4),
**not** chirality. The robust facts are single-seed: the figure-eight (m=1) is the unique perfectly coherent seed
(`|Z_k|=1`; `Z_{k=4}=ω`), vanishing period `=|O_K^×|/2`, two scales by m mod 4; plus the Lee–Yang σ₃ bridge.

`probe.py` verifies (validated convention: `R=T`, `L=STS⁻¹`, framing-free `T`; eigenvalue-order method, exact):
- **S1c** field content m=1..7 (m≡2 mod 4 → ℚ(i) content — quantum-group, m mod 4); **S7 [corrected]** the control —
  achiral words span all three fields (field is composition, not chirality); **S1a** `Z_{k=4}(M_1)=ω`; **S3a**
  pure-phase m=1-unique; **S2** vanishing period `=|O_K^×|/2` (m=1→3, m=2→2, non-arith irregular); **S4** two scales by
  m mod 4; **S5 [corrected]** vanishing is composition not chirality; **S6** silver↔L5a1; **S8** the Lee–Yang σ₃.
- **Quarantined:** S9 (RRL κ-degree=3) did **not** reproduce (got 1/2, not 3) — not banked.

```
python frontier/B132_quantum_layer/probe.py
python -m pytest tests/test_b132_quantum_layer.py -q
```

**Reconciliation:** the handoff was stale (pre-B130/B131). Its "KEY" Step 17 (two-seed fork) = the already-merged
**B131**; this quantum field-fusion is its **companion** (classical fork ↔ quantum fusion). Renumbered to
B132/K015,K016/P009/V121.

**Tier.** MATH (quantum topology) + a firewalled physics reading (POSTULATED; native physics = Lee–Yang, S030). Naming
`knowledge/K015` + `K016`; `philosophy/P009` (Monadic Closure synthesis, *not* a theorem — the seven closures reduce to
~3 root causes). Nothing to `CLAIMS.md`; P1–P16, B85, S031, B124–B131 untouched. See `FINDINGS.md`; ledger **V121**.
