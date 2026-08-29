#!/usr/bin/env python3
"""P3 CLAIM TRACE -- the written draft against its own arcs.
Seal: seals/P3_CLAIM_TRACE_PREREG.md.  Pinned to the PAPER's commit, not the lane's
default pin, because the draft was written against this corpus state."""
import os, re, json, sys
PAPER_PIN = "89affd5bbd4b900397af2bf3b987ff8f05f5cb80"   # main @ THE PAPER currency pass
os.environ.setdefault("OA_REF", PAPER_PIN)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _oa_source as OA
assert OA.REF == PAPER_PIN, f"pin not honoured: {OA.REF}"

ARCS = OA.arc_verdicts()
print(f"arc records at the paper's own commit {PAPER_PIN[:8]}: {len(ARCS)}")

# ---- the claim ledger, extracted by hand under the seal's rule, published in full ----
# (id, section, the claim as the draft states it, distinctive retrieval tokens)
CLAIMS = [
 ("C01","2","the four ADE faces are canonically linked, so conditioned on one label the recurrence has probability 1","ade canonically linked recurrence probability mckay du val modular invariant"),
 ("C02","2","E6 is the only exceptional label an imaginary quadratic field can reach","exceptional label imaginary quadratic reach e6 only"),
 ("C03","2","there are exactly two surjections pi_1(m004) ->> 2T = SL(2,3)","surjection 2T SL(2,3) exactly two m004"),
 ("C04","2","37.2% of the first 400 one-cusped census manifolds (two-generator) admit such a surjection; 32.8% admit exactly two; ties reproduce across two implementations","census 400 one-cusped surjection base rate 37 32 two-generator"),
 ("C05","2","m003 shares the invariant trace field Q(sqrt-3) with m004 without being a knot complement","m003 sibling trace field knot complement shares"),
 ("C06","2","access to the relevant McKay group is generic across the metallic family","mckay group generic metallic family grammar access"),
 ("C07","2","the programme applied base-rate reasoning to numerical coincidences long before its flagship structural claim","base rate numerical coincidence flagship structural lag provenance"),
 ("C08","3","m004 is the unique arithmetic knot complement [LITERATURE]","unique arithmetic knot complement reid"),
 ("C09","3","among metallic grammars R^m L^m exactly one has a modular shadow of McKay type, m=1","metallic grammar modular shadow mckay unique golden m=1"),
 ("C10","3","|SL(2,Z/N)| is a binary polyhedral order for exactly N in {3,4,5}","SL(2,Z/N) order binary polyhedral 24 48 120 exactly"),
 ("C11","3","the conductor of the metallic grammar R^m L^m is m^2+4","conductor metallic grammar m^2+4 level"),
 ("C12","3","a mixed Tate motive exists for finite-volume hyperbolic 3-manifolds with Beilinson regulator the complex volume [LITERATURE]","mixed tate motive beilinson regulator complex volume lee"),
 ("C13","4","252 candidate contents; the colour condition kills 222; exactly two survive rigid, chiral, anomaly-free","252 contents 222 colour condition two survivors anomaly"),
 ("C14","4","no token of the object appears in that computation, confirmed by an audit of the executable statement","zero object tokens audit executable arena content"),
 ("C15","4","widening the alphabet to adjoints admits seven contents, and to a further bi-fundamental fourteen","alphabet dependent adjoint seven bifundamental fourteen"),
 ("C16","4","the object supplies a rank-3 abelian sector, the abelian complement of three orthogonal A2s among the 72 roots","rank 3 abelian sector three orthogonal A2 72 roots trinification"),
 ("C17","4","an SM-shaped 15-plet is available inside the 27","15-plet inside 27 sm-shaped available"),
 ("C18","4","the three linear conditions cut the 5-dim charge space to a line and the cubic is -18(t-3)(t+3)","linear conditions cubic -18 hypercharge forcing line"),
 ("C19","4","the global form is [SU(3)xSU(2)xU(1)]/Z6, kernel computed exactly, uniform across six Weyl realizations","global form Z6 kernel six weyl realizations uniform"),
 ("C20","4","the global form is falsifiable in principle through line-operator spectra","line operator spectra falsifiable global form"),
 ("C21","4","the cascade terminates because the SM is the terminal registerable algebra, with a positive control","termination theorem terminal registerable positive control"),
 ("C22","4","the adjoint does not occur in 27x27, so no adjoint VEV gives a 27 fermion mass","adjoint 27 tensor product mass vev cannot"),
 ("C23","4","the landing on su(3)+su(2)+u(1)^3 is the A2+A1 Levi, Borel-de Siebenthal/Dynkin [LITERATURE]","landing A2+A1 levi borel de siebenthal dynkin deflation"),
 ("C24","5","no period of the object is an SM ratio, tested exhaustively against the sealed target list at bounded height","periods sealed targets bounded height no relation exhaustive"),
 ("C25","5","the object's natural invariants -- volume, Mahler-type, spectral -- are disjoint from the targets","natural invariants volume mahler spectral disjoint targets"),
 ("C26","5","over a 216-cell grid against 18 sealed targets, relations passing the regulator gate number zero","216 grid 18 sealed targets regulator gate zero"),
 ("C27","5","extending the basis with the object's complex volume -- verified independent -- leaves the count zero","complex volume basis extended independent count zero"),
 ("C28","5","the anomaly conditions are homogeneous, so they fix a direction and never a scale, in any theory","hypercharge normalisation not derivable homogeneous direction scale"),
 ("C29","5","the 64-dim complement is four irreducibles of multiplicity one -- two spin-2 colour singlets, two coloured bi-vectors -- with invariant content zero","64 complement spacetime branch invariant content zero irreducibles"),
 ("C30","5","the unsheddable units are the standard extra abelian directions and the rank reduction lives in the skipped steps","rank reduction u(1)_psi u(1)_chi skipped su(5) unsheddable"),
 ("C31","5","Mostow rigidity fixes shape and not size [LITERATURE]","mostow rigidity scale free shape size"),
 ("C32","6","the several self-closure failures are one Z/2-torsor class under a single global involution c","four probes one Z/2 class torsor involution self-close"),
 ("C33","6","c restricts to a Galois generator, a complex conjugation on a cyclotomic sector, and the geometric mirror","galois generator complex conjugation cyclotomic geometric mirror restriction"),
 ("C34","6","the proof is an equivariance: an equivariant map of torsors under one group is an isomorphism","equivariant map torsors isomorphism proof one group"),
 ("C35","6","for a heterogeneous pair the mirror is realisable over GL2(Z) only with determinant -1","heterogeneous pair GL2(Z) determinant -1 mirror odd relational"),
 ("C36","6","the class is invariant under simultaneous GL2(Z)-conjugation, so no act of selection is needed","simultaneous conjugation selector-free invariant no selection"),
 ("C37","6","an invariant selector cannot pick a point of its own orbit","invariant selector cannot pick point orbit"),
 ("C38","6","the deciding criterion is kappa, the same Fricke invariant founding the object's existence","kappa fricke invariant gen_det founding obstruction observer criterion"),
 ("C39","6","every internal operation preserves kappa identically, but kappa differs at the object and its mirror","kappa preserved identically internal operations mirror differs irremovable"),
 ("C40","6","the trace ring is the same quadratic integers at every depth, so the Galois choice is spent once","trace ring Z[omega] every depth spent once coordinatisation"),
 ("C41","6","the anti-conjugating element acts as the Galois generator NECESSARILY, so it discriminates nothing [WITHDRAWN SUPPORT]","anti-conjugating galois generator necessarily vacuous eigenline"),
 ("C42","6","the partner is not canonical, at both the field and the embedding level [WITHDRAWN SUPPORT]","partner canonical refuted admissibility fraction embedding"),
 ("C43","7","l is external by design; no dimensionless quantity flows from it and it survives elimination","dimensionful unit external by design elimination scale"),
 ("C44","7","c_BH = 6 sigma and c((E6)_1) = 78/13 = 6, so proving the boundary theory is (E6)_1 IS sigma=1","central charge 78/13 (E6)_1 sigma boundary identification"),
 ("C45","7","the sigma row's missing object is one graded character under six stated conditions; the candidate set is empty","graded character six conditions candidate set empty sigma"),
 ("C46","7","for lambda one sub-route is closed because the relevant unit rank is 0 so that regulator is identically 1","lambda unit rank zero regulator identically 1 dirichlet"),
 ("C47","7","lambda's attempted exhaustion proof failed and is withdrawn; no acceptance criterion exists","lambda exhaustion failed withdrawn no acceptance criterion"),
 ("C48","7","P(B0): the cubic gives one nonlinear condition and the coupling one canonical linear functional, 3->2->1","P(B0) cubic linear functional 3 2 1 higgs projective one condition short"),
 ("C49","7","whether a second independent condition exists reduces to one binary property of the internal grading","second condition binary property internal grading Z/12 character"),
 ("C50","1","no unique four-dimensional field theory follows, and unrestricted uniqueness is refuted","unique four-dimensional field theory uniqueness refuted"),
]
TOK = re.compile(r"[a-z0-9_]+")
STOP = set("the a an of and or is are be to in on at for by with that this it as not no from "
           "one two three four five six its own then than so which what where when".split())
def toks(s): return {w for w in TOK.findall(s.lower()) if w not in STOP and len(w) > 1}

def retrieve(tokens, k=4):
    scored=[]
    for a in ARCS.values():
        txt = (a.get("claim_one_line") or "")
        at = toks(txt)
        if not at: continue
        ov = tokens & at
        if not ov: continue
        scored.append((len(ov)/ (len(tokens)**0.5), len(ov), a["id"], a.get("verdict"), txt))
    scored.sort(reverse=True)
    return scored[:k]

out = {}
for cid, sec, claim, q in CLAIMS:
    cand = retrieve(toks(q))
    out[cid] = dict(section=sec, claim=claim, candidates=[
        dict(arc=c[2], verdict=c[3], overlap=c[1], text=c[4]) for c in cand])
json.dump(out, open("/tmp/claude-0/-home-user-golden-gate/7aec077f-59a6-5129-b1a7-361cc5dcb800/scratchpad/trace_candidates.json","w"), indent=1)
print(f"claims extracted: {len(CLAIMS)}   candidates written")
nohit = [c for c in out if not out[c]["candidates"]]
print(f"claims with ZERO mechanical candidates: {len(nohit)} {nohit}")
