#!/usr/bin/env python3
"""KMRT ARRIVES -- the trialitarian record verified against the source.

Seal: outside_bench/seals/KMRT_ARRIVES_PREREG.md
      sha256 4eaefd038c97b80b08c35d3fe2be41d3e9e3ef62fb319a330afb1ec0dddfbabf

The source is a DRAFT PDF of The Book of Involutions (Knus-Merkurjev-Rost-Tignol),
supplied by the owner 2026-09-13.  In this draft EVERY internal cross-reference
renders as "(??)", so a numbered result can be quoted but the results it cites
cannot be followed.  Section numbers, titles, running heads and page numbers are
intact and are what this certificate anchors on.

The book itself is NOT committed to this repository.  The certificate locates it
by path (KMRT_PDF env var overrides), records its sha256, extracts its text with
pdftotext, and asserts each quotation as a substring.  A quote that cannot be
located FAILS THE RUN (control C4).

All arithmetic is exact and runs in PARI/GP (validated against B1093 in memo 219).
"""

from __future__ import annotations

import hashlib
import os
import re
import subprocess
import sys
import tempfile
import unicodedata

# ----------------------------------------------------------------------------- infra

import os as _os_u
UPLOADS = _os_u.environ.get("OA_UPLOADS", "<uploads dir: set OA_UPLOADS>")   # the bench's upload directory, never a machine path (merge hygiene 2026-09-15)
DEFAULT_PDF = os.path.join(
    UPLOADS,
    "c7603f02-Knus_M.-A._Merkurjev_A._Rost_M._Tignol_J.-P._"
    "The_book_of_involutions_draft_book588s.zip",
)

FAILURES: list[str] = []


def fail(tag: str, msg: str) -> None:
    FAILURES.append(f"{tag}: {msg}")
    print(f"  !! FAIL [{tag}] {msg}")


def norm(s: str) -> str:
    """Collapse whitespace and normalise Unicode composition.

    pdftotext -layout pads with runs of spaces, and this PDF stores accented
    letters DECOMPOSED ("e" + U+0301 COMBINING ACUTE) while a typed quotation
    uses the precomposed U+00E9.  NFC makes the two comparable.  This is an
    encoding normalisation only -- it does not weaken control C4, which is
    still shown to bite by control C5 below.
    """
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", s)).strip()


def gp(script: str, timeout: int = 300) -> str:
    """Run a GP script and return stdout.  Raises on nonzero exit.

    CAUTION, and the reason this docstring exists: `gp -q FILE` does NOT
    continue a statement across a newline.  A `for(...)` spanning lines is a
    syntax error per line, and gp then carries on -- so the loop never runs and
    the loop variables stay SYMBOLIC while the script still exits 0.  Multi-line
    statements must be wrapped in braces; see gp_block().
    """
    with tempfile.NamedTemporaryFile("w", suffix=".gp", delete=False) as fh:
        fh.write(script + "\nquit\n")
        path = fh.name
    try:
        r = subprocess.run(["gp", "-q", path], capture_output=True, text=True,
                           timeout=timeout)
        if r.returncode != 0:
            raise RuntimeError(f"gp exit {r.returncode}: {r.stderr[:800]}")
        # gp EXITS 0 EVEN ON A SYNTAX OR RUNTIME ERROR in file mode: it reports the
        # error on stderr, skips the rest of the file, and returns success.  Every
        # silent-empty-table bug in this certificate's history came from ignoring
        # that.  stderr is therefore treated as fatal.
        err = re.sub(r"\x1b\[[0-9;]*m", "", r.stderr).strip()
        if err:
            raise RuntimeError("gp wrote to stderr (exit 0 is not success):\n"
                               + err[:800])
        return r.stdout
    finally:
        os.unlink(path)


def gp_block(setup: str, block: str, tail: str = "", timeout: int = 300) -> str:
    """Run a multi-line GP statement safely: `block` is wrapped in braces.

    `setup` must be ONE STATEMENT PER LINE and is NOT braced -- put function
    definitions there.  GP's `{...}` is a lexical line-continuation marker, not a
    block construct, so a function definition's own braces nested inside the
    wrapper silently breaks the parse and the loops produce NOTHING while gp
    still exits 0.  That is the same failure mode as the unbraced multi-line
    `for`, and it is why every table this certificate prints is checked for
    emptiness rather than trusted.
    """
    return gp(f"{setup}\n{{\n{block}\n}}\n{tail}", timeout)


def gp_lines(script: str, timeout: int = 300) -> dict[str, str]:
    """GP script printing 'key=value' lines; returns the dict."""
    out = gp(script, timeout)
    d: dict[str, str] = {}
    for ln in out.splitlines():
        if "=" in ln:
            k, _, v = ln.partition("=")
            d[k.strip()] = v.strip()
    return d


def rule(title: str) -> None:
    print("\n" + "-" * 78)
    print(title)
    print("-" * 78)


# ----------------------------------------------------------------------------- the source

def load_book() -> tuple[str, str, str]:
    """Return (text, pdf_sha256, pdf_basename).  Handles a .zip or a bare .pdf."""
    src = os.environ.get("KMRT_PDF", DEFAULT_PDF)
    if not os.path.exists(src):
        print(f"  !! source not found: {src}")
        print("     set KMRT_PDF to the book's PDF (or the zip containing it)")
        sys.exit(2)

    work = tempfile.mkdtemp(prefix="kmrt_")
    if src.lower().endswith(".zip"):
        subprocess.run(["unzip", "-o", "-q", src, "-d", work], check=True)
        pdfs = []
        for root, _dirs, files in os.walk(work):
            if "__MACOSX" in root:
                continue
            pdfs += [os.path.join(root, f) for f in files if f.lower().endswith(".pdf")]
        if len(pdfs) != 1:
            print(f"  !! expected exactly one PDF in the zip, found {len(pdfs)}")
            sys.exit(2)
        pdf = pdfs[0]
    else:
        pdf = src

    sha = hashlib.sha256(open(pdf, "rb").read()).hexdigest()
    txt = os.path.join(work, "kmrt.txt")
    subprocess.run(["pdftotext", "-layout", pdf, txt], check=True)
    return open(txt, encoding="utf-8", errors="replace").read(), sha, os.path.basename(pdf)


BOOK = ""          # raw extracted text
BOOK_N = ""        # whitespace-normalised


def quote(tag: str, page_hint: str, text: str) -> bool:
    """Control C4: assert `text` is really in the book, print it, return presence."""
    ok = norm(text) in BOOK_N
    mark = "FOUND" if ok else "ABSENT"
    print(f"\n  [{tag}] {page_hint} -- {mark} in the supplied text")
    for ln in text.strip().splitlines():
        print(f"      {ln.strip()}")
    if not ok:
        fail("C4", f"{tag} quotation not located in the book")
    return ok


# ----------------------------------------------------------------------------- main

def main() -> int:
    global BOOK, BOOK_N

    print("=" * 78)
    print(" KMRT ARRIVES -- the trialitarian record verified against the source")
    print("=" * 78)

    BOOK, sha, name = load_book()
    BOOK_N = norm(BOOK)
    print(f"\n  source          : {name}")
    print(f"  sha256          : {sha}")
    print(f"  extracted chars : {len(BOOK):,}")
    draft = "(??)" in BOOK
    print(f"  draft (cross-references render as '(??)') : {draft}")
    if not draft:
        print("  NOTE: this copy resolves its cross-references -- not the draft the seal describes.")

    # ---------------------------------------------------------------- C5 : the quote instrument
    rule("CONTROL C5 -- the quotation instrument must be able to say ABSENT")
    print("""
    C4 asserts quotations are present.  A substring test that always says FOUND
    proves nothing, so before any quotation is trusted the instrument is shown
    rejecting a sentence built to look exactly like the book's prose and to be
    false about it.  (Memo 164: control passing is not instrument working.)""")
    decoy = ("6D4 if L is a cyclic field extension of F and 3D4 if L (x) Delta "
             "is a Galois field extension with group S3 over F")
    decoy_found = norm(decoy) in BOOK_N
    print(f"\n    decoy (the 3D4/6D4 clauses SWAPPED): {'FOUND' if decoy_found else 'ABSENT'}")
    # NB the PDF's Delta is U+2206 INCREMENT, not U+0394 GREEK CAPITAL DELTA.
    real = "6D4 if L \u2297 \u2206 is a Galois field extension with group S3 over F"
    real_found = norm(real) in BOOK_N
    print(f"    the true clause, same instrument    : {'FOUND' if real_found else 'ABSENT'}")
    c5 = (not decoy_found) and real_found
    print(f"\n  C5: {'PASS' if c5 else 'FAIL'} -- the instrument separates the two")
    if not c5:
        fail("C5", "the quotation instrument cannot distinguish a decoy from the source")

    # ---------------------------------------------------------------- C3 : the field
    rule("CONTROL C3 -- PARI's K reproduces B1093's hand-proved facts")
    d = gp_lines("""
        K = nfinit(x^3 - 12*x - 5);
        print("disc=", K.disc);
        print("sign=", K.sign);
        print("naut=", #nfgaloisconj(K));
        print("irred=", polisirreducible(x^3-12*x-5));
        print("galgrp=", polgalois(x^3-12*x-5)[4]);
    """)
    print(f"    disc(K)        = {d['disc']}        (B1093: 6237)")
    print(f"    signature      = {d['sign']}      (B1093: [3,0], totally real)")
    print(f"    #Aut(K/Q)      = {d['naut']}           (memo 204: 1)")
    print(f"    x^3-12x-5 irreducible = {d['irred']}")
    print(f"    Gal of the closure    = {d['galgrp']}")
    c3 = (d["disc"] == "6237" and d["sign"] == "[3, 0]" and d["naut"] == "1"
          and d["irred"] == "1")
    print(f"\n  C3: {'PASS' if c3 else 'FAIL'}")
    if not c3:
        fail("C3", "PARI's K does not reproduce B1093")

    # ---------------------------------------------------------------- CELL 5 (cheap, do it first)
    rule("CELL 5 -- is the bench's own citation right?")
    head_x = "X. TRIALITARIAN CENTRAL SIMPLE ALGEBRAS"
    head_viii = "VIII. COMPOSITION AND TRIALITY"
    in_x = norm(head_x) in BOOK_N
    in_viii = norm(head_viii) in BOOK_N
    print(f"    running head '{head_x}'  present: {in_x}")
    print(f"    running head '{head_viii}' present: {in_viii}")
    # locate the running head nearest each section title
    def chapter_of(section_title: str) -> str:
        i = BOOK.find(section_title)
        if i < 0:
            return "NOT FOUND"
        window = BOOK[max(0, i - 6000): i + 6000]
        hits = re.findall(r"\b([IVX]+)\.\s+[A-Z][A-Z ]{6,}", window)
        return hits[0] if hits else "NO RUNNING HEAD NEARBY"

    ch43 = chapter_of("43. Trialitarian Algebras")
    ch44 = chapter_of("44.B. The Clifford invariant")
    ch36 = chapter_of("36. Twisted Compositions")
    print(f"\n    section 43   sits in chapter : {ch43}")
    print(f"    section 44.B sits in chapter : {ch44}")
    print(f"    section 36   sits in chapter : {ch36}")
    cell5 = "A" if (ch43 == "X" and ch44 == "X") else ("B" if ch43 == "VII" else "NEITHER")
    print(f"\n  >>> CELL 5 OUTCOME {cell5}: the standing ask says 'Ch. VII SS43 and SS44.B';")
    print(f"      in this draft SS43 and SS44 are CHAPTER {ch43}, and SS36 is CHAPTER {ch36}.")

    # ---------------------------------------------------------------- CELL 1
    rule("CELL 1 -- does KMRT's own definition type the object's cubic as 6D4?")
    q43c = """43.C. Trialitarian algebras of type 2D4 . We say that a trialitarian algebra
T = (E, L, ∆, σ, αi ) of type 1D4 if L is split, 2D4 if L = F × K for K a quadratic
separable field extension over F isomorphic to ∆, 3D4 if L is a cyclic field extension
of F and 6D4 if L ⊗ ∆ is a Galois field extension with group S3 over F ."""
    got43c = quote("SS43.C", "p. 556", q43c)

    print("\n    Now every quantity that sentence tests, computed for K:")
    d = gp_lines("""
        K = nfinit(x^3 - 12*x - 5);
        print("issplit=", 0);
        print("isfield=", polisirreducible(x^3-12*x-5));
        print("disc=", K.disc);
        print("sqfree=", core(K.disc));
        print("discsquare=", issquare(K.disc));
        print("naut=", #nfgaloisconj(K));
        C = polredbest(polcompositum(x^3-12*x-5, x^2-77)[1]);
        print("closurepoly=", C);
        print("closuredeg=", poldegree(C));
        print("closureaut=", #nfgaloisconj(nfinit(C)));
        print("closurelabel=", polgalois(C)[4]);
        print("closureord=", polgalois(C)[1]);
        print("closureabelian=", galoisisabelian(galoisinit(C), 1));
        print("cubiclabel=", polgalois(x^3-12*x-5)[4]);
        print("cubicord=", polgalois(x^3-12*x-5)[1]);
    """, timeout=900)
    print(f"    L = K is a FIELD (not split)           : {d['isfield'] == '1'}")
    print(f"    so L is not F x F x F  -> NOT 1D4")
    print(f"    L is cubic, not F x (quadratic)        -> NOT 2D4")
    print(f"    disc(K) = {d['disc']}, squarefree part {d['sqfree']}, a square: "
          f"{d['discsquare'] == '1'}")
    print(f"    => Delta = Q(sqrt({d['sqfree']})) is a FIELD, so K is NOT cyclic")
    print(f"    #Aut(K/Q) = {d['naut']} (cyclic would need 3)  -> NOT 3D4")
    print(f"\n    K (x) Delta : {d['closurepoly']}")
    print(f"        degree over Q      = {d['closuredeg']}")
    print(f"        #automorphisms     = {d['closureaut']}  (Galois iff = degree)")
    print(f"        order of the group = {d['closureord']}")
    print(f"        abelian            = {d['closureabelian'] == '1'}")
    print(f"        PARI's degree-6 label = {d['closurelabel']}")
    print("        -- PARI names S3 ACTING ON 6 POINTS 'D_6(6)': the dihedral group of")
    print("           order 6 IS S3.  The structural test used here is ORDER 6 AND")
    print("           NON-ABELIAN, not the label string.")
    print(f"        and on the cubic itself PARI returns {d['cubiclabel']}, order {d['cubicord']}")

    cell1_ok = (got43c
                and d["isfield"] == "1"
                and d["discsquare"] == "0"
                and d["sqfree"] == "77"
                and d["naut"] == "1"
                and d["closuredeg"] == "6"
                and d["closureaut"] == "6"
                and d["closureord"] == "6"
                and d["closureabelian"] == "0"
                and d["cubiclabel"].strip('"') == "S3")
    cell1 = "A" if cell1_ok else "B"
    print(f"\n  >>> CELL 1 OUTCOME {cell1}: K (x) Delta IS a Galois field extension with")
    print("      group S3 over Q -- KMRT's 6D4 clause, literally, and none of the other three.")

    # ---------------------------------------------------------------- CELL 2
    rule("CELL 2 -- is a cyclic composition available over K?")
    q36b = """36.B. Cyclic compositions. Twisted compositions of dimension 8 over cyclic
cubic extensions were introduced in Springer [?]. We first recall Springer’s defini-
tion. Let (L/F, ρ) be a cyclic F -algebra of degree 3 with ρ a generator of the
group Gal(L/F ) = A3 ."""
    got36b = quote("SS36.B", "p. 494", q36b)
    q36b2 = """Observe that the choice of a generator ρ of
the group Gal(L/F ) is part of the datum defining a cyclic composition."""
    got36b2 = quote("SS36.B", "p. 494", q36b2)
    q36c = """36.C. Twisted Hurwitz compositions. In this section we first extend the
construction of a twisted composition C ⊗ L given in Example (??) for L cyclic to
an arbitrary cubic étale algebra L and a para-Hurwitz algebra (C, ?, n)."""
    got36c = quote("SS36.C", "p. 498", q36c)

    print(f"\n    #Aut(K/Q) = {d['naut']}.  Gal(K/Q) = A3 requires 3 automorphisms.")
    cell2_ok = got36b and got36b2 and d["naut"] == "1"
    cell2 = "A" if cell2_ok else "B"
    print(f"\n  >>> CELL 2 OUTCOME {cell2}: the generator rho that SS36.B makes PART OF THE DATUM")
    print("      does not exist over K.  No cyclic composition over K, by the definition.")
    print(f"      And SS36.C supplies the replacement for arbitrary cubic etale L: {got36c}")

    # ---------------------------------------------------------------- CELL 3
    rule("CELL 3 -- is memo 204's pinned shape KMRT's normal form?")
    q438 = """(43.8) Theorem. Let Q be a quaternion algebra over a cubic étale algebra L.
Then M4 (Q) admits a trialitarian structure T (Q) if and only if NL/F ([Q]) = 1 in
Br(F )."""
    got438 = quote("Thm 43.8", "p. 553", q438)
    q439 = """(43.9) Proposition. Let L/F be a cubic étale algebra and let Q be a quaternion
algebra over L. The following conditions are equivalent:
(1) NL/F ([Q]) = 1.
(2) Q ≃ (a, b)L with b ∈ F × and NL (a) = 1."""
    got439 = quote("Prop 43.9", "p. 553", q439)
    q4311 = """(43.11) Proposition. Let K/F be quadratic étale, let L/F be cubic étale and let
a ∈ L× be such that NL (a) = 1. Let Q be the quaternion algebra (K ⊗ L/L, a)L"""
    got4311 = quote("Prop 43.11", "p. 554", q4311)
    q4314 = """(43.14) Proposition. The following conditions are equivalent:
(1) E(a1 ) ≃ E(a2 ) as trialitarian algebras."""
    got4314 = quote("Prop 43.14", "p. 556", q4314)
    qalbert = """over number fields any central simple algebra which admits an involution of the first kind is of the form Mn (Q)"""
    gotalbert = quote("SS43.B (Albert)", "p. 553", qalbert)

    print("""
    Memo 204 addendum 4 pinned the object's commutant as a QUATERNION ALGEBRA
    OVER K CONTAINING K(sqrt 77) AS A MAXIMAL SUBFIELD, with the second slot
    UNKNOWN -- written there as "(77, b)_K with b unknown".

    KMRT 43.9 fixes which slot is which: the rational element is b IN F^x, and
    the unknown is a IN L^x with N_{L/F}(a) = 1.  Memo 204's 77 IS the rational
    slot.  So the object's candidate is""")
    print("        Q = (a, 77)_K ,   a in K^x ,   N_{K/Q}(a) = 1 ,")
    print("    and 43.11 says EVERY such a gives a trialitarian algebra E(a) = M_4(Q).")
    cell3_ok = got438 and got439 and got4311
    cell3 = "A" if cell3_ok else "B"
    print(f"\n  >>> CELL 3 OUTCOME {cell3}: memo 204's pin sits inside KMRT's normal form,")
    print("      with exactly one unknown, and that unknown is norm-one in K.")

    # ---------------------------------------------------------------- C1
    rule("CONTROL C1 -- nfhilbert must be able to say BOTH things")
    d1 = gp_lines("""
        K = nfinit(x^3 - 12*x - 5);
        print("split_11_77=", nfhilbert(K, 1, 77));
        print("ram_m1_m1=", nfhilbert(K, -1, -1));
        print("Q_ram_2_2=", hilbert(-1,-1,2));
    """)
    print(f"    nfhilbert(K,  1, 77) = {d1['split_11_77']}   (a square in the first slot: must split)")
    print(f"    nfhilbert(K, -1, -1) = {d1['ram_m1_m1']}   (K totally real: (-1,-1) must ramify)")
    c1 = d1["split_11_77"] == "1" and d1["ram_m1_m1"] == "-1"
    print(f"\n  C1: {'PASS' if c1 else 'FAIL'} -- the instrument returns both values in this run")
    if not c1:
        fail("C1", "nfhilbert did not exhibit both values")

    # ---------------------------------------------------------------- CELL 4
    rule("CELL 4 -- does the classification DECIDE memo 204's open E-question?")
    print("""
    THE FAMILY, stated before the search:  for x ranging over
        x = c0 + c1*t + c2*t^2 ,  t a root of x^3-12x-5 ,  c_i in [-3,3] , x != 0 ,
    put  a = x^3 / N_{K/Q}(x) .   Then N_{K/Q}(a) = N(x)^3 / N(x)^3 = 1 identically,
    so every member of the family is admissible for 43.9/43.11 BY CONSTRUCTION.
    The certificate checks that identity rather than assuming it.

    REAL PLACES, settled in advance and not by search: b = 77 > 0 under all three
    real embeddings of K, so (a,77)_K is SPLIT AT EVERY REAL PLACE for EVERY a.
    Memo 204's "unramified at all three real places" is therefore automatic for
    this shape -- it constrains nothing, and no example needs screening for it.
    """)
    setup = "K = nfinit(x^3 - 12*x - 5); t = Mod(x, x^3-12*x-5);"
    block = r"""
    found = 0; tested = 0; normfail = 0; nonsplit = 0;
    for(c0=-3,3, for(c1=-3,3, for(c2=-3,3,
        xx = c0 + c1*t + c2*t^2;
        if(xx == 0, next);
        nx = norm(xx);
        if(nx == 0, next);
        a = xx^3 / nx;
        tested = tested + 1;
        if(norm(a) != 1, normfail = normfail + 1);
        if(nfhilbert(K, lift(a), 77) == -1,
            nonsplit = nonsplit + 1;
            if(found < 6,
                found = found + 1;
                print("HIT=", found, ";", c0, ";", c1, ";", c2, ";", lift(a), ";", nx)
            )
        )
    )));
    print("tested=", tested);
    print("normfail=", normfail);
    print("nonsplit=", nonsplit);
    """
    out = gp_block(setup, block, timeout=1800)

    hits = []
    stats = {}
    for ln in out.splitlines():
        if ln.startswith("HIT="):
            parts = ln.split(";")
            hits.append({"i": parts[0].split("=")[1].strip(),
                         "c": (parts[1].strip(), parts[2].strip(), parts[3].strip()),
                         "a": parts[4].strip(), "nx": parts[5].strip()})
        elif "=" in ln:
            k, _, v = ln.partition("=")
            stats[k.strip()] = v.strip()

    print(f"    family size searched        : {stats.get('tested')}")
    print(f"    members with N(a) != 1      : {stats.get('normfail')}   (must be 0)")
    print(f"    members with (a,77)_K NOT split : {stats.get('nonsplit')} (first six reported)")
    if stats.get("normfail") != "0":
        fail("CELL4", "the family's norm-one identity does not hold -- family is wrong")

    for h in hits:
        print(f"\n      x = {h['c'][0]} + {h['c'][1]}*t + {h['c'][2]}*t^2 ,  N(x) = {h['nx']}")
        print(f"      a = x^3/N(x) = {h['a']}")

    cell4 = "A" if hits else "B"

    # ---------------------------------------------------------------- C2
    rule("CONTROL C2 -- KMRT's own consequence, checked on every example found")
    print("""
    43.9 (2)=>(1) is the projection formula: cor_{K/Q}(a,77)_K = (N_{K/Q}(a),77)_Q
    = (1,77)_Q = 1.  Its arithmetic content is that the ramified primes of K lie
    over each rational prime in EVEN NUMBER.  That is checked here, not assumed.
    A quaternion algebra (a,b) can ramify only at primes above 2, at primes where
    v(b) is odd (here: 7 and 11), and at primes where v(a) is odd -- so factoring
    a and adjoining 2, 7, 11 gives a PROVABLY COMPLETE candidate set.
    """)
    kept, discarded = [], []
    for h in hits:
        setup2 = f"K = nfinit(x^3 - 12*x - 5); a = {h['a']};"
        block2 = r"""
        cand = List();
        f = idealfactor(K, a);
        for(i=1, matsize(f)[1], listput(cand, f[i,1]));
        for(j=1, 3, p = [2,7,11][j]; d = idealprimedec(K, p);
            for(i=1, #d, listput(cand, d[i])));
        seen = List();
        for(i=1, #cand,
            pr = cand[i];
            key = Str(pr.p, "_", pr.f, "_", pr.e, "_", pr.gen[2]);
            dup = 0;
            for(j=1, #seen, if(seen[j] == key, dup = 1));
            if(dup == 0,
                listput(seen, key);
                if(nfhilbert(K, a, 77, pr) == -1,
                    print("RAM=", pr.p, ";", pr.f, ";", pr.e))
            )
        );
        print("ncand=", #seen);
        """
        out2 = gp_block(setup2, block2, timeout=900)
        ram, ncand = [], "?"
        for ln in out2.splitlines():
            if ln.startswith("RAM="):
                p, f_, e_ = ln.split("=")[1].split(";")
                ram.append((int(p), int(f_), int(e_)))
            elif ln.startswith("ncand="):
                ncand = ln.split("=")[1].strip()
        byp: dict[int, int] = {}
        for p, _f, _e in ram:
            byp[p] = byp.get(p, 0) + 1
        ok = all(v % 2 == 0 for v in byp.values())
        print(f"\n      a = {h['a'][:60]}{'...' if len(h['a']) > 60 else ''}")
        print(f"        candidate primes tested          : {ncand} (complete: above 2, 7, 11, and odd v(a))")
        print(f"        ramified finite primes (p, f, e) : {ram if ram else 'NONE'}")
        print(f"        count over each rational prime   : {byp}")
        print(f"        all counts even (N_K/Q([Q]) = 1) : {ok}")
        (kept if ok else discarded).append((h, ram, byp))
        if not ok:
            print("        >> DISCARDED: violates 43.9's consequence, reported not kept")

    c2 = bool(hits) and not discarded
    print(f"\n  C2: {'PASS' if c2 else ('FAIL' if discarded else 'NO EXAMPLES TO CHECK')}"
          f" -- {len(kept)} kept, {len(discarded)} discarded")
    if discarded:
        fail("C2", f"{len(discarded)} example(s) violate the projection formula")

    # ---------------------------------------------------------------- verdict
    rule("CELL 4 VERDICT")
    if cell4 == "A" and kept:
        h, ram, byp = kept[0]
        print(f"""
    OUTCOME A.  Exhibited: a = {h['a']}
    with N_{{K/Q}}(a) = 1, so by 43.11 M_4((a,77)_K) IS a trialitarian algebra over
    K -- type 6D4 by CELL 1 -- and by CELL 3 it is in KMRT's normal form.  It is
    SPLIT AT ALL THREE REAL PLACES (77 > 0 everywhere) and NOT SPLIT globally
    (nfhilbert = -1), ramifying at {byp}.

    So a NON-SPLIT quaternion algebra satisfies EVERY constraint the record has
    established about the object's commutant.""")
    else:
        print(f"""
    OUTCOME B.  No member of the searched family of size {stats.get('tested')} gave a
    non-split (a,77)_K.  REPORTED AS A NOT-FOUND OVER A STATED FAMILY, not as a
    proof that none exists.""")

    # ---------------------------------------------------------------- CELL 6
    rule("CELL 6 -- could (a,77)_K have been non-split at all?  [NOT PREREGISTERED]")
    print("""
    FILED AFTER CELL 4 RETURNED B, under seal ADDENDUM 1 and standing rule
    R121/memo 213: when a statistic comes out identical across every case, ask
    whether it COULD have differed BEFORE banking the constancy.  Nothing below
    is preregistered and the memo says so.

    n_p := the number of primes w of K above p at which 77 is NOT a square in
    K_w -- i.e. the number of primes above p where a quaternion algebra
    (77, .)_K is CAPABLE of ramifying at all.""")

    setup6 = "\n".join([
        "K = nfinit(y^3 - 12*y - 5);",
        "rnf = rnfinit(K, x^2 - 77);",
        "nA(p) = {my(d=idealprimedec(K,p),n=0); for(i=1,#d, my(t=nfmodprinit(K,d[i]));"
        " if(!issquare(nfmodpr(K,77,t)), n=n+1)); n;}",
        "nB(p) = {my(d=idealprimedec(K,p),n=0); for(i=1,#d,"
        " if(#rnfidealprimedec(rnf,d[i]) < 2, n=n+1)); n;}",
    ])
    block6 = r"""
    print("Mdisc=", factor(nfinit(polredbest(polcompositum(y^3-12*y-5, y^2-77)[1])).disc));
    for(j=1,4, p=[2,3,7,11][j]; d = idealprimedec(K,p);
      print("SMALL=", p, ";", vector(#d,i,[d[i].e,d[i].f]), ";",
            vector(#d,i,idealval(K,77,d[i])), ";", nB(p)));
    mx = 0; mism = 0; pat = List();
    forprime(p=2, 500,
      b = nB(p);
      if(b > mx, mx = b);
      if(p != 2 && p != 3 && p != 7 && p != 11,
        if(nA(p) != b, mism = mism + 1; print("MISMATCH=", p)));
      d = idealprimedec(K,p);
      key = Str(vector(#d,i,d[i].f), " e", vector(#d,i,d[i].e));
      seen = 0;
      for(i=1, #pat, if(pat[i][1] == key, seen = 1;
        if(pat[i][2] != b, print("NONCONSTANT=", key, ";", p))));
      if(seen == 0, listput(pat, [key, b, p])));
    print("maxn=", mx);
    print("mismatch=", mism);
    for(i=1, #pat, print("PATTERN=", pat[i][1], ";", pat[i][2], ";", pat[i][3]));
    """
    out6 = gp_block(setup6, block6, timeout=1800)

    small, patterns, mismatches = [], [], []
    st6 = {}
    for ln in out6.splitlines():
        if ln.startswith("SMALL="):
            small.append(ln.split("=", 1)[1].split(";"))
        elif ln.startswith("PATTERN="):
            patterns.append(ln.split("=", 1)[1].split(";"))
        elif ln.startswith("MISMATCH="):
            mismatches.append(ln.split("=", 1)[1].strip())
        elif ln.startswith("NONCONSTANT="):
            fail("CELL6", f"n_p is not constant on a splitting pattern: {ln}")
        elif "=" in ln:
            k, _, v = ln.partition("=")
            st6[k.strip()] = v.strip()

    if not small or not patterns:
        fail("CELL6", "a GP table came back EMPTY -- the block did not execute")
    print(f"\n    disc of the sextic M = K(sqrt 77):  {st6.get('Mdisc','?')}")
    print("    -- so M/Q ramifies ONLY at 3, 7, 11: those are the finitely many")
    print("       primes that cannot be reached by a Frobenius-class argument,")
    print("       and each is computed individually below.")
    print("\n    p  | (e,f) of the primes of K | v_w(77)       | n_p")
    print("    ---+--------------------------+---------------+----")
    for row in small:
        print(f"    {row[0].strip():<3}| {row[1].strip():<25}| {row[2].strip():<14}| {row[3].strip()}")

    print("\n    n_p by splitting pattern, over every prime p < 500:")
    print("    f-pattern and e-pattern            | n_p | first p")
    print("    -----------------------------------+-----+--------")
    for row in patterns:
        print(f"    {row[0].strip():<35}| {row[1].strip():<4}| {row[2].strip()}")
    print("\n    n_p was CONSTANT on every splitting pattern observed (a NONCONSTANT")
    print("    line above would have failed the run; there is none).")
    print(f"\n    max n_p over all p < 500 : {st6.get('maxn')}")

    # ---- C7
    print("\n  CONTROL C7 -- two independent instruments")
    print(f"    residue-field test vs splitting test, odd p < 500 with 77 a unit:")
    print(f"    disagreements: {len(mismatches)} {mismatches if mismatches else ''}")
    c7 = (not mismatches) and bool(patterns)
    print(f"    (p = 2 was EXCLUDED IN ADVANCE: the residue-field test is invalid in")
    print(f"     characteristic 2.  It is not excluded because it disagreed.)")
    print(f"  C7: {'PASS' if c7 else 'FAIL'}")
    if not c7:
        fail("C7", "the two square-tests disagree where both are valid")

    # ---- C6
    print("\n  CONTROL C6 -- is 'n_p <= 1' a fact about 77, or about the instrument?")
    setup6b = "K = nfinit(y^3 - 12*y - 5);"   # no function defs: brace-safe
    block6b = r"""
    for(j=1, 6, b = [77, 5, 13, 33, -1, 3][j];
      rnf2 = rnfinit(K, x^2 - b);
      mx = 0; atp = 0;
      forprime(p=2, 300,
        d = idealprimedec(K,p); n = 0;
        for(i=1,#d, if(#rnfidealprimedec(rnf2,d[i]) < 2, n = n+1));
        if(n > mx, mx = n; atp = p));
      print("BVAL=", b, ";", mx, ";", atp));
    """
    out6b = gp_block(setup6b, block6b, timeout=1800)
    bvals = [ln.split("=", 1)[1].split(";") for ln in out6b.splitlines()
             if ln.startswith("BVAL=")]
    print("\n      b   | max n_p over p < 300 | attained at p")
    print("      ----+----------------------+--------------")
    for row in bvals:
        print(f"      {row[0].strip():<4}| {row[1].strip():<21}| {row[2].strip()}")
    if not bvals:
        fail("C6", "the control's GP table came back EMPTY -- the block did not execute")
    others = [int(r[1]) for r in bvals if r[0].strip() != "77"]
    c6 = bool(others) and max(others) >= 2
    print(f"\n    Some b reaches n_p >= 2 : {c6}")
    print("    So the count CAN exceed 1, and 'n_p <= 1' is a property of 77 over K.")
    print("    THE REASON, and it is not a coincidence: 77 is the squarefree part of")
    print("    disc(K), so Q(sqrt 77) is K's QUADRATIC RESOLVENT and K(sqrt 77) is K's")
    print("    GALOIS CLOSURE.  For a generic b, K(sqrt b) is not Galois over Q and the")
    print("    count is unconstrained.")
    print(f"  C6: {'PASS' if c6 else 'FAIL'}")
    if not c6:
        fail("C6", "no b reached n_p >= 2; the statistic could not have differed")

    cell6_ok = (st6.get("maxn") == "1" and c6 and c7 and bool(small) and bool(patterns)
                and all(r[3].strip() in ("0", "1") for r in small))
    cell6 = "A" if cell6_ok else "B"
    # SS44.16 is what makes CELL 6's arithmetic structural rather than merely negative.
    q4416 = """(44.16) Proposition. (1) If T = (E, L, σ, αE ) is a trialitarian algebra such that
[E] = 1 ∈ Br(L), then there exists a twisted composition Γ = (V, L, N, β) such that
T = End(Γ).
(2) Γ, Γ0 are twisted compositions such that End(Γ) ≃ End(Γ0 ) if and only if there
exists λ ∈ L× such that Γ0 ≃ Γλ ."""
    got4416 = quote("Prop 44.16", "p. 563", q4416)
    q436 = """(43.6) Proposition. For any trialitarian algebra T = (E, L, σ, αE ) the central
simple L-algebra E satisfies NL/F ([E]) = 1 ∈ Br(F )."""
    got436 = quote("Prop 43.6", "p. 552", q436)
    if not (got4416 and got436):
        fail("CELL6", "the two propositions CELL 6 leans on could not be located")

    if cell6 == "A":
        print(f"""
  >>> CELL 6 OUTCOME A.  n_p <= 1 for EVERY rational prime p.  Exhaustive because
      M = K(sqrt 77) ramifies only at 3, 7, 11 -- all three computed above -- and at
      every unramified p the count depends only on the Frobenius class in S3, of
      which there are three, each with a computed representative.

      CONSEQUENCE, a deduction and not a search:  let Q be ANY quaternion algebra
      over K containing K(sqrt 77) as a maximal subfield, with N_{{K/Q}}([Q]) = 1.
        * it can ramify at no more than ONE prime above each rational prime (n_p <= 1);
        * the norm condition forces an EVEN number above each rational prime;
        * so it ramifies at NO finite place;
        * and 77 > 0 in all three real embeddings, so at no real place either.
      A quaternion algebra unramified at every place is SPLIT.

      SO THERE WAS NEVER A NON-SPLIT EXAMPLE TO FIND.  CELL 4's OUTCOME B was the
      TRUE ANSWER, not a search limit.

      AND THE NORM CONDITION IS NOT AN ASSUMPTION HERE: 43.6, quoted above, gives
      N_{{L/F}}([E]) = 1 for EVERY trialitarian algebra.  So the hypothesis is only
      that the object's E carries the trialitarian structure -- which is what the
      6D4 typing asserts and CELL 1 verified against the definition.

      WHAT [E] = 1 THEN BUYS, by 44.16(1) quoted above: the object's trialitarian
      algebra is End(Gamma) for a TWISTED COMPOSITION Gamma over K -- and 44.16(2)
      classifies those up to Gamma -> Gamma_lambda.  SS36.C constructs them for an
      arbitrary cubic etale L by descent from L (x) Delta.  The structure memo 203
      reached for from search summaries is a named, finite, constructible object.""")
    else:
        print(f"""
  >>> CELL 6 OUTCOME B.  The exhaustiveness argument did NOT close: max n_p =
      {st6.get('maxn','?')}, tables populated = {bool(small) and bool(patterns)},
      C6 = {'PASS' if c6 else 'FAIL'}, C7 = {'PASS' if c7 else 'FAIL'}.
      NO CONSEQUENCE IS DRAWN.  CELL 4's outcome B stands as a not-found over a
      stated family and nothing more.""")

    # ---------------------------------------------------------------- summary
    print("\n" + "=" * 78)
    print(" OUTCOMES")
    print("=" * 78)
    print(f"   CELL 1 (KMRT types the object 6D4)        : {cell1}")
    print(f"   CELL 2 (no cyclic composition over K)     : {cell2}")
    print(f"   CELL 3 (memo 204's pin is the normal form): {cell3}")
    print(f"   CELL 4 (classification decides E?)        : {cell4}")
    print(f"   CELL 5 (the bench's citation)             : {cell5}")
    print(f"   CELL 6 (could it have differed?) NOT PREREG: {cell6}")
    print(f"   C1 instrument bites   : {'PASS' if c1 else 'FAIL'}")
    print(f"   C2 projection formula : {'PASS' if c2 else ('FAIL' if discarded else 'N/A')}")
    print(f"   C3 field is B1093's K : {'PASS' if c3 else 'FAIL'}")
    print(f"   C4 quotations located : {'PASS' if not [f for f in FAILURES if f.startswith('C4')] else 'FAIL'}")
    print(f"   C5 quote instr. bites : {'PASS' if c5 else 'FAIL'}")
    print(f"   C6 count could differ : {'PASS' if c6 else 'FAIL'}")
    print(f"   C7 two instruments    : {'PASS' if c7 else 'FAIL'}")
    if FAILURES:
        print("\n  FAILURES:")
        for f in FAILURES:
            print(f"    - {f}")
    print("=" * 78)
    return 1 if FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
