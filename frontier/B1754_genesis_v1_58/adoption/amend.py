#!/usr/bin/env python3
"""B1754 -- GENESIS v1.57 (main's) -> v1.58 (main's): the ladder's rule in the three seats' merged wording, at the owner's
ruling on P-385 (the SM seat's relay §271, carrying the web seat's and the audit lane's opinions): the rungs are the moves'
quotients by T^N, not every finite quotient; the container a composition requirement adopted by ruling; R2 recorded with
its hypothesis.  Every status cell unchanged.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.58 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_57_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_57 = "ebd39a7bd854f3d76b6d27ee39e68a987a11995ac176bc86d332571658a3871b"
CHANGES = [
 ("**Version 1.57 · 2026-10-24 · canonical.**", "**Version 1.58 · 2026-10-24 · canonical.**"),
 ("every finite rung of the moves' ladder at once — the end at 5 follows from the moves' orders 2 and 3 (W153), and E₈ "
  "as the single container of the rungs is adopted by the ruling, not derived ([v1.57] the web seat's correction of "
  "main's clause, P-379: the rungs' groups form no chain, so the container is a choice of rule); the rule fixes the "
  "algebra, not its embedding or its fields (FK11)",
  "every finite rung of the moves' ladder at once — [v1.58] the rungs are the moves' quotients by T^N, "
  "Γ/⟨⟨T^N⟩⟩ = Δ(2, 3, N), finite exactly for N = 2, 3, 4, 5, the end at 5 forced by the moves' orders 2 and 3 (W153; "
  "not every finite quotient of the moves: PSL(2, 𝔽₇) is a quotient of the infinite Δ(2, 3, 7)); the container, the "
  "least single simple algebra holding every rung's finite diagram, E₈, is a composition requirement adopted by the "
  "ruling, not derived, and the prime 5 enters with it ([v1.57] the web seat's correction of main's clause, P-379: the "
  "rungs' groups form no chain, so the container is a choice of rule; [v1.58] the three seats' merged wording, P-385); "
  "the rule fixes the algebra, not its embedding or its fields (FK11); R2 (invariance under every move) selects a "
  "unimodular lattice only for one scalar holomorphic theta series — for any even lattice (Im τ)^{r/2} Σ∣Θ_μ∣² is "
  "invariant — so the joint action would have to earn a chiral lattice before R2 could pay for an input"),
 ("- **v1.57 · 2026-10-24 · main B1752.**",
  "- **v1.58 · 2026-10-24 · main B1754.** The ladder's rule in the three seats' merged wording at the owner's ruling on "
  "P-385 (the SM seat's relay §271): the rungs are the quotients by T^N, not every finite quotient; the container a "
  "composition requirement adopted by ruling; R2 recorded with its hypothesis. No status cell changes; the v1.57 entry "
  "below is not rewritten.\n"
  "- **v1.57 · 2026-10-24 · main B1752.**"),
]


def build():
    src = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(src.encode("utf-8")).hexdigest() == SHA_V1_57, "the received v1.57 is not the pinned one"
    out = src
    for old, new in CHANGES:
        assert out.count(old) == 1, ("anchor not unique", old[:70], out.count(old))
        out = out.replace(old, new)
    return out


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.58 · 2026-10-24 · canonical.**" in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written (v1.58)")
