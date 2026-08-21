# B8117 — L172: **there is no Fibonacci-anyon device**, and the negative closes a route

**Date:** 2026-08-21 · **Seat:** cc3, audit · **Lane:** LITERATURE (owner-routed package, lane 3).
**Gate 5 untouched.**

> **SCOPE.** A literature pass dated **2026-08-21**, **abstract/summary level, declared**.
> Establishes **what HOSTS the Fibonacci anyons** in each demonstration — a material, or a
> processor — which is the only question L172 asked. It does **not** assess any experiment's
> fidelity, and does **not** claim a native device is impossible — only that **none exists in the
> literature reached**.

---

## The question, and the answer

**Asked:** *what can a Fibonacci-anyon device NATIVELY do today, so the torsor→gate dictionary types
against real hardware claims?*

> ### **Nothing — because there is no Fibonacci-anyon device.** Every demonstration is a **digital simulation** of Fibonacci string-nets on a **gate-based processor**.

| cite | what it is | the decisive clause |
|---|---|---|
| **`arXiv:2404.00091`** · *Nat. Phys.* `s41567-024-02529-6` (2024) | Fibonacci string-net **simulated on 27 superconducting TRANSMONS**; topological entanglement entropy verified; two anyon pairs created; fusion and braiding shown | *"by applying unitary gates on the **underlying physical qubits**"* — the braid is **implemented by qubit gates**, not by moving quasiparticles in a material |
| ***Nat. Commun.* `s41467-025-61493-8`** (2025) | string-net condensation, Fibonacci braiding for universal gates | realized **ON a processor** — simulation, not a material host |
| ***Nature* `s41586-026-10709-y`** (15 Jul 2026) | **the current hardware state of the art for UNIVERSALITY**: 54 qubits, Quantinuum H2, non-Abelian **S₃** order; universal via braiding **plus FUSION as a primitive**; magic state prepared topologically | the platform that reached universality did it with **S₃, not Fibonacci**, and **needed fusion** — braiding alone did not suffice |
| **Kliuchnikov–Bocharov–Svore**, *PRL* **112**, 140504 (2014); `arXiv:1310.4150` | compiles a single-qubit unitary into a Fibonacci **braid pattern**, asymptotically depth-optimal; classifies the exactly-implementable unitaries | the direction is **unitary → braid**: the braid is a **compiler OUTPUT given a target**, never a measurement |

## ⚠ The consequence for the torsor→gate dictionary

> **A golden-ratio structure appearing in a compiled Fibonacci braid is PUT IN by the simulation,
> not READ OUT of hardware.**

So a dictionary typed *"against real hardware claims"* **has no hardware to type against**, and any
crossing resting on *"the device natively realizes the golden structure"* would be **circular** —
**the device realizes what the compiler was told to realize.**

## The class the negative names

**Anything requiring a NATIVE non-abelian golden substrate.** The boundary is **SIMULATION vs
REALIZATION** — **not a precision boundary.** No improvement in qubit count or fidelity crosses it,
because **the golden content enters through the compiler at every scale.**

## ⚠ And it composes with B8111, which closes a route

B8111 established that the discriminating content of the tone-level crossing is exactly **`φ/2` and
`1/(2φ)`**, at resolution better than **`0.101910213188`**. **On a simulated braid those values are
INPUTS TO THE COMPILER.**

> **One cannot measure to `0.1019` a quantity one supplied.** The resolution requirement is
> unmeetable **in principle**, not in practice.

**Therefore the anyon-device route to L179 (*are the tones observables?*) is CLOSED for now.** The
**surviving** route is the condensed-matter one catalogued in **B8094** — photonic and cold-atom
quasicrystals — where the golden structure sits **in the material** and **the phason is a physical
dial, not a compiler argument.**

**That is the useful output of this lane: of two candidate experimental anchors, it says which one
is live.**

## Not found — recorded, not dropped

**Parzanchevski–Sarnak "golden gates"** was searched for and **did not appear in the returned
results**. It is **not cited here** — recorded as not-found rather than quietly omitted, and rather
than cited from memory.

## Artifacts

`results.json` · `tests/test_b8117_l172_anyon_devices.py`
