#!/usr/bin/env python3
"""SM-C11 (P-333): the sealed F-CI read on o10_150729 and the companions' census to word length 10 (card
relays/cards/SM_C11_the-five-ended-companion-in-F-CI.md, pushed before this run).  Main's F-CI cell (B1492's
fci_L8a15.py) is imported unchanged from a checkout of main (first argument) and called by name; companions are written
as triangulation files in a scratch folder (second argument) and read by name.  Main's states() (B1454) gives the states.
    python3 run_c11.py MAIN_CHECKOUT SCRATCH [out.json]"""
import sys, os, json, time, signal, itertools, importlib.util, pathlib, warnings
warnings.filterwarnings("ignore")
import snappy
HERE = pathlib.Path(__file__).resolve().parent
MAIN = pathlib.Path(sys.argv[1]).resolve(); SCR = pathlib.Path(sys.argv[2]).resolve(); SCR.mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(HERE))
import companion as K


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


FCI = load(MAIN / "frontier" / "B1492_the_three_ended_companion_read" / "verification" / "fci_L8a15.py", "fci")
GEN = load(MAIN / "frontier" / "B1454_genesis_v1_verified_and_adopted" / "verification" / "genesis_own.py", "genesis_own")
CAP = 300


class Timeout(Exception): pass


def _alarm(*a): raise Timeout()


def perm_group(perms):
    """closure of a set of permutations (tuples)"""
    n = len(next(iter(perms))); ident = tuple(range(n)); G = {ident}; frontier = [ident]
    gens = list(perms)
    while frontier:
        p = frontier.pop()
        for g in gens:
            q = tuple(g[p[i]] for i in range(n))
            if q not in G: G.add(q); frontier.append(q)
    return G


def parity(p):
    n = len(p); seen = [False] * n; s = 0
    for i in range(n):
        if not seen[i]:
            j, L = i, 0
            while not seen[j]: seen[j] = True; j = p[j]; L += 1
            s += L - 1
    return s % 2


def fci_read(name):
    """main's cell, unchanged, then the reading of its output"""
    os.chdir(SCR); FCI.HERE = SCR
    signal.signal(signal.SIGALRM, _alarm); signal.alarm(CAP)
    try:
        FCI.main(name)
    finally:
        signal.alarm(0)
    d = json.load(open(SCR / f"fci_{name}.json"))
    ends = d["cusps"]; isos = d["isometries"]
    perms = {tuple(r["cusp_images"]) for r in isos if r["orientation"] == "preserving"}
    allp = {tuple(r["cusp_images"]) for r in isos}
    G = perm_group(perms) if perms else set(); Ga = perm_group(allp) if allp else set()
    orbit0 = {p[0] for p in Ga}
    three_ends = sorted({c for r in isos if r["orientation"] == "preserving" for c, v in zip(r["fixed_cusps"], r["det_values"]) if v == 3})
    vals = {}
    for r in isos:
        for v in r["det_values"]: vals[v] = vals.get(v, 0) + 1
    out = {"name": name, "ends": ends, "isometries": len(isos), "chiral": d["summary"]["chiral"],
           "end_group_order_preserving": len(G), "end_group_order_all": len(Ga),
           "end_group_all_even": bool(G) and all(parity(p) == 0 for p in G), "transitive_on_ends": len(orbit0) == ends,
           "cusp_fixing_values": vals, "three": 3 in vals, "ends_with_three": three_ends, "cusp_shapes": d["cusp_shapes"]}
    out["A5_on_ends"] = ends == 5 and len(G) == 60 and out["end_group_all_even"]
    return out


def hexagonal(shape_str):
    """is the cusp shape in the SL(2,Z)-orbit of exp(i pi/3)?"""
    z = complex(shape_str.replace("*I", "j").replace(" ", "")) if "I" in shape_str else complex(shape_str)
    for _ in range(200):
        z = complex(z.real - round(z.real), z.imag)
        if abs(z) < 1 - 1e-12: z = -1 / z
        else: break
    import cmath
    return min(abs(z - cmath.exp(1j * cmath.pi / 3)), abs(z - cmath.exp(2j * cmath.pi / 3))) < 1e-6


def second_path(name):
    """the negative's second computation: cusp maps from symmetry_group().isometries()"""
    M = snappy.Manifold(name); S = M.symmetry_group(); vals = {}
    for iso in S.isometries():
        maps = iso.cusp_maps(); imgs = list(iso.cusp_images())
        d0 = int(maps[0][0][0] * maps[0][1][1] - maps[0][0][1] * maps[0][1][0])
        if d0 == -1: continue
        for i in range(M.num_cusps()):
            if imgs[i] == i:
                X = maps[i]; a, b, c, d = int(X[0][0]), int(X[0][1]), int(X[1][0]), int(X[1][1])
                v = abs((a - 1) * (d - 1) - b * c); vals[v] = vals.get(v, 0) + 1
    p1 = {}
    for iso in S.isometries():
        maps = iso.cusp_maps(); imgs = list(iso.cusp_images())
        for i in range(M.num_cusps()):
            if imgs[i] == i:
                X = maps[i]; v = abs(int(X[0][0]) * int(X[1][1]) - int(X[0][1]) * int(X[1][0])); p1[v] = p1.get(v, 0) + 1
    return {"order": int(S.order()), "cusp_fixing_values": vals, "three": 3 in vals, "P1_values_det_X": p1, "P1_three": 3 in p1}


def main():
    out_path = pathlib.Path(sys.argv[3]) if len(sys.argv) > 3 else HERE / "c11_results.json"
    res = {}
    # controls (E5)
    m003 = snappy.Manifold("m003"); C3, d3 = K.companion(m003)
    lllr = snappy.Manifold("b++LLLR"); C5, d5 = K.companion(lllr)
    res["E5"] = {"m003_companion_is_o10_150729": bool(C3.is_isometric_to(snappy.Manifold("o10_150729"))), "m003_degree": d3,
                 "LLLR_companion_is_L8a15": bool(C5.is_isometric_to(snappy.Manifold("L8a15"))), "LLLR_degree": d5}
    res["E5"]["L8a15_fci"] = fci_read("L8a15")
    # P2: the trivial cover in place of the companion fails the degree check
    res["P2_trivial_cover_degree_fails"] = 1 != abs(2 - K.trace(1, "LLLR"))
    # Part 1
    res["part1"] = fci_read("o10_150729")
    p1 = res["part1"]
    res["E"] = {"E1_A5_on_ends": p1["A5_on_ends"], "E2_three_on_all_five_ends": p1["ends_with_three"] == list(range(5)),
                "E3_hexagonal": None, "E5": res["E5"]["m003_companion_is_o10_150729"] and res["E5"]["LLLR_companion_is_L8a15"]
                and res["E5"]["L8a15_fci"]["isometries"] == 12 and not res["E5"]["L8a15_fci"]["three"]
                and res["E5"]["L8a15_fci"]["end_group_order_all"] == 6}
    res["part1_second_path"] = second_path("o10_150729")
    res["E"]["E3_hexagonal"] = all(hexagonal(x) for x in p1["cusp_shapes"])
    res["part1"]["hexagonal_by_cusp"] = [hexagonal(x) for x in p1["cusp_shapes"]]
    # Part 2: the census
    rows = []; t00 = time.time()
    for n in range(2, 11):
        for w in GEN.states(n):
            for sign in (1, -1):
                tag = ("+" if sign > 0 else "-") + w; tr = K.trace(sign, w); ends = abs(2 - tr)
                row = {"state": tag, "length": n, "trace": tr, "ends": ends}
                try:
                    M = snappy.Manifold("b+%s%s" % ("+" if sign > 0 else "-", w))
                    if ends <= 1:
                        row["companion"] = "the state itself (one fixed point)"; rows.append(row); continue
                    C, deg = K.companion(M)
                    row["degree"] = deg; row["cusps"] = C.num_cusps(); row["degree_check"] = deg == ends == C.num_cusps()
                    nm = "comp_%s.tri" % tag
                    C.save(str(SCR / nm))
                    t0 = time.time(); r = fci_read(nm); row.update({k: r[k] for k in ("isometries", "chiral", "end_group_order_all",
                        "transitive_on_ends", "cusp_fixing_values", "three", "ends_with_three")}); row["seconds"] = round(time.time() - t0, 1)
                except Timeout:
                    row["skipped"] = "over %d s" % CAP
                except Exception as e:
                    row["error"] = str(e)[:200]
                rows.append(row)
                print(json.dumps({k: row.get(k) for k in ("state", "trace", "ends", "degree_check", "isometries", "three", "skipped", "error")}), flush=True)
    res["census"] = rows
    done = [r for r in rows if "three" in r]
    res["summary"] = {"states": len(rows), "companions_read": len(done), "skipped": sum("skipped" in r for r in rows),
                      "errors": sum("error" in r for r in rows), "degree_check_fails": sum(r.get("degree_check") is False for r in rows),
                      "companions_with_three": [r["state"] for r in done if r["three"]],
                      "E4_another_companion_with_three": any(r["three"] for r in done if r["state"] not in ("-LR", "-RL")),
                      "seconds": round(time.time() - t00, 1)}
    json.dump(res, open(out_path, "w"), indent=1, default=str)
    print(json.dumps({"E": res["E"], "part1": res["part1"], "summary": res["summary"]}, indent=1, default=str))


if __name__ == "__main__":
    main()
