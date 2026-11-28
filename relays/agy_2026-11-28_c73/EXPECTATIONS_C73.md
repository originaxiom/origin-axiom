# Pre-Registered Expectations — Card AGY-C73 (2026-11-28)

**Seat:** `agy` (`fam3-v1-high-01`, branch `agy/cusp-action-2026-11-20`)
**Mode:** Pure listening (`0 of 19` empirical inputs; order-`30` line held per `M18` item `5`)
**Premises on `main`:** `B1987`, `B1993`, `B1996`, `B1997`, `B1998`, `B2004`, `B2008`

## Blind-Spot Question Asked Before Computation

Across `B1993`, `B1996`, `B1998`, and `B2008`, four pieces of structure were observed inside finite boxes or sparse Arnoldi runs whose exact algebraic laws were sitting in plain sight:
1. Why do all nonzero integer solutions of $X_{-2} : x^2 + y^2 + z^2 = x y z$ over **all** of $\mathbb{Z}^3$ (`beyond B1993's box max <= 3000 and B1998's box max <= 400`) collapse
to strictly two $\langle L, R \rangle$-orbits (`positive + one single mixed-sign orbit`) while avoiding $(0, 0, 0) \bmod 2$ in exact bijection with the four $\mathrm{SL}(2,
\mathbb{Z})$ spin lifts?
2. Why does the $2$-adic cusp neighbourhood $N_{2^k} \subset (2\mathbb{Z}/2^k\mathbb{Z})^3$ (`B1998`) drop from maximum orbit size `24` at `mod 8` to `12` at `mod 16` and then lock
at `24` (`rate 1/\sqrt{2}` over $\mathbb{Q}(\sqrt{-7})$) for **every** $k \ge 5$ up to $\mathbb{Z}_2$?
3. What are the exact algebraic identities of `B1987` and `B1996`'s unidentified $5$-adic and $7$-adic cusp decay eigenvalues (`mod 125`, `mod 343`, and `mod 625`), why do the $p
\ge 5$ cusp neighbourhoods break into multiple sheets instead of one giant orbit, and do they also live over prime-power roots of unity like `B1997`'s ninth roots at $p = 3$?
4. Does `B2008`'s discrete mirror lock $\tau(x, y, z) = (y, x, z)$ hold identically on the analytic coordinate ring $\mathbb{C}[X_\omega]$ (`closing B2008 Open #2 / NI-4 on main`),
while acting with opposite sign (`-1`) on the canonical holomorphic Goldman-Poincare two-form $\Omega_{X_\omega} = \frac{dx \wedge dy}{2z - x y}$?

## Falsifiable Pre-Registered Claims (`E1`–`E4`)

- **`E1` (Global All-$\mathbb{Z}^3$ Orbit & Spin-Parity Theorem on $X_{-2}(\mathbb{Z})$, Closing `B1993` Open #2 & `B1998` Post-Hoc Parity Law):**
  1. Modulo $3$, $x^2 + y^2 + z^2 \equiv x y z \pmod 3$ has unique solution $(0, 0, 0) \in \mathbb{F}_3^3$, forcing $3 \mid x, y, z$ globally on $X_{-2}(\mathbb{Z})$.
  2. Every nonzero $v = (x, y, z) \in X_{-2}(\mathbb{Z})$ satisfies $x y z = x^2 + y^2 + z^2 > 0$, so its sign vector $\mathrm{sgn}(v)$ lies in the Klein group $V_4 = \{(+,+,+),
    (+,-,-), (-,+,-), (-,-,+)\}$, and $|g(v)| = g(|v|)$ holds identically on $X_{-2}(\mathbb{Z}) \setminus \{0\}$ for all $g \in \{L, R, L^{-1}, R^{-1}\}$.
  3. Strict $\ell^1$-norm Vieta descent reduces every $v \in X_{-2}(\mathbb{Z}) \setminus \{0\}$ under $\langle L, R \rangle$ to one of the four minimal vectors $|v| = (3, 3, 3)$
    with $\mathrm{sgn}(v) \in V_4$, and the single word $M = L^{-1} \circ R \in \langle L, R \rangle$ cycles $(3, -3, -3) \mapsto (-3, 3, -3) \mapsto (-3, -3, 3) \mapsto (3, -3,
    -3)$ while $\langle L, R \rangle$ preserves $(+, +, +)$. Hence $X_{-2}(\mathbb{Z})$ has **strictly three** $\langle L, R \rangle$-orbits over all of $\mathbb{Z}^3$: $\{(0, 0,
    0)\}$, $\mathrm{Orb}(3, 3, 3)$, and $\mathrm{Orb}(3, -3, -3)$.
  4. Writing $(x, y, z) = (3a, 3b, 3c)$, $2$-adic descent modulo $4$ proves $(a, b, c) \not\equiv (0, 0, 0) \pmod 2$ globally, and modulo $2$ reduction forces $(a, b, c) \bmod 2
    \in \{(1, 1, 1), (0, 1, 1), (1, 0, 1), (1, 1, 0)\}$, in $\langle L, R \rangle$-equivariant $1 + 3$ bijection with the four character lifts $\mathrm{Hom}(F_2, \{\pm 1\}) \cong
    V_4$.

- **`E2` (All-$k$ $2$-Adic Cusp Closure Theorem to $\mathbb{Z}_2$, Proving `B1998` for All $k \ge 3$):**
  1. Because $u^2 + v^2 + w^2 \equiv 2^r u v w \pmod 4$ ($r \ge 1$) admits zero primitive solutions in $(\mathbb{Z}/4\mathbb{Z})^3$, every $(x, y, z) \in N_{2^k}$ ($k \ge 3$)
    satisfies $\min(v_2(x), v_2(y), v_2(z)) \ge \lceil (k - 1)/2 \rceil$, giving exact cardinalities $|N_{2^{2m}}| = 2^{3m}$, $|N_{2^{2m+1}}| = 2^{3m+2}$, and projective limit
    $N_{\mathbb{Z}_2} = \varprojlim N_{2^k} = \{(0, 0, 0)\}$.
  2. For every even $k = 2m \ge 4$, $x z \equiv y z \equiv 0 \pmod{2^{2m}}$ on $N_{2^{2m}}$, so $L(x, y, z) = (x, z, -y)$ and $R(x, y, z) = (z, y, -x)$ generate $S_4$ (`with
    maximum orbit 12 at k = 4 because 2 == -2 mod 4 on 2Z/16Z, and 24 for every m >= 3`). For every odd $k = 2m + 1 \ge 3$, writing $(x, y, z) = 2^m(u, v, w)$ reduces $x z \equiv
    2^{2m}(u w \bmod 2) \pmod{2^{2m+1}}$ with $u + v + w \equiv 0 \pmod 2$, locking the maximum orbit size at **strictly `24`** and the slowest non-undamped $W_+$ modulus at
    $\sqrt{2}$ (`via x^2 \pm x + 2` over $\mathbb{Q}(\sqrt{-7})$) for **all** $k \ge 3$ (`except size 12 at k = 4`, still with slowest modulus $\sqrt{2}$).

- **`E3` (Hidden $p$-Adic Casimir Sheet Invariant & Exact Cyclotomic Chebyshev Law on the $5$- and $7$-Towers, Resolving `B1996` Open #3 & `B1998` Open #1):**
  1. For every prime $p$ and $k \ge 2$, $\eta_k(x, y, z) = \frac{\tilde{x}^2 + \tilde{y}^2 + \tilde{z}^2 - \tilde{x}\tilde{y}\tilde{z}}{p^k} \bmod p \in \mathbb{F}_p$ is
    independent of the lift $(\tilde{x}, \tilde{y}, \tilde{z}) \in (p\mathbb{Z})^3$ and strictly $(L, R)$-invariant (`partitioning N_{343} \setminus 7 N_{49} at p = 7, k = 3 into 2
    * 7 = 14 orbits of 1,176, and combining with the F_5 null-cone double sheet at p = 5 to partition N_{125} \setminus 5 N_{25} into 25 orbits of 120 and N_{625} \setminus 5
    N_{125} into 25 orbits of 3,000`).
  2. At $k = 3$ (`mod p^3`) for $p \in \{3, 5, 7\}$, the slowest non-undamped $W_+$ eigenvalue on each top cusp orbit satisfies the universal Chebyshev reciprocal quartic $x^4 - (1
    + 4\cos(\pi/p))x^2 + 4 = 0$ over $\mathbb{Q}(\cos(2\pi/p))$: complex of modulus $\sqrt{2}$ at $p = 3$ (`x^4 - 3x^2 + 4`), real root of irreducible $P_{5,3}(x) = x^8 - 4x^6 +
    7x^4 - 16x^2 + 16$ in $(1677861/10^6, 1677862/10^6)$ at $p = 5$ (`mod 125`), and real root of irreducible $P_{7,3}(x) = x^{12} - 5x^{10} + 11x^8 - 27x^6 + 44x^4 - 80x^2 + 64$
    in $(1855165/10^6, 1855166/10^6)$ at $p = 7$ (`mod 343`).
  3. At $p = 5, k = 4$ (`mod 625`, orbit size `3,000`), $\mathrm{Deck}(\mathcal{O}_{625}/\mathcal{O}_{125}) \cong (\mathbb{Z}/5\mathbb{Z})^2$ is an exact regular abelian cover of
    order `25`, and exact `sp.ZZ` factorization proves `B1996`'s unidentified `mod 625` eigenvalue lies in $(1989420/10^6, 1989421/10^6)$ as the largest real root of the
    irreducible degree-`40` polynomial $P_{5,4}(x) \in \mathbb{Z}[x]$ whose reciprocal Chebyshev variable $v = x^2 + 4/x^2 - 1$ satisfies $v^5 - 20v^3 + 80v = 64\cos(\pi/5)$, i.e.
    $x^2 + 4/x^2 = 1 + 4\cos(\pi/25)$ over **twenty-fifth roots of unity** $\mathbb{Q}(\cos(2\pi/25))$ (`with all five remaining cyclic lines of (\mathbb{Z}/5\mathbb{Z})^2 bounded
    at modulus \sqrt{2}`).

- **`E4` (Analytic Coordinate-Ring `NI-4` Lock & $\tau$-Odd Goldman-Poincare Two-Form on $X_\omega$, Closing `B2008` Open #2 & Illuminating Open #1):**
  1. On the affine coordinate ring $\mathcal{R} = \mathbb{Q}(\omega)[x, y, z]/(x^2 + y^2 + z^2 - x y z)$ of $X_\omega$, the pullback $\tau^*$ of $\tau(x, y, z) = (y, x, z)$
    satisfies $\tau^* \circ C^* \circ \tau^* = (C^{-1})^*$, $\tau^* \circ \Pi_1 = \Pi_2 \circ \tau^*$ (`for \Pi_q = \frac{1}{3}(I + \omega^{-q} C^* + \omega^{-2q}(C^2)^*)`), and
    $[\tau^*, \mathcal{W}_6^*] = 0$ identically on $\mathcal{R}$, locking the analytic charged polynomial sectors $\mathcal{R}_{q=1} \cong \mathcal{R}_{q=2}$ at every degree
    filtration.
  2. Conversely, the canonical holomorphic Goldman-Poincare two-form $\Omega_{X_\omega} = \frac{dx \wedge dy}{2z - x y}$ on $X_\omega$ is strictly even (`+1`) under all
    orientation-preserving modular moves $L, R, C, \sigma$ (`L^*\Omega_{X_\omega} = R^*\Omega_{X_\omega} = C^*\Omega_{X_\omega} = +\Omega_{X_\omega}`) and strictly **odd** (`-1`)
    under the mirror swap (`\tau^*\Omega_{X_\omega} = -\Omega_{X_\omega}`), providing the exact intrinsic geometric carrier of the orientation sign inside `<G_k, \tau>^{ab} \cong
    \mathbb{Z}_2 \times \mathbb{Z}_2$.

## Planted-Fault Controls (`PF1`–`PF5`)

- `PF1`: Mutate $M = L^{-1} \circ R$ to $L \circ R$ (`fails mixed-sign root cycling at |(x,y,z)| = (3,3,3)`).
- `PF2`: Drop the mod-$4$ quadratic obstruction in `E2` (`falsely allows primitive 2-adic lifts and orbit growth > 24`).
- `PF3`: Replace $1 + 4\cos(\pi/5)$ by $1 + 2\cos(\pi/5)$ in $P_{5,3}(x)$ (`breaks sp.ZZ nullity on \mathcal{O}_{125}`).
- `PF4`: Replace $\cos(\pi/25)$ by $\cos(2\pi/25)$ (`125 vs 157 middle coefficient`) in $P_{5,4}(x)$ (`selects subleading root in (1957019/10^6, 1957020/10^6) instead of top root in (1989420/10^6, 1989421/10^6)`).
- `PF5`: Flip $\tau^* \Omega_{X_\omega} = -\Omega_{X_\omega}$ to $+\Omega_{X_\omega}$ (`violates symbolic Jacobian pullback modulo x^2 + y^2 + z^2 - x y z`).
