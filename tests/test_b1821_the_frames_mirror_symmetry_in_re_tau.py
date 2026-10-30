"""B1821 -- the frame's mirror symmetry in Re tau: the committed checks show it, and one mirror pair is recomputed here by
the committed evaluator (a planted wrong pairing fails)."""
import json, pathlib, sys
from fractions import Fraction as F
ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1821_the_frames_mirror_symmetry_in_re_tau" / "verification"


def test_the_committed_checks():
    rel = json.loads((V / "sym_check_relative.json").read_text(encoding="utf-8"))["aggregates"]
    assert rel["mirror"]["row_by_row_max_dlog10"] < 1e-5 and rel["mirror"]["row_by_row_degenerate_mismatches"] == 0
    c = json.loads((V / "re_symmetry_check_200.json").read_text(encoding="utf-8"))
    assert c["n"] == 200 and c["all_groups_identical"] == 200 and c["errors"] == 0


def _bag(rows, flip):
    out = {}
    for r in rows:
        vd = r["V defined"]
        v = tuple(round(t, 5) for t in list(r["up"]) + list(r["down"]) + list(r["lepton"]) + (list(r["V"]) if vd else [])) + ((round(-r["J"] if flip else r["J"], 5),) if vd else ())
        out.setdefault((r["direction"], r["radius"]), []).append(v)
    return {k: sorted(v) for k, v in out.items()}


def test_one_mirror_pair_recomputed_and_a_wrong_pairing_fails():
    sys.path.insert(0, str(V)); import cm_zero_line as Z
    a, b, x, y = F(2, 5), F(1, 10), 0.3, 2.5
    A = Z.rows_at(complex(x, y), (a, b)); B = Z.rows_at(complex(-x, y), (a, (-b) % 1)); W = Z.rows_at(complex(-x, y), (a, b))
    assert _bag(A, False) == _bag(B, True)
    assert _bag(A, False) != _bag(W, True)        # the control: the mirror needs the line conjugated too
