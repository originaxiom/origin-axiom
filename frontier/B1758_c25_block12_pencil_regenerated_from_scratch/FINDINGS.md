# B1758 — THE BLOCK-12 PENCIL REGENERATED FROM SCRATCH AND C25'S WALL SIGN CERTIFIED IN EXACT RATIONAL ARITHMETIC (P-301 / R70-1): PROVED — WITHOUT `b12_tower.pkl`, `det₁₄(ρ)` AND `e(ρ)` ARE REBUILT OVER `ℚ[ρ]/μ(ρ)` FROM B854 IN 1.5 s; `det₁₄(ρ) = (9084997258444800000/13⁴)(ρ + 13/235200)² + 2727198720 ≥ 2 727 198 720 > 0` FOR ALL REAL `ρ`; `THEOREM_LEDGER` C25 CONFIRMED

**Verdict: PROVED.** agy, 2026-10-26 (P-301, first item in Review 70's R70-1 verification queue; L228's remainder).
Pure structure (`0 of 19`).

## 1. The question (P-301 / R70-1)

`THEOREM_LEDGER` C25 (*the Second Measurement*, B892, B893) carries the clause *"the wall complex in the split frame, at
all three roots"* from B893's M3 (`frontier/B893_omega_vs_measurement/signature_and_walls.py`), which evaluated
$\det_{14}(\rho) \in F = \mathbb{Q}[\rho]/\mu(\rho)$ at the three real roots of
$$\mu(\rho) = 500716339200\,\rho^3 - 2075673600\,\rho^2 - 4769856\,\rho + 2197$$
to obtain $3.8548 \times 10^9$, $2.7926 \times 10^9$, and $1.3209 \times 10^{10}$. Review 68 (L228) and Review 70 (R70-1)
noted that `signature_and_walls.py` read $\det_{14}(\rho)$ from a session-scratchpad pickle (`$SCRATCH/b12_tower.pkl`) that
is not in the repository (E80-shaped), and asked to:
1. Regenerate the block-12 pencil $(R_8, R_{14}, R_{16}, \mu, C_2, C_0, e, \det_{14})$ from the repository's exact $E_6$
   centraliser tower (`B854/e6_centralizer.py`) from a clean checkout;
2. Certify the signs $\det_{14}(\rho_i) > 0$ (and $e(\rho_i) > 0$) at all three real roots of $\mu(\rho)$ in exact
   rational arithmetic; and
3. Confirm C25 or correct it with a dated note.

## 2. Exact rational regeneration of the block-12 pencil

1. **Isolation of block 12 ($N_{12} \subset \mathfrak{e}_6$, $\dim_{\mathbb{Q}} N_{12} = 12$):**
   From `B854/e6_centralizer.py`, the exact rational $78 \times 78$ adjoint matrices $\mathrm{ad}(x_8)$, $\mathrm{ad}(x_{14})$,
   $\mathrm{ad}(x_{16}) \in M_{78}(\mathbb{Q})$ commute pairwise. The squarefree part of $\mathrm{charpoly}(\mathrm{ad}(x_{14}))$
   has a unique irreducible degree-6 factor whose nullspace on $\mathfrak{e}_6$ has dimension 12:
   $$f_6(t) = t^6 + 19856793600\,t^4 + 98573063018250240000\,t^2 + 142198242829436706619392000000.$$
   Restricting $\mathrm{ad}(x_n)$ ($n \in \{8, 14, 16\}$) to $N_{12} = \ker f_6(\mathrm{ad}(x_{14}))$ via its 12 pivot rows
   yields exact $12 \times 12$ rational matrices $R_8, R_{14}, R_{16} \in M_{12}(\mathbb{Q})$ satisfying
   $\mathrm{ad}(x_n) N_{12} = N_{12} R_n$ and $[R_m, R_n] = 0$ identically.
2. **Restriction of scalars to $W_4(\rho) = \ker(R_8 + \rho R_{16})$ over $F = \mathbb{Q}[\rho]/\mu(\rho)$:**
   Using the $3 \times 3$ companion matrix $C_\mu$ of $\mu(\rho)$, the blown-up operator
   $M_{36} = R_8 \otimes I_3 + R_{16} \otimes C_\mu \in M_{36}(\mathbb{Q})$ has exact $\mathbb{Q}$-nullspace dimension 12,
   giving the 4-dimensional $F$-module $W_4(\rho)$. Extracting $F$-traces via the non-degenerate trace form
   $G_{ij} = \mathrm{Tr}_{F/\mathbb{Q}}(\rho^{i+j})$ and Newton's identities gives the exact polynomials in
   $F = \mathbb{Q}[\rho]/\mu(\rho)$:
   - For $R_{16}|_{W_4(\rho)}$, $\mathrm{charpoly}_F(R_{16}|_{W_4})(s) = s^4 + C_2(\rho) s^2 + C_0(\rho) = (s^2 - e(\rho))^2$
     with $C_2(\rho)^2 - 4 C_0(\rho) = 0 \pmod{\mu(\rho)}$, $(R_{16}|_{W_4})^2 = e(\rho) I_4$ identically (semisimple), and
     $$e(\rho) = -\frac{1}{2} C_2(\rho) = -\frac{752150557025548369920000}{13^6}\,\rho^2 + \frac{159895951748628480000}{13^5}\,\rho + \frac{82022486586163200}{13^4}.$$
   - For $R_{14}|_{W_4(\rho)}$, $\mathrm{charpoly}_F(R_{14}|_{W_4})(s) = (s^2 + \det_{14}(\rho))^2$ with
     $$\det_{14}(\rho) = \frac{9084997258444800000}{13^4}\,\rho^2 + \frac{77253378048000}{13^3}\,\rho + \frac{461060812800}{13^2}.$$
   - **Direct proof of B906 (zero $\gamma$-part of $\det_{14}$):** Because $(R_{16}|_{W_4})^2 = e(\rho) I_4$, the exact
     projector onto the 2-dimensional $+\gamma$ eigenspace $V_2^+(\gamma) = \ker(R_{16}|_{W_4} - \gamma I_4)$ over
     $E = F[\gamma]/(\gamma^2 - e(\rho))$ is $P_+ = \frac{1}{2}\left(I_4 + \frac{\gamma}{e(\rho)} R_{16}|_{W_4}\right)$.
     Direct trace evaluation gives $\mathrm{tr}_F(W_{16} W_{14}) = 0$ and $\mathrm{tr}_F(W_{16} W_{14}^2) = 0$ identically
     in $F$, so both $\mathrm{tr}_E(W_{14}|_{V_2^+}) = 0$ and $\det_E(W_{14}|_{V_2^+}) = \det_{14}(\rho) \in F$ have
     identically zero $\gamma$-component.

## 3. Three independent exact proofs that $\det_{14}(\rho) > 0$ at all three roots

1. **Proof 1 — Completing the square over $\mathbb{Q}$ (global positivity on $\mathbb{R}$):**
   As a quadratic polynomial in $\rho$ over $\mathbb{Q}$, $\det_{14}(\rho) = A\rho^2 + B\rho + C$ has $A = 9084997258444800000 / 13^4 > 0$
   and negative discriminant $B^2 - 4AC = -99106371577736671002624000000 / 13^4 < 0$. Completing the square gives the
   exact rational identity:
   $$\det_{14}(\rho) = \frac{9084997258444800000}{28561}\left(\rho + \frac{13}{235200}\right)^2 + 2727198720 \ge 2727198720 > 0 \qquad \forall\,\rho \in \mathbb{R}.$$
   Thus $\det_{14}(\rho)$ is strictly positive for **every** real number $\rho \in \mathbb{R}$, with an exact integer global
   minimum of $2\,727\,198\,720$.
2. **Proof 2 — Exact resultant / minimal polynomial over $\mathbb{Q}$:**
   The minimal polynomial of $u = \det_{14}(\rho)$ over $\mathbb{Q}$ is
   $$g_3(u) = \mathrm{monic}\,\mathrm{Res}_\rho(\mu(\rho),\, u - \det_{14}(\rho)) = u^3 - 19856793600\,u^2 + 98573063018250240000\,u - 142198242829436706619392000000 = -f_6(\sqrt{-u}).$$
   Because the coefficients of $f_6(t)$ are strictly positive, $g_3(u) < 0$ for all $u \le 0$, so all three real roots
   $u_i = \det_{14}(\rho_i)$ are strictly positive. Likewise, $\mathrm{monic}\,\mathrm{Res}_\rho(\mu(\rho),\, v - e(\rho))$
   has strictly alternating signs $(+, -, +, -)$, certifying $e(\rho_i) > 0$ at all three real roots.
3. **Proof 3 — Exact rational root-isolation intervals (`sympy.Poly.intervals`, $\varepsilon = 10^{-25}$):**
   Isolating the three real roots of $\mu(\rho)$ in exact rational intervals $[a_i, b_i] \subset \mathbb{Q}$ of width $< 10^{-25}$
   gives exact rational lower bounds matching B893's stored floating-point values to every stored digit (`rel_diff = 0.0`):
   - Root 0 ($\rho_0 \approx -1.9380502097204333 \times 10^{-3}$): $\det_{14}(\rho_0) > 3\,854\,784\,701.3353986740 > 0$, $e(\rho_0) > 1\,451\,926\,255\,963.8335 > 0$.
   - Root 1 ($\rho_1 \approx +3.9822150125035273 \times 10^{-4}$): $\det_{14}(\rho_1) > 2\,792\,616\,188.7290024757 > 0$, $e(\rho_1) > 3\,018\,616\,647\,404.4209 > 0$.
   - Root 2 ($\rho_2 \approx +5.6852368717353868 \times 10^{-3}$): $\det_{14}(\rho_2) > 13\,209\,392\,709.9355983734 > 0$, $e(\rho_2) > 283\,511\,130\,354.8228 > 0$.
4. **Modular cross-checks (`q = 40123, 40493, 40583, 40693`):**
   Evaluating $e(\rho)$ and $\det_{14}(\rho)$ modulo $q = 40123$ at the three roots $\rho_q \in \{13418, 23094, 27063\}$ of
   $\mu \bmod 40123$ reproduces B892's exact wall point $(\rho_q, \gamma_q, a_q) = (27063, 13410, 2675)$ where
   $e(27063) \equiv 13410^2 \equiv 36937 \pmod{40123}$ and $-\det_{14}(27063) \equiv -26392 \equiv 2675^2 \pmod{40123}$.

## 4. Consequence for `THEOREM_LEDGER` C25 and `POINT_REGISTER` P-301

C25's clause *"the wall complex in the split frame, at all three roots"* ($a^2 = -\det_{14}(\rho_i) < 0$ while
$\gamma^2 = e(\rho_i) > 0$ at all three real roots of $\mu$) is **confirmed in exact rational arithmetic** from a clean
checkout without `b12_tower.pkl`. P-301 is **DONE**.

## Files

- `verification/regenerate_b12_tower.py` → `b12_tower_regenerated.json`, `regenerate_b12_tower_run.txt`.
- The lock: `tests/test_b1758_c25_block12_pencil_regenerated.py`.

## Seen first

`VERDICT topic-sweep /b12_tower|det_14|det14|B893|B892|C25|block-12/ (full text): 18 of 1528 arcs on main match (NEGATIVE 2, OPEN 1, PROVED 15)`
— among them B854, B877, B892, B893, B906. **The register:** P-301, R70-1 (Review 70). **Literature:** none beyond the record's exact Lie-algebraic centraliser pencil over $\mathbb{Q}[\rho]/\mu(\rho)$.
