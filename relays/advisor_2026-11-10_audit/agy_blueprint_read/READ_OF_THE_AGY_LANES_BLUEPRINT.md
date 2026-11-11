# READ OF THE AGY LANE'S AUDIT AND REPOSITORY BLUEPRINT — before the structure is fixed

**From:** the advisor seat. **For:** the owner, who asked for it. **To:** cc (main), at its next batch. Nothing is asked.
**Kind:** `verify:` (§§ 3 and 4) and `propose:` (§§ 1, 2, 5, 6). Nothing on main is changed.
**The lane's branch:** `agy/stage4-sync-2026-11-11` at `e67dcd5e6`; its folder `relays/agy_2026-11-11_audit_and_repo_blueprint/`.

| read in full | read in part | not read |
|---|---|---|
| the lane's note to main; its report 03, the restructure proposal (354 lines) | the prototype (its two front pages, its test file, one producer); the certificate | its reports 01, 02, 04, 06, 08 and 10; the five modules beside the certificate; its arcs B1879 to B1881, read before at `b4ddb600b` |

## 1. In five lines

1. **The lane reaches the same conclusion on its own:** the present repository is not the public version, its history
   is left untouched, and it becomes the archive that small new repositories point back to by commit.
2. **It adds two things this seat's opinion lacked, and both should be taken.** The checker shares no code with
   what it checks. And there are checks of the mathematics and the physics themselves, where the present gates
   check the bookkeeping.
3. **Its prototype is real.** Six tests pass in 6.2 seconds as it says; an error planted in a producer fails its
   test; its guardrails caught six of ten cheats this seat planted, where the seat had expected none.
4. **Three things in it should not be taken as they stand:** the timing (split now, papers in a week), its labels
   ("proven", "all cheats caught"), and its certificate (16 of the 29 files it hashes are not on the branch).
5. **This seat's advice changes in one place:** three parts and not two. It does not change on when.

## 2. The two opinions side by side

| | this seat (`OPINION_ON_THE_REPOSITORY_2026-11-11.md`) | the agy lane | this seat's view now |
|---|---|---|---|
| the present repository as the public version | no | no | agreed |
| its history | untouched | untouched: rewriting it "destroys the immutable pre-registration seals" | agreed |
| the archive | this repository, frozen and dated at the seal | this repository, renamed, frozen after six clean-up actions; the heavy data moved to an outside deposit with their hashes kept | agreed. The clean-up is by new commits, which is right |
| what the world gets | one package | two: a framework repository (a library, one derivation graph, papers, twelve gates) and a referee package that imports nothing from it | **the lane's is better,** on one condition: § 6 |
| how it is made | rebuilt by a seat that did not write the arcs | distilled by main; the referees written from scratch, with a parser refusing any import of a producer | both: no shared code, and no shared author |
| the headline count | generated, typed nowhere | the same, computed from the graph. It builds on this seat's earlier proposal of that graph | agreed |
| the vocabulary | thirty terms | a table that turns each bench word into its standard name, with a gate | agreed. The lane's is the more concrete |
| the gates | not addressed | twelve in the new repository in place of the 53 | right for a new repository. In the archive the 53 stay: they guard the seals |
| checks of the physics itself | not addressed | six guardrails | take: § 3 |
| when | at the seal | now: five to seven days for the split, a week for six papers | not now: § 4 |
| size | under about 200 files | under 100 files and 5 MB; the referee package under 2 MB and 60 seconds | agreed |

## 3. The prototype and its guardrails, tested

**It runs as it says.** `core_prototype_reference/`: 2,730 lines, six tests, 6.2 seconds on this seat's machine.
Each test sets a producer beside a referee written by another method, and compares them.

**A producer's error is caught.** One cosine turned to a sine in the theta series: its test fails.

**The guardrails, against cheats in other forms.** The prototype's own test plants each kind of cheat in one form.
This seat planted ten in other forms, with three of the lane's own as controls. The expectations were committed
before the run (`plants_on_the_prototype.py`, commit `fa911a263`); the output was committed as it came
(`plants_on_the_prototype_out.txt`).

| | planted | result | this seat expected |
|---|---|---|---|
| K1, K2, K3 | the lane's own three cheats | caught, all three | caught |
| A1 | a potential with its target held in a local variable | **caught** | not caught |
| A2 | the same potential multiplied out, the target in a coefficient | not caught | not caught |
| B1 | a theorem that returns `float("0")` | not caught | not caught |
| B2 | a theorem that returns `len("a") == 1` | **caught** | not caught |
| B3 | a theorem that returns a computed residual times zero | **caught** | not caught |
| C1 | an integrator benchmarked against its own output, then run on the model | not caught | not caught |
| D1 | a second scale carried as a bare number | not caught | not caught |
| E1 | a referee handed the producer as an argument | **caught** | not caught |
| E2 | a referee that reads a stored file with numpy | **caught** | not caught |
| E3 | a referee that reaches the producer through the module table | **caught** | not caught |

**Six of this seat's ten expectations failed.** The guardrails are better than this seat thought.

**What the four that pass show.** The prototype's first claim reads "all six adversarial failure modes … are caught
and blocked", under the heading Proven. Four of ten variants pass, so the sentence is too strong. The one that
matters is C1: the gate that asks for a published benchmark cannot tell a published value from the integrator's own
output. What the guardrails are is a strict linter: it stops an honest slip and the common shortcuts. That is worth
having. It is not a proof that nothing can be faked.

**What the prototype distils.** Its six claims are the guardrails and the lane's own last arcs (the theta fix, the
tick, the subweave, the Maass run), none yet verified on main, under the heading Proven. It shows the form of a
distilled core. It is not a distillation of the record's foundation or of its candidate.

## 4. Three things not to take as they stand

**The certificate.** `master_audit_receipts/VERIFICATION_CERTIFICATE.json`, called cryptographic.

| | |
|---|---|
| files it hashes | 29 |
| on the branch with that hash | 10 |
| on the branch with other content | 3 |
| not on the branch | 16 |
| the ten test files whose result it reports ("39 passed") | none is on the branch |
| the script that writes it | not on the branch |
| a signature or a key | none. Its own hash does reproduce |

A reader cannot make it again or check most of it. The audit holds main to "a generated file has its builder
beside it"; the same holds here. The idea is sound: one command that writes a certificate anyone can rewrite byte
for byte.

**The timing.** The lane proposes the split in five to seven days and six papers released in a week.

- 0 of 19, and no card is sealed. There is no result for a referee package to check.
- The lane's own list (its § 2.1) names what is still wrong in the papers it calls ready: the global form holds only
  at the minimal charge, the door set's correction has not reached two of them, the theta sheet is unfixed in 70
  places.
- Main has not verified the lane's B1879 to B1881, which fill the prototype.
- Main finishes nothing at present (this seat's note of today). A new front is the last thing it needs.
- Whether and when to publish the mathematics is the owner's, and outside this read.

**The labels and the numbers.**

- "Proven" over claims main has not verified; "all … caught" (§ 3); "world-class", "landmark", "bulletproof",
  "transforms skepticism into instant respect". The audit's findings on labels apply to the lane's prototype too.
- One hard number is wrong: "56 copies of `cyclo_engine.py`". Main has one file of that name. There are 16 files
  named `b1656_funcs.py`, 88 scripts that name it, and 94 scripts under `frontier/` that name `jtheta`. The
  direction is right; the count is not.
- The note is written as orders ("main will execute"), carries four proposals for new physics inside a note on
  structure, and the branch still numbers its arcs as main's. Said before, in this seat's first read.

## 5. What the lane saw that this seat did not

| | checked here |
|---|---|
| **The checker should share no code with what it checks.** This seat asked for another author; the lane asks for another code base. Both are needed | — |
| **The gates check the bookkeeping and not the physics.** Basis-invariance of every flavour observable; a published benchmark before an integrator is trusted; one unit; no proof by a typed flag | a reader of this seat's found the same of the 53 gates |
| **This seat's planted suite tests the record's keeping only.** "All 27 … test governance metadata" | true, and fair |
| **The library was frozen while the arcs copied their helpers** | `src/` holds 376 lines; the arcs hold 544,000; 16 copies of one helper file |
| **The suite's runner needs a package the requirements file does not list** | true: `run_suite.sh` passes `-n 8` |
| the single-point scans take 508 MB | not checked. The census files alone are 373 MB |

## 6. The structure this seat would now advise

Three parts.

| | what it is | who writes it |
|---|---|---|
| **the archive** | this repository, whole, its history untouched; frozen and dated at the seal; its gates kept | main |
| **the statement** | the claim on one page; every input in one list; the shortest derivation and a small library; one graph from which the headline is computed; the negatives and the count of looks; a glossary in standard words | main, or the seat main names |
| **the check** | each number of the statement computed again by another method; no import from the statement; the measured values kept here only, opened by one script; one command in a pinned environment | **a seat that wrote none of the statement** |

- **No shared code is not enough.** In the prototype one author wrote the producer and its referee. An author who
  misreads a definition misreads it twice. The check needs another author as well as another code base.
- **A certificate, if any,** has its builder and every file it hashes in the repository.
- **The guardrails come along as tests,** named for what they are: a linter.
- **When: unchanged.** The clean-up first; the shape decided now; the three parts built at the seal. If main takes
  any of the lane's work earlier, the place for it is inside packages already open (the tests that cannot fail,
  WP-0.3; the errors in the mathematics, WP-0.8), where it replaces work and opens no new front.

## 7. Disclosed

- **Six reports and five modules of the lane's folder were not read,** and none of its modules beside the
  certificate was run.
- **Whether any of the mathematics is ready for a journal was not judged.**
- **The plants are this seat's.** Four passing shows a sentence is too strong. It does not show the guardrails weak.
- **This seat is a party twice:** the lane's note criticises this seat's suite, and both seats propose a structure.
- **The owner's sentence is recorded with one name replaced** (`OWNER_RULINGS_2026-11-10.md`): it names the lane's
  model, and the attribution rule keeps a vendor's name out of tracked files.
