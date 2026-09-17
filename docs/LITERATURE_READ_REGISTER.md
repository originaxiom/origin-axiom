# THE LITERATURE READ REGISTER — what this programme has READ AT SOURCE, and what it has only CITED

**Created 2026-09-17, seat `xb` (xB023), at the owner's direction:**

> *"why dont we deep search all literature to all objects and families and its roots to see whether
> insightful work already exist and read these papers properly to understand our subjects better"*

**Why this exists.** On 2026-09-17 a single session found that **four of five citations given from
memory were wrong** (E58's instance), and then found a **sixth** defect of a different kind: a
theorem correctly quoted but **applied outside its hypotheses** (B1239's use of Kawauchi on cusped
manifolds). `docs/THEOREM_REGISTRY.md` records the programme's **own** theorems and their novelty
status. **This register records EXTERNAL theorems and whether anyone here has actually opened the
paper.**

## The three grades, and the rule

| grade | meaning |
|---|---|
| **READ-AT-SOURCE** | someone here obtained the paper and quoted the statement **from its own text**, with hypotheses transcribed |
| **CITED-UNREAD** | the statement is used from a secondary source, a summary, or memory. **It may not carry a load-bearing step alone.** |
| **UNREACHABLE** | the source was sought and could not be obtained (paywall, no preprint). **Records the attempt so it is not re-attempted blindly.** |

> **THE RULE THIS REGISTER ENFORCES: a CITED-UNREAD theorem may motivate a computation, may suggest
> a prediction, and may be named — but it may NOT be the sole support for a banked conclusion.
> Where a CITED-UNREAD statement is load-bearing, MEASURE the statement instead and grade the
> result as a measured law.**
>
> **And the lesson that cost the most: quoting a theorem correctly is NOT enough. Check that the
> object in hand SATISFIES ITS HYPOTHESES.** A correctly-quoted theorem applied to the wrong class
> of object fails exactly as badly as a misquoted one — and is harder to see.

---

## The register

| source | statement, as used here | grade | where it bears | notes |
|---|---|---|---|---|
| **A. Kawauchi, *On 3-manifolds admitting orientation-reversing involutions*, J. Math. Soc. Japan 33 (1981) 571–589** | **THEOREM I:** *"Given a pair (M, α), then the torsion subgroup T₁(M;ℤ) of the homology group H₁(M;ℤ) is isomorphic to a direct double A⊕A or a direct sum A⊕A⊕ℤ₂ for some A."* — where the paper's own opening fixes a **pair (M,α)** as *"M a **CLOSED, ORIENTED** 3-manifold, α an orientation-reversing involution."* **THEOREM III:** σ(M)=0 ⟺ σ(α,M)=0 ⟺ M bounds a compact 4-manifold with a compatible involution (four equivalent conditions), with **Definition 1.2** making σ(α,M) the number of **discrete fixed points mod 2**. | **READ-AT-SOURCE** (2026-09-17, xB023) | B1239's torsion step; xB023 W2/K1–K3 | **FORCED A CORRECTION.** A free involution has Fix = ∅ ⇒ σ(α,M)=0 ⇒ σ(M)=0 ⇒ **strict** direct double, so the paraphrase *"free ⇒ Tor = A⊕A"* **is sound**. Its one defect is that **B1239 applies it to CUSPED manifolds**, which are not pairs (M,α): measured failure **590 of 1260**. Tested on 46 manifolds built to satisfy the hypotheses: **46/46**. |
| **W. D. Neumann and J. Yang, *Rationality problems for K-theory and Chern–Simons invariants of hyperbolic 3-manifolds*, Enseign. Math. 41 (1995); arXiv math/9712225** | **THEOREM A:** *"The Chern–Simons invariant CS(M) of a hyperbolic 3-manifold is rational if the associated embedding of the invariant trace field k(M) is a CM-embedding."* Plus their **conjecture**: if `k ∩ k̄ ⊂ ℝ` then CS(M) is **irrational** — which covers **all odd-degree trace fields**. | **READ-AT-SOURCE** (theorem statements; 2026-09-17, xB023 literature pass) | xB015's rational-CS result on the 112-family; the 1.51 % base rate | The record already had this **correctly** after xB015's own correction, including that it is the **Enseign. Math.** paper and **not** the Duke *Bloch invariants* paper. This pass **confirms**, it does not correct. `ℚ(√−3)` is imaginary quadratic, hence CM, which is why the family's CS is rational. |
| **R. Meyerhoff and M. Ouyang, *The η-invariants of cusped hyperbolic 3-manifolds*, Canad. Math. Bull. 40 (1997) 204–213, DOI 10.4153/CMB-1997-025-8** | the cusped η–cs relation; **L194's named tool** for closing the cusp-local lemma | **UNREACHABLE** — Cambridge Core paywall; no preprint found (2026-09-17). Abstract obtained: *"The η-invariant for a cusped hyperbolic 3-manifold is defined and applications are discussed. Such an invariant detects the chirality of a hyperbolic knot or link."* | L194's open half | **THE BLOCKER.** L194's register entry has carried it as *"cited, not read"* since 2026-09-02. **xB023 cites it nowhere** and closes nothing with it. Secondary route noted: Yoshida's formula for η(M(p,q)) and Meyerhoff's special-singular-frame construction are described in citing literature — a legitimate next attempt, **not** a substitute. |
| **CGHN (Coulson–Goodman–Hodgson–Neumann), *Computing arithmetic invariants of 3-manifolds*** | p. 14: SnapPy computes closed CS **only mod ½**; p. 15: the APS relation `3η(M) ≡ 2cs(M) + τ (mod 2)` | **CITED-UNREAD** (quoted through B1239) | B1239's closed-case argument; xB023's mod-½ fence | B1239's **main** closed conclusion rests on this, not on Kawauchi. **Flagged for a read pass** — it is currently the load-bearing unread citation in the L194 chain. |
| **Neumann–Reid**, invariant trace field = the field generated by the tetrahedron shapes | used to identify the **shape field** with the **invariant trace field** | **CITED-UNREAD** | xB022 V4 | xB022 **declined to rely on it**: it reports the **shape field** and explicitly does **not** claim the identification. The correct handling of a CITED-UNREAD statement, and the model for this register. |
| **Witten, arXiv:1001.2933 eq. 2.2; Gukov, hep-th/0306165 §1.1** | `σ` is a continuous parameter of complex Chern–Simons; nothing couples it to `k` | **CITED-UNREAD** | xB016's closure of the index→anchor route; xB021 S4's limit | Load-bearing for a **negative** (a route being closed), which is the lower-risk direction — but it should still be read. |
| **Bergeron–Venkatesh, Conjecture 1.3** | the `1/(6π)` torsion growth constant | **CITED-UNREAD, and mis-graded once** | corrected earlier this session | It is a **CONJECTURE, not a theorem**, and the record previously carried it as a theorem. Already corrected; listed here so the correction is not lost. |

---

## Standing targets for the next literature pass

Ordered by how much weight they currently carry unread:

1. **CGHN** — the APS relation and the mod-½ statement. **Highest priority**: it is the load-bearing unread citation in the entire L194 chain.
2. **Meyerhoff–Ouyang** — L194's blocker. Try an interlibrary route, Ouyang's thesis, or a citing paper that reproduces the formula in full.
3. **Neumann–Reid** — would upgrade xB022 V4 from *shape field* to *invariant trace field* and remove a declared fence.
4. **Witten / Gukov** — read at the equation level, to make xB016's closure a read closure.
5. **Floyd–Hatcher, Guéritaud** (punctured-torus bundles) and **Minsky** (punctured-torus groups) — the family's own roots; B1404 already verified the Minsky relay against the arXiv record.

**This register is appended to, never rewritten.** A grade may only move **upward** (CITED-UNREAD →
READ-AT-SOURCE) by an arc that quotes the source's own text, and the arc is named in the row.
