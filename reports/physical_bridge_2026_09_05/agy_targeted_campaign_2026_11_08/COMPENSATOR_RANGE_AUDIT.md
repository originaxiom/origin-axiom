# Faithful $E_8$ Compensator Range Audit: Outer Clifford Witness Beyond the Connected $\operatorname{U}(3)$ Phase (`AGY-01a-r1`)

- **Date:** `2026-11-09`
- **Status / Evidence Grade:** `AUTHOR HAND PROOF / UNREVIEWED` (`scientific_execution_authorized = false`; no scientific code, CAS, imports, test collection, or runs executed; formal independent review and scientific admission remain outstanding)
- **Active Microtask:** `AGY-01a-r1` (`REVIEW_AGY_01A_6CCE_2026_11_09.md` at `c542ba48fca5cb8bb6700634abedaffbe887f25f`, SHA256 `f1cd3d27efce72e2056e001db165f362430cbb56933baf9b37488c505620a43e`; `START_HERE.md`, SHA256 `b2d56e4317dd738831f204b1c1d3f548be9355e038bde2112e5961d519c44b07`; `TASKS.json`, SHA256 `0afe195709212ea78353bd71bcd75202592cc97cd176c8086e37e5950dbcf5d8`; `RUN_TICKET_AGY_01A.md` at `99a0364f2f17ffb02923042a7e9edd4a0e1af99d`, SHA256 `27f0ff5d08031a0233d9128471920adae1dd5a5f63dea93dbff99c120edb484a`)
- **Accepted Documentary Baseline:** `INPUT_LEDGER.md` (`605294403ecdd26666f3902881558e4bf6b85e93`, SHA256 `98bf93b4be89297901e8f9718f88ea526105b717310df63b75e21deb282713e5`); `REVIEW_AGY_00B2A_R2_605294_2026_11_09.md` (`99a0364f2f17ffb02923042a7e9edd4a0e1af99d`, SHA256 `5454ef0dcb42f51bcce00567cfbaa54532f8e3b7de5df4afc9892eeb37d63e6d`)
- **Pinned Source Inputs:**
  - `OPEN_PIN2_CORRECTION_BEYOND_THE_CHOSEN_EM_CIRCLE_2026_11_09.md` (`9a2bd40b3cf0a4d675a3c7013f83873d620a7bde`, SHA256 `56b948a9b9b53f5eeec9242c57b3e0dd3d79751195dba1c705118d6060230aa8`)
  - `FULL_E8_COMPENSATOR_LIFT_AND_REGISTER_TRANSPORT.md` (`2f690bc486adf2dfc07dd4fd94bf62b6db27bc86`, SHA256 `6012816683f17ac83e7d3bdb4f6d8b987ec8155ee2caa09ce651dbf0b194ed4c`)
  - `PIN2_COMPENSATOR_COHERENCE_AND_ELECTROMAGNETIC_PHASE.md` (`2f690bc486adf2dfc07dd4fd94bf62b6db27bc86`, SHA256 `fc67d4446b11f54c731b7e7aac56b496e501d5fa397040363de6c8074909a3b9`)
  - `ELECTROWEAK_TWO_TRIPLE_PHYSICAL_KERNEL.md` (`2f690bc486adf2dfc07dd4fd94bf62b6db27bc86`, SHA256 `871529dd81603e1a70126f6ee518ae5c2758c107cf7e9fff62ae96f646a0813f`)
  - `COUPLED_QUATERNION_STATIONARY_BUNDLE_AND_CUSP_LAW.md` (`2f690bc486adf2dfc07dd4fd94bf62b6db27bc86`, SHA256 `221a7cd2dce2ff7dec0b135c348b7bb52e15bc27e5563d420756fbe31f9978a1`)
  - `EXACT_ORDER_THREE_ELECTROWEAK_BRANCH.md` (`2f690bc486adf2dfc07dd4fd94bf62b6db27bc86`, SHA256 `3eae4eba764343746f46db14b58ae5d03ee412534b4067219143c40c3a2f09aa`)
  - Group-structure reference: B. McInnes, *The Semispin Groups in String Theory*, `arXiv:hep-th/9906059` (§§II–III, pp. 4–13, adapted to Euclidean $v^2=+1$)

---

## 1. Duty 1: Real Five-Space Split $V_{5,+}\oplus V_{5,-}$, Compact Form, and Orientation Sign $\delta$ of Source $A$

In `EXACT_ORDER_THREE_ELECTROWEAK_BRANCH.md` (§3) and `ELECTROWEAK_TWO_TRIPLE_PHYSICAL_KERNEL.md` (§2), the $D_5$ vector carrier $10$ on coordinates $(6,4,7,5,8)$ is presented in the split isotropic basis $B\oplus B^*\cong\mathbb{C}^5\oplus\mathbb{C}^5$ with positive Hermitian inner product $v^\dagger w$ and symmetric bilinear form $Q_{\text{split}}$. Compact $\mathfrak{so}(10)$ matrices satisfy $X^\dagger=-X$ and $X^T Q_{\text{split}}+Q_{\text{split}}X=0$, commuting with the anti-unitary real structure $\tau_{\mathbb{R}}(v)=Q_{\text{split}}\overline{v}$. On the fixed real subspace $\mathbb{R}^{10}=\{v\in\mathbb{C}^{10}:\tau_{\mathbb{R}}(v)=v\}$, the Hermitian and symmetric forms coincide as the positive-definite Euclidean metric.

In this split frame, $H=\operatorname{diag}(H_5,-H_5)$ with $H_5=\operatorname{diag}(-4,-2,0,2,4)$, $E=\operatorname{diag}(E_5,-E_5^T)$, and $G=\sqrt{10}\begin{pmatrix}0&B_Z\\J_5 B_Z J_5&0\end{pmatrix}$ with $J_5=\operatorname{anti-diag}(1,-1,1,-1,1)$ and $\sqrt{10}\,B_Z J_5=E_5$. Conjugating by $U_0=\operatorname{diag}(I_5,J_5)$ and $W_\sigma=\frac{1}{\sqrt{2}}\begin{pmatrix}I_5&I_5\\I_5&-I_5\end{pmatrix}$ gives $U_{\pm}=U_0 W_\sigma$, separating $E_{\pm}=(E\pm G)/2$ and $H_{\pm}=[E_{\pm},E_{\pm}^\dagger]=(H\pm\Delta)/2$ onto the two 5-blocks while transporting $Q_{\text{split}}$ to $Q_{\pm}=U_{\pm}^T Q_{\text{split}}U_{\pm}=\operatorname{diag}(J_5,-J_5)$.

To pass to an explicit $\tau_{\mathbb{R}}$-real orthonormal basis of $V_{5,+}\oplus V_{5,-}$ where both the Hermitian and symmetric forms equal $I_5\oplus I_5=I_{10}$, define the unitary matrix $R_5$ satisfying $R_5^\dagger R_5=I_5$, $J_5 R_5=\overline{R_5}$, and $R_5^T J_5 R_5=I_5$, and set $U_{\text{real}}=U_{\pm}\operatorname{diag}(R_5,i R_5)$:
```text
Q_split=[[0,I_5],[I_5,0]],  J_5=anti-diag(1,-1,1,-1,1),  N=diag(I_5,-I_5)
R_5=(1/sqrt(2))[[1,i,0,0,0],[0,0,1,i,0],[0,0,0,0,sqrt(2)],[0,0,-1,i,0],[1,-i,0,0,0]]
U_real=(1/sqrt(2))[[R_5,i*R_5],[conj(R_5),-i*conj(R_5)]]
U_real^dagger*U_real=I_10,  U_real^T*Q_split*U_real=diag(I_5,I_5),  Q_split*conj(U_real)=U_real
U_real^-1*(E_+,H_+)*U_real=(diag(E5_tilde,0),diag(H5_tilde,0)),  (E5_tilde,H5_tilde)=R_5^dagger*(E_5,H_5)*R_5
U_real^-1*(E_-,H_-)*U_real=(diag(0,E5_tilde),diag(0,H5_tilde))
```
The first five columns $(e_1^+,\dots,e_5^+)$ and last five columns $(e_1^-,\dots,e_5^-)$ of $U_{\text{real}}$ form $\tau_{\mathbb{R}}$-real orthonormal bases of $V_{5,+}$ and $V_{5,-}$ on which compact generators of both triples are real skew-symmetric matrices in $\mathfrak{so}(V_{5,+})\oplus\mathfrak{so}(V_{5,-})$.

In `FULL_E8_COMPENSATOR_LIFT_AND_REGISTER_TRANSPORT.md` (§2–§3), the first compensator on the split carrier is $A_{\text{vec}}=(-i N)\exp(-i\pi H/4)$ with $N=\operatorname{diag}(I_5,-I_5)$ and $D_5$ torus logarithm $x=(-1/4)^5+(1/2,1/4,0,-1/4,-1/2)=(1/4,0,-1/4,-1/2,-3/4)$, defining the faithful $E_8$ torus lift $A=\exp(2\pi i x_{D_5})$ preserving all spinor-product actions. In the real frame $U_{\text{real}}$:
```text
U_real^-1*(-i*N)*U_real=[[0,I_5],[-I_5,0]]=:J_10
U_real^-1*A_vec*U_real=[[0,O_5],[-O_5,0]],  O_5=exp(-i*pi*H5_tilde/4) in SO(5),  det(O_5)=+1
J_10*e_a^+=-e_a^-,  J_10*e_a^-=+e_a^+,  A_vec*e_a^-=+O_5*e_a^+,  A_vec*e_a^+=-O_5*e_a^-  (a=1..5)
```
Let $W=e_1^+ e_2^+ e_3^+ e_4^+ e_5^+$ and $U=e_1^- e_2^- e_3^- e_4^- e_5^-$ be the raw Clifford products of the five plus-frame and five minus-frame basis vectors, and define the raw $10$-volume $\omega_{10}:=W U$. Under the Euclidean Clifford map ($v^2=+1$), the $\operatorname{Spin}(10)$ subgroup $\exp(\frac{\theta}{2}\sum_{a=1}^5 e_a^+ e_a^-)$ covers $\exp(\theta J_{10})$ along the five $D_5$ Cartan planes:
- At $\theta=\pi/2$, $\prod_{a=1}^5\frac{1+e_a^+ e_a^-}{\sqrt{2}}$ covers $J_{10}=U_{\text{real}}^{-1}(-i N)U_{\text{real}}$ with torus coordinate $(-1/4)^5$.
- At $\theta=\pi$, $\prod_{a=1}^5(e_a^+ e_a^-)=(-1)^{10}W U=W U=\omega_{10}$ has torus coordinate $(-1/2)^5$ and equals $C^{-1}$, while at $\theta=-\pi$, $C=\exp(2\pi i(1/2)^5_{D_5})=\prod_{a=1}^5(-e_a^+ e_a^-)=-W U=-\omega_{10}$.

Orienting $V_{5,+}$ and $V_{5,-}$ by $\operatorname{vol}(V_{5,+}):=-W$ and $\operatorname{vol}(V_{5,-}):=U$ so that $\operatorname{vol}(V_{5,+})\operatorname{vol}(V_{5,-})=-W U=C=-\omega_{10}$, conjugation by $A$ sends $U$ to $W$ ($U^2=+1$):
```text
W=e_1^+...e_5^+,  U=e_1^-...e_5^-,  omega_10=W*U=C^-1=-C,  vol(V_5+)=-W,  vol(V_5-)=U,  vol(V_5+)*vol(V_5-)=C
A*U*A^-1=(A_vec*e_1^-)...(A_vec*e_5^-)=det(+O_5)*W=W=-C*U=C^-1*U
delta=-1 in Spin(16)  (mapping to Zeta in E_8, so A*U*A^-1=Zeta*C*U)
```
Thus the orientation sign of the source lift $A$ is uniquely fixed at **$\delta=-1$**.

---

## 2. Duty 2: Faithful $\operatorname{Spin}(16)\to E_8$ Map, Central Kernel, Half-Spin Chirality, and Global Subgroup Structure

Decompose $\mathbb{R}^{16}=\mathbb{R}^{10}_{D_5}\oplus\mathbb{R}^6_{D_3}=V_{5,+}\oplus V_{5,-}\oplus V_6$ with raw orthonormal basis $(e_1^+,\dots,e_5^+,e_1^-,\dots,e_5^-,f_1,\dots,f_6)$ satisfying $v_r v_s+v_s v_r=2\delta_{rs}$ in $\operatorname{Cl}(\mathbb{R}^{16})$. Let $C_6=\exp(2\pi i(1/2,1/2,1/2)_{D_3})$ be the $D_3$ central torus lift on $V_6$, and orient $(f_1,\dots,f_6)$ so that its raw product $\omega_6:=f_1 f_2 f_3 f_4 f_5 f_6=-C_6$ matches $\omega_{10}=W U=-C$. Then the raw $16$-volume element $\omega_{16}:=\omega_{10}\omega_6=W U f_1\cdots f_6=(-C)(-C_6)=C C_6=\exp(2\pi i(1/2)^8_{D_8})$ satisfies $\omega_{16}^2=(-1)^{16\cdot 15/2}=+1$ and acts as $+1$ on every even-parity $E_8$ half-root $\frac{1}{2}(\pm 1)^8$ ($\sum_{r=1}^8\epsilon_r\equiv 0\pmod 4$). The centre of $\operatorname{Spin}(16)$ is $Z(\operatorname{Spin}(16))=\{1,-1_{\operatorname{Spin}(16)},\omega_{16},-\omega_{16}\}\cong\mathbb{Z}_2\times\mathbb{Z}_2$.

Under the maximal connected proper rank-$8$ subgroup $\operatorname{Ss}(16)=\operatorname{Spin}(16)/\langle\omega_{16}\rangle$ of compact $E_8$, the Lie algebra decomposes as:
```text
omega_10=W*U=-C,  omega_6=f_1...f_6=-C_6,  omega_16=omega_10*omega_6=C*C_6,  ker(pi_E8:Spin(16)->E_8)={1,omega_16}
248=120_{so(16)}+128_{S+},  120=(45,1)+(1,15)+(10,6),  128=(16,4)+(bar16,bar4)=S+(R^16) [omega_16=+1]
pi_E8(-1_{Spin(16)})=Zeta,  Zeta|_120=+1,  Zeta|_128=-1,  Zeta^2=1
C=vol(V_5+)*vol(V_5-)=-omega_10=exp(2*pi*i*(1/2)^5_{D_5}),  C^2=(-1)^{10*9/2}=-1_{Spin(16)}|->Zeta
K_{10,6}=<(omega_10,omega_6)>={(1,1),(omega_10,omega_6),(-1,-1),(-omega_10,-omega_6)} ~= Z_4
```
In $E_8$, $C$ has exact order $4$ ($C^2=\mathrm{Zeta}$, $C^4=1$): it acts by $+1$ on $(45,1)\oplus(1,15)$, by $-1$ on $(10,6)$, by $+i$ on $(16,4)$, and by $-i$ on $(\overline{16},\overline{4})$, keeping all $120$ and $128$ coefficients faithful. As shown in McInnes (`hep-th/9906059` §§II–III), the multiplication map $\operatorname{Spin}(10)\times\operatorname{Spin}(6)\to\operatorname{Spin}(16)$ first kills $(-1,-1)$ and the semispin quotient $\pi_{E_8}$ kills $\omega_{16}=\omega_{10}\omega_6$, so the connected $(10+6)$ block subgroup inside $\operatorname{Ss}(16)\subset E_8$ is $(\operatorname{Spin}(10)\times\operatorname{Spin}(6))/K_{10,6}$ with cyclic order-$4$ central kernel $K_{10,6}$. Elements of the odd-odd Clifford product $\operatorname{Pin}_-(10)\cdot\operatorname{Pin}_-(6)\subset\operatorname{Spin}(16)$ project to the non-identity (orientation-reversing) coset of the $(10+6)$-stabilizer in $\operatorname{Ss}(16)\subset E_8$.

---

## 3. Duty 3: Centralizer Action, Square $(A h_k)^2$, Circle Inversion, and Centre Detection for $h_1$ and $h_3$

For distinct orthonormal vectors $f_1,f_2,f_3\in V_6$ and $U=e_1^- e_2^- e_3^- e_4^- e_5^-\in\operatorname{Pin}_-(10)$, set the odd-odd Clifford products in $\operatorname{Spin}(16)$:
```text
h_1=U*f_1  (degree 6 in Cl^0(R^16)),  h_3=U*f_1*f_2*f_3  (degree 8 in Cl^0(R^16))
```
1. **Centralization of the ordered compact triples and $K_\alpha$:**
   Conjugation in $\operatorname{Cl}(\mathbb{R}^{16})$ by an even product of orthonormal vectors acts on $\mathbb{R}^{16}$ by $-1$ on their span and $+1$ on their orthogonal complement. Thus on $\mathbb{R}^{16}=V_{5,+}\oplus V_{5,-}\oplus V_6$, $\operatorname{Ad}_{h_k}$ acts as $(+I_5)\oplus(-I_5)\oplus R_{f_1,\dots,f_k}$, where $R_{f_1,\dots,f_k}\in\operatorname{O}_-(6)$ reflects $\operatorname{span}(f_1,\dots,f_k)$ by $-1$ and fixes its $(6-k)$-dimensional complement in $V_6$. On $\mathfrak{so}(V_{5,-})\cong\Lambda^2 V_{5,-}$, $(-I_5)\wedge(-I_5)=+I_{\Lambda^2 V_{5,-}}$, so $\operatorname{Ad}_{h_k}$ fixes both triples $(E_+,E_+^\dagger,H_+)$ and $(E_-,E_-^\dagger,H_-)$. Directly in $\operatorname{Spin}(16)$, every bivector $e_a^+ e_b^+\in\mathfrak{so}(V_{5,+})$ and $e_a^- e_b^-\in\mathfrak{so}(V_{5,-})$ commutes with $U=e_1^-\cdots e_5^-$ (sharing $0$ or $2$ indices) and with $f_1\cdots f_k$ (sharing $0$ indices). Hence $h_k$ commutes in $E_8$ with $\operatorname{Spin}(V_{5,+})\times\operatorname{Spin}(V_{5,-})$, including $K_\alpha=\exp(-i\alpha(H_+-H_-)/2)$ and $P=\exp(-i\pi(H_++H_-)/2)$.

2. **Derivation of $A h_k A^{-1}$, $(A h_k)^2$, and circle inversion in faithful $E_8$:**
   Since $A\in\operatorname{Spin}(10)\subset\operatorname{Cl}^0(V_{5,+}\oplus V_{5,-})$ has even degree, $A$ commutes with $f_1\cdots f_k\in\operatorname{Cl}(V_6)$. Using $A U A^{-1}=W=-C U=\mathrm{Zeta}\,C U$ ($\delta=-1$), $U^2=(-1)^{5\cdot 4/2}=+1$, $U f_a=-f_a U$, $U W=(-1)^{25}W U=-W U$, and $A^2=C^{-1}P=C K_\pi$ (with $K_\pi=\mathrm{Zeta}\,P$ and $C^{-1}=\mathrm{Zeta}\,C$), we obtain:
```text
A*h_k*A^-1=(A*U*A^-1)*f_1...f_k=delta*C*h_k=-C*h_k=Zeta*C*h_k
h_k*C*h_k^-1=U*C*U^-1=-C=Zeta*C=C^-1,  h_k*K_alpha*h_k^-1=K_alpha,  h_k*P*h_k^-1=P
(A*h_k)^2=(A*h_k*A^-1)*A^2*h_k=(delta*C*h_k)*(C*K_pi)*h_k=delta*C*(h_k*C*h_k^-1)*K_pi*h_k^2=delta*K_pi*h_k^2
h_1^2=U*f_1*U*f_1=-U^2*f_1^2=-1_{Spin(16)}|->Zeta  ==>  (A*h_1)^2=Zeta*K_pi*Zeta=K_pi
h_3^2=U*f_1*f_2*f_3*U*f_1*f_2*f_3=-U^2*(f_1*f_2*f_3)^2=+1_{Spin(16)}|->1  ==>  (A*h_3)^2=Zeta*K_pi!=K_pi
(A*h_k)*K_alpha*(A*h_k)^-1=A*(h_k*K_alpha*h_k^-1)*A^-1=A*K_alpha*A^-1=K_{-alpha}
```
Replacing $A$ by the second $\operatorname{Spin}(10)$ lift $\widetilde{A}=\mathrm{Zeta}\,A$ leaves $A h_k A^{-1}$ and $(A h_k)^2$ unchanged because $\mathrm{Zeta}^2=1$.
- **Verdict on $h_1$ vs $h_3$:** **$h_1=U f_1$ satisfies both faithful $\operatorname{Pin}(2)$ relations** $(A h_1)^2=K_\pi$ and $(A h_1)K_\alpha(A h_1)^{-1}=K_{-\alpha}$ across all $248$ $E_8$ coefficients. Conversely, the particular product **$h_3=U f_1 f_2 f_3$ fails the square relation on the $128$ half-root sectors** by the nontrivial central element $\mathrm{Zeta}$ ($(A h_3)^2=\mathrm{Zeta}\,K_\pi=P$), which acts as $+1$ on $120$ and $-1$ on $128$.

---

## 4. Duty 4: Bundle Gluing, Peripheral Commutator, Unbroken $A_3$ Subalgebra, and Matter Action for $A'=A h_1$

For the passing witness $h_1=U f_1$ at the ticket's $\chi=0$ setting, set $A'=A h_1$ and $B'=D A'$ with $D=K_{\pi/2}=\exp(-i\pi(H_+-H_-)/4)$:
```text
Ad_{h_1}(E,G)=(E,G)  ==>  Ad_{A'}(E,G)=(-i*E,+i*G),  Ad_{B'}(E,G)=(-G,+E)
rho(a)*Ad_{A'}(Phi_0)=Phi_0,  rho(b)*Ad_{B'}(Phi_0)=Phi_0,  Phi_0=(E,G)/(2*sqrt(2)*ell)
A'*D*(A')^-1=D^-1,  (B')^2=D*(A'*D*(A')^-1)*(A')^2=(A')^2=K_pi=Zeta*P
[A',B']=A'*(D*A')*(A')^-1*(D*A')^-1=(A'*D*(A')^-1)*D^-1=D^-2=K_pi=Zeta*P,  P*[A',B']=Zeta
(A_3=so(6))^h_1=Lambda^2(f_1^perp)=so(5)  (10-dim fixed gauge subalgebra; 5-dim f_1^f_1^perp negated)
h_1*omega_10*h_1^-1=-omega_10 (h_1*C*h_1^-1=-C),  h_1*omega_6*h_1^-1=-omega_6  ==>  h_1:(16,4)<->(bar16,bar4)
```
1. **Scalar pair and metric preservation:** Because $\operatorname{Ad}_{h_1}$ fixes $E=E_++E_-$ and $G=E_+-E_-$, $(A',B')$ compensates the quaternion flavour holonomy $\rho(a)=F_i,\rho(b)=F_j$ on $\Phi_0=(E,G)/(2\sqrt{2}\ell)$ identically to $(A,B)$. Since $h_1\in E_8$ is compact, the positive Killing metric $\kappa(X^\dagger Y)$ and symplectic form $\varepsilon_F$ remain covariantly preserved.
2. **Peripheral commutator:** Because $A' D(A')^{-1}=D^{-1}$, $[A',B']=D^{-2}=\mathrm{Zeta}\,P$ is unchanged from $[A,B]$, and the combined peripheral cusp transition remains $P[A',B']=\mathrm{Zeta}$ ($+1$ on $120$, $-1$ on $128$).
3. **Unbroken $A_3$ subalgebra and core action on matter ($\chi=0$):** Since $A,D\in\operatorname{Spin}(10)$ commute with $A_3=\mathfrak{so}(6)=\Lambda^2 V_6$, $(A',B')$ act on $(1,15)$ via $\operatorname{Ad}_{h_1}=\Lambda^2 R_{f_1}$, reducing $\mathfrak{so}(6)$ to the $10$-dimensional subalgebra $\mathfrak{so}(5)=\Lambda^2(f_1^\perp)$ of bivectors orthogonal to $f_1$ (while negating the $5$-dimensional space $f_1\wedge f_1^\perp$). Along core cycles $a,b$:
   - On $(45,1)$: $\operatorname{Ad}_{h_1}$ fixes $\mathfrak{so}(5)_+\oplus\mathfrak{so}(5)_-$ ($20$ dims) and negates the mixed coset $V_{5,+}\otimes V_{5,-}$ ($25$ dims).
   - On $(10,6)$: $\operatorname{Ad}_{h_1}$ acts as $(+I_5\oplus-I_5)\otimes R_{f_1}$.
   - On $128=(16,4)\oplus(\overline{16},\overline{4})$: because $h_1=U f_1$ anticommutes individually with $\omega_{10}=-C$ and $\omega_6=-C_6$ while commuting with $\omega_{16}=\omega_{10}\omega_6$, core transport by $A'$ and $B'$ **interchanges the internal $\operatorname{Spin}(10)\times\operatorname{Spin}(6)$ half-spinor summands $(16,4)\leftrightarrow(\overline{16},\overline{4})$** (an internal representation property distinct from physical four-dimensional weak chirality, which requires the fermion operator and weak-current calculation).

---

## 5. Duty 5: Conclusion on the Faithful Compensator Range and Sufficient Exclusion Premise

1. **Constructive outer $\operatorname{Pin}(2)$ witness:** Within the full compact correction centralizer $Z_{E_8}(\mathfrak{so}(5)_+\oplus\mathfrak{so}(5)_-,K_\alpha)$ at $\chi=0$, the odd-odd Clifford coset $\operatorname{Pin}_-(10)\cdot\operatorname{Pin}_-(6)$ in $\operatorname{Ss}(16)\subset E_8$ admits the explicit faithful $\operatorname{Pin}(2)$ witness $h_1=U f_1$ ($A'=A h_1,B'=D A'$), whereas the particular product $h_3=U f_1 f_2 f_3$ is obstructed on $128$ by the source orientation sign $\delta=-1$ ($(A h_3)^2=\mathrm{Zeta}\,K_\pi\neq K_\pi$).
2. **Sufficient correction-range premise and open global classification:** Demanding $\operatorname{Pin}(2)$ coherence, scalar-pair flavour gluing, and peripheral commutator $[A,B]=\mathrm{Zeta}\,P$ in compact $E_8$ does **not** alone force the connected $\operatorname{U}(3)$ electromagnetic phase; $h_1=U f_1$ is an allowed outer alternative fixing $\mathfrak{so}(5)\subset\mathfrak{so}(6)$. Restricting the correction factor $h$ to the **connected centralizer $\operatorname{Spin}(6)$** is a **sufficient extra premise** that excludes the outer witness $h_1$ and yields the unique connected $\operatorname{U}(3)$ electromagnetic phase $h_{\text{em}}$. Between the two explicit compared constructions ($h_{\text{em}}\in\operatorname{Spin}(6)$ vs $h_1=U f_1$), $h_{\text{em}}$ acts trivially on $(45,1)$ and preserves the internal $\operatorname{Spin}(10)$ half-spinor summands $(16,4)$ and $(\overline{16},\overline{4})$, whereas $h_1$ negates $V_{5,+}\otimes V_{5,-}\subset(45,1)$ and swaps $(16,4)\leftrightarrow(\overline{16},\overline{4})$ around core cycles; whether every disconnected centralizer component is exhausted by these properties remains open pending a full disconnected-centralizer classification.
3. **Prospective verification duties (unrun):** Once separately admitted, an executable check should build $U_{\text{real}},A_{\text{vec}},C,U,h_1,h_3$ in the faithful $248$-dimensional $E_8$ representation and verify $A U A^{-1}=\mathrm{Zeta}\,C U$, $(A h_1)^2=K_\pi$, $(A h_3)^2=\mathrm{Zeta}\,K_\pi$, $[A',B']=\mathrm{Zeta}\,P$, the $10$-dimensional fixed $\mathfrak{so}(5)\subset A_3$, and the internal $(16,4)\leftrightarrow(\overline{16},\overline{4})$ swap on $128$.
