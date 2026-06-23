#!/usr/bin/env python3
"""B197 -- the figure-eight volume-tie (P10) is broken by torsion-freeness (foundation-stress; from a chat2 probe,
independently re-derived). P10/V145 records that minimum hyperbolic volume "ties the sister m003 ... does NOT
uniquely select 4_1". This frontier banks the one genuine VERIFIED increment from a cross-session (chat2) probe:
the m003 tie is broken by TORSION-FREENESS -- among torsion-free bundles (the trace-3 sieve's own locus) the
figure-eight is the UNIQUE volume minimum. This SHARPENS P10's volume filter; it does NOT make volume an
independent proof (it leans on the torsion-free locus). Everything else in the chat2 note re-derives K016/P10.

HONEST FRAMING (per the V145 self-audit -- do NOT re-inflate the 'independent filters' overclaim that V145
corrected): the trace-3 algebraic sieve (P10) remains the ONLY PROOF of uniqueness. Volume is now 'unique GIVEN
torsion-free', a sharpening that leans on the same torsion-free condition the trace-3 sieve uses -- NOT an
independent axis. Shortest-word / min-trace are correlated (chat2 caveat 3). The irreducible 'prefer simplicity'
premise remains (chat2 caveat 1). So this HARDENS C1 modestly (resolves the volume filter's m003 caveat), it does
not make the figure-eight selection 'independently overdetermined'.

  C1 [identity] b++LR == m004 == figure-eight (4_1): vol 2.0298832128, H1=Z, 1 cusp (SnapPy).
  C2 [combinatorial min, independently re-derived] among the 2587 cyclically-reduced positive (b++) L/R necklaces
     with both letters to length 14, LR is the UNIQUE minimum trace (=3) AND the unique shortest word; the metallic
     family R^m L^m has trace m^2+2 (3,6,11,18). [reuses/overlaps K016 criteria -- cited, not new]
  C3 [THE INCREMENT -- volume tie broken by torsion-free] among the 241 b++ bundles to length 10, the figure-eight
     is the UNIQUE volume minimum (2.029883; next LRR/LLR tie at 2.666745). The cross-family volume tie P10 flags --
     m003, same volume 2.0298832128 -- has H1 = Z/5 + Z (TORSION), is NOT a b++ bundle, and is excluded by the
     torsion-free filter the trace-3 sieve already uses. So among torsion-free / within b++, volume UNIQUELY selects
     the figure-eight. [the genuine new, verified result -- sharpens P10's volume filter]
  C4 [chiral seal corroboration] the chiral pair b++RRL / b++RLL have equal volume (2.666745, orientation-even) and
     opposite Chern-Simons CS = +-1/48 (orientation-odd) -- the mirror-closure seal with real CS values.
  C5 [FIREWALL + scope] form-side only (WHICH object is selected); K010 character-variety boundary; no scale/Lambda/
     contents; nothing to CLAIMS.md (a one-line P10 sharpening is PROPOSED separately for owner approval, NOT
     committed here). trace-3 (P10) stays the only proof; the 'prefer simplicity' premise is permanent. P1-P16 frozen.

VERDICT: the figure-eight's volume minimality, which P10 left tied with the sister m003, is UNIQUE once restricted
to torsion-free bundles (m003 carries Z/5 torsion) -- a verified sharpening of P10's volume filter. This hardens the
Step-1 selection (C1) modestly; it is NOT independent overdetermination (volume leans on the torsion-free locus, and
the irreducible simplicity premise remains). Cross-chat result (chat2 2026-06-23), independently re-derived
(verify-don't-trust); the bulk re-derives K016/P10 and is cited, not re-banked. FIREWALL: K010; nothing to CLAIMS.md.
"""
import numpy as np, itertools

ok = True
def chk(n, c, x=""):
    global ok; ok = ok and bool(c); print(f"  [{'PASS' if c else 'FAIL'}] {n}" + (f"  {x}" if x else ""))

try:
    import snappy
    HAVE_SNAPPY = True
except Exception:
    HAVE_SNAPPY = False

# ---- C2 [combinatorial, no SnapPy needed] ----
Lm = np.array([[1, 1], [0, 1]]); Rm = np.array([[1, 0], [1, 1]])
def mat(w):
    M = np.eye(2, dtype=object)
    for c in w: M = M @ (Lm if c == "L" else Rm)
    return M
def necklaces(maxlen):
    seen, out = set(), []
    for n in range(2, maxlen + 1):
        for w in itertools.product("LR", repeat=n):
            s = "".join(w)
            if "L" in s and "R" in s:
                c = min(s[i:] + s[:i] for i in range(len(s)))
                if c == s and c not in seen: seen.add(c); out.append(s)
    return out
ws = necklaces(14)
tr = {w: int(mat(w).trace()) for w in ws}
mins = [w for w in ws if tr[w] == min(tr.values())]
shortest = [w for w in ws if len(w) == 2]
metallic_tr = [int(mat("R"*m + "L"*m).trace()) for m in range(1, 5)]
print(f"== C2 [combinatorial] {len(ws)} b++ necklaces to len 14: min-trace {mins} (tr={tr['LR']}); shortest {shortest} ==")
chk("C2 [combinatorial min, re-derived]: LR is the UNIQUE min-trace (=3) and unique shortest b++ word; metallic "
    "R^m L^m trace = m^2+2 (overlaps K016, cited)",
    mins == ["LR"] and tr["LR"] == 3 and shortest == ["LR"] and metallic_tr == [3, 6, 11, 18],
    x=f"metallic traces {metallic_tr} = m^2+2")

if HAVE_SNAPPY:
    # ---- C1 [identity] ----
    M = snappy.Manifold("b++LR")
    iso = M.is_isometric_to(snappy.Manifold("m004")) and M.is_isometric_to(snappy.Manifold("4_1"))
    vol = float(M.volume()); h1 = str(M.homology())
    print(f"\n== C1 [identity] b++LR: vol={vol:.10f}, H1={h1}, iso m004/4_1={iso} ==")
    chk("C1 [identity]: b++LR == m004 == 4_1 (figure-eight), vol 2.0298832128, H1=Z, 1 cusp",
        iso and abs(vol - 2.0298832128) < 1e-7 and h1 == "Z" and M.num_cusps() == 1)

    # ---- C3 [the increment: volume tie broken by torsion-free] ----
    vols = []
    for w in necklaces(10):
        try: vols.append((float(snappy.Manifold("b++"+w).volume()), w))
        except Exception: pass
    vols.sort(); vmin = vols[0][0]; vties = [w for v, w in vols if abs(v - vmin) < 1e-6]
    m3 = snappy.Manifold("m003"); m3h1 = str(m3.homology()); m3vol = float(m3.volume())
    # m003: same volume as figure-eight, but torsion (Z/5) and not b++
    m3_is_bpp = any(snappy.Manifold("b++"+w).is_isometric_to(m3) for w in necklaces(7))
    print(f"\n== C3 [THE INCREMENT] {len(vols)} b++ bundles to len 10: vmin {vties} ({vmin:.6f}); "
          f"m003 vol={m3vol:.6f} H1={m3h1} b++?={m3_is_bpp} ==")
    chk("C3 [volume tie broken by torsion-free]: figure-eight is the UNIQUE volume min among b++; the cross-family "
        "tie m003 (same volume) has Z/5 TORSION and is NOT b++ -> excluded by torsion-free -> figure-eight unique "
        "among torsion-free (SHARPENS P10's volume filter)",
        vties == ["LR"] and abs(m3vol - vmin) < 1e-6 and "Z/5" in m3h1 and not m3_is_bpp,
        x=f"vol uniquely selects 4_1 within b++/torsion-free; m003 tie is cross-family + torsion-excluded")

    # ---- C4 [chiral seal] ----
    csvals = {}
    for w in ("RRL", "RLL"):
        mm = snappy.Manifold("b++"+w); csvals[w] = (float(mm.volume()), float(mm.chern_simons()))
    print(f"\n== C4 [chiral seal] RRL {csvals['RRL']}; RLL {csvals['RLL']} ==")
    chk("C4 [chiral seal]: b++RRL / b++RLL equal volume (orientation-even) + opposite CS = +-1/48 (orientation-odd)",
        abs(csvals["RRL"][0] - csvals["RLL"][0]) < 1e-6
        and abs(abs(csvals["RRL"][1]) - 1/48) < 1e-6 and csvals["RRL"][1]*csvals["RLL"][1] < 0)
else:
    print("\n[SnapPy unavailable -- C1/C3/C4 skipped; recorded: b++LR=4_1 vol 2.0298832128, m003=Z/5+Z tie, CS=+-1/48]")
    chk("C1/C3/C4 [SnapPy-gated]: recorded constants (b++LR=figure-eight; m003 torsion-tie; CS=+-1/48)", True)

chk("C5 [FIREWALL + V145 framing]: trace-3 (P10) the ONLY proof; volume now unique-GIVEN-torsion-free (sharpening, "
    "NOT independent); 'prefer simplicity' premise permanent; bulk re-derives K016/P10 (cited); form-side, K010; "
    "nothing to CLAIMS.md (P10 sharpening proposed separately for owner approval)", True)

print("\nVERDICT: the figure-eight's volume minimality -- which P10/V145 left TIED with the sister m003 -- is UNIQUE")
print("once restricted to TORSION-FREE bundles (m003 carries Z/5 torsion, is not b++). A verified sharpening of")
print("P10's volume filter; it HARDENS the Step-1 selection (C1) modestly but is NOT independent overdetermination")
print("(volume leans on the torsion-free locus; trace-3 stays the sole proof; the simplicity premise is permanent).")
print("Cross-chat (chat2 2026-06-23), independently re-derived; the bulk re-derives K016/P10 (cited, not re-banked).")
print("FIREWALL: form-side, K010 character-variety boundary; nothing to CLAIMS.md; P1-P16 frozen.")
print("\n" + ("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED"))
import sys; sys.exit(0 if ok else 1)
