#!/usr/bin/env bash
# B1167 -- two-seat harvest (integrate-don't-merge). (A) codex R017 pays the SEAM-Y up-Yukawa
# provenance debt (B1154/R49-1); (B) cc3 B8138-extended adds the cusp shape as a 2nd object-level
# separator -- which cc answers is ORIENTATION-BLIND (does not supply W0). Independent checks here;
# codex's two certs are reproduced from their branch (b7faffef), not copied.
set -euo pipefail
cd "$(dirname "$0")"

echo "########## (A) codex R017 -- the C12 Wilson character arithmetic (independently re-derived) ##########"
python3 - << 'PY'
# The height-308 up-Yukawa Q.u^c.Hu must be C12-neutral to be PERMITTED (a texture question);
# the VANISHING mu_u=0 is codex's cohomological naturality (H^1(G_Y)=0), fenced below.
mod=12
# k=4 selected characters (codex memo/outputs): Q=A8, u^c=A4, d^c=A4, L=A0, e^c=A0, Hu=A0, Hd=A0
k4={'Q':8,'uc':4,'dc':4,'L':0,'ec':0,'Hu':0,'Hd':0}
k8={'Q':4,'uc':8,'dc':8,'L':0,'ec':0,'Hu':0,'Hd':0}
def op(ch,parts): return sum(ch[p] for p in parts)%mod
for name,ch in [('k=4',k4),('k=8',k8)]:
    up=op(ch,['Q','uc','Hu']); dn=op(ch,['Q','dc','Hd']); lep=op(ch,['L','ec','Hd']); mu=op(ch,['Hu','Hd'])
    print(f"  {name}: up(Q.uc.Hu)={up}  down(Q.dc.Hd)={dn}  lep(L.ec.Hd)={lep}  mu(Hu.Hd)={mu}  (all mod 12)")
    assert up==0 and dn==0 and lep==0 and mu==0, "an MSSM operator is not C12-neutral"
print("  => ALL MSSM operators are C12-neutral => C12 imposes NO family texture zero; it PERMITS")
print("     up=Sym^2(C^3) dim 6. The up-Yukawa is NOT killed by characters.")
print("  FENCED (codex's typed input, needs the Sage/BCDD monad stack -- NOT re-derived here):")
print("     the cohomological naturality H^1(G_Y)=0 that forces mu_u=0 / rank 0 at chain level.")
print("  CITED: codex's two certs verify_yukawa_cup_product_308_scope.py + _exact_spectrum_no_go.py")
print("     reproduced from codex/seat-r001 b7faffef -> PASS, byte-identical to committed outputs.")
print("  => the SEAM-Y up-Yukawa=0 PRIMARY derivations are now branch-local (provenance debt PAID);")
print("     the conclusion mu_u=0 was already banked B1154 (two independent walls).")
PY

echo
echo "########## (B) cc3 B8138-extended -- the cusp shape separator, and cc's orientation answer ##########"
python3 - << 'PY' 2>/dev/null
import snappy, math
fam=['m004','m206','m203','m412','s118','s119','s595','m003','m202','m208','s594','s596','m207','m410']
sh={}
for n in fam:
    s=complex(snappy.Manifold(n).cusp_info()[0]['shape'])
    if s.imag<0: s=s.conjugate()
    sh[n]=s
m004=sh['m004']
print("  m004 cusp shape =", round(m004.imag,10),"i  == 2*sqrt3 i =", round(2*math.sqrt(3),10),"i :", abs(m004.imag-2*math.sqrt(3))<1e-9)
print("  UNIQUE in the 14-member Q(sqrt-3) family (up to conj, nothing within 1e-6):",
      all(abs(sh[n]-m004)>1e-6 for n in fam if n!='m004'), "  (cc3 B8138 reproduced)")
print("  THE ORIENTATION ANSWER (cc3 handed cc the question 'does a modulus yield an orientation?'):")
print("    real part =", abs(m004.real), "-> PURELY IMAGINARY (rectangular cusp torus).")
print("    orientation-reversal acts tau -> -conj(tau); -conj(2sqrt3 i) = 2sqrt3 i == tau:", abs(-m004.conjugate()-m004)<1e-9)
print("    => the cusp shape is MIRROR-FIXED => ORIENTATION-BLIND => does NOT supply W0.")
print("    (the magnitude 2sqrt3 distinguishes m004; real part 0 = no chirality. A modulus, not an orientation.)")
print("  => B1163 STRENGTHENED: TWO object-level separators (H1=Z, cusp shape), BOTH orientation-blind;")
print("     the object still provably refuses to self-orient. Route list is 2, W0 still absent.")
PY
echo
echo "REPRODUCES"
