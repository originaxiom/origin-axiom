# Transition-Resolved Coefficient Roster on the Coherent Phases (`AGY-02a`, Repaired in `AGY-02b`)

- **Date:** `2026-11-09`
- **Status / Evidence Grade:** `PARTIAL_HAND_ROSTER_SUPPORTED_WITH_BINDING_CORRECTIONS` (`REVIEW_AGY_02A_D1F_2026_11_09.md`, SHA256 `9ef01b8f4c6418198da299c698726a1100d60b0eba0199469d783c1fc50f624d`; bundled physical repairs in `AGY-02b`, `scientific_execution_authorized = false`)
- **Active & Prior Tickets:** `RUN_TICKET_AGY_02A.md` (`4e26a293681cd9246c7469d96fe5ef68d4455a5920f744a4a8c7f3f4136f5560`); `RUN_TICKET_AGY_02B.md` (`6b4b7622c016c3fc0e5e6a1360523952ad6ecaa5e3883e0b9d6573eca00c61f5`)
- **Baseline Pins:** Physical `3234bbdd76245bcd484cbbf1bae24aab84d281da` (extended through `65b359b222daaf7e3deb3e5d084dbc312bec2905`); Canonical GENESIS `217e37c4f37bd80998f3c3e10cad358023f58114`
- **Accepted / Supported Campaign Dependencies:**
  - `CENTRALIZER_COMPONENTS.md` (`a0e86b7164e401498869fce468a5fcfad140ca28529e86d721b3dffab7673075`), `COHERENT_PHASE_CLASSES.md` (`9b0ec09b6b5effbfd5853dcd599f95ff3bb2106d39c1a2146c226b069630f6d0`), `REGISTER_TO_GRADING.md` (`965c3652ce550b448e3aa37e0b397f5492339882ce18b38a94f4bdf36addf008`), `COMPENSATOR_RANGE_AUDIT.md` (`81b29726b20218ed2625de06369c7a5d55c13427d85d81ed2888d27a3280a0d3`), `INPUT_LEDGER.md` (`98bf93b4be89297901e8f9718f88ea526105b717310df63b75e21deb282713e5`)
- **Pinned Operator & Word-Architecture Sources:**
  - `PHYSICAL_ROSTER_TARGETS_AND_NEUTRAL_TAIL_CONTROL_2026_11_09.md` (`65b359b222daaf7e3deb3e5d084dbc312bec2905`, `4079abd1606bcd72e4f20b0a89db1fd14de8f7a2fcb8ad9d5858160f912915e6`)
  - `weave_physical_mass_2026_10_08/PROOF.md` (`04fbb6b7ddc23fe2ae56aa24f3df6e9a710f6278363213b8a509b06ace83ef8d`)
  - `weave_curved_action_2026_10_08/PROOF.md` (`c505823ce2b934b9737780acf3d6bbbeeb8482613b7ecc76a2ece58b1c2ebc4f`)
  - `COUPLED_QUATERNION_STATIONARY_BUNDLE_AND_CUSP_LAW.md` (`221a7cd2dce2ff7dec0b135c348b7bb52e15bc27e5563d420756fbe31f9978a1`)
  - `COUPLED_HALF_ROOT_KERNEL_AND_CORE_LIFT_SENSITIVITY.md` (`789adf7544bf5c679305aa8b9ba7525b6375155b026c839e01c34c281be23875`)
  - `ELECTROWEAK_TWO_TRIPLE_PHYSICAL_KERNEL.md` (`871529dd81603e1a70126f6ee518ae5c2758c107cf7e9fff62ae96f646a0813f`)
  - `COUPLED_UP_SECTOR_PARABOLIC_COUNT_2026_11_08.md` (`477743caf7f2edc91117ed9f7ef24efcb834c5a8968bfd19ffc46865d75d9ff9`)
  - `UP_SECTOR_EXPLORATORY_NEUTRAL_NOTES_2026_11_08.md` (`c4110e34a25e37d72dd9ec1823cb01320071cb6ae17608d68c3a658bd38a9de0`)
  - `QUARTER_PHASE_CHARACTER_BRIDGE_AND_COHERENT_WORD_CONTROL_2026_11_09.md` (`83453638584cb34219ca389bfb7a753259fd3a1f9f2e651ada07cfbe3002a733`)

---

## 1. Duty 1: Baseline Stationary Saddle and Specified Zero-Wilson ($W = 1$) Comparison Choice

Fix the complete finite-area once-punctured elliptic curve $\Sigma_{1,1}$ ($\pi_1(\Sigma_{1,1})=\langle a,b\rangle\cong F_2$, oriented cusp loop $c=[a,b]=a b a^{-1}b^{-1}$) with curvature $-1/\ell^2$ (`weave_curved_action_2026_10_08/PROOF.md`), extending spin line $S$ ($S^2\cong K_{\Sigma_{1,1}}$, peripheral cusp sign $-1$, compact order-two spin character $\eta:F_2\to\{\pm 1\}$, $\eta(c)=+1$), natural slot densities $(\Omega^2,1/2,\Omega,\Omega)$, flat quaternion flavour bundle $F$ ($\operatorname{Hol}_F=\rho:F_2\to Q_8\subset\operatorname{SU}(2)$, $\rho(a)=F_i=\operatorname{diag}(i,-i)$, $\rho(b)=F_j=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$, $\rho(c)=-I_2$), spin connection $A_{\text{spin}}=s_{\text{spin}}H/2$ ($H=H_++H_-$), and balanced two-triple scalar saddle:
```text
Phi_0 = (q_hat, r_hat) = (E, G)/(2*sqrt(2)*ell) = ((E_+ + E_-), (E_+ - E_-))/(2*sqrt(2)*ell),   F_spin/dvol + [q_hat, q_hat^dagger] + [r_hat, r_hat^dagger] = 0
```
- **Why zero extra Wilson ($W=1$) is our specified phase-comparison choice:**
  In $G_0=\operatorname{Spin}(6)\cong\operatorname{SU}(4)$ with Cartan generators $J_1=f_1 f_2, J_2=f_3 f_4, J_3=f_5 f_6$, the previously explored order-three electromagnetic Wilson line $W_{\text{em}}=\exp(\frac{2\pi}{3}(J_1+J_2+J_3))\in G_0$ commutes with $D_5$ and $h_4=\exp(-\frac{\pi}{4}(J_1+J_2+J_3))$, **but does not commute with $h_1=\pi_{E_8}(U f_1)\in s G_0$** in the adapted frame:
```text
tau(J_1, J_2, J_3) = (-J_1, J_2, J_3)  ==>  h_1 * W_em * h_1^-1 = exp((-4*pi/3)*J_1) * W_em != W_em   (since exp((-4*pi/3)*J_1) != 1 on 6 and 4 of A_3)
```
  Setting $W=1$ is our specified baseline for comparing $h_4\in\mathcal{O}_0$ and $h_1\in\mathcal{O}_1$ without importing a $G_0$-only Wilson factor; common compatible Wilson subgroups in $G_0^\tau=\operatorname{Spin}(5)$ ($J_1=0$) or a changed full transport problem remain possible constructions (`REVIEW_AGY_02A_D1F_2026_11_09.md`).

---

## 2. Duty 2: Four Physical Left Weyl Slots, Corrected Trace-Dual Output Bundles, and Peripheral Sign

The physical fermion field (`weave_physical_mass_2026_10_08/PROOF.md` §1–2, `PHYSICAL_ROSTER_TARGETS_AND_NEUTRAL_TAIL_CONTROL_2026_11_09.md` §1) consists of **four independent left-handed Weyl coefficients** $\psi=(\lambda,a,u,v)$ valued in $\mathfrak{e}_8$ with coordinate kinetic densities $(\Omega^2,1/2,\Omega,\Omega)$ under $dx\,dy$. Let $E_m$ denote the smooth unitary gauge-weight bundle with geometric spin power $S^{-m}$ where $[H/2,X]=m X$ ($m:=m_++m_-\in\mathbb{Z}$, $H_\pm=2 m_\pm$). The input slots are $\lambda\in E_m$, $a\in\bar{K}\otimes E_m$, $(u,v)\in S\otimes F\otimes E_m$, and the weighted mass map $M=U_{\text{out}}\circ T\circ U_{\text{in}}$ has rows:
```text
U_in(lambda, a, u, v) = ((a, u, v),  i*Omega^2*lambda/sqrt(2)),     U_out(g, p_1, p_2, t) = (g,  2*i*t,  p_2/Omega,  -p_1/Omega)
M(lambda, a, u, v) = (g := D_0^dagger x,  2*i*t + sqrt(2)*D_z lambda,  p_2/Omega - sqrt(2)*i*[q^dagger, lambda],  -p_1/Omega - sqrt(2)*i*[r^dagger, lambda])
D_0^dagger x = -[D_z a - 2*i*Omega*([q^dagger, u] + [r^dagger, v])]/(sqrt(2)*Omega^2),   p_1 = D_bar u + i*[q, a],   p_2 = D_bar v + i*[r, a],   t = [q, v] - [r, u]
```
Here $g=D_0^\dagger x\in E_m$ is a scalar gauge-parameter-type section, $2i t+\sqrt{2}D_z\lambda\in K\otimes E_m$ is a $(1,0)$-form section, and the last two rows lie in $\bar{S}\otimes\bar{F}\otimes E_m$ (under $t=dz/dw$, $(u,v)$ gains $t^{1/2}$, $\bar{D}$ adds $\bar{t}$, and $\Omega^{-1}$ adds $|t|^{-1}$, giving $\bar{t}^{1/2}$). Using the smooth metric identifications $\bar{K}\simeq S^{-2}$, $K\simeq S^2$, $\bar{S}\simeq S^{-1}$ (while retaining holomorphic structures, densities, and metric volume factors in operator/sheaf calculations), the input/output bundles, core transitions ($\gamma\in F_2$, after factoring a reference spin bundle so $S$ carries the explicit order-two flat character $\eta$), and peripheral cusp transition ($c=[a,b]$) are:
```text
Input bundles  (lambda, a, (u,v)^T):                     (E_m ~= S^-m,   K_bar tensor E_m ~= S^(-2-m),   S tensor F tensor E_m ~= S^(1-m) tensor F)
Output bundles (g, 2it+sqrt(2)D_z lambda, spin pair):    (E_m ~= S^-m,   K tensor E_m     ~= S^(2-m),    S_bar tensor F_bar tensor E_m ~= S^(-1-m) tensor F_bar)
Core (gamma in F_2, explicit spin choice eta):           (lambda,a; g,form) |--> eta(gamma)^(-m)*Ad_{K_h(gamma)};   (u,v)^T |--> eta(gamma)^(1-m)*rho(gamma)*Ad_{K_h(gamma)};   output spin |--> eta(gamma)^(-1-m)*conj(rho(gamma))*Ad_{K_h(gamma)}
Cusp (c = [a,b]):                                        M_cusp(scalar/form) = (-1)^(-m)*Ad_{K_pi} = (-1)^m*Ad_{Zeta*P} = Ad_Zeta;   M_cusp(spin) = (-1)^(+-1-m)*(-I_2)*Ad_{K_pi} = Ad_Zeta   (on ALL slots!)
```
Note that $\eta(\gamma)^{-m}$ is already included when the powers $S^{-m},S^{\pm 2-m},S^{\pm 1-m}$ carry the spin choice $\eta$ (do not count $\eta$ twice or omit its gauge-induced power $\eta^{-m}$).

---

## 3. Duty 3: Complete $248$ Branching, Explicit Vector Intertwiner $T$, and Outer $X$-Grading on $128$

Under $\mathfrak{so}(10)\oplus\mathfrak{su}(4)\subset\mathfrak{e}_8$ (`ELECTROWEAK_TWO_TRIPLE_PHYSICAL_KERNEL.md` §3), $\mathfrak{e}_8=(45,1)\oplus(1,15)\oplus(10,6)\oplus(16,4)\oplus(\overline{16},\bar{4})$. Under the two principal $\mathfrak{su}(2)_\pm\subset\mathfrak{so}(5)_\pm\subset\mathfrak{so}(10)$ triples, each module $V_{(j,k)}=V_j\otimes V_k$ ($\dim=(2j+1)(2k+1)$) has $H_\pm$-weights $2 m_\pm$ and universal $D_5$ operators:
```text
m = m_+ + m_- in Z,   P = exp(-i*pi*H/2) = (-1)^m,   D = exp(-i*pi*(H_+ - H_-)/4) = (-i)^(m_+ - m_-),   K_pi = D^2 = Zeta*P = (-1)^(m_+ - m_-),   Zeta = (-1)^(2*m_+)
Ad_A(H_+, H_-) = (H_-, H_+),   Ad_A(E_+, E_-) = (-i*E_-, -i*E_+),   X = A*h,   Y = D*A*h,   X^2 = Y^2 = (X*Y)^2 = K_pi,   X*Y = D
```
1. **Connected Phase $h_4=\exp(-\frac{\pi}{4}(J_1+J_2+J_3))\in G_0$** (unbroken $\mathfrak{u}(3)=\mathfrak{su}(3)_c\oplus\mathfrak{u}(1)_{\text{em}}$, $\dim 9$; parallel grading $X C X^{-1}=Y C Y^{-1}=C$, $\eta_{K_{h_4}}=(0,0)$):
   - $(1,15)=V_{(0,0)}\otimes(8_0\oplus 1_0\oplus 3_{-4/3}\oplus\bar{3}_{+4/3})$ ($15$ dims, $m=0$, $A=D=1$, $\mathrm{Zeta}=+1$): $\operatorname{Ad}_{h_4}=+1$ on $8_0\oplus 1_0$ ($9$ dims, $(X,Y)=\chi_{(0,0)}$) and $-1$ on $3_{-4/3}\oplus\bar{3}_{+4/3}$ ($6$ dims, $(X,Y)=\chi_{(1,1)}$).
   - $(10,6)=[V_{(2,0)}\oplus V_{(0,2)}]\otimes(3_{+2/3}\oplus\bar{3}_{-2/3})$ ($60$ dims, $m\in\{\pm 2,\pm 1,0\}$, $\mathrm{Zeta}=+1$): $\operatorname{Ad}_{h_4}=+i$ on $3_{+2/3}$ ($30$ dims, $(X,Y)=(i A, i D A)$) and $-i$ on $\bar{3}_{-2/3}$ ($30$ dims, $(X,Y)=(-i A, -i D A)$). On each $10$-dim paired fibre $W=V_{(2,0)}\oplus V_{(0,2)}$, the surviving Koszul bundles have **aggregate ranks $(2,4,2)$**: **rank-$2$** extreme bundles $S^{-2}G_0$ (degree $0$, core characters $(+1,-1)\oplus(-1,+1)$) and $S^4 G_2$ (degree $2$), and two **rank-$2$** middle bundles $S^3 V_3\oplus S^{-1}V_{-1}$ (degree $1$, peripheral $-I_2$) (`COUPLED_UP_SECTOR_PARABOLIC_COUNT_2026_11_08.md` §2, `PHYSICAL_ROSTER_TARGETS_AND_NEUTRAL_TAIL_CONTROL_2026_11_09.md` §5).
   - $(16,4)\oplus(\overline{16},\bar{4})=V_{(3/2,3/2)}\otimes[(1_{+1}\oplus 3_{-1/3})\oplus(1_{-1}\oplus\bar{3}_{+1/3})]$ ($128$ dims, $m\in\{\pm 3,\pm 2,\pm 1,0\}$, $\mathrm{Zeta}=-1$): $(16,4)$ and $(\overline{16},\bar{4})$ are preserved separately ($z=e^{-i\pi/4}$, $h_4|_{1_{+1}}=-z$, $h_4|_{3_{-1/3}}=+z$, $h_4|_{1_{-1}}=-z^{-1}$, $h_4|_{\bar{3}_{+1/3}}=+z^{-1}$). On each $16$-dim $V_{(3/2,3/2)}$ fibre, $X|_{v_{\text{top}}}=\alpha\in\{\pm 1\}$, reducing to $S^{-3}L_\alpha\to(S^1 L_+\oplus S^1 L_-)\to S^5 L_{-\alpha}$ with $\{L_+,L_-\}=\{\chi_{(0,0)},\chi_{(1,1)}\}$ (Koszul ranks $(1,2,1)$).
   - $(45,1)=([V_{(1,0)}\oplus V_{(0,1)}]\oplus[V_{(3,0)}\oplus V_{(0,3)}]\oplus V_{(2,2)})\otimes 1_0$ ($6+14+25=45$ dims, $\mathrm{Zeta}=+1$): $\operatorname{Ad}_{h_4}=+1$ on all $45$ dims ($(X,Y)=(A,D A)$).
2. **Outer Phase $h_1=\pi_{E_8}(U f_1)\in s G_0$** (unbroken $\mathfrak{so}(5)\subset\mathfrak{a}_3$, $\dim 10$; orientation-reversing $X C X^{-1}=Y C Y^{-1}=C^{-1}$, $\eta_{K_{h_1}}=(1,1)$):
   The chosen $\operatorname{Spin}(16)$ representative $U f_1$ acts on $V_{16}=V_{5,+}\oplus V_{5,-}\oplus\mathbb{R}f_1\oplus V_5^\perp$ by $q_{16}(U f_1)=\operatorname{diag}(+I_5,-I_5,-1,+I_5)$ (the semispin quotient in $E_8$ does not carry a global vector-$16$ representation):
   - $(1,15)=V_{(0,0)}\otimes(10_{\mathfrak{so}(5)}\oplus 5_{\text{vec}})$ ($15$ dims, $m=0$): $\operatorname{Ad}_{h_1}=+1$ on $10_{\mathfrak{so}(5)}$ ($(X,Y)=\chi_{(0,0)}$) and $-1$ on $5_{\text{vec}}$ ($(X,Y)=\chi_{(1,1)}$).
   - $(10,6)=[V_{(2,0)}\oplus V_{(0,2)}]\otimes(1_{\text{axis}}\oplus 5_{\text{vec}})$ ($60$ dims): With $Z=\operatorname{diag}(+I_5,-I_5)$ on $W=V_{(2,0)}\oplus V_{(0,2)}$, $\operatorname{Ad}_{h_1}=-Z$ on $1_{\text{axis}}$ ($10$ dims, $(X,Y)=(-A Z,-D A Z)$) and $+Z$ on $5_{\text{vec}}$ ($50$ dims, $(X,Y)=(+A Z,+D A Z)$). Because $E_\pm,E_\pm^\dagger,H_\pm$ are block-diagonal on $V_{(2,0)}\oplus V_{(0,2)}$ while $A Z=-Z A$ and $D Z=Z D$, the constant unitary operator $T=\exp(i\pi Z/4)=\operatorname{diag}(e^{i\pi/4}I_5,e^{-i\pi/4}I_5)$ commutes with $\bar{D},D_z,A_{\text{spin}}$ and all Higgs commutators $\operatorname{ad}_{\hat{q}},\operatorname{ad}_{\hat{r}},\operatorname{ad}_{\hat{q}^\dagger},\operatorname{ad}_{\hat{r}^\dagger}$, so $\mathcal{U}_{T^{\pm 1}}=\operatorname{diag}(T^{\pm 1},T^{\pm 1},I_2\otimes T^{\pm 1})$ on the four input and trace-dual output slots unitarily intertwines the full linearized operator $M$ between $h_4$ and $h_1$ (`PHYSICAL_ROSTER_TARGETS_AND_NEUTRAL_TAIL_CONTROL_2026_11_09.md` §3):
```text
T = exp(i*pi*Z/4):  [T, E_+-] = [T, E_+-^dagger] = [T, H_+-] = 0,  T*(i*A)*T^-1 = A*Z,  T^-1*(i*A)*T = -A*Z,  T*D*T^-1 = D,  U_{T^+-1}*M_(h_4)*U_{T^+-1}^-1 = M_(h_1, +-Z)
```
   - $(16,4)\oplus(\overline{16},\bar{4})$ ($128$ dims): On $128$, $h_1^2=\mathrm{Zeta}=-1$ (eigenvalues $\pm i$). Instead, $X=A h_1$ interchanges $(16,4)\leftrightarrow(\overline{16},\bar{4})$, commutes with $\operatorname{Spin}(5)$, and satisfies $X^2=K_\pi=+1$ on the $8$-dim simultaneous highest space $|3/2,3/2\rangle_{16,4}\oplus|3/2,3/2\rangle_{\overline{16},\bar{4}}$, splitting it into $\alpha=+1$ and $\alpha=-1$ $\operatorname{Spin}(5)$ four-plets. Extending by the lowering strings (`PHYSICAL_ROSTER_TARGETS_AND_NEUTRAL_TAIL_CONTROL_2026_11_09.md` §4):
```text
X * (E_+^dagger)^n * (E_-^dagger)^k v_top = alpha * i^(n+k) * (E_+^dagger)^k * (E_-^dagger)^n v_top   (alpha = +-1 on v_top; gives 64 + 64 X-labelled packages)
```
   - $(45,1)$ ($45$ dims): $\operatorname{Ad}_{h_1}=+1$ on $[V_{(1,0)}\oplus V_{(0,1)}]\oplus[V_{(3,0)}\oplus V_{(0,3)}]$ ($20$ dims, $(X,Y)=(A,D A)$) and $\operatorname{Ad}_{h_1}=-1$ on $V_{(2,2)}$ ($25$ dims, $(X,Y)=(-A,-D A)=\chi_{(1,1)}\otimes(A,D A)$).

---

## 4. Duty 4, 5 & 6: Operator-Invariant Blocks, Corrected Koszul Ranks, Direct $V_{(2,2)}$ Weyl Sequence, and `AGY-02b` Join

| Operator-Invariant Block | Dim | $D_5$ Modules & Input/Output Slot Powers ($m=m_++m_-$) | Connected Phase $h_4\in G_0$ ($\mathfrak{u}(3)$, $\eta_{K_{h_4}}=(0,0)$) | Outer Phase $h_1\in s G_0$ ($\mathfrak{so}(5)$, $\eta_{K_{h_1}}=(1,1)$) | Cusp $\operatorname{Ad}_{\mathrm{Zeta}}$, Koszul Ranks & Continuum Structure |
|---|---:|---|---|---|---|
| $(1,15)_+$ (unbroken gauge) | $9$ / $10$ | $V_{(0,0)}$ ($m=0$; in $S^0,S^{-2},S^1\otimes F$; out $S^0,S^2,S^{-1}\otimes\bar{F}$) | $(1,8_0\oplus 1_0)$, $h_4=+1$, $(X,Y)=\chi_{(0,0)}$ | $(1,10_{\mathfrak{so}(5)})$, $h_1=+1$, $(X,Y)=\chi_{(0,0)}$ | $+1$ ($\nu\in\mathbb{Z}$); **zero-angular cusp continuum** $M_{\text{spin}}^\dagger M_{\text{spin}}=-\partial_t^2 I_2$ |
| $(1,15)_-$ (broken $A_3/G_{\text{unbr}}$) | $6$ / $5$ | $V_{(0,0)}$ ($m=0$; in $S^0,S^{-2},S^1\otimes F$; out $S^0,S^2,S^{-1}\otimes\bar{F}$) | $(1,3_{-4/3}\oplus\bar{3}_{+4/3})$, $h_4=-1$, $(X,Y)=\chi_{(1,1)}$ | $(1,5_{\text{vec}})$, $h_1=-1$, $(X,Y)=\chi_{(1,1)}$ | $+1$ ($\nu\in\mathbb{Z}$); **same cusp tail continuum** $-\partial_t^2 I_2$ on all $15$ $A_3$ dirs |
| $(10,6)$ (paired vector-cross) | $60$ | $[V_{(2,0)}\oplus V_{(0,2)}]\otimes 6$ ($m\in\{\pm 2,\pm 1,0\}$; 10-dim $D_5$ fibre) | $3_{+2/3}$ ($h_4=+i$) $\oplus$ $\bar{3}_{-2/3}$ ($h_4=-i$); $(X,Y)=(\pm i A,\pm i D A)$ | $1_{\text{axis}}$ ($-Z$) $\oplus$ $5_{\text{vec}}$ ($+Z$); intertwined with $h_4$ by $T=\exp(i\pi Z/4)$ | $+1$ ($\nu\in\mathbb{Z}$); **Koszul ranks $(2,4,2)$**: rank-2 $S^{-2}G_0\to(S^3 V_3\oplus S^{-1}V_{-1})\to S^4 G_2$ (avoids $a=1$) |
| $(16,4)\oplus(\overline{16},\bar{4})$ (half-root spinors) | $128$ | $V_{(3/2,3/2)}\otimes(4\oplus\bar{4})$ ($m\in\{\pm 3,\pm 2,\pm 1,0\}$; 16-dim $D_5$ fibre) | Preserves $(16,1_{+1})_{-z}, (16,3_{-1/3})_{+z}, (\overline{16},1_{-1})_{-z^{-1}}, (\overline{16},\bar{3}_{+1/3})_{+z^{-1}}$ | Swaps $(16,4)\leftrightarrow(\overline{16},\bar{4})$; $X|_{v_{\text{top}}}=\alpha=\pm 1$ gives $64+64$ packages | $-1$ ($\nu\in\mathbb{Z}+\frac{1}{2}$, **gapped cusp**); **Koszul ranks $(1,2,1)$**: $S^{-3}L_\alpha\to(S^1 L_+\oplus S^1 L_-)\to S^5 L_{-\alpha}$ |
| $(45,1)_{\text{unequal}}$ ($\Lambda^2(5_+)\oplus\Lambda^2(5_-)$) | $20$ ($6+14$) | $[V_{(1,0)}\oplus V_{(0,1)}]$ ($6$) $\oplus$ $[V_{(3,0)}\oplus V_{(0,3)}]$ ($14$) | $h_4=+1$ on all $20$; $(X,Y)=(A,D A)$ | $h_1=+1$ on all $20$; $(X,Y)=(A,D A)$ (**identical** to $h_4$) | $+1$ ($\nu\in\mathbb{Z}$); **Koszul ranks $(2,4,2)$** on each pair; $a\in\{-1,2,0,3\}$ and $\{-3,4,-2,5\}$ avoid $a=1$ |
| $(45,1)_{(2,2)}$ ($5_+\otimes 5_-$) | $25$ | $V_{(2,2)}$ ($m\in\{\pm 4,\pm 3,\pm 2,\pm 1,0\}$; **Koszul ranks $(1,2,1)$**) | $h_4=+1$ on all $25$; $(X,Y)=(A,D A)$ | $h_1=-1$ on all $25$; $(X,Y)=(-A,-D A)=\chi_{(1,1)}\otimes(A,D A)$ | $+1$ ($\nu\in\mathbb{Z}$); $S^{-4}L_{\text{ph}}\to S^1 V_1^{(2,2)}\to S^6 L_{\text{ph}}$; **direct 4-slot $a=1$ threshold continuum** |

- **Direct physical four-slot threshold witness on $V_{(2,2)}$ (`PHYSICAL_ROSTER_TARGETS_AND_NEUTRAL_TAIL_CONTROL_2026_11_09.md` §2) & `AGY-02b` Join:**
  In balanced flavour coordinates $(q',r')=\frac{1}{2\ell}(E_+,E_-)$, the mixed extremes $v_u=|-2,+2\rangle, v_v=|+2,-2\rangle\in V_{(2,2)}$ have $m=0$ and obey $E_+^\dagger v_u=E_- v_u=0$, $E_-^\dagger v_v=E_+ v_v=0$. For $\lambda=a=0$, $u'=f_L(t)v_u, v'=0$ with $f_L(t)=L^{-1/2}\chi((t-L^2)/L)$ ($t=\ln y$), every Higgs commutator in the scalar and form rows vanishes, cusp transport is $+1$, and $\|M\psi_L\|\le c_\ell\|\chi'\|/L\to 0$, proving $0\in\sigma_{\text{ess}}(M|_{V_{(2,2)}})$ directly on the four-slot physical domain. The complete global $L^2$ harmonic kernel and adjoint-domain resolution of $(45,1)$ is carried out in `NEUTRAL_D5_KERNEL.md` (`AGY-02b`).
