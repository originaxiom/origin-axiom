# THE KNOT READING'S S³ IS THE OBJECT'S OPEN-BOOK CLOSING (A FOLLOW-UP TO f823dd25f; THE OWNER'S "ATTACK THE CHIRAL PREMISE"; DATA-FREE): THE OBJECT'S TWO-TICK WORD LR, READ LETTER BY LETTER AS DEHN TWISTS WITH THE BOUNDARY FIXED, IS AN OPEN BOOK OF S³ WHOSE BINDING IS THE FIGURE-EIGHT KNOT. IN EITHER ORIENTATION L AND R ARE TWISTS OF OPPOSITE HANDEDNESS ABOUT DUAL CURVES (B287 RECORDS THE MONODROMY AS t_α t_β⁻¹), AND BALDWIN NAMES (Σ, xy⁻¹)'S BINDING THE FIGURE EIGHT; HIS LEMMA 2.1 MAKES THAT OPEN BOOK THE DOUBLE COVER OF S³ BRANCHED ALONG THE CLOSED BRAID σ₁σ₂⁻¹, AN UNKNOT. SO THE KNOT READING'S S³ IS NOT BROUGHT IN FROM OUTSIDE: IT IS THE CLOSING THAT FILLS THE BINDING, THE MERIDIAN FILLING THAT B287'S TABLE LISTS AS S³. B287'S DISTINGUISHED CLOSING IS THE OTHER STANDARD ONE, THE FIBER SLOPE, WHICH CAPS THE PAGE AND GIVES THE SOL TORUS BUNDLE OF A. SO, OF THE OBJECT'S OWN TOPOLOGICAL READINGS, THE PREMISE BECOMES WHICH CARRIES THE SCALE: THE BINDING IN ITS OPEN BOOK (ONE FACTOR, WITTEN'S (2.30)), THE UNCLOSED BUNDLE (TWO FACTORS), OR B287'S CAPPED CLOSING, A SOL MANIFOLD WHOSE REPRESENTATIONS ALL HAVE VOLUME ZERO; f823dd25f'S (i-b), P-725'S TWO SECTORS, IS NOT A CLOSING AND STANDS. AMONG POSITIVE WORDS WITH BOTH LETTERS ONLY LR CLOSES THIS WAY TO A HOMOLOGY SPHERE; THE EXCURSION MEMBERS' OPEN BOOKS HAVE H₁ ≠ 0, WHERE WITTEN'S S³ STEP DOES NOT APPLY. NOTHING IS EVALUATED

**From:** the web seat (chat1), 2026-11-06. **To:** cc (main).

**On:**
- this seat's f823dd25f (THE CHIRAL PREMISE, ATTACKED). Its reading (i-a), the knot 4₁ in S³ in a holomorphic
  representation, read one factor without the pin. It took S³ as m004's unique S³ filling, which "adds one decision, to
  fill, and no choice of filling". This note adds that this filling is the closing of the object's own word, read as an
  open book;
- B287 (the distinguished closing) and its table of m004's exceptional fillings;
- the owner's goal, "Find a process in the object that places τ, the line and an energy scale, so we stop choosing
  them", and his choice "Attack the chiral premise".

**Kind:** data-free. One pre-registered check, committed before it ran:
`relays/chat1_2026-11-06_chiral/open_book_check.py`, sha256 aaa6fa48… recorded 22:52:45Z at 7f4ffee95; output at
028917ec1, O1–O8 all True as predicted.
- It is sympy on 2 × 2 integer matrices, plus three SnapPy checks. It prints the library versions and booleans only.
- Before the run, the file was compiled, and its sympy and SnapPy calls were exercised on unrelated inputs (m003, an
  unrelated matrix) outside the repository.

**Swept first** (main at 5b90ef469; `--no-aliases`; main-only form):
- `VERDICT topic-sweep /open book|binding|Dehn twist|Hopf band|plumbing|boundary twist|fibered knot|genus.one fibered|monodromy of the figure|meridian filling|S³ filling|filling slope/ (full text): 111 of 1594 arcs on main match (NEGATIVE 27, OPEN 4, PROVED 79, no verdict file 1); 4 register rows match (DONE 3, QUEUED 1)`

**What it finds:**
- **No arc uses "open book", "Hopf band" or "genus one fibered".**
- **"binding"** (about 70 arcs, some only in their claim lines) matches in other senses: an obligation ("binding
  throughout"), a constraint, or the Fibonacci tight-binding chain.
- **"plumbing"** (13) names instrument controls.
- **"filling slope"** (13) is chiefly the record's closings. B82, B83, B86 and B153 use it for a character-variety
  component's slope, and B214 and B215 for the Borromean parent.
- **"Dehn twist"** (11) is chiefly the trace map and the mapping-class action (B148, B132, B150, B154).
  - **B132's convention takes the letters same-handed:** its SU(2)_k layer uses "Dehn twists `R=T`, `L=S T S⁻¹`".
    T and S T S⁻¹ are conjugate in SL(2,ℤ), so B132's m = 1 word is xy, the periodic class of trace 1, not LR.
  - B204 (ρ_k(L) written as S T⁻¹ S⁻¹) and B613 ("the S-conjugation swaps R ↔ L⁻¹") take them opposite-handed, as
    GENESIS and B287 do. This note follows those.
- **"boundary twist"** (1): B1634.
  - It cites "Mod(S₁¹) ≅ B₃ acting faithfully on π₁ = F₂, the boundary twist acting as conjugation by the commutator",
    and records "⟨L, R⟩ ≅ B₃ meets Inn(F₂) exactly in ⟨Δ⁴⟩ = ⟨conj(a b⁻¹ a⁻¹ b)⟩", with "Δ⁻¹ = R L⁻¹ R".
  - So on the ruled branch each letter is already one generator of the open book's monodromy group, with L and R⁻¹
    the positive ones and no boundary twist.
- **"monodromy of the figure"** (1): B1341, in a dynamics sense.
- **"fibered knot"** (2): B1263, "A fibered knot's fiber is the commutator subgroup"; and B287, read in full.
- **The 4 register rows** match "binding" (P-341, P-386, P-407) or "filling slope" (P-646).
- **Beside the sweep:** B1294 reads the fillings M(p/q) as double branched covers of S³ (Montesinos); B1733 has
  ∣det(A − I)∣; B1802 checks branch links of fillings.
- **B287 already holds the two facts this note builds on.**
  - "the once-punctured-torus bundle with monodromy word aB = t_α t_β⁻¹ = [[2,1],[1,1]] = A is isometric to m004";
  - the filling table, from "**0** | **ℤ** | **Sol — torus bundle**" to "meridian | 0 | `S³` | (the 10th)".
  - Its distinguished closing is the fiber slope: "the fiber slope (the boundary slope of the fiber, the 0-surgery
    m004(0,1)) caps the puncture and yields the closed Sol torus bundle whose monodromy is exactly A = [[2,1],[1,1]]".
- **Not on the record:** the word read as an open book; S³ as that open book's closed manifold; and the bearing of
  either on Witten's (2.30). B1294 and B1634 hold the pieces, but neither names the open book or its binding.

## 1. The open book of the object's word

**The letters are twists of opposite handedness (O1, O2).**
- **The convention.** A right-handed Dehn twist about a primitive class c acts on H₁ of the torus as v ↦ v + i(c, v)c,
  with i(u, v) = uᵀJv.
- **With J = [[0,1],[−1,0]]:** L is the right-handed twist about (1,0), and R is the inverse of the right-handed twist
  about (0,1).
- **R is a right-handed twist about no primitive class.** The right-handed twist about (p, q) has the matrix
  [[1 − pq, p²], [−q², 1 + pq]], whose lower-left entry is never positive (O1 checks entries up to 20).
- **With the other orientation, −J,** L is left-handed and R right-handed.
- **Convention-free:** S L S⁻¹ = R⁻¹ for S = [[0,−1],[1,0]], and the parabolic classes [[1, n],[0,1]] are pairwise
  non-conjugate in SL(2,ℤ). So R is conjugate to L⁻¹, not to L.
- **So in either orientation the record's L and R lift, letter by letter, to twists of opposite handedness about dual
  curves.** That is B287's "t_α t_β⁻¹", and B1634's L and R⁻¹ as the positive generators.

**The letter-by-letter lift is an open book.**
- **Baldwin's x and y are right-handed twists about dual curves on T,** the genus one surface with one boundary
  component, fixing the boundary.
  - arXiv:math/0607370 § 2: the mapping class group "is generated by right-handed Dehn twists about dual
    non-separating curves, x and y";
  - arXiv:0804.3624: "The diffeomorphism h² = (xy)⁶ is isotopic to a right-handed Dehn twist around a curve δ parallel
    to ∂T".
- **His Lemma 2.1** (arXiv:0804.3624): "If K is the closed 3-braid specified by w then Σ(K) has an open book
  decomposition (T, w(x, y, x⁻¹, y⁻¹))", where Σ(K) is "the double cover of S³ branched along K".
- **The lift of LR is xy⁻¹,** that is w = σ₁σ₂⁻¹; or its mirror x⁻¹y, w = σ₁⁻¹σ₂.

**Its closed manifold is S³, and its binding is the figure-eight (O3, O7, O8).**
- **Baldwin states it directly** (arXiv:math/0607370 § 2): "1. the binding of the open book (Σ, xy⁻¹), i.e. the figure
  eight", with the trefoils for x⁻¹y⁻¹ and xy.
- **By Lemma 2.1:**
  - σ₁σ₂⁻¹ has a 3-cycle as its permutation, so its closure is a knot;
  - its diagram has 2 crossings, so it is the unknot, and Σ(unknot) = S³;
  - the binding is then a genus one fibered knot in S³, and "the only GOF-knots in S³ are the right- and left-handed
    trefoil knots and the figure eight knot" (arXiv:math/0607370);
  - its monodromy has trace 3, so it is pseudo-Anosov, while the trefoils' monodromies, xy and its inverse, are
    periodic (xy has trace 1 and order 6, O3). So the binding is the figure-eight.
- **SnapPy is consistent.** '4_1' is isometric to 'b++LR', and its meridian filling has trivial fundamental group and
  trivial H₁ (O8). That filling is the row B287's table lists as "meridian | 0 | `S³`".
- **The lift's one decision is the literal one.**
  - Each letter is one twist, and no boundary twist is inserted. On the ruled branch this is the record's own
    ⟨L, R⟩ ≅ B₃ (B1634), whose Δ⁴ is the boundary twist.
  - Inserting d boundary twists gives −1/d surgery on the binding (arXiv:0804.3624). At d = ±1 that is B287's ±1 row, a
    homology sphere other than S³. So S³ needs d = 0.

## 2. Two standard closings of the object, and which one the knot reading uses

- **The open-book closing fills the binding.** Its slope is the meridian, here the flow line through the fixed
  boundary. It gives S³ with the figure-eight as binding.
  - This is the closing Witten's (2.30) needs: a Wilson line on the binding in S³. There the partner's flat
    connection 𝒜̃ is gauge-trivial, so the partner factor B̃(t̃) is present but does not depend on the knot.
  - So the knot reading's S³ (f823dd25f § 2 (f)) is the object's own open-book closing, not an outside embedding.
- **B287's distinguished closing caps the page.** Its slope is the fiber slope, and it gives the Sol torus bundle with
  monodromy exactly A.
  - B287 calls it "a canonical, forced, distinguished closing".
  - The knot reading does not use it.
- **B287's table already lists both closings.**
  - B287 chose the capped one for re-seeing A.
  - The open-book one is what the single-factor reading of the scale needs.
  - The hand decides neither: the amphichiral symmetry sends slope p/q to −p/q, which fixes both 0 and the meridian.

## 3. What the premise becomes

**The object supplies three topological readings.** Which one carries the scale is the premise, and the hand bit
decides none of them (f823dd25f § 3):
- **the binding in its open book:** a holomorphic Wilson line in S³, one factor, its partner present and blind to the
  knot (Witten's (2.30));
- **the unclosed bundle m004:** its partition function, with both factors depending on it (DGLZ (1.5));
- **B287's capped closing,** the Sol torus bundle:
  - its fundamental group is solvable, hence amenable, so its simplicial volume is 0;
  - since |Vol ρ| ≤ v₃‖M‖, every representation has volume 0 (standard; named, not re-derived);
  - so only a Chern–Simons phase can survive there, and no volume exponent.

**f823dd25f's readings, placed:**
- (i-a) and (ii) both read the knot in S³, so both sit on the open-book closing.
- (i-0) is the unclosed bundle with σ pinned to k.
- (i-b), P-725's two sectors, is not a closing and is unchanged.

**Of the three, only the binding in its open book gives the quantity main evaluated without the pin.**
- The unclosed bundle gives it only at the pin, and only in its classical exponent (f823dd25f § 2 (c)).
- The capped closing carries no volume exponent.
- f823dd25f's costs stay:
  - the volume pairs with t/2, not σ;
  - the value is exact only with Witten's choice of cycle;
  - the representation is a holomorphic one of dimension q's order.

## 4. LR is the only positive word that closes this way to a homology sphere

- **H₁ of the closing.** For an open book (T, φ) with connected binding, H₁ is the cokernel of φ_* − I on H₁(T). The
  mapping torus has H₁ = ℤ ⊕ coker(φ_* − I), and filling the binding kills the ℤ.
- **For φ in SL(2,ℤ), det(φ − I) = 2 − tr φ (O4).** For LR, φ − I is unimodular, so H₁ = 0 (O4). This is B287's
  "torsion 1" for its n = 1 base, seen on the other closing.
- **Among positive words in L and R with both letters, trace 3 occurs only for LR and RL.**
  - Such a word is cyclically LR·u with u positive.
  - If u is not empty, u = I + N with N ≥ 0 and N ≠ 0. Then tr(LR·u) = 3 + tr(LR·N) > 3, since every entry of LR is
    positive.
  - O5 confirms it for lengths 2 to 10.
  - So only LR's open book (RL's is conjugate to it) is a homology sphere.
- **The excursion members.** For P-723's L⁵R(LR)^k and L⁶R(LR)^k (k = 0–12) and P-726's L¹⁰RLR, tr − 2 > 1 (O6). Their
  open books have H₁ of order tr − 2 > 1.
  - A non-zero finite H₁ gives non-trivial abelian flat connections. So Witten's step "as S³ is simply-connected, …
    we can take 𝒜̃ = 0" does not apply there.
  - With non-trivial flat 𝒜̃ the integration cycle need not be a single product. Witten's S³ case is a product
    "(rather than a sum of such products, as in the more typical case (2.27))".
  - This agrees with f823dd25f's finding that no member is a knot complement in S³.

## 5. What this asks of main (owed, not done here)

1. **If R2's first choice is the knot reading (f823dd25f's (i-a)),** say that its S³ is the object's open-book closing,
   and reconcile it with B287's distinguished closing, which is the capped one.
2. **Confirm the standard fact § 3 uses:** every representation of the Sol closing's group has volume zero, so B287's
   distinguished closing carries no volume exponent.
3. **The literal lift** (one twist per letter, no boundary twist) is B1634's ⟨L, R⟩ ≅ B₃ on the ruled branch. Say
   whether the knot reading takes that lift.
4. **B132's convention.**
   - Its SU(2)_k layer takes the letters same-handed ("R=T, L=S T S⁻¹"), so its m = 1 word is the periodic class of
     trace 1, not the figure-eight's LR.
   - B204 and B613 take them opposite-handed, as GENESIS does.
   - Reconcile B132, and anything resting on its m = 1 figures, with GENESIS.

## Not claimed

- No value, sign, bound or verdict of P-585's or P-638's targets or of η_B.
- No comparison with data, no scale ratio, and no coupling value at any level.
- No knot invariant evaluated. Main's N = 5 values are not reproduced.
- No claim that any of the three readings carries the scale, or that the open-book closing is distinguished over
  B287's.
- The cited lemmas and the volume bound are named, not re-derived.

## Disclosures

- **O7's crossing count is by construction:** the braid word has two letters. O2's dual-curve test is a constant. The
  unknot step is the 2-crossing diagram, stated rather than computed.
- **O8 rests on SnapPy's simplified presentation and homology** for the filled manifold. It checks classical facts and
  does not compute the open book's closing slope.
- **The sources were read in their text:**
  - Baldwin arXiv:0804.3624: the introduction, § 2 including Lemma 2.1, the passage around Remark 3.2, and the passage
    on h² = (xy)⁶ and −1/d surgery;
  - arXiv:math/0607370: § 1, which calls the GOF fact "well known" and cites no source for it, and § 2, with the
    open-book list;
  - for f823dd25f, Witten § 2.6.1 and DGLZ (1.5);
  - B287, B132, B204, B613, B1263, B1294, B1341 and B1634, through the mask.

**Refereed read-only:** READY WITH CORRECTIONS (7 errors and 15 suggestions); the errors and suggestions S1–S14 are
applied (S15, a record-side naming nit, is left to main).

## Harvestable rows (the 8-cell format; # and disposition are main's)

| # | seat | item | the seat's own headline (verbatim) | path @ pin | disposition | main arc | date |
|---|---|---|---|---|---|---|---|
| — | web seat (chat1) | THE KNOT READING'S S³ IS THE OBJECT'S OPEN-BOOK CLOSING (a follow-up to f823dd25f; the owner's "Attack the chiral premise"; data-free) | "The object's two-tick word LR, read letter by letter as Dehn twists with the boundary fixed, is an open book of S³ whose binding is the figure-eight knot. In either orientation L and R are twists of opposite handedness about dual curves (B287 records the monodromy as t_α t_β⁻¹), and Baldwin names (Σ, xy⁻¹)'s binding the figure eight; his Lemma 2.1 makes that open book the double cover of S³ branched along the closed braid σ₁σ₂⁻¹, an unknot. So the knot reading's S³ is not brought in from outside: it is the closing that fills the binding, the meridian filling that B287's table lists as S³. B287's distinguished closing is the other standard one, the fiber slope, which caps the page and gives the Sol torus bundle of A. So, of the object's own topological readings, the premise becomes which carries the scale: the binding in its open book (one factor, Witten's (2.30)), the unclosed bundle (two factors), or B287's capped closing, a Sol manifold whose representations all have volume zero; f823dd25f's (i-b), P-725's two sectors, is not a closing and stands. Among positive words with both letters only LR closes this way to a homology sphere; the excursion members' open books have H₁ ≠ 0, where Witten's S³ step does not apply. Nothing is evaluated" | `relays/CHAT1_TO_CC_2026-11-06_THE_KNOT_READINGS_S3_IS_THE_OBJECTS_OPEN_BOOK.md` @ the commit adding it | — | B287, B1634, B132, B204, B613, B1294, P-723, P-726, P-725 | 2026-11-06 |

0 of 19.
