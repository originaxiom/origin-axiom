# Transition-Resolved Coefficient Roster on the Coherent Phases (`AGY-02a`)

- **Date:** `2026-11-09`
- **Status / Evidence Grade:** `AUTHOR HAND DERIVATION / UNREVIEWED` (`scientific_execution_authorized = false`; no scientific code, CAS, imports, collection, or runs; formal independent review and admission owed)
- **Active Microtask:** `AGY-02a` (`RUN_TICKET_AGY_02A.md` at `3234bbdd76245bcd484cbbf1bae24aab84d281da`, SHA256 `4e26a293681cd9246c7469d96fe5ef68d4455a5920f744a4a8c7f3f4136f5560`; `START_HERE.md`, SHA256 `ec0304baf51c03d1ade7a3295254eaf60ae887ee45febb9ec86984c60a86bce3`; `TASKS.json`, SHA256 `cbaf8f72a2c0b22196a92aa6a7c1beee58c791e7bf1a3b3cbfc2374442dd79bb`; `REVIEW_AGY_01D_1C6C_2026_11_09.md`, SHA256 `9b85f5b39d41bb8c148aeb4491c70bbfdaf4e8c50da1c938d3faa62263ec0609`)
- **Baseline Pins:** Physical `01d425c3c10399449de4121e53be9c064bbcc8b8` (extended through `3234bbdd76245bcd484cbbf1bae24aab84d281da`); Canonical GENESIS `217e37c4f37bd80998f3c3e10cad358023f58114`
- **Accepted / Supported Campaign Dependencies:**
  - `CENTRALIZER_COMPONENTS.md` (`a0e86b7164e401498869fce468a5fcfad140ca28529e86d721b3dffab7673075`), `COHERENT_PHASE_CLASSES.md` (`9b0ec09b6b5effbfd5853dcd599f95ff3bb2106d39c1a2146c226b069630f6d0`), `REGISTER_TO_GRADING.md` (repaired in `AGY-02a`, `965c3652ce550b448e3aa37e0b397f5492339882ce18b38a94f4bdf36addf008`), `COMPENSATOR_RANGE_AUDIT.md` (`81b29726b20218ed2625de06369c7a5d55c13427d85d81ed2888d27a3280a0d3`), `INPUT_LEDGER.md` (`98bf93b4be89297901e8f9718f88ea526105b717310df63b75e21deb282713e5`)
- **Pinned Operator & Word-Architecture Sources:**
  - `weave_physical_mass_2026_10_08/PROOF.md` (`04fbb6b7ddc23fe2ae56aa24f3df6e9a710f6278363213b8a509b06ace83ef8d`)
  - `weave_curved_action_2026_10_08/PROOF.md` (`c505823ce2b934b9737780acf3d6bbbeeb8482613b7ecc76a2ece58b1c2ebc4f`)
  - `COUPLED_QUATERNION_STATIONARY_BUNDLE_AND_CUSP_LAW.md` (`221a7cd2dce2ff7dec0b135c348b7bb52e15bc27e5563d420756fbe31f9978a1`)
  - `COUPLED_HALF_ROOT_KERNEL_AND_CORE_LIFT_SENSITIVITY.md` (`789adf7544bf5c679305aa8b9ba7525b6375155b026c839e01c34c281be23875`)
  - `ELECTROWEAK_TWO_TRIPLE_PHYSICAL_KERNEL.md` (`871529dd81603e1a70126f6ee518ae5c2758c107cf7e9fff62ae96f646a0813f`)
  - `COUPLED_UP_SECTOR_PARABOLIC_COUNT_2026_11_08.md` (`477743caf7f2edc91117ed9f7ef24efcb834c5a8968bfd19ffc46865d75d9ff9`)
  - `UP_SECTOR_EXPLORATORY_NEUTRAL_NOTES_2026_11_08.md` (`c4110e34a25e37d72dd9ec1823cb01320071cb6ae17608d68c3a658bd38a9de0`)
  - `QUARTER_PHASE_CHARACTER_BRIDGE_AND_COHERENT_WORD_CONTROL_2026_11_09.md` (`83453638584cb34219ca389bfb7a753259fd3a1f9f2e651ada07cfbe3002a733`)

---

## 1. Duty 1: Baseline Stationary Saddle and Why Zero Extra Wilson ($W = 1$) Is Fixed

Fix the complete finite-area once-punctured elliptic curve $\Sigma_{1,1}$ ($\pi_1(\Sigma_{1,1})=\langle a,b\rangle\cong F_2$, oriented cusp loop $c=[a,b]=a b a^{-1}b^{-1}$) with curvature $-1/\ell^2$ (`weave_curved_action_2026_10_08/PROOF.md`), extending spin line $S$ ($S^2\cong K_{\Sigma_{1,1}}$, peripheral cusp sign $-1$, compact order-two spin character $\eta:F_2\to\{\pm 1\}$, $\eta(c)=+1$), natural slot densities $(\Omega^2,1/2,\Omega,\Omega)$, flat quaternion flavour bundle $F$ ($\operatorname{Hol}_F=\rho:F_2\to Q_8\subset\operatorname{SU}(2)$, $\rho(a)=F_i=\operatorname{diag}(i,-i)$, $\rho(b)=F_j=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$, $\rho(c)=-I_2$), spin connection $A_{\text{spin}}=s_{\text{spin}}H/2$ ($H=H_++H_-$), and balanced two-triple scalar saddle:
```text
Phi_0 = (q_hat, r_hat) = (E, G)/(2*sqrt(2)*ell) = ((E_+ + E_-), (E_+ - E_-))/(2*sqrt(2)*ell),   F_spin/dvol + [q_hat, q_hat^dagger] + [r_hat, r_hat^dagger] = 0
```
- **Why zero extra Wilson ($W=1$) is the mandatory phase-comparison baseline:**
  In the connected $G_0=\operatorname{Spin}(6)\cong\operatorname{SU}(4)$ centralizer with Cartan generators $J_1=f_1 f_2, J_2=f_3 f_4, J_3=f_5 f_6$, the previously explored order-three electromagnetic Wilson line $W_{\text{em}}=\exp(\frac{2\pi}{3}(J_1+J_2+J_3))\in G_0$ commutes with $D_5$ and with the connected phase $h_4=\exp(-\frac{\pi}{4}(J_1+J_2+J_3))$, **but does NOT commute with the outer phase $h_1=\pi_{E_8}(U f_1)\in s G_0$**:
```text
tau(J_1, J_2, J_3) = (-J_1, J_2, J_3)  ==>  h_1 * W_em * h_1^-1 = exp((-4*pi/3)*J_1) * W_em != W_em   (since exp((-4*pi/3)*J_1) != 1 on 6 and 4 of A_3)
```
  Any extra Wilson factor commuting with $K_{h_1}$ must lie in $G_0^\tau=\operatorname{Spin}(5)$ ($J_1=0$). Setting $W=1$ compares the connected phase representative $h_4\in\mathcal{O}_0$ and the outer phase representative $h_1\in\mathcal{O}_1$ on an identical footing without importing a $G_0$-only symmetry breaking.

---

## 2. Duty 2: Four Physical Left Weyl Slots, Trace-Dual Target, Core Gluing, and Peripheral Sign

The physical fermion field (`weave_physical_mass_2026_10_08/PROOF.md` §1–2, `weave_curved_action_2026_10_08/PROOF.md` §3–4) consists of **four independent left-handed Weyl coefficients** $\psi=(\lambda,a,u,v)$ valued in $\mathfrak{e}_8$: the scalar gaugino $\lambda$, the $(0,1)$-form chiral multiplet $a$, and the flavour-doublet $(1,0)$-spinor multiplets $(u,v)^T$. No right-handed antiparticles are added as independent left fields. On a simultaneous $(H_+,H_-)$ weight space with $H_\pm=2 m_\pm$ and integer total weight $m:=m_++m_-\in\mathbb{Z}$ ($[H/2,\cdot]=m$), the local spin-gauge trivialization (`weave_curved_action_2026_10_08/PROOF.md` §3) and trace-dual isometries $U_{\text{in}},U_{\text{out}}$ (`weave_physical_mass_2026_10_08/PROOF.md` §2) are:
```text
U_in(lambda, a, u, v) = ((a, u, v),  i*Omega^2*lambda/sqrt(2)),     U_out(g, p_1, p_2, t) = (g,  2*i*t,  p_2/Omega,  -p_1/Omega)
M(lambda, a, u, v) = (U_out o T o U_in)(lambda, a, u, v) = (D_0^dagger x,  2*i*t + sqrt(2)*D_z lambda,  p_2/Omega - sqrt(2)*i*[q^dagger, lambda],  -p_1/Omega - sqrt(2)*i*[r^dagger, lambda])
D_0^dagger x = -[D_z a - 2*i*Omega*([q^dagger, u] + [r^dagger, v])]/(sqrt(2)*Omega^2),   p_1 = D_bar u + i*[q, a],   p_2 = D_bar v + i*[r, a],   t = [q, v] - [r, u]
```
For each weight $m=m_++m_-\in\mathbb{Z}$ and coherent core holonomy $K_h:F_2\to E_8$ ($K_h(a)=X=A h$, $K_h(b)=Y=D A h$), the four input slots and four conjugate-left output slots have spin powers, core transitions ($\gamma\in F_2$), and cusp transition ($c=[a,b]$):
```text
Input slots  (lambda, a, (u,v)^T):                     (S^-m,   S^(-2-m),   S^(1-m) tensor F)
Output slots (g, 2it, (p_2/Omega, -p_1/Omega)^T):      (S^(1-m), S^(-1-m),  S^(-m) tensor F_bar)
Core (gamma in F_2):   (lambda, a) |--> Ad_{K_h(gamma)}(lambda, a);   (u,v)^T |--> eta(gamma)*rho(gamma)*Ad_{K_h(gamma)}(u,v)^T;   (p_2,-p_1)^T |--> eta(gamma)*conj(rho(gamma))*Ad_{K_h(gamma)}(p_2,-p_1)^T
Cusp (c = [a,b]):      M_cusp(lambda,a) = (-1)^(-m)*Ad_{K_pi} = (-1)^m*Ad_{Zeta*P} = Ad_Zeta;   M_cusp(u,v) = (-1)^(1-m)*(-I_2)*Ad_{K_pi} = Ad_Zeta   (on ALL four slots!)
```
Here $\epsilon_F\rho(\gamma)=\overline{\rho(\gamma)}\epsilon_F$ ($\epsilon_F=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$) intertwines the trace-dual $(p_2/\Omega,-p_1/\Omega)^T$ with $\overline{\rho(\gamma)}$, and around the puncture $c=[a,b]$ the extending-spin sign $(-1)^k$ on $S^k$, the spin-gauge holonomy $\operatorname{Ad}_P=(-1)^m$, the flavour commutator $\rho(c)=-I_2$, and the coherent gauge commutator $K_h(c)=[X,Y]=K_\pi=\mathrm{Zeta}\,P$ combine to give $\operatorname{Ad}_{\mathrm{Zeta}}$ on **every slot and every phase**.

---

## 3. Duty 3: Complete $248$ Branching, Universal $D_5$ Weight Laws, and Core/End Transitions on $h_4$ vs $h_1$

Under $\mathfrak{so}(10)\oplus\mathfrak{su}(4)\subset\mathfrak{e}_8$ (`ELECTROWEAK_TWO_TRIPLE_PHYSICAL_KERNEL.md` §3), $\mathfrak{e}_8=(45,1)\oplus(1,15)\oplus(10,6)\oplus(16,4)\oplus(\overline{16},\bar{4})$. Under the two principal $\mathfrak{su}(2)_\pm\subset\mathfrak{so}(5)_\pm\subset\mathfrak{so}(10)$ triples, each irreducible module $V_{(j,k)}=V_j\otimes V_k$ ($\dim=(2j+1)(2k+1)$) has $H_\pm$-weights $2 m_\pm$ ($m_+\in\{-j,\dots,j\}$, $m_-\in\{-k,\dots,k\}$) and universal $D_5$ operators:
```text
m = m_+ + m_- in Z,   P = exp(-i*pi*H/2) = (-1)^m,   D = exp(-i*pi*(H_+ - H_-)/4) = (-i)^(m_+ - m_-),   K_pi = D^2 = Zeta*P = (-1)^(m_+ - m_-),   Zeta = (-1)^(2*m_+)
Ad_A(H_+, H_-) = (H_-, H_+),   Ad_A(E_+, E_-) = (-i*E_-, -i*E_+),   X = A*h,   Y = D*A*h,   X^2 = Y^2 = (X*Y)^2 = K_pi,   X*Y = D
```
1. **Connected Phase $h_4=\exp(-\frac{\pi}{4}(J_1+J_2+J_3))\in G_0$** (unbroken centralizer $\mathfrak{u}(3)=\mathfrak{su}(3)_c\oplus\mathfrak{u}(1)_{\text{em}}$, $\dim 9$; parallel grading $X C X^{-1}=Y C Y^{-1}=C$, $\eta_{K_{h_4}}=(0,0)$):
   - $(1,15)=V_{(0,0)}\otimes(8_0\oplus 1_0\oplus 3_{-4/3}\oplus\bar{3}_{+4/3})$ ($15$ dims, $m=0$, $A=D=1$, $\mathrm{Zeta}=+1$): $\operatorname{Ad}_{h_4}=+1$ on $8_0\oplus 1_0$ ($9$ dims, $(X,Y)=(+1,+1)=\chi_{(0,0)}$) and $\operatorname{Ad}_{h_4}=-1$ on $3_{-4/3}\oplus\bar{3}_{+4/3}$ ($6$ dims, $(X,Y)=(-1,-1)=\chi_{(1,1)}$).
   - $(10,6)=[V_{(2,0)}\oplus V_{(0,2)}]\otimes(3_{+2/3}\oplus\bar{3}_{-2/3})$ ($60$ dims, $m\in\{\pm 2,\pm 1,0\}$, $\mathrm{Zeta}=+1$): $\operatorname{Ad}_{h_4}=+i$ on $3_{+2/3}$ ($30$ dims, $(X,Y)=(i A, i D A)$) and $-i$ on $\bar{3}_{-2/3}$ ($30$ dims, $(X,Y)=(-i A, -i D A)$). On $\operatorname{span}(v_+,v_-)$ ($m=+2$, $D=-I_2$, $A_{\text{top}}^2=-I_2$), $X_{\text{top}}=\pm i A_{\text{top}}$ has $X_{\text{top}}^2=+I_2$; under the paired Koszul reduction with flavour $\rho$, each $10$-dim $D_5$ fibre contracts to rank-$1$ extremes $S^{-2}G_0,S^4 G_2$ and a rank-$2$ middle bundle $(S^3 V_3\oplus S^{-1}V_{-1})$ with peripheral $-I_2$ (`COUPLED_UP_SECTOR_PARABOLIC_COUNT_2026_11_08.md` §2–4).
   - $(16,4)\oplus(\overline{16},\bar{4})=V_{(3/2,3/2)}\otimes[(1_{+1}\oplus 3_{-1/3})\oplus(1_{-1}\oplus\bar{3}_{+1/3})]$ ($128$ dims, $m\in\{\pm 3,\pm 2,\pm 1,0\}$, $\mathrm{Zeta}=-1$): $(16,4)$ and $(\overline{16},\bar{4})$ are **preserved separately**. With $z=e^{-i\pi/4}$, $h_4|_{1_{+1}}=-z$, $h_4|_{3_{-1/3}}=+z$, $h_4|_{1_{-1}}=-z^{-1}$, $h_4|_{\bar{3}_{+1/3}}=+z^{-1}$. On each $16$-dim $V_{(3/2,3/2)}$ fibre, $X|_{v_{\text{top}}}=\alpha\in\{\pm 1\}$ ($\alpha^2=K_\pi|_{v_{\text{top}}}=+1$), and the surviving Koszul lines are $S^{-3}L_\alpha\to(S^1 L_+\oplus S^1 L_-)\to S^5 L_{-\alpha}$ with $\{L_+,L_-\}=\{\chi_{(0,0)},\chi_{(1,1)}\}$ (`COUPLED_HALF_ROOT_KERNEL_AND_CORE_LIFT_SENSITIVITY.md` §2, §5).
   - $(45,1)=([V_{(1,0)}\oplus V_{(0,1)}]\oplus[V_{(3,0)}\oplus V_{(0,3)}]\oplus V_{(2,2)})\otimes 1_0$ ($6+14+25=45$ dims, $\mathrm{Zeta}=+1$): $\operatorname{Ad}_{h_4}=+1$ on all $45$ dims, so $(X,Y)=(A,D A)$.
2. **Outer Phase $h_1=\pi_{E_8}(U f_1)\in s G_0$** (unbroken centralizer $\mathfrak{so}(5)\subset\mathfrak{a}_3$, $\dim 10$; orientation-reversing $X C X^{-1}=Y C Y^{-1}=C^{-1}$, $\eta_{K_{h_1}}=(1,1)$):
   On $V_{16}=V_{5,+}\oplus V_{5,-}\oplus\mathbb{R}f_1\oplus V_5^\perp$, $q_{16}(h_1)=\operatorname{diag}(+I_5,-I_5,-1,+I_5)$ (`COHERENT_PHASE_CLASSES.md` §1):
   - $(1,15)=V_{(0,0)}\otimes(10_{\mathfrak{so}(5)}\oplus 5_{\text{vec}})$ ($15$ dims, $m=0$, $\mathrm{Zeta}=+1$): $\operatorname{Ad}_{h_1}=+1$ on $10_{\mathfrak{so}(5)}$ ($10$ dims, $(X,Y)=\chi_{(0,0)}$) and $\operatorname{Ad}_{h_1}=-1$ on $5_{\text{vec}}=\mathbb{R}f_1\wedge V_5^\perp$ ($5$ dims, $(X,Y)=\chi_{(1,1)}$).
   - $(10,6)=[V_{(2,0)}\oplus V_{(0,2)}]\otimes(1_{\text{axis}}\oplus 5_{\text{vec}})$ ($60$ dims, $\mathrm{Zeta}=+1$): Since $q_{16}(h_1)=(+I_5,-I_5)=\sigma_z$ on $V_{5,+}\oplus V_{5,-}$ while $q_{16}(h_1)=-1$ on $\mathbb{R}f_1$ and $+I_5$ on $V_5^\perp$, $\operatorname{Ad}_{h_1}$ acts on $V_{(2,0)}\oplus V_{(0,2)}$ by $-\sigma_z$ on $1_{\text{axis}}$ ($10$ dims, $(X,Y)=(-A\sigma_z,-D A\sigma_z)$) and by $+\sigma_z$ on $5_{\text{vec}}$ ($50$ dims, $(X,Y)=(+A\sigma_z,+D A\sigma_z)$). Because $A$ exchanges $V_{(2,0)}\leftrightarrow V_{(0,2)}$, $A\sigma_z=-\sigma_z A$, so $( \mp A\sigma_z)^2=-A^2=K_\pi$, giving the **same** reduced Koszul bundle structure on each of the $1+5=6$ directions as on $h_4$!
   - $(16,4)\oplus(\overline{16},\bar{4})$ ($128$ dims, $\mathrm{Zeta}=-1$): Because $X C X^{-1}=C^{-1}$, $X=A h_1$ and $Y=D A h_1$ **interchange $(16,4)\leftrightarrow(\overline{16},\bar{4})$**. Only the combined $128$-dim sum is operator-invariant, splitting under $\operatorname{Spin}(5)\times\langle h_1\rangle$ into two $64$-dim blocks $(V_{(3/2,3/2)},4_{\operatorname{Spin}(5),\alpha=+1})\oplus(V_{(3/2,3/2)},4_{\operatorname{Spin}(5),\alpha=-1})$, each $16$-dim fibre carrying $S^{-3}L_\alpha\to(S^1 L_+\oplus S^1 L_-)\to S^5 L_{-\alpha}$ with $\{L_+,L_-\}=\{\chi_{(0,0)},\chi_{(1,1)}\}$.
   - $(45,1)$ ($45$ dims, $\mathrm{Zeta}=+1$): On $\Lambda^2(V_{5,+})\oplus\Lambda^2(V_{5,-})=[V_{(1,0)}\oplus V_{(0,1)}]\oplus[V_{(3,0)}\oplus V_{(0,3)}]$ ($6+14=20$ dims), $\operatorname{Ad}_{h_1}=(+1)^2=(-1)^2=+1$ ($(X,Y)=(A,D A)$, **identical** to $h_4$). On $V_{5,+}\otimes V_{5,-}=V_{(2,2)}$ ($25$ dims), $\operatorname{Ad}_{h_1}=(+1)(-1)=-1$, twisting $(X,Y)=(-A,-D A)=\chi_{(1,1)}\otimes(A,D A)$ relative to $h_4$!

---

## 4. Duty 4 & 5: Operator-Invariant Coefficient Blocks, Koszul Reductions, and Continuum Channels

Because $\operatorname{ad}_{\hat{q}},\operatorname{ad}_{\hat{r}}$ raise $m_\pm\mapsto m_\pm+1$ while $X=A h$ exchanges $V_j\otimes V_k\leftrightarrow V_k\otimes V_j$ (and on $h_1$ swaps $16\leftrightarrow\overline{16}$), unequal modules $V_{(j,0)}\oplus V_{(0,j)}$ ($j=1,2,3$) and, on $h_1$, $(16,4)\oplus(\overline{16},\bar{4})$ must be kept as paired blocks under $M=U_{\text{out}}T U_{\text{in}}$:

| Operator-Invariant Block | Dim | $D_5$ Two-Triple Modules & Weights $m=m_++m_-$ | Connected Phase $h_4\in G_0$ ($\mathfrak{u}(3)$, $\eta_{K_{h_4}}=(0,0)$) | Outer Phase $h_1\in s G_0$ ($\mathfrak{so}(5)$, $\eta_{K_{h_1}}=(1,1)$) | Cusp $\operatorname{Ad}_{\mathrm{Zeta}}$ & Reduced Bundle / Continuum Structure |
|---|---:|---|---|---|---|
| $(1,15)_+$ (unbroken gauge) | $9$ ($h_4$) / $10$ ($h_1$) | $V_{(0,0)}$ ($m=0$; slots $S^0,S^{-2},S^1\otimes F$) | $(1,8_0\oplus 1_0)$, $h_4=+1$, $(X,Y)=\chi_{(0,0)}$ | $(1,10_{\mathfrak{so}(5)})$, $h_1=+1$, $(X,Y)=\chi_{(0,0)}$ | $+1$ ($\nu\in\mathbb{Z}$); **zero-angular cusp continuum** $M_{\text{spin}}^\dagger M_{\text{spin}}=-\partial_t^2 I_2$ |
| $(1,15)_-$ (broken $A_3/G_{\text{unbr}}$) | $6$ ($h_4$) / $5$ ($h_1$) | $V_{(0,0)}$ ($m=0$; slots $S^0,S^{-2},S^1\otimes F$) | $(1,3_{-4/3}\oplus\bar{3}_{+4/3})$, $h_4=-1$, $(X,Y)=\chi_{(1,1)}$ | $(1,5_{\text{vec}})$, $h_1=-1$, $(X,Y)=\chi_{(1,1)}$ | $+1$ ($\nu\in\mathbb{Z}$); **same cusp tail continuum** $-\partial_t^2 I_2$ on all $15$ $A_3$ dirs |
| $(10,6)$ (paired vector-cross) | $60$ ($30+30$ on $h_4$; $10+50$ on $h_1$) | $[V_{(2,0)}\oplus V_{(0,2)}]\otimes 6$ ($m\in\{\pm 2,\pm 1,0\}$; 10-dim $D_5$ fibre) | $3_{+2/3}$ ($h_4=+i$) $\oplus$ $\bar{3}_{-2/3}$ ($h_4=-i$); $(X,Y)=(\pm i A,\pm i D A)$ | $1_{\text{axis}}$ ($h_1=-\sigma_z$) $\oplus$ $5_{\text{vec}}$ ($h_1=+\sigma_z$); $(X,Y)=(\mp A\sigma_z,\mp D A\sigma_z)$ | $+1$ ($\nu\in\mathbb{Z}$); reduced $S^{-2}G_0\to(S^3 V_3\oplus S^{-1}V_{-1})\to S^4 G_2$ (avoids $a=1$; middle rank-2 cusp $-I_2$) |
| $(16,4)\oplus(\overline{16},\bar{4})$ (half-root spinors) | $128$ ($16+48+16+48$ on $h_4$; $64+64$ on $h_1$) | $V_{(3/2,3/2)}\otimes(4\oplus\bar{4})$ ($m\in\{\pm 3,\pm 2,\pm 1,0\}$; 16-dim $D_5$ fibre) | Preserves $(16,1_{+1})_{-z}, (16,3_{-1/3})_{+z}, (\overline{16},1_{-1})_{-z^{-1}}, (\overline{16},\bar{3}_{+1/3})_{+z^{-1}}$ ($z=e^{-i\pi/4}$) | Swaps $(16,4)\leftrightarrow(\overline{16},\bar{4})$; splits into $4_{\operatorname{Spin}(5),\alpha=+1}\oplus 4_{\operatorname{Spin}(5),\alpha=-1}$ ($64+64$) | $-1$ ($\nu\in\mathbb{Z}+\frac{1}{2}$, **gapped cusp**); reduced $S^{-3}L_\alpha\to(S^1 L_+\oplus S^1 L_-)\to S^5 L_{-\alpha}$, $\{L_+,L_-\}=\{\chi_{(0,0)},\chi_{(1,1)}\}$ |
| $(45,1)_{\text{unequal}}$ (adjoint $\Lambda^2(5_+)\oplus\Lambda^2(5_-)$) | $20$ ($6+14$) | $[V_{(1,0)}\oplus V_{(0,1)}]$ ($6$, $m\in\{\pm 1,0\}$) $\oplus$ $[V_{(3,0)}\oplus V_{(0,3)}]$ ($14$, $m\in\{\pm 3,\pm 2,\pm 1,0\}$) | $h_4=+1$ on all $20$; $(X,Y)=(A,D A)$ | $h_1=+1$ on all $20$; $(X,Y)=(A,D A)$ (**identical** to $h_4$) | $+1$ ($\nu\in\mathbb{Z}$); extremes $S^{-1},S^3$ ($j=1$) and $S^{-3},S^5$ ($j=3$) have cusp $-I_2$, middle $S^2,S^0$ and $S^4,S^{-2}$ cusp $+I_2$ |
| $(45,1)_{(2,2)}$ (adjoint $5_+\otimes 5_-$) | $25$ | $V_{(2,2)}$ ($m\in\{\pm 4,\pm 3,\pm 2,\pm 1,0\}$; surviving $S^{-4}\to S^1 V_1^{(2,2)}\to S^6$) | $h_4=+1$ on all $25$; $(X,Y)=(A,D A)$ | $h_1=-1$ on all $25$; $(X,Y)=(-A,-D A)=\chi_{(1,1)}\otimes(A,D A)$ | $+1$ ($\nu\in\mathbb{Z}$); middle $S^1 V_1^{(2,2)}$ has cusp $-I_2$ at **critical $a=1$ non-closed-range threshold continuum** |

- **Explicit continuum channels on both coherent phases:**
  1. **$(1,15)$ zero-angular radial continuum (`COUPLED_QUATERNION_STATIONARY_BUNDLE_AND_CUSP_LAW.md` §5):** On all $15$ directions of $A_3$ (both $9+6$ on $h_4$ and $10+5$ on $h_1$), $D_5$ acts trivially ($[E,T]=[G,T]=[H,T]=0$) and peripheral holonomy is $+1$. In $t=\ln y$, zero-angular spin variations $(u T, v T)$ decouple from $(\lambda,a)$ with $M_{\text{spin}}(u,v)=(i\partial_t v, -i\partial_t u)$ and $M_{\text{spin}}^\dagger M_{\text{spin}}=-\partial_t^2 I_2$, putting $0\in\sigma_{\text{ess}}(M)$ on both phases.
  2. **$(45,1)_{(2,2)}$ critical $a=1$ threshold endpoint (`UP_SECTOR_EXPLORATORY_NEUTRAL_NOTES_2026_11_08.md`):** In $V_{(2,2)}$, the middle surviving Koszul package $S^1 V_1^{(2,2)}$ sits at the critical exponent $a=1$ with peripheral $-I_2$, where physical $H^0_{L^2}=0$ by the maximum principle while the radial range is not closed and the essential spectrum reaches zero (unlike $(10,6)$, whose powers $a\in\{-2,3,-1,4\}$ avoid $a=1$).

---

## 5. Duty 6: Smallest Consequential Next Kernel Problem (`AGY-02b` Preview)

With the complete $248$-direction transition-resolved roster established on both $h_4$ and $h_1$ at $W=1$:
1. On $(10,6)$ and $(16,4)\oplus(\overline{16},\bar{4})$, the reduced Koszul line/rank-2 bundles per invariant $D_5$ fibre are **structurally identical** between $h_4$ and $h_1$ (differing only by the unbroken $A_3$ multiplicity grouping: $3_{+2/3}\oplus\bar{3}_{-2/3}$ vs $1_{\text{axis}}\oplus 5_{\text{vec}}$ on $(10,6)$, and $1_{+1}\oplus 3_{-1/3}\oplus 1_{-1}\oplus\bar{3}_{+1/3}$ vs $4_{\operatorname{Spin}(5),\alpha=+1}\oplus 4_{\operatorname{Spin}(5),\alpha=-1}$ on $128$).
2. The **only** block in $248$ where $h_4$ and $h_1$ induce genuinely different core characters on the $D_5$ fibre itself (beyond the $1$-dim $(1,15)$ sign split $9_+ \oplus 6_-$ vs $10_+ \oplus 5_-$) is the **$25$-dimensional neutral block $V_{(2,2)}\subset(45,1)$**, where $\operatorname{Ad}_{h_4}|_{V_{(2,2)}}=+1$ whereas $\operatorname{Ad}_{h_1}|_{V_{(2,2)}}=-1=\chi_{(1,1)}$.
3. Therefore, the **smallest consequential next kernel problem** is to derive the exact source-representative actions, domain transfer, and $L^2$ harmonic kernel counts across the coupled sectors—specifically resolving the $D_5$-neutral $(45,1)=[V_{(1,0)}\oplus V_{(0,1)}]\oplus[V_{(3,0)}\oplus V_{(0,3)}]\oplus V_{(2,2)}$ block (and its $\chi_{(1,1)}$-twisted $V_{(2,2)}$ counterpart on $h_1$ at the critical $a=1$ endpoint) alongside the $W=1$ specialization of $(10,6)$ and $128$.
