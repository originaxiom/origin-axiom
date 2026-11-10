# Prompt A3 — the adversary (same arena; the brief is to make something else win)

You are taking part in an adversarial exercise. Below are statements of a philosophical principle in its author's
own words, and a small mathematical arena. Another reader has formalised the principle so that the first thing that
exists is the alternating history LR (or its mirror RL), and the next thing that exists is that same alternating
history with one run of a single letter lengthened.

**Your brief:** produce a formalisation that a fair reader would accept as at least as faithful to the words, under
which something else wins — a different first existent, or a different second step. Then argue, honestly, how
faithful your reading is compared with the other one, and say where your reading strains the words if it does.

Rules of the exercise:
- Work from the words and the arena alone. Do NOT read, list or search any file in your working directory or
  anywhere else, and do not use the web.
- You MAY run short Python computations for arithmetic. Keep any scratch file under {SCRATCH}.
- At most about 1100 words.

**The arena.** A pair of integer counts (a, b). Two elementary updates: L sends (a, b) to (a + b, b), and R sends
(a, b) to (a, a + b); as matrices on column vectors, L = [[1,1],[0,1]] and R = [[1,0],[1,1]]. A history is a finite
word in L and R, and it may be repeated periodically. Whether the inverse updates, the exchange of the two counts,
or negative counts are allowed is for you to decide from the words.

Answer under these headings:

1. **Definitions in the arena** (distinction, cancellation, existing, interaction).
2. **What exists first, second, third** under your reading, with words and matrices.
3. **Order and mirror.**
4. **Depart further:** your rule for what exists next relative to a ground, and the first few things it selects.
5. **Faithfulness:** which phrases of the words your reading honours better than the other reader's, and which it
   strains.
6. **Choices** you made that the words did not force.

{WORDS}

Write your complete answer to the file {OUT} (create it; plain Markdown) and also return the same text as your final
message.
