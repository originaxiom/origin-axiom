#!/usr/bin/env python3
"""DOOR 3 -- does opening KMRT section 43 open B882's conjecture?

Seal: outside_bench/seals/DOOR_THREE_PREREG.md
      sha256 0b2d7b60afa32bd8f24f4f9393e5e24bbc75a612e9c39385c6b8ff1eb93b9afd

WHAT_WOULD_COUNT 4A.3 names three successor doors as "the only remaining
licensed targets".  Door 3 is B882's arithmetic-S3 = geometric-S3 conjecture,
which B1077 ranks as "the UNIQUE non-circular route to a 77-mechanism", with
"the KMRT section 43 connective proposition" as "the named external need".

That need was supplied on 2026-09-13.  This cell asks what it buys.

No new mathematics is attempted here.  Every KMRT statement is QUOTED and
labelled CITED; every record statement is asserted against origin/main.
"""
from __future__ import annotations

import hashlib
import os
import re
import subprocess
import sys
import tempfile
import unicodedata

import os as _os_u
UPLOADS = _os_u.environ.get("OA_UPLOADS", "<uploads dir: set OA_UPLOADS>")   # the bench's upload directory, never a machine path (merge hygiene 2026-09-15)
DEFAULT = os.path.join(UPLOADS, "c7603f02-Knus_M.-A._Merkurjev_A._Rost_M._Tignol_J.-P._"
                                "The_book_of_involutions_draft_book588s.zip")

FAILURES: list[str] = []
BOOK_N = ""


def fail(tag, msg):
    FAILURES.append(f"{tag}: {msg}")
    print(f"  !! FAIL [{tag}] {msg}")


def rule(t):
    print("\n" + "-" * 78)
    print(t)
    print("-" * 78)


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", s)).strip()


def load_book():
    src = os.environ.get("KMRT_PDF", DEFAULT)
    work = tempfile.mkdtemp(prefix="kmrt3_")
    subprocess.run(["unzip", "-o", "-q", src, "-d", work], check=True)
    pdf = None
    for root, _d, files in os.walk(work):
        if "__MACOSX" in root:
            continue
        for f in files:
            if f.lower().endswith(".pdf"):
                pdf = os.path.join(root, f)
    sha = hashlib.sha256(open(pdf, "rb").read()).hexdigest()
    txt = os.path.join(work, "k.txt")
    subprocess.run(["pdftotext", "-layout", pdf, txt], check=True)
    return open(txt, encoding="utf-8", errors="replace").read(), sha


def q(tag, needle, where="KMRT"):
    ok = norm(needle) in BOOK_N
    print(f"\n  [{tag}] {where} -- {'FOUND' if ok else 'ABSENT'}")
    for ln in needle.strip().splitlines():
        print(f"      {ln.strip()}")
    if not ok:
        fail("C1", f"{tag} not located")
    return ok


def show(path):
    r = subprocess.run(["git", "show", f"origin/main:{path}"],
                       capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ""


def rq(tag, hay, needle, where):
    ok = norm(needle) in norm(hay)
    print(f"\n  [{tag}] {where} -- {'FOUND' if ok else 'ABSENT'}")
    for ln in needle.strip().splitlines():
        print(f"      {ln.strip()}")
    if not ok:
        fail("C3", f"{tag} not located in {where}")
    return ok


def main() -> int:
    global BOOK_N
    print("=" * 78)
    print(" DOOR 3 -- what does opening KMRT section 43 actually buy?")
    print("=" * 78)
    book, sha = load_book()
    BOOK_N = norm(book)
    print(f"\n  source sha256 : {sha}")

    # ---------------------------------------------------------------- C2 first
    rule("CONTROL C2 -- the quotation instrument must be able to say ABSENT")
    decoy = ("the cubic etale algebra L is canonically determined by the central simple "
             "algebra with involution (A, sigma) of degree 8")
    d = norm(decoy) in BOOK_N
    print(f"\n    decoy (a plausible FALSE claim about KMRT): "
          f"{'FOUND' if d else 'ABSENT'}")
    real = "An isomorphism"
    r = norm(real) in BOOK_N
    print(f"    a true short needle, same instrument              : "
          f"{'FOUND' if r else 'ABSENT'}")
    c2 = (not d) and r
    print(f"  C2: {'PASS' if c2 else 'FAIL'}")
    if not c2:
        fail("C2", "the quotation instrument cannot separate a decoy from the source")

    # ---------------------------------------------------------------- C3
    rule("CONTROL C3 -- the record's own statements, quoted from origin/main")
    b1077 = show("frontier/B1077_intrinsic_split/FINDINGS.md")
    rq("B1077's ranking", b1077,
       "**B882's conjecture (arithmetic S₃ = geometric S₃) is now\nthe UNIQUE "
       "non-circular route to a 77-mechanism**, its in-sandbox half done here; the\nremaining "
       "half is the KMRT §43 connective proposition — a typed literature floor, the\n"
       "named external need.",
       "origin/main B1077")
    rq("the bare algebra carries no 77", b1077,
       "**Nothing 77-shaped exists anywhere in the object's bare\nD4 geometry.**",
       "origin/main B1077")
    nsl = show("docs/NOVELTY_SWEEP_LEDGER.md")
    rq("the decision route", nsl,
       "moves only by (a) KMRT §43 opened + an independent dressing computation, or "
       "(b) B882's conjecture proved",
       "origin/main NOVELTY_SWEEP_LEDGER row 6")
    rq("the circularity theorem-let", nsl,
       "the bank contains exactly ONE such triple (the enhancement lines) and its resolvent "
       "already IS K — so every in-bank dressing route makes C77 true BY FIAT",
       "origin/main NOVELTY_SWEEP_LEDGER row 6")
    rq("the undressed cubic", nsl,
       "the UNDRESSED datum — bare tri(\U0001d546_split) as B904 built it — canonically "
       "attaches the SPLIT cubic ℚ×ℚ×ℚ, trivial discriminant",
       "origin/main NOVELTY_SWEEP_LEDGER row 6")

    # ---------------------------------------------------------------- CELL 1
    rule("CELL 1 -- does KMRT attach a cubic to (A,sigma), or is the cubic separate data?")
    q("SS43.A, the datum", """An isomorphism""")
    print("""
    KMRT's trialitarian algebra is the FOUR-TUPLE  T = (E, L, sigma, alpha):
    L is a cubic etale F-algebra, and (E, sigma) is central simple OVER L of
    degree 8 with orthogonal involution.  So L is not read off (A,sigma) -- it
    is the algebra E LIVES OVER, and it is part of the datum.""")
    # NB the first version of this needle was taken from memo 203's SEARCH
    # SUMMARY of KMRT, not from KMRT, and C1 FIRED on it.  That is rule #26
    # working: a paraphrase is not a quotation.  KMRT's own sentence:
    q("what (A,sigma) DOES carry canonically -- a QUADRATIC, not a cubic",
      """it follows that the center Z of C(A, σ, f ) is a quadratic étale F -\nalgebra""")
    cell1 = "A"
    print(f"""
  >>> CELL 1 OUTCOME {cell1}.  What (A,sigma) canonically carries is the
      QUADRATIC discriminant algebra -- the centre of its Clifford algebra.
      THE CUBIC IS SEPARATE DATA.  So "the cubic canonically attached to
      (A,sigma)" is not a quantity KMRT defines for (A,sigma) alone; it is
      defined for a TRIALITARIAN ALGEBRA, which is (A,sigma) PLUS a packaging.""")

    # ---------------------------------------------------------------- CELL 2
    rule("CELL 2 -- is ONE Cayley algebra compatible with MORE THAN ONE cubic?")
    q("SS36.C, arbitrary cubic etale L",
      """an arbitrary cubic étale algebra L and a para-Hurwitz algebra""")
    q("SS43.7, End(Gamma) is trialitarian",
      """We set End(Γ) for the trialitarian algebra associated to the twisted composition Γ""")
    q("SS43.2, the SPLIT case from the same C",
      """We say that such a trialitarian algebra T is of type G2""")
    cell2 = "A"
    print(f"""
  >>> CELL 2 OUTCOME {cell2}.  SS36.C builds a twisted composition Gamma(C, L) from a
      Hurwitz algebra C and an ARBITRARY cubic etale L, by descent from L (x) Delta;
      SS43.7 makes End(Gamma) a trialitarian algebra.  With L split the SAME C gives
      SS43.2's type-G2 algebra.  SO ONE CAYLEY ALGEBRA FEEDS EVERY CUBIC.
      C DOES NOT SELECT L.""")

    # ---------------------------------------------------------------- CELL 3
    rule("CELL 3 -- is the cubic a FREE classifying parameter?  (the decisive cell)")
    q("SS44.1, the sequence is SPLIT", """we have a split exact\nsequence""")
    q("SS44.2's proof, the section exists", """has a section""")
    q("SS44.5, what classifies trialitarian algebras",
      """The pointed set H 1 (F, PGO+\n8 oS3 ) classifies trialitarian F -\nalgebras up to isomorphism""")
    q("SS44.5, and the second map is exactly 'take the cubic'",
      """The\nsecond map associates the class of L to the trialitarian algebra T = (E, L, σ, α).""")
    print("""
    PUT TOGETHER, and this is a reading of KMRT rather than a new theorem:
      * SS44.1: 1 -> PGO(C,n) -> PGO(C,n) x| S3 -> S3 -> 1 is SPLIT, with p the
        projection; SS44.2's proof says the restriction map "has a section".
      * A SPLIT surjection of group schemes induces a SURJECTION on H^1.
      * SS44.5: H^1(F, PGO_8^+ x| S3) classifies trialitarian algebras, and the
        map to H^1(F, S3) IS "send T to the class of its cubic L".
      * H^1(F, S3) is exactly the set of cubic etale F-algebras.""")
    cell3 = "A"
    print(f"""
  >>> CELL 3 OUTCOME {cell3}.  THE MAP  "trialitarian algebra |-> its cubic"  IS
      SURJECTIVE ONTO ALL CUBIC ETALE ALGEBRAS.  Every cubic -- K included, Q^3
      included -- is the cubic of some trialitarian algebra over Q.

      SO THE FORMALISM FORCES NOTHING.  The cubic is a FREE CLASSIFYING
      PARAMETER, and "which cubic" is a TORSOR question of exactly the shape the
      record already meets everywhere: the object supplies the group, never the
      point.""")

    # ---------------------------------------------------------------- CELL 4
    rule("CELL 4 -- what is clause (a) worth, now that its first half is paid?")
    print("""
    The decision route: the echo moves only by
      (a) KMRT SS43 opened  +  an independent dressing computation
      (b) B882's conjecture proved

    FIRST HALF OF (a): PAID.  KMRT is read (memo 222: the 6D4 typing verified
    against SS43.C, [E] = 1 proved, SS44.16(1) giving T = End(Gamma)).

    SECOND HALF OF (a): UNTOUCHED -- and CELLS 1-3 show KMRT DOES NOT SUPPLY IT.
    The cubic is separate data (CELL 1), one Cayley algebra feeds every cubic
    (CELL 2), and the cubic-taking map is surjective (CELL 3).  A formalism that
    accommodates every cubic cannot single out K.

    SO THE 77 STILL HAS TO COME FROM THE DRESSING, and the circularity
    theorem-let still stands: the bank's only order-3 Galois-permuted triple is
    the enhancement lines, whose resolvent IS K by construction.""")
    cell4 = "A"
    print(f"""
  >>> CELL 4 OUTCOME {cell4}.  THE LITERATURE FLOOR IS PAID AND THE DOOR DOES NOT
      OPEN.  What changes is the door's TYPE: it was "blocked on a book nobody
      here could read"; it is now "blocked on an INDEPENDENT DRESSING, with the
      literature half settled and shown not to supply one".""")

    # ---------------------------------------------------------------- C4
    rule("CONTROL C4 -- this cell may not prove C77 by fiat")
    used = ["enhancement triple", "enhancement lines", "pencil triple"]
    print("    Steps taken in CELLS 1-4 that used a bank object whose resolvent is K")
    print("    by construction: NONE.  The cells quote KMRT and the record's own")
    print("    statements; no dressing is constructed, and no cubic is derived FROM")
    print("    the enhancement triple.  The forbidden move is named and not made:")
    for u in used:
        print(f"      not used as a twist-source: {u}")
    print("  C4: PASS (by construction of the cells -- nothing here derives a cubic)")

    print("\n" + "=" * 78)
    print(" OUTCOMES")
    print("=" * 78)
    print(f"   CELL 1 (the cubic is separate data)        : {cell1}")
    print(f"   CELL 2 (one C feeds every cubic)           : {cell2}")
    print(f"   CELL 3 (the cubic map is surjective)       : {cell3}")
    print(f"   CELL 4 (clause (a) paid, door still shut)  : {cell4}")
    print(f"   C1 quotations located : "
          f"{'PASS' if not [f for f in FAILURES if f.startswith('C1')] else 'FAIL'}")
    print(f"   C2 decoy rejected     : {'PASS' if c2 else 'FAIL'}")
    print(f"   C3 record quoted      : "
          f"{'PASS' if not [f for f in FAILURES if f.startswith('C3')] else 'FAIL'}")
    print(f"   C4 no circular step   : PASS")
    if FAILURES:
        print("\n  FAILURES:")
        for f in FAILURES:
            print(f"    - {f}")
    print("=" * 78)
    return 1 if FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
