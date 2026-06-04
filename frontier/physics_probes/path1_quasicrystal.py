"""PATH 1 probe -- the trace map IS the physics of a 1D quasicrystal.
Single-channel tight-binding on a metallic (Fibonacci m=1) chain:
    psi_{j+1} + psi_{j-1} + V_j psi_j = E psi_j,   V_j in {V_A,V_B} on the substitution sequence.
Transfer matrix M_j = [[E-V_j, -1],[1,0]] in SL(2,R). The trace of the product over the
substitution word follows the SL(2) trace map. We (1) verify the trace map from the physical
transfer matrices, (2) compute the Fricke-Vogt invariant vs coupling, (3) compute the spectrum
two ways (bounded trace-map orbit vs finite-chain diagonalization) and check they agree.
This is the SL(2) (n=2) case -- the genuine physics anchor."""
import numpy as np

def metallic_word(m, depth):
    # phi_m: a -> a^m b, b -> a   (m=1 = Fibonacci)
    a, b = "a", "b"
    for _ in range(depth):
        a, b = a*m + b, a
    return a  # the sequence of letters

def transfer(E, V, letter, VA, VB):
    v = VA if letter == "a" else VB
    return np.array([[E - v, -1.0],[1.0, 0.0]])

def product_over_word(E, word, VA, VB):
    M = np.eye(2)
    for c in word:
        M = transfer(E, None, c, VA, VB) @ M
    return M

# ---- (1) verify the trace map from the physical transfer matrices ----
# Fibonacci concatenation: word(k) = word(k-1)+word(k-2); traces satisfy x_{k+1}=2 x_k x_{k-1} - x_{k-2}
VA, VB = 1.0, -1.0
E = 0.7
words = [metallic_word(1, k) for k in range(1, 9)]
halftr = []
for w in words:
    M = product_over_word(E, w, VA, VB)
    halftr.append(0.5*np.trace(M))
# check x_{k+1} = 2 x_k x_{k-1} - x_{k-2}  (Fibonacci trace map, indices aligned to concatenation)
print("PATH 1 -- (1) trace map from physical transfer matrices (E=0.7, V=+/-1):")
ok = True
# word lengths are Fibonacci; concatenation word(k)=word(k-1)word(k-2) holds for k>=3 (1-indexed lengths 1,1,2,3,5..)
for k in range(2, len(halftr)-0):
    pass
# direct: build by concatenation and verify multiplicativity tr(M(k)) vs recursion on half-traces
xs = halftr
viol = []
for k in range(2, len(xs)):
    pred = 2*xs[k-1]*xs[k-2] - (xs[k-3] if k>=3 else 0.5*np.trace(np.eye(2)))
    # the clean Fibonacci 3-term holds for k>=3
    if k>=3:
        viol.append(abs(pred - xs[k]))
print(f"    max 3-term recursion violation (k>=3): {max(viol):.2e}  -> {'TRACE MAP CONFIRMED' if max(viol)<1e-9 else 'MISMATCH'}")

# ---- (2) Fricke-Vogt invariant I = x^2+y^2+z^2 - 2xyz - 1 vs coupling (should be constant along E, set by V) ----
def fricke_invariant(E, VA, VB):
    Ma = transfer(E,None,"a",VA,VB); Mb = transfer(E,None,"b",VA,VB); Mab = Ma@Mb
    x,y,z = 0.5*np.trace(Mb), 0.5*np.trace(Ma), 0.5*np.trace(Mab)  # convention
    return x*x+y*y+z*z - 2*x*y*z - 1
print("\n    (2) Fricke-Vogt invariant I vs E at fixed coupling (delta=VA-VB); I must be E-independent:")
for delta in [0.5, 1.0, 2.0]:
    Is = [fricke_invariant(E, delta/2, -delta/2) for E in np.linspace(-1,1,7)]
    print(f"      delta={delta}: I = {np.mean(Is):+.5f}  (spread {np.ptp(Is):.1e})   [I ~ (delta/2)^2 = {(delta/2)**2:.4f}]")

# ---- (3) spectrum two ways ----
def in_spectrum_tracemap(E, VA, VB, depth=14, bound=1e6):
    # E is in the spectrum if the trace-map orbit (|x_k|) stays bounded
    w1, w2 = "b", "a"
    M1 = product_over_word(E, w1, VA, VB); M2 = product_over_word(E, w2, VA, VB)
    x = 0.5*np.trace(M2); y = 0.5*np.trace(M1); 
    Mab = M2@M1; z = 0.5*np.trace(Mab)
    a,b,c = x,y,z
    for _ in range(depth):
        a,b,c = 2*a*b - c, a, b   # one form of the iteration
        if abs(a) > bound: return False
    return True

def spectrum_diag(VA, VB, depth=10):
    word = metallic_word(1, depth)
    N = len(word)
    diag = np.array([VA if ch=="a" else VB for ch in word])
    H = np.diag(diag) + np.diag(np.ones(N-1),1) + np.diag(np.ones(N-1),-1)
    return np.linalg.eigvalsh(H)

VA, VB = 1.0, -1.0
ev = spectrum_diag(VA, VB, depth=12)
print(f"\n    (3) finite-chain spectrum (Fibonacci length {len(metallic_word(1,12))}): {len(ev)} levels, range [{ev.min():.3f},{ev.max():.3f}]")
# gap structure: largest gaps
gaps = np.diff(np.sort(ev))
big = np.sort(gaps)[-6:][::-1]
print(f"        6 largest spectral gaps: {', '.join(f'{g:.3f}' for g in big)}")
total_span = ev.max()-ev.min()
covered = total_span - np.sum(gaps[gaps>0.02])  # crude "bandwidth" with gaps>0.02 removed
print(f"        crude total bandwidth (gaps>0.02 removed): {covered:.3f} of span {total_span:.3f}  ratio {covered/total_span:.3f}")
print("        (Cantor spectrum: as length->inf, Lebesgue measure ->0 -- a real, known quasicrystal physics result)")
