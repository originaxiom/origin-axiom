import json,re
d={e['id']:e for e in json.load(open('../../frontier/B738_pathfinder_compiler/kill_graph.json'))}
def q(i):
    e=d[i]; kf=str(e.get('kill_form')).replace('\n',' ')
    if len(kf)>30: t=kf
    else: t=f"[{kf}] "+str(e['claim_killed']).replace('\n',' ')
    t=t.replace('|','/')
    return t[:135].rstrip()+('...' if len(t)>135 else '')
C=[]
def add(cid,commit,ids,named,why):
    for i in ids: assert i in d,i
    C.append((cid,commit,ids,named,why))
add('W-01',"The mass-and-mixing frame is B1656's point coupling: four spin-structure channels on the fibre torus, a Higgs that is a modular form of the single fibre modulus tau, an end radius from the canonical cusp, read at a rigid address (line, horocycle, reading, c = 3).",
 ['B1660','B1668','B1696','B1698','B1699','B1702','B1711','B1712','B1713','B1720','B1722','B1723','B1729','B1732','B1740','B1743','B1744','B1746','B1748','B1789','B1790','B1791','B1792','B1793','B1795','B1798','B1811','B1814','B1817','B1823','B1825'],
 'RECORD NAMES IT. Each of these entries carries a scope.frame field of the form "B1656\'s frame/coupling ..." (or FR-FIB / its multiplier), and the hatches say so in words: B1668 "another frame or end condition", B1711 "another Higgs section", B1811 "a frame other than B1656\'s", B1817/B1790 "a non-point coupling", B1825 "a larger reach ... the mixing as the meeting of two addresses (P-555; P-415\'s towers)". The memory/FIELD STAGE note records B1653: a point coupling has rank <= 2 (a single-tower wall, P-415).',
 'Not inferred; the cluster is the late programme\'s dominant scope.')
add('W-02',"One Higgs object, holomorphic and nearly null, read the same way in every sector (an adjoint-type direction pushed onto the C^3 null cone by the hierarchy), with no identity/singlet channel and no twist of its own.",
 ['B1642','B1644','B1740','B1743','B1744','B1746','B1748','B1790','B1795','B1825'],
 'RECORD NAMES IT (partly). B1826 FINDINGS: "a hierarchy pushes the Higgs vector towards the C^3 null cone, locking both sectors\' lightest left vector ... a frame that keeps both sectors\' lightest vector on one sector-blind direction cannot carry the CKM\'s corners in the measured order". The lock itself is B1739 (the Higgs is nearly null; r falls like e^(-pi Im tau)). P-562 (the Higgs\'s own hypercharge twist) and P-366 (every single holomorphic or antiholomorphic section is exactly null, tends to I = 1, or falls like C e^(-pi Im tau)) state it as a frame property. The Higgs "reading" (S vs S-tilde) is B1790/P-295/P-394.',
 'The wall-to-commitment link for B1825 is stated by B1826; for B1642/B1644/B1795 I infer it from their kill_forms (antisymmetric pairing, exact zero from Jacobi, shared light members).')
add('W-03',"A single shared modulus tau (and a single address) for up, down and lepton sectors; tau is a free or fitted continuous number, never placed by the object.",
 ['B1617','B1673','B1696','B1698','B1699','B1702','B1711','B1712','B1713','B1720','B1722','B1723','B1791','B1825'],
 'RECORD NAMES IT for the end of the chain: B1826/P-555 ("the mixing as the meeting of two addresses ... the up and down sectors\' diagonalisations at different loci"), B1791 ("Im tau is not found forced in B1656\'s frame"), P-343/P-373 ("what fixes Im tau ~ 3.03"), P-328 ("five inputs unruled (tau, the line, the horocycle, the reading, the lepton factor)"). The shared-tau commitment is INFERRED by me for the individual tau-census walls (B1696-B1723): their hatches ask for "a principle that selects the point" without saying the single-tau choice is the cause.',
 'Named at B1825/B1826/P-555; inferred for B1696-B1723.')
add('W-04',"Hand-set discrete inputs: the lepton/down Georgi-Jarlskog factor c = 3, the sector reading rule (which sector reads the conjugate Higgs), the line order, the horocycle.",
 ['B1729','B1789','B1790','B1792','B1793','B1798','B1817'],
 'RECORD NAMES IT. P-294 "derive the lepton factor 3", P-295/P-394 "derive the reading rule", P-402 "the horocycle is a counted discrete input with no row", P-328 the input ledger. B1798: "the lepton factor c = 3 was chosen on the same data and the null holds it fixed"; B1817: "no limit tracks N_c and none is 3 at N_c = 3".',
 'Named.')
add('W-05',"The test convention: specificity is measured against random hierarchical targets (and a class-choosing null), and the look count prices every discrete choice; this makes most fits that reach the six 'generic' (0.12% - 26.8% of random hierarchies fit as well).",
 ['B1668','B1696','B1698','B1702','B1711','B1712','B1713','B1720','B1722','B1732','B1748','B1798','B1814','B1823','B1825','B995','B1340','B1096','B971','B1007','B1338','B986','B1452'],
 'RECORD NAMES IT as a convention, not as a cause of the miss: B1798 "(R71-1) THE_BAR\'s PASSED once the null lets each random target choose its own line class", P-446/P-447 (price c by the nine values scanned), P-418 (one honest scoreboard), P-554 ("the six do not compress, even at a frame address"). The earlier instrument-blind walls (B995, B1340, B1096, B971, B1007, B1338, B986, B1452) are self-identified "a check that cannot fail" (P-317, E2/MB12). I infer the grouping.',
 'Partly named (B1798, P-317, P-554); grouping inferred.')
add('W-06',"Chirality and the generation count are read as a cohomological index of the object (or of its covers/companions/cusps) in a flat E6 or SM-frame module; the index is mirror-even/dual-odd, so the object's own symmetries kill it.",
 ['B1084','B1086','B1259','B1267','B1291','B1295','B1296','B1297','B1322','B1330','B1335','B1442','B1455','B1470','B1480','B1493','B1495','B1498','B1499','B1602','B1603','B1610','B1794','B252','B279','W5-B565-T3/B605','W8-B643/B658','W9-B644/B650'],
 'RECORD NAMES IT. B1086 "Poincare duality ... totals are structurally blind to handedness"; B1455 "the class index is invariant under pullback by any symmetry ... and odd under dualising"; B1603 hatch "the chirality from something other than the index (B1487: the index is mirror-even)"; B1480 "the index under the mirror\'s swap of spin structures". B1267: "the wall extends past closedness AND past the abelian sector".',
 'Named, in the kill graph itself.')
add('W-07',"The gauge algebra is the centralizer of an abelian or finite image of the holonomy (2T, a torus, Zariski-dense or not), so it is abelian and of the wrong rank; non-abelian holonomy and non-principal embeddings are the only other routes.",
 ['B854','B925','B959','B960','B1094','B1140','B1258','B1336','B574','B561'],
 'RECORD NAMES IT. B1336: "ABELIAN OR NOTHING, by Borel density ... B854\'s u(1)^4 is the centralizer of 2T, the FINITE McKay image, which is a different object from the geometric holonomy; conflating them is what left the half looking open." B1094 hatch: "NON-ABELIAN holonomy -- the single live hatch". B959: "the torality step assumes the SIMPLY CONNECTED form of E6".',
 'Named.')
add('W-08',"The Standard Model's gauge algebra and matter are hosted by one geometric tower/frame at a time (flat G2 orbifold, Spin(10) on the 3-cycle, an F-theory 7-brane configuration), instead of by several towers meeting at loci.",
 ['B1084','B1259','B1805','B1808','B1812','B299','B305'],
 'RECORD NAMES IT. The owner\'s P-415 ("is it possible that the reality finally emerges as the interaction of what\'s allowed on all towers, instead of the thread going through one of them") is registered as the live successor; B1812\'s kill ends "the towers-meeting-at-loci reading ... in this frame"; B1259: "Chiral matter by the G2 route requires genuine CURVATURE ... a different construction".',
 'Named (P-415, B1812, B1259).')
add('W-09',"SM values are read from the object's banked numbers by a kind-matched pairing (couplings to moduli, phases to CP, boundary + desert to couplings, regulators to ratios), with measured data contacted by sealed one-shot windows.",
 ['B915','B925','B1005','B1006','B1027','B1063','B1066','B1075','B1076','B1137','B1142','B579','B687','B558','B539','B703','B332','B321','B1096'],
 'PARTLY NAMED. B1066/B1075 name "THE LISTENER MAP: the fine identification of physical apparatus with listener state ... does not exist as banked mathematics"; B1076 "which-datum-picks-the-gauge"; B915 "The desert assumption died, not the boundary"; B1005 "The falsifier fires FOR THE ENUMERATED SPACE, NOT IN PRINCIPLE". The one-shot-window convention (B1063: "the refresh was one-shot and is SPENT") is a test convention the record states; that it is the cause of the misses is not claimed.',
 'Named for the identification gaps; inferred for the one-shot convention.')
add('W-10',"The object is one manifold (m004, the golden word) or one word state, and its arithmetic fields (Q(sqrt-3), Q(sqrt5), McKay groups) are credited as object-specific.",
 ['B307','B996','B1062-V2-axis','B258-silver-inference','B693','B727','B1165','B1157','B1142','B1222','B1330','B225','B313','B443'],
 'RECORD NAMES IT in the standing rule (memory: "THE OBJECT IS THE FAMILY, NOT m004") and in the kills: B996 "access to the McKay group 2T ... is specific to the golden grammar" (genericity); B1165 "the closing is CO-LOCATED with the gravitational sector ... not identical" (cloud ME2: swap m004 for 5_2 and the dynamical sector reproduces); P-318 B997\'s golden uniqueness "fails at m = 4".',
 'Named.')
add('W-11',"Symmetry (a Z/2, an involution, a mirror, amphichirality) is expected to select the object's data; but every forcing symmetry is either satisfied identically by the admissible class or deletes the term it was meant to produce.",
 ['B1174','B1203','B1209','B1222','B1223','B1262','B979','B1064','B1610','B2' if False else 'B1455'],
 'RECORD NAMES IT. B1203 hatch: "THE NARROWING IS THE HATCH: the forcing principle must BREAK a symmetry rather than impose one"; B1064: "the object\'s amphichirality deletes the quantized sector of its own boundary action (CS = 0)"; B1222 tests the thesis "THE SELECTION IS THE OBSTRUCTION" and refutes its sign. P-139 (the selection principle FK9, OPEN) and P-419 ("only one selection mechanism was tried (potentials: mirror-even, landing at fixed points)") state it as a programme-level commitment.',
 'Named.')
add('W-12',"A dimensional firewall: the object supplies shapes (ratios, phases, indices) and no scale; arithmetic Chern-Simons is finite-group valued while the object's term is archimedean-analytic.",
 ['B1064','B1108','B1244','B1157','B1165','B5'],
 'RECORD NAMES IT. B1108: "the theory supplies exactly the term proved to vanish (CS = 0 by amphichirality) and lacks entirely the term carried; the negative names its class: THE ARCHIMEDEAN BOUNDARY"; B1244 audited the firewall and found zero over-fenced items (the firewall is not itself a wall). The unchecked cause is whether the firewall rules out scale-bearing readings the record has not tried (B1108 hatch: Arakelov reading; volume-conjecture route; P-462 B707\'s tests "named and never run").',
 'Named (B1108); the firewall is a commitment the record audits and keeps.')
add('W-13',"No action, kinetic or Kahler term, and no dynamics for tau or for the zero modes as fields; the weave's measure over threads is a counting convention.",
 ['B1629','B1663','B1673','B1699','B1722','B1723','B1791','B1814','B1823'],
 'RECORD NAMES IT. P-073 (owner, "if the principle is the seed, we miss the field"): "the record has no action, kinetic or Kahler term, no dynamics for tau, and does not use the zero modes as fields; the common root of P-014, P-015, P-020, P-022, P-025, P-069". B1813 (PROVED): "the weave\'s own measure depends on how its threads are counted"; B1704: no content on record holds tau off the cusp.',
 'Named.')
add('W-14',"Masses read as group-residual vacua of the weave's finite/triplet representation (Mp2(Z), 2O, residual symmetry groups) with no modulus: the pre-fibre frame.",
 ['B1615','B1616','B1617','B1628','B1632','B1635','B1672','B1610'],
 'RECORD NAMES IT and moved past it: hatches B1615 "the masses are not in the weave\'s group: a forced modulus (the fibre\'s tau) or dynamics", B1616 "neutrino masses from a forced modulus", B1617 "Yukawa couplings as modular forms of weight k". The successor is W-01. (Several are audited in B1655 as refuted in part.)',
 'Named; superseded by the fibre frame.')
add('W-15',"Numerics and extraction limits in the SL(n) tower era (double precision, single-precision plateaus): scope cutoffs, not physics.",
 ['B58','B60','B62','B66','B84','B165','B172','B198','B154','B157'],
 'RECORD NAMES IT (kill_form method-limit; hatch deepen-past-plateau on 23 entries). Low priority; the memory marks this era "superseded; capstones only".',
 'Named.')
PY=open('gen.py').read() if False else None
import sys
out=[]
w=out.append
w("# A4 -- the walls mapped to the framing commitments that cause them, and the hatches never tried\n")
w("*Scope and method.* Source: `frontier/B738_pathfinder_compiler/kill_graph.json` (858 entries; the file is not sorted by id: its last 120 positions mix B959-B1825). I read claim_killed, kill_form and hatch for those 120 positions, for the 57 entries that carry a `scope.frame` field (B1455-B1825), for all 29 entries with priority high/HIGH, and the one-line claim of every entry of kill_form genericity, no-landing-site, value-numerology, zero-intertwiner and method-limit. 510 entries have no hatch (FACE-ONLY 343, UNTRIAGED 167): I did not read them one by one, so cluster counts below are counts of entries I read, a floor, not a census of 858. Also read: the open rows of `docs/POINT_REGISTER.md` (236 rows not DONE/DECLINED), the head of `docs/OPEN_LEADS.md` (its live-catalog currency note is dated 2026-10-15 and its body is the SL(n)-tower era; the live open points are the register's, not OPEN_LEADS's), and `frontier/B1826_.../FINDINGS.md`. Attempt checks: `scripts/checks/topic_sweep.py` (topic regexes, `--full`).\n")
w("Quotes are copied from the kill graph's kill_form (or, where kill_form is a category label, claim_killed). A wall can sit in more than one cluster; I list it in each. Nothing here judges derivability.\n")
w("## 1. Clusters of walls by the commitment they point at\n")
tot=0
for cid,commit,ids,named,why in C:
    ids=list(dict.fromkeys(ids))
    w(f"### {cid} -- {commit}\n")
    w(f"- **Walls: {len(ids)}** (kill graph ids). Named vs inferred: {why}")
    w(f"- **Cause named by the record?** {named}")
    w("- **The walls:**")
    for i in ids: w(f"  - `{i}` {q(i)}")
    w("")
w("(Counts are of entries I read; kill graph ids on one line of a cluster may repeat in another.)\n")
open('A4_body_part1.md','w').write('\n'.join(out))
print([ (c[0],len(set(c[2]))) for c in C])
