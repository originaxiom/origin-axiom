"""B1539 -- the population, as structure (nothing twisted is computed here).

The covers: sm:B1536's covers of degree <= 12 of m004 and m003 (its banked post_run_rooms.json) where both supplies already live
at the trivial character (n(1) >= 1 and n(rho) >= 1), and those where the four alone has two (n(rho) >= 2): 30 covers.
The characters: every own character of order dividing m(cover), m = 60 on the covers of degree 5 and 9 and 6 on degree 10, one
representative per Galois orbit (Lemma C), read in routes R' and P'.  The sample: every member of the orbits whose
representative's crc32 is 0 mod SAMPLE (Lemma C's check, P2).

    python3 population.py      -> the manifest, by cover (about 30 s)"""
import json
import sys
import zlib
from pathlib import Path

HERE = Path(__file__).resolve().parent

def _sib(alias, name):
    """this arc's own modules, by path under unique names (E12: sm:B1536's route_r puts sm:B1535's folder, with its own
    read_out.py and controls.py, first on sys.path, and sm:B1536's has its own population.py and run.py)"""
    import importlib.util
    if alias not in sys.modules:
        spec = importlib.util.spec_from_file_location(alias, HERE / name)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[alias] = mod
        spec.loader.exec_module(mod)
    return sys.modules[alias]


O = _sib("b1539_own_chars", "own_chars.py")

POP = O._load("b1539_b1536_population", O.B1536V / "population.py")
SAMPLE = 100


def members():
    """[(state, cover, degree, n(1), n(rho), cusps)], m004 first, then by degree and name"""
    rooms = json.loads((O.B1536V / "post_run_rooms.json").read_text())
    out = []
    for st in ("m004", "m003"):
        for x in rooms[st]["trivial character supplies"]:
            if (x["n(1)"] >= 1 and x["n(rho)"] >= 1) or x["n(rho)"] >= 2:
                out.append((st, x["cover"], x["degree"], x["n(1)"], x["n(rho)"], x["cusps"]))
    return sorted(out, key=lambda r: (r[0] != "m004", r[2], r[1]))


def modulus(deg):
    return 60 if deg in (5, 9) else 6


def sampled(st, cid, rep):
    return zlib.crc32(f"{st}:{cid}:{','.join(map(str, rep))}".encode()) % SAMPLE == 0


_STATES = {}


def cover(st, cid):
    """(state, perms, PCover, Ab) of a member"""
    if st not in _STATES:
        S = O.CL.state(st)
        _STATES[st] = (S, dict(POP.covers(S)))
    S, covs = _STATES[st]
    perms = covs[cid]
    cov = O.R.PCover(S["G"], perms)
    return S, perms, cov, O.Ab(cov)


def manifest():
    """{"state:cover": {degree, m, H_1, characters, orbits, orbits by order, sampled orbits, sampled characters}}"""
    out = {}
    for st, cid, deg, n1, nr, cus in members():
        S, perms, cov, ab = cover(st, cid)
        m = modulus(deg)
        reps = O.orbit_reps(ab, m)
        by = {}
        for _, _, k in reps:
            by[k] = by.get(k, 0) + 1
        smp = [(c, s) for c, s, _ in reps if sampled(st, cid, c)]
        out[f"{st}:{cid}"] = {"degree": deg, "cusps": cus, "n(1)": n1, "n(rho)": nr, "m": m,
                              "H_1": {"free": len(ab.free), "torsion": [d for _, d in ab.torsion]},
                              "characters": sum(s for _, s, _ in reps), "orbits": len(reps),
                              "orbits by order": {str(k): v for k, v in sorted(by.items())},
                              "sampled orbits": len(smp), "sampled characters": sum(s for _, s in smp)}
    return out


def main():
    man = manifest()
    tot = {"covers": len(man)}
    for k in ("characters", "orbits", "sampled orbits", "sampled characters"):
        tot[k] = sum(v[k] for v in man.values())
    for key, v in man.items():
        print(f"{key}: degree {v['degree']}, (n(1), n(rho)) = ({v['n(1)']}, {v['n(rho)']}), H_1 = Z^{v['H_1']['free']} + "
              f"{v['H_1']['torsion']}, m = {v['m']}: {v['characters']} characters in {v['orbits']} orbits "
              f"{v['orbits by order']}; sampled {v['sampled orbits']} orbits ({v['sampled characters']} characters)")
    print(json.dumps(tot))
    return man, tot


if __name__ == "__main__":
    main()
