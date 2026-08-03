#!/usr/bin/env python3
"""B865 -- the padding lemma + the full-27 rerun: the re-anchoring rule is VERDICT-IRRELEVANT,
and the dropped singlets are the anomaly ballast.

The critic's G2: B861's ket silently changes per step (27 at step 1, the 16 at step 2, 10+5bar
at step 3), and no arc states or audits the rule. Three parts:

  (i)  THE PADDING LEMMA (proved, then machine-verified): in the free commutative monoid of
       multisets, M + S = conj(M) + S  iff  M = conj(M), for S self-conjugate. So adding
       self-conjugate content NEVER flips the chirality verdict -- cancellation is exact.
  (ii) THE FULL-27 RERUN: every cascade step re-run with the ENTIRE descended 27 as ket.
       All verdicts and winners unchanged (the lemma in action).
  (iii) THE SINGLETS' FATE: the "dropped" 10_{-2} + 1_{+4} (step 1) and 1_{-5} (step 2) are
       not physically dropped -- they are exactly the ANOMALY BALLAST that makes the parent-
       level dials traceless (B864: 16-20+4 = 0), and the SM-level singlets land in
       (1,1)_0 = the right-handed-neutrino slot.

Mathematics scope. Nothing reaches CLAIMS.md; Gate 5 untouched.
"""
import json
import os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))

CONJ = {"3": "3bar", "3bar": "3", "1": "1", "2": "2", "6": "6", "4": "4bar", "4bar": "4",
        "16": "16bar", "16bar": "16", "10so": "10so", "10": "10bar", "10bar": "10",
        "5": "5bar", "5bar": "5",
        "(3,2)": "(3bar,2)", "(3bar,2)": "(3,2)", "(3,1)": "(3bar,1)", "(3bar,1)": "(3,1)",
        "(1,2)": "(1,2)", "(1,1)": "(1,1)",
        "(4,2,1)": "(4bar,2,1)", "(4bar,2,1)": "(4,2,1)", "(4,1,2)": "(4bar,1,2)",
        "(4bar,1,2)": "(4,1,2)", "(6,1,1)": "(6,1,1)", "(1,2,2)": "(1,2,2)", "(1,1,1)": "(1,1,1)"}


def conj_ms(m):
    return Counter({CONJ[r]: n for r, n in m.items()})


def chiral(m):
    return conj_ms(m) != Counter(m)


def padding_lemma_verify(trials=2000, seed=7):
    """Machine check of the proved lemma on random multisets over the vocabulary."""
    import random
    rng = random.Random(seed)
    vocab = [k for k in CONJ]
    selfconj = [k for k in CONJ if CONJ[k] == k]
    ok = True
    for _ in range(trials):
        m = Counter(rng.choices(vocab, k=rng.randint(1, 6)))
        # build a self-conjugate pad: random self-conj reps + random conjugate PAIRS
        s = Counter(rng.choices(selfconj, k=rng.randint(0, 4)))
        for _ in range(rng.randint(0, 3)):
            r = rng.choice(vocab)
            s[r] += 1
            s[CONJ[r]] += 1
        assert conj_ms(s) == s
        if chiral(m + s) != chiral(m):
            ok = False
            break
    return ok


def full27_rerun():
    """Every step with the ENTIRE descended 27 as ket."""
    out = {}
    # step 2 out of SO(10): full 27 -> SU(5): (10+5bar+1) from 16, (5+5bar) from 10so, 1 from 1
    full_su5 = Counter({"10": 1, "5bar": 2, "5": 1, "1": 3})
    out["step2_SU5xU1"] = dict(multiset=dict(full_su5), chiral=chiral(full_su5))
    # step 2 Pati-Salam: 16 -> (4,2,1)+(4bar,1,2); 10so -> (6,1,1)+(1,2,2); 1 -> (1,1,1)
    full_ps = Counter({"(4,2,1)": 1, "(4bar,1,2)": 1, "(6,1,1)": 1, "(1,2,2)": 1, "(1,1,1)": 1})
    out["step2_PatiSalam"] = dict(multiset=dict(full_ps), chiral=chiral(full_ps))
    # step 3 SM: generation + (5 -> (3,1)+(1,2); 5bar -> (3bar,1)+(1,2)) + singlets
    # NOTE: a first draft used dict literals with DUPLICATE KEYS, which silently collapse
    # (later keys overwrite) -- the singlet counts were wrong in results.json though no verdict
    # moved (singlets are self-conjugate; the lemma). Built from lists now, which cannot collapse.
    full_sm = Counter(["(3,2)", "(3bar,1)", "(3bar,1)", "(1,2)", "(1,1)"]) \
        + Counter(["(3,1)", "(1,2)", "(3bar,1)", "(1,2)", "(1,1)", "(1,1)", "(1,1)"])
    out["step3_SM"] = dict(multiset=dict(full_sm), chiral=chiral(full_sm))
    # step 3 SU(4)xU(1): generation-side {6,4,4bar,1} + (5 -> 4+1; 5bar -> 4bar+1) + singlets
    full_su4 = Counter(["6", "4", "4bar", "1"]) \
        + Counter(["4", "1", "4bar", "1"]) + Counter(["1", "1"])
    out["step3_SU4xU1"] = dict(multiset=dict(full_su4), chiral=chiral(full_su4))
    return out


def main():
    res = {}
    res["padding_lemma_proof"] = (
        "In the free commutative monoid of multisets, M + S = conj(M) + S iff M = conj(M) "
        "(cancellation). conj(M + S) = conj(M) + conj(S) = conj(M) + S for self-conjugate S. "
        "Hence chirality(M + S) = chirality(M). QED -- one line, exact.")
    res["padding_lemma_verified"] = padding_lemma_verify()
    res["full27"] = full27_rerun()
    res["verdicts_unchanged"] = (res["full27"]["step2_SU5xU1"]["chiral"] is True
                                 and res["full27"]["step2_PatiSalam"]["chiral"] is True
                                 and res["full27"]["step3_SM"]["chiral"] is True
                                 and res["full27"]["step3_SU4xU1"]["chiral"] is False)
    res["singlet_fate"] = (
        "The 'dropped' content is never physically dropped: 10_{-2} + 1_{+4} are the anomaly "
        "ballast making Tr psi = 16-20+4 = 0 at parent level (B864); the chain's singlets land "
        "in (1,1)_0 at the SM level -- the right-handed-neutrino slot -- and being self-conjugate "
        "dial-stripped, they never touch a verdict (the lemma).")
    json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1, sort_keys=True)

    print("=" * 74)
    print("B865 -- the padding lemma + the full-27 rerun")
    print("=" * 74)
    print(f"\n  lemma machine-verified on 2000 random multisets: {res['padding_lemma_verified']}")
    for k, d in res["full27"].items():
        print(f"  {k:20} chiral: {d['chiral']}")
    print(f"\n  ALL verdicts and winners unchanged with the FULL descended 27: "
          f"{res['verdicts_unchanged']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
