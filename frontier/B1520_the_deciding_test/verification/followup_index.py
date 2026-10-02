#!/usr/bin/env python3
"""B1520 -- the handoff's decisive follow-up at the chiral configurations (PREREGISTRATION section 4, F).

At the exceptional points of Ballas' family with the central twist mu = -1 (q0 = 17 +- 12 sqrt2), W1 = [[A, c], [0, 1]] (A = mu rho_q0,
c a generator of H^1(pi; A)) is the rank-five non-split extension that carries main's index I(W1) = -1 (B1509, banked). For each of
the sixteen maps Phi = (sigma, d) of symmetries.json, build Phi(W1) (generators W1(sigma(g)), inverse-transposed when d = 1) and
compute I(Phi(W1)) with this seat's banked index instrument (B1374's index_lib over GF(p), driven as in B1509's extension_index.py:
primes 1009, 1033, 1129, both square roots of 2). The construction of Phi(W1) is new here; the instrument is the banked one.
Expected from L1 and L2: I(Phi(W1)) = -1 for the eight bare maps and +1 for the eight dualised ones.
--controls-only runs the identity alone, bare and dualised: I(W1) = -1 is B1509's banked value and I(W1*) = -I(W1) is the definition
(L2), so neither is an outcome; they check the construction and the instrument's path before the seal.
Usage: python3 followup_index.py [--controls-only]   (writes followup_index.json, or followup_index_controls.json)"""
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
_spec = importlib.util.spec_from_file_location(
    "b1509_extension_index", ROOT / "frontier/B1509_the_join_on_the_projective_vacuum/verification/extension_index.py")
EX = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(EX)
IL = EX.IL
R, MU, LAM = EX.WORD_R, EX.WORD_MU, EX.WORD_L


def representatives():
    sym = json.loads((HERE / "symmetries.json").read_text(encoding="utf-8"))
    return {k: {"m": v["m"], "n": v["n"], "orientation": v["orientation"]} for k, v in sym["representatives"].items()}


def transformed(F, W, sigma, dual):
    mats = {}
    for g in ("m", "n"):
        X = W.word(sigma[g])
        mats[g] = F.T(F.inverse(X)) if dual else X
    return IL.Rep(F, ["m", "n"], mats)


def main():
    controls_only = "--controls-only" in sys.argv
    reps = representatives()
    if controls_only:
        reps = {"id": reps["id"]}
    rows = []
    for p in EX.PRIMES:
        F = IL.GF(p)
        r2 = F.sqrt(2)
        assert r2 * r2 % p == 2
        for s2 in (r2, p - r2):
            q0 = (17 + 12 * s2) % p
            A = IL.Rep(F, ["m", "n"], EX.modp_rep(F, q0, p - 1))
            assert A.check_relators([R])
            c = EX.modp_cocycle(F, A)
            W1 = EX.modp_ext(F, A, c)
            assert W1.check_relators([R])
            base = IL.index(W1, [R], MU, LAM)[0]
            row = {"p": p, "q0 mod p": q0, "I(W1)": base, "I(Phi W1)": {}}
            for name, sig in reps.items():
                for dual in (False, True):
                    V = transformed(F, W1, sig, dual)
                    assert V.check_relators([R]), ("not a representation", name, dual)
                    row["I(Phi W1)"][("D." if dual else "") + name] = IL.index(V, [R], MU, LAM)[0]
            rows.append(row)
    ok = all(r["I(W1)"] == -1 for r in rows) and all(
        v == (1 if k.startswith("D.") else -1) for r in rows for k, v in r["I(Phi W1)"].items())
    banked = all(r["I(W1)"] == -1 for r in rows)
    out = {"maps": sorted(rows[0]["I(Phi W1)"]), "rows": rows,
           "BANKED IDENTITY: I(W1) = -1 at all six prime-root pairs (B1509)": banked,
           "every bare image -1 and every dualised image +1": ok}
    name = "followup_index_controls.json" if controls_only else "followup_index.json"
    (HERE / name).write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
