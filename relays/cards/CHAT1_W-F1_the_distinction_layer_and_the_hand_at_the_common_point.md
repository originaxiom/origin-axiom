# W-F1: the distinction layer under the grammar, and the hand at the common point

*The web seat (chat1), 2026-11-14. At the author's word to this seat on 2026-11-14: the foundations become this
seat's main task, and it computes for itself the checks other seats proposed, rather than relaying them. Not proposed by
main; committed, with its expectations, before anything of it is computed, and sent to main with its result.*

## 1. The question

Two readings were put forward this week, and each can be tested on exact arithmetic.

1. **A layer under the grammar (this seat's reading).** A distinction is an involution, and three independent
   distinctions, ℤ/2 ∗ ℤ/2 ∗ ℤ/2, carry what the grammar now postulates:
   - two records: the even part is free on x = ab, y = bc;
   - the commutator as the square of the product of the three;
   - the quaternion point as the Pauli triple, with [x, y] = −I;
   - the grammar's moves as re-descriptions of the three.

   **The rule for postulates.** A postulate is strengthened when its opposite is *dead*: it collapses to completed
   cancellation (finite, abelian, flat). It is a choice when its opposite is alive. Part A computes the rows of that
   test that exact arithmetic can decide.
2. **"The hand is the arrow"** (a reading another seat put to the author). Reversing the act gives the mirror
   manifold. The proposed test asks that every handed quantity flip exactly when φ becomes φ⁻¹, and stay put under
   everything else. Part B computes three things:
   - the identity behind it;
   - which manifolds of the census are amphichiral (on those, reversing the act is a symmetry);
   - for one handed quantity, the class of the act at the common point among the rotations of order 3 of A₄ ("ζ
     against ζ̄"), what it flips under.

## 2. What will be delivered

`relays/CHAT1_TO_CC_2026-11-14_W-F1_THE_DISTINCTION_LAYER_AND_THE_HAND.md`. It will hold:
- the results;
- where they meet the record's own definitions of the hand (W1, W24 to W29, W34, B1609). These are read through the
  mask only after the output is committed.

## 3. How it is done

`relays/chat1_2026-11-14_wf1/wf1_checks.py`. Its definitions and expectations are in its header. It is sealed (sha256
in `SCRIPT_SHA256.txt`), committed and pushed before its one run. It shares nothing with any other seat's code and reads
nothing of the record.

## 4. How it could come out wrong

- **A census that is not the record's.** The control is the count of 758 states and 536 manifolds.
- **An automorphism that is not the matrix it claims to be.** Every automorphism is checked against its abelianisation,
  with one planted error.
- **A test that cannot fail.** The flip test is also run with the word put in place of its inverse (a planted error),
  and must then report no flips.
- **A reading of "the hand" that differs from the record's.** The note will say so, and what follows from it.

## 5. Firewall

Data-free: exact arithmetic on words, matrices and the finite group 2O. No τ, no frame, nothing measured.

## 6. Needed from main

Nothing. Main is told of the card in this seat's status, and the note is sent to main.
