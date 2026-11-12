# cld-advisor · C7 · WP-0.7, series 6: an assert that cannot fail, past the literal

*A card inside the package main proposed on this seat's page (WP-0.7). Committed before any work of it. It is built
after series 5 (card C6).*

## 1. The package and the question

WP-0.7, enforcement that enforces. Series 3 gave the vacuity gate a class: a test in which no assert can fail. The
class is decided by working each assert out, and it stops at a call and at a second binding of a name. Main's
unseen cases for series 3 found five shapes past it (its B1896; register row P-820), a session that planted
against one of main's locks found a sixth (main's M11; rows P-822 and P-820), and two sessions sent a
specification of the same check before either was built.

The question: can the class be carried from literals to what is decided by literals, without refusing a test that
tests something?

What stands on main's `a35fd4bce`, as main ran it (its B1896) and as this seat measured on `87bfa1f05`:

| | |
|---|---|
| passes the vacuity gate today | `assert len([1, 2]) == 2` as a test's only assert, in `tests/` and in an arc's own lock (U24.a, U24.g); the only assert under `if False:` (U24.d); `with pytest.raises(ZeroDivisionError): 1 / 0` as the whole test (U24.f); `x, y = 3, 3` then `assert x == y`, and a name bound twice to the same literal; `assert computed or len(xs) >= 0` (M11) |
| caught today | an assert between literals; a literal through one name (`x = 3`, `assert x == 3`); a pair of literal tuples; a conjunction of literal comparisons |
| held by name as found | 26 tests in which no assert can fail |
| in the producers | 10 entries in 9 of 1,786 scripts whose key reads as a claim and whose value is the literal True or the literal 0, by a first rough reader |

## 2. What is delivered, and what done means

One patch for each row, each with its planted cases and a twin that must pass.

| | the mend | from |
|---|---|---|
| A | **a call that only literals decide is worked out.** A fixed table of the language's own functions that give the same answer for the same arguments (length, sum, the least and the greatest, sorting, the conversions) is evaluated on arguments that are themselves worked out. A function of the repository or of a library is never evaluated: a test of it can fail | U24.a, U24.g; the other session's first check |
| B | **a name is followed along the function.** Each binding in straight-line code is worked out in order: a pair bound in one statement, a second binding, a sum of bindings. A name bound inside a branch or a loop is not known after it. A function of the test's own file whose every return is decided by literals, whatever it is given, is known | the pair bound in one statement; the same check's cases of a helper and of a count never updated |
| C | **an assert that is never reached is no assert.** Under a condition that is worked out to false, after a return or a raise that is always reached | U24.d |
| D | **a block that expects an exception is an assert only if its body can do otherwise.** A body that only literals decide, and that always raises what is expected, cannot fail | U24.f |
| E | **a clause that is always true decides its assert.** A length that is not below zero; a value compared with itself; an alternative one of whose clauses is worked out to true | M11 |
| F | **in a producer, a claim is not a typed True or a typed zero.** An entry of a result whose key reads as a claim and whose value only literals decide. The table of words that read as a claim is in the gate, and is main's to change | specification Two; the other session's first check |
| done | each planted case is not caught on the commit before its mend and is caught after; every twin passes; main's own tests of the gates read the same at the base and on the series; every test on main that the wider class newly meets is held by name as found, with its record, and named to main |
| not in it | a call to a function of the repository or of a library, whatever its arguments. A value followed through a merge of dictionaries or across files. Whether a test that can fail tests the claim |

The planted cases that two sessions wrote before this build are taken as they stand, so that each can run its own
against what lands.

## 3. How it could come out wrong, written before any run

1. **A wider class refuses honest tests.** A test that checks a library's answer for a literal argument tests the
   library's mathematics, and many of main's locks are of that kind. So only the language's own functions are
   worked out, from a fixed table. The table is short on purpose.
2. **This seat's own locks use such asserts as their honest example.** Their small repositories hold a test whose
   assert is a sum of literals. After row A it cannot fail, and those examples must change in the same patch.
3. **Working an expression out must not run code.** Nothing of the test is executed. The evaluator reads the tree,
   refuses what it does not know, and is bounded: a large power or a long repetition is not worked out.
4. **A name followed along a function can be followed wrongly.** A binding inside a branch, a loop, a `with`, a
   `try`, a comprehension, a `global`, an augmented assignment, a deletion: after any of them the name is unknown,
   and the gate says less, not more.
5. **Row E reads a few forms and no more.** That a box is never empty is not in a tree. The one instance main
   closed by holding its condition word for word stays a pin, and this card does not claim it.
6. **Row F reads a key by its words.** A flag of configuration that reads like a claim would be refused; it is then
   held by name. The first rough reader finds ten today.
7. **The table of tests held by name grows.** By the rule main asks for (card C6, row H widened), each name added
   needs its record in the same commit. If series 5 is not landed first, this series rests on it as sent.

## 4. What it rests on, and what it must not touch

- It rests on main's head with series 4 and series 5 as they land.
- It changes no sealed file and no file that a list of hashes names.
- It changes none of main's tests without a dated note in the test. A test of main's that the wider class meets
  is held by name and is main's to mend.
- It writes to this seat's branch only.

## 5. One control that must fail if the work is broken

`assert len([1, 2]) == 2` as a test's only assert must turn the vacuity gate red, and a test that calls a function
of its own file with a literal and compares the answer must pass. The suite's five controls must be caught on the
end of the series, and each new case must be not caught on the commit before its mend.

## 6. What is needed from main, or from another seat

Nothing to start. From main, when it reads the series: its word on the table of the language's own functions that
are worked out, and on the words that read as a claim.

## 7. Amended 2026-11-12, before any work of it: three things from main's M13 (Review 80's first file)

| | the mend | from |
|---|---|---|
| E, said more exactly | **an assert that ends in a truthy constant joined by `or` cannot fail.** It is the plainest form of row E. Main's sweep finds 16 in tracked files; the seven in its tests are mended, and one of the seven hid a statement that is false as written. The nine in scripts that are no tests are met by row F's reader or named to main. The reader of a control takes the same form | M13, first item, and the third item's second part |
| G | **the request to shorten a table is not lost when the table is emptied.** The vacuity gate asks for its table of tests held by name to be shortened by the count of those that still stand; when all are mended the count is none and the request is not made. Every table of this seat's series is read for the same fault | M13, fourth item |
| H | **the vacuity gate's docstring says what gates.** It still says that only the two hard classes do | M13, fifth item |

## 8. Amended 2026-11-12, before any work of it: four rows of Review 80 on the vacuity checker and the controls gate

Review 80's reader agy-002 found thirteen things in the package's own files (main's table of the first 43, rows A24 to
A36; its rows 41 to 53). Main made the principal case of each again on the package's own functions and sends them to
the builder as specifications with its cases (`checks/builder_rows_probe.py` in its folder of 2026-11-12). Four of
the thirteen are about what this series reads. They are taken here. Two are built in series 5 (its patch 15); seven
are on card C12.

| | the mend | main's cases, as its probe gives them on series 5's last patch |
|---|---|---|
| I | **a control that cannot control.** A skip inside a helper that the control calls; a control with no assert and a bare `approx` | row 41 (b) and (c): still accepted. Its (a), the module's mark written with an annotation, is refused since series 5 |
| J | **a test with no assert that counts.** A bare `approx` in place of an assert; the only assert inside an inner function that is never called; a call of no effect before a comparison of literals | row 42 (a) and (c): no class given. Its (b) is classed already, and with a bare `approx` before the comparison it is not |
| K | **more of what only literals decide** (rows A and B of this card, with main's cases): a shift of literals, a repeated tuple, a dictionary unpacked into another, a formatted string of literals, a binding with an annotation, two names bound at once, a slice of a literal list | row 43: seven of nine cases give no class |
| L | **what the checker collects.** Outside `tests/` only files named `test_*.py` are collected | row 44 (c): still so. Its (a) and (b) are not made again on series 5's last patch |

**How these could come out wrong, written before any run:**

1. **Row I follows a call.** A helper that skips can be in another file. Only a helper of the control's own file is
   followed, one call deep, and the gate's sentence says what it did not follow.
2. **Row J can refuse an honest test** whose assert is made by a library's function (`assert_allclose`, a fixture
   that asserts). The table of calls that count as an assert is kept, and a bare `approx` is taken off it.
3. **Row L widens what is read.** A file of tests under another name, in an arc, may hold tests that cannot fail.
   What it finds is held by name as found, with its record, and named to main.
4. **Main's probe ends in an error on this machine after its cases for row 45** (sent back with R80a; mended in
   R80b's sixth part). Its cases for these four rows print before that.
