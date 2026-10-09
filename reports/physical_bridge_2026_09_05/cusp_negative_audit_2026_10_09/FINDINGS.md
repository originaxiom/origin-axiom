# B1629 audit: computation preserved, finite equality corrected

October 9, 2026. Research audit of main87d769c7a, sealed and pushed at
4fcee76ab706a065c7d4b16dc29d0ac48ece64ac before execution. The full
corrected upstream producer reproduced unchanged. All 170 exact finite
fractions agree between two different methods; its complete P2 finite
height profile is independently recovered. Seven focused tests pass.

This verifies the corrected computation and narrows how broadly it was
written. No physical cusp source or chiral spectrum is derived here.

## Results preserved

- The unchanged post_seal_cusp.py run reproduces the entire saved JSON.
  Its original disclosed repair remains part of the record.
- A rooted-word enumeration and a separate Mobius-inversion calculation
  agree exactly for n=2..18 and every k=1..n: 170 fractions. All 35
  published P4 decimals are recovered at their stated precision.
- Integer matrix products and rational squared radii recover the census
  of 2536 primitive necklaces through length14, its unique minimizing
  word LR, minimum squared height5/4, second squared height2, maximum,
  and both published L^k R and L^k R^k profiles.
- The tail tends to (k+1)/2^k at fixed k in this symbolic ensemble. The
  decay and absence of mass at an infinite run survive. An explicit
  conditioning bound proves the convergence without fitting.

The height check verifies the author's rotation-based statistic. It does
not prove all-length uniqueness or compute a maximum over every modular
conjugate. This limit on the census does not refute the classical result.

## Correction to the finite equality

The headline, P4 summary, claim and kill row say (k+1)/2^k holds at every
length. Their ensemble is conditioned on primitiveness, and that exact
equality fails. For n=10,k=2 the probability is

    124/165 = 0.751515... != 3/4.

The producer already gives the correct decimal. The defect is in the
reporting. The exact finite law is

    A_n = sum_{d|n} mu(d) 2^(n/d)
    p_n(k) = sum_{d|n} mu(d) E_(n/d)(k) / A_n
    E_m(k) = 2                    for m<=k
             (k+1) 2^(m-k)        for m>k.

PROOF.md derives the law, including subtraction of constant words.
Conditioning changes the probability by at most the excluded-word
probability, bounded above by n*2^(-n/2). The valid replacement is a
finite formula and a limit; the limiting positive should be retained.

## Scope of the dynamical inference

The assertion that the required unit of end data is therefore not
dynamical is not established by this instrument. Its measured objects
are words, radii and letter-run occupancy. No equation for that end datum
is tested.

A concrete control shows why a zero atom alone is insufficient. In the
fair Bernoulli symbolic process the occupancy tail decays, while arbitrarily
long runs occur almost surely. Avoiding an all-L block in N disjoint
k-blocks has probability (1-2^(-k))^N. Main itself retains that the wider
weave reaches arbitrarily high; that positive also survives this audit.

Letter time also differs from arclength: LLLR and LLRR both have four
letters, but traces5 and6 and different hyperbolic translation lengths.
The author already discloses the proxy. Applying a geometric measure
theorem requires the ensemble and time conversion to be exhibited. This
audit does not compute a replacement physical measure.

Even a bounded selected orbit needs a further implication before it
excludes dynamical boundary response, topological end constraints or
field equations in an admitted model. Neither the tested words nor this
audit supplies that physical map. This limits an inference; it does not
establish a successful mechanism. The selected tick's bounded behavior
is preserved.

## Computation integrity

The upstream test checks saved JSON, source integrity and adoption prose.
It does not replay the producer. This audit replayed the corrected
producer in an isolated extraction and checked it with two different
algorithms. Neither new algorithm uses a saved pass flag to establish
the fractions.

Opposing controls reject the exact finite-limit equality, periodic and
constant words, and full-length runs in a primitive population. Positive
controls recover the unconditioned formula, tiny populations, cyclic
wrap, rotation-invariant heights and the correct height minimum.
No failed audit run occurred.

The new implementations share an author. They do not constitute outside
analytic review. The different-author upstream computation was replayed.
REPLAY_RUN.log, NATIVE_RUN.log, REFERENCE_RUN.log and FOCUSED_RUN.log hold
literal stdout; RECEIPTS.json records exits, timing and digests. Sources
are pinned in INPUTS.json and science files in PRESEAL.json. Eight native
predicates, six reference predicates and seven tests pass. No broader
regression or full-suite certificate is claimed for this audit.

Preseal governance: 26 PASS, four inherited FAIL categories, exit1.
The checkpoint has not received main-bank or outside analytic acceptance.

## Consequence for the physics campaign

A dynamical source route remains undecided by this statistic. Require
the actual map from generated structure to one action, its stationary
end law, physical fermion domain and charged spectrum/anomalies.

The next silver test remains the variation of one real superfield action
and its integrated parallel-gauge normal response. B1629's modular-surface
statistic does not decide that operator problem. W47's flat-twist/domain
classification and W48's conditional dressing are separate audit targets.
The parameter-free SM/TOE mission remains active and unachieved.
