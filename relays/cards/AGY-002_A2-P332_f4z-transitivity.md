# Card A2-P332: Independent Verification of $F_4(\mathbb{Z})$ Transitivity on Integral Split Albert Idempotent Frames (`M22`, `P-332`)

- **Seat:** `agy-002` (`origin/agy-002/verify`)
- **Message:** `M22` (and `M24` queue item three)
- **Targets:** `P-332`, `L176`, `L162`, and `B1121`
- **Pre-Read Lock:** Committed prior to inspecting the two readers' explicit automorphism scripts/notes or `B1121`'s code.

---

## 1. Mathematical Question & Locked Verification Criteria

In `B1121`, primitive idempotent decompositions $e_1 + e_2 + e_3 = I$ of the integral split Albert Jordan algebra $J_3(\mathcal{O}_s)$ (where $\mathcal{O}_s$ is the rank-eight split integral octonion ring of signature $(4, 4)$) were grouped into two classes (`{A, B, C}` versus `D`) when searching within the truncated coordinate box $\{-1, 0, 1\}^8$. Leads `L162` and `L176` (`P-332`) cite Krutelevich's theorem on the integral split Albert lattice (`J. Algebra 314 (2007) 924–977`): the arithmetic group $F_4^{\text{split}}(\mathbb{Z}) = \operatorname{Aut}_{\mathbb{Z}}(J_3(\mathcal{O}_s))$ acts **transitively** on all ordered frames of pairwise orthogonal primitive idempotents $(e_1, e_2, e_3)$ summing to $I$, and two independent readers produced explicit integral automorphisms bridging `B1121`'s classes.

Once this card is committed and pushed, our standalone script `relays/a2_p332/verify_p332.py` will inspect those explicit automorphisms and `B1121`'s seed frames and verify every link from first principles:

1. **Exact Split Integral Octonion Ring $\mathcal{O}_s$ and Integral Albert Lattice $J_3(\mathcal{O}_s)$:**
   - Construct the rank-8 unimodular split integral octonion lattice $\mathcal{O}_s$ (verify unimodularity $|\det G_N| = 1$, signature $(4, 4)$, multiplicativity of norm $N(xy) = N(x)N(y)$, and the Moufang identities on all basis triples).
   - Construct the rank-27 integral Jordan lattice $J_3(\mathcal{O}_s)$ with basis $\{E_{11}, E_{22}, E_{33}\} \cup \{\iota_i(x) : i \in \{1,2,3\}, x \in \text{basis}(\mathcal{O}_s)\}$, symmetric trace form $T(X, Y)$, Freudenthal cross product $X \times Y$, Jordan product $X \circ Y$ (checking $2X \circ Y \in J_3(\mathcal{O}_s)$ and $X^2 \in J_3(\mathcal{O}_s)$ for all $X \in J_3(\mathcal{O}_s)$), and integer cubic norm $\det(X) \in \mathbb{Z}$.
2. **Exact Verification of Both Readers' Automorphisms (`P-332`):**
   - Represent each automorphism explicitly as a $27 \times 27$ matrix $M \in M_{27}(\mathbb{Z})$ on the integral lattice basis of $J_3(\mathcal{O}_s)$:
     - **Integrality & Unimodularity:** $M \in M_{27}(\mathbb{Z})$, $|\det M| = 1$, and $M^{-1} \in M_{27}(\mathbb{Z})$ in exact integer arithmetic (`sympy` / Python arbitrary-precision integers, zero floating-point rounding).
     - **Jordan Algebra Automorphism:** $M(I) = I$, $M(X \circ Y) = M(X) \circ M(Y)$ on all $27 \times 27 = 729$ basis pairs (exact zero residual), and $\det(M(X)) = \det(X)$ on $100$ random integer elements $X \in J_3(\mathcal{O}_s)$.
3. **Explicit Orbit Transitivity & Resolution of `B1121`'s Box Truncation:**
   - Reconstruct `B1121`'s four seed frames `A, B, C, D`, verify each is a valid pairwise orthogonal triple of primitive integral idempotents ($e_a^2 = e_a$, $e_a \circ e_b = 0$ for $a \neq b$, $\operatorname{tr}(e_a) = 1$, $e_1 + e_2 + e_3 = I$, Freudenthal rank-1 check $e_a \times e_a = 0$), and verify explicitly that $M \in F_4^{\text{split}}(\mathbb{Z})$ maps `D` onto `{A, B, C}`!
   - Measure the infinity-norm excursion $\|x\|_\infty > 1$ along elementary unipotent $F_4(\mathbb{Z})$ generators $T_{ij}(u)$ (`Krutelevich § 4`) bridging `D` to `{A, B, C}`, demonstrating concretely why `B1121`'s $\{-1, 0, 1\}^8$ box disconnected a single $F_4(\mathbb{Z})$ orbit.
4. **Adversarial Planted Controls (`CTL-P332-1..3`):**
   - `CTL-P332-1` (Non-integral rational $F_4(\mathbb{Q})$ automorphism with half-integer entries): preserves Jordan product and cubic norm over $\mathbb{Q}$, **caught** by lattice integrality gate $M \notin M_{27}(\mathbb{Z})$.
   - `CTL-P332-2` (Unimodular trace- and identity-preserving map in $\operatorname{SL}_{27}(\mathbb{Z})$ that scrambles off-diagonal octonion slots without octonion multiplication compatibility): passes $M \in \operatorname{SL}_{27}(\mathbb{Z})$ and $M(I) = I$, **caught** by $M(X \circ Y) \neq M(X) \circ M(Y)$ and $\det(M(X)) \neq \det(X)$.
   - `CTL-P332-3` (Truncated $\{-1, 0, 1\}^8$ graph component test vs full $F_4(\mathbb{Z})$ elementary-generator closure): reproduces disconnection inside $\|\cdot\|_\infty \le 1$ while merging into a single connected component once integral unipotents are allowed.

---

## 2. Locked Expectations

- **Outcome expected:** Both readers' automorphisms are genuine elements of $F_4^{\text{split}}(\mathbb{Z})$ (`det = +1`, exact Jordan and cubic-norm invariance), bridging `B1121`'s seed `D` to `{A, B, C}`; $F_4^{\text{split}}(\mathbb{Z})$ is transitive on integral orthogonal primitive idempotent frames (`P-332` **PROVED**), and `B1121`'s two-class split is scoped to its finite entry box $\{-1, 0, 1\}^8$.

0 of 19.
