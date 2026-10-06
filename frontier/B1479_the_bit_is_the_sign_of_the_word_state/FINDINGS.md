# B1479 — THE BIT IS THE SIGN OF THE WORD STATE: on all 379 primitive words to length 12 the two signs share a volume and differ by half a longitude at the cusp, and on all 34 amphichiral words the + state is rectangular at CS = 0 and the − state rhombic at ¼ — where no spin structure survives the mirror

**Verdict: PROVED** — every sealed prediction holds with no exception, on the range sealed (reach: class — the primitive
word states to length 12, GENESIS §3's X_gen, named as that set). A census law with a named mechanism; the half-shift is
not proved on this page and the law is conjectural beyond length 12. cc (main), 2026-10-06/07. Sealed `646cc2b7d`
(sha256 ba56ca22). L246; frame F-CI. No physical quantity. **0 of 19.**

## 0. Seen first, and literature

As sealed: `VERDICT topic-sweep /cusp shape|rhombic|rectangular cusp|shear/: 60 of 1348 arcs on main match (NEGATIVE 9, OPEN 6,
PROVED 45)` — none relates the sign of a word state to the cusp's type; B1459 uses the fibre's elliptic involution on
levels, B1226 lists amphichiral members at ¼, neither states the sign as the bit. Seen before the seal and disclosed
there: the 16 amphichiral states to length 8 (B1478's census), the two controls, the web seat's listening log. **Lengths
9–12 were not opened.** **Literature:** the layered-triangulation description of these bundles (Guéritaud) is cited from
memory and unread; no cell rests on it — the shapes of both signs are computed for every word.

## 1. Results (`verification/sign_law.py` → `sign_law.json`; 758 states, all hyperbolic, no errors)

| | sealed prediction | prior | result |
|---|---|---|---|
| **P2** | the half-shift: for every word, Im z(−w) = Im z(+w), Re z(−w) − Re z(+w) ∈ ½ + ℤ, volumes equal | 95% | **HOLDS, 379 of 379** |
| **P1** | on every word with an amphichiral state: both signs amphichiral; + rectangular at CS = 0; − rhombic at CS = ¼ | 93% | **HOLDS, 34 of 34** — 1, 1, 2, 4, 9, 17 words at lengths 2, 4, 6, 8, 10, 12; the 26 at lengths 10 and 12 unopened before the seal |
| **P3** | on every amphichiral − state the longitude's trace is −2 on every lift | 85% | **HOLDS, 34 of 34** (152 spin structures) |

**So, on the word states to length 12:** a word is amphichiral with both signs or with neither; with the sign + its
mirror is rectangular, its Chern–Simons class is 0, and nothing at the cusp forbids a mirror-symmetric spin structure;
with the sign − its mirror is rhombic, its class is ¼, and by B1477's Theorem A **no spin structure is fixed by any
mirror** — a proof on each of the 34, whose inputs are an integer matrix and signs.

**The mechanism, named and not proved here.** −A is A composed with the fibre's elliptic involution, which turns the
puncture's boundary circle by π: the same tetrahedra, the cusp's closing-up shifted by half the longitude. Rectangular
becomes rhombic. P2 is that statement, measured on every word.

## 2. What it says in the genesis' terms — stated, not banked as physics

GENESIS generates words; the sign is carried as an **extension** of the grammar (FK4, inverse moves, OPEN; FK6,
positivity, CHOSEN). This arc finds that the sign is exactly the bit B1474–B1477 located: on a + state the mirror can
fix a spin structure, on a − state it cannot. **The place where a hand can be registered on a fermion without a
continuous choice is the part of the state space the genesis does not yet generate.** Whether the sign is forced,
chosen or generated is FK4/FK6's question and now has a consequence attached to it. Nothing here selects a hand: the
two signs of an amphichiral word are both there, and the − state is still its own mirror image as a manifold.

Under the owner's rule (the family is the object) and the web seat's A3 (name the set): this is a statement about
X_gen to length 12. B1186's 112 and the census at large are B1477's range, where the law is "¼ ⟺ rhombic".

## 3. The web seat's four relays since its pin — re-run and rowed (head `df6dfec51`)

| relay | states | on main's bench |
|---|---|---|
| NONORIENTABLE INDEX | a twisted class index I_w(V) = n(V) − n(V*⊗w) on non-orientable N; the register lemma I(M; p*V) = I_w(N; V) + I_w(N; V⊗w), 264 of 264; every count vanishes on m000 and N3 over F₁₃ | output identical to the seat's log; seal e88cac0f verifies |
| LISTENING LOG | three metallic acts, ten ticks, native invariants only; E1–E4 pass after an instrument fault its own expectations caught | reproduced: identical except twelve lines printing the class 0 as 0.0 against 0.5; seal 5b5e70c6 verifies |
| SEEN-FIRST, RETROACTIVE | the log "largely re-found the July breath campaigns" (B469, B470, B479, B596, B701, B732); four candidates not found in the record | taken as written; the July arcs are not credited to the seat, by its own word |
| FIRING DESCENT | s961's 72 firing modules do not descend to m025: the deck fixes none and pairs them with equal index; the firing is ℤ/4 data of the orientable tick | output identical to the seat's log; sealed by commit order (no hash file) |

**Its open cells, answered as far as the data goes.** *Every orientable tick is amphichiral at CS = 0:* an orientable
tick is an orientation double cover, its deck is a free mirror, a free action on a torus is a glide, a glide needs a
rectangular lattice, and rectangular means 0 by B1477's census law — and here by P1, since the orientable ticks are +
states. *|Sym| = 2k at odd ticks, 4k at even:* reproduced for all three acts (2, 8, 6, 16, 10, 24, 14, 32, 18, 40);
unexplained here. *The 2T door's counts:* each is 24 × (the number of 2T-quotients) since |Aut(2T)| = 24 — 48, 96, 192,
240, 768 are 2, 4, 8, 10, 32 quotients; the change points are the seat's (the clocks at 2 and 3), the numbers stay open.
The seat's sealed, unrun question (the first level with a background, across the acts) is its own to run.

## 4. Disclosed

P1 is post-hoc at lengths ≤ 8 (8 of the 34 words) and a test at lengths 10 and 12 (26). The instrument reuses B1477's
`cusp_shear.py` and `range_census.py` unchanged. Numerical except the integer cusp maps and the trace signs. The
half-shift is measured, not proved. The reading of §2 is a reading.
