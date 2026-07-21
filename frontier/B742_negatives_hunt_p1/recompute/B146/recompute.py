"""B739 Stage B recompute — target B146 (sealed Stage-A kill record, ground=dead-probe).

BANKED KILL UNDER TEST (E19 compute-not-cite, both directions):
  B146 killed B145's arithmetic arm — "every quadratic-trace-field o-p-t bundle is
  amphichiral / no arithmetic chiral o-p-t bundle" — by exhibiting RRL/RLL: chiral
  once-punctured-torus bundles whose arithmeticity-relevant INVARIANT trace field is
  imaginary quadratic, x^2-x+2 = Q(sqrt(-7)).

THE DISCRIMINATING FACT (what, if true, kills the claim):
  There EXISTS a once-punctured-torus bundle in B145's range whose invariant trace
  field is imaginary quadratic (degree 2, discriminant < 0 — the arithmetic-NECESSARY
  condition, Maclachlan–Reid) and which is CHIRAL (admits no orientation-reversing
  self-isometry).  Witness claimed: b++RRL (and its mirror b++RLL), field x^2-x+2.

RE-DERIVED HERE, from the original arc's own declared conventions:
  (1) combinatorial amphichirality criterion — B136 probe.py `anti_palindromic`
      (re-implemented inline verbatim-semantics; NOT imported, so no banked dir is
      touched);
  (2) the range — B145 probe.py `enumerate_words(maxlen=7)`: cyclic-primitive words
      over {R,L} containing both letters, length 2..7 (maxlen=7 is B146
      arithmetic_arm's declared default);
  (3) mirror convention — B146 probe.py `mirror_word`: swap R<->L then reverse;
      mirror manifold of b++W is b++mirror_word(W);
  (4) invariant trace field — B146 arithmetic_arm's exact call:
      Manifold("b++"+w).invariant_trace_field_gens().find_field(prec=200, degree=12,
      optimize=True); "imaginary quadratic" = degree 2 and field discriminant < 0;
      None/exception -> word skipped (B146's own `continue` semantics, but counted
      transparently here);
  (5) GEOMETRIC chirality (E19 hardening beyond the banked combinatorial proxy):
      SnapPy kernel symmetry group of the cusped hyperbolic manifold;
      amphichiral <=> is_amphicheiral() True (an orientation-reversing self-isometry
      exists).  This checks the KILL'S OBJECT (the manifold), not only B136's word
      criterion.
  (6) orientation-(in)dependent cross-checks per B146 dichotomy_witness conventions:
      volume/H1 equal across the mirror pair, CS proxy = Im(complex_volume) flips.

Deterministic: no wall-clock, no randomness, no network.  Requires snappy under
sage-python (Sage gates leg (4) only; every other leg is snappy/stdlib).

Run:  ~/.local/bin/sage-python recompute.py
"""
from __future__ import annotations

import sys

# ------------------------------------------------------------------------------------
# Conventions (1)-(3), re-implemented inline from the cited arcs' probe.py sources.
# ------------------------------------------------------------------------------------

def mirror_word(w: str) -> str:
    """B146 probe.py: mirror = swap R<->L, then reverse."""
    return w.translate(str.maketrans("RL", "LR"))[::-1]


def anti_palindromic(w: str) -> bool:
    """B136 probe.py: the swapped word is a cyclic rotation of the reversed word.
    anti_palindromic(w) <=> the bundle word is self-mirror (amphichiral, combinatorial
    criterion)."""
    sw = w.translate(str.maketrans("RL", "LR"))
    return len(w) == len(sw) and sw in (w[::-1] + w[::-1])


def _cyclic_rep(w: str) -> str:
    """Lexicographically least cyclic rotation (B145 probe.py convention)."""
    return min(w[i:] + w[:i] for i in range(len(w)))


def _is_primitive(w: str) -> bool:
    """Not a proper power of a shorter cyclic word (B145 probe.py convention)."""
    n = len(w)
    for d in range(1, n):
        if n % d == 0 and w == w[:d] * (n // d):
            return False
    return True


def enumerate_words(maxlen: int = 7):
    """B145 probe.py: cyclic-primitive words over {R,L} containing both letters,
    lengths 2..maxlen, one representative per cyclic class, sorted (len, lex)."""
    seen, out = set(), []
    for n in range(2, maxlen + 1):
        for bits in range(1, 2 ** n - 1):
            w = "".join("R" if (bits >> i) & 1 else "L" for i in range(n))
            if "R" not in w or "L" not in w or not _is_primitive(w):
                continue
            rep = _cyclic_rep(w)
            if rep not in seen:
                seen.add(rep)
                out.append(rep)
    return sorted(out, key=lambda w: (len(w), w))


# ------------------------------------------------------------------------------------
# Part 1 — combinatorial facts (stdlib only; unconditional).
# ------------------------------------------------------------------------------------

def part1_combinatorial():
    print("=" * 98)
    print("PART 1 — combinatorial layer (B136/B145/B146 conventions, re-implemented inline)")
    print("=" * 98)
    words = enumerate_words(7)
    print(f"range: enumerate_words(7) -> {len(words)} cyclic-primitive words, lengths 2..7")
    for w in ("RL", "RRLL", "RRL", "RLL"):
        print(f"  anti_palindromic({w!r}) = {anti_palindromic(w)}"
              f"   (True => self-mirror/amphichiral word; False => chiral word)")
    mw = mirror_word("RRL")
    pair = _cyclic_rep(mw) == _cyclic_rep("RLL")  # compare CYCLIC CLASSES (B145 convention)
    print(f"  mirror_word('RRL') = {mw!r}; cyclic classes: mirror {_cyclic_rep(mw)!r} vs "
          f"RLL {_cyclic_rep('RLL')!r}   -> RRL/RLL form a mirror PAIR: {pair}")
    return words


# ------------------------------------------------------------------------------------
# Part 2 — geometric chirality of the kill's objects (snappy; no Sage needed).
# ------------------------------------------------------------------------------------

def part2_geometric():
    """NOTE (run-1 correction, logic-only): B145's `_cyclic_rep` is the LEXICOGRAPHIC
    minimum with L < R, so the scan names the RRL/RLL cyclic classes 'LRR'/'LLR'.
    Run 1 of this recompute keyed this dict on the banked spellings only and the
    verdict cross-reference came up empty — a key-mismatch bug in the VERDICT LOGIC
    (every substantive leg already computed the banked values).  Fixed by keying on
    `_cyclic_rep` and by CHECKING (not assuming) that rotated words give isometric
    bundles.  Run 1 is preserved in the campaign workflow journal."""
    import snappy

    print()
    print("=" * 98)
    print("PART 2 — geometric layer (SnapPy kernel symmetry group; convention (5))")
    print("=" * 98)
    amph = {}       # keyed by cyclic representative (B145 convention)
    for w in ("RL", "RRLL", "RRL", "RLL", "LR", "LLRR", "LRR", "LLR"):
        M = snappy.Manifold("b++" + w)
        S = M.symmetry_group()
        a = bool(S.is_amphicheiral())
        key = _cyclic_rep(w)
        if key in amph and amph[key] != a:
            raise RuntimeError(f"rotation inconsistency at {w} (class {key})")
        amph[key] = a
        print(f"  b++{w:<5} (class {key:<5}) vol={M.volume()!r:<20} H1={M.homology()}   "
              f"symmetry group {S}   is_amphicheiral={a}")
    rot_isom = snappy.Manifold("b++RRL").is_isometric_to(snappy.Manifold("b++LRR"))
    print(f"  rotation-invariance check: b++RRL is_isometric_to b++LRR = {rot_isom}"
          f"   (cyclic rotation of the word gives the same bundle)")
    M, Mb = snappy.Manifold("b++RRL"), snappy.Manifold("b++RLL")
    vol_eq = abs(float(M.volume()) - float(Mb.volume())) < 1e-9
    h1_eq = str(M.homology()) == str(Mb.homology())
    cs_m = float(M.complex_volume().imag())
    cs_mb = float(Mb.complex_volume().imag())
    cs_flip = abs(cs_m + cs_mb) < 1e-9
    isom = M.is_isometric_to(Mb)
    print(f"  mirror-pair cross-checks (convention (6)): vol_eq={vol_eq}  H1_eq={h1_eq}  "
          f"CS proxy: Im(cvol)(RRL)={cs_m:+.12f}, Im(cvol)(RLL)={cs_mb:+.12f}, "
          f"flips={cs_flip}")
    print(f"  b++RRL is_isometric_to b++RLL (unoriented isometry checker): {isom}")
    geo_kill_leg = ((not amph[_cyclic_rep("RRL")]) and (not amph[_cyclic_rep("RLL")])
                    and amph[_cyclic_rep("RL")] and amph[_cyclic_rep("RRLL")])
    print(f"  GEOMETRIC chirality leg: b++RRL and b++RLL admit NO orientation-reversing "
          f"self-isometry (CHIRAL), b++RL and b++RRLL do (amphichiral): {geo_kill_leg}")
    return amph, {"vol_eq": vol_eq, "h1_eq": h1_eq, "cs_flip": cs_flip, "isometric_pair": isom}


# ------------------------------------------------------------------------------------
# Part 3 — the invariant-trace-field scan (Sage-gated; B146 arithmetic_arm, convention (4)).
# ------------------------------------------------------------------------------------

def part3_invariant_trace_fields(words):
    try:
        import sage.all  # noqa: F401
        import snappy
    except Exception as e:  # pragma: no cover
        print(f"\nPART 3 SKIPPED — sage unavailable ({e}); run under sage-python")
        return None

    print()
    print("=" * 98)
    print("PART 3 — invariant trace fields over the full range (Sage; B146's exact call)")
    print("=" * 98)
    imagquad = []          # (word, defining poly, field discriminant, anti_palindromic)
    skipped = []
    for w in words:
        try:
            M = snappy.Manifold("b++" + w)
            itf = M.invariant_trace_field_gens().find_field(prec=200, degree=12, optimize=True)
            if itf is None:
                skipped.append((w, "find_field returned None"))
                continue
            K = itf[0]
            if K.degree() == 2 and K.discriminant() < 0:
                imagquad.append((w, str(K.defining_polynomial()), int(K.discriminant()),
                                 anti_palindromic(w)))
        except Exception as e:
            skipped.append((w, f"{type(e).__name__}: {e}"))
            continue
    print(f"  scanned {len(words)} words; {len(skipped)} skipped "
          f"(B146 `continue` semantics): {skipped if skipped else '[]'}")
    print("  imaginary-quadratic (degree-2, disc<0 = arithmetic-NECESSARY) invariant trace fields:")
    print("    word   | invariant trace field | field disc | anti_palindromic (word-level amphichiral)")
    for w, poly, disc, ap in imagquad:
        print(f"    {w:<6} | {poly:<21} | {disc:>10} | {ap}")

    # The one-hop wrong-object check (citation_chain): B145 consulted the NON-invariant
    # trace field (trace_field_gens) — show what that proxy gives on the witness pair.
    print("  one-hop wrong-object check — B145's proxy (NON-invariant trace_field_gens) on the pair:")
    for w in ("RRL", "RLL"):
        tf = snappy.Manifold("b++" + w).trace_field_gens().find_field(
            prec=200, degree=12, optimize=True)
        if tf is None:
            print(f"    b++{w}: trace field not identified at prec=200/degree<=12")
        else:
            print(f"    b++{w}: NON-invariant trace field = {tf[0].defining_polynomial()} "
                  f"(degree {tf[0].degree()}) — degree 2? {tf[0].degree() == 2}")
    return imagquad


# ------------------------------------------------------------------------------------
# Verdict logic — the discriminating fact, both directions.
# ------------------------------------------------------------------------------------

def main():
    words = part1_combinatorial()
    amph, pair = part2_geometric()
    imagquad = part3_invariant_trace_fields(words)

    print()
    print("=" * 98)
    print("DISCRIMINATING FACT — evaluation")
    print("=" * 98)
    if imagquad is None:
        print("  BLOCKED at the Sage leg: invariant trace field not recomputed.")
        sys.exit(2)

    # Kill holds iff some in-range bundle has imaginary-quadratic invariant trace field
    # AND is chiral — chirality certified GEOMETRICALLY (Part 2), with the banked
    # combinatorial criterion as cross-check.  Scan words are already cyclic reps
    # (B145 convention: lexicographic min, L < R — so the banked names RRL/RLL appear
    # as classes LRR/LLR); amph is keyed the same way.
    witness_classes = (_cyclic_rep("RRL"), _cyclic_rep("RLL"))  # = ('LRR', 'LLR')
    chiral_iq = [(w, poly, disc) for (w, poly, disc, ap) in imagquad
                 if w in amph and not amph[w]]
    consistent = all((w not in amph) or (amph[w] == ap) for (w, poly, disc, ap) in imagquad)
    print(f"  imaginary-quadratic bundles in range: {[(w, p, d) for w, p, d, _ in imagquad]}")
    print(f"  of these, GEOMETRICALLY chiral (no orientation-reversing self-isometry): {chiral_iq}")
    print(f"  combinatorial criterion agrees with geometry on all checked words: {consistent}")
    print(f"  mirror-pair witness intact (vol/H1 equal, CS flips, unoriented-isometric): "
          f"{pair}")
    kill_holds = (
        len(chiral_iq) > 0
        and any(w in witness_classes and poly == "x^2 - x + 2" and disc == -7
                for (w, poly, disc) in chiral_iq)
        and pair["vol_eq"] and pair["h1_eq"] and pair["cs_flip"]
    )
    print()
    if kill_holds:
        print("  VERDICT LEG: RECONFIRMED — a CHIRAL o-p-t bundle with imaginary-quadratic")
        print("  (arithmetic-necessary) invariant trace field EXISTS in B145's range:")
        print("  b++RRL / b++RLL, invariant trace field x^2 - x + 2 = Q(sqrt(-7)), disc -7.")
        print("  B145's 'every quadratic-trace-field o-p-t bundle is amphichiral' is FALSE")
        print("  at the invariant-trace-field level, exactly as banked by B146.")
    else:
        print("  VERDICT LEG: the banked discriminating fact did NOT recompute — REVIVED path.")
    sys.exit(0 if kill_holds else 1)


if __name__ == "__main__":
    main()
