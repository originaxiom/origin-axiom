#!/usr/bin/env python3
"""
B775 Phase-2 Wave-1 -- Cell P2-AABB : the aAbB derivation door.

QUESTION (sealed, prereg 4f73e186): derive the three closing bits {c, theta, gamma5}
FROM the golden substitution sigma: a->ab, b->a  -- from ITS OWN algebraic/statistical
structure (incidence matrix, eigenstructure, letter-doubling) -- NOT by analogy.

SEALED CRITERION:
  DERIVED  (all three bits fall out of sigma, map shown, reproduced 2nd way) -> RESOLVED-A
  DISMISSED(no derivation; suggestive analogy; tombstone)                    -> RESOLVED-B
  PARTIAL  (some bits derive -- state which)                                 -> UNRESOLVED

DISCIPLINE (binding): do NOT force a positive (B772 unearned-positive lesson); do NOT
force a negative either (B525 -- compute the discriminating fact in-cell, never cite).
A "chord/theta-odd" object must be genuinely non-abelian, not a relabeled trace
invariant (B774). Exact/symbolic; a positive reproduced a second way.

BANKED REFERENCE FRAME (what {c,theta,gamma5} ARE, from B766 measurement torsor / C20):
  c      = conjugation / orientation / self-other side-swap (flips chirality's side)
  theta  = reversal (SL(2) trace-reversal; flips ONLY the chord; a MATRIX-level odd)
  gamma5 = the golden Galois  phi <-> 1-phi  ((1-phi)^2 = phi^-2), = time's branch
  rank of the discrete menu = EXACTLY 3 (B766, saturated); chord = c XOR theta (dependent)
Courier aAbB reading (S-room, never gated -- B768 receipt #5): the 4-letter alphabet
  {a,A,b,B} with distinctions {case, position, pair} -> {c, theta, gamma5}.
"""
import json
import sympy as sp

OUT = {}
LOG = []
def log(s=""):
    print(s); LOG.append(s)

phi = (1 + sp.sqrt(5)) / 2
lam = sp.symbols("lambda")

log("="*74)
log("PART 1 -- sigma's exact structure (the raw material of any derivation)")
log("="*74)

# sigma: a->ab, b->a.  Incidence (abelianization) matrix M: columns = images.
#   |a|_a=1 |a|_b=1  (image of a = ab)
#   |b|_a=1 |b|_b=0  (image of b = a )
M = sp.Matrix([[1, 1], [1, 0]])
# Row-stochastic Fibonacci LETTER-TRANSITION (Markov) matrix used in the prereg:
T = sp.Matrix([[1/phi**2, 1/phi], [1, 0]])

charM = sp.expand(M.charpoly(lam).as_expr())
disc  = sp.discriminant(charM, lam)
eigM  = sorted(M.eigenvals().keys(), key=lambda z: sp.re(z))
detM  = M.det()
eigT  = sorted(T.eigenvals().keys(), key=lambda z: sp.re(z))
detT  = sp.simplify(T.det())

log(f"  incidence M = {M.tolist()}")
log(f"  char poly(M) = {charM}    discriminant = {disc}")
log(f"  eig(M) = {[sp.nsimplify(e) for e in eigM]}   (= 1-phi , phi)")
log(f"  det(M) = {detM}   (orientation-reversing: det < 0)")
log(f"  Markov T eig = {[sp.nsimplify(e) for e in eigT]}   (= -1/phi , 1)  det(T)={detT}")

# sanity: the golden conjugate identity gamma5 acts on
assert sp.simplify((1 - phi)**2 - 1/phi**2) == 0
assert sp.simplify(eigM[0] - (1 - phi)) == 0 and sp.simplify(eigM[1] - phi) == 0
assert detM == -1
assert sp.simplify(sorted(eigT, key=sp.re)[0] + 1/phi) == 0
# letter-doubling: |sigma(a)|=2, |sigma(b)|=1  (NON-uniform: the "doubling")
lens = {"a": 2, "b": 1}
log(f"  letter lengths |sigma(a)|,|sigma(b)| = {lens['a']},{lens['b']}  (a->ab doubles; b->a does not)")
log(f"  alphabet(sigma) = {{a,b}}  -> size 2  -> ONE native 'which-letter' bit")
OUT["part1"] = dict(charpoly=str(charM), disc=int(disc), detM=int(detM),
                    eigM="{1-phi, phi}", eigT="{-1/phi, 1}", alphabet_size=2)

log("")
log("="*74)
log("PART 2 -- bit-by-bit: does a CANONICAL involution emerge from sigma, AND is its")
log("          identification with the NAMED object-bit FORCED (not chosen)?")
log("="*74)

bit = {}

# ---- gamma5 : the golden Galois  phi <-> 1-phi ------------------------------
log("")
log("[gamma5]  candidate native Z/2 = Gal(Q(sqrt5)/Q) on the eigenvalues of M")
# route (i): splitting field of the char poly
splitfield_disc = disc                      # = 5  -> Q(sqrt5), quadratic -> Gal = Z/2
# route (ii): the nontrivial automorphism sends phi -> its conjugate; check it is 1-phi
sig_conj = sp.sqrt(5).subs(sp.sqrt(5), -sp.sqrt(5))  # symbolic stand-in
phi_conj = (1 - sp.sqrt(5))/2
route_ii = sp.simplify(phi_conj - (1 - phi)) == 0 and sp.simplify(phi*phi_conj - detM) == 0
# forced identification? object's gamma5 (B766) is defined ON exactly phi,1-phi in Q(sqrt5):
forced_g5 = (disc == 5) and route_ii and sp.simplify((1-phi)**2 - 1/phi**2) == 0
log(f"    route(i)  disc(charpoly) = {disc} => splitting field Q(sqrt{disc}), Gal = Z/2  [{disc==5}]")
log(f"    route(ii) nontrivial aut: phi -> 1-phi ; phi*(1-phi) = det(M) = -1          [{route_ii}]")
log(f"    IDENTIFICATION FORCED?  object gamma5 IS the Q(sqrt5) Galois on {{phi,1-phi}}")
log(f"    -> SAME field, SAME numbers, SAME involution.  FORCED = {forced_g5}")
bit["gamma5"] = dict(emerges=True, forced=bool(forced_g5), reproduced_two_ways=True,
                     mechanism="Gal(Q(sqrt5)/Q) on eig(M)={phi,1-phi}; disc=5")

# ---- theta : reversal / the negative subdominant eigenvalue -----------------
log("")
log("[theta]   candidate native Z/2 #1 = word/subshift REVERSAL  sigma~(a)=ba, sigma~(b)=a")
# reversal substitution (reverse each image); it is an involution on the set of
# substitutions that share the Fibonacci subshift, distinct from sigma:
sigma  = {"a": "ab", "b": "a"}
sigrev = {k: v[::-1] for k, v in sigma.items()}
rev_is_involution = {k: sigrev[k][::-1] for k in sigrev} == sigma
rev_differs       = sigrev != sigma      # genuine (non-trivial) Z/2 on the pair {sigma, sigma~}
log(f"    sigma~ = {sigrev} ;  reverse-of-reverse = sigma  [{rev_is_involution}] ;  sigma~ != sigma  [{rev_differs}]")
log("          candidate native Z/2 #2 = sign of the subdominant eigenvalue = sign(-1/phi) = -")
subdom_sign_neg = bool(sp.re(sorted(eigT, key=sp.re)[0]) < 0)
log(f"    subdominant eig(T) = -1/phi < 0  [{subdom_sign_neg}]  (the oscillation sign)")
# forced identification with the object's theta?
#   object theta = SL(2) trace-reversal, a MATRIX-level chord-odd (B766/B774: NOT a
#   trace invariant).  Two obstructions to a FORCED map:
#   (a) route #2 (-1/phi = the weld theta-odd trace) is E20-FLAGGED MECHANICALLY
#       UNLINKED (B768 V3 / receipt #5) -- and is a SEPARATE cell (P2-WELD). Using it
#       here would be exactly the unearned link the prereg quarantines.
#   (b) route #1 (word reversal) is an involution of the SUBSHIFT; identifying it with
#       the object's SL(2) trace-map theta needs a substitution<->trace-map BRIDGE that
#       is NOT established in-cell. Self-test (B774): the object's theta acts at
#       MATRIX level (chord); word-reversal acts on letters -- no derived equivalence.
forced_theta = False
log("    IDENTIFICATION FORCED?  #2 is E20-UNLINKED (quarantined to P2-WELD); #1 needs")
log("    an unbuilt substitution<->trace-map bridge (object theta is MATRIX-level, B774).")
log(f"    -> a native Z/2 EXISTS, but its map to object-theta is ANALOGY.  FORCED = {forced_theta}")
bit["theta"] = dict(emerges=True, forced=bool(forced_theta), reproduced_two_ways=False,
                    mechanism="reversal Z/2 exists AND subdom sign<0 -- but map to SL(2)-trace-theta unforced (E20/bridge)")

# ---- c : conjugation / orientation / self-other side-swap -------------------
log("")
log("[c]       candidate native Z/2 = the letter-swap  s: a<->b  (the self/other flip)")
# is s an automorphism of sigma?  compute  s . sigma . s  and compare to sigma.
def apply(sub, w):           return "".join(sub[ch] for ch in w)
def swap(w):                 return w.translate(str.maketrans("ab", "ba"))
s_sigma_s = {L: swap(apply(sigma, swap(L))) for L in "ab"}   # (s o sigma o s)(L)
c_is_automorphism = (s_sigma_s == sigma)
log(f"    (s o sigma o s) = {s_sigma_s}   vs   sigma = {sigma}")
log(f"    a<->b an automorphism of sigma?  {c_is_automorphism}   "
    f"(sigma is NOT letter-symmetric: a spawns 2, b spawns 1)")
# det(M) = -1 is an orientation Z/2 VALUE -- but it is a fixed scalar invariant, not a
# free involution acting on sigma's states, and it does not encode a self/other side.
# The courier assigns c to the CASE bit {a,A} -- uppercase is NOT in sigma's 2-letter
# alphabet: it is IMPORTED.
log("    det(M) = -1 is an orientation VALUE, not a free involution, and encodes no self/other side.")
log("    courier maps c to CASE {a,A}: uppercase A,B are NOT in sigma's alphabet {a,b} -> IMPORTED.")
forced_c = False
log(f"    -> NO native conjugation involution (a<->b not an automorphism); case-bit imported.  FORCED = {forced_c}")
bit["c"] = dict(emerges=False, forced=bool(forced_c), reproduced_two_ways=False,
                mechanism="a<->b is NOT a sigma-automorphism; det=-1 is a value not an involution; case {a,A} imported")

OUT["bits"] = bit

log("")
log("="*74)
log("PART 3 -- the counting obstruction (why the FULL 3-bit map cannot come from sigma)")
log("="*74)
# sigma's alphabet = 2 letters -> 1 native which-letter bit; plus the eigenvalue-Galois
# bit. The courier's {a,A,b,B} = 4 letters carries only log2(4)=2 independent bits, so
# THREE distinctions {case,position,pair} are dependent (one = XOR of the other two) --
# exactly B766's chord = c XOR theta. And {A,B} (case) is not sigma's.
n_letters_sigma  = 2
bits_from_alpha  = 1                        # floor(log2(2))
n_letters_aAbB   = 4
bits_from_aAbB   = 2                        # floor(log2(4))  -> 3 distinctions dependent
log(f"  sigma alphabet {{a,b}}: {n_letters_sigma} letters -> {bits_from_alpha} independent letter-bit")
log(f"  courier {{a,A,b,B}}: {n_letters_aAbB} letters -> only {bits_from_aAbB} independent bits")
log(f"    => the 3 distinctions {{case,position,pair}} are DEPENDENT (one = XOR of the other two)")
log(f"    => matches B766 'chord = c XOR theta' (rank-3 lives on the RICHER object, not sigma)")
log("  the object's rank-3 discrete menu (B766) lives on the character variety / CM field;")
log("  it is NOT canonically sourced by the 2-letter substitution alone.")
OUT["counting"] = dict(sigma_alphabet=2, native_letter_bits=1, aAbB_letters=4,
                       aAbB_independent_bits=2, third_distinction="dependent (XOR)")

log("")
log("="*74)
log("PART 4 -- VERDICT LOGIC (in-code; emits UNRESOLVED for PARTIAL)")
log("="*74)

derived = {b: (bit[b]["emerges"] and bit[b]["forced"] and bit[b]["reproduced_two_ways"])
           for b in ("c", "theta", "gamma5")}
n_derived = sum(derived.values())
log(f"  per-bit DERIVED (emerges AND forced-identification AND reproduced): {derived}")
log(f"  count derived = {n_derived} of 3")

if n_derived == 3:
    verdict, terminal = "RESOLVED-A", "DERIVED"
elif n_derived == 0:
    verdict, terminal = "RESOLVED-B", "DISMISSED-TOMBSTONE"
else:
    verdict, terminal = "UNRESOLVED", "PARTIAL"

log("")
log(f"  VERDICT = {verdict}   (terminal: {terminal})")
log("  Reading:")
log("   * gamma5 GENUINELY DERIVES -- it is the Q(sqrt5) Galois on eig(M)={phi,1-phi};")
log("     same field, same numbers, same involution as B766's gamma5. Reproduced 2 ways")
log("     (disc=5 => Z/2 ; phi*(1-phi)=det M=-1 with phi->1-phi). NOT base-rate: sigma's")
log("     growth field IS Q(sqrt5), the object's gamma5 field.")
log("   * theta: a native Z/2 EXISTS (subshift reversal; subdominant sign<0) but its map")
log("     to the object's MATRIX-level SL(2)-trace theta is UNFORCED -- the -1/phi route")
log("     is E20-UNLINKED (P2-WELD's job) and the reversal route lacks a subst<->trace")
log("     bridge. ANALOGY, not derivation.")
log("   * c: NO native involution -- a<->b is not a sigma-automorphism (sigma is letter-")
log("     asymmetric); det=-1 is a value not an involution; the case bit {a,A} is imported")
log("     (not in sigma's alphabet). ANALOGY/IMPORT, not derivation.")
log("   * counting obstruction: a 2-letter substitution carries 1 native letter-bit + the")
log("     eigenvalue-Galois bit; it cannot canonically source THREE independent named")
log("     involutions. The object's rank-3 menu lives on the richer character-variety/CM")
log("     structure (B766), not on sigma.")
log("   => the courier {case,position,pair}<->{c,theta,gamma5} map is gamma5-anchored")
log("      ANALOGY: 1 of 3 bits derives; 2 of 3 are imposed. PARTIAL -> UNRESOLVED.")

OUT["verdict"]  = verdict
OUT["terminal"] = terminal
OUT["derived"]  = derived
OUT["n_derived"] = n_derived

with open("results.json", "w") as f:
    json.dump(OUT, f, indent=2)
with open("output.txt", "w") as f:
    f.write("\n".join(LOG) + "\n")
log("")
log("  wrote results.json + output.txt")
