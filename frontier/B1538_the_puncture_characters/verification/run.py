#!/usr/bin/env python3
"""B1538 -- THE RUN: the line's supply at the puncture characters of every fibre-direction cover in population A, and the four's
supplies wherever the line could carry two (PREREGISTRATION sections 5-6).

    python3 -u run.py --part L [--workers k] --record    ->  run_L.jsonl   (one row per chunk of a cover; resumable)
    python3 -u run.py --part F --record                  ->  run_F.jsonl   (only if Part L has a candidate)

PART L.  Population A: the states m004 (+LR), m003 (-LR), m136 (+LLRR) and m135 (-LLRR).  Every fibre-direction cover
M_(D,w) with 2 <= |D| <= 12, up to conjugacy.  The fibre characters zeta of order dividing m(C), one per Galois orbit:
  - m(C) = lcm(b, e), e being the exponent of the torsion of the invariant character group, and b the first of 12, 6, 4, 2, 1
    whose count is at most BUDGET Galois orbits;
  - a cover above BUDGET even at b = 1 is listed as not read.
Only the puncture characters are read (the puncture-trivial ones are Lemma W''s, read in the controls).  At each zeta:
  - route W: every root of unity s with h^1(N; (zeta, s)) >= 1, exactly, with h^1, the trivial cusps and n;
  - route P at every root found, at two primes: h^1, the trivial cusps and n must agree with route W;
  - route P at s = 1 and s = -1 at every zeta (a check that route W misses no root there), and at every s in mu_12 at a fixed
    1-in-50 sample of the zeta (crc32 of the cover and zeta);
  - route T at every (zeta, s) with n >= 1 and degree k |D| <= DEG_T: b1(N') - #cusps(N') = the sum over j mod k of
    n(chi^j), each read by route P.
PART F.  At every candidate chi = (zeta, s) of Part L with n(chi) >= 2, at every finite-order nu with nu^4 = chi:
  - nu = (zeta', s'), with zeta' an invariant character with zeta'^4 = zeta and s'^4 = s;
  - routes R and P4 (punct_four) read membership h^1(nu^5 rho), capW and capL2;
  - each candidate first writes a header row with its planned readings (4 per fourth root zeta'), so that the read-out can
    require every one of them (the audit lane's R87).
Every reading records; nothing is asserted on outcomes."""
import json
import sys
import time
import warnings
import zlib
from math import gcd
from multiprocessing import Pool
from pathlib import Path

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import punct_covers as F  # noqa: E402
import punct_present as RP  # noqa: E402
import punct_transfer as T  # noqa: E402
import punct_wang as W  # noqa: E402

STATES_A = ["+LR", "-LR", "+LLRR", "-LLRR"]
NAMES = {"+LR": "m004", "-LR": "m003", "+LLRR": "m136", "-LLRR": "m135"}
DMAX = 12
BUDGET = 300000
DEG_T = 2400
SAMPLE = 50
CHUNK = 20000          # Galois orbits per record at most (orbit_count bounds the puncture orbits from above)


def lcm(a, b):
    return a * b // gcd(a, b)


def phi(m):
    return sum(1 for k in range(1, m + 1) if gcd(k, m) == 1)


def mobius(n):
    r, k = 1, 2
    while k * k <= n:
        if n % k == 0:
            n //= k
            if n % k == 0:
                return 0
            r = -r
        k += 1
    return -r if n > 1 else r


def orbit_count(C, m):
    tot = 0
    for e in range(2, m + 1):
        if m % e == 0:
            tot += sum(mobius(e // f) * C.count_characters(f) for f in range(1, e + 1) if e % f == 0) // phi(e)
    return tot


def modulus(C):
    """m(C) and b, or (None, None) if the cover is above BUDGET even at b = 1"""
    ex = 1
    for t in C.torsion:
        ex = lcm(ex, t)
    for b in (12, 6, 4, 2, 1):
        m = lcm(b, ex)
        if orbit_count(C, m) <= BUDGET:
            return m, b
    return None, None


def population():
    """[(state, lattice, wbar label, cover id)], every cover of population A"""
    out = []
    for sw in STATES_A:
        st = F.State(sw)
        for lat, w in F.covers(st, DMAX):
            out.append((sw, lat, w, f"{NAMES[sw]}.D{lat[0] * lat[2]}.{lat[0]}-{lat[1]}-{lat[2]}.w{w}"))
    return out


def primes(L):
    return RP.primes_1_mod(L, 1 << 30, 2)


def read_cover_L(task):
    sw, lat, w, cid, chunk, nchunks = task
    t0 = time.time()
    st = F.State(sw)
    C = F.Cover(st, lat, w)
    Pr = RP.Presentation(C)
    m, b = modulus(C)
    row = {"cover": cid, "chunk": chunk, "chunks": nchunks, "state": NAMES[sw], "word": sw, **C.summary(), "m": m, "b": b}
    if m is None:
        row["read"] = False
        row["seconds"] = round(time.time() - t0, 1)
        return row
    row["read"] = True
    allreps = sorted(r for r in C.galois_reps(m) if C.is_puncture(r[0], r[1]))
    reps = allreps[chunk::nchunks]
    row["puncture orbits"] = len(reps)
    row["puncture characters"] = sum(o for _, _, o in reps)
    hits, checks_p, checks_t, sample_p = [], {"reads": 0, "disagree": []}, {"reads": 0, "skipped": 0, "disagree": []}, 0
    for ez, mm, osz in reps:
        rw = W.read(C, list(ez), mm)
        roots = rw["rows"]
        found = {}
        for r_ in roots:
            j, k = r_["s"]
            L = r_["L"]
            ezL = [e * (L // mm) % L for e in ez]
            es = j * (L // k) % L
            if (es * 12) % L == 0:                     # s in mu_12: its index there
                found[es * 12 // L] = r_["h1"]
            for p in primes(L):
                rp = RP.read(Pr, ezL, es, L, p)
                checks_p["reads"] += 1
                if (rp["h1"], rp["trivial cusps"], rp["n"]) != (r_["h1"], r_["trivial cusps"], r_["n"]):
                    checks_p["disagree"].append([list(ez), mm, r_["s"], r_, rp, p])
            if r_["n"] >= 1:
                hit = {"zeta": list(ez), "m": mm, "orbit": osz, "s": r_["s"], "h1": r_["h1"],
                       "trivial cusps": r_["trivial cusps"], "n": r_["n"],
                       "puncture values": C.puncture_values(list(ez), mm)}
                # route T: b1(N') - #cusps(N') against the sum of n over the powers (route P)
                _, kchi = T.cover_perms(C, ezL, es, L)
                rt = None
                if kchi * C.d <= DEG_T:
                    try:
                        rt = T.read(C, ezL, es, L)
                    except AssertionError as exc:
                        rt = {"error": str(exc)}
                if rt is not None and "error" not in rt:
                    k_ = rt["k"]
                    tot = 0
                    for jj in range(k_):
                        ezj = [(e * jj) % L for e in ezL]
                        esj = (es * jj) % L
                        tot += RP.read(Pr, ezj, esj, L, primes(L)[0])["n"]
                    checks_t["reads"] += 1
                    hit["transfer"] = {"degree": rt["degree"], "b1 - cusps": rt["n_N'"], "sum n": tot}
                    if rt["n_N'"] != tot:
                        checks_t["disagree"].append([list(ez), mm, r_["s"], rt, tot])
                else:
                    checks_t["skipped"] += 1
                    hit["transfer"] = rt if rt and "error" in rt else "skipped (degree)"
                hits.append(hit)
        # route P where route W found no root: s = 1, -1 always; mu_12 on a fixed sample
        key = zlib.crc32(f"{cid}|{ez}|{mm}".encode())
        ks = range(12) if key % SAMPLE == 0 else (0, 6)
        sample_p += 1 if key % SAMPLE == 0 else 0
        L = lcm(mm, 12)
        ezL = [e * (L // mm) % L for e in ez]
        for kk in ks:
            es = kk * (L // 12)
            want = found.get(kk, 0)
            rp = RP.read(Pr, ezL, es, L, primes(L)[0])
            checks_p["reads"] += 1
            if rp["h1"] != want:
                checks_p["disagree"].append([list(ez), mm, ["mu12", kk], want, rp])
    row["hits"] = hits
    row["max n"] = max([h["n"] for h in hits], default=0)
    row["route P"] = checks_p
    row["route T"] = checks_t
    row["mu12 sample"] = sample_p
    row["seconds"] = round(time.time() - t0, 1)
    return row


def main():
    args = sys.argv[1:]
    part = args[args.index("--part") + 1]
    workers = int(args[args.index("--workers") + 1]) if "--workers" in args else 1
    rec = "--record" in args
    if part == "L":
        out = HERE / "run_L.jsonl"
        done = set()
        if out.exists():
            done = {(r["cover"], r["chunk"]) for r in map(json.loads, out.read_text().splitlines())}
        tasks = []
        for sw, lat, w, cid in population():
            C = F.Cover(F.State(sw), lat, w)
            m, _ = modulus(C)
            size = orbit_count(C, m) if m else 0
            nch = max(1, -(-size // CHUNK))
            tasks += [(size, (sw, lat, w, cid, i, nch)) for i in range(nch) if (cid, i) not in done]
        tasks = [t for _, t in sorted(tasks, key=lambda x: -x[0])]
        print(f"B1538 run, Part L: {len(tasks)} chunks to read ({len(done)} done)", flush=True)
        t0 = time.time()
        with Pool(workers) as pool:
            for row in pool.imap_unordered(read_cover_L, tasks):
                if rec:
                    with open(out, "a") as f:
                        f.write(json.dumps(row) + "\n")
                print(f"{row['cover']} chunk {row['chunk'] + 1}/{row['chunks']}: {row['seconds']} s "
                      f"(total {time.time() - t0:.0f} s)", flush=True)
    else:
        read_part_F(rec)


def read_part_F(rec):
    """Part F: at every candidate of Part L (a puncture chi with n(chi) >= 2), every finite-order nu with nu^4 = chi:
    membership h^1(nu^5 rho) in both routes, and at every member the supplies (capW, capL2) in both routes"""
    import punct_four as FO          # sm:B1536's route_r resets PARI's stack: Part F runs in its own process
    rows_L = [json.loads(line) for line in (HERE / "run_L.jsonl").read_text().splitlines() if line.strip()]
    cands = [(r, h) for r in rows_L if r["read"] for h in r["hits"] if h["n"] >= 2]
    print(f"B1538 run, Part F: {len(cands)} candidates", flush=True)
    out = HERE / "run_F.jsonl"
    for r, h in cands:
        sw = r["word"]
        st = F.State(sw)
        lat = tuple(r["lattice"])
        w = int(r["cover"].rsplit(".w", 1)[1])
        C = F.Cover(st, lat, w)
        rho, _ = FO.exact_four(sw)
        cov = FO.R.PCover(st.G, C.perms)
        Pr = RP.Presentation(C)
        j, k = h["s"]
        roots = C.fourth_roots(h["zeta"], h["m"])
        chi = {"zeta": h["zeta"], "m": h["m"], "s": h["s"], "n": h["n"]}
        head = {"kind": "candidate", "cover": r["cover"], "chi": chi, "fourth roots": len(roots), "planned": 4 * len(roots)}
        if rec:                                              # the read-out requires every planned reading (R87)
            with open(out, "a") as f:
                f.write(json.dumps(head) + "\n")
        for ezp, mp in roots:
            for t in range(4):                               # s' = z_(4k)^(j + k t), s'^4 = z_k^j
                L = lcm(lcm(mp, 4 * k), 24)
                ezL = [e * (L // mp) % L for e in ezp]
                es = (j + k * t) * (L // (4 * k)) % L
                p = RP.primes_1_mod(L, 1 << 30, 1)[0]
                rho_p = FO.four_mod_p(rho, p, L)
                hR = FO.membership_r(C, rho_p, ezL, es, L, p, cov)
                hP = FO.membership_p4(C, rho_p, ezL, es, L, p, Pr)
                row = {"kind": "reading", "cover": r["cover"], "chi": chi,
                       "nu": {"zeta": list(ezp), "m": mp, "s": [j + k * t, 4 * k]}, "prime": p,
                       "h1 R": hR, "h1 P4": hP, "member": hR >= 1 or hP >= 1}
                if row["member"]:
                    row["R"] = FO.supplies_r(C, rho_p, ezL, es, L, p, cov)
                    row["P4"] = FO.supplies_p4(C, rho_p, ezL, es, L, p, Pr)
                if rec:
                    with open(out, "a") as f:
                        f.write(json.dumps(row) + "\n")
    print("Part F done", flush=True)


if __name__ == "__main__":
    main()
