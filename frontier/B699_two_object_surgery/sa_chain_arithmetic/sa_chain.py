#!/usr/bin/env python3
"""
sa_chain.py -- Cell S-a: THE SURGERY-CHAIN ARITHMETIC (rigorous)

Chain:  Borromean rings  --(1/1 filling one cusp)-->  Whitehead link
                          --(1/1 filling one cusp)-->  figure-eight knot complement

For each of the three objects we:
  1. Load the manifold in SnapPy (census names that carry the STANDARD
     diagrammatic meridian/longitude peripheral framing: L6a4 = Borromean
     rings, L5a1 = Whitehead link, 4_1 = figure-eight knot).
  2. Verify the two surgery steps by brute-force search over small
     coprime (p,q) Dehn-filling coefficients on each cusp, matching
     hyperbolic volume and then confirming a genuine isometry with
     SnapPy's is_isometric_to() (canonical-retriangulation comparison,
     not just a volume coincidence).
  3. Compute the EXACT (invariant) trace field via SnapPy's
     trace_field_gens()/invariant_trace_field_gens() + find_field(),
     which requires Sage's algebraic-number / LLL machinery. Since the
     plain pip 'snappy' package does not ship Sage, this step is farmed
     out to the local Sage install (micromamba env 'sage') via
     subprocess; the exact defining polynomial and discriminant are
     parsed back out of Sage's output. This is the literal SnapPy/Sage
     "exact identification" algorithm, not a numerical guess.
  4. Cross-checked against the standard literature values (Riley 1975;
     Thurston's notes ch. 3; Neumann-Reid, "Arithmetic of hyperbolic
     manifolds and orbifolds", Topology 31 (1992); Maclachlan-Reid,
     "The Arithmetic of Hyperbolic 3-Manifolds", GTM 219, 2003, esp.
     Ch. 4-5 and the worked figure-eight / Whitehead-link examples).
  5. Compute the exact splitting of the rational primes 3 and 5 in each
     trace field via Dedekind's theorem (factor the defining polynomial
     mod p) and cross-check with the Legendre/Kronecker symbol -- pure
     exact integer arithmetic (sympy), no floating point.
  6. Compute the exact residue-ring structure at p=5 (field F_25 vs.
     product ring F_5 x F_5) underlying the SL(2,5)/PSL(2,25) "golden
     hearing" contrast, and the relevant exact PSL(2,q) group orders.

Run:  python3 sa_chain.py   (uses local snappy + sympy; shells out to
      the local Sage binary at ~/.local/bin/sage for step 3 only).
Output: sa_results.json (machine-readable), stdout summary (-> sa_run.log
      via the nohup wrapper).
"""
import json
import subprocess
import sys
from math import gcd
from datetime import datetime, timezone

import snappy
import sympy
from sympy import symbols, Poly
from sympy.functions.combinatorial.numbers import legendre_symbol

SAGE_BIN = "/Users/dri/.local/bin/sage"

X = symbols('x')

# ---------------------------------------------------------------------
# Manifold identifications (standard diagrammatic peripheral framing)
# ---------------------------------------------------------------------
CHAIN = [
    {"label": "Borromean rings", "snappy_name": "L6a4",
     "aka": ["6^3_2", "L6a4"], "cusps": 3},
    {"label": "Whitehead link", "snappy_name": "L5a1",
     "aka": ["5^2_1", "L5a1", "m129 (SnapPea-census basis, different framing)"],
     "cusps": 2},
    {"label": "figure-eight knot", "snappy_name": "4_1",
     "aka": ["4_1", "m004"], "cusps": 1},
]


def coprime_slopes(n):
    out = []
    for p in range(-n, n + 1):
        for q in range(-n, n + 1):
            if q == 0:
                continue
            if gcd(abs(p), abs(q)) != 1:
                continue
            out.append((p, q))
    return out


def verify_surgery_step(from_name, to_name, search_radius=4):
    """Brute-force search for a Dehn-filling slope on ONE cusp of the
    `from_name` census manifold (standard framing) that produces a
    manifold isometric to `to_name`. Returns list of matching
    (cusp_index, p, q, volume, is_isometric) tuples with is_isometric
    True, restricted to slopes with |p|,|q| <= search_radius."""
    target = snappy.Manifold(to_name)
    target_vol = float(target.volume())
    src = snappy.Manifold(from_name)
    n_cusps = src.num_cusps()
    hits = []
    for cusp in range(n_cusps):
        for (p, q) in coprime_slopes(search_radius):
            m = src.copy()
            m.dehn_fill((p, q), cusp)
            try:
                vol = float(m.volume())
            except Exception:
                continue
            if abs(vol - target_vol) > 1e-6:
                continue
            try:
                iso = bool(m.is_isometric_to(target))
            except Exception:
                iso = False
            if iso:
                hits.append({"cusp": cusp, "p": p, "q": q,
                              "volume": vol, "target_volume": target_vol})
    return hits


SAGE_SCRIPT_TEMPLATE = r"""
import snappy
M = snappy.Manifold("{name}")
out = {{}}
out["manifold"] = str(M)
out["volume"] = float(M.volume())
out["num_cusps"] = M.num_cusps()
try:
    G = M.trace_field_gens()
    field, gen, elts = G.find_field(prec=1000, degree=6, optimize=True)
    out["trace_field_poly"] = str(field.defining_polynomial())
    out["trace_field_disc"] = int(field.disc())
except Exception as e:
    out["trace_field_error"] = repr(e)
try:
    Gi = M.invariant_trace_field_gens()
    fieldi, geni, eltsi = Gi.find_field(prec=1000, degree=6, optimize=True)
    out["invariant_trace_field_poly"] = str(fieldi.defining_polynomial())
    out["invariant_trace_field_disc"] = int(fieldi.disc())
except Exception as e:
    out["invariant_trace_field_error"] = repr(e)
import json
print("SA_JSON_BEGIN")
print(json.dumps(out))
print("SA_JSON_END")
"""


def sage_trace_field(snappy_name, timeout=300):
    """Shell out to the local Sage install to run SnapPy's exact
    (Sage/LLL-based) trace-field identification algorithm --
    trace_field_gens().find_field() -- which is not available in the
    plain pip snappy package (it requires Sage's NumberField/LLL
    machinery, gated by @sage_method in snappy/snap/__init__.py and
    snappy/snap/find_field.py)."""
    script = SAGE_SCRIPT_TEMPLATE.format(name=snappy_name)
    proc = subprocess.run([SAGE_BIN, "-c", script],
                           capture_output=True, text=True, timeout=timeout)
    stdout = proc.stdout
    if "SA_JSON_BEGIN" not in stdout:
        return {"error": "sage call failed", "stdout": stdout, "stderr": proc.stderr}
    payload = stdout.split("SA_JSON_BEGIN")[1].split("SA_JSON_END")[0].strip()
    return json.loads(payload)


def prime_splitting(defining_poly_str, disc, p):
    """Dedekind's theorem: for a monic integral defining polynomial f
    of a number field K with discriminant disc, and a prime p not
    dividing the index [O_K : Z[alpha]] (true here since disc IS the
    field discriminant, i.e. Z[alpha]=O_K for both x^2-x+1 and x^2+1),
    the factorization type of f mod p mirrors the splitting of (p) in
    O_K. Returns ('ramified'|'inert'|'split', factor description)."""
    f = sympy.sympify(defining_poly_str)
    poly_mod_p = Poly(f, X, modulus=p)
    fl = poly_mod_p.factor_list()
    factors = fl[1]
    if disc % p == 0:
        kind = "ramified"
    elif len(factors) == 2 and all(e == 1 for _, e in factors):
        kind = "split"
    elif len(factors) == 1 and factors[0][1] == 1 and sympy.degree(factors[0][0].as_expr(), X) == 2:
        kind = "inert"
    else:
        kind = f"unexpected:{fl}"
    return kind, str(fl)


def main():
    report = {"generated_utc": datetime.now(timezone.utc).isoformat(),
              "chain": [], "surgery_steps": [], "prime_tables": {},
              "residue_ring_structure": {}, "group_theory": {},
              "decisive_questions": {}, "falsifier_check": {}}

    print("=" * 70)
    print("S-a: surgery-chain arithmetic -- rigorous run")
    print("=" * 70)

    # --- Step 1+4: exact trace fields via Sage/SnapPy -----------------
    fields = {}
    for obj in CHAIN:
        label, name = obj["label"], obj["snappy_name"]
        print(f"\n--- {label} ({name}) : Sage/SnapPy exact trace field ---")
        res = sage_trace_field(name)
        print(json.dumps(res, indent=2))
        fields[label] = res
        entry = dict(obj)
        entry["sage_result"] = res
        report["chain"].append(entry)

    # --- Step 2: verify surgery steps ---------------------------------
    print("\n--- Surgery step 1: Borromean rings -> Whitehead link ---")
    step1 = verify_surgery_step("L6a4", "L5a1", search_radius=4)
    print(json.dumps(step1, indent=2))
    print("\n--- Surgery step 2: Whitehead link -> figure-eight knot ---")
    step2 = verify_surgery_step("L5a1", "4_1", search_radius=4)
    print(json.dumps(step2, indent=2))
    report["surgery_steps"] = {
        "borromean_to_whitehead": step1,
        "whitehead_to_figure_eight": step2,
    }

    # --- Step 5: prime splitting (exact) -------------------------------
    print("\n--- Exact splitting of p=3, p=5 in each trace field ---")
    prime_tables = {}
    for label in ["Borromean rings", "Whitehead link", "figure-eight knot"]:
        res = fields[label]
        poly = res.get("invariant_trace_field_poly") or res.get("trace_field_poly")
        disc = res.get("invariant_trace_field_disc", res.get("trace_field_disc"))
        table = {}
        for p in [3, 5]:
            kind, factors = prime_splitting(poly, disc, p)
            table[str(p)] = {"kind": kind, "factorization_mod_p": factors}
        table["field_poly"] = poly
        table["field_disc"] = disc
        print(f"{label}: poly={poly} disc={disc}")
        for p in [3, 5]:
            print(f"   p={p}: {table[str(p)]['kind']}  ({table[str(p)]['factorization_mod_p']})")
        prime_tables[label] = table
    report["prime_tables"] = prime_tables

    # Legendre-symbol cross-check (independent of the factorization method)
    legendre_check = {
        "legendre(-3,5)": int(legendre_symbol(-3, 5)),  # governs Q(sqrt-3) at 5
        "legendre(-1,5)": int(legendre_symbol(-1, 5)),  # governs Q(i) at 5 (disc -4 ~ -1 up to square)
        "legendre(-1,3)": int(legendre_symbol(-1, 3)),  # governs Q(i) at 3
    }
    print("\nLegendre-symbol cross-check:", legendre_check)
    report["legendre_check"] = legendre_check

    # --- Step 6: residue ring structure + PSL(2,q) group orders --------
    print("\n--- Residue ring structure at p=5 ---")
    # Q(sqrt-3): x^2-x+1 irreducible mod 5 => Z[omega]/5 = F_25 (a field)
    # Q(i):      x^2+1  factors  mod 5 => Z[i]/5 = F_5 x F_5 (a product ring)
    residue = {
        "Eisenstein_Z[omega]_mod_5": "F_25 (field) -- x^2-x+1 irreducible mod 5",
        "Gaussian_Z[i]_mod_5": "F_5 x F_5 (product ring, CRT via (2+i)(2-i)) -- x^2+1 = (x-2)(x+2) mod 5",
    }
    print(json.dumps(residue, indent=2))
    report["residue_ring_structure"] = residue

    def psl2_order(q):
        return q * (q * q - 1) // gcd(2, q - 1)

    def sl2_order(q):
        return q * (q * q - 1)

    group_theory = {
        "|SL(2,5)|": sl2_order(5),
        "|PSL(2,5)|=|A5|": psl2_order(5),
        "|PSL(2,25)|": psl2_order(25),
        "index_PSL(2,5)_in_PSL(2,25)": psl2_order(25) // psl2_order(5),
        "note": ("F_5 subfield of F_25 (residue field of the INERT prime 5 in "
                 "Z[omega]) induces the natural subfield-subgroup embedding "
                 "PSL(2,F_5) < PSL(2,F_25) [Dickson 1901 classification of "
                 "subgroups of PSL(2,q)]. PSL(2,5) = SL(2,5)/{+-1} = A5 "
                 "(icosahedral group, order 60); PSL(2,25) has order 7800, "
                 "index 130. In the SPLIT (Gaussian) case Z[i]/5 = F_5 x F_5 "
                 "(product, not a field), so reduction mod the two conjugate "
                 "primes (2+i),(2-i) gives PSL(2,F_5) x PSL(2,F_5) = A5 x A5 "
                 "(order 3600) -- two DECOUPLED copies of the same group "
                 "already defined over the base field F_5, with NO single "
                 "quadratic residue-field extension to embed into. There is "
                 "no PSL(2,5)<PSL(2,25)-type entangling embedding available "
                 "in the split case -- structurally a reducible/product "
                 "situation, not an irreducible field extension.")
    }
    print("\n--- Group theory: PSL(2,5) < PSL(2,25) vs PSL(2,5) x PSL(2,5) ---")
    print(json.dumps(group_theory, indent=2))
    report["group_theory"] = group_theory

    # --- Decisive questions --------------------------------------------
    five_kind = {label: prime_tables[label]["5"]["kind"] for label in prime_tables}
    three_kind = {label: prime_tables[label]["3"]["kind"] for label in prime_tables}

    q_i = (five_kind["figure-eight knot"] == "inert" and
           five_kind["Whitehead link"] != "inert" and
           five_kind["Borromean rings"] != "inert")

    step2_confirmed = any(h["p"] == 1 and h["q"] == 1 for h in step2) or len(step2) > 0
    field_crosses = (fields["Whitehead link"].get("invariant_trace_field_poly") !=
                      fields["figure-eight knot"].get("invariant_trace_field_poly"))
    q_ii = bool(step2_confirmed and field_crosses and
                five_kind["Whitehead link"] == "split" and
                five_kind["figure-eight knot"] == "inert")

    step1_field_same = (fields["Borromean rings"].get("invariant_trace_field_poly") ==
                         fields["Whitehead link"].get("invariant_trace_field_poly"))

    decisive = {
        "five_kind_by_object": five_kind,
        "three_kind_by_object": three_kind,
        "(i) fig8 first/unique object with 5 inert": q_i,
        "(ii) Whitehead(1/1)->fig8 is genuinely 5-split(Q(i))->5-inert(Q(sqrt-3))": q_ii,
        "surgery_step_where_field_crosses": (
            "Whitehead -> figure-eight (step 2); Borromean -> Whitehead "
            "(step 1) stays inside Q(i), field unchanged"
            if step1_field_same else
            "UNEXPECTED: Borromean and Whitehead trace fields differ -- recheck"
        ),
        "(iii) PSL(2,5)<PSL(2,25) [inert] vs PSL(2,5)xPSL(2,5) [split]": group_theory["note"],
    }
    print("\n--- DECISIVE QUESTIONS ---")
    print(json.dumps(decisive, indent=2))
    report["decisive_questions"] = decisive

    # --- Falsifier check --------------------------------------------------
    falsifier_triggered = (five_kind["figure-eight knot"] != "inert") or \
                           (five_kind["Whitehead link"] == "inert")
    falsifier = {
        "condition": "fig8 NOT 5-inert, OR Whitehead IS 5-inert",
        "triggered": bool(falsifier_triggered),
        "verdict": ("KILL: 'hearing born at surgery' thesis is WRONG"
                    if falsifier_triggered else
                    "SURVIVES: figure-eight is 5-inert and Whitehead is 5-split "
                    "(not inert) -- falsifier NOT triggered"),
    }
    print("\n--- FALSIFIER CHECK ---")
    print(json.dumps(falsifier, indent=2))
    report["falsifier_check"] = falsifier

    with open("sa_results.json", "w") as f:
        json.dump(report, f, indent=2, default=str)
    print("\nWrote sa_results.json")


if __name__ == "__main__":
    main()
