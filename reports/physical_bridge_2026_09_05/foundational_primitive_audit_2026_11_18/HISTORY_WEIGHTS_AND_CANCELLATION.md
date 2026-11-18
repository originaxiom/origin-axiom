# History composition does not make a history weight a group character

2026-11-18. Author hand continuation under `6941e2b1b`.
Not independently checked. No scientific import, execution, CAS,
enumeration or test. The probabilistic setting below is supplied as
a mathematical control, not derived physical probability or an action.

## 1. Retain what composes

Let A be a finite alphabet of admitted updates T_a on a specified state
space X, with their legal domains. Write h=a_1...a_n chronologically,
and T_h=T_(a_n)...T_(a_1). Concatenation h k means h first, then k.
It follows that T_(h k)=T_k T_h whenever the whole history is legal.

Now additionally supply one-step probabilities p_a(x), nonnegative,
zero for illegal steps, and summing to one at each admitted state.
Assume the conditional next-step law depends only on this complete
x. The Markov assumption and the p_a are explicit extra inputs.

For a legal history define its state after j steps by x_j and put

    W(h;x)=product_(j=1)^n p_(a_j)(x_(j-1)),
    W(empty;x)=1.                                   (1)

Set W(h;x)=0 for an illegal history without evaluating its undefined
later states. Equation (2) is used where its prefix h is legal.

This is forced by the stipulated one-step conditional law, rather than
an independent global choice for each history. It obeys

    W(h k;x)=W(h;x) W(k;T_h x).                      (2)

Summing (1) over all length-n histories gives one, by successively
summing the last step. It also gives finite-history consistency:

    sum_a W(h a;x)=W(h;x).                           (3)

These are useful conditional composition laws. They do not derive the
local probabilities, legal updates, complete state or Markov property.
State-dependent memory can be included in X; its existence and physical
law cannot be inferred merely by giving it a register name.

## 2. The cancellation test

Take two formal labels u,u^-1 with mutually inverse evaluated updates.
Give their next-step choices fixed positive probabilities p and 1-p,
where 0<p<1. Then

    T_(u u^-1)=T_empty,
    W(u u^-1;x)=p(1-p) != 1=W(empty;x).              (4)

Thus the history weight does not factor through the final transformation
alone. This is a precise failure of descent, not a failure of state
composition. It does not say that an observed endpoint is insufficient
for every purpose or that every formal history needs a physical memory.

In particular, a random walk on the group is still well-defined: at a
fixed length n, sum the word weights over all histories with each endpoint.
Its distribution generally depends on n as well as the endpoint. Equation
(4) forbids replacing all those distinctions by a single endpoint-only
word weight; it does not forbid the aggregated transition law.

There is also a same-length control. In the supplied free-group alphabet
a,a^-1,b,b^-1, give the two a labels probability p each and the two b
labels probability q each, with p,q>0, 2p+2q=1 and p!=q. The length-two
histories a a^-1 and b b^-1 have the same evaluated identity but weights
p^2 and q^2. Here endpoint plus length still loses the individual history
weight. Inversion symmetry is respected; exchange of a with b is not
imposed as a law symmetry. If that additional exchange is imposed, this
particular p!=q control does not meet it and cannot refute it. As before,
the summed endpoint kernel remains well-defined.

If a different model gives the register a genuine change after an
object returns, that register belongs in X and in T_h. The full-state
descent test must then be performed again. The earlier internal-undo
packet gives an explicit example of that distinction.

## 3. Why a positive group character answers a different question

Let G be a supplied group and w:G->R_(>0) satisfy

    w(gh)=w(g)w(h), w(1)=1.

It follows that w(g^-1)=1/w(g). If one also requires
w(g^-1)=w(g), then w(g)=1 for all g. Equivalently, an additive real
group action A with A(g^-1)=A(g) vanishes. An everywhere nonnegative
additive A also vanishes because A(g)+A(g^-1)=0.

These elementary arguments do not show that every physical action or
weight vanishes. A nonnegative path cost can be additive under path
concatenation without descending to the group obtained by cancelling
inverse labels. Complex amplitudes, transfer operators, sums over
intermediate states and state-dependent cocycles have different laws.
They must not be ruled out by the positive-character calculation.

The earlier INTEGER_END_DATA_AND_REGISTER.md already distinguishes an
additive label on the specified lifted group from a state-dependent
end cocycle. That scoped distinction is reused, not overwritten or
newly certified by this simpler character observation.

## 4. Normalize the right sample space

Equation (3) normalizes each length separately. Summing those weights
over the disjoint union of all finite lengths would give infinity.
This is not an inconsistency of a continuing stochastic process:
prefix events of different lengths overlap; they are not disjoint
outcomes of that process. Nor does it exclude an infinite-history law.

If instead a model asks for a completed finite history as the outcome,
it needs a stopping rule or length distribution. For example an explicitly
supplied independent stopping probability rho, 0<rho<1, gives

    W_stop(h;x)=rho(1-rho)^|h| W(h;x),
    sum_h W_stop(h;x)=sum_n rho(1-rho)^n=1.          (5)

The parameter rho is supplied for this control, not physically predicted.
A model with no stopping event should not be required to introduce it.
Full support, equal weights at a fixed length, a measure on completed
histories and a measure on infinite paths are different specifications.

## 5. What this pays, and what it leaves

Given the actual local registered law, the full finite-history products,
their consistent marginals and the summed transition kernels follow.
There is no need to choose every global history weight separately.
That is a conditional dependency reduction, not a foundational input
reduction: the local law still has to be derived or priced.

The process-reading proposal is therefore meaningful when it supplies
an actual law and retains its relevant history data. It does not earn
that law merely by iterating a map. The finite action-weight tests on
particular thread populations remain controls of those chosen weight
prescriptions, rather than exclusions of all process realizations.

None of this identifies these probabilities with OA's quantum amplitudes,
selects a physical action or boundary condition, or settles the observer,
qualia, SM3, vacuum-selection or gravity duties.
