"""B598-P0 — the C1 baseline (locks): the Kashaev 1-loop constant is 3^(-1/4).

See frontier/B598_l85_campaign/FINDINGS.md.
"""
import mpmath as mp
import pytest

# E12 (module-level-dps sweep): the VOL literal is an IMPORT-TIME constant that
# needs dps=30; compute it under a save/restore so the collection-time import
# no longer leaks dps=30 into later-collected modules.
_saved_dps = mp.mp.dps
mp.mp.dps = 30
VOL = mp.mpf("2.029883212819307250042405108549")
mp.mp.dps = _saved_dps


@pytest.fixture(autouse=True)
def _dps_30():
    # E12 repair (the b204 pattern): both locks compute the Kashaev sum at
    # RUNTIME with 1e-25/1e-8 tolerances; pin the dps=30 they were banked at,
    # per test, instead of trusting the collection-time global to survive.
    saved = mp.mp.dps
    mp.mp.dps = 30
    yield
    mp.mp.dps = saved


def _kashaev(N):
    s = mp.mpf(0)
    p = mp.mpf(1)
    for k in range(0, N):
        if k > 0:
            p *= 4 * mp.sin(mp.pi * k / N) ** 2
        s += p
    return s


def test_growth_rate_is_volume():
    N = 400
    v = _kashaev(N)
    r = v * mp.e ** (-N * VOL / (2 * mp.pi)) / mp.mpf(N) ** mp.mpf(1.5)
    corrected = (mp.log(v) - mp.mpf(1.5) * mp.log(N) - mp.log(r)) / N
    assert abs(corrected - VOL / (2 * mp.pi)) < 1e-25


def test_one_loop_constant_is_3_to_minus_quarter():
    rs = []
    for N in (100, 200, 400, 800):
        v = _kashaev(N)
        rs.append(v * mp.e ** (-N * VOL / (2 * mp.pi)) / mp.mpf(N) ** mp.mpf(1.5))
    out = list(rs)
    fac = 2
    while len(out) > 1:
        out = [(fac * b - a) / (fac - 1) for a, b in zip(out, out[1:])]
        fac *= 2
    assert abs(out[0] - 3 ** mp.mpf(-0.25)) < 1e-8   # 4-pt Richardson; competitor 0.18 away
