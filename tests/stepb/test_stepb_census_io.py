"""The loader on a synthetic census written in the refined census's format (data-free): hashes refused when tampered,
the reading index, the a0/F_-2 duplicate check (and its refusal), the mirror partner."""
import gzip, json, pathlib, sys
import numpy as np
import pytest
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'scripts' / 'stepb')); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import census_io as IO

LABELS = ["".join("S~" if r else "S" for r in (u, d, l)) for u in (0, 1) for d in (0, 1) for l in (0, 1)]


def write_census(tmp, n_lines=2, n_tau=3, seed=0, break_dup=False):
    rng = np.random.default_rng(seed); man = {}
    for li in range(n_lines):
        name = "N02_%d-2_1-2.jsonl.gz" % li
        with gzip.open(tmp / name, "wt", encoding="utf-8") as fh:
            for ti in range(n_tau):
                rows = []
                for d in range(13):
                    for r in range(2):
                        for lab in LABELS:
                            base = rng.random(9) * 0.5 + 0.01
                            rows.append([d, r, lab, sorted(base[0:2].tolist()), sorted(base[2:4].tolist()), sorted(base[4:6].tolist()), base[6:9].tolist(), 1e-5, True])
                # make F_-2 (6) equal a0 (1)
                idx = {(row[0], row[1], row[2]): row for row in rows}
                for r in range(2):
                    for lab in LABELS:
                        a0 = idx[(1, r, lab)]; f = idx[(6, r, lab)]
                        f[3:9] = [list(x) if isinstance(x, list) else x for x in a0[3:9]]
                        if break_dup and r == 0 and lab == "SSS":
                            f[3] = [f[3][0] * 1.5, f[3][1]]
                fh.write(json.dumps({"line": [str(li) + "/2", "1/2"], "order": 2, "tau": [0.1 * ti, 1.0 + ti], "rows": rows}) + "\n")
        man[name] = IO.sha256(tmp / name)
    return man


def test_load_and_shapes(tmp_path):
    man = write_census(tmp_path)
    cen, info = IO.load(tmp_path, man)
    assert info["n_cfg"] == 6 and len(cen.cfg) == 6 * 12 * 2 * 8          # F_-2 dropped: twelve directions
    assert set(np.unique(cen.d)) == set(range(13)) - {6}
    assert info["worst_a0_Fm2_log10"] < 1e-12


def test_tampering_is_refused(tmp_path):
    man = write_census(tmp_path)
    name = sorted(man)[0]; raw = (tmp_path / name).read_bytes()
    (tmp_path / name).write_bytes(raw[:-1] + bytes([raw[-1] ^ 1]))
    with pytest.raises(ValueError):
        IO.load(tmp_path, man)


def test_missing_or_extra_files_are_refused(tmp_path):
    man = write_census(tmp_path)
    with pytest.raises(ValueError):
        IO.load(tmp_path, dict(list(man.items())[:1]))


def test_duplicate_direction_check_can_fail(tmp_path):
    man = write_census(tmp_path, break_dup=True)
    with pytest.raises(ValueError):
        IO.load(tmp_path, man)


def test_reading_index_and_mirror():
    assert [IO.reading_index(l) for l in LABELS] == list(range(8))
    assert IO.reading_index("S~SS") == 4 and IO.reading_index("SSS~") == 1
    from fractions import Fraction as Fr
    assert IO.mirror_partner(IO.line_key("2/5", "1/10")) == IO.line_key("2/5", "9/10")
    assert IO.mirror_partner(IO.line_key("0", "0")) == IO.line_key("0", "0")


def test_compact_loader_matches_and_is_small(tmp_path):
    man = write_census(tmp_path, n_lines=2, n_tau=3)
    cen, info = IO.load(tmp_path, man)
    cc, cinfo = IO.load_compact(tmp_path, man, n_cfg_expected=6)
    import stepb_core as C
    F = C.features(cen)
    assert cc.F.shape == F.shape and np.allclose(cc.F, F.astype(np.float32), atol=1e-6, equal_nan=True)
    assert (cc.d == cen.d).all() and (cc.k == cen.k).all() and (cc.vdef == cen.vdef).all()
    assert cinfo["bytes_per_row"] <= 60


def test_compact_loader_refuses_a_short_census(tmp_path):
    man = write_census(tmp_path, n_lines=2, n_tau=3)
    with pytest.raises(ValueError):
        IO.load_compact(tmp_path, man, n_cfg_expected=7)


def test_compact_loader_keeps_J_signed(tmp_path):
    """the fifth review's N3: the interpolant's tenth coordinate is J signed; the loader must not drop the sign"""
    man = write_census(tmp_path, n_lines=1, n_tau=2)
    for name in list(man):
        recs = [json.loads(l) for l in gzip.open(tmp_path / name, "rt")]
        for rec in recs:
            for i, row in enumerate(rec["rows"]):
                dd = 1 if row[0] == 6 else row[0]                          # F_-2 keeps a0's J (one direction, B1824)
                j = dd * 16 + row[1] * 8 + LABELS.index(row[2])
                row[7] = (-1) ** j * 1e-5 * (1 + 0.01 * j)
        with gzip.open(tmp_path / name, "wt", encoding="utf-8") as fh:
            for rec in recs: fh.write(json.dumps(rec) + "\n")
        man[name] = IO.sha256(tmp_path / name)
    cen, _ = IO.load(tmp_path, man)
    cc, _ = IO.load_compact(tmp_path, man, n_cfg_expected=2)
    assert (np.sign(cc.J) == np.sign(cen.J)).all() and (cc.J < 0).any() and np.allclose(cc.J, cen.J, rtol=1e-6)


def test_dup_rule_agrees_at_the_census_precision_and_refuses_real_disagreements():
    d = IO.dup_disagreement
    assert d(1e-17, 1e-35) == 0.0 and d(0.0, 1e-15) == 0.0                 # structural zeros: roundoff against roundoff
    assert d(1.00008e-11, 1e-11) == 0.0                                    # the precision limit (absolute)
    assert d(0.1, 0.1 * (1 + 2e-7)) == 0.0                                 # the identity's agreement (log10)
    assert d(1.2e-12, 0.9e-12) == 0.0                                      # straddling the floor within the precision
    assert d(0.1, 0.11) > 1e-6                                             # a real disagreement
    assert d(1e-3, 1e-13) == float("inf") and d(0.0, 1e-3) == float("inf") # a physical value against a structural zero
    assert d(1e-6, 1e-6 + 2e-9) > 0                                        # beyond the absolute limit at a small value
