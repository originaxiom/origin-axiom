"""
Step 1: verify the algebraic reduction
   t_w(kappa) := tr( rho_Weil(RL) @ P_w )
             =  (1/n) * sum_{mu,alpha in G} exp( i*pi/kappa * Q(mu,alpha) )
   Q(mu,alpha) = |mu|^2 - |alpha|^2 + 2*ip(alpha, (I-w) mu)
against the ground truth computed directly from weil_mechanism.py's operators.
"""
import os
import importlib.util, os, sys
import numpy as np

HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    "..", "B587_weil_mechanism")
spec = importlib.util.spec_from_file_location("wm", os.path.join(HERE, "weil_mechanism.py"))
wm = importlib.util.module_from_spec(spec)
# prevent the module's __main__ print-block from running by wrapping exec in a guarded namespace
src = open(os.path.join(HERE, "weil_mechanism.py")).read()
# cut off everything from the top-level "print(" driver code (after function/data defs)
cut = src.index('print("registered conductor menus')
src_defs = src[:cut]
ns = {"__file__": os.path.join(HERE, "weil_mechanism.py")}
exec(compile(src_defs, "weil_mechanism.py", "exec"), ns)

ip_weight = ns['ip_weight']
build_G = ns['build_G']
weil_ops = ns['weil_ops']
rho_weil = ns['rho_weil']
WEYL = ns['WEYL']
mono = ns['mono']
conductor_menu = ns['conductor_menu']

def ground_truth_terms(kap, word):
    T, S, perms, n = weil_ops(kap)
    M = rho_weil(word, T, S)
    return {key: np.trace(M @ P) for key, (P, sg) in perms.items()}

def gauss_sum_term(kap, wi, pm):
    """Direct double Gauss sum over G x G for the word 'RL' term (+-w_wi)."""
    reps, index, canon = build_G(kap)
    n = len(reps)
    Wm, sg = WEYL[wi]
    w = pm * Wm  # the actual permutation-generating matrix used in P_w
    q = ip_weight(reps, reps)                      # |mu|^2 for all reps, shape (n,)
    # Q(mu,alpha) = |mu|^2 - |alpha|^2 + 2*ip(alpha, (I-w) mu)
    Iw = np.eye(2, dtype=int) - w
    wmu = (Iw @ reps.T).T                           # (I-w) mu for each mu, shape (n,2)
    cross = ip_weight(reps[None, :, :], wmu[:, None, :])  # cross[a_idx, m_idx] = ip(alpha, (I-w)mu)
    # cross shape: broadcasting reps[None,:,:] (1,n,2) with wmu[:,None,:] (n,1,2) -> (n,n,2)-> ip -> (n,n)
    Qmat = q[None, :] - q[:, None] + 2.0 * cross   # Qmat[a,m] = |mu_m|^2 - |alpha_a|^2 + 2 ip(alpha_a,(I-w)mu_m)
    phase = np.exp(1j * np.pi * Qmat / kap)
    return phase.sum() / n

print("word = RL; comparing ground truth term traces vs the derived double Gauss sum")
mismatches = 0
for kap in range(5, 13):
    gt = ground_truth_terms(kap, "RL")
    for wi in range(6):
        for pm in (1, -1):
            key = (pm, wi)
            gtv = gt[key]
            gsv = gauss_sum_term(kap, wi, pm)
            ok = abs(gtv - gsv) < 1e-6
            if not ok:
                mismatches += 1
                print(f"  MISMATCH kap={kap} key={key}: ground={gtv:.6f} gauss={gsv:.6f}")
    print(f"  kap={kap}: all 12 terms match: {mismatches==0}")

print(f"\nTOTAL mismatches: {mismatches}")
