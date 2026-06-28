"""B266 -- wall #2: the figure-eight's arithmetic CANONICALLY SELECTS E6 (via the ramified prime).
FIREWALLED (arithmetic / rep theory, not physics). Nothing to CLAIMS.md.

The question (wall #2, B259/B260): we kept CHOOSING E6 as the 3d-3d "type". Is E6 actually SELECTED by the
figure-eight, or imposed by hand? There were two E6's: the "input-E6" (the 6d (2,0) type we picked) and the
"output-McKay-E6" (E6 attached to the trace field Q(sqrt-3) via McKay). This probe shows the output-E6 is NOT
arbitrary -- it is forced by the unique ramified prime of the trace field, through a chain of theorems.

THE SELECTION CHAIN (each link a theorem; all verified):
  1. figure-eight invariant trace field = Q(sqrt-3)         [SnapPy: min poly x^2-2x+4, disc -3; classical
     Maclachlan-Reid]. The Riley rep is manifestly over Z[omega] (t = 1+omega, t^2-t+1=0), O_3 = Z[omega].
  2. Q(sqrt-3) has discriminant -3; its UNIQUE ramified prime is 3; the residue field at p=(sqrt-3) is F_3.
  3. reduction mod p:  the figure-eight group ->> SL(2,F_3)  (the Riley rep mod (sqrt-3): omega==1, t==2,
     so a=[[1,1],[0,1]], b=[[1,0],[2,1]] -- two parabolics that GENERATE all of SL(2,F_3), order 24). VERIFIED.
  4. SL(2,F_3) = 2T  (binary tetrahedral group, order 24).                                     [classical]
  5. McKay(2T) = affine E6  (7 nodes, marks {1,1,1,2,2,2,3}).                       [GAP, mckay_selection_sage]

So E6 is CANONICALLY attached to the figure-eight's arithmetic.

WHY E6 AND NOT ANOTHER TYPE (the canonicity, + the two-ended structure recovered):
  * SL(2,F_q) is binary-polyhedral (a McKay/ADE group) ONLY for q in {3,5}: -> 2T/E6 and 2I/E8. (q=2 gives
    S_3; q>=7 gives groups far too large.)
  * For Q(sqrt-3) only 3 ramifies (5 is inert -> F_25, huge), so the UNIQUE McKay-reduction is mod 3 -> 2T -> E6.
  * The OTHER arithmetic end Q(sqrt5) (the spherical / det-5 end, B247-B261) ramifies at 5 -> SL(2,F_5)=2I -> E8.
    => the two-ended E6/E8 structure = the two ramified-prime reductions of the two end-fields.
  * E7 (= McKay of 2O, binary octahedral) is HOMELESS: |2O|=48 is never an SL(2,q) order q(q^2-1), so 2O is no
    prime reduction of any such arithmetic group. This reproduces B256 ("E7 geometrically homeless") from one
    mechanism.

CONVERTS WALL #2: from "input-E6 (chosen) vs output-E6 (McKay), link unknown/arbitrary" to "the output-E6 is
CANONICALLY selected by the trace field's ramified prime (theorems), and the figure-eight group itself surjects
onto 2T=McKay-E6." HONEST GUARDRAIL (verify-don't-trust): nothing in the 3d-3d framework forces the 6d INPUT type
to equal McKay(reduction mod the ramified prime); that identification stays a CONJECTURE -- but now a sharp,
motivated one, not an arbitrary imposition. Wall #2 is reframed (and half-closed), not eliminated.

Run: python arithmetic_selects_e6.py  (pyenv; pure python + sympy). McKay graphs reproduced by sage-python
mckay_selection_sage.py.
"""
import sympy as sp

# affine ADE marks (= dims of the binary-polyhedral group's irreps); from mckay_selection_sage.py + classical.
MCKAY = {
    "2T": {"as_SL2Fq": 3, "order": 24, "affine_type": "E6", "marks": [1, 1, 1, 2, 2, 2, 3]},
    "2I": {"as_SL2Fq": 5, "order": 120, "affine_type": "E8", "marks": [1, 2, 2, 3, 3, 4, 4, 5, 6]},
    "2O": {"as_SL2Fq": None, "order": 48, "affine_type": "E7", "marks": [1, 1, 2, 2, 2, 3, 3, 4]},
}
AFFINE_MARKS = {"E6": [1, 1, 1, 2, 2, 2, 3], "E7": [1, 1, 2, 2, 2, 3, 3, 4], "E8": [1, 2, 2, 3, 3, 4, 4, 5, 6]}


def fig8_mod3_order():
    """Order of the figure-eight group's image under the Riley rep reduced mod the ramified prime (sqrt-3).
    omega == 1 mod (sqrt-3) => t = 1+omega == 2; a,b are two parabolics over F_3."""
    a = ((1, 1), (0, 1)); b = ((1, 0), (2, 1))

    def mul(x, y):
        return tuple(tuple(sum(x[i][k] * y[k][j] for k in range(2)) % 3 for j in range(2)) for i in range(2))

    S = {((1, 0), (0, 1))}; frontier = list(S)
    while frontier:
        nf = []
        for g in list(S):
            for h in (a, b):
                p = mul(g, h)
                if p not in S:
                    S.add(p); nf.append(p)
        frontier = nf
    return len(S)


def sl2_order(q):
    """|SL(2,F_q)| = q(q^2-1)."""
    return q * (q * q - 1)


def ramified_prime_and_residue(d):
    """For Q(sqrt d) (squarefree d): discriminant, the ramified prime(s), and the residue field order.
    disc = d if d=1 mod 4 else 4d; ramified primes = primes | disc; at a ramified prime e=2,f=1 -> residue F_p."""
    disc = d if d % 4 == 1 else 4 * d
    ram = [int(p) for p in sp.primefactors(abs(disc))]
    return disc, {p: p for p in ram}          # residue field order = p (f=1 at a ramified prime)


if __name__ == "__main__":
    print("=== B266: the figure-eight's arithmetic selects E6 (via the ramified prime) ===\n")

    # link 3: the figure-eight group surjects onto SL(2,F_3) = 2T = McKay E6
    o = fig8_mod3_order()
    print(f"figure-eight Riley rep mod (sqrt-3): image order = {o} = |SL(2,F_3)| = {sl2_order(3)}  "
          f"-> surjects onto 2T: {o == sl2_order(3) == 24}")

    # links 4-5: McKay graphs (from GAP), matched to affine ADE marks
    print("\nMcKay correspondence (binary polyhedral -> affine ADE):")
    for g, info in MCKAY.items():
        ok = sorted(info["marks"]) == sorted(AFFINE_MARKS[info["affine_type"]])
        fq = f"SL(2,{info['as_SL2Fq']})" if info["as_SL2Fq"] else "(not any SL(2,q))"
        print(f"  {g} {fq:>13}  order {info['order']:>3}  -> affine {info['affine_type']}  marks {info['marks']}  match:{ok}")
        assert ok

    # canonicity: SL(2,F_q) binary-polyhedral only for q in {3,5}; ramified primes of the two end-fields
    print("\nramified-prime reductions of the two arithmetic ends:")
    for d, end in [(-3, "hyperbolic [figure-eight]"), (5, "spherical [det-5 end]")]:
        disc, res = ramified_prime_and_residue(d)
        for p, fo in res.items():
            bp = {3: "2T -> E6", 5: "2I -> E8"}.get(fo, "(not binary-polyhedral)")
            print(f"  Q(sqrt{d:>2}) {end:24} disc={disc:>3}, ramified at {p}: residue F_{fo} -> SL(2,F_{fo}) = {bp}")

    # E7 homelessness: 2O is never SL(2,q)
    print(f"\nE7 (2O, order 48): is 48 an SL(2,q) order? "
          f"{48 in [sl2_order(q) for q in range(2, 30)]}  -> 2O has NO prime-reduction home (B256 E7-homeless)")
    assert 48 not in [sl2_order(q) for q in range(2, 30)]
    assert MCKAY["2T"]["affine_type"] == "E6" and fig8_mod3_order() == 24
    print("\n=> output-E6 is canonically selected by the trace field's ramified prime (not arbitrary).")
    print("   Open (sharp conjecture): whether the 3d-3d INPUT type must equal this E6. Wall #2 reframed. ALL PASS")
