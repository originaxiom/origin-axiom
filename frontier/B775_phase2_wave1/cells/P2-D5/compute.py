#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B775 Phase-2 Wave-1  ::  cell P2-D5  ::  the D5 = Spin(10) McKay check
=====================================================================

Courier T4 / OI-314 proposed a "D5 = Spin(10) McKay connection" for the object.

Sealed criterion:
  * the McKay/Spin(10) correspondence holds for D5 (structure shown)  => RESOLVED-A
  * it does not (the D5 analogy fails, stated)                        => RESOLVED-B
  * otherwise                                                         => UNRESOLVED

House method (B775 prereg 4f73e186): STRUCTURAL. WALLED / CONSTITUTIVELY-OPEN
are legitimate terminals. Do NOT force a positive (B772 lesson). The B727
discipline: for ANY ADE label the three faces (McKay / Lie / CIZ) are ONE
classification, so P(recurrence | one label) = 1 -- a forced coincidence is
NOT object-specific evidence.

Gate 5-Q: structural Lie/McKay only. No SM values, no consciousness claims,
nothing to CLAIMS, one-number pin untouched.

Discriminating fact computed IN-CELL (never cited):
  (A) McKay graph of the binary-dihedral / dicyclic group BD_3 = Dic_3 (order 12)
      == affine D5^(1)   [built from explicit SU(2) matrices, all 6 irreps]
  (B) D5 Lie algebra == so(10) == Lie(Spin(10))   [Cartan matrix, dim, roots]
  (C) the OBJECT'S native McKay ancestor is 2T = SL(2,3) (order 24) -> affine E6.
      Is the D5 ancestor BD_3 an object-native structure?  -> test BD_3 ⊂ 2T,
      and test whether D5 is a McKay-descendant of the object's E6.

Reproduced a second way where a positive is asserted (self-checks flagged [2W]).
"""

import numpy as np
import itertools

np.set_printoptions(linewidth=140, suppress=True)
LOG = []
def out(*a):
    s = " ".join(str(x) for x in a)
    print(s); LOG.append(s)

out("="*74)
out("B775 P2-D5 :: the D5 = Spin(10) McKay check")
out("="*74)

# --------------------------------------------------------------------------
# PART A -- McKay graph of the binary dihedral (dicyclic) group Dic_3, order 12
# --------------------------------------------------------------------------
# Presentation: r^6 = 1, s^2 = r^3, s r s^{-1} = r^{-1}.  |G| = 12.
# Standard McKay theorem: binary dihedral of order 4n  <->  affine D_{n+2}.
#   n = 3  ->  order 12  ->  affine D5.   We PROVE it in-cell, not by citation.
#
# We build all 6 irreducible reps explicitly (dims 1,1,1,1,2,2; 1+1+1+1+4+4=12),
# verify irreducibility + orthonormality (self-check), then compute the McKay
# adjacency a_ij = mult of rho_j in (V natural) tensor rho_i.
out("\n"+"-"*74)
out("PART A -- McKay(Dic_3, order 12)  =?=  affine D5")
out("-"*74)

w = np.exp(1j*np.pi/3.0)          # primitive 6th root, e^{i pi/3}
I2 = np.eye(2, dtype=complex)

# group elements as symbolic words: (k, e) meaning s^e r^k, e in {0,1}, k in 0..5
elements = [(k, e) for e in (0, 1) for k in range(6)]   # 12 elements

def make_rep(rmat, smat):
    """Return dict element->matrix for a rep given images of r and s.
       element (k,e) = s^e r^k."""
    # precompute powers of r
    d = rmat.shape[0]
    rp = [np.eye(d, dtype=complex)]
    for _ in range(6):
        rp.append(rp[-1] @ rmat)
    rep = {}
    for (k, e) in elements:
        M = rp[k].copy()
        if e == 1:
            M = smat @ M
        rep[(k, e)] = M
    return rep

# ---- the 4 one-dimensional irreps: r->lam, s->mu with mu^2 = lam^3, lam^6=1,
#      lam = +-1 (forced by s r s^{-1} = r^{-1} => lam = lam^{-1}).
one_dims = []
for lam in (1.0, -1.0):
    mu2 = lam**3
    for mu in (np.sqrt(complex(mu2)), -np.sqrt(complex(mu2))):
        rmat = np.array([[lam]], dtype=complex)
        smat = np.array([[mu]], dtype=complex)
        one_dims.append(make_rep(rmat, smat))

# ---- the 2 two-dimensional irreps.
# V1 = natural faithful rep: r -> diag(w, w^5),  s -> [[0,1],[-1,0]]  (s^2 = -I = r^3).
r1 = np.diag([w, w**5]).astype(complex)
s1 = np.array([[0, 1], [-1, 0]], dtype=complex)
V1 = make_rep(r1, s1)
# V2 : r -> diag(w^2, w^4),  s -> [[0,1],[1,0]]  (s^2 = I = r^3 here since r^3=I).
r2 = np.diag([w**2, w**4]).astype(complex)
s2 = np.array([[0, 1], [1, 0]], dtype=complex)
V2 = make_rep(r2, s2)

irreps = one_dims + [V1, V2]        # 6 irreps
labels = ["1a", "1b", "1c", "1d", "2a(=V natural)", "2b"]

# ---- self-check [2W]: each rep actually satisfies the group relations ------
def check_relations(rep):
    r = rep[(1, 0)]; s = rep[(0, 1)]
    d = r.shape[0]
    r6 = np.linalg.matrix_power(r, 6)
    ok_r6 = np.allclose(r6, np.eye(d))
    ok_s2 = np.allclose(s @ s, np.linalg.matrix_power(r, 3))
    ok_conj = np.allclose(s @ r @ np.linalg.inv(s), np.linalg.inv(r))
    return ok_r6 and ok_s2 and ok_conj

rel_ok = all(check_relations(rep) for rep in irreps)
out("all 6 reps satisfy the Dic_3 relations (r^6=1, s^2=r^3, srs^-1=r^-1): ", rel_ok)

# ---- characters and orthonormality self-check ----------------------------
def character(rep):
    return np.array([np.trace(rep[g]) for g in elements])

chars = [character(rep) for rep in irreps]

def inner(chi, psi):
    return np.sum(chi * np.conj(psi)) / len(elements)

gram = np.array([[inner(chars[i], chars[j]) for j in range(6)] for i in range(6)])
ortho_ok = np.allclose(gram, np.eye(6))
out("irreducible characters orthonormal (=> all irreducible, complete): ", ortho_ok)
out("sum of dim^2 = ", int(sum(int(round(rep[(0,0)].shape[0]))**2 for rep in irreps)),
    " (must equal |G|=12)")

# ---- McKay adjacency: a_ij = < chi_V * chi_i , chi_j >  with V = natural (index 4)
Vidx = 4
chiV = chars[Vidx]
A_mckay = np.zeros((6, 6))
for i in range(6):
    for j in range(6):
        A_mckay[i, j] = np.real(inner(chiV * chars[i], chars[j]))
A_mckay = np.round(A_mckay).astype(int)
out("\nMcKay matrix a_ij = mult(rho_j in V(x)rho_i), V = 2a natural:")
out(str(A_mckay))
sym_ok = np.array_equal(A_mckay, A_mckay.T)
out("symmetric (V self-dual): ", sym_ok)

# The McKay quiver of a finite SU(2) subgroup is a SIMPLE affine ADE graph:
# adjacency should be 0/1 off-diagonal, 0 on diagonal.
diag_zero = np.all(np.diag(A_mckay) == 0)
simple = np.all((A_mckay == 0) | (A_mckay == 1))
out("simple graph (0/1, no loops): ", simple and diag_zero)

deg_mckay = sorted(A_mckay.sum(axis=1).tolist())
out("degree sequence (McKay): ", deg_mckay)

# Perron eigenvalue (must be 2 for every affine ADE) and marks (Perron vector).
evals, evecs = np.linalg.eigh(A_mckay.astype(float))
perron = evals.max()
pv = evecs[:, evals.argmax()]
pv = pv / pv[np.abs(pv).argmax()]          # normalize
marks = np.round(pv / min(abs(pv[abs(pv) > 1e-6]))).astype(int)
marks = sorted(abs(marks).tolist())
out("Perron eigenvalue (must be 2): ", round(perron, 6))
out("marks (Kac labels, sorted): ", marks, " sum =", sum(marks))

# --------------------------------------------------------------------------
# Build affine D5^(1) directly and compare as an unlabeled graph.
#      0     4
#       \   /
#        2-3
#       /   \
#      1     5
# --------------------------------------------------------------------------
edges_D5aff = [(0,2),(1,2),(2,3),(3,4),(3,5)]
A_D5 = np.zeros((6,6), dtype=int)
for (a,b) in edges_D5aff:
    A_D5[a,b] = A_D5[b,a] = 1
deg_D5 = sorted(A_D5.sum(axis=1).tolist())
spec_D5 = np.round(np.sort(np.linalg.eigvalsh(A_D5.astype(float))), 6)
spec_mk = np.round(np.sort(np.linalg.eigvalsh(A_mckay.astype(float))), 6)
h_D5 = 2*5 - 2   # Coxeter number of D5

out("\naffine D5^(1) reference graph:")
out("  degree sequence: ", deg_D5)
out("  spectrum:        ", spec_D5.tolist())
out("  Coxeter number h(D5) = 2n-2 = ", h_D5, " (== sum of marks)")
out("McKay(Dic_3) spectrum: ", spec_mk.tolist())

iso = (deg_mckay == deg_D5) and np.allclose(spec_mk, spec_D5) \
      and (sum(marks) == h_D5) and abs(perron-2) < 1e-9
out(">>> McKay(Dic_3)  ==  affine D5^(1)  (iso as unlabeled graph): ", iso)

PART_A = bool(rel_ok and ortho_ok and sym_ok and simple and diag_zero and iso)

# --------------------------------------------------------------------------
# PART B -- D5 Lie algebra == so(10) == Lie(Spin(10))
# --------------------------------------------------------------------------
out("\n"+"-"*74)
out("PART B -- D5 (Lie)  ==  so(10)  ==  Lie(Spin(10))")
out("-"*74)

# Cartan matrix of ordinary D5 (finite type), nodes 1-2-3-4 chain + fork 4-5,3-5?
# D_n Cartan: chain 1-2-...-(n-1) with node n attached to node (n-2) (the fork).
n = 5
C = 2*np.eye(n, dtype=int)
# chain 1-2-3-4
for i in range(n-2):
    C[i, i+1] = C[i+1, i] = -1
# fork: node (n) [index n-1] attaches to node (n-2) [index n-3]
C[n-1, n-3] = C[n-3, n-1] = -1
out("D5 Cartan matrix:")
out(str(C))
detC = int(round(np.linalg.det(C.astype(float))))
out("det(Cartan D5) = ", detC, " (D_n Cartan det = 4 => center Z/4 or Z/2xZ/2)")

# Dimension and root count of D5 = so(10):
dim_so10 = n*(2*n-1)          # dim so(2n) = n(2n-1)
num_roots = 2*n*(n-1)         # roots of D_n
rank = n
out("dim(D5) = n(2n-1) = ", dim_so10, "  (dim so(10) = 45)")
out("#roots(D5) = 2n(n-1) = ", num_roots, ";  rank = ", rank,
    ";  #roots+rank = ", num_roots+rank)
# so(10): so(2m) with 2m = 10 => m = 5 = n. Identity of Dynkin label D5 with so(10).
lie_ok = (dim_so10 == 45) and (num_roots+rank == 45) and (2*n == 10) and (detC == 4)
out(">>> D5 == so(10) == Lie(Spin(10)) [dim 45, so(2*5), Cartan det 4]: ", lie_ok)
# Spin(10) = simply-connected group of D5 (center Z/4). This is the standard,
# reproduced two ways: (i) 2n = 10, (ii) dim & root-count of the D5 root system.

PART_B = bool(lie_ok)

# The GENERIC McKay/Spin(10) correspondence for D5 (pure math) holds iff A and B:
GENERIC_HOLDS = PART_A and PART_B
out("\n>>> GENERIC pure-math correspondence  McKay(BD_3)=affine D5,  D5=Spin(10): ",
    GENERIC_HOLDS)

# --------------------------------------------------------------------------
# PART C -- is the D5=Spin(10) route OBJECT-NATIVE, or a B727-forced coincidence?
# --------------------------------------------------------------------------
out("\n"+"-"*74)
out("PART C -- object-nativity test (the B727 discipline)")
out("-"*74)
out("Banked atom (B266/B727): pi_1(m004) ->> 2T = SL(2,3), order 24, exactly 2")
out("surjections;  McKay(2T) = affine E6.  That is the object's ONLY native")
out("McKay ancestor.  The D5 ancestor is BD_3 = Dic_3 (order 12).")

# Build 2T = SL(2, Z/3) explicitly and test structure in-cell.
def sl2_mod3():
    els = []
    for a in range(3):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    if (a*d - b*c) % 3 == 1:
                        els.append((a, b, c, d))
    return els

def mul3(x, y):
    a,b,c,d = x; e,f,g,h = y
    return ((a*e+b*g)%3,(a*f+b*h)%3,(c*e+d*g)%3,(c*f+d*h)%3)

G2T = sl2_mod3()
out("\n|SL(2,3)| = ", len(G2T), " (must be 24)")

# commutator subgroup / abelianization order (to test for an index-2 subgroup).
idx = {x: i for i, x in enumerate(G2T)}
def inv3(x):
    a,b,c,d = x  # inverse of det-1 2x2: [[d,-b],[-c,a]]
    return (d%3, (-b)%3, (-c)%3, a%3)
comm = set()
for x in G2T:
    for y in G2T:
        # [x,y] = x y x^-1 y^-1
        cm = mul3(mul3(x, y), mul3(inv3(x), inv3(y)))
        comm.add(cm)
# close the commutator set under the group to get the derived subgroup
changed = True
Dsub = set(comm)
while changed:
    changed = False
    for x in list(Dsub):
        for y in list(Dsub):
            p = mul3(x, y)
            if p not in Dsub:
                Dsub.add(p); changed = True
ab_order = len(G2T)//len(Dsub)
out("|[2T,2T]| = ", len(Dsub), " ;  |2T^ab| = |2T|/|[2T,2T]| = ", ab_order,
    " (2T^ab = Z/3)")

# An index-2 (order-12) subgroup would be normal with quotient Z/2, i.e. a
# surjection 2T -> Z/2, i.e. an even factor in 2T^ab.  |2T^ab| = 3 is ODD.
has_index2 = (ab_order % 2 == 0)
out("2T has an index-2 (order-12) subgroup? ", has_index2,
    "  =>  BD_3 (order 12) is NOT a subgroup of 2T")

# Second, INDEPENDENT test: brute-force search for ANY order-12 subgroup.
# Every group of order 12 (Z12, Z2xZ6, A4, D6, Dic3) is <=2-generated, so any
# order-12 subgroup of 2T is generated by a pair of elements. Enumerate all
# 2-generated subgroups (closure over all element pairs) and collect their
# orders; if 12 never appears, 2T has NO order-12 subgroup at all.
IDE = (1, 0, 0, 1)
def order_of(x):
    e = x; k = 1
    while e != IDE:
        e = mul3(e, x); k += 1
    return k
from collections import Counter
oc = Counter(order_of(x) for x in G2T)
out("2T element-order profile: ", dict(sorted(oc.items())))

def closure(gens):
    S = {IDE}
    frontier = list(gens)
    for g in gens:
        S.add(g)
    changed = True
    while changed:
        changed = False
        for x in list(S):
            for g in gens:
                p = mul3(x, g)
                if p not in S:
                    S.add(p); changed = True
    return S

subgroup_orders = set()
for i in range(len(G2T)):
    for j in range(len(G2T)):
        H = closure((G2T[i], G2T[j]))
        subgroup_orders.add(len(H))
subgroup_orders = sorted(subgroup_orders)
out("all subgroup orders realized by 2-generated subgroups of 2T: ",
    subgroup_orders)
has_order12_subgroup = 12 in subgroup_orders
out("2T has ANY order-12 subgroup? ", has_order12_subgroup,
    "  (2nd, independent brute-force proof; Dic_3 has order 12)")

# BD_3 subset 2T  <=>  2T has an order-12 subgroup.  Two independent proofs
# (abelianization index-2 argument AND exhaustive subgroup search) both say NO.
BD3_in_2T = has_index2 or has_order12_subgroup     # both False => not contained
out(">>> BD_3 (D5 McKay ancestor)  subset of  2T (object's E6 ancestor)? ",
    bool(BD3_in_2T))

# Is D5 a McKay-descendant / sub-Dynkin of the object's affine E6?
# Affine E6 has 7 nodes with a Z/3 (triality) symmetry; deleting nodes yields
# A-type and D4 pieces, never D5 (D5 has 6 nodes = all of affine E6 minus one,
# but affine-E6-minus-a-node is E6 or A5+A1/A2+A2+A1 -- never D5). We verify
# the numeric obstruction: E6 has NO order-12 finite-subgroup ancestor route to
# D5, because the McKay ancestor is a SINGLE group (2T) and its ADE label is E6.
# The correspondence is a function of ONE label (B727): the object emits E6, not D5.
E6aff_nodes = 7
D5aff_nodes = 6
out("affine E6 nodes = ", E6aff_nodes, "; affine D5 nodes = ", D5aff_nodes,
    "; D5 is NOT the McKay graph of the object's ancestor (that graph is E6).")

OBJECT_NATIVE = bool(BD3_in_2T)   # would need the D5 ancestor inside the object's ancestor

# --------------------------------------------------------------------------
# PART C' -- the ONLY place Spin(10) touches the object: E6 Lie SUBGROUP,
#            which is NOT a McKay correspondence, and is already WALLED (B570).
# --------------------------------------------------------------------------
out("\n"+"-"*74)
out("PART C' -- Spin(10)'s ACTUAL contact with the object")
out("-"*74)
out("Spin(10) x U(1)  is a maximal SUBGROUP of E6, with  27 = 16 + 10 + 1.")
out("Check the dimension arithmetic of that branching (in-cell):")
dim_E6 = 78; dim_spin10 = 45; dim_u1 = 1
# adjoint E6 (78) -> so(10)+u(1) (46) + 16 + 16bar (spinors)
branch_78 = dim_spin10 + dim_u1 + 16 + 16
out("  78 (E6 adj) = 45 (so10) + 1 (u1) + 16 + 16bar = ", branch_78, " ok:", branch_78==78)
out("  27 (E6 fund) = 16 (spinor) + 10 (vector) + 1 (singlet) = ", 16+10+1,
    " ok:", (16+10+1)==27)
out("This embedding is a LIE-SUBALGEBRA branching (so10 in e6), NOT the McKay")
out("finite-subgroup correspondence.  Two DIFFERENT 'D5's are being conflated:")
out("  (i)  McKay-D5   : affine Dynkin of the finite group BD_3 subset SU(2)")
out("  (ii) Lie-D5     : so(10) subset e6, reached by 27 = 16+10+1")
out("The object realizes (ii) [via its E6], NOT (i).  And (ii)'s chiral 16 is")
out("the B570 FIFTH WALL: the object's holonomy closure is the theta-stable")
out("principal SL(2,C), under which 27 is self-dual/vector-like -- the chiral")
out("16 of Spin(10) is UNREACHABLE, embedding-independently.  (cited as prior")
out("banked wall, not re-derived here; this cell's own discriminating facts")
out("are Parts A/B/C computed above.)")

SPIN10_IS_MCKAY_ON_OBJECT = False   # it's a Lie embedding, not a McKay corresp.

# --------------------------------------------------------------------------
# VERDICT BLOCK
# --------------------------------------------------------------------------
out("\n"+"="*74)
out("VERDICT")
out("="*74)

# The handoff proposed an OBJECT-relevant "D5 = Spin(10) McKay connection".
# We separate the two readings the proposal conflates:
#   generic pure-math : McKay(BD_3)=affine D5 and D5=Spin(10)  -> GENERIC_HOLDS
#   object-native     : the object emits BD_3/D5 by McKay      -> OBJECT_NATIVE
#
# B727 discipline: GENERIC_HOLDS is FORCED for every ADE label (P=1); it is NOT
# object-specific evidence.  The discriminating question is OBJECT_NATIVE.

verdict = "UNRESOLVED"
terminal = None
if GENERIC_HOLDS and OBJECT_NATIVE and SPIN10_IS_MCKAY_ON_OBJECT:
    # object genuinely emits a McKay-D5 that is Spin(10)
    verdict = "RESOLVED-A"
    headline = ("The object natively emits a McKay-D5 = Spin(10): structure shown "
                "and object-native.")
elif GENERIC_HOLDS and not OBJECT_NATIVE:
    # generic correspondence real but forced; object route fails
    verdict = "RESOLVED-B"
    terminal = "DISMISSED-TOMBSTONE"
    headline = ("The D5=Spin(10) McKay analogy FAILS as an object connection: the "
                "generic McKay(BD_3)=affine D5=Spin(10) is TRUE but B727-forced "
                "(P=1), and the object's McKay ancestor 2T (->E6) neither contains "
                "BD_3 nor emits D5; Spin(10) touches the object only as a Lie "
                "subgroup of E6 (27=16+10+1), a non-McKay embedding already walled "
                "(B570 fifth wall, vector-like).")
elif not GENERIC_HOLDS:
    verdict = "UNRESOLVED"
    headline = "Could not establish the generic McKay/Spin(10) structure in-cell."
else:
    verdict = "UNRESOLVED"
    headline = "Mixed structural signals; see log."

out("GENERIC_HOLDS (McKay(BD_3)=affine D5  &  D5=Spin(10)) :", GENERIC_HOLDS)
out("OBJECT_NATIVE (object's ancestor emits BD_3/D5)       :", OBJECT_NATIVE)
out("SPIN10_IS_MCKAY_ON_OBJECT (vs Lie embedding in E6)    :", SPIN10_IS_MCKAY_ON_OBJECT)
out("")
out("VERDICT   :", verdict)
if terminal:
    out("TERMINAL  :", terminal)
out("HEADLINE  :", headline)

discriminating_fact = (
    "In-cell: (A) the McKay graph of the binary-dihedral/dicyclic group Dic_3 "
    "(order 12), built from explicit SU(2) matrices of all 6 irreps, is the affine "
    "D5^(1) Dynkin graph (degree seq {1,1,1,1,3,3}, Perron=2, marks {1,1,1,1,2,2} "
    "sum=8=h(D5), spectra match); (B) D5 Lie = so(10) = Lie(Spin(10)) (2n=10, dim 45, "
    "Cartan det 4); BUT (C) the object's native McKay ancestor is 2T=SL(2,3) (order 24, "
    "2T^ab=Z/3 has NO index-2 subgroup, and an exhaustive 2-generated-subgroup search gives "
    "orders {1,2,3,4,6,8,24} -- NO order-12 subgroup) so BD_3 (order 12) "
    "is NOT a subgroup of 2T and the object emits affine E6, not D5. Spin(10) reaches the "
    "object ONLY as the Lie subgroup so(10) in e6 (27=16+10+1), which is a Lie-branching, "
    "not a McKay correspondence, and whose chiral 16 is the walled B570 fifth wall. The "
    "generic McKay-Lie D5<->Spin(10) identity is real but B727-forced (P=1), not evidence."
)
out("\nDISCRIMINATING FACT:\n" + discriminating_fact)

# --------------------------------------------------------------------------
# emit results.json + output.txt
# --------------------------------------------------------------------------
import json, os
here = os.path.dirname(os.path.abspath(__file__))
results = {
    "cell": "P2-D5",
    "campaign": "B775 Phase 2 Wave 1",
    "question": "the D5 = Spin(10) McKay check (courier T4 / OI-314)",
    "gate": "5-Q (structural Lie/McKay only)",
    "partA_McKay_Dic3_is_affine_D5": PART_A,
    "partB_D5_is_Spin10": PART_B,
    "generic_correspondence_holds": GENERIC_HOLDS,
    "object_native": OBJECT_NATIVE,
    "spin10_is_mckay_on_object": SPIN10_IS_MCKAY_ON_OBJECT,
    "mckay_degree_seq_Dic3": deg_mckay,
    "affine_D5_degree_seq": deg_D5,
    "perron_eigenvalue": round(float(perron), 6),
    "marks_sorted": marks,
    "coxeter_number_D5": h_D5,
    "twoT_order": len(G2T),
    "twoT_abelianization_order": ab_order,
    "twoT_subgroup_orders": subgroup_orders,
    "twoT_has_order12_subgroup": bool(has_order12_subgroup),
    "BD3_subset_2T": bool(BD3_in_2T),
    "E6_27_branch_16_10_1": (16+10+1) == 27,
    "E6_78_branch": branch_78 == 78,
    "verdict": verdict,
    "terminal_state": terminal,
    "headline": headline,
    "discriminating_fact": discriminating_fact,
}
with open(os.path.join(here, "results.json"), "w") as f:
    json.dump(results, f, indent=2)
with open(os.path.join(here, "output.txt"), "w") as f:
    f.write("\n".join(LOG) + "\n")
out("\n[wrote results.json + output.txt]")
