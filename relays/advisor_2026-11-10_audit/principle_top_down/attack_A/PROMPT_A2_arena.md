# Prompt A2 — a formal statement inside a given arena (the target hidden)

You are taking part in a blind exercise. Below are statements of a philosophical principle in its author's own
words, and a small mathematical arena. Your task is to turn the principle into mathematics inside that arena:
definitions and consequences, not commentary.

Rules of the exercise:
- Work from the words and the arena alone. Do NOT read, list or search any file in your working directory or
  anywhere else, and do not use the web: reading anything would spoil the blindness and invalidate your answer.
- You MAY run short Python computations for arithmetic (integer matrices, enumeration of short words). Keep any
  scratch file under {SCRATCH}.
- Be concrete. Where the words do not decide something, decide it, and say that you did.
- At most about 1100 words.

**The arena.** A pair of integer counts (a, b). Two elementary updates: L sends (a, b) to (a + b, b), and R sends
(a, b) to (a, a + b); as matrices on column vectors, L = [[1,1],[0,1]] and R = [[1,0],[1,1]]. A history is a finite
word in L and R, and it may be repeated periodically. Whether the inverse updates, the exchange of the two counts,
or negative counts are allowed is for you to decide from the words.

Answer these, in this order, under these headings:

1. **Definitions in the arena.** Precisely: what a distinction is here; cancellation (give every sense you find the
   words support); what it means for a history to exist; what "interaction" means here and why a single update
   alone is not enough.
2. **What exists first.** Under your definitions, which history is the first thing that exists? Then the second and
   the third. Give the words and their matrices, and say what criterion ordered them.
3. **Order and mirror.** Is the history "L then R" different from "R then L" under your definitions? Is the
   exchange of the two counts an allowed act, and what follows from allowing or refusing it?
4. **Depart further.** Take your first existent as the ground. Give a precise rule for what exists next *relative to
   that ground* — "the difference between distinctions gets selected to depart further" — and compute the first few
   things your rule selects. State whether your rule is a minimum under an ordering or persistence with no ordering.
5. **What is forbidden.** Histories or structures that cannot exist under your formalisation.
6. **Choices.** Every choice you made that the words and the arena did not force, each with the alternative you
   rejected.

{WORDS}

Write your complete answer to the file {OUT} (create it; plain Markdown) and also return the same text as your final
message.
