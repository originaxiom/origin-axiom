#!/usr/bin/env python3
"""B1655 -- GENESIS v1.45 (main's, B1651) -> v1.46 (main's): main's audit of its own negatives since B1600 (the owner's
ruling on POINT_REGISTER P-152, 2026-10-15). FK14's B1602 carrier withdrawn in part (B1604, B1605) and its even-trace
counts over candidate kernels; FK11's six kinds and the scope of B1604's theorem; FK9's 'free' as frozen pieces, with
B1646's 'never between' a quartic statement; FK15's 'not forced' for a point or density Higgs; GM5c's near-omega clause,
which has no cell; W50's recomputation on main noted; the log.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.46 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_45_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_45 = "8aa87afff1a3a0cc5e32725048042c69006f70ccc7425339a6fa1b0604a7b56f"

FK14 = (" **[v1.46] Withdrawn in part (main's audit of its negatives, P-152, B1655; B1604 §2b, B1605 R2).** The "
        "−LLRLRLRR member above was instrument noise: its cover's relators run to 720–902 letters and the four's residual "
        "at 40 digits is 6 × 10² (B1604's Euler control). Re-read at 70 digits on certified covers, no odd-trace thread "
        "among the 19 read carries a member (B1605): on odd trace the root's pair ±LR is alone to length eight at order "
        "two, so the ±LR exclusivity holds rather than fails. On even trace the forced kernel is one of two (D₄) or four "
        "(V₄) candidates and is not identified (B1602's preregistration): 16 of 42 even threads carry on some candidate "
        "kernel and 26 on none.")
FK11 = (" **[v1.46] (B1655)** Six kinds on certified covers, not eight (B1603's correction; B1605). B1604's theorem is that "
        "no twisted Euler characteristic, and not B1492's class index, carries n_5̄ = n_10 on a thread or a cover; "
        "\"governed by no characteristic class\" means that no formula I(Λ²E) = f(I(E)) fits the reliable data. "
        "Indices of other kinds (η-invariants, L²) are not addressed by it.")
FK9 = (" **[v1.46] Scoped (main's audit of its negatives, P-152, B1655).** Each \"free\" above is a frozen piece's — one "
       "fibre, one τ, the field held fixed — and bounds that piece, not the interacting weave of threads and field (the "
       "owner, 2026-10-15). B1646's \"never between\" holds for a quartic potential: one octic invariant, or the zero "
       "modes' own one-loop term, puts minima between the isotropic cone and the real locus (the audit's check, "
       "reproduced on main). The Higgs directions tested as vacua were real (B1644's 400 directions, B1646's units); "
       "the isotropic directions were not tested as vacua, and the near-ω regime is uncomputed (GM5c's [v1.46] note). "
       "B990's law concerns the orbit of one point.")
FK15 = (" **[v1.46] Scoped (B1655).** Not forced for a point or density Higgs (B1651's premise P1, tested by no cell). A "
        "smooth Higgs of (0, 1) type that carries a parity couples at the puncture, forced at the price of one framed "
        "datum per parity (B1651's addendum of 2026-10-14, the Szegő reading); B1654 adopts that typing.")
GM5C = (" **[v1.46] Audited (main's audit of its negatives, P-152, B1655).** B1617's \"near ω the degeneracy splits by "
        "powers of ε … quasi-degenerate\" and v1.35's \"no hierarchy at ω or near it\" have no cell: no spectrum near ω "
        "was computed. The clause is an inference from the near-fixed-point mechanism, whose own input, distinct "
        "residual charges, B1617's Z4 found. On the ruled branch the residual at ω is cyclic of order 12 (B1634). τ = ω "
        "stays retired only as \"no hierarchy found at ω\" (B1640); the near-ω regime is open.")
CHANGES = [
 ("**Version 1.45 · 2026-10-14 · canonical.**", "**Version 1.46 · 2026-10-15 · canonical.**"),
 ("its sign twin and the other 28 odd-trace threads carry nothing.",
  "its sign twin and the other 28 odd-trace threads carry nothing." + FK14),
 ("(B1603: eight kinds of reading on 442 classes).", "(B1603: eight kinds of reading on 442 classes)." + FK11),
 ("main tests it first at the joint potential (P-132), sealed first.",
  "main tests it first at the joint potential (P-132), sealed first." + FK9),
 ("The \"which\" half, banked: where a Higgs can couple the fibre's zero modes is not forced.",
  "The \"which\" half, banked: where a Higgs can couple the fibre's zero modes is not forced." + FK15),
 ("B1618's 'degenerate for every weight' used the inner automorphisms, which are not moves here.",
  "B1618's 'degenerate for every weight' used the inner automorphisms, which are not moves here." + GM5C),
 ("(registered, not yet recomputed on main)", "(registered; recomputed on main by B1635 and scoped by B1640, below)"),
 ("- **v1.45 · 2026-10-14 · main B1651.**",
  "- **v1.46 · 2026-10-15 · main B1655.** Main's audit of its own negatives since B1600 (the owner's ruling on P-152): "
  "FK14's B1602 carrier withdrawn in part (B1604, B1605) and the even-trace counts read over candidate kernels; FK11's "
  "six kinds and the scope of B1604's theorem; FK9's \"free\" as frozen pieces, B1646's \"never between\" quartic only; "
  "FK15's \"not forced\" for a point or density Higgs; GM5c's near-ω clause, which has no cell; W50's recomputation on "
  "main noted. The v1.26 entry below records WM3 as first banked.\n"
  "- **v1.45 · 2026-10-14 · main B1651.**"),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_45, "the received v1.45 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.46 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.46, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
