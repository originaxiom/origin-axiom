"""The null's charge assignments for the twisted-units comparison (DESIGN_DRAFT.md): pure algebra, no mass.

Gauge-invariant integer 6Y assignments (Q, u, d, L, e, H) with Q.u^c.H, Q.d^c.Hbar and L.e^c.Hbar neutral:
  H = -(Q + u), d = H - Q, e = H - L;   free: Q, u, L;   box: every |q| <= 12.
Each sector's coupling vector twist (B1656): ubar = (qL + qR) w, delta = (qL - qR) w; on an order-N line only the
residues mod N matter. B1656's residue c_s theta_s(ubar) theta_s(delta) is even or odd in each argument and symmetric
under ubar <-> delta, so two sectors' coupling vectors agree (up to per-channel signs and a common factor) when
{+-ubar, +-delta} agree mod N as unordered pairs of classes up to sign.
Eligible at N (the SM's terms there): the three sectors split (no two agree), no sector untwisted (ubar, delta not
both 0 mod N), and no field's charge = 0 mod N (revised before the seal of PREREGISTRATION_TWISTED_UNITS.md: in the
per-field reading a matter field with charge = 0 mod N has an exact zero, since R = FM12[1], E4F[1] = E4 R and R.R = 0;
the Standard Model has no such field at N = 9, 11 or 12). Box |q| <= 18 (was 12, which left only 132 such draws). Excluded: the SM, its negative, and any draw equal to k.SM mod N for a unit k mod N, at N = 9, 11 or 12.
The order is a fixed shuffle (seed below); the seal takes the first M eligible draws.

Check (also pure algebra): the SM's own eligibility by order must reproduce relay §126's table.
Usage: python3 null_draws.py > null_draws_run.txt  (writes null_draws.json beside itself)
"""
import json, math, pathlib, random

SEED = 20261015
BOX = 18
ORDERS = (9, 11, 12)
SM = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6, "H": 3}
FIELDS = ("Q", "u", "d", "L", "e", "H")
SECT = {"up": ("Q", "u"), "down": ("Q", "d"), "lepton": ("L", "e")}


def twists(ch, N):
    out = {}
    for s, (l, r) in SECT.items():
        ub, de = (ch[l] + ch[r]) % N, (ch[l] - ch[r]) % N
        cls = lambda x: min(x % N, (-x) % N)
        out[s] = tuple(sorted((cls(ub), cls(de))))
    return out


def status(ch, N):
    t = twists(ch, N)
    coinc = [f"{a}={b}" for a, b in (("up", "down"), ("down", "lepton"), ("up", "lepton")) if t[a] == t[b]]
    untw = [s for s in t if t[s] == (0, 0)]
    null_id = [s for s, (l, r) in SECT.items() if (ch[l] - ch[r]) % N == 0]   # delta in the lattice: identity channel zero
    return {"split": not coinc, "coincidences": coinc, "untwisted": untw, "identity channel null": null_id}


def eligible(ch, N):
    st = status(ch, N)
    return st["split"] and not st["untwisted"] and all(v % N for v in ch.values())


def is_unit_multiple_of_SM(ch, N):
    for k in range(1, N):
        if math.gcd(k, N) == 1 and all((ch[f] - k * SM[f]) % N == 0 for f in FIELDS):
            return k
    return None


if __name__ == "__main__":
    print("The SM's own status by order (compare relay §126):")
    for N in range(2, 14):
        st = status(SM, N)
        print(f"  N = {N:2d}: split {st['split']}, coincidences {st['coincidences']}, untwisted {st['untwisted']}, "
              f"identity channel null {st['identity channel null']}")
    pool, excluded_equiv, ineligible = [], 0, 0
    for Q in range(-BOX, BOX + 1):
        for u in range(-BOX, BOX + 1):
            for L in range(-BOX, BOX + 1):
                H = -(Q + u); d = H - Q; e = H - L
                ch = {"Q": Q, "u": u, "d": d, "L": L, "e": e, "H": H}
                if any(abs(v) > BOX for v in ch.values()):
                    continue
                if ch == SM or all(ch[f] == -SM[f] for f in FIELDS):
                    continue
                if any(is_unit_multiple_of_SM(ch, N) for N in ORDERS):
                    excluded_equiv += 1; continue
                if not all(eligible(ch, N) for N in ORDERS):
                    ineligible += 1; continue
                pool.append(ch)
    rng = random.Random(SEED)
    rng.shuffle(pool)
    print(f"box |q| <= {BOX}: eligible at N = 9, 11 and 12: {len(pool)}; excluded as k.SM mod N: {excluded_equiv}; "
          f"ineligible at some N: {ineligible}")
    print("first five draws in the fixed order:", pool[:5])
    print("identity-channel-null patterns among the first 199 (N = 9, 11, 12):")
    pat = {}
    for ch in pool[:199]:
        key = tuple(tuple(status(ch, N)["identity channel null"]) for N in ORDERS)
        pat[key] = pat.get(key, 0) + 1
    for k, v in sorted(pat.items(), key=lambda kv: -kv[1]):
        print(f"  {k}: {v}")
    print("the SM's pattern:", tuple(tuple(status(SM, N)["identity channel null"]) for N in ORDERS))
    out = {"seed": SEED, "box": BOX, "orders": ORDERS, "eligible": len(pool), "excluded_equivalent": excluded_equiv,
           "ineligible": ineligible, "draws_in_order": pool}
    (pathlib.Path(__file__).resolve().parent / "null_draws.json").write_text(json.dumps(out, indent=0) + "\n")
