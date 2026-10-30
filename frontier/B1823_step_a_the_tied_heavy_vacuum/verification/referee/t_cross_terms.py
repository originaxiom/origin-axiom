"""Under the draft's OWN exhibited weight/character assignment (checks_extra.json section 2: k_H = 0, r_H = 0, every copy
k_L = 0, c_L = 0), which gauge-invariant CROSS-COPY terms are also modular-invariant?  A term needs a form whose weight and
character cancel its fields'.  Singlet forms of weight w and character chi_eta^t exist iff some s >= 0, s = t mod 24, has
w - s/2 in {0, 4, 6, 8, ...} (eta^s E4^p E6^r); weight-3/2 triplets of rho_R (x) chi_eta^r: the copies' own F_a (r = 2a) or DR (r = 0).
Gauge-invariant renormalisable superpotential terms among the heavy fields and H: L_i Lbar_j, E_i Ebar_j, H L_i Ebar_j."""
import json, pathlib
from fractions import Fraction as Fr
HERE = pathlib.Path(__file__).resolve().parent
ce = json.loads((HERE.parent / "checks_extra.json").read_text())["weight_character_assignment"]["rows"]

def singlet_exists(w, t):
    for s in range(t % 24, 200, 24):
        rest = w - Fr(s, 2)
        if rest < 0:
            break
        if rest.denominator == 1 and int(rest) % 2 == 0 and int(rest) != 2:
            return "eta^%d x (weight %d level-1 form)" % (s, int(rest))
    return None

out = {}
for menu in ("Z", "H"):
    rows = [r for r in ce if r["menu"] == menu]
    res = {}
    for n in (2, 3, 8):
        cops = rows[:n]
        allowed = {"L_i Lbar_j": [], "E_i Ebar_j": [], "H L_i Ebar_j": []}
        for i, ri in enumerate(cops):
            for j, rj in enumerate(cops):
                if i == j:
                    continue
                kL, kLb = Fr(ri["k"]["L"]), Fr(rj["k"]["Lbar"]); cL, cLb = ri["chi_eta_power"]["L"], rj["chi_eta_power"]["Lbar"]
                f = singlet_exists(kL + kLb, (-(cL + cLb)) % 24)
                if f: allowed["L_i Lbar_j"].append([i + 1, j + 1, f])
                kE, kEb = Fr(ri["k"]["E"]), Fr(rj["k"]["Ebar"]); cE, cEb = ri["chi_eta_power"]["E"], rj["chi_eta_power"]["Ebar"]
                f = singlet_exists(kE + kEb, (-(cE + cEb)) % 24)
                if f: allowed["E_i Ebar_j"].append([i + 1, j + 1, f])
                w = Fr(ri["k"]["H"]) + kL + Fr(rj["k"]["Ebar"]); r_need = (-(ri["chi_eta_power"]["H"] + cL + rj["chi_eta_power"]["Ebar"])) % 24
                trip = [cc for cc in cops if cc["chi_eta_power"]["Y3"] % 24 == r_need]
                if w == Fr(3, 2) and trip:
                    allowed["H L_i Ebar_j"].append([i + 1, j + 1, "the weight-3/2 triplet of copy %d (r = %d)" % (trip[0]["copy"], r_need)])
        res["n%d" % n] = {k: dict(count=len(v), off_diagonal_pairs=n * (n - 1), examples=v[:6]) for k, v in allowed.items()}
    out["menu_" + menu] = res
out["reading"] = ("with every copy's L at k = 0, c = 0, the cross terms L_i Lbar_j (form Y_L,j) and H L_i Ebar_j (triplet Y3,j) "
                  "carry exactly the weight and character of copy j's own terms, so they are invariant for every i != j; the "
                  "construction's 'one copy, one block' superpotential sets them to zero by choice (no symmetry of the exhibited "
                  "assignment forbids them); another member of the affine family of assignments would have to be exhibited")
(HERE / "t_cross_terms.json").write_text(json.dumps(out, indent=1))
for m in ("menu_Z", "menu_H"):
    for nn, v in out[m].items():
        print(m, nn, {k: "%d/%d" % (x["count"], x["off_diagonal_pairs"]) for k, x in v.items()})
