# Card A2-TICK: Independent Third Derivation of `B1926` From Its Statement Alone (`M24`)

- **Seat:** `agy-002` (`origin/agy-002/verify`)
- **Message:** `M24` (queue item four: new derivation card)
- **Statement (`M24` verbatim, sole input):**
  > On a once-punctured-torus bundle with an orientation-reversing monodromy, show (or refute) three things:
  > - no 1-cocycle over a character trivial on the cusp's meridian is non-zero on the scar `[a, b]`;
  > - over the characters twisted by the orientation character, such classes are free;
  > - each twisted class at level `n` pulls back to a class non-zero on the scar at the double cover, level `2n`.
- **Strict Blindness:** **Zero** files in `frontier/B1926*` (or any summary of `B1926` elsewhere in the repository) have been opened or inspected. Everything below is derived solely from `M24`'s statement and standard algebraic topology / Fox free differential calculus.

---

## 1. Analytical Derivation & Locked Expectations Before Running Code

Let $\Sigma = \Sigma_{1,1}$ be a compact connected oriented once-punctured torus with $\pi_1(\Sigma, p_0) = F_2 = \langle a, b \rangle$ and boundary loop ("scar") $\lambda = [a, b] = a b a^{-1} b^{-1} \in [F_2, F_2]$. Let $f : (\Sigma, \partial\Sigma) \to (\Sigma, \partial\Sigma)$ be an orientation-reversing homeomorphism inducing $\sigma \in \operatorname{Aut}(F_2)$ with abelianisation $A_\sigma \in \operatorname{GL}_2(\mathbb{Z})$, $\det(A_\sigma) = -1$.

### Premise & Convention Audit ("What the statement needed and did not say")

Before computing, pure Fox calculus exposes **three unstated premises / edge-case qualifications** that decide whether the three claims hold literally or require sharp scoping:

1. **Unstated Premise P1 (Geometric Cusp Meridian $\mu$ vs Algebraic HNN Suspension Letter $t$):**
   - By Nielsen's theorem, any $\sigma \in \operatorname{Aut}(F_2)$ with $\det(A_\sigma) = -1$ satisfies $\sigma([a, b]) = w_\sigma [a, b]^{-1} w_\sigma^{-1}$ for a word $w_\sigma \in F_2$ (for example, the algebraic tick $\sigma_{\text{alg}}(a) = ab,\; \sigma_{\text{alg}}(b) = a$ has $w_\sigma = a \neq 1$, whereas its inner conjugate $\sigma_0(a) = ba,\; \sigma_0(b) = a$ fixes a boundary basepoint $p_0 \in \partial\Sigma$ and satisfies $\sigma_0([a, b]) = [a, b]^{-1}$ on the nose with $w_{\sigma_0} = 1$).
   - In $\pi_1(M_\sigma) = \langle a, b, t \mid t a t^{-1} = \sigma(a),\; t b t^{-1} = \sigma(b) \rangle$, the Klein-bottle peripheral subgroup $\pi_1(\partial M_\sigma) \cong \pi_1(K^2)$ has scar $\lambda = [a, b]$ and **geometric cusp meridian** $\mu = [a, b]^k w_\sigma^{-1} t$ satisfying $\mu [a, b] \mu^{-1} = [a, b]^{-1}$.
   - **Critical consequence:** $\chi(\mu) = \chi(w_\sigma)^{-1}\chi(t)$ is independent of the framing integer $k$ (since $\chi([a,b]) = 1$) and of outer-automorphism gauge, **but $\chi(\mu) \neq \chi(t)$ whenever $\chi(w_\sigma) \neq 1$**! Claim 1 holds for the **geometric cusp meridian** $\mu$, and **fails** if one substitutes the un-gauged HNN letter $t$ when $\chi(w_\sigma) \neq 1$.

2. **Exact Proof of Claim 1 (`c([a, b]) = 0` when $\chi(\mu) = +1$, in characteristic $\neq 2$):**
   - Over any commutative ring $R$ in which $2$ is a non-zero-divisor (e.g. $\mathbb{Z}$, $\mathbb{Z}[\zeta_d]$, $\mathbb{Q}(\zeta_d)$, or $\mathbb{C}$), every multiplicative character $\chi : \pi_1(M_\sigma) \to R^\times$ has $\chi([a, b]) = 1$, hence $c([a, b]^{-1}) = -c([a, b])$ for every 1-cocycle $c \in Z^1(M_\sigma; R_\chi)$.
   - Applying $c(xy) = c(x) + \chi(x)c(y)$ to $\mu [a, b] = [a, b]^{-1} \mu$ cancels $c(\mu)$ identically and gives the universal peripheral identity:
     $$\big(\chi(\mu) + 1\big)\, c([a, b]) = 0.$$
   - Therefore, whenever $\chi(\mu) = +1$ (and $2$ is not a zero-divisor in the coefficient module; **note counterexample in characteristic two**, where $\chi(\mu) = +1 = -1$!), $2\,c([a, b]) = 0 \implies c([a, b]) = 0$. **Expected outcome for Claim 1: HOLDS** (with characteristic $\neq 2$ and geometric meridian $\mu$ stated explicitly).

3. **Sharp Qualification on Claim 2 (Trivial-Fibre Exception & Integral $2$-Torsion at Even Order):**
   - The orientation character $\omega = w_1(TM_\sigma) : \pi_1(M_\sigma) \to \{\pm 1\}$ satisfies $\omega(a) = \omega(b) = +1$ and $\omega(\mu) = -1$. Twisting any meridian-trivial character $\chi_+$ ($\chi_+|_{F_2} = \chi_0,\; \chi_+(\mu) = +1$) by $\omega$ gives $\chi_- = \chi_+ \otimes \omega$ with $\chi_-|_{F_2} = \chi_0$ and $\chi_-(\mu) = -1$.
   - In the boundary-preserving gauge $\sigma_0([a, b]) = [a, b]^{-1}$, let $\alpha = \chi_0(a)$, $\beta = \chi_0(b)$, $u_\chi = (\alpha - 1, \beta - 1)^T$, $v_\chi^T = (1 - \beta, \alpha - 1)$, and $D_\chi(\sigma_0) \in M_2(R)$ be the twisted Fox Jacobian. Fox's fundamental identity and chain rule give:
     $$D_\chi(\sigma_0)\, u_\chi = +u_\chi, \qquad v_\chi^T D_\chi(\sigma_0) = -v_\chi^T, \qquad c([a, b]) = v_\chi^T \begin{pmatrix} c(a) \\ c(b) \end{pmatrix}.$$
   - **Edge Case 2a (Trivial fibre character $\chi_0 = 1$, i.e. $\chi_- = \omega$ itself):** Here $u_\chi = 0$ and $v_\chi = 0$, so **$c([a, b]) = 0$ identically**! Moreover, for every hyperbolic orientation-reversing monodromy ($\operatorname{tr} A_\sigma \neq 0$, including every odd tick power $J^n$), $\det(A_\sigma + I_2) = \operatorname{tr}(A_\sigma) \neq 0$, so $H^1(M_\sigma; \mathbb{C}_\omega) = 0$ and $H^1(M_\sigma; \mathbb{Z}_\omega) \cong \mathbb{Z}/2\mathbb{Z}$ (pure 2-torsion, **zero** free rank!). Thus **Claim 2 requires excluding the trivial fibre character $\chi|_{F_2} = 1$** (note that at $n = 1$ tick $J = \begin{pmatrix}1 & 1\\ 1 & 0\end{pmatrix}$, $|\det(J - I_2)| = |\operatorname{tr} J| = 1$, so **zero** non-trivial $J$-invariant fibre characters exist!).
   - **Non-trivial fibre characters ($\chi_0 \neq 1$):** Since $u_\chi \neq 0$ and $v_\chi^T \neq 0$ with $v_\chi^T u_\chi = 0$, over $K = \mathbb{Q}(\zeta_d)$ or $\mathbb{C}$ the Fox Jacobian $D_\chi(\sigma_0)$ ALWAYS has eigenvalues $\{+1, -1\}$ ($\operatorname{tr} D_\chi = 0,\; \det D_\chi = -1$), $\dim_K H^1(M_\sigma; K_{\chi_-}) = 1$, and scar evaluation $\operatorname{ev}_{[a,b]} : H^1(M_\sigma; K_{\chi_-}) \xrightarrow{\sim} K$ is a **linear isomorphism** (every non-zero twisted class is non-zero on $[a, b]$, and the space of classes is free of rank one over $K$!).
   - **Edge Case 2b (Integral freeness over $R = \mathbb{Z}[\zeta_d]$ when $2 \mid d$ vs $2 \nmid d$):** Over the ring of algebraic integers $R = \mathbb{Z}[\zeta_d]$ ($d = \operatorname{ord}(\chi_0)$):
     - When $d \ge 3$ is **odd**, the ideal $(\alpha - 1, \beta - 1, 2)R = R$ is the unit ideal, so $H^1(M_\sigma; R_{\chi_-})$ is **strictly torsion-free** (rank-1 projective, and free of rank 1 whenever $\operatorname{Pic}(R) = 0$, e.g. $d = 5, 11$).
     - When $d$ is **even** (e.g. $d = 2$ at three ticks $J^3 = \begin{pmatrix}3 & 2\\ 2 & 1\end{pmatrix}$, where $\operatorname{tr}(J^3) = 4$ gives three order-2 characters), $2 \mid (\alpha - 1, \beta - 1)$, and $H^1(M_{J^3}; \mathbb{Z}_{\chi_-}) \cong \mathbb{Z} \oplus (\mathbb{Z}/2\mathbb{Z})$ has **free rank 1** (non-zero on $[a, b]$) **plus a non-trivial $2$-torsion summand $\mathbb{Z}/2\mathbb{Z}$** (vanishing on $[a, b]$)!

4. **Exact Proof of Claim 3 (Pullback to the Orientation Double Cover, Level $n \to 2n$):**
   - Let $\pi : M_{\sigma^2} \to M_\sigma$ be the orientation double cover ($\ker \omega = F_2 \rtimes_{\sigma_0^2} \mathbb{Z}\langle \tilde{\mu} \rangle$, $\tilde{\mu} = \mu^2$).
   - Because $\pi_*([a, b]) = [a, b]$ and $\pi_*(\tilde{\mu}) = \mu^2$, every orientation-twisted character $\chi_-$ ($\chi_-(\mu) = -1,\; \chi_-|_{F_2} = \chi_0 \neq 1$) pulls back to a **meridian-trivial** character $\widetilde{\chi} = \pi^*\chi_-$ upstairs ($\widetilde{\chi}(\tilde{\mu}) = (-1)^2 = +1,\; \widetilde{\chi}|_{F_2} = \chi_0$), and for every twisted class $[c] \neq 0$,
     $$(\pi^* c)([a, b]) = c(\pi_*([a, b])) = c([a, b]) \neq 0.$$
   - Moreover, since $\operatorname{tr} D_\chi(\sigma_0) = 0$ and $\det D_\chi(\sigma_0) = -1$, Cayley–Hamilton gives $D_\chi(\sigma_0^2) = D_\chi(\sigma_0)^2 = I_2$ **identically**, so $\dim_K H^1(M_{\sigma^2}; K_{\widetilde{\chi}}) = 1$ and $\pi^* : H^1(M_\sigma; K_{\chi_-}) \xrightarrow{\sim} H^1(M_{\sigma^2}; K_{\widetilde{\chi}})$ is an **isomorphism**!
   - We verify **both** meanings of "level $n \to$ level $2n$": (i) tick-bundle cover index $n \to 2n$ ($\sigma = \sigma_0^n$ at odd $n = 1, 3, 5, 7, 9$ pulling back to $\sigma_0^{2n}$ at $2n = 2, 6, 10, 14, 18$), and (ii) congruence / character-order structure ($J^3 \equiv I_2 \pmod 2 \implies J^6 \equiv I_2 \pmod 4$, and total character image $\mu_d \cdot \{\pm 1\} = \mu_{2d}$ for odd $d$).

---

## 2. Adversarial Planted Controls (`CTL-TICK-1..3`)

1. **`CTL-TICK-1` (Algebraic HNN letter $t$ confused with geometric cusp meridian $\mu$):** Using $\sigma_{\text{alg}}(a) = ab, \sigma_{\text{alg}}(b) = a$ ($w_\sigma = a \neq 1$) and setting $\chi(t) = +1$ instead of $\chi(\mu) = \chi(a^{-1} t) = +1$ produces a 1-cocycle with $c([a, b]) \neq 0$, proving P1 is load-bearing.
2. **`CTL-TICK-2` (Trivial fibre character $\chi = \omega$ edge case):** Evaluating $H^1(M_{J^n}; \mathbb{Z}_\omega)$ at $\chi|_{F_2} = 1, \chi(\mu) = -1$ gives pure 2-torsion $\mathbb{Z}/2\mathbb{Z}$ and $c([a, b]) = 0$, proving the $\chi|_{F_2} \neq 1$ hypothesis in Claim 2 is mandatory.
3. **`CTL-TICK-3` (Orientation-preserving control $\det A_\sigma = +1$):** Replacing $\sigma_0$ by $\sigma_0^2 = LR$ ($\det = +1$) allows meridian-trivial characters $\chi(\tilde{\mu}) = +1$ to have $c([a, b]) \neq 0$, confirming orientation reversal ($\det = -1$) is what drives Claim 1.

0 of 19.
