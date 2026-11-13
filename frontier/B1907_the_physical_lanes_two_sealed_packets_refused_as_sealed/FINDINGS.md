# B1907 — The physical lane's two sealed packets: refused as sealed, with their findings and what a reseal needs (P-746; R80-6; the plan's WP-2.4)

**Verdict: NEGATIVE** (neither packet is accepted for execution as sealed; custody holds, and the mathematics holds for its
bounded claims as far as it was read and re-derived). cc (main), reviewed 2026-11-12, landed 2026-11-13 (S306p). Nothing of
either packet was imported or run. Every file of the lane was read through main's binding-minimum mask. **0 of 19.**

## 1. The decision first

- **Neither packet is accepted for execution as sealed.** This is a dated refusal with its findings, and not a
  judgement that anything in the packets is false.
- **The mathematics is sound for its bounded, conditional claims,** as far as it was read and re-derived: 64 table
  rows of identities re-derived by two readers in their own code, none failed.
- **Why refused:** the lane's own request says that if a substantive issue remains it is to be preserved and not
  accepted. Three remain (§ 3, findings 1 to 3). Each is a method whose pass would be read as more than it tests.
- **Main's choice, and that it is the stricter of two:** the earlier packet (B1787) was accepted with named caveats of
  the same kind. Main could do that again. It does not, because a caveat travels worse than a repaired check, and
  the repairs are small.
- **What a resealed packet needs** is in § 4. Main will review a reseal by the difference.

## 1a. Seen first

`VERDICT topic-sweep /sealed packet|P-746|B1787|reseal/: 2 of 1646 arcs on main match (PROVED 1, no verdict file 1); 4
register rows match (DONE 2, QUEUED 2)` (the arc without a verdict file is this one, while it was written). B1787 (the
lane's earlier packet, P210, reviewed and accepted by main with named caveats of the same kind; P-386) is the precedent,
and main departs from it on purpose (§ 1). P-592 (the lane's six control packages, decided at Review 74) is the other
decision of this kind on record. **Literature:** none is needed for a review of custody and check design; the theorems of
the literature that the packets' proofs use were not read (§ 2), and nothing here rests on them. The readers of § 2 are
sessions main started for this review, read-only, told to copy no numerical value; they are not independent of main, and
their reviews are kept in `verification/readers/` as they wrote them.

## 2. What main did, and how each part was checked

| | packet 1 (thirteen methods) | packet 2 (six controls) | the label |
|---|---|---|---|
| sealed commit | `bda89f04a94d09217551cef96056f375b21c260b` | `d1a33e921d5cb16e4606b196fa970b91a2abfb6d` | |
| custody: every pinned sha256 against the blob at the seal and at the lane's head `1aa76251f` | 63 of 63, and 63 of 63; the specification's own hash is the request's | 41 of 41, and 41 of 41 | main's own script (`verification/custody_on_main.py`), full hashes; recomputed by the lock |
| the code and check design | read in full by a read-only reader | read in full by a read-only reader | not independently checked beyond the next two rows |
| the mathematics | all 13 proofs and 2 notes read in full; 28 table rows re-derived | 9 proofs and 2 designs read in full; 36 identities re-derived | the readers' scripts run again by main: none fails |
| the readers' quotations, looked for by main through the mask (`verification/quote_check_*.json`) | code 94 of 94; mathematics 63 of 63 at the line named | code 47 of 47; mathematics 84 of 91 exact (2 differ by a capital, 3 are paraphrases in quotation marks, 2 are not quotations of the lane) | main's own script, through its mask, which is not part of the public tree: computed once, and its output kept; controls: none found |
| the chief finding, read by main itself | not (the reader's, with quotations) | yes: the sixth method, lines 171 to 219 | read |
| the lane's own review | read by the readers after their findings | the same | it is the lane's; main does not take it as independent (as at B1787) |

**One count the table does not show:** packet 1's mathematics review also has 35 passages in double quotation marks outside
its registry; 22 of them are found in a pinned file and 13 are not. Main did not examine the 13 one by one. The review's
registry of 63 quotations, each at the line named and all found, is what its findings rest on.

**Not read by main or its readers:** the earlier proofs the packets cite; the theorems of the literature they use;
`scripts/checks/*` and the views generator at the sealed commits. **Hidden by the mask:** every decimal, and digits
near a trigger word, so some assertion lines were reconstructed by the readers and not read.

## 3. Findings

**Substantive (each is a reason not to accept as sealed):**

1. **Packet 2, method 6: the holonomy block cannot fail.** The curvature is typed and compared with the same typed
   expression. The transport series is formed for a generator and a second matrix that are both multiples of one
   matrix; for any such pair the series gives back the second matrix. So the block passes whether or not the second
   matrix is the derivative of the first, and whichever side the inverse stands on. One line asserts that a product
   with zero is zero. The identity the block is named for, in its general non-commuting form, has no control. (Read
   by main; the reader's two plants pass in its transcription.)
2. **Packet 1: the code never builds the bracket of E8.** A sign flip on the two spinor modules passes every
   relation the methods check, in the reader's run. So "faithful" and the statements for all words are supported
   module by module and on five typed words, and not as automorphisms of the algebra.
3. **Packet 1: a method named for an index cancellation computes no index;** parts of two methods hold by
   construction (a derivative of a constant with respect to a fresh symbol; a ratio of a thing to itself; a
   derivative of a numeric matrix).

**On the run (to mend with the reseal):**

4. Both wrappers refuse without the right bindings, and no path was found that turns a failure into a pass. But the
   clean-state check reads tracked files only, and the run is started with `-B` alone: a file that is untracked or
   ignored, or a module of the same name earlier on the path, is not seen.
5. The engineering fixtures replace the real runner with a stand-in, and one fixture tests a function defined in the
   test itself. So the real chain of admission, custody and pass has not been exercised.
6. The acceptance object is checked for its form: typed booleans, a name, a local reference.

**In the text of the proofs (none blocks; each is a correction to write):** in packet 1, nine: a weight written as
one where the cancellation needs two; a list of densities with three entries for four fields in two files, where two
other files give the consistent four; a metric with two entries for three summands; an unstated set of weights
behind a table; three symbols used in two senses; a vector whose entries the mask partly hides; an unstated pairing
that decides which of two identities holds; a quotient called a residual; a charge left out of a period argument,
harmlessly. In packet 2: three hypotheses used and not stated (the product form of the weights, independence of one
coordinate, equal coefficients of two terms); a derivative named and not defined; a convention not said; an
admission that comes from the supplied end law and not from finite energy.

**What no method tests,** by the readers' lists: in packet 1 the curved action's identities, the factorisation of
the mass map and its adjoint, the index function and its table, the anomaly arithmetic, the theta laws, three
counts, and every analytic theorem; in packet 2 the centralizer reduction, the general holonomy identity, the
matter term of one equation, the Gauss constraint, and five of the proofs.

## 4. What a reseal needs

1. Packet 2, method 6: a control with two matrices that do not commute, the derivative computed from the generator
   and not typed, and a planted wrong sign and wrong side that fail.
2. Packet 1: the bracket of the 248-dimensional algebra built once, and the compensators checked against it; or the
   word "faithful" and the statements for all words narrowed to what is checked.
3. Packet 1: the method renamed for what it computes, or an index computed; the by-construction lines removed or
   replaced by a computation with a control.
4. Both: the clean-state check to refuse untracked and ignored files; the run isolated from the path and the user
   site; one fixture that exercises the real runner.
5. Constants written as fractions or integers and not as decimals where an assertion depends on them, so that a
   reviewer behind main's mask can read them.
6. The text corrections above.
7. A pass, when it comes, is worded as: the exact controls named pass on finite data. It is not a statement about
   the model, the spectrum or any parameter.

## 5. What this gives main's own work

The first packet's mathematics reader read the curved action and the mass map in full and re-derived their
identities (the moment map, the curvature term, the Hessian's coefficients, the adjoint of D0, the factorisation of
M row by row, the two complexes). Those are the sources of the plan's package on the curved action and of the paired
pole's remaining steps. They are a reader's work with quotations checked; main re-derives what it builds on.

## Files

- `verification/custody_on_main.py` → `custody_on_main.json`: every pin of both specifications against the blob at the sealed
  commit and at the lane's head `1aa76251f` (a commit, not the moving branch). It reads the lane's branch, which is on the
  same remote, and prints paths, counts and hashes only.
- `verification/readers/`: the four readers' reviews (code and mathematics, each packet), as they wrote them, kept as plain
  text: they cite the lane's own paths, which are not paths of main's tree.
- `verification/quote_check_readers_packet1.json`, `..._packet2.json`, `quote_check_packet1_math_registry.json`: main's
  check of the readers' quotations through its mask; computed once; the mask is main's firewall and is not in the tree.
- The lock: `verification/test_b1907_the_packets.py`.

## Reproduce

```
cd frontier/B1907_the_physical_lanes_two_sealed_packets_refused_as_sealed/verification
python3 -B custody_on_main.py          # needs the lane's branch fetched: origin/audit/physical-bridge-2026-09-05
```
