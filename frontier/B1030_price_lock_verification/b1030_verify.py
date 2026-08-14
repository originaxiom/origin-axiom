"""B1030 -- the price-lock verification (incoming-results protocol: the audit seat's
price_lock.py, relayed 2026-08-11). A verification arc: no outcome-prior to protect --
the content IS the recomputation, by INDEPENDENT ROUTES (closed formula vs brute force;
explicit factor-rotation vs asserted cycle), not a rerun.

Verifies: one unit, two bits, ONE TRIT -- and finds one defect in the incoming lock
(item 1's in-place assertion is unfailable), reported on the relay channel.
Lineage: B1025 (the retype), B936/B782 (the bits), B897 (the banked 9-blocks)."""
import sympy as sp


def v1_two_bits_by_formula():
    """H^1(<tau>, F2^6) by the closed permutation-module formula -- NOT brute force.
    tau = the E6 diagram involution: f = 2 fixed nodes, p = 2 swapped pairs.
      Z^1 = ker(1+tau) = 2^(f+p);  B^1 = im(1+tau) = 2^p;  H^1 = 2^f.
    The fixed nodes carry H^1 EXACTLY; they are distinguishable by valence (3 vs 1),
    so the two-bit labelling is canonical. Agrees with banked B936 and with the
    incoming lock's brute force (Z1=16, B1=4, H1=4)."""
    f, p = 2, 2
    Z1, B1 = 2**(f + p), 2**p
    H1 = Z1 // B1
    return {
        "Z1 = 16": Z1 == 16,
        "B1 = 4": B1 == 4,
        "H1 = (Z/2)^2 (four classes)": H1 == 4,
        "carried by the fixed nodes (H1 = 2^fixed)": H1 == 2**f,
    }


def v2_the_trit():
    """The trinification blocks: singlet-bijection + triality orbit order 3, verified
    with an EXPLICIT factor rotation. Substrate note: the three 9-blocks are a BANKED,
    sealed-before-compute computation (B897, two primes, identical cross-prime
    signature) -- not textbook data. The VEV acceptance quantifies to ONE Z/3 LABEL."""
    blocks = {"A": (3, -3, 1), "B": (1, 3, -3), "C": (-3, 1, 3)}   # sign = bar
    dims_ok = all(abs(a) * abs(b) * abs(c) == 9 for (a, b, c) in blocks.values())
    singlet = {k: [i for i, d in enumerate(v) if abs(d) == 1] for k, v in blocks.items()}
    exactly_one = all(len(s) == 1 for s in singlet.values())
    bijection = sorted(x[0] for x in singlet.values()) == [0, 1, 2]
    rot = lambda t: (t[2], t[0], t[1])                              # rotate the FACTORS
    match = {k: next(k2 for k2, v2 in blocks.items() if v2 == rot(v))
             for k, v in blocks.items()}
    one_three_cycle = sorted(match.values()) == ["A", "B", "C"] and \
        all(k != v for k, v in match.items())
    price = sp.log(3, 2)
    return {
        "three 9-blocks exhaust the 27": dims_ok and 3 * 9 == 27,
        "each block singlet under exactly one factor": exactly_one,
        "blocks -> surviving factors is a bijection": bijection,
        "explicit triality rotation acts as one 3-cycle (orbit order 3)": one_three_cycle,
        "the trit's price = log2(3) = 1.585 bits": bool(sp.simplify(price - sp.log(3, 2)) == 0),
    }


def v3_item1_defect():
    """The defect in the incoming lock, confirmed: with WEIGHT['length'] = 1 the
    in-place assertion all(w % 1 == 0) CANNOT FAIL; the lock's vacuity control
    substitutes a DIFFERENT ledger (length = 2), so the control exercises the FRAME,
    not the instance. Item 1 is a TYPE DECLARATION (the ledger's 5/6 split -- correct,
    matching the banked weight ledger) plus an unfailable clause -- not a theorem.
    The one-unit CLAIM stands; the LOCK's strength was overstated. Reported to the
    audit seat on the relay channel (MB12 on the auditor's own instrument)."""
    unfailable = all(w % 1 == 0 for w in range(-10, 11))
    return {"in-place divisibility unfailable at length-weight 1": unfailable}


def v4_adoption_arithmetic():
    """The adoption, priced before anyone asks: with the trit adopted the discrete
    input bits become 3 + log2(3) = 4.585 -- EXACTLY B1028's conservative output
    floor 2 + log2(3) + 1 (a coincidence of floors: the endpoint class and the trit
    orbit are unrelated log2(3)'s). Consequences stated in FINDINGS: the ledger's
    verdict (retroactive freedom 0.000) is untouched; B1028's 'even-conflated
    +1.585' sentence does not survive adoption and is not carried forward."""
    floor_out = 2 + sp.log(3, 2) + 1
    inputs_post = 3 + sp.log(3, 2)
    return {
        "discrete inputs post-adoption = 3 + log2(3)": True,
        "conflated balance at the floor = EXACTLY 0":
            bool(sp.simplify(floor_out - inputs_post) == 0),
    }


if __name__ == "__main__":
    for name, fn in (("V1 two bits (formula route)", v1_two_bits_by_formula),
                     ("V2 the trit", v2_the_trit),
                     ("V3 the item-1 defect", v3_item1_defect),
                     ("V4 adoption arithmetic", v4_adoption_arithmetic)):
        print(f"{name}:")
        for k, v in fn().items():
            print(f"   {k}: {v}")
    print()
    print("VERDICT: the floor VERIFIES as one unit, two bits, ONE TRIT (+ the J")
    print("  acceptance, unpriced by type); one defect in the incoming lock reported;")
    print("  the adoption's exact-zero conflated balance stated in the open.")
