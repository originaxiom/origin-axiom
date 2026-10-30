"""The mirror symmetry of the rigid census's frame, checked on 200 random configurations (data-free; REFINED_CENSUS_PLAN § 2):
outputs at (-x + iy, line (a, -b)) against those at (x + iy, (a, b)), as multisets over the eight readings within each
(direction, radius) group, J -> -J, the mixing dropped where the census marks it undefined.  Seed 7300; Im tau 0.9-4.0,
Re tau 0.01-0.49.  Writes re_symmetry_check_200.json."""
# B1821 (2026-10-30): committed from the audit room as the census's instrument; the only change is the import path, set to this folder.
import json, os, pathlib, random, sys
from multiprocessing import Pool
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


def check(arg):
    import cm_zero_line as Z
    N, a, b, x, y = arg
    from fractions import Fraction as F
    a, b = F(a), F(b)
    try:
        A = Z.rows_at(complex(x, y), (a, b)); B = Z.rows_at(complex(-x, y), (a, (-b) % 1))
    except Exception as ex:
        return [N, str(a), str(b), x, y, "error", repr(ex)[:80]]
    def bag(rows, flip):
        out = {}
        for r in rows:
            vd = r["V defined"]
            v = tuple(round(t, 5) for t in list(r["up"]) + list(r["down"]) + list(r["lepton"]) + (list(r["V"]) if vd else [])) + ((round(-r["J"] if flip else r["J"], 5),) if vd else ()) + (vd,)
            out.setdefault((r["direction"], r["radius"]), []).append(v)
        return {k: sorted(v) for k, v in out.items()}
    ba, bb = bag(A, False), bag(B, True)
    return [N, str(a), str(b), x, y, sum(1 for k in ba if ba[k] == bb.get(k)), len(ba)]


if __name__ == "__main__":
    import rigid_census_full_menu as M
    rnd = random.Random(7300)
    jobs = [(m[0], str(m[1]), str(m[2]), round(rnd.uniform(0.01, 0.49), 3), round(rnd.uniform(0.9, 4.0), 3)) for m in (rnd.choice(M.MENU) for _ in range(200))]
    with Pool(int(os.environ.get("RC_WORKERS", "8"))) as P:
        res = P.map(check, jobs, chunksize=1)
    ok = sum(1 for r in res if r[5] != "error" and r[5] == r[6]); err = sum(1 for r in res if r[5] == "error")
    (HERE / "re_symmetry_check_200.json").write_text(json.dumps({"seed": 7300, "n": len(res), "all_groups_identical": ok, "errors": err, "rows": res}, indent=1), encoding="utf-8")
    print("200 random configurations: all 26 groups identical under the mirror in", ok, "| errors", err, "| not identical", [r for r in res if r[5] != "error" and r[5] != r[6]][:5])
