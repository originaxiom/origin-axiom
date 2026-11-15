"""P-862 step 1 helper (main, 2026-11-15): pull every row of the record's governing tables that states a relation among
physical parameters (masses, mixings, couplings, charges, counts), with its arc numbers, into one file for main to read
and type by hand. It reads; it decides nothing."""
import re, pathlib
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
SRC = ["docs/LAW_MAP.md", "docs/FALSIFIER_REGISTER.md", "docs/THEOREM_REGISTRY.md", "docs/THE_CLAIM.md", "GENESIS.md"]
KEYS = re.compile(r"Y_e|Y_d|Y_u|lepton|down quark|down rows|sin²|sin\^2|weak angle|Koide|Georgi|Jarlskog|m₁ ?m₃|m1 m3|geometric mass|TM1|TM2|CKM|PMNS|V_us|V_cb|V_ub|θ₁₂|θ₁₃|θ₂₃|δ_CP|mixing|hierarch|massless|charge quant|hypercharge|global form|generation|chiral|exotic|Z′|Z'|proton|neutrino|Majorana|Dirac|θ̄|theta-bar|strong.CP|unification|b-τ|b–τ|bottom-tau|top", re.I)
out = []
for s in SRC:
    p = ROOT / s
    if not p.exists(): continue
    for n, l in enumerate(p.read_text().split("\n"), 1):
        if l.startswith("|") and KEYS.search(l) and not set(l.strip()) <= set("|-: "):
            arcs = sorted(set(re.findall(r"\bB\d{2,4}\b", l)), key=lambda x: int(x[1:]))
            out.append("%s:%d [%s] %s" % (s, n, " ".join(arcs[:12]), l[:900]))
(pathlib.Path(__file__).resolve().parent / "candidates.txt").write_text("\n".join(out) + "\n")
print(len(out), "candidate rows written")
