"""B266 verification (R6 addendum, 2026-06-28): the E6 vs E8 ends are arithmetically ASYMMETRIC at the GROUP level.

Re-confirms the load-bearing E6 leg (pi_1(4_1) DOES surject onto SL(2,F_3)=2T) AND verifies an incoming
deep-research finding (Stuebner 2025, arXiv:2502.06488): pi_1(4_1) does NOT surject onto A_5 = PSL(2,5), hence not
onto its double cover 2I = SL(2,F_5). So the figure-eight has a genuine GROUP surjection only at the E6 end; the E8
end (det=5, Q(sqrt5)) is a FIELD-level coincidence of the spherical companion, not a surjection of pi_1(4_1).

Method: GAP GQuotients (surjections up to automorphism) on the SnapPy figure-eight presentation.
Run: sage-python verify_surjections.py   (needs SnapPy + GAP via Sage).
"""
import snappy
from sage.all import gap


def surjection_counts():
    M = snappy.Manifold("4_1")
    G = M.fundamental_group()
    gens, rels = G.generators(), G.relators()
    gap.eval("F := FreeGroup({});".format(", ".join('"%s"' % g for g in gens)))
    relstr = []
    for r in rels:
        s = ""
        for ch in r:
            if ch.islower():
                s += "F.%d*" % (ord(ch) - ord("a") + 1)
            else:
                s += "F.%d^-1*" % (ord(ch.lower()) - ord("a") + 1)
        relstr.append(s.rstrip("*"))
    gap.eval("G := F / [{}];".format(", ".join(relstr)))
    return {
        "2T = SL(2,3)": int(gap.eval("Length(GQuotients(G, SL(2,3)));")),
        "A5 = PSL(2,5)": int(gap.eval("Length(GQuotients(G, AlternatingGroup(5)));")),
        "2I = SL(2,5)": int(gap.eval("Length(GQuotients(G, SL(2,5)));")),
    }


# Verified result (2026-06-28, sage-python + GAP):
EXPECTED = {"2T = SL(2,3)": 2, "A5 = PSL(2,5)": 0, "2I = SL(2,5)": 0}

if __name__ == "__main__":
    c = surjection_counts()
    print("pi_1(4_1) surjections (up to Aut):", c)
    print("E6 leg (2T):", "GENUINE" if c["2T = SL(2,3)"] > 0 else "ABSENT")
    print("E8 leg (2I):", "ABSENT (field-level only)" if c["2I = SL(2,5)"] == 0 else "present")
    assert c == EXPECTED, (c, EXPECTED)
    print("OK -- E6/E8 ends asymmetric at the group level (confirms Stuebner 2025).")
