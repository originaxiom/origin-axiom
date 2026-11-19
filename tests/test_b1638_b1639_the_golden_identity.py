"""B1638 and B1639 -- the golden identity sum_p g_p(tau) g_p(N tau) = 8 (g_p = (theta_p/eta)^2, N = [[-1,-2],[2,-1]]) and its
derivation from Ramanujan's degree-5 modular equation.  Sealed instruments unchanged; the stored results; live: the
factorisation N = G1 diag(5,1) G2 with G1, G2 in Gamma(2); the identity at two points; bite controls: the axis matrix of
L^2 R^2 gives a non-constant sum, and a swapped matching is not 8."""
import hashlib, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
A8 = ROOT / "frontier" / "B1638_the_golden_identity"
A9 = ROOT / "frontier" / "B1639_the_golden_identity_from_ramanujans_quintic"


def _sealed(arc, name, sha):
    first = open(arc / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith(f"# sealed at {sha}")
    assert hashlib.sha256(open(arc / "verification" / name, "rb").read()).hexdigest() == first.split()[4]


def test_sealed_and_stored():
    _sealed(A8, "golden_identity.py", "2401dab14")
    _sealed(A9, "golden_from_ramanujan.py", "081a02663")
    d = json.load(open(A8 / "verification" / "golden_identity.json"))
    assert d["I1"]["max_abs_H_minus_8"] < 1e-40 and d["I5"]["max_F_minus_8"] < 1e-40
    assert all(v > 1e-3 for v in d["I2"].values()) and all(v["spread"] > 1e-3 for v in d["I3"].values())
    assert all(v["max_abs_H_minus_8"] < 1e-40 for v in d["I4"].values())
    r = json.load(open(A9 / "verification" / "golden_from_ramanujan.json"))
    assert r["R1"]["count_both_in_Gamma2"] > 0 and r["R2_max_residual"] < 1e-40 and r["R3_max_relative_residual"] < 1e-40
    assert json.load(open(A9 / "arc_verdict.json"))["verdict"] == "PROVED"


def test_the_factorisation():
    mul = lambda A, B: [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    G1, D, G2 = [[1, 4], [4, 17]], [[5, 0], [0, 1]], [[-5, -6], [6, 7]]
    assert mul(mul(G1, D), G2) == [[-1, -2], [2, -1]]
    for G in (G1, G2):
        assert G[0][0] * G[1][1] - G[0][1] * G[1][0] == 1 and [x % 2 for r in G for x in r] == [1, 0, 0, 1]


def test_the_identity_live_and_its_bite():
    import mpmath as mp
    mp.mp.dps = 30
    def g(t):
        e = lambda x: mp.exp(1j * mp.pi * t * x)
        th = (mp.fsum(e((n + mp.mpf(1) / 2) ** 2) for n in range(-40, 40)), mp.fsum(e(n * n) for n in range(-40, 41)),
              mp.fsum((-1) ** abs(n) * e(n * n) for n in range(-40, 41)))
        eta = mp.exp(1j * mp.pi * t / 12) * mp.fprod(1 - mp.exp(2j * mp.pi * t * n) for n in range(1, 300))
        return [(x / eta) ** 2 for x in th]
    mob = lambda M, t: (M[0][0] * t + M[0][1]) / (M[1][0] * t + M[1][1])
    N = [[-1, -2], [2, -1]]
    for t in (mp.mpc(0.21, 0.88), mp.mpc(-0.37, 1.6)):
        a, b = g(t), g(mob(N, t))
        assert abs(mp.fsum(x * y for x, y in zip(a, b)) - 8) < 1e-20
        assert abs(a[0] * b[1] + a[1] * b[0] + a[2] * b[2] - 8) > 1e-3        # a swapped matching is not 8
    # L^2 R^2 = [[5, 2], [2, 1]]: N_M = [[d - a, -2b], [2c, d - a]] = [[-4, -4], [4, -4]]; its sum is not constant
    NM = [[-4, -4], [4, -4]]
    vals = [mp.fsum(x * y for x, y in zip(g(t), g(mob(NM, t)))) for t in (mp.mpc(0.21, 0.88), mp.mpc(-0.37, 1.6))]
    assert abs(vals[0] - vals[1]) > 1e-3



def test_the_discriminants_to_100_p031():
    """P-031 (2026-11-19): every primitive class of the ruled branch with discriminant <= 100, at weights 1, 2 and 4 --
    only LR at weight 2 is constant; the committed run is read here (it takes minutes) and its rows are held"""
    import json, pathlib
    V = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1638_the_golden_identity" / "verification"
    run = (V / "discriminants_to_100_run.txt").read_text(); rows = json.loads((V / "discriminants_to_100.json").read_text())
    assert "classes: 22 (discriminants [5, 12, 21, 32, 45, 60, 77, 96])" in run and "constant (spread < 1e-20): [('LR', 5, 2)]" in run
    assert len(rows) == 22 and sum(1 for r in rows for k in (1, 2, 4) if r["spread_k%d" % k] < 1e-20) == 1
    assert {r["disc"] for r in rows if r["content"] == 1} == {5, 21, 45, 77}
    lr = next(r for r in rows if r["word"] == "LR"); assert lr["spread_k2"] < 1e-25 and lr["spread_k1"] > 1e-3 and lr["spread_k4"] > 1e-3
