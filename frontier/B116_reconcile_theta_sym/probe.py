"""B116 -- reconcile the theta-split (B112) with the Sym two-sequence (B103): they DIVERGE at n=6.

The reconciliation B112 <-> B103 (run on request). It was meant to JOIN the two halves of the rho_n prize; what
it actually found is a CORRECTION to B112's all-n claim (verify-don't-trust, banked as an explicit downgrade like
V90/V91).

THE TWO DECOMPOSITIONS of the (n^2-1)-dim trivial-point tower:
  * theta-split (B62/B112): the opposition involution -w0 on the A_{n-1} root spaces -- B112 PROVED its
    eigenspace combinatorics are ceil((n-h)/2) / floor((n-h)/2) for ALL n.
  * Sym two-sequence (B103/B58, V27 membership rule): the tower = (+)_d Sym^d(M)^{mu_d}, mu_d=[2<=d<=n]+[0<=d<=n-3];
    sym_counts(n) gives its char(+-M^h) multiplicities. B103 PROVED this is the EXACT module-iso at n=3,4.

THE FINDING:
  (1) The Sym two-sequence = the ACTUAL TOWER. sym_counts(5) = {char(M^h): 1->2,2->2,3->1,4->1,5->1;
      char(-M^h): 1->1,2->1,3->1} EXACTLY matches the resolved SL(5) tower (B61 22/24 + B62's 2): it includes
      char(M^5) (the degree=rank top power) automatically (= Sym^5's top weight) -- no separate 'promotion' needed.
  (2) The theta-split EQUALS the Sym two-sequence (hence the tower) ONLY for n<=5; at n>=6 they DIVERGE -- exactly
      the banked V26/V27 result: a_1 (char M) Sym 2 vs theta 3; a_2 Sym 3 vs theta 2; b_2 (char -M^2) Sym 1 vs
      theta 2 (the parity is swapped). They still AGREE on the contested a_3(n=6)=2 (a second independent vote).

THE CORRECTION TO B112 (explicit downgrade, NOT silent): B112 proves the theta-split COMBINATORICS (a real
A_{n-1} root-system theorem) for all n. But the IDENTIFICATION of the theta-split with the TOWER's char-
multiplicities -- the long-standing V25 unproven step -- holds only for n<=5 (verified against the exact n<=4
tower + the SL(5) data) and is CONTESTED at n>=6 (the theta-split <-> Sym divergence). So B112 is 'the sign half
proved for n<=5', NOT 'for all n'; the all-n sign half is OPEN, blocked by the same theta-split-vs-Sym
divergence that needs the ambient SL(n) trace ring (the perennial wall). The Sym two-sequence is the better
tower-candidate (it = the actual tower wherever the tower is known), and proving IT for all n (B103's open
problem) is the live route -- not the theta-split.

Standalone trace-map / Lie theory; NO physics; no CLAIMS.md promotion; the rho_n proof stays the prize; P1-P16
untouched.
"""
from __future__ import annotations

import importlib.util
import math
import pathlib
import sys

_ROOT = pathlib.Path(__file__).resolve().parents[2]


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, _ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


_SYM = _load("b116_sym", "frontier/B58_phaseA/sym_decomposition.py")

# The resolved SL(5) tower (B61 22/24 + B62 structural), as char(M^h)/char(-M^h) multiplicities.
_SL5_TOWER_A = {1: 2, 2: 2, 3: 1, 4: 1, 5: 1}     # char(M^h)
_SL5_TOWER_B = {1: 1, 2: 1, 3: 1}                  # char(-M^h)


def sym_two_sequence(n):
    """char(M^h) / char(-M^h) multiplicities from the Sym two-sequence (B103/B58, V27 membership rule)."""
    a, b = _SYM.sym_counts(n)
    return dict(sorted(a.items())), dict(sorted(b.items()))


def theta_split(n):
    """char(M^h) / char(-M^h) multiplicities from the theta-split eigenspace dims (B112), heights 1..n-1."""
    a = {h: math.ceil((n - h) / 2) for h in range(1, n)}
    b = {h: math.floor((n - h) / 2) for h in range(1, n)}
    return {h: v for h, v in a.items() if v}, {h: v for h, v in b.items() if v}


def sym_equals_sl5_tower():
    """The Sym two-sequence reproduces the resolved SL(5) tower EXACTLY (incl. char(M^5), the degree=rank top)."""
    a, b = sym_two_sequence(5)
    return {"sym_a": a, "sym_b": b, "sl5_a": _SL5_TOWER_A, "sl5_b": _SL5_TOWER_B,
            "matches": a == _SL5_TOWER_A and b == _SL5_TOWER_B, "has_top_char_M5": a.get(5, 0) == 1}


def agreement_table(nmax=8):
    """Per-n: do the theta-split and Sym agree on heights 2..n-1 (i.e. up to the single height-1 degree=rank
    promotion)? They agree for n<=5 (Sym = theta-split + one promotion) and DIVERGE for n>=6 (they differ at
    heights >= 2, so the difference is no longer a single promotion)."""
    out = {}
    for n in range(3, nmax + 1):
        sa, sb = sym_two_sequence(n)
        ta, tb = theta_split(n)
        # heights 2..n-1 (above the height-1 promotion); the theta-split has no height-n term by construction
        agree = all(sa.get(h, 0) == ta.get(h, 0) and sb.get(h, 0) == tb.get(h, 0) for h in range(2, n))
        out[n] = {"agree_heights_2_to_nminus1": agree, "sym_a": sa, "theta_a": ta, "sym_b": sb, "theta_b": tb}
    return out


def differ_by_single_promotion(n):
    """n<=5: Sym = theta-split with exactly one height-1 char promoted to char(M^n) (agree on heights 2..n-1,
    differ by 1 at height 1, plus Sym's char(M^n)). n>=6: NOT a single promotion (differ at heights >= 2)."""
    sa, sb = sym_two_sequence(n)
    ta, tb = theta_split(n)
    agree_above = all(sa.get(h, 0) == ta.get(h, 0) and sb.get(h, 0) == tb.get(h, 0) for h in range(2, n))
    h1_diff = (ta.get(1, 0) - sa.get(1, 0)) + (tb.get(1, 0) - sb.get(1, 0))   # theta has one extra at h=1
    has_top = sa.get(n, 0) == 1
    return agree_above and h1_diff == 1 and has_top


def divergence_at_n6():
    """The theta-split and Sym diverge at n=6 -- reproduces the banked V26/V27 (a_1 2v3, a_2 3v2, b_2 1v2)."""
    sa, sb = sym_two_sequence(6)
    ta, tb = theta_split(6)
    return {"a1_sym_vs_theta": (sa.get(1, 0), ta.get(1, 0)), "a2_sym_vs_theta": (sa.get(2, 0), ta.get(2, 0)),
            "b2_sym_vs_theta": (sb.get(2, 0), tb.get(2, 0)),
            "a3_both": (sa.get(3, 0), ta.get(3, 0)),     # both 2 -- the agreed contested mode
            "diverge": (sa.get(1, 0), sa.get(2, 0), sb.get(2, 0)) != (ta.get(1, 0), ta.get(2, 0), tb.get(2, 0))}


def b112_correction():
    """The explicit downgrade of B112's all-n claim."""
    return {"b112_proves": "the theta-split eigenspace COMBINATORICS (ceil/floor) for all n -- a real A_{n-1} theorem",
            "identification_with_tower": "holds for n<=5 (verified vs the exact n<=4 tower + SL(5) data); "
                                         "CONTESTED at n>=6 (theta-split <-> Sym diverge, V26/V27)",
            "corrected_claim": "B112 is the sign half proved for n<=5, NOT for all n; the all-n sign half is OPEN",
            "live_route": "the Sym two-sequence (B103) = the actual tower wherever known; proving IT for all n "
                          "(B103's open problem) is the route, not the theta-split"}


def main():
    print("=" * 78)
    print("B116 -- reconcile theta-split (B112) vs Sym two-sequence (B103): they DIVERGE at n=6")
    print("=" * 78)
    s = sym_equals_sl5_tower()
    print(f"\n[1] Sym two-sequence == the resolved SL(5) tower: {s['matches']} (has char(M^5) top: {s['has_top_char_M5']})")
    print(f"    Sym n=5: char(M^h) {s['sym_a']}  char(-M^h) {s['sym_b']}")
    print("\n[2] theta-split vs Sym: differ by a single degree=rank promotion? (agree on heights 2..n-1):")
    for n, r in agreement_table(8).items():
        print(f"    n={n}: agree heights 2..n-1 = {r['agree_heights_2_to_nminus1']}  "
              f"(single-promotion: {differ_by_single_promotion(n)})")
    d = divergence_at_n6()
    print(f"\n[3] divergence at n=6 (Sym vs theta): a_1 {d['a1_sym_vs_theta']}, a_2 {d['a2_sym_vs_theta']}, "
          f"b_2 {d['b2_sym_vs_theta']}  (a_3 both {d['a3_both']}) -- matches V26/V27")
    c = b112_correction()
    print("\n[CORRECTION to B112] (explicit downgrade, verify-don't-trust):")
    for k, v in c.items():
        print(f"    {k}: {v}")
    print("\nVERDICT: the Sym two-sequence is the actual tower; the theta-split (B112) = the tower only n<=5 and")
    print("diverges at n=6. B112's 'sign half all n' -> 'sign half n<=5; all-n OPEN'. The Sym proof is the route.")


if __name__ == "__main__":
    main()
