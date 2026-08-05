"""B907 (SEALED cell): the real-form selector.

Inner involutions of the built frame: the 64 sign characters chi on the root
lattice (diagonal: h fixed, e_alpha -> chi(alpha) e_alpha). Outer: the diagram
flip tau (lifted with a fitted cocycle character, B893-style) composed with
the chi's. Classes identified by fixed-subalgebra dimension:
  36 = sp(4) (split e6(6)),  38 = su(6)+su(2) (e6(2)),
  46 = so(10)+u(1) (e6(-14)), 52 = f4 (e6(-26)), 78 = compact.
C-compatibility: an involution is C-compatible when every torus charge x_n is
a +-1/-1 eigenvector; the wall-reality criterion (sealed):
  wall REAL in the form  <=>  eps(x14) = +1  AND  eps(x16) = -1
(gamma real stays real; a imaginary becomes form-real). eps(x8), eps(x22)
recorded for the full picture (the first-measurement seesaw).
"""
import io, os, contextlib, json, itertools
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(open(os.path.join(HERE, "..", "B854_centralizer_exact",
                                   "e6_centralizer.py")).read(),
                 "b854", "exec"), globals())
print("frame rebuilt; roots", len(ROOTS), flush=True)

# basis: 0..5 h, 6+IDX[r] root vectors
def chi_val(signs, root):
    v = 1
    for i in range(6):
        if root[i] % 2:
            v *= signs[i]
    return v

CH = {n: [sp.Rational(c) for c in INV[n]] for n in ns}
# support analysis per charge: h-part and root-part
def charge_action(signs, n):
    """return eps if x_n is an eigenvector of sigma_chi, else None"""
    vec = CH[n]
    eps = None
    for i in range(6):
        if vec[i] != 0:
            eps = 1  # h fixed => any h-content forces eps = +1
            break
    for r in ROOTS:
        c = vec[6 + IDX[r]]
        if c != 0:
            e = chi_val(signs, r)
            if eps is None:
                eps = e
            elif e != eps:
                return None
    return eps

results = {"inner": [], "outer": []}
# ---- inner sweep: 64 sign characters ----
for signs in itertools.product((1, -1), repeat=6):
    npos = sum(1 for r in ROOTS if chi_val(signs, r) == 1)
    fixdim = 6 + npos
    acts = {n: charge_action(signs, n) for n in ns}
    results["inner"].append({
        "signs": list(signs), "fixed_dim": fixdim,
        "eps": {str(n): acts[n] for n in ns},
        "C_compatible": all(a is not None for a in acts.values())})
print("inner sweep done", flush=True)

# ---- the outer lift tau: diagram flip 1<->6, 3<->5 (0-indexed 0<->5, 2<->4) ----
FLIP = {0: 5, 5: 0, 1: 1, 2: 4, 4: 2, 3: 3}
def flip_root(r): return tuple(r[FLIP[i]] for i in range(6))
# lift: tau(e_alpha) = d(alpha) e_{flip(alpha)}, tau(h_i) = h_{FLIP[i]};
# d must satisfy d(a)d(b)eps(flip a, flip b) = eps(a,b) d(a+b) on all bracket
# pairs. Fit d as a character: d(alpha) = prod t_i^{m_i(alpha)} with t in
# {+-1}^6, t_i symmetric under FLIP; test each candidate on all root pairs.
def eps_pair(a, b):
    return eps(a, b)   # the frame's structure-constant sign function
cands = []
for t in itertools.product((1, -1), repeat=6):
    if any(t[i] != t[FLIP[i]] for i in range(6)):
        continue
    ok = True
    for a in ROOTS:
        for b in ROOTS:
            s = tuple(a[i] + b[i] for i in range(6))
            if s in IDX:
                da = 1; db = 1; ds = 1
                for i in range(6):
                    if a[i] % 2: da *= t[i]
                    if b[i] % 2: db *= t[i]
                    if s[i] % 2: ds *= t[i]
                if da*db*eps_pair(flip_root(a), flip_root(b)) != eps_pair(a, b)*ds:
                    ok = False; break
        if not ok: break
    if ok:
        cands.append(t)
print("outer lift characters found:", len(cands), cands[:4], flush=True)

def tau_charge_action(t, signs, n):
    """action of tau_t composed with sigma_chi on x_n: eigen or None.
    tau: h_i -> h_FLIP[i]; e_a -> d(a) e_{flip a}; then chi."""
    vec = CH[n]
    # build image vector
    img = [sp.Integer(0)]*78
    for i in range(6):
        if vec[i]:
            img[FLIP[i]] += vec[i]
    for r in ROOTS:
        c = vec[6 + IDX[r]]
        if c:
            d = 1
            for i in range(6):
                if r[i] % 2: d *= t[i]
            fr = flip_root(r)
            img[6 + IDX[fr]] += c*d*chi_val(signs, fr)
    # eigen test
    eps_v = None
    for k in range(78):
        if vec[k] == 0 and img[k] == 0: continue
        if vec[k] == 0: return None
        ratio = sp.Rational(img[k]) / sp.Rational(vec[k])
        if ratio not in (1, -1): return None
        if eps_v is None: eps_v = int(ratio)
        elif int(ratio) != eps_v: return None
    return eps_v

def outer_fixed_dim(t, signs):
    """fixed dim of tau_t o sigma_chi: h-part: fixed subspace of FLIP (4);
    roots: flip-fixed roots with d*chi = 1 count 1 each; flip-2-cycles
    contribute 1 per cycle iff product of (d*chi) over the pair = 1."""
    dim = 4  # h: FLIP has 4-dim fixed subspace (2 swapped pairs + 2 fixed)
    seen = set()
    for r in ROOTS:
        if r in seen: continue
        fr = flip_root(r)
        d = 1
        for i in range(6):
            if r[i] % 2: d *= t[i]
        if fr == r:
            if d*chi_val(signs, r) == 1: dim += 1
            seen.add(r)
        else:
            dfr = 1
            for i in range(6):
                if fr[i] % 2: dfr *= t[i]
            prod = d*chi_val(signs, fr)*dfr*chi_val(signs, r)
            if prod == 1: dim += 1
            seen.add(r); seen.add(fr)
    return dim

if cands:
    t0 = cands[0]
    for signs in itertools.product((1, -1), repeat=6):
        fixdim = outer_fixed_dim(t0, signs)
        acts = {n: tau_charge_action(t0, signs, n) for n in ns}
        results["outer"].append({
            "signs": list(signs), "fixed_dim": fixdim,
            "eps": {str(n): acts[n] for n in ns},
            "C_compatible": all(a is not None for a in acts.values())})
print("outer sweep done", flush=True)

# ---- the verdict table ----
FORM = {36: "e6(6) split", 38: "e6(2)", 46: "e6(-14)", 52: "e6(-26)",
        78: "compact"}
verdict = {}
for kind in ("inner", "outer"):
    for row in results[kind]:
        fd = row["fixed_dim"]
        name = FORM.get(fd)
        if name is None or not row["C_compatible"]:
            continue
        e = row["eps"]
        wall_real = (e["14"] == 1 and e["16"] == -1)
        key = name
        verdict.setdefault(key, {"wall_real_witness": None, "eps_patterns": []})
        pat = (e["8"], e["14"], e["16"], e["22"], kind)
        if pat not in verdict[key]["eps_patterns"]:
            verdict[key]["eps_patterns"].append(pat)
        if wall_real and verdict[key]["wall_real_witness"] is None:
            verdict[key]["wall_real_witness"] = {"kind": kind,
                                                 "signs": row["signs"],
                                                 "eps": e}
print(json.dumps({k: {"wall_real": v["wall_real_witness"] is not None,
                      "n_patterns": len(v["eps_patterns"])}
                  for k, v in verdict.items()}, indent=1), flush=True)
json.dump({"sweep": results, "verdict": verdict},
          open(os.path.join(HERE, "results.json"), "w"), indent=1,
          default=str)
print("saved", flush=True)
