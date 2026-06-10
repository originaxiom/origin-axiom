"""B149 decomposition (sage-python) -- minimal_associated_primes of the SL(4) {1,1,w,w^2} defining ideal over Q(w),
stratified by rank of the coupling block Q = t[0:2,2:4], with the per-component M^4=L verdict by EXACT IDEAL
MEMBERSHIP. Each stratum runs in ITS OWN process (an AlarmInterrupt mid-Singular corrupts Singular state, so strata
must be isolated). Serializes per-stratum JSON, then merges to decomposition.json with the rolled-up verdict.

  per stratum:  ~/.local/bin/sage-python -u frontier/B149_sl4_ideal_completeness/decompose.py <label>
  merge:        python frontier/B149_sl4_ideal_completeness/decompose.py --merge   (pyenv ok)

Why stratify by rank(Q). Z(A) = GL(V_1) x GL(V_w) x GL(V_{w^2}) gauge makes the full 16-var ideal intractable. Every Q
is gauge-equivalent to a normal form by rank: rank 2 -> Q=I_2; rank 1 -> Q=[[1,c],[0,0]] (c free) or [[0,1],[0,0]];
rank 0 -> Q=0. These FOUR slices EXHAUST all reps up to gauge; each is small/tractable. M^4=L is gauge-invariant, so
per-component membership is valid on each slice. The verdict is the decomposition EXHIBITED, not asserted. No physics.
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ALLOWED = {(0, 0), (0, 1), (1, 0), (1, 1), (2, 3), (3, 2)}
TIMEOUT = 400

# Q entries (t02,t03,t12,t13). The slices exhaust all Q UP TO GAUGE. Rank-1 Q=[[1,c],[0,0]] collapses under residual
# gauge to just c=0 (Q=[[1,0],[0,0]]) and c!=0 (=~ Q=[[1,1],[0,0]]); together with [[0,1],[0,0]] these are the three
# rank-1 normal forms. So: rank2 (I_2), rank1 in 3 fixed forms, rank0 -- all FIXED (no free Q var) and tractable.
STRATA = {
    "rankQ2_Qinv": {(0, 2): 1, (0, 3): 0, (1, 2): 0, (1, 3): 1},      # Q = I_2 (B89's stratum)
    "rankQ1_10":   {(0, 2): 1, (0, 3): 0, (1, 2): 0, (1, 3): 0},      # Q = [[1,0],[0,0]]
    "rankQ1_11":   {(0, 2): 1, (0, 3): 1, (1, 2): 0, (1, 3): 0},      # Q = [[1,1],[0,0]]
    "rankQ1_b":    {(0, 2): 0, (0, 3): 1, (1, 2): 0, (1, 3): 0},      # Q = [[0,1],[0,0]]
    "rankQ0":      {(0, 2): 0, (0, 3): 0, (1, 2): 0, (1, 3): 0},      # Q = 0
}


def run_stratum(label):
    from sage.all import (QQ, AlarmInterrupt, NumberField, PolynomialRing, alarm,
                          cancel_alarm, diagonal_matrix, matrix, polygen)

    K = NumberField(polygen(QQ)**2 + polygen(QQ) + 1, "w")
    w = K.gen()
    qsub = STRATA[label]
    pinned = {pos: val for pos, val in qsub.items() if val is not None}
    keep = [(i, j) for i in range(4) for j in range(4) if (i, j) not in pinned]
    R = PolynomialRing(K, ["t%d%d" % (i, j) for (i, j) in keep])
    var = {pos: R(name) for pos, name in zip(keep, R.gens())}

    def entry(i, j):
        return R(pinned[(i, j)]) if (i, j) in pinned else var[(i, j)]

    t = matrix(R, 4, 4, lambda i, j: entry(i, j))
    A = diagonal_matrix(R, [R(1), R(1), R(w), R(w**2)])
    A2 = diagonal_matrix(R, [R(1), R(1), R(w**2), R(w)])
    S = t * A * t
    I = R.ideal([S[i, j] for i in range(4) for j in range(4) if (i, j) not in ALLOWED])
    u = t.adjugate(); det = t.determinant(); mu = A2 * t
    E = A2 * t * A * u * A2 * t * A2 * u * A2 + det * (mu * mu * mu * mu)   # [A,B]det^2 + det*mu^4

    out = {"label": label, "n_vars": R.ngens(), "Q": {str(p): str(v) for p, v in qsub.items()}}
    try:
        alarm(TIMEOUT)
        primes = I.minimal_associated_primes()
        cancel_alarm()
    except AlarmInterrupt:
        out["obstruction"] = "minimal_associated_primes TIMEOUT after %ds" % TIMEOUT
        print("  [%s] TIMEOUT" % label, flush=True)
        return out
    comps = []
    for k, P in enumerate(primes):
        m4l = all((E[i, j] in P) for i in range(4) for j in range(4))
        comps.append({"index": k, "dim": int(P.dimension()), "m4_equals_l": bool(m4l),
                      "det_t_vanishes": bool(det in P), "gens": [str(g) for g in P.gens()]})
        print("  [%s] comp %d: dim=%d M^4=L=%s det_t=0:%s" % (label, k, comps[-1]["dim"],
              comps[-1]["m4_equals_l"], comps[-1]["det_t_vanishes"]), flush=True)
    out["n_components"] = len(primes)
    out["components"] = comps
    return out


def merge():
    strata = {}
    for label in STRATA:
        f = HERE / ("decomposition_%s.json" % label)
        strata[label] = json.loads(f.read_text()) if f.exists() else {"obstruction": "not run"}
    done = all("components" in s for s in strata.values())
    violations = [(lab, c["index"]) for lab, s in strata.items()
                  for c in s.get("components", []) if not c["m4_equals_l"] and not c["det_t_vanishes"]]
    verdict = {
        "all_strata_decomposed": done,
        "det_nonzero_components_violating_M4L": violations,
        "note": ("'det_nonzero_components_violating_M4L' flags components with det t != 0 where M^4=L fails -- but this "
                 "uses ONLY det != 0, NOT the MB7 irreducibility filter. The genuine-bundle-rep question needs "
                 "IRREDUCIBILITY (Burnside), settled exactly over F_p in irreducibility_fp.json: every such component is "
                 "REDUCIBLE (the only stratum carrying irreducible reps is rankQ2 = B89's family, where M^4=L holds). "
                 "See FINDINGS.md for the combined verdict (OUTCOME (a): B89's family is the complete IRREDUCIBLE locus)."),
    }
    result = {"field": "Q(w), w^2+w+1=0",
              "ideal": "S=tAt off-pattern, A=diag(1,1,w,w^2), 10 quadratics in 16 vars; stratified by rank(Q)",
              "strata": strata, "verdict": verdict}
    (HERE / "decomposition.json").write_text(json.dumps(result, indent=2))
    print(json.dumps(verdict, indent=2))
    return 0


def main():
    if len(sys.argv) < 2:
        print("usage: decompose.py <label|--merge>", flush=True)
        return 2
    if sys.argv[1] == "--merge":
        return merge()
    label = sys.argv[1]
    out = run_stratum(label)
    (HERE / ("decomposition_%s.json" % label)).write_text(json.dumps(out, indent=2))
    print("wrote decomposition_%s.json" % label, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
