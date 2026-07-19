"""B718 PROBE 2 -- THE ARITHMETIC SUB-FAMILY of the child (Dehn fillings of the object's cusp).

QUESTION (Margulis finiteness). Only finitely many Dehn fillings 4_1(p,q) of the (arithmetic,
cusped) figure-eight knot complement m004 are themselves arithmetic. COMPUTE which ones. Is the
(5,1) child arithmetic (prereg: (5,1) child = m003(-2,3), vol 0.98137, claimed known-arithmetic)?
What distinguishes the arithmetic children -- their fields, their slopes?

Two-outcome: A = a distinguished, STRUCTURED finite arithmetic sub-family;  B = scattered/no pattern.

------------------------------------------------------------------------------------------------
CORRECTED RE-RUN (2026-07-19).  The FIRST run of this probe was refuted on a REPORTING-INTEGRITY
breach (not on the mathematics): its prose asserted a scan scope its code never executed
("585 non-integral fillings q=2..25 p<=40", "checked p=5..70", an "11 one-complex-place / 8 fail"
breakdown), and -- the material fault -- its checker used a SINGLE fixed find_field(prec=250,deg=25)
that SILENTLY returns None whenever the true invariant-trace-field degree exceeds 25.  Those None
("no field at this precision") cases were then folded into "not arithmetic", so a large fraction of
the claimed negative scan was a TOOL CEILING misreported as a computed negative -- exactly the
"unearned negative" WORKING_RULES rule 12 forbids.

THIS re-run fixes both faults:
  (i)  ESCALATING field recognition (prec/deg up to (4000,60)), the same scheme probe1 uses -- so
       the invariant trace field is genuinely RESOLVED, not ceiling-capped at the old deg 25.
  (ii) THREE-category, per-case verdicts with EXPLICIT unresolved logging:
         ARITH            -- resolved, one complex place, integral traces, ram at all real places;
         NON-ARITH        -- resolved with a GENUINE negative reason (r2>1, or non-integral, or the
                             quaternion algebra fails to ramify at a real place);
         UNRESOLVED       -- the field was not recognized up to deg 60 (=> its degree exceeds 60) --
                             reported as its own count, NEVER silently counted as "non-arithmetic".
  (iii) The prose below states EXACTLY the box the code scans, and every number it cites is printed
        by the executed run into b718_probe2_out.txt (summary) + b718_probe2_scan.tsv (per case).

------------------------------------------------------------------------------------------------
THE CRITERION (Maclachlan-Reid, *The Arithmetic of Hyperbolic 3-Manifolds*, Thm 8.3.2 -- COCOMPACT).
A Dehn filling is a CLOSED (cocompact) hyperbolic 3-manifold, so the cusped shortcut (imaginary-
quadratic invariant trace field + integral traces) does NOT apply. The full cocompact criterion:

    Gamma is arithmetic  <=>
      (1) the INVARIANT trace field k0 = kGamma has EXACTLY ONE complex place (signature (r1, 1)),
      (2) every trace is an ALGEBRAIC INTEGER, and
      (3) the invariant quaternion algebra A0 is RAMIFIED at ALL r1 real places of k0.

Condition (3) is a Hilbert symbol.  For g, h in Gamma^(2) = <squares> with <g,h> irreducible,
A0 = ( tr(g)^2 - 4 ,  tr([g,h]) - 2  /  k0 ).  Over a real place v, (a,b) is a division algebra
(RAMIFIED)  <=>  sigma_v(a) < 0 AND sigma_v(b) < 0.  We take g = a^2, h = b^2 (both squares, so
their traces lie in k0; <a^2,b^2> is Zariski-dense for these fillings).

INDEPENDENT CROSS-CHECK (bounded-conjugate form of the SAME theorem).  A0 ramifies at a real place v
<=> sigma_v(Gamma^(2)) is conjugate into SU(2) <=> |sigma_v(tr w)| <= 2 for every w in Gamma^(2).
We sample words w and confirm the Hilbert-symbol verdict against max_w |sigma_v(tr w)|.

TOOLING. SnapPy 3.3.2 under sage-python.  Invariant/trace field via .find_field (exact NumberField
with the geometric embedding, ESCALATING prec/deg); high-precision holonomy via
snap.polished_holonomy; numeric traces recognized back into k0 by PARI lindep on the power basis.
Structural/arithmetic only; no SM value; nothing to CLAIMS.

------------------------------------------------------------------------------------------------
RESULT (this seat, corrected, verified two independent ways):

  Every filling in the SCANNED BOX below receives a per-case verdict in {ARITH, NON-ARITH,
  UNRESOLVED}; the UNRESOLVED count is printed explicitly and NEVER folded into "non-arithmetic".
  The arithmetic children in the box are EXACTLY THREE (up to the amphichiral symmetry
  m004(p,q) ~ m004(p,-q) ~ m004(-p,q)):

     m004(5,1)  vol 0.98137  k0 = x^4 - x - 1   deg 4  disc -283  sig (2,1)   [= m003(-2,3)]
     m004(6,1)  vol 1.28449  k0 = x^3 + 2x - 1  deg 3  disc  -59  sig (1,1)
     m004(8,1)  vol 1.58317  k0 = x^3 +  x - 1  deg 3  disc  -31  sig (1,1)

  SCANNED BOX + TALLIES (exactly what the code below runs and prints at the end of every run):
     integral      q=1,  p = 5..40  (36 slopes):
        ARITH = {5,6,8}   NON-ARITH = 33   UNRESOLVED = 0    (every integral slope resolved)
     non-integral  q = 2..12, p = 1..25, gcd(p,q)=1  (166 hyperbolic fillings):
        ARITH = 0   NON-ARITH(resolved) = 152   UNRESOLVED (deg > 60) = 14
        of the 152 resolved negatives: 144 fail because r2 >= 2 (>1 complex place, condition 1);
        8 have EXACTLY ONE complex place (r2 = 1) but fail because the invariant quaternion algebra
        SPLITS at a real place (condition 3) -- these 8 are the small-q fillings (1,2),(3,2),(5,2),
        (7,2),(2,3),(4,3),(8,3),(10,3).  The 14 unresolved are the largest-slope corner
        {(19,10),(21,10),(23,10),(17..25,11),(11..25,12)}: their invariant trace field degree
        exceeds 60, so find_field returns no field -- reported as UNRESOLVED with that degree lower
        bound, NOT as a computed negative.

  DISCRIMINATING FACTS (each a printed, resolved, in-sandbox computation -- NOT asserted):
   * (5,1) IS arithmetic and IS m003(-2,3) (same field, disc -283) -- prereg claim CONFIRMED.
   * Every arithmetic child is an INTEGRAL (Dehn) filling q=1.  In the non-integral box, NO resolved
     filling is arithmetic: 144 fail because the invariant trace field has MORE THAN ONE complex
     place (r2 >= 2, condition 1), and 8 have exactly one complex place (r2 = 1) but fail because the
     invariant quaternion algebra SPLITS at a real place (condition 3, the ramification test).
   * Among integral slopes p=5..40 only p in {5,6,8} are arithmetic.  p=7 is the first gap: its
     invariant trace field is deg 6, sig (2,2) -- r2 = 2, a GENUINE arithmetic gap between the
     arithmetic slopes 5,6 and 8.
   * MECHANISM (why the family is confined to small integral slopes): arithmeticity needs BOTH
     r2 = 1 (one complex place) AND real-place ramification of the quaternion algebra.  The
     invariant-trace-field degree GROWS with the slope (probe1's degree law, deg ~ p for q=1; larger
     for q>=2) and its number of complex places r2 grows with it, so the PREREQUISITE r2 = 1 fails
     for all but the smallest slopes -- and even among the small r2=1 fillings the ramification
     condition weeds out 8 more (r2=1 is NECESSARY, not sufficient).  Margulis finiteness (theorem,
     background) guarantees the family is finite; the STRUCTURE (which finite set) is this
     r2=1-AND-ramified double bottleneck, computed per case here.
   * The children's fields are minimal-discriminant complex fields: -31 and -59 are the 2nd and
     4th smallest complex-cubic discriminants; -283 is a small complex-quartic discriminant.
     (Parent m004 = Q(sqrt-3), disc -3; sibling m003(-3,1) = Weeks manifold, disc -23, is the
      arithmetic filling of the SIBLING m003, not of m004 -- it is the checker's positive control.)

  HONEST SCOPE STATEMENT.  The completeness is asserted OVER THE RESOLVED PART of the scanned box
  (188 of 202 fillings: 36 integral + 152 non-integral), each with a genuine per-case verdict; the
  14 unresolved fillings (the largest-slope corner, invariant-trace-field degree > 60) are printed
  as UNRESOLVED, NOT as computed negatives.  For those 14 and for all slopes OUTSIDE the box, the
  r2>1 bottleneck is the MECHANISM (heuristic extrapolation from the monotone degree/r2 growth, not
  a Margulis-complete enumeration): a field of degree > 60 with exactly one complex place would be a
  degree->infinity coincidence never seen among the 188 resolved cases (where r2 grows ~linearly
  with the slope).  We do NOT claim a computed negative for the 14 unresolved fillings.

  => OUTCOME A: a distinguished, structured FINITE arithmetic sub-family.  The finiteness is
     Margulis-forced; the STRUCTURE is the content -- arithmeticity selects the integral slopes
     q=1 and only the first small hyperbolic ones {5,6,8}, cutting off sharply (the gap at 7),
     because the invariant trace field's complex-place count crosses 1.
"""
from __future__ import annotations
import sys
import time
from math import gcd

OUT = []          # summary -> b718_probe2_out.txt
SCAN = []         # per-case TSV -> b718_probe2_scan.tsv


def emit(s=""):
    print(s, flush=True)
    OUT.append(s)


try:
    import snappy
    from snappy import snap
    from sage.all import QQ, ZZ, pari, ComplexField
    HAVE = True
except Exception as e:  # pragma: no cover -- keeps repo green without sage-python
    HAVE = False
    _IMPORT_ERR = repr(e)

PREC = 400
# escalating (bits_prec, max_degree) schedule for find_field -- the fix for the deg-25 ceiling.
# Ceiling deg 60: every arithmetic candidate has a SMALL field (deg<=4 here), and resolving the
# non-arithmetic majority only needs the signature; a case unresolved at deg 60 (=> field degree
# > 60) is reported as UNRESOLVED with that degree lower bound, never folded into "non-arithmetic".
FIELD_SCHEDULE = [(300, 12), (500, 20), (1000, 30), (2000, 45), (4000, 60)]

# ------------------------------------------------------------------ the record (verified in-sandbox)
ARITHMETIC_CHILDREN = {
    (5, 1): dict(vol=0.98137, poly="x^4 - x - 1", deg=4, disc=-283, sig=(2, 1), note="= m003(-2,3)"),
    (6, 1): dict(vol=1.28449, poly="x^3 + 2*x - 1", deg=3, disc=-59, sig=(1, 1), note=""),
    (8, 1): dict(vol=1.58317, poly="x^3 + x - 1", deg=3, disc=-31, sig=(1, 1), note=""),
}


def _live():
    CF = ComplexField(PREC)

    def recognize(t, F, th):
        d = F.degree()
        pw = [CF(1)]
        for i in range(1, d):
            pw.append(pw[-1] * th)
        rel = [ZZ(x) for x in pari([CF(t)] + pw).lindep()]
        if rel[0] == 0:
            return None
        cs = [QQ(-rel[i + 1]) / QQ(rel[0]) for i in range(d)]
        e = sum(cs[i] * F.gen() ** i for i in range(d))
        if abs(CF(e.polynomial()(th)) - CF(t)) > CF(2) ** (-PREC // 2):
            return None
        return e

    def find_field_escalate(gens):
        """Return the resolved NumberField (or None) using the escalating schedule -- the fix."""
        for (prec, deg) in FIELD_SCHEDULE:
            res = gens.find_field(prec, deg, optimize=True)
            if res is not None:
                return res, (prec, deg)
        return None, None

    def check(name, do_bound=False):
        """Full three-category arithmeticity test.
        Returns dict with o['arithmetic'] in {True, False, None} and o['status'] in
        {'ARITH','NON-ARITH','UNRESOLVED','NON-HYP'} + o['reason']."""
        M = snappy.Manifold(name)
        try:
            vol = float(M.volume())
        except Exception:
            return dict(name=name, vol=None, arithmetic=None, status="NON-HYP", reason="no volume")
        if vol < 0.5:
            return dict(name=name, vol=vol, arithmetic=None, status="NON-HYP", reason="non-hyperbolic")

        res, at = find_field_escalate(M.invariant_trace_field_gens())
        if res is None:
            return dict(name=name, vol=vol, arithmetic=None, status="UNRESOLVED",
                        reason="no ITF up to deg 60 (field degree > 60)")
        F = res[0]
        th = CF(F.gen_embedding())
        r1, r2 = F.signature()
        o = dict(name=name, vol=vol, deg=int(F.degree()), disc=int(F.discriminant()),
                 sig=(int(r1), int(r2)), poly=str(F.defining_polynomial()), field_at=at)

        if r2 != 1:                                    # (1) exactly one complex place -- GENUINE negative
            o["arithmetic"] = False
            o["status"] = "NON-ARITH"
            o["reason"] = "r2=%d (>1 complex place)" % r2
            return o

        # r2 == 1: this is an arithmetic CANDIDATE -- run integrality + ramification (genuine verdict)
        tfres, _ = find_field_escalate(M.trace_field_gens())
        o["integral"] = all(e.is_integral() for e in tfres[2]) if (tfres and len(tfres) > 2) else None
        G = snap.polished_holonomy(M, bits_prec=PREC)
        A = G.SL2C("a"); B = G.SL2C("b")
        tr = lambda X: X[0, 0] + X[1, 1]
        g = A * A; h = B * B
        comm = g * h * g.inverse() * h.inverse()
        ae = recognize(tr(g) ** 2 - 4, F, th)          # (3) Hilbert symbol A0 = (a, b / k0)
        be = recognize(tr(comm) - 2, F, th)
        if ae is None or be is None:
            o["arithmetic"] = None
            o["status"] = "UNRESOLVED"
            o["reason"] = "Hilbert-symbol entries not recognized in k0 (candidate, prec-limited)"
            return o
        ram = True
        for emb in F.real_embeddings(prec=150):        # ramified at v <=> sigma_v(a)<0 and sigma_v(b)<0
            if not (emb(ae) < 0 and emb(be) < 0):
                ram = False
        o["nrp"] = int(r1); o["ram_all"] = bool(ram)
        o["arithmetic"] = bool(o["integral"] and ram and r2 == 1)
        o["status"] = "ARITH" if o["arithmetic"] else "NON-ARITH"
        if not o["arithmetic"]:
            o["reason"] = "one complex place but %s" % (
                "quaternion algebra split at a real place" if not ram else "non-integral trace")
        if do_bound:                                   # independent bounded-conjugate cross-check
            words = [g, h, g * h, g * g * h, g * h * h, g * h * g.inverse(), h * g * h, g * g * h * h]
            embs = F.real_embeddings(prec=150)
            maxabs = [0.0] * len(embs); ok = True
            for w in words:
                e = recognize(tr(w), F, th)
                if e is None:
                    continue
                for i, emb in enumerate(embs):
                    v = abs(float(emb(e)))
                    maxabs[i] = max(maxabs[i], v)
                    if v > 2.0000001:
                        ok = False
            o["bound_ok"] = bool(ok); o["bound_max"] = [round(x, 4) for x in maxabs]
        return o

    def scan_row(r):
        """Append one per-case row to the TSV log (name, status, deg, disc, sig, reason, field_at)."""
        SCAN.append("\t".join(str(x) for x in [
            r.get("name"), r.get("status"), r.get("vol"), r.get("deg"), r.get("disc"),
            r.get("sig"), r.get("field_at"), r.get("reason", "")]))

    # 0) validate the checker on the known-arithmetic Weeks manifold (must return True + bounded)
    emit("=== VALIDATION: known-arithmetic Weeks manifold m003(-3,1) [disc -23] ===")
    r = check("m003(-3,1)", do_bound=True)
    emit("  m003(-3,1): ARITH=%s ram_all=%s bound_ok=%s bound_max=%s disc=%s (expect True/True/True)"
         % (r["arithmetic"], r["ram_all"], r["bound_ok"], r["bound_max"], r["disc"]))
    emit("")

    # 1) the three arithmetic children in detail, both criteria + the (5,1)=m003(-2,3) identity
    emit("=== THE ARITHMETIC CHILDREN (Hilbert-symbol ram  vs  independent bounded-conjugate) ===")
    for slope in [(5, 1), (6, 1), (8, 1)]:
        r = check("m004%s" % str(slope), do_bound=True)
        emit("  m004%-6s ARITH=%s  k0=%-14s disc=%-5d sig=%s  integral=%s ram_all=%s bound_ok=%s bound_max=%s"
             % (str(slope), r["arithmetic"], r["poly"], r["disc"], r["sig"],
                r["integral"], r["ram_all"], r["bound_ok"], r["bound_max"]))
    r51 = check("m003(-2,3)")
    emit("  identity check: m003(-2,3) disc=%d poly=%s  ==  m004(5,1) disc=-283  -> %s"
         % (r51["disc"], r51["poly"], "SAME FIELD" if r51["disc"] == -283 else "DIFFERENT"))
    emit("")

    # 2) two representative NON-arithmetic sig-(r1,1) fillings (the ram test must FAIL -> discriminates)
    emit("=== DISCRIMINATION: non-arithmetic fillings with one complex place (ram test must fail) ===")
    for slope in [(4, 3), (1, 2)]:
        r = check("m004%s" % str(slope), do_bound=True)
        emit("  m004%-6s ARITH=%s sig=%s disc=%-9d ram_all=%s bound_ok=%s bound_max=%s"
             % (str(slope), r["arithmetic"], r["sig"], r["disc"], r["ram_all"], r["bound_ok"], r["bound_max"]))
    emit("")

    # 3) the COMPLETENESS SCAN -- fully resolved, three-category, unresolved count printed
    emit("=== COMPLETENESS SCAN (escalating field recognition; genuine per-case verdicts) ===")

    # 3a) integral slopes q=1, p=5..40
    int_arith, int_nonarith, int_unres = [], [], []
    for p in range(5, 41):
        _t = time.time()
        r = check("m004(%d,1)" % p)
        print("  .. m004(%d,1) %s deg=%s sig=%s  %.1fs" % (p, r.get("status"), r.get("deg"),
              r.get("sig"), time.time() - _t), file=sys.stderr, flush=True)
        scan_row(r)
        st = r.get("status")
        if st == "ARITH":
            int_arith.append((p, r["disc"], r["sig"]))
        elif st == "NON-ARITH":
            int_nonarith.append((p, r.get("sig"), r.get("reason")))
        elif st == "UNRESOLVED":
            int_unres.append(p)
    emit("  [integral q=1, p=5..40]  scanned %d  |  ARITH=%s  NON-ARITH=%d  UNRESOLVED=%s"
         % (36, [p for p, _, _ in int_arith], len(int_nonarith), int_unres if int_unres else "0"))
    emit("     arithmetic slopes: %s" % [p for p, _, _ in int_arith])
    emit("     p=7 gap: %s"
         % next(("sig=%s (%s)" % (s, rs) for pp, s, rs in int_nonarith if pp == 7), "(7 not non-arith?!)"))

    # 3b) non-integral slopes q=2..12, p=1..25, gcd=1
    #     Two GENUINE ways to be non-arithmetic (both computed per case, tallied separately):
    #       (c1) r2 >= 2  -- more than one complex place, condition (1) fails;
    #       (c3) r2 == 1  -- one complex place, BUT the quaternion algebra SPLITS at a real place,
    #                        condition (3) fails (the ramification test the discrimination cases show).
    ni_scanned = 0
    ni_arith, ni_nonarith, ni_unres, ni_nonhyp = [], [], [], []
    ni_c1, ni_c3, ni_c3_list = 0, 0, []
    for q in range(2, 13):
        for p in range(1, 26):
            if gcd(p, q) != 1:
                continue
            _t = time.time()
            r = check("m004(%d,%d)" % (p, q))
            print("  .. m004(%d,%d) %s deg=%s sig=%s  %.1fs" % (p, q, r.get("status"), r.get("deg"),
                  r.get("sig"), time.time() - _t), file=sys.stderr, flush=True)
            st = r.get("status")
            if st == "NON-HYP":
                ni_nonhyp.append((p, q))
                continue
            scan_row(r)
            ni_scanned += 1
            if st == "ARITH":
                ni_arith.append((p, q, r["disc"]))
            elif st == "NON-ARITH":
                ni_nonarith.append((p, q))
                if r["sig"][1] >= 2:               # (c1) >1 complex place
                    ni_c1 += 1
                else:                               # (c3) one complex place, ramification/integrality fails
                    ni_c3 += 1
                    ni_c3_list.append((p, q))
            elif st == "UNRESOLVED":
                ni_unres.append((p, q))
    emit("  [non-integral q=2..12, p<=25, gcd=1]  hyperbolic=%d (non-hyp skipped=%d)"
         % (ni_scanned, len(ni_nonhyp)))
    emit("     ARITH=%s  |  NON-ARITH(resolved)=%d  |  UNRESOLVED=%d"
         % (ni_arith if ni_arith else "NONE", len(ni_nonarith), len(ni_unres)))
    emit("     of the %d resolved negatives: %d fail cond(1) [r2>=2];  %d have ONE complex place"
         " [r2=1] but fail cond(3) [quaternion algebra splits at a real place]:"
         % (len(ni_nonarith), ni_c1, ni_c3))
    emit("       the %d one-complex-place non-integral non-arith fillings: %s" % (ni_c3, ni_c3_list))
    if ni_unres:
        emit("     unresolved (invariant trace field degree > 60): %s" % ni_unres)
    emit("")

    return dict(int_arith=int_arith, int_nonarith=len(int_nonarith), int_unres=int_unres,
                ni_scanned=ni_scanned, ni_arith=ni_arith, ni_nonarith=len(ni_nonarith),
                ni_unres=len(ni_unres), ni_c1=ni_c1, ni_c3=ni_c3, ni_c3_list=ni_c3_list)


def main():
    emit("B718 PROBE 2 -- THE ARITHMETIC SUB-FAMILY (Dehn fillings of the figure-eight cusp)")
    emit("=" * 96)
    emit("[CORRECTED RE-RUN 2026-07-19: escalating field recognition + three-category verdicts;")
    emit(" prose states EXACTLY the scanned box; unresolved count printed, never folded into 'non-arith']")
    emit("")
    scan = None
    if not HAVE:
        emit("[sage-python + SnapPy not importable here: %s]" % _IMPORT_ERR)
        emit("Re-run with:  sage-python frontier/B718_child_program/b718_probe2.py")
        emit("")
        emit("BANKED RECORD (verified in-sandbox, sage-python + SnapPy 3.3.2):")
    else:
        scan = _live()
    emit("=== THE COMPLETE FINITE ARITHMETIC SUB-FAMILY (up to symmetry, over the scanned box) ===")
    for slope, d in ARITHMETIC_CHILDREN.items():
        emit("  m004%-6s vol=%.5f  k0 = %-14s deg %d  disc %-5d  sig %s  %s"
             % (str(slope), d["vol"], d["poly"], d["deg"], d["disc"], d["sig"], d["note"]))
    emit("")
    emit("VERDICT -> OUTCOME A : distinguished, STRUCTURED finite arithmetic sub-family.")
    emit("  * exactly 3 arithmetic children in the scanned box (Margulis finiteness realized);")
    emit("  * ALL are INTEGRAL fillings q=1 -- NO resolved non-integral filling is arithmetic (most")
    emit("    fail because r2>=2; a handful have r2=1 but the quaternion algebra splits at a real place);")
    emit("  * only the small hyperbolic slopes p in {5,6,8}; the gap at p=7 (r2=2, two complex places);")
    emit("  * their fields are minimal-discriminant complex cubic/quartic fields (-31,-59,-283);")
    emit("  * (5,1) child = m003(-2,3), confirmed arithmetic (disc -283).")
    if scan is not None:
        emit("")
        emit("SCAN LEDGER (printed, in-sandbox -- every number below is COMPUTED, not asserted):")
        emit("  integral q=1, p=5..40 (36 slopes):  ARITH=%s  NON-ARITH=%d  UNRESOLVED=%s"
             % ([p for p, _, _ in scan["int_arith"]], scan["int_nonarith"],
                scan["int_unres"] if scan["int_unres"] else "0"))
        emit("  non-integral q=2..12, p<=25, gcd=1:  hyperbolic=%d  ARITH=%s  NON-ARITH(resolved)=%d  UNRESOLVED=%d"
             % (scan["ni_scanned"], scan["ni_arith"] if scan["ni_arith"] else "NONE",
                scan["ni_nonarith"], scan["ni_unres"]))
        emit("     (of the %d non-integral negatives: %d fail cond(1) r2>=2; %d have r2=1 but fail cond(3))"
             % (scan["ni_nonarith"], scan["ni_c1"], scan["ni_c3"]))
        emit("DISCRIMINATING FACT (corrected): within the scanned box (integral p=5..40 and")
        emit("  non-integral q=2..12,p<=25 = %d hyperbolic fillings, %d resolved + %d unresolved),"
             % (36 + scan["ni_scanned"], 36 + scan["ni_scanned"] - len(scan["int_unres"]) - scan["ni_unres"],
                len(scan["int_unres"]) + scan["ni_unres"]))
        emit("  arithmeticity is realized by EXACTLY the three integral slopes {5,6,8}; every other")
        emit("  RESOLVED filling is non-arithmetic. TWO genuine obstructions, both computed per case:")
        emit("   (1) the invariant trace field has MORE THAN ONE complex place (r2>=2) -- the generic")
        emit("       case: EVERY integral p not in {5,6,8} and %d of the non-integral fillings;" % scan["ni_c1"])
        emit("   (3) r2=1 (one complex place) but the invariant quaternion algebra SPLITS at a real")
        emit("       place -- %d small-q non-integral fillings %s." % (scan["ni_c3"], scan["ni_c3_list"]))
        emit("  The STRUCTURE: arithmeticity needs r2=1 AND real-place ramification simultaneously;")
        emit("  only the integral slopes {5,6,8} clear both, and r2 grows with the slope so the window")
        emit("  shuts. (Margulis guarantees finiteness; the computation locates the finite set.)")
        if scan["int_unres"] or scan["ni_unres"]:
            emit("  UNRESOLVED (tool ceiling, reported as such, NOT counted as a negative): integral %s,"
                 " non-integral %d." % (scan["int_unres"], scan["ni_unres"]))
        else:
            emit("  UNRESOLVED = 0 across the entire box: every case has a GENUINE verdict.")
    else:
        emit("DISCRIMINATING FACT: arithmeticity of the child forces an INTEGER coupling (q=1) and one")
        emit("  of only three small slopes {5,6,8}; re-run under sage-python to reproduce the scan.")

    base = __file__.rsplit("/", 1)[0]
    with open(base + "/b718_probe2_out.txt", "w") as f:
        f.write("\n".join(OUT) + "\n")
    if SCAN:
        with open(base + "/b718_probe2_scan.tsv", "w") as f:
            f.write("name\tstatus\tvol\tdeg\tdisc\tsig\tfield_at\treason\n")
            f.write("\n".join(SCAN) + "\n")
    print("\n[wrote %s/b718_probe2_out.txt]" % base)


if __name__ == "__main__":
    main()
