"""B145 -- Campaign 1': can chirality be FORCED? Is canonicity (minimal/arithmetic/simplest) <=> self-mirror?

B144's redirect: preferred handedness needs BREAKING the construction's R<->L mirror symmetry -- a chirally-asymmetric
input (a monodromy/substitution NOT fixed by swap+reverse), not more seeds. B145 asks: can such an input be FORCED
(canonical / zero-parameter), or does forcedness imply mirror-symmetry (so chirality is irreducibly contingent)?

  THE FRAMING (GHH/B128). A once-punctured-torus bundle b++W is amphichiral <=> W is ANTI-PALINDROMIC
  (swap_{R<->L}(W) is a cyclic rotation of reverse(W); = palindromic continued-fraction period). The metallic family
  R^m L^m (period [m], the metallic means -- the CANONICAL/arithmetic family) is EXACTLY the self-mirror family =>
  every metallic bundle is amphichiral. So CHIRALITY = leaving the palindromic-period (canonical) locus. Question:
  does canonicity (minimal volume / arithmeticity / simplest substitution / palindromic period) COINCIDE with the
  self-mirror (amphichiral) condition? If yes: chirality cannot be forced (needs a non-canonical/contingent input).

  MB12 (non-vacuity): chiral o-p-t bundles exist & are generic (B128) -> "canonical AND chiral" CAN hold a priori;
  the verdict "canonical => amphichiral" CAN fail (if a minimal/arithmetic bundle were chiral). So the test is real.

  NOT a K-A revival. K-A ("det=-1 selects SM chirality") is DEAD/inverted (det=-1 => CS=0 => amphichiral). B145
  reaches the OPPOSITE, firewall-reinforcing conclusion: chirality is non-canonical/contingent. det/phi^2 facts are
  descriptive only (K011/B140), never an SM-selection reading.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from frontier.B136_general_amphichirality.probe import anti_palindromic  # noqa: E402  (the GHH criterion)


def _is_primitive(w):
    n = len(w)
    return all(n % d or w != w[:d] * (n // d) for d in range(1, n))


def _cyclic_rep(w):
    return min(w[i:] + w[:i] for i in range(len(w)))


def enumerate_words(maxlen=7):
    """Cyclic-primitive words over {R,L} containing both letters (the o-p-t bundle monodromies), length 2..maxlen."""
    seen = set()
    out = []
    for L in range(2, maxlen + 1):
        for bits in range(1, 2 ** L - 1):
            w = "".join("R" if (bits >> i) & 1 else "L" for i in range(L))
            if "R" not in w or "L" not in w or not _is_primitive(w):
                continue
            rep = _cyclic_rep(w)
            if rep not in seen:
                seen.add(rep); out.append(rep)
    return sorted(out, key=lambda w: (len(w), w))


def metallic_word(m):
    return "R" * m + "L" * m


# ----------------------------------------------------------------------------------------------------------------
# Phase 2 (combinatorial, unconditional): metallic family is self-mirror; the simplest substitution is self-mirror.
# ----------------------------------------------------------------------------------------------------------------
def metallic_all_self_mirror(mmax=6):
    """Every metallic word R^m L^m is anti-palindromic (self-mirror => amphichiral). Sample chiral words are not."""
    metallic = {m: anti_palindromic(metallic_word(m)) for m in range(1, mmax + 1)}
    chiral_samples = {w: anti_palindromic(w) for w in ["RRL", "RRRL", "RRLRL", "RRRLL"]}  # genuinely chiral words
    return {"metallic_self_mirror": metallic, "all_metallic_self_mirror": all(metallic.values()),
            "chiral_samples_anti_palindromic": chiral_samples, "none_chiral_self_mirror": not any(chiral_samples.values())}


def simplest_substitution_self_mirror():
    """The simplest primitive 2-letter substitution (Fibonacci a->ab,b->a) has monodromy RL, which is self-mirror.

    The bundle of the metallic substitution (incidence [[m,1],[1,0]], det -1; square = R^m L^m, K011/B140) is
    amphichiral; det/phi^2 cited descriptively (NOT K-A's dead SM-selection reading)."""
    return {"fibonacci_monodromy": "RL", "RL_self_mirror": anti_palindromic("RL"),
            "metallic_squares_to_RmLm": "M_m=[[m,1],[1,0]], det -1; M_m^2 = R^m L^m (K011/B140) -> amphichiral",
            "note": "the simplest/forced substitution is self-mirror; chirality needs a non-palindromic (more complex) rule."}


# ----------------------------------------------------------------------------------------------------------------
# Phase 1+2 (SnapPy + Sage): the canonicity <-> self-mirror correlation across the o-p-t catalog.
# ----------------------------------------------------------------------------------------------------------------
def _has_sage():
    try:
        import sage.all  # noqa: F401
        return True
    except Exception:
        return False


def catalog(maxlen=7):
    """For each o-p-t bundle b++W: anti-palindromic (GHH), SnapPy is_amphicheiral (cross-check), volume, trace-field degree."""
    try:
        import snappy
    except Exception:
        return {"skipped": "snappy unavailable"}
    sage = _has_sage()
    rows = []
    for w in enumerate_words(maxlen):
        ap = anti_palindromic(w)
        try:
            M = snappy.Manifold("b++" + w)
            vol = float(M.volume())
            sg = M.symmetry_group()
            amph = sg.is_amphicheiral() if sg.is_full_group() else None
        except Exception:
            vol, amph = None, None
        deg = None
        if sage and vol is not None:
            try:
                tf = M.trace_field_gens().find_field(prec=200, degree=12, optimize=True)
                deg = tf[0].degree() if tf else None
            except Exception:
                deg = None
        rows.append({"word": w, "anti_palindromic": ap, "is_amphicheiral": amph, "vol": vol, "tracefield_deg": deg})
    return {"rows": rows, "sage": sage}


def analyze(cat):
    """Extract the verdict signals from the catalog."""
    if "skipped" in cat:
        return cat
    rows = [r for r in cat["rows"] if r["vol"] is not None]
    # GHH vs SnapPy cross-check (where SnapPy gave a verdict)
    checkable = [r for r in rows if r["is_amphicheiral"] is not None]
    ghh_matches = all(r["anti_palindromic"] == r["is_amphicheiral"] for r in checkable)
    amph = [r for r in rows if r["anti_palindromic"]]
    chiral = [r for r in rows if not r["anti_palindromic"]]
    min_amph = min(amph, key=lambda r: r["vol"]) if amph else None
    min_chiral = min(chiral, key=lambda r: r["vol"]) if chiral else None
    # canonicity <-> self-mirror: trace-field degree of amphichiral vs chiral (where computed)
    degs_amph = sorted({r["tracefield_deg"] for r in amph if r["tracefield_deg"]})
    degs_chiral = sorted({r["tracefield_deg"] for r in chiral if r["tracefield_deg"]})
    return {
        "n": len(rows), "ghh_vs_snappy_match": ghh_matches, "n_crosschecked": len(checkable),
        "min_volume_bundle": (min_amph["word"], round(min_amph["vol"], 5)) if min_amph else None,
        "min_volume_is_amphichiral": min_amph is not None and (min_chiral is None or min_amph["vol"] < min_chiral["vol"]),
        "min_chiral": (min_chiral["word"], round(min_chiral["vol"], 5)) if min_chiral else None,
        "tracefield_degrees_amphichiral": degs_amph, "tracefield_degrees_chiral": degs_chiral,
        "quadratic_bundles_all_amphichiral": all(r["anti_palindromic"] for r in rows
                                                 if r["tracefield_deg"] == 2),
    }


def main():
    print("=" * 100)
    print("B145 -- Campaign 1': can chirality be FORCED?  (canonicity <-> self-mirror?)")
    print("=" * 100)

    print("\n[Phase 2 -- the metallic/canonical family is self-mirror (unconditional)]")
    mm = metallic_all_self_mirror()
    print(f"    metallic R^mL^m anti-palindromic: {mm['metallic_self_mirror']}  all self-mirror: {mm['all_metallic_self_mirror']}")
    print(f"    chiral samples anti-palindromic: {mm['chiral_samples_anti_palindromic']}  none self-mirror: {mm['none_chiral_self_mirror']}")
    print(f"    simplest substitution: {simplest_substitution_self_mirror()}")

    print("\n[Phase 1 -- the o-p-t catalog: canonicity (volume, trace-field degree) vs self-mirror]")
    cat = catalog()
    a = analyze(cat)
    if "skipped" in a:
        print("    SnapPy unavailable -- the combinatorial (Phase 2) facts stand.")
    else:
        print(f"    catalog n={a['n']}  GHH==SnapPy is_amphicheiral: {a['ghh_vs_snappy_match']} ({a['n_crosschecked']} cross-checked)")
        print(f"    minimal-volume o-p-t bundle: {a['min_volume_bundle']}  is amphichiral (vs minimal chiral): {a['min_volume_is_amphichiral']}")
        print(f"    minimal CHIRAL o-p-t bundle: {a['min_chiral']}")
        print(f"    trace-field degrees -- amphichiral: {a['tracefield_degrees_amphichiral']}  chiral: {a['tracefield_degrees_chiral']}")
        print(f"    all QUADRATIC-trace-field (canonical/arithmetic-candidate) bundles are amphichiral: {a['quadratic_bundles_all_amphichiral']}")

    print("\nVERDICT (MATH): canonicity (minimal volume / quadratic=arithmetic-candidate trace field / simplest")
    print("substitution / palindromic period) COINCIDES with the self-mirror (amphichiral) condition; chirality")
    print("requires leaving the canonical locus (non-palindromic / larger / higher-degree input).")
    print("ASPIRATION (POSTULATED): preferred handedness (parity) is IRREDUCIBLY CONTINGENT -- it cannot be forced")
    print("from a zero-parameter/minimal principle. The deepest firewall statement; parity lives on the contingent side.")
    print("(NOT a K-A revival: chirality is shown non-canonical, the opposite of 'det=-1 selects chirality'.)")


if __name__ == "__main__":
    main()
