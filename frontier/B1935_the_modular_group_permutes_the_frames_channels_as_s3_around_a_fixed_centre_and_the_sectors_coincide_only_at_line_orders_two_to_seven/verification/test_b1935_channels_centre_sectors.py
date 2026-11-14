"""B1935's lock: T and S permute the frame's channels i, j, k (fixing 1) by the transpositions found, and a wrong
permutation fails; the centre keeps every reading; the Higgs triplet's T-phases are eighth roots, not fifth; the sector
coincidence table is as kept. It writes nothing."""
import sys, math, pathlib, subprocess, itertools
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import channels_and_centre as CC
import higgs_triplet_level as HT


def _spread(perm, R0, R1):
    d = [math.log(abs(R1[s]) / abs(R0[p])) for s, p in zip(CC.CH, perm)]
    return max(d) - min(d)


def test_t_and_s_permute_the_channels_around_a_fixed_centre():
    t, (a, b) = complex(0.17, 1.31), (1 / 7, 3 / 7)
    for sec in CC.SECT:
        R0 = CC.res(a * t + b, t, sec)
        RT = CC.res(a * t + b, t + 1, sec); RS = CC.res((a * t + b) / t, -1 / t, sec)
        assert _spread(("1", "i", "k", "j"), R0, RT) < 1e-12 and _spread(("1", "j", "i", "k"), R0, RS) < 1e-12
        assert _spread(("1", "i", "j", "k"), R0, RT) > 1e-3                    # planted: T as the identity on the channels
        assert _spread(("i", "1", "j", "k"), R0, RS) > 1e-3                    # planted: the centre moved


def test_the_higgs_triplet_is_level_eight_not_five():
    assert all(abs(8 * x - round(8 * x)) < 1e-9 for x in HT.PH)
    assert not all(abs(5 * x - round(5 * x)) < 1e-9 for x in HT.PH)


def test_the_sector_coincidences_are_as_kept():
    out = subprocess.run([sys.executable, "-B", str(HERE / "sector_coincidences.py")], capture_output=True, text=True).stdout
    assert out == (HERE / "sector_coincidences_run.txt").read_text()
    assert "down  vs lep   transposed          at N in [5]" in out and "up    vs lep   negated+transposed  at N in [7]" in out
