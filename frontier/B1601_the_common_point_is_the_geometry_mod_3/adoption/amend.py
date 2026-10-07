#!/usr/bin/env python3
"""B1601 -- GENESIS v1.24 (main's, B1600) -> v1.25 (main's): W5 and W7 recorded at FK14 -- the four at the common point is
the trivial line plus the triplet (W5), and the common point is every odd-trace thread's geometry modulo a prime of norm
three, W3's forced cover the thread's own congruence cover at it (W7, sealed); the version log.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.25 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_24_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_24 = "58b5db5fba9d5d39b3ad9dc72e7f65ec7b5ba27f0b3fb37412966f3622fa90e3"

CHANGES = [
 ("**Version 1.24 · 2026-10-07 · canonical.**", "**Version 1.25 · 2026-10-07 · canonical.**"),
 ("W1–W4 hold either way, the weave's group on the triplet of order 24 with L and R, 48 with all four. ",
  "W1–W4 hold either way, the weave's group on the triplet of order 24 with L and R, 48 with all four. "
  "**[v1.25] W5 (main, B1601):** at the common point the frames' own module, the four (ν ⊗ ρ ⊗ ρ̄), is the trivial line plus the three parity lines — Ad(i) and Ad(j) act on (1, i, j, k) by the signs (1, +, −, −) and (1, −, +, −) — so \"the generation is the trivial line\" (B1493) and \"the three parity lines\" (W4) are the two parts of one module (the seat's \"matches the quaternion axes\", stated on the four). "
  "**[v1.25] W7, THE COMMON POINT IS THE GEOMETRY MOD 3 (main, B1601, sealed; a weave result):** on every odd-trace thread to length eight (sixteen, none chosen) the fibre's traces (tr a, tr b, tr ab) at the geometric point generate exactly one prime of the thread's trace field, of norm three, so the holonomy reduces there to the quaternion point: W2's common structure is each thread's own geometry seen modulo a prime of norm three, and W3's forced A₄ cover is the thread's congruence cover at that prime (SL(2, 𝔽₃) = 2T). On every even-trace thread to length eight (twenty-one) the ideal is a power of a prime above 2, where the common point is the trivial representation; nothing above 3. The lemma: the Fricke map's linear part at the common point is the signed parity permutation of the three lines — dL and dR quarter turns about two axes, the cube's rotation group S₄ — a third turn about a body diagonal exactly for odd trace, whose axis (±1, ±1, ±1) is isotropic for x² + y² + z² only in characteristic three; over 𝔽₃ the parabolic Markov surface has the common point as its only point. The meeting is universal on odd trace, so it is not what singles out ±LR for content (the SM seat's W6 census): the ±LR pattern stays arithmeticity's, unexplained. "),
 ("- **v1.24 · 2026-10-07 · main B1600.** The weave.\n",
  "- **v1.25 · 2026-10-07 · main B1601.** The common point is the geometry mod 3.\n"
  "  - FK14: W5 — the four at the common point is the trivial line plus the triplet; W7 — on every odd-trace thread to length eight the holonomy reduces to the common point at exactly one prime of norm three (on none of even trace), so the forced A₄ cover is the thread's own congruence cover at it; the lemma (the isotropic axis in characteristic three) proved, the exact norm a census law, the theorem open.\n"
  "- **v1.24 · 2026-10-07 · main B1600.** The weave.\n"),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_24, "the received v1.24 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.25 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.25, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
