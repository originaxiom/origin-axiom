# Full Compact Centralizer Components of the Two Ordered Principal $\operatorname{SU}(2)$ Triples in $E_8$ (`AGY-01b`)

- **Date:** `2026-11-09`
- **Status / Evidence Grade:** `AUTHOR HAND PROOF / UNREVIEWED` (`scientific_execution_authorized = false`; no scientific code, CAS, imports, test collection, or runs executed; formal independent review and scientific admission remain outstanding)
- **Active Microtask:** `AGY-01b` (`RUN_TICKET_AGY_01B.md` at `c57e13613ca6c6e990bcdfc8f54495731ad1f579`, SHA256 `85d24f49a3587227914e6ae4f3b47c22ce7e190ae27a0727c48d023f75cf486a`; `START_HERE.md`, SHA256 `acbfef029a239b0be93f9b0de19d4f013d7232db347cf08bcb85e231013f238f`; `TASKS.json`, SHA256 `e33ec5fe1c4f1cf916db809d71ce9abe1e11d5fe0da962113274081a1d3b2f40`)
- **Accepted Dependencies:**
  - `COMPENSATOR_RANGE_AUDIT.md` (`476d20bbb4a2e52bf1650fd0d8819d6cd869027e`, SHA256 `81b29726b20218ed2625de06369c7a5d55c13427d85d81ed2888d27a3280a0d3`) and `REVIEW_AGY_01A_R1_476D_2026_11_09.md` (`c57e13613ca6c6e990bcdfc8f54495731ad1f579`, SHA256 `3337e40640fc3e70831f256376a7535c892828e4c644a3216b29df5f38ca8c99`)
  - `INPUT_LEDGER.md` (`605294403ecdd26666f3902881558e4bf6b85e93`, SHA256 `98bf93b4be89297901e8f9718f88ea526105b717310df63b75e21deb282713e5`), `MODEL_MANIFEST.md` (`6552aec6894a4a94a2ced785ac3af8c25f801ba8`, SHA256 `811956e0ffc5ca9f141c57e6eb5e98bc576aa5b8e7fe18909c4fc2cd9136ebdb`), `CLAIM_DEPENDENCIES.md` (`43af86dbecb335ddd0952533dc2680d4a4e7f64a`, SHA256 `eb68f876fdf5b842c471738d7fc1c672f685db1a552d30ad669d7f1dba02802a`)
- **Pinned Source Inputs:**
  - `OPEN_PIN2_CORRECTION_BEYOND_THE_CHOSEN_EM_CIRCLE_2026_11_09.md` (`9a2bd40b3cf0a4d675a3c7013f83873d620a7bde`, SHA256 `56b948a9b9b53f5eeec9242c57b3e0dd3d79751195dba1c705118d6060230aa8`)
  - `FULL_E8_COMPENSATOR_LIFT_AND_REGISTER_TRANSPORT.md` (`2f690bc486adf2dfc07dd4fd94bf62b6db27bc86`, SHA256 `6012816683f17ac83e7d3bdb4f6d8b987ec8155ee2caa09ce651dbf0b194ed4c`)
  - `PIN2_COMPENSATOR_COHERENCE_AND_ELECTROMAGNETIC_PHASE.md` (`2f690bc486adf2dfc07dd4fd94bf62b6db27bc86`, SHA256 `fc67d4446b11f54c731b7e7aac56b496e501d5fa397040363de6c8074909a3b9`)
  - `ELECTROWEAK_TWO_TRIPLE_PHYSICAL_KERNEL.md` (`2f690bc486adf2dfc07dd4fd94bf62b6db27bc86`, SHA256 `871529dd81603e1a70126f6ee518ae5c2758c107cf7e9fff62ae96f646a0813f`)
  - Literature references: R. Steinberg, *Torsion in Reductive Groups*, Adv. Math. **15** (1975), 63–92 (Thm. 1.4 / Cor. 1.7); B. McInnes, *The Semispin Groups in String Theory*, `arXiv:hep-th/9906059` (§§II–III)

---

## 1. Duty 1: Precise Definition of the Ordered Two-Triple Centralizer $\mathcal{C} \subset E_8$

Let $E_8$ be the compact, connected, simply connected ($\pi_1(E_8)=1$), centre-free Lie group with compact Lie algebra $\mathfrak{e}_8$ ($248$-dimensional) and compact Hermitian involution $X^\dagger=-X$ on $\mathfrak{e}_8\otimes\mathbb{C}$. The two ordered principal triples $(E_+,E_+^\dagger,H_+)$ and $(E_-,E_-^\dagger,H_-)$ span compact subalgebras $\mathfrak{s}_{\pm}=\operatorname{span}_{\mathbb{R}}\{i H_{\pm},E_{\pm}-E_{\pm}^\dagger,i(E_{\pm}+E_{\pm}^\dagger)\}\cong\mathfrak{su}(2)_{\pm}$, generating connected compact subgroups $S_{\pm}=\exp(\mathfrak{s}_{\pm})\subset E_8$:
```text
s_+=span_R{i*H_+, E_+-E_+^dagger, i*(E_++E_+^dagger)},  s_-=span_R{i*H_-, E_--E_-^dagger, i*(E_-+E_-^dagger)}
S_+=exp(s_+),  S_-=exp(s_-),  C := Z_{E_8}(s_+,s_-) = {g in E_8 : Ad_g(E_+-)=E_+-, Ad_g(E_+-^dagger)=E_+-^dagger, Ad_g(H_+-)=H_+-} = Z_{E_8}(S_+ x S_-)
```
Because $\operatorname{Ad}_g$ on $\mathfrak{e}_8$ is $\mathbb{R}$-linear, its complex-linear extension to $\mathfrak{e}_8\otimes\mathbb{C}$ satisfies $\operatorname{Ad}_g(X^\dagger)=(\operatorname{Ad}_g X)^\dagger$; since $S_{\pm}$ are connected, centralizing $(E_{\pm},E_{\pm}^\dagger,H_{\pm})$ is identical to centralizing $S_+\times S_-$.
- **Distinction from $Z_{E_8}(\operatorname{Spin}(5)_+\times\operatorname{Spin}(5)_-)$:** Since $\mathfrak{s}_{\pm}\cong\mathfrak{so}(3)_{\text{prin},\pm}\subset\mathfrak{so}(5)_{\pm}$ has dimension $3<10$, only $Z_{E_8}(\operatorname{Spin}(5)_+\times\operatorname{Spin}(5)_-)\subseteq\mathcal{C}$ is immediate; equality is proved in Duty 3 below.
- **Distinction from normalizer:** Elements exchanging the two triples (such as the source compensator $A$ with $\operatorname{Ad}_A(H_+,H_-)=(H_-,H_+)$) belong to the normalizer $N_{E_8}(S_+\times S_-)$, not to $\mathcal{C}$.

---

## 2. Duty 2: Faithful Identity $\exp(i\pi H_+)=\mathrm{Zeta}$ and Group-Level Reduction $E_8\to\operatorname{Ss}(16)$

In `FULL_E8_COMPENSATOR_LIFT_AND_REGISTER_TRANSPORT.md` (§4), $H_+$ has principal spin-$2$ eigenvalues $(-4,-2,0,2,4)$ on $V_{5,+}$ and $0$ on $V_{5,-}\oplus V_6$. In an orthogonal Cartan basis of $\mathfrak{so}(16)=\mathfrak{so}(V_{5,+}\oplus V_{5,-}\oplus V_6)$, $\frac{1}{2}H_+$ has rotation frequencies $(2,1,0,0,0,0,0,0)$:
```text
(1/2)*H_+ ~ (2,1,0,0,0,0,0,0) in t_{D_8}:  <(2,1,0^6), alpha> in Z  (for all 120 integer D_8 roots alpha)
<(2,1,0^6), (1/2)(eps_1,...,eps_8)> = eps_1 + eps_2/2 in Z + 1/2  (for all 128 half-roots)
==>  exp(i*pi*H_+)|_120 = +1,  exp(i*pi*H_+)|_128 = -1  ==>  exp(i*pi*H_+) = Zeta = exp(i*pi*H_-) in E_8
g in C  ==>  Ad_g(H_+)=H_+  ==>  g*Zeta*g^-1 = g*exp(i*pi*H_+)*g^-1 = exp(i*pi*H_+) = Zeta  ==>  C subset Z_{E_8}(Zeta)
```
Every $g\in\mathcal{C}$ therefore centralizes the involution $\mathrm{Zeta}\in S_+$. By the Borel–Steinberg theorem (Steinberg 1975, Thm. 1.4 / Cor. 1.7: the centralizer of any single torus element in a compact, connected, simply connected Lie group is connected), $Z_{E_8}(\mathrm{Zeta})$ is **connected**. Since the $+1$ eigenspace of $\operatorname{Ad}_{\mathrm{Zeta}}$ on $\mathfrak{e}_8=120_{\mathfrak{so}(16)}\oplus 128_{S_+}$ is $120_{\mathfrak{so}(16)}$, connectedness yields $Z_{E_8}(\mathrm{Zeta})=\exp(120_{\mathfrak{so}(16)})=\operatorname{Ss}(16)=\operatorname{Spin}(16)/\langle\omega_{16}\rangle$ globally:
```text
Z_{E_8}(Zeta) = Ss(16) = Spin(16)/{1,omega_16}   ==>   C = Z_{Ss(16)}(S_+ x S_-) subset Ss(16)
```

---

## 3. Duty 3: Lift to $\operatorname{Spin}(16)$, Real-$16$ Schur Commutant, and Connectedness Commutation Lift

Retain the `AGY-01a-r1` convention on $\mathbb{R}^{16}=V_{5,+}\oplus V_{5,-}\oplus V_6$: $W=e_1^+\cdots e_5^+$, $U=e_1^-\cdots e_5^-$, $\omega_{10}=W U=-C$, $\omega_6=f_1\cdots f_6=-C_6$, and $\omega_{16}=\omega_{10}\omega_6=C C_6$, with double covers $\pi_{E_8}:\operatorname{Spin}(16)\to\operatorname{Ss}(16)$ ($\ker\pi_{E_8}=\{1,\omega_{16}\}$) and $q_{16}:\operatorname{Spin}(16)\to\operatorname{SO}(16)$ ($\ker q_{16}=\{1,-1_{\operatorname{Spin}(16)}\}$). Let $\widetilde{S}_{\pm}=\exp(\mathfrak{s}_{\pm})\subset\operatorname{Spin}(V_{5,\pm})\subset\operatorname{Spin}(16)$ be the unique connected lifts of $S_{\pm}$, and set $\widetilde{\mathcal{C}}:=\pi_{E_8}^{-1}(\mathcal{C})\subseteq\operatorname{Spin}(16)$.
1. **Why orthogonal commutation lifts without sign or spinor obstruction:**
   For any $\tilde{g}\in\operatorname{Spin}(16)$, the group commutator maps $\tilde{s}\mapsto\tilde{g}\tilde{s}\tilde{g}^{-1}\tilde{s}^{-1}$ and $s\mapsto\pi_{E_8}(\tilde{g})s\pi_{E_8}(\tilde{g})^{-1}s^{-1}$ are continuous maps from the **connected** group $\widetilde{S}_+\times\widetilde{S}_-$ into the discrete central kernels $\ker(q_{16})=\{1,-1_{\operatorname{Spin}(16)}\}$ and $\ker(\pi_{E_8})=\{1,\omega_{16}\}$ Whenever $q_{16}(\tilde{g})\in\operatorname{SO}(16)$ commutes with $q_{16}(\widetilde{S}_+\times\widetilde{S}_-)$ on $\mathbb{R}^{16}$, $\tilde{g}\tilde{s}\tilde{g}^{-1}\tilde{s}^{-1}$ takes values in $\{1,-1_{\operatorname{Spin}(16)}\}$, equals $1$ at $\tilde{s}=1$, and by connectedness of $\widetilde{S}_+\times\widetilde{S}_-$ is **identically $1$** in $\operatorname{Spin}(16)$ (including on the faithful spinor representation $128_{S_+}$) and in $\operatorname{Ss}(16)\subset E_8$:
```text
widetilde(C) = pi_E8^-1(C) = Z_{Spin(16)}(widetilde(S)_+ x widetilde(S)_-) = q_16^-1(Z_{SO(16)}(q_16(widetilde(S)_+ x widetilde(S)_-)))
```
2. **Real-$16$ orthogonal commutant:**
   Under $q_{16}(\widetilde{S}_+\times\widetilde{S}_-)\cong\operatorname{SO}(3)_{\text{prin},+}\times\operatorname{SO}(3)_{\text{prin},-}$, $\mathbb{R}^{16}$ decomposes into three pairwise non-isomorphic subspaces: $V_{5,+}=(5,1)$, $V_{5,-}=(1,5)$, and $V_6=6\times(1,1)$. Because each spin-$2$ carrier $V_{5,\pm}\otimes\mathbb{C}$ has five multiplicity-one $H_{\pm}$-weights $(-4,-2,0,2,4)$, Schur's Lemma gives $\operatorname{End}_{\mathfrak{s}_{\pm}}(V_{5,\pm})=\mathbb{R} I_5$ and zero intertwining maps between $V_{5,+}$, $V_{5,-}$, and $V_6$. Imposing $O^T O=I_{16}$ and $\det(O)=+1$ yields the $4$-component group in $\operatorname{SO}(16)$:
```text
Z_{SO(16)}(q_16(widetilde(S)_+ x widetilde(S)_-)) = { diag(eps_+*I_5, eps_-*I_5, M_6) : eps_+,eps_- in {+-1}, M_6 in O(6), det(M_6)=eps_+*eps_- }
```
   Since $\pm I_5$ commutes with all of $\operatorname{SO}(5)_{\pm}$, every such $O$ centralizes $\operatorname{SO}(5)_+\times\operatorname{SO}(5)_-$, proving $\mathcal{C}=Z_{E_8}(\operatorname{Spin}(5)_+\times\operatorname{Spin}(5)_-)$.

---

## 4. Duty 4: Transport Through $\operatorname{Ss}(16)$, Component Collapse $4\to 2$, and Explicit Pin Isomorphism

Lift the four $\operatorname{SO}(16)$ components $(\epsilon_+,\epsilon_-)\in\{\pm 1\}^2$ via $q_{16}^{-1}$ to $\widetilde{\mathcal{C}}\subset\operatorname{Spin}(16)$:
- Recall $\omega_6=f_1\cdots f_6=\exp(\frac{\pi}{2}(f_1 f_2+f_3 f_4+f_5 f_6))\in\operatorname{Spin}(6)$ lies in the **connected** subgroup $\operatorname{Spin}(6)\subset\operatorname{Spin}(16)$ and satisfies $\omega_6^2=(-1)^{15}=-1_{\operatorname{Spin}(16)}\in\operatorname{Spin}(6)$ and $q_{16}(\omega_6)=\operatorname{diag}(+I_5,+I_5,-I_6)$. Thus both sheets of $q_{16}^{-1}(\operatorname{diag}(+I_5,+I_5,\operatorname{SO}(6)))$ lie in the single connected group $\operatorname{Spin}(6)$.
- Since $q_{16}(\omega_{10})=\operatorname{diag}(-I_5,-I_5,+I_6)$ and $\omega_{10}=\omega_{16}\omega_6^{-1}$ with $\omega_6^{-1}=-\omega_6\in\operatorname{Spin}(6)$, the four connected components of $\widetilde{\mathcal{C}}\subset\operatorname{Spin}(16)$ are:
```text
widetilde(C)_{(+1,+1)} = Spin(6),                       widetilde(C)_{(-1,-1)} = omega_10*Spin(6) = C*Spin(6) = omega_16*Spin(6)
widetilde(C)_{(+1,-1)} = U*Pin_-(6) = h_1*Spin(6),      widetilde(C)_{(-1,+1)} = W*Pin_-(6) = omega_10*h_1*Spin(6) = omega_16*h_1*Spin(6)
```
Under $\pi_{E_8}:\operatorname{Spin}(16)\to\operatorname{Ss}(16)\subset E_8$, $\ker(\pi_{E_8})=\{1,\omega_{16}\}$ has trivial intersection with $\operatorname{Spin}(6)\sqcup h_1\operatorname{Spin}(6)$ (since $\omega_{16}=\omega_{10}\omega_6\notin\operatorname{Cl}(V_6)\cup U\operatorname{Cl}(V_6)$) and maps $\omega_{16}\mapsto 1$. Consequently, $\widetilde{\mathcal{C}}_{(-1,-1)}$ merges with $\widetilde{\mathcal{C}}_{(+1,+1)}$ and $\widetilde{\mathcal{C}}_{(-1,+1)}$ merges with $\widetilde{\mathcal{C}}_{(+1,-1)}$, leaving **exactly two connected components** in $\mathcal{C}\subset E_8$:
```text
C = C_0 sqcup C_1,   C_0 = pi_E8(Spin(6)) ~= Spin(6) ~= SU(4),   C_1 = h_1*C_0 = pi_E8(U*Pin_-(6)),   pi_0(C) = C/C_0 ~= Z_2
C = -omega_10 = pi_E8(omega_6) = -C_6 in Z(C_0),   Zeta = C^2 = pi_E8(-1_{Spin(16)}) = pi_E8(omega_6^2) in Z(C_0)
h_1 = U*f_1 in C_1:   h_1^2 = Zeta in Z(C_0),   h_1*g_0*h_1^-1 = f_1*g_0*f_1^-1,   (h_1*g_0)*(h_1*g_0') = Zeta*(f_1*g_0*f_1^-1)*g_0' in C_0
```
In the declared Euclidean Clifford convention ($u^2=+1$ on $V_6$, $\operatorname{Pin}(6)=\operatorname{Spin}(6)\sqcup\operatorname{Pin}_-(6)\subset\operatorname{Cl}(V_6)^\times$), the map $\Phi_{\operatorname{Pin}}:\operatorname{Spin}(6)\sqcup U\operatorname{Pin}_-(6)\to\mathcal{C}$ given by $g_0\mapsto\pi_{E_8}(g_0)$ and $U x\mapsto\pi_{E_8}(U x)$ is a **bijective group isomorphism**, twisting the odd-odd product by $(U x)(U y)=-U^2 x y=-x y\mapsto\mathrm{Zeta}\,\pi_{E_8}(x y)$ because $U$ anticommutes with $\operatorname{Pin}_-(6)$.

---

## 5. Duty 5: Location of Accepted Witnesses and Exact Component-Selection Duty

1. **Identity component $\mathcal{C}_0=\pi_{E_8}(\operatorname{Spin}(6))\cong\operatorname{SU}(4)$:** Contains the centre $Z(\mathcal{C}_0)=\langle C\rangle=\{1,C,\mathrm{Zeta},C^{-1}\}\cong\mathbb{Z}_4$ and the connected $\operatorname{U}(3)$ electromagnetic $\operatorname{Pin}(2)$ corrections $h_4=\exp(2\pi i(1/4,1/4,1/4)_{D_3})$ and $\mathrm{Zeta}\,h_4$ (plus their $\mathcal{C}_0$-conjugates). Every $g\in\mathcal{C}_0$ acts trivially on $(45,1)$ and preserves the internal $\operatorname{Spin}(10)\times\operatorname{Spin}(6)$ summands $(16,4)$ and $(\overline{16},\overline{4})$.
2. **Outer component $\mathcal{C}_1=h_1\mathcal{C}_0=\pi_{E_8}(U\operatorname{Pin}_-(6))$:** Contains **both** the passing witness $h_1=U f_1$ ($(A h_1)^2=K_\pi$, fixing $\mathfrak{so}(5)\subset\mathfrak{so}(6)$) **and** the obstructed product $h_3=U f_1 f_2 f_3=h_1(f_2 f_3)\in h_1\mathcal{C}_0$ ($(A h_3)^2=\mathrm{Zeta}\,K_\pi\neq K_\pi$ since $(f_2 f_3)^2=-1_{\operatorname{Spin}(16)}$ cancels $h_1^2=-1_{\operatorname{Spin}(16)}$), as well as $W f_1=\omega_{16}h_1(-\omega_6)\mapsto h_1(-\omega_6)\in\mathcal{C}_1$. Every $g\in\mathcal{C}_1$ fixes $\mathfrak{so}(5)_+\oplus\mathfrak{so}(5)_-$, negates $V_{5,+}\otimes V_{5,-}\subset(45,1)$, acts on $A_3=\mathfrak{so}(6)$ by an outer reflection $\operatorname{Ad}_{M_6}$ ($\det M_6=-1$), and swaps the internal summands $(16,4)\leftrightarrow(\overline{16},\overline{4})$ on $128$.
3. **Exact component-selection duty:** Because $\pi_0(\mathcal{C})=\{\mathcal{C}_0,\mathcal{C}_1\}\cong\mathbb{Z}_2$ has **no third component**, selecting the connected component $h\in\mathcal{C}_0$ is a **strict binary choice** and is **globally equivalent across all of $\mathcal{C}$** to requiring trivial action on $(45,1)$ or preservation of the internal $(16,4)$ summand under core transport. Full conjugacy classification of all solutions to $(A h)^2=K_\pi$ inside $\mathcal{C}_1$, together with the physical gauge/matter dictionary, operator domains, and 4D weak chirality, remain separate downstream duties.
4. **Prospective controls (unrun):** Once separately admitted, an executable check should verify $\exp(i\pi H_+)=\mathrm{Zeta}$ on $248$, confirm $\pi_{E_8}(\omega_{10})=\pi_{E_8}(-\omega_6)\in\mathcal{C}_0$ and $\pi_{E_8}(W f_1)=\pi_{E_8}(U f_1(-\omega_6))\in\mathcal{C}_1$, and test component multiplication on $120\oplus 128$.
