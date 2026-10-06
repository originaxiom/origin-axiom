# B1479 — PREREGISTRATION: THE BIT IS THE SIGN OF THE WORD STATE

**Sealed before `sign_law.py` runs on anything but the word LR with its two signs (m004 and m003).** cc (main),
2026-10-06. L246 (what decides the swap), now stated in the genesis' own grammar; after B1477 (the bit is decided at the
cusp) and the web seat's listening log of the same day.

**The question.** GENESIS §3 generates word states: a cyclic word in L, R with a sign. B1474–B1477 located a fermionic
bit — whether any spin structure survives the mirror — on the cusp's lattice (rhombic or rectangular) and on the
Chern–Simons class (¼ or 0). *Is that bit simply the sign of the word?*

## 0. Seen first

- `VERDICT topic-sweep /cusp shape|rhombic|rectangular cusp|shear/: 60 of 1348 arcs on main match (NEGATIVE 9, OPEN 6, PROVED 45)`
  (run for B1477 the same day; B1477 itself is now the 61st): none relates the sign of a word state to the cusp's type.
  B1459 uses the fibre's elliptic involution on levels (the zeros at complete points); B1226 noted "m003/m135/m207 are
  amphichiral with CS = ¼"; B855 that m003 is commensurable with m004. The sign as the bit is stated nowhere I found.
- **Seen in data before this seal, all of it:** (i) B1478's census of the 74 primitive word states to length 8 (run to
  check the web seat's amendment A3): its 16 amphichiral states are 8 words with both signs, **sign + at CS = 0 on 8 of 8,
  sign − at CS = ¼ on 8 of 8**; (ii) the two controls on this instrument: b++LR = m004 (zero, rectangular, shape
  −2 − 0.2887i, volume 2.0298832) and b+-LR = m003 (quarter, rhombic, shape −2.5 − 0.2887i, the same volume, longitude
  trace −2 on both lifts); (iii) the web seat's listening log: the golden act's even ticks are m004, m206, s961, t12839,
  o10_150696 — B1474's FIX members. So lengths 2–8 are post-hoc for P1; **lengths 9–12 are not opened.** The cusp type
  and shape of no state but the two controls has been computed.
- **Literature:** that the layered triangulation of a once-punctured-torus bundle depends on the word and that the sign
  changes only the closing-up by the fibre's elliptic involution is Guéritaud's description, cited from memory and
  unread on this bench. **No cell rests on it** (the owner's rule of 2026-10-06): the shapes are computed for both signs
  of every word and compared.

## 1. Statements

**The half-shift (expected a theorem; tested as P2).** The monodromy −A is A composed with the fibre's elliptic
involution, which rotates the puncture's boundary circle by π. The two bundles have the same tetrahedra; the cusp
torus' closing-up is shifted by half the longitude. So z(−w) = z(+w) + ½ (mod 1) for the cusp shape z = Mu/L relative
to the rational longitude, with equal imaginary part and equal volume.

**The sign law (P1).** On an amphichiral word, the + state's mirror is rectangular and its Chern–Simons class is 0; the
− state's mirror is rhombic and its class is ¼. With B1477's Theorem A and P3 this makes the − state one on which no
spin structure survives any mirror.

## 2. Cells and predictions

`sign_law.py 12`: the 379 primitive cyclic words to length 12 up to the swap, both signs (758 states).

| | prediction | prior |
|---|---|---|
| **P2** | half-shift on every word whose two states are hyperbolic: Im equal, Re differing by ½ mod 1, volumes equal | 95% |
| **P1** | on every word with an amphichiral state: both signs amphichiral; + rectangular at 0; − rhombic at ¼ | 93% (lengths 9–12 are the test) |
| **P3** | on every amphichiral − state the longitude's trace is −2 on every lift | 85% |

**Kills.** P2: one word with a different shift. P1: one amphichiral word off the pattern (in particular a + state at ¼,
a − state at 0, or a word amphichiral with one sign only). P3: one amphichiral − state with a lift of longitude trace +2
— then Theorem A does not cover it and the page says which spin structures are left to the numerical certificates.

**Reading.** All three hold: the bit of B1474–B1477 is the sign of the word state on the word states to length 12 — a
census law with a named mechanism, conjectural beyond length 12 until the half-shift is proved on the page. Then the
consequence for the genesis is stated and NOT banked as physics: the sign is the part of the state space GENESIS marks
as an extension (FK4 open, FK6 chosen); where it is absent no hand can be registered on a fermion.

## 3. Also in this arc (not predictions)

The web seat's four relays since its pin (the non-orientable index, the listening log, its retroactive seen-first, the
firing descent) are re-run in a pinned worktree and rowed; its two open cells (|Sym| = 2k / 4k along a tower; the 2T
door's counts) are computed and reported as data, with whatever explanation the data supports, labelled.

## 4. Disclosed

Instrument at the seal (sha256, first 16): `sign_law.py` 7250216f710f04d0; it reuses B1477's `cusp_shear.py` and `range_census.py`
unchanged. Numerical except the integer cusp maps. The seat's own note that its listening log "largely re-found the July
breath campaigns" is taken as written; nothing of it is credited to this arc.

## 5. Scope

Frame F-CI. Object: the primitive word states to length 12 (X_gen of GENESIS §3, named as that set). Reach class.
No physical quantity is computed. 0 of 19 before and after.
