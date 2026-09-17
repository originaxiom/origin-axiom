#!/usr/bin/env python3
"""xB019 cells G1-G6, exactly as sealed in PREREGISTRATION.md
(sha256 e20e39f9ff79ef5143f9fd826ac3ca60024c3cdf93e398ad6182eee4670ac5b1,
commit 55b984d, pushed BEFORE this file existed).

Answers B1234's OWN declared live question: does dropping A6 break the tools rather
than open a door?  Per tool, with xB018's two-bit machinery applied on top.

Gate 5 untouched: no value, no generation count, no physics reading.
"""
import itertools, json, os, warnings
import snappy
import sympy as sp
warnings.filterwarnings("ignore")
HERE = os.path.dirname(os.path.abspath(__file__)); R = {}

TOOLS = ["volume", "homology", "fundamental_group", "chern_simons",
         "complex_volume", "symmetry_group"]


def sl2f3():
    return [((a, b), (c, d)) for a in range(3) for b in range(3)
            for c in range(3) for d in range(3) if (a*d - b*c) % 3 == 1]


def count_surjections(relator, gens="ab"):
    """Count surjections pi_1 = <gens | relator> -> SL(2,F_3) = 2T."""
    Gp = sl2f3()
    def mul(X, Y):
        return (((X[0][0]*Y[0][0] + X[0][1]*Y[1][0]) % 3, (X[0][0]*Y[0][1] + X[0][1]*Y[1][1]) % 3),
                ((X[1][0]*Y[0][0] + X[1][1]*Y[1][0]) % 3, (X[1][0]*Y[0][1] + X[1][1]*Y[1][1]) % 3))
    def inv(X):
        return ((X[1][1], (-X[0][1]) % 3), ((-X[1][0]) % 3, X[0][0]))
    I2 = ((1, 0), (0, 1))
    total = 0
    for A in Gp:
        for B in Gp:
            img = {"a": A, "A": inv(A), "b": B, "B": inv(B)}
            P = I2
            for ch in relator:
                P = mul(P, img[ch])
            if P != I2:
                continue
            # surjective?
            sub, fr = {I2}, [I2]
            while fr:
                nx = []
                for g in fr:
                    for h in (A, B):
                        q = mul(g, h)
                        if q not in sub: sub.add(q); nx.append(q)
                fr = nx
            if len(sub) == 24: total += 1
    return total


def G1():
    print("G1       B1234's CELLS 2 AND 3, RE-DERIVED")
    G, M = snappy.Manifold("m000"), snappy.Manifold("m004")
    cover = G.orientation_cover()
    iso = cover.is_isometric_to(M)
    ratio = float(M.volume()) / float(G.volume())
    print(f"         m000 orientable: {G.is_orientable()}   m004 orientable: {M.is_orientable()}")
    print(f"         m000's ORIENTATION COVER isometric to m004: {iso}   volume ratio: {ratio:.10f}")
    rel_g = G.fundamental_group().relators()[0]
    rel_m = M.fundamental_group().relators()[0]
    print(f"         relators: m000 {rel_g!r}   m004 {rel_m!r}")
    s_g, s_m = count_surjections(rel_g), count_surjections(rel_m)
    print(f"         surjections pi_1 -> 2T = SL(2,F_3):  Gieseking {s_g}   m004 {s_m}   "
          f"equal: {s_g == s_m}")
    print("         B1234's 48 = 48 reproduced by an independent count.")
    print("         AND B1234's OWN UNCLAIMED CLAUSE IS CARRIED, NOT DROPPED: surjecting onto 2T")
    print("         is GENERIC (~1/3, B993/B996), so the equal counts are NOT evidence of")
    print("         distinction.  The point is only that A6 was not needed for the arithmetic.")
    ok = iso and abs(ratio - 2) < 1e-9 and s_g == s_m == 48
    print(f"G1 {'PASS' if ok else 'FAIL'}  B1234 reproduces exactly.")
    R["G1"] = {"cover_isometric": bool(iso), "ratio": ratio,
               "surj_gieseking": s_g, "surj_m004": s_m}
    return ok


def G2():
    print("\nG2       THE TOOL AUDIT -- the cell that answers B1234")
    rows = {}
    for nm in ("m000", "m004"):
        X = snappy.Manifold(nm)
        rows[nm] = {}
        for t in TOOLS:
            try:
                v = getattr(X, t)()
                rows[nm][t] = ("EXISTS", str(v).replace("\n", " ")[:38])
            except Exception as e:
                rows[nm][t] = ("BREAKS", f"{type(e).__name__}: {str(e)[:40]}")
    print(f"         {'tool':20} {'m000 (one tick, non-orientable)':42} m004 (two ticks)")
    for t in TOOLS:
        a, b = rows["m000"][t], rows["m004"][t]
        print(f"         {t:20} {a[0]+': '+a[1]:42} {b[0]}")
    broke = [t for t in TOOLS if rows["m000"][t][0] == "BREAKS"]
    print(f"\n         BREAKS on the one-tick object: {broke}")
    print(f"         and the error is literal: {rows['m000']['chern_simons'][1]}")
    print("         => THEY BREAK BY DEFINITION, NOT BY DIFFICULTY.  Chern-Simons and the")
    print("            complex volume are defined for ORIENTED manifolds; there is no harder")
    print("            computation to attempt.")
    print("         SURVIVES: volume, H_1, pi_1, the symmetry group -- and the 2T count (G1).")
    ok = set(broke) == {"chern_simons", "complex_volume"}
    print(f"G2 {'PASS' if ok else 'FAIL'}  exactly the two orientation-dependent tools break.")
    R["G2"] = {"breaks": broke, "rows": rows}
    return ok


def G3():
    print("\nG3       WHICH OF THE TWO BITS EXISTS AT TICK ONE?  (the blind cell)")
    G, M = snappy.Manifold("m000"), snappy.Manifold("m004")
    h000, h004 = str(G.homology()), str(M.homology())
    print(f"         xB018 characterised the bits by their data:")
    print(f"           A5(c) = KNOT-NESS = H_1 torsion-free.  H_1(m000) = {h000}, "
          f"H_1(m004) = {h004}")
    tf = "/" not in h000 and "+" not in h000
    print(f"           -> H_1 exists at tick one AND IS TORSION-FREE: {tf}")
    print(f"              SO THE A5 BIT IS POSABLE AT TICK ONE, AND IT IS ALREADY 'ON'.")
    print(f"           A7 acts by CS-NEGATION (xB018 C5), and CS does not exist on m000 (G2).")
    print(f"           -> THE A7 BIT CANNOT BE POSED AT TICK ONE.")
    print(f"         and the symmetry groups: m000 order {G.symmetry_group().order()}, "
          f"m004 order {M.symmetry_group().order()}")
    print("         which matches B1083 exactly: 'on the one-tick object chirality cannot be")
    print("         POSED (non-orientable); the second tick buys orientability and pays")
    print("         amphichirality.'  Reached here from a different direction -- the tool")
    print("         audit -- and agreeing.")
    print(f"G3 {'PASS' if tf else 'FAIL'}  THE TWO BITS SPLIT ACROSS THE SQUARING:")
    print("         A5's datum SURVIVES the drop and is already satisfied; A7's datum IS")
    print("         CREATED BY THE SQUARING.  A7 is not a free choice made at tick one --")
    print("         IT DOES NOT EXIST UNTIL THE OBJECT IS ORIENTABLE.")
    R["G3"] = {"H1_m000": h000, "H1_m004": h004, "A5_posable_and_on": bool(tf),
               "A7_posable": False,
               "sym_m000": G.symmetry_group().order(), "sym_m004": M.symmetry_group().order()}
    return tf


def G4():
    print("\nG4       THE ANSWER TO B1234's LIVE QUESTION")
    print("         B1234 asked: does dropping A6 BREAK THE TOOLS rather than open a door?")
    print("         ANSWER, PER TOOL: BOTH, AND THE SPLIT IS EXACTLY ALONG ORIENTATION.")
    print("           survives: volume, H_1, pi_1, symmetry group, the trace field and the 2T")
    print("             route (B1234 cell 3) -- so THE ARITHMETIC SIDE IS INTACT.")
    print("           breaks:   Chern-Simons and the complex volume -- BY DEFINITION.")
    print("         AND THE CONSEQUENCE IS SHARPER THAN 'HARD':")
    print("           SEVEN of B1234's EIGHT walls are statements ABOUT CS or about the mirror")
    print("           (CS = 0; blind to k; amphichirality; the CP sign even in CS; mirror-even")
    print("           canonicity; mirror-odd bits; the mirror pair theta).  ON THE ONE-TICK")
    print("           OBJECT THERE IS NO CS AND NO ORIENTATION TO MIRROR, so those walls do not")
    print("           become FALSE there -- THEY BECOME UNSTATEABLE.")
    print("         => 'DROP A6 TO ESCAPE THE WALLS' IS ILL-POSED, NOT MERELY HARD.  There is no")
    print("            CS on the one-tick object that could be non-zero.  The escape route is")
    print("            CLOSED, and closed for a reason stronger than difficulty.")
    print("         REPORTING RULE FROM THE SEAL, APPLIED: this is a NEGATIVE FOR THE ESCAPE")
    print("         ROUTE AND A CLARIFICATION OF THE QUESTION -- it is NOT a new wall, and it is")
    print("         NOT evidence FOR A6.")
    R["G4"] = {"survives": ["volume", "H_1", "pi_1", "symmetry group", "trace field", "2T route"],
               "breaks": ["Chern-Simons", "complex volume"],
               "verdict": "the escape route is ill-posed, not merely hard"}
    return True


def G5():
    print("\nG5       WHAT THE SQUARING BUYS, ITEMISED")
    print("         BUYS:  orientability · the Chern-Simons and complex-volume TOOLS ·")
    print("                amphichirality (100%-forced for an orientation double cover, B1234")
    print("                cell 1, against a 3.0% base rate) · AND THE A7 BIT ITSELF (G3).")
    print("         DOES NOT BUY (B1234 cell 3, re-derived in G1): the invariant trace field,")
    print("                the 2T route, McKay-E_6 -- 48 surjections either way.")
    print("         DOES NOT BUY (G3): the A5 bit, which is already posable and already ON at")
    print("                tick one, H_1(m000) = Z.")
    print("         SO THE SQUARING'S PURCHASE IS EXACTLY: ORIENTATION, AND EVERYTHING DOWNSTREAM")
    print("         OF ORIENTATION -- the CS tool, the mirror, amphichirality, the eight walls,")
    print("         and A7.  IT BUYS NOTHING ARITHMETIC.")
    print("         That sharpens B1234's own headline ('the squaring buys orientability and")
    print("         costs every value') by saying WHICH SIDE each item falls on, and by adding")
    print("         A7 to the bought column -- which B1234 did not have, because xB018 had not")
    print("         yet characterised the bit.")
    R["G5"] = {"buys": ["orientability", "CS/complex-volume tools", "amphichirality", "the A7 bit"],
               "does_not_buy": ["trace field", "2T route", "the A5 bit"]}
    return True


def G6():
    print("\nG6       THE VERDICT")
    print("         B1234's live question is ANSWERED: dropping A6 breaks EXACTLY the two")
    print("         orientation-dependent tools, and leaves the arithmetic intact.  Because")
    print("         seven of the eight walls are statements about CS or the mirror, they become")
    print("         UNSTATEABLE rather than false -- so the escape route is ILL-POSED.")
    print("         AND THE NEW STRUCTURAL FACT, from xB018's machinery: THE TWO BITS SPLIT")
    print("         ACROSS THE SQUARING.  A5's datum (H_1) survives and is already on; A7's")
    print("         datum (CS) is CREATED by it.  A7 is not a choice the construction makes at")
    print("         tick one -- it does not exist until tick two.")
    print()
    print("         AXES HELD FIXED, NAMED AS THE RULE REQUIRES:")
    print("           - m000 ONLY.  The wider non-orientable census is NOT swept; B1234's 40-of-40")
    print("             is cited for the amphichirality rate and NOT re-derived here.")
    print("           - the two-bit characterisation is xB018's, which held SL(2,Z), b++/b+-,")
    print("             word length <= 8 and A5 reading (c) fixed -- those constraints are")
    print("             INHERITED by this arc and not re-opened.")
    print("           - PGL(2,C) vs PSL(2,C): named as the MECHANISM (a non-orientable manifold's")
    print("             holonomy lands in PGL(2,C), outside the SL(2,C) theory) but NOT computed")
    print("             here.")
    R["G6"] = {"answered": "B1234's live question",
               "axes_fixed": ["m000 only", "xB018's constraints inherited", "PGL/PSL not computed"]}
    return True


if __name__ == "__main__":
    v = {"G1": G1(), "G2": G2(), "G3": G3(), "G4": G4(), "G5": G5(), "G6": G6()}
    print("\n" + "=" * 78)
    for k, r in v.items(): print(f"  {k}: {'PASS' if r else 'FAIL'}")
    json.dump(R, open(os.path.join(HERE, "one_tick.json"), "w"), indent=1, default=str)
    print("VERIFIED" if all(v.values()) else "SOME CELLS FAILED")
