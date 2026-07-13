"""B563 — Campaign 2c: the Planck-ratio bin retry NULLS (chat-2 handoff, re-verified).

The tower's large magnitudes (lambda_n doubly-exponential to ~1e29; |e_n| to ~1e61)
were tested against 10 unit-free Planck ratios, prereg'd NULL. Re-verified here:
  - the object's best |ln ratio| = 0.6825 (|e_4| vs m_Pl/m_mu) -- a factor-~2 miss;
  - it does NOT beat chance (null p ~ 0.5);
  - a plastic-seed growth ladder brushes hierarchy numbers CLOSER than the object.
See frontier/B563_planck_ratio_null/FINDINGS.md.
"""
import math
import random


def _tower(seed, rungs=12):
    lam = seed
    out = [lam]
    for _ in range(rungs):
        lam = lam * (1 + math.sqrt(lam))
        out.append(lam)
    return out


_PHI = (1 + 5 ** 0.5) / 2
_E = [11, 809, 18845089, 228654672055316545291,
      14551745085338356602787456737044854593029948485574326872937769]
_mPl = 1.220890e19
_MASSES = dict(m_e=0.51099895e-3, m_mu=0.1056584, m_tau=1.77686, m_p=0.938272,
               m_W=80.377, m_Z=91.1876, m_H=125.25, m_t=172.69, v=246.22)
_TARGETS = {f"mPl/{k}": _mPl / v for k, v in _MASSES.items()}
_TARGETS["rhoPl/rhoL"] = 1e122


def _best(outputs):
    return min(abs(math.log(o / t)) for o in outputs for t in _TARGETS.values())


def test_object_best_is_e4_vs_mPl_over_mmu():
    obj = _tower(_PHI) + [float(e) for e in _E]
    b = _best(obj)
    assert abs(b - 0.6825) < 1e-3                 # best |ln ratio| = 0.6825
    # the realizing pair is |e_4| vs m_Pl/m_mu (a factor-~2 miss, not a hit)
    pairs = sorted((abs(math.log(o / t)), o, tn)
                   for o in obj for tn, t in _TARGETS.items())
    assert pairs[0][2] == "mPl/m_mu" and abs(pairs[0][1] - float(_E[3])) < 1


def test_object_does_not_beat_chance():
    obj_best = _best(_tower(_PHI) + [float(e) for e in _E])
    rng = random.Random(0)
    N = 500

    def trial():
        s = math.exp(rng.uniform(math.log(1.05), math.log(5.0)))
        analogs = [10 ** rng.uniform(1, 61) for _ in range(5)]
        return _best(_tower(s) + analogs)
    p = sum(1 for _ in range(N) if trial() <= obj_best) / N
    assert p > 0.2                                # NOT significant (~0.5), prereg'd NULL


def test_plastic_ladder_brushes_closer_than_object():
    obj_best = _best(_tower(_PHI) + [float(e) for e in _E])
    plastic = _best(_tower(1.3247179572) + [float(e) for e in _E])
    assert plastic < obj_best                     # random growth-matched ladder is closer
