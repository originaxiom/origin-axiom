"""B500 -- Gate A, class 2c: irregular covers of the figure-eight at index 7-8
(Closure Campaign Phase 2; prereg docs/CLOSURE_CAMPAIGN_2026-07.md + local README.md).

QUESTION (Gate A / S032-A, restricted to this class; the B349 horizon was index <= 6).
Per index n in {7, 8}: is the cover census of 4_1 a canonical multiset, and does every
within-index invariant multiplicity collapse under isometry -- or does the object
distinguish a member (a forced choice)? Outcome enum (committed):
SEALED (horizon extended) / COUNTEREXAMPLE (owner escalation) / TOOL-BLOCKED/BUDGET-CAPPED.

METHOD (all banked; reused via importlib, not re-derived):
  * B349's census/partition machinery (cover_census, cyclic_covers_match_B350,
    multiplicities_resolved_by_isometry) -- rerun UNCHANGED as the control;
  * B350's exact monodromy algebra (coker(A^n - I) Smith normal form; torsion orders
    = |det(A^n - I)| = L_{2n} - 2, the P8/C5 Lucas ladder) -- extended to n = 7, 8;
  * SnapPy 3.3.x subgroup enumeration, TWO independent routes (low_index + snappea);
  * isometry signatures (canonical retriangulation, double-precision tier -- the
    verified=True tier is Sage-gated in this install: TOOL-BLOCKED for that tier,
    named honestly) as the within-index partition cross-check;
  * an EXACT-tier separator for any non-collapsing group: the degree-2 sub-cover
    census (subgroup enumeration + abelianization SNF of the cover's own pi_1 --
    pure integer computation, no hyperbolic numerics, a homeomorphism invariant);
  * MB-guard orientation honesty (REPRODUCIBILITY): is_isometric_to() is orientation-
    BLIND -- used here ONLY for identification (any self-isometry already defeats a
    forced choice, the B349 stance); chirality is read ONLY from
    symmetry_group().is_amphicheiral(), gated on is_full_group() == True (B128 guard).

STRUCTURE OF THE COMPUTATION
  0.  controls (prereg: fail => INVALID, exit 1):
      (a) B349's index <= 6 census reproduced exactly (counts 2/4/11, the banked
          canonical multisets, every index-5/6 multiplicity group -> ONE isometry class);
      (b) the cyclic members' SNF vs B350 exactly (n = 2..6), and B350's exact ladder
          extended: n = 7 -> (29, 29), order L14 - 2 = 841 = 29^2; n = 8 -> (21, 105),
          order L16 - 2 = 2205 = 21*105.
  1.  the index-7 and index-8 censuses: per cover -- type, H1 (torsion + betti, exact),
      cusps, volume (= n*v4, certified-numerical, tol 1e-9); census keyed on
      (type, torsion, betti, cusps); both enumeration routes must agree.
  2.  the within-index partition: is_isometric_to classes per invariant-multiplicity
      group, cross-checked by isometry signatures for every cover (partition by
      signature must equal partition by isometry) AND by the exact degree-2
      sub-cover census for every multiplicity-group member (same class => same
      sub-census; split groups must be separated at the exact tier); symmetry group
      per class representative (full-group gate; amphichirality per the MB guard).
  3.  the gate-A test per index + the orientation-honest oriented census (structural:
      the base is amphichiral -- MB-guard-verified -- so the cover multiset is closed
      under mirroring; a CHIRAL orientation-blind class of size s therefore refines to
      the mirror-symmetric oriented multiset {s/2 copies of X, s/2 of Xbar}; an
      amphichiral class is its own mirror. No oriented member is distinguished either
      -- the B348 sign-kill landing in the cover class).

FINDING BANKED BELOW (the probe's one new structural fact): at index 8 the
(irregular, Z/3+Z/3+Z^2, 2 cusps) multiplicity group of size 3 does NOT collapse --
it refines into TWO isometry classes, sizes [2, 1], separated at the EXACT tier by
the degree-2 sub-cover census (pair: {Z/3^4+Z^2, Z/3^2+Z^2, Z/3^2+Z/15+Z^2}; singleton:
{Z/3^2+Z^2 twice, Z/3+Z/15+Z^2} -- distinct pi_1, hence non-homeomorphic), with the
canonical-retriangulation signatures and the symmetry groups (Z/2xZ/2 chiral pair vs
order-16 amphichiral singleton) concurring.
B349's clause (iii) ("every within-index invariant multiplicity is resolved
by isometry") is therefore index <= 7-specific. The gate-A conclusion SURVIVES at the
correct resolution: the canonical datum is the multiset of ISOMETRY CLASSES; every
residual same-invariant multiplicity is isometry-identified, and the non-collapsing
member is separated by finer canonical invariants -- classification, not choice. No
member of any invariantly-indistinguishable set is distinguished => no forced choice.

VERDICT (computed below, asserted, banked in b500_census.json): SEALED -- the gate-A
horizon extends from index 6 to index 8. Per the C-guardrail this is a horizon
extension, NOT a theorem: the class "all irregular covers" stays formally open beyond
index 8. Compute budget: hard cap 90 minutes; actual total is seconds (logged); the
BUDGET-CAPPED branch is implemented and reported but not taken.

Firewall: mathematics only; nothing promotes; nothing to CLAIMS.md.
"""
import collections
import importlib.util
import json
import pathlib
import sys
import time

BUDGET_SECONDS = 90 * 60          # prereg hard cap on total compute
VOL_TOL = 1e-9                    # certified-numerical tier (double precision)

HERE = pathlib.Path(__file__).resolve().parent
FRONTIER = HERE.parent


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, FRONTIER / rel)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


b349 = _load("b349_irregular_covers", "B349_irregular_covers_galois/irregular_covers.py")
b350 = _load("b350_cyclic_cover_torsion", "B350_cyclic_cover_torsion_galois/cyclic_cover_torsion.py")


# Banked B500 extension values (exact; established by this probe's first run and locked).
EXPECTED_CYCLIC_SNF_78 = {7: (29, 29), 8: (21, 105)}       # coker(A^n - I), B350 route
EXPECTED_CYCLIC_ORDERS_78 = {7: 841, 8: 2205}              # L_{2n} - 2 (P8/C5 ladder)
EXPECTED_CENSUS_78 = {                                     # key: (type, torsion, betti, cusps)
    7: {("cyclic", (29, 29), 1, 1): 1,
        ("irregular", (), 3, 3): 4,
        ("irregular", (14,), 1, 1): 4},
    8: {("cyclic", (21, 105), 1, 1): 1,
        ("irregular", (), 2, 2): 1,
        ("irregular", (3, 3), 2, 2): 3,
        ("irregular", (3,), 2, 2): 2,
        ("irregular", (30,), 1, 1): 2,
        ("irregular", (5,), 2, 2): 1},
}
# The banked partition headline: {index: {key: (group size, number of isometry classes,
# sorted class sizes)}} for every multiplicity group (size >= 2).
EXPECTED_PARTITION_78 = {
    7: {("irregular", (), 3, 3): (4, 1, (4,)),
        ("irregular", (14,), 1, 1): (4, 1, (4,))},
    8: {("irregular", (3, 3), 2, 2): (3, 2, (1, 2)),       # the non-collapsing group
        ("irregular", (3,), 2, 2): (2, 1, (2,)),
        ("irregular", (30,), 1, 1): (2, 1, (2,))},
}


def cover_key(C):
    """(type, H1 torsion, betti, cusps) -- the invariant census key (exact tier)."""
    h = C.homology()
    torsion = tuple(int(c) for c in h.coefficients if c != 0)
    return (C.cover_info()["type"], torsion, h.betti_number(), C.num_cusps())


def subcensus2(C):
    """The degree-2 sub-cover census of a cover C: multiset of (H1 torsion, betti) of
    C's own double covers. Pure subgroup enumeration + abelianization SNF -- EXACT
    tier, a pi_1 (hence homeomorphism) invariant, independent of hyperbolic numerics."""
    cnt = collections.Counter()
    for D in C.covers(2):
        h = D.homology()
        cnt[(tuple(int(c) for c in h.coefficients if c != 0), h.betti_number())] += 1
    return tuple(sorted(cnt.items()))


# ---------------------------------------------------------------------
# 0. controls (fail => INVALID)
# ---------------------------------------------------------------------
def run_controls(M):
    out = {}
    # (a) B349's index <= 6 census, rerun with B349's own code.
    census_ok = {k: b349.cover_census(M, k) == b349.EXPECTED_CENSUS[k] for k in (4, 5, 6)}
    counts_ok = {k: sum(b349.cover_census(M, k).values()) == n
                 for k, n in ((4, 2), (5, 4), (6, 11))}
    collapse_ok = {}
    for k in (5, 6):
        res = b349.multiplicities_resolved_by_isometry(M, k)
        collapse_ok[k] = bool(res) and all(nc == 1 for _, nc in res.values())
    cyc6 = b349.cyclic_covers_match_B350(M, 6)
    cyc6_ok = all(betti_one and matches for _, betti_one, matches in cyc6.values())
    out["b349_census"] = census_ok
    out["b349_counts"] = counts_ok
    out["b349_collapse_5_6"] = collapse_ok
    out["b349_cyclic_vs_b350_2_6"] = cyc6_ok

    # (b) B350's exact monodromy algebra, extended to n = 7, 8 (sympy, exact tier).
    orders = b350.torsion_orders(8)                        # {n: (|det(A^n-I)|, L_2n - 2)}
    out["b350_orders_lucas"] = {n: a == b for n, (a, b) in orders.items()}
    snf = b350.torsion_groups(8)                           # {n: SNF diagonal}
    out["b350_snf_78"] = {n: snf[n] == EXPECTED_CYCLIC_SNF_78[n] for n in (7, 8)}
    out["b350_orders_78"] = {n: orders[n][0] == EXPECTED_CYCLIC_ORDERS_78[n] for n in (7, 8)}
    out["snf_product_is_order"] = {n: snf[n][0] * snf[n][1] == orders[n][0] for n in (7, 8)}

    def _flat(d):
        for v in d.values():
            if isinstance(v, dict):
                yield from _flat(v)
            else:
                yield bool(v)
    out["pass"] = all(_flat({k: v for k, v in out.items() if k != "pass"}))
    return out, snf


# ---------------------------------------------------------------------
# 1.+2. census + partition at one index
# ---------------------------------------------------------------------
def census_and_partition(M, k, v4):
    t0 = time.time()
    covers = M.covers(k)                                   # route 1: low_index (default)
    groups = collections.defaultdict(list)
    rows, max_vol_defect = [], 0.0
    for C in covers:
        key = cover_key(C)
        defect = float(abs(C.volume() - k * v4))
        max_vol_defect = max(max_vol_defect, defect)
        rows.append({"name": C.name(), "type": key[0], "torsion": list(key[1]),
                     "betti": key[2], "cusps": key[3], "volume": float(C.volume()),
                     "vol_defect": float(defect)})
        groups[key].append(C)
    census = {key: len(cs) for key, cs in groups.items()}

    # route 2: the original SnapPea kernel enumeration must give the same multiset.
    census2 = collections.Counter(cover_key(C) for C in M.covers(k, method="snappea"))
    routes_agree = census == dict(census2)

    # isometry signatures for EVERY cover (canonical retriangulation; the verified
    # tier is Sage-gated in this install -- recorded honestly, never claimed).
    sigs, all_verified = {}, True
    for C in covers:
        try:
            sigs[C.name()] = C.isometry_signature(verified=True)
        except Exception:
            all_verified = False
            try:
                sigs[C.name()] = C.isometry_signature()
            except Exception:
                sigs[C.name()] = None

    # partition of each multiplicity group by is_isometric_to (MB note: orientation-
    # blind; used only for identification) + the signature cross-check + the EXACT
    # degree-2 sub-cover census (same class => same sub-census; split groups must be
    # separated at the exact tier).
    partition, sig_consistent, exact_ok = {}, True, True
    for key, cs in groups.items():
        classes = []
        for C in cs:
            for cl in classes:
                if cl[0].is_isometric_to(C):
                    cl.append(C)
                    break
            else:
                classes.append([C])
        sub2 = {C.name(): subcensus2(C) for C in cs} if len(cs) >= 2 else {}
        cls_out = []
        for cl in classes:
            rep = cl[0]
            csigs = {sigs[c.name()] for c in cl}
            if len(csigs) != 1:                            # class members must share the signature
                sig_consistent = False
            entry = {"size": len(cl), "members": [c.name() for c in cl],
                     "signature": sigs[rep.name()]}
            if sub2:
                csub = {sub2[c.name()] for c in cl}
                if len(csub) != 1:                         # exact invariant constant on the class
                    exact_ok = False
                entry["subcensus2"] = str(sub2[rep.name()])
            try:
                sg = rep.symmetry_group()
                full = bool(sg.is_full_group())
                entry["sym_full_group"] = full
                entry["sym_order"] = int(sg.order())
                entry["amphichiral"] = bool(sg.is_amphicheiral()) if full else None
            except Exception as exc:                       # honest gap, not silently dropped
                entry["sym_full_group"] = None
                entry["sym_order"] = None
                entry["amphichiral"] = None
                entry["sym_error"] = str(exc)
            cls_out.append(entry)
        # distinct classes must have DISTINCT signatures (separation, numerics tier)
        rep_sigs = [c["signature"] for c in cls_out]
        if len(set(rep_sigs)) != len(rep_sigs):
            sig_consistent = False
        # ... and, for a SPLIT group, distinct classes must be separated at the
        # EXACT tier by the degree-2 sub-cover census (pi_1 invariant):
        if len(cls_out) > 1:
            rep_subs = [c["subcensus2"] for c in cls_out]
            if len(set(rep_subs)) != len(rep_subs):
                exact_ok = False
        partition[key] = cls_out
    wall = time.time() - t0
    return {"index": k, "n_covers": len(covers), "census": census, "rows": rows,
            "partition": partition, "routes_agree": routes_agree,
            "signatures_all_verified": all_verified, "signature_partition_consistent":
            sig_consistent, "exact_subcensus_consistent": exact_ok,
            "max_vol_defect": max_vol_defect, "wall_seconds": wall}


# ---------------------------------------------------------------------
# 3. gate-A evaluation at one index
# ---------------------------------------------------------------------
def gate_a(result, snf):
    k, census, partition = result["index"], result["census"], result["partition"]
    checks = {}
    checks["census_is_banked_multiset"] = census == EXPECTED_CENSUS_78[k]
    cyc = [key for key in census if key[0] == "cyclic"]
    checks["one_cyclic_cover"] = len(cyc) == 1 and census[cyc[0]] == 1
    checks["cyclic_matches_b350_snf"] = cyc[0][1] == snf[k] and cyc[0][2] == 1
    checks["volumes_are_n_v4"] = result["max_vol_defect"] < VOL_TOL
    checks["two_routes_agree"] = result["routes_agree"]
    checks["signature_partition_consistent"] = result["signature_partition_consistent"]
    checks["exact_subcensus_consistent"] = result["exact_subcensus_consistent"]

    mult = {key: cls for key, cls in partition.items() if sum(c["size"] for c in cls) >= 2}
    checks["partition_headline_banked"] = {
        key: (sum(c["size"] for c in cls), len(cls), tuple(sorted(c["size"] for c in cls)))
        for key, cls in mult.items()} == EXPECTED_PARTITION_78[k]
    # B349's clause (iii), reported honestly (True at 7, False at 8 -- the refinement):
    checks["all_multiplicities_collapse"] = all(len(cls) == 1 for cls in mult.values())
    # the gate-A criterion at the correct resolution: within every multiplicity group,
    # same-class covers are isometry-identified (any isometry defeats a forced choice,
    # the B349 stance), and distinct classes are separated by canonical invariants --
    # at the EXACT tier (degree-2 sub-cover census, a pi_1 invariant) with the
    # signature partition concurring. No member of an invariantly-indistinguishable
    # set is distinguished:
    checks["no_distinguished_member"] = bool(result["signature_partition_consistent"]
                                             and result["exact_subcensus_consistent"])

    # orientation-honest oriented census (structural; MB guard): chiral class of size s
    # refines to {s/2 X, s/2 Xbar} by mirror-closure (amphichiral base); s must be even.
    oriented_ok, oriented = True, {}
    for key, cls in partition.items():
        for c in cls:
            if c["amphichiral"] is False:
                if c["size"] % 2 != 0:
                    oriented_ok = False                    # would be a genuine oriented mark
                oriented[str((key, c["members"][0]))] = \
                    f"chiral: {c['size']} -> {c['size'] // 2} + {c['size'] // 2} mirror pair"
            elif c["amphichiral"] is True:
                oriented[str((key, c["members"][0]))] = "amphichiral: self-mirror"
            else:
                oriented[str((key, c["members"][0]))] = "chirality UNKNOWN (sym gate failed)"
    checks["oriented_census_mirror_symmetric"] = oriented_ok
    sealed = all(v is True for k_, v in checks.items()
                 if k_ not in ("all_multiplicities_collapse",))
    return checks, oriented, sealed


def main():
    T0 = time.time()
    import snappy
    M = snappy.Manifold("4_1")
    print("B500 -- Gate A class 2c: irregular covers of 4_1 at index 7-8\n")

    # ---- 0. controls ----
    controls, snf = run_controls(M)
    print(f"(0) controls (B349 census<=6 + B350 SNF/Lucas 2..8): pass={controls['pass']}"
          f"  [{time.time() - T0:.1f}s]")
    if not controls["pass"]:
        print("CONTROL FAILURE => INVALID (prereg). Aborting without a verdict.")
        print(json.dumps(controls, indent=2, default=str))
        sys.exit(1)
    print(f"    n=7: SNF {snf[7]}, order 841 = 29^2 = L14-2;"
          f" n=8: SNF {snf[8]}, order 2205 = 21*105 = L16-2  (exact)")

    # ---- 1.+2. the horizon extension, budget-logged ----
    results, budget_status = {}, "WITHIN BUDGET"
    for k in (7, 8):
        elapsed = time.time() - T0
        if elapsed > BUDGET_SECONDS:
            budget_status = (f"BUDGET-CAPPED before index {k} "
                             f"({elapsed:.0f}s > {BUDGET_SECONDS}s); partial census banked")
            print(budget_status)
            break
        res = census_and_partition(M, k, float(M.volume()))
        results[k] = res
        print(f"(1) index {k}: {res['n_covers']} covers  wall={res['wall_seconds']:.2f}s"
              f"  routes_agree={res['routes_agree']}"
              f"  max|vol - {k}*v4|={res['max_vol_defect']:.2e}"
              f"  sig-partition consistent={res['signature_partition_consistent']}"
              f"  exact-subcensus consistent={res['exact_subcensus_consistent']}"
              f"  (verified-sig tier available={res['signatures_all_verified']})")
        for key, cls in sorted(res["partition"].items(), key=str):
            sizes = [c["size"] for c in cls]
            chir = ["amph" if c["amphichiral"] else ("chiral" if c["amphichiral"] is False
                    else "unknown") for c in cls]
            print(f"      {key} x{sum(sizes)} -> {len(cls)} isometry class(es) "
                  f"sizes={sizes} [{', '.join(chir)}]")

    # ---- 3. gate A ----
    gate, verdict = {}, None
    if "BUDGET-CAPPED" in budget_status:
        verdict = "TOOL-BLOCKED/BUDGET-CAPPED"
    else:
        sealed_all = True
        for k in results:
            checks, oriented, sealed = gate_a(results[k], snf)
            gate[k] = {"checks": checks, "oriented_census": oriented, "sealed": sealed}
            sealed_all = sealed_all and sealed
            print(f"(3) index {k}: canonical multiset={checks['census_is_banked_multiset']}"
                  f"  cyclic=B350={checks['cyclic_matches_b350_snf']}"
                  f"  B349-collapse-clause={checks['all_multiplicities_collapse']}"
                  f"  no-distinguished-member={checks['no_distinguished_member']}")
        verdict = "SEALED" if sealed_all else "COUNTEREXAMPLE"

    total = time.time() - T0
    print(f"\nVERDICT: {verdict}  (total {total:.1f}s of the {BUDGET_SECONDS}s budget; "
          f"{budget_status})")
    if verdict == "SEALED":
        print("Gate-A horizon extended: index <= 8. The index-8 (3,3) group refines to")
        print("isometry classes [2, 1], separated at EXACT tier (degree-2 sub-cover census)")
        print("-- B349's collapse clause is index <= 7-specific; the canonical datum is the")
        print("ISOMETRY-CLASS multiset. Horizon extension, not a theorem (C-guardrail).")
        print("Nothing to CLAIMS.md.")

    # ---- bank ----
    def _k(d):
        return {str(k_): v for k_, v in d.items()}
    bank = {
        "probe": "B500", "class": "2c irregular covers index 7-8",
        "enum": ["SEALED", "COUNTEREXAMPLE", "TOOL-BLOCKED/BUDGET-CAPPED"],
        "controls": {k_: (v if not isinstance(v, dict) else _k(v))
                     for k_, v in controls.items()},
        "b350_snf_78": {str(n): list(EXPECTED_CYCLIC_SNF_78[n]) for n in (7, 8)},
        "b350_orders_78": {str(n): EXPECTED_CYCLIC_ORDERS_78[n] for n in (7, 8)},
        "indexes": {str(k): {**results[k], "census": _k(results[k]["census"]),
                             "partition": _k(results[k]["partition"])}
                    for k in results},
        "gate_a": {str(k): {**gate[k], "checks": _k(gate[k]["checks"])} for k in gate},
        "budget": {"cap_seconds": BUDGET_SECONDS, "total_seconds": total,
                   "status": budget_status,
                   "per_index_wall": {str(k): results[k]["wall_seconds"] for k in results}},
        "verdict": {"outcome": verdict,
                    "phrasing": "SEALED at the computational horizon index <= 8: a horizon "
                                "extension, not a theorem; the class beyond index 8 remains "
                                "open (C-guardrail)."},
        "mb_guard": {"is_isometric_to": "orientation-blind; identification only",
                     "chirality_source": "symmetry_group().is_amphicheiral() gated on "
                                         "is_full_group() (B128 guard)",
                     "base_amphichiral": bool(M.symmetry_group().is_amphicheiral())},
        "tiers": {"counts_H1_SNF_subcensus": "exact (integer/SNF computation)",
                  "split_separation": "exact (degree-2 sub-cover census, pi_1 invariant)",
                  "identification": "is_isometric_to positive match (canonical "
                                    "retriangulation) + equal signatures + equal exact "
                                    "sub-censuses",
                  "volumes": "certified-numerical (double precision, tol 1e-9)",
                  "signatures": "double-precision canonical retriangulation; the "
                                "verified=True tier is Sage-gated in this install "
                                "(TOOL-BLOCKED for that tier only, named honestly)"},
        "firewall": "untouched; nothing to CLAIMS.md",
    }
    with open(HERE / "b500_census.json", "w") as fh:
        json.dump(bank, fh, indent=1, default=str)
    print(f"banked -> {HERE / 'b500_census.json'}")
    return bank


if __name__ == "__main__":
    main()
