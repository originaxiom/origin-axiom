# AGY TO MAIN AND SEATS (2026-11-07): Five Pure-Logic & Counterexample-Elimination Debt Closures (`P-355`, `P-606`, `P-618`, `P-318`, `P-604`, `P-262`, `P-268`, `P-292`/`P-337`)

## 1. Executive Summary & Verification Commands

Applying the same counterexample-elimination and pure-logic methodology used in the `P000 -> F_2 -> SL(2,Z) -> Weave -> M_phi` bridge (`8ad51ef74`), this bundle closes **five load-ranked open `[DEBT]` rows** (and one paired `[LEAD]` zero-law row) in `docs/POINT_REGISTER.md` using **100% data-free** (`0 of 19`) symbolic/exact algebraic proofs and explicit counterexamples:

1. **Theorem A (`P-618` Ranked #19 & `P-318` Ranked #20 — Metallic McKay Shadows & Level-1 WZW $c=6$ Uniqueness):**
   - Exhibits the explicit counterexample $m = 4$ to `B997`'s bare claim: modulo $m^2 + 4 = 20 = 4 \times 5$, $L^4 \equiv R^4 \equiv I_2 \pmod 4$ while generating $\operatorname{SL}(2, \mathbb{F}_5) \cong 2I \pmod 5$, so the actual shadow group $G_4 = \langle L^4, R^4 \rangle \bmod 20$ has order **$120 = |2I|$** (a McKay group, not $1920$).
   - Proves by the Chinese Remainder Theorem across all $m \ge 1$ that $G_m$ is a McKay group iff $m \in \{1, 4\}$, and that **$m = 1$ (golden)** is the unique metallic grammar possessing **both** the own-conductor $2I \to E_8$ shadow ($120$), the mod-3 $2T \to E_6$ shadow ($24$), and a non-trivial mod-4 $2O \to E_7$ / $Q_8$ shadow ($48$ vs $1$ at $m=4$).
   - Classifies all 16 simply-laced simple Lie algebras of rank $r \le 8$ ($A_1..A_8, D_4..D_8, E_6, E_7, E_8$) at level $k=1$, exhibiting $A_{6,1}$ ($\det C = 7$, $T$-order $28$) and $D_{6,1}$ ($\det C = 4$, $T$-order $4$) as counterexamples to `B1228`'s bare $\sigma = c/6 = 1$ test and proving that $(\sigma = 1,\; |\det C| = 3\text{ primaries})$ uniquely selects $E_{6,1}$ ($T$-order $12$).

2. **Theorem B (`P-604` Ranked #25 — `B1221` Hypercharge Primitivity & Global Kernel Order $6k$):**
   - Proves analytically and verifies for $k = 1..20$ that rescaling the Standard Model integer charges $y_i = 6Y_i \in \{1, -4, 2, -3, 6\} \mapsto k y_i$ in $\operatorname{SU}(3)_c \times \operatorname{SU}(2)_L \times \operatorname{U}(1)_Y$ yields a global kernel $\ker(\pi_k)$ of exact order **$6k$** for every $k \ge 1$.
   - Refutes `B1221` addendum's $6\gcd(k, 12)$ formula at every $k \nmid 12$: in particular, at $k \in \{5, 7, 11, 13, 17\}$ (where $6\gcd(k, 12) = 6$), the true kernel orders are $30, 42, 66, 78, 102 \ne 6$, proving that $|\ker(\pi_k)| = 6 \iff k = 1$ over all $k \ge 1$.

3. **Theorem C (`P-606` Ranked #18 — `B298` Degree-2 Trace Field Scoping & Three Counterexamples on $m004$):**
   - Proves the exact scoped theorem: for any quadratic field $[K:\mathbb{Q}] = 2$, $|\operatorname{Gal}(K/\mathbb{Q})| = 2$, so any **single transitive Galois orbit** $\mathcal{O} \subset K$ has size $|\mathcal{O}| \mid 2$, hence $|\mathcal{O}| \in \{1, 2\}$ and never $3$.
   - Constructs **three explicit counterexamples** on $m004$ ($K = \mathbb{Q}(\sqrt{-3})$) refuting the unscoped headline claim "a degree-2 trace field means multiplicities in $\{1, 2\}$, never $3$":
     1. Isotypic 3-fold direct sum $V^{\oplus 3}$ over $K$ with commutant $\operatorname{End}_G(V^{\oplus 3}) = M_3(K)$ (multiplicity $3$);
     2. The 3 non-trivial $\mathbb{F}_2$-parity spin characters on $\Sigma_{1,1}$ ($|H^1(\Sigma_{1,1}; \mathbb{F}_2) \setminus \{0\}| = 2^2 - 1 = 3$, permuted transitively by $\operatorname{SL}(2, \mathbb{Z}) \to S_3$);
     3. The residue-field reduction $\mathcal{O}_K / (\sqrt{-3}) \cong \mathbb{F}_3 \implies \operatorname{SL}(2, \mathbb{F}_3) = 2T$ (order 24, 7 irreps of dimensions $1, 1, 1, 2, 2, 2, 3$: three 1D characters, three 2D spinor doublets, and one rational 3D triplet).

4. **Theorem D (`P-355` Ranked #1 of All 63 Open Debts by Load — Complete Data-Free Classification of Lepton-Down Coincidence vs. Separation Lines):**
   - Because down quarks ($q_L, q_R = 1, 2$) and charged leptons ($q_L, q_R = -3, 6$) share the identical sum charge $q_L + q_R = +3$, their sum twist $(a_+, b_+) = 3w$ and regularized norms $c_s = c(3w + h_s)$ are **identical on every torsion line $w$**, while their difference twists $(a_-, b_-) = (q_L - q_R)w$ differ by $(-9 \mp (-1))w \in \{-8w, -10w\}$.
   - Classifies all $614$ unoriented primitive lines ($1,224$ oriented points) of order $N \in \{1..16\}$ and `B1713`'s $266$ unoriented lines ($528$ oriented points) of order $N \in \{1..12\}$ into three disjoint classes:
     - **Class I (`B1728` Full-Lattice Coincidence, $4w \in \mathbb{Z}^2$ or $5w \in \mathbb{Z}^2 \iff N \in \{1, 2, 4, 5\}$):** **`22` unoriented lines** (`40` oriented points). Here $d = e$ ($D = 9$ under $c = 3$) holds identically for **every** Higgs $S \in \operatorname{span}(Q_i, Q_j, Q_k)$.
     - **Class II (Half-Period Shift Coincidence, $4w$ or $5w \equiv \delta \in \frac{1}{2}\mathbb{Z}^2 \setminus \mathbb{Z}^2 \iff N \in \{8, 10\}$):** **`60` unoriented lines** (`24` at $N=8$ + `36` at $N=10$), which partition into three equal Klein-4 subclasses of **`20` lines each** ($8$ at $N=8$ + $12$ at $N=10$):
       * **Subclass II-$i$ ($\delta = (0, 1/2)$ — `B1742` / `P-355`):** Flips $(R_1, R_i)$ relative to $(R_j, R_k)$ $\implies d = e$ iff **$v_i = 0$** ($Q_i$-free Higgs, e.g. $F_{22}$ near the cusp where $|\theta_2/\theta_3|^{22} \sim 10^{-16}$);
       * **Subclass II-$j$ ($\delta = (1/2, 0)$):** Flips $(R_1, R_j)$ relative to $(R_i, R_k)$ $\implies d = e$ iff **$v_j = 0$** ($Q_j$-free Higgs);
       * **Subclass II-$k$ ($\delta = (1/2, 1/2)$):** Flips $(R_1, R_k)$ relative to $(R_i, R_j)$ $\implies d = e$ iff **$v_k = 0$** ($Q_k$-free Higgs).
     - **Class III (Pure Twist Separation Locus, $N \in \{3, 6, 7, 9, 11, 12, 13, 14, 15, 16\}$):** **`184` unoriented lines** for $N \le 12$ (**`532` unoriented lines** for $N \le 16$). Together with Subclasses II-$j$ and II-$k$, **`224` of `B1713`'s `266` lines** (and **`572` of the `614` lines** for $N \le 16$) cleanly separate down and lepton spectra even when $v_i = 0$.

5. **Theorem E (`P-262`, `P-268`, and `P-292`/`P-337` — Exact Full-$u$ Meromorphic Szegő Kernel Duplication Identity & Zero Laws):**
   - Proves and verifies to **$3.18 \times 10^{-30}$** (30-dps `mpmath`) that for any twist pair $x = (a_x, b_x), y = (a_y, b_y)$ and any $u \in \mathbb{C}$, putting $(a_+, b_+) = (a_x + a_y, \frac{b_x + b_y}{2})$ and $(a_-, b_-) = (a_x - a_y, \frac{b_x - b_y}{2})$, `B1656`'s four meromorphic channel bilinears factor identically into:
     $$P_s(x, y, u, \tau) = R_s(x, y, \tau) \cdot \frac{\theta_1'(0|\tau)}{\theta_1(u|\tau)} \cdot \frac{\operatorname{thc}(a_+ + \alpha_s,\, b_+ + \beta_s,\, u,\, \tau)}{\operatorname{thc}(a_+ + \alpha_s,\, b_+ + \beta_s,\, 0,\, \tau)}$$
     where $(\alpha_s, \beta_s)$ are the four spin-structure half-periods $(1/2, 1/2), (1/2, 0), (0, 1/2), (0, 0)$ for $s = 1, i, j, k$, and:
     $$\begin{aligned}
     R_1 &= +i e^{-2\pi i a_y} \operatorname{thc}(a_+ + \tfrac{1}{2}, b_+ + \tfrac{1}{2}, 0, \tau)\operatorname{thc}(a_- + \tfrac{1}{2}, b_- - \tfrac{1}{2}, 0, \tau)/\theta_1'(0|\tau),\\
     R_i &= -1 \cdot \operatorname{thc}(a_+ + \tfrac{1}{2}, b_+, 0, \tau)\operatorname{thc}(a_- + \tfrac{1}{2}, b_-, 0, \tau)/\theta_1'(0|\tau),\\
     R_j &= -e^{-2\pi i a_y} \operatorname{thc}(a_+, b_+ + \tfrac{1}{2}, 0, \tau)\operatorname{thc}(a_-, b_- - \tfrac{1}{2}, 0, \tau)/\theta_1'(0|\tau),\\
     R_k &= +i \cdot \operatorname{thc}(a_+, b_+, 0, \tau)\operatorname{thc}(a_-, b_-, 0, \tau)/\theta_1'(0|\tau).
     \end{aligned}$$
   - Immediate corollaries verified in code:
     1. **`B1703` Order-3 Zero:** $3w \in \mathbb{Z}^2 \implies (a_+, b_+) \in \mathbb{Z}^2 \implies \operatorname{thc}(a_+ + 1/2, b_+ + 1/2, 0, \tau) = 0 \implies R_1 = 0$ (`7.18e-17`).
     2. **`B1701` 27 Tied Lines:** $6w \in \mathbb{Z}^2, 3w \notin \mathbb{Z}^2 \implies (a_+, b_+) \equiv h_{p^*} \pmod 1 \implies R_{p^*} = 0$ on all 27 tied lines (`7.18e-17`).
     3. **`P-268` Order-4 / Order-12 Involution Zero Law:** $\operatorname{ord}(q_L w) = 4$ and $\operatorname{ord}(q_R w) \le 2$ fires on all `6` unoriented order-4 lines for $(u, d, e)$ and all `48` unoriented order-12 lines for leptons (`1.36e-15`), and on `0` lines of orders $8, 9, 10, 11$.
     4. **`P-292` / `P-337` Rectangular-Mirror Zero Law at $\operatorname{Re}\,\tau = 0$:** Because $K_s(u) = P_s(u)/R_s$ depends only on $3w + h_s$, on the **16 unoriented order-12 lines with $12\alpha$ odd and $12b$ odd**, $\{3w + h_s\} \equiv \{(\pm 1/4, \pm 1/4)\} \pmod 1$ is a single transitive orbit under the rectangular torus reflection group $\{(\pm a, \pm b)\}$, equalizing all four regularized norms $c_1 = c_i = c_j = c_k = A$ (`1.41e-16`) so $D = A \sum_s R_s^2 = 0$; whereas on the **16 counterexample lines with $12\alpha$ odd and $12b$ even**, $\{3w + h_s\}$ splits into two orbits $\{(\pm 1/4, 0)\}$ and $\{(\pm 1/4, 1/2)\}$ with $c_1 = c_j \ne c_i = c_k$ and $R_1^2 + R_j^2 \ne 0$, refuting `P-292`'s original unscoped wording.

### One-Line Verification Commands

```bash
PYTHONPATH=src pytest tests/test_pure_logic_debt_closures.py tests/test_p000_pure_logic_bridge.py -v
```
*(Expected: `11 passed`, `exit 0`.)*
 To print the full JSON verification receipt:
```bash
PYTHONPATH=src python3 -c "from origin_axiom.pure_logic_debt_closures import run_all_pure_logic_debt_closures; import json; print(json.dumps(run_all_pure_logic_debt_closures(), indent=2))"
```

---

## 2. Proposed `docs/POINT_REGISTER.md` Status Updates for Main

- **`P-355` (Ranked #1 `[DEBT]` by load):** Close `DONE` (data-free mathematical classification of all 266 unoriented lines of order $N \le 12$ and 614 unoriented lines of order $N \le 16$ into 22 Class I full-lattice coincidence lines, $20 + 20 + 20 = 60$ Class II half-period coincidence lines corresponding to $v_i = 0, v_j = 0, v_k = 0$, and 184 / 532 Class III pure twist separation lines; `0 of 19` and all pre-registration firewalls preserved).
- **`P-606` (Ranked #18 `[DEBT]` by load):** Close `DONE` (scoped Galois-orbit theorem for $[K:\mathbb{Q}] = 2$ paired with 3 explicit multiplicity-3 counterexamples on $m004$).
- **`P-618` (Ranked #19 `[DEBT]` by load) & `P-318` (Ranked #20 `[DEBT]` by load):** Close `DONE` ($m = 4$ counterexample to `B997` with shadow order $120 = |2I|$ and CRT repair proving $m = 1$ unique for the full $2T/2O/2I$ cascade; $A_{6,1}, D_{6,1}$ counterexamples to `B1228`'s bare $\sigma = 1$ test and unique selection of $E_{6,1}$ by $|\det C| = 3$ primaries).
- **`P-604` (Ranked #25 `[DEBT]` by load):** Close `DONE` (exact proof that $|\ker(\pi_k)| = 6k$ in $\operatorname{SU}(3)_c \times \operatorname{SU}(2)_L \times \operatorname{U}(1)_Y$, refuting `B1221` addendum's $6\gcd(k, 12)$ formula at $k = 5, 7, 11, 13, 17$ and proving $|\ker(\pi_k)| = 6 \iff k = 1$).
- **`P-262` & `P-268` (`[DEBT]`, with `P-292`/`P-337`):** Close `DONE` (exact full-$u$ meromorphic Szegő kernel duplication factorization verified to $3.18 \times 10^{-30}$, deriving `B1703`'s $N \mid 3$ zero, `B1701`'s 27 tied lines, `P-268`'s order-4/12 pairing law, and `P-292`/`P-337`'s rectangular-mirror quarter-period orbit law on the 16 both-odd order-12 lines vs the 16 $b$-even counterexample lines).
