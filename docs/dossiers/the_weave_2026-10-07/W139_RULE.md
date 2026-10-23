# W139 — the E₆ breaking arc: can the vevs of the families' 27s break m_e = m_d? The extended down-quark and charged-lepton mass matrices under E₆'s cubic, what keeps them equal, and what could split them (the rule, committed before the script)

The SM-derivation seat, 2026-10-23. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **W137** found that the minimal joint frame forces M_e = M_d: the Higgs sits in the families' 10s, and SO(10)'s
  16·16·10 does the rest. So D ≡ 1, against P-094's 10.58. Its open question was whether E₆'s own breaking can split
  them. After E₆ breaks, d^c mixes with the 27's exotic D^c, and L with the 10's Higgs-like doublets.
- **Main's sweep queued exactly this** (P-338): "what remains is the mixing of the 27's exotic states with the
  Standard Model's after E₆ breaks, which no arc computes".
- **The owner agreed (2026-10-23)** that this comes first: it either rescues or retires the joint frame's lepton
  sector.

## The objects

- **E₆'s 27 in the trinification basis.** Under SU(3)_C × SU(3)_L × SU(3)_R the 27 is (3, 3̄, 1) ⊕ (1, 3, 3̄) ⊕
  (3̄, 1, 3): three 3 × 3 matrices Q^a_α, L^α_{α′} and Q^c_{α′ a}. Its cubic invariant is
  N = det Q + det L + det Q^c − tr(Q L Q^c), the cubic norm of the exceptional Jordan algebra.
- **The embedding of the Standard Model.**
  - SU(2)_L acts on α ∈ {1, 2}, with T₃ = diag(½, −½, 0) on L's α and its negative on Q's α.
  - Hypercharge is Y = t_L − t_R on L, −t_L on Q and t_R on Q^c, with t_L = diag(−1/6, −1/6, 1/3) and
    t_R = diag(−2/3, 1/3, 1/3). The electric charge is T₃ + Y.
  - By hand this gives the Standard Model's 16 ⊕ 10 ⊕ 1. In L: one Y = +½ doublet (h_u), two Y = −½ doublets (L and
    h_d), e^c, and two neutral singlets (ν^c, S). In Q: the quark doublet and the exotic D. In Q^c: u^c, d^c and D^c.
- **Three families.** The superpotential is W = Σ λ_{ijk} N(Φ_i, Φ_j, Φ_k), with λ totally symmetric (W135) and N
  polarised.
- **The vevs.** Any values in the five neutral directions of each family's L:
  - h_u⁰ (α = 2, α′ = 1);
  - the two Y = −½ doublets' neutral parts (α = 1, α′ = 2, 3);
  - the two singlets (α = 3, α′ = 2, 3).
  These are every vev a 27 can carry that keeps colour and electric charge. They include E₆'s breaking to SO(10)
  and to SU(5).
- **The extended mass matrices** (6 × 6, two states per family):
  - the charge −1/3 quarks, (d, D) against (d^c, D^c);
  - the charged leptons, (e, h_d⁻) against (e^c, h_u⁺).
  Both come from W's second derivatives at the vevs. The quarks come only from the tr(Q L Q^c) term, and the
  leptons only from det L.

## Weave or thread

**WEAVE-type**, as W137:
- the joint frame (E₆ from the moves, W135);
- all three families, every symmetric coupling λ, every vev of the 27s that keeps colour and electric charge;
- claims about all of them at once.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| E0 | **The instrument: N is E₆'s cubic.** The linear maps A of ℂ²⁷ that preserve N to first order (∇N(X)·AX = 0 for all X) form a space of dimension exactly 78. Exact rank over ℚ at 1 500 random integer points | 85% |
| E1 | **The embedding.** With the stated T₃ and Y, the 27's components carry exactly the Standard Model's 16 ⊕ 10 ⊕ 1. That is the multiset of (colour, electric charge, Y), with colour triplets counted once. The neutral colourless components are exactly the five listed | 97% |
| E2 | **The theorem.** For any symmetric λ and any vevs in the fifteen neutral directions of the three families, the extended charge −1/3 quark matrix and the extended charged-lepton matrix have the same six singular values. Checked at ten random complex points to 10⁻¹⁰ relative | 92% |
| E3 | **The light states.** At hierarchical vevs (the singlets 10⁴ times the doublets, as E₆ → SU(5) above the weak scale), the three lightest down-type and charged-lepton masses agree to 10⁻⁸ relative at five random points. So m_e = m_d, m_μ = m_s, m_τ = m_b, and D ≡ 1 | 90% |
| E4 | **The control: the relation is E₆'s normalisation.** With det L's coefficient changed to 2, every lepton singular value doubles while the quarks' stay. At that coefficient the symmetry algebra of the cubic drops to dimension 24, SU(3)³ alone | 80% |
| E5 | the read-out, and a READING by hand on what can split the two | — |

## What the outcomes mean (fixed now)

- **E0 to E4 hold.** Then:
  - **No vev of the families' 27s breaks m_e = m_d.** That includes E₆ → SO(10) → SU(5) through S and ν^c, the
    mixing of d^c with D^c and of L with h_d, and the doublets' vevs.
    - Every such vev is an SU(5) singlet or the neutral part of an SU(5) doublet. Here SU(5) is the one that
      commutes with the SU(2) rotating d^c into D^c; under SU(5) × SU(2) the 27 is (10, 1) ⊕ (5̄, 2) ⊕ (5, 1) ⊕
      (1, 2), with (ν^c, S) the last.
    - Under E₆'s cubic, the extended down and lepton matrices are then transposes of each other, in every family
      structure.
    - This extends W137's exclusion from the minimal Higgs to every vev of the 27s.
  - **So the joint frame's lepton sector cannot be rescued inside the 27s.** It needs a source that breaks SU(5)'s
    relation between leptons and down quarks. By hand, the known sources are:
    - a 351′ Higgs, whose SO(10) 126 carries the Georgi–Jarlskog 45 and its −3;
    - a 351 (its 120);
    - the adjoint 78's vev in higher operators;
    - a hypercharge flux or flat hypercharge line.
  - **The record already has the last one in main's frame** (B1656's flat lines, read through hypercharge in B1728).
    There, order-5 lines keep SU(5)'s five-ality and give D_frame = 1 exactly (B1726, W138's C1), while the best
    six-row sits on an order-10 line with D_frame = 1.22.
    - Read together with this arc: only a flat hypercharge line that breaks SU(5)'s relation can split leptons from
      down quarks.
    - The joint frame and main's frame then need the same ingredient, which W134 left out ("flat U(1) lines inside
      E₆").
- **E0 fails** (dimension ≠ 78). The cubic's normalisation is wrong. E2 and E3 are read only after it is resolved post
  hoc.
- **E2 fails** (the singular values differ somewhere). Some 27 vev splits leptons from down quarks. That vev and the
  split are recorded as found: the positive this seat does not expect.

## What stays out

- The 351′, 351 and 78 Higgses, and their Clebsches, which are cited from the literature and not computed.
- Flat lines and fluxes inside E₆; running between scales; the D quarks' and the extra doublets' phenomenology;
  proton decay through D.
- The 27̄s and vector-like pairs beyond the three families.

## Seen before the rule (disclosed)

- **Read:** W137's record; main's sweep commits (P-338, P-314); B1728's and B1726's statements on order-5 lines;
  W138's C1.
- **By hand:**
  - the hypercharge and isospin assignment and E1's multiset;
  - the theorem's argument. The quark block is the restriction of ⟨L⟩ to α ∈ {1, 3}, α′ ∈ {2, 3}, from tr(Q L Q^c).
    The lepton block is the matching cofactor block of det L, the same entries up to signs and transposition, and
    the family sum has the same λ.
  - the SU(5) reading (every neutral direction of a 27 is an SU(5) singlet or a doublet's neutral part);
  - E4's factor of 2.
- **From the literature** (general knowledge): the trinification form of E₆'s cubic; the Georgi–Jarlskog 45 inside
  SO(10)'s 126.
- **Not run:** nothing has been computed by a script.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed launch is disclosed, with its log kept. Any failed prediction is recorded as failed, and any later check is
  labelled post hoc.

0 of 19.
