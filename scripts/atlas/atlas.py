"""The Recurrence Atlas -- mine the origin-axiom repo into a motif x probe x obstacle graph.

A META-tool about the STRUCTURE OF THE WORK, not physics. Firewall-safe: nothing to CLAIMS; it makes
no value claim. It maps which mathematical MOTIFS recur across the frontier probes, at which OBSTACLES,
and (heuristically) where a *conserved* motif re-surfaces at a *foreign* obstacle -- the honest signal
of the "self-generating object" as opposed to mere tool-reuse.

Grounded in the repo's own vocabulary (K001/K007: kappa is the one conserved first integral; the trace
map is method; the two ends / omega are structural invariants; FAILURE_ATLAS: the obstacle taxonomy).

Run:  python scripts/atlas/atlas.py           # mines -> scripts/atlas/atlas_data.json + a summary
Import: mine(), analyze(), meeting_points()    # (tests / query.py / render.py sys.path-insert this dir)
"""
import os
import re
import json
import glob
from collections import Counter, defaultdict

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
DATA = os.path.join(os.path.dirname(__file__), 'atlas_data.json')

# --------------------------------------------------------------------------------------------------
# THE MOTIF LEXICON (grounded in knowledge/K001..K022, docs/atlas/GLOSSARY, the HINT recurrence-hints)
#   conserved: first-integral (must recur, mathematically) | structural (invariant of a transform)
#              | tool (our method -> recurrence is a selection effect) | no (derived/incidental)
# --------------------------------------------------------------------------------------------------
LEXICON = {
    "figure_eight":   dict(kind="object", conserved="no", domain="topology",
                           gloss="the simplest hyperbolic knot; the carrier object",
                           patterns=[r"figure.eight", r"\b4_?1\b", "4₁", "m004", "fig-8", "fig8"]),
    "trace_map":      dict(kind="dynamics", conserved="tool", domain="dynamics",
                           gloss="the trace map / Dehn-twist words / monodromy / substitution -- the METHOD",
                           patterns=[r"trace.?map", "Dehn", "monodromy", "automorphism", "A=LR",
                                     r"R\^?m ?L\^?m", "RmLm", r"phi_?m", r"T_?a\b", r"T_?b\b",
                                     "substitution", "Fricke.Vogt", "mapping class", "mapping torus"]),
    "kappa":          dict(kind="invariant", conserved="first-integral", domain="dynamics",
                           gloss="the conserved commutator trace kappa = tr[a,b] = the Suto invariant",
                           patterns=["kappa", "κ", "Casimir", r"Su(t|t.)o", "Suto",
                                     r"tr\[a,?b\]", "commutator trace", "first integral", "Fricke"]),
    "metallic":       dict(kind="structure", conserved="structural", domain="arithmetic",
                           gloss="the metallic family lambda_m tower (golden/silver/bronze)",
                           patterns=["metallic", r"lambda_?m", r"λ_?m", "silver", "bronze", "tower",
                                     r"char\(M", r"m\^?2 ?\+ ?4", "m²\\+4"]),
    "dickson_tower":  dict(kind="structure", conserved="structural", domain="representation",
                           gloss="the Dickson tower rho_n / degree=rank / the det=-1 parity",
                           patterns=["Dickson", "degree.?=.?rank", r"rho_?n", r"ρ_?n", "det ?= ?-1",
                                     "det=-1", "two-sequence", r"L ?= ?\(-1\)", "Sym\\^"]),
    "eisenstein":     dict(kind="arithmetic", conserved="structural", domain="arithmetic",
                           gloss="the Eisenstein end: Q(sqrt-3), omega, E6, 2T",
                           patterns=["Eisenstein", r"sqrt.?-?3", "√−3", "√-3", "ℚ\\(√−3\\)", "omega",
                                     "ω", "cube root", "2T", "\\bE6\\b", "E₆"]),
    "golden":         dict(kind="arithmetic", conserved="structural", domain="arithmetic",
                           gloss="the golden end: Q(sqrt5), phi, E8, 2I",
                           patterns=["golden", r"sqrt.?5", "√5", "ℚ\\(√5\\)", r"\bphi\b", "φ",
                                     "Fibonacci", "2I", "\\bE8\\b", "E₈"]),
    "z3_generation":  dict(kind="symmetry", conserved="structural", domain="arithmetic",
                           gloss="the generation Z/3 (deck / commensurator / omega-circulant)",
                           patterns=["ℤ/3", "Z/3", "generation", "omega-circulant", "ω-circulant",
                                     "deck", "commensurator", "trinification"]),
    "amphichiral_cp": dict(kind="symmetry", conserved="structural", domain="topology",
                           gloss="amphichirality / the CP sign +-pi/6 / CS=0",
                           patterns=["amphichir", "CP sign", "CP phase", r"pi/6", "π/6", "mirror",
                                     "CS ?= ?0", "chern.?simons", "chirality"]),
    "torsion":        dict(kind="arithmetic", conserved="structural", domain="arithmetic",
                           gloss="the (Z/4)^2 congruence torsion / Alexander polynomial",
                           patterns=["torsion", "ℤ/4", "Z/4", "congruence", "Alexander", r"H_?1",
                                     r"\\(√−15\\)", "sqrt-15", "√−15"]),
    "symplectic":     dict(kind="structure", conserved="structural", domain="geometry",
                           gloss="the Goldman symplectic / Neumann-Zagier pairing",
                           patterns=["Goldman", "symplectic", "Poisson", "Neumann.?Zagier",
                                     "NZ pairing", "peripheral"]),
    "quasicrystal":   dict(kind="dynamics", conserved="structural", domain="quantum",
                           gloss="the Fibonacci quasicrystal / Suto / Damanik-Gorodetski",
                           patterns=["quasicrystal", "Fibonacci Hamiltonian", "KKT", "Cantor",
                                     "Damanik", "Gorodetski", "aperiodic", "Sturmian"]),
    "apolynomial":    dict(kind="structure", conserved="no", domain="topology",
                           gloss="the A-polynomial / Cooper-Long / AJ",
                           patterns=["A-polynomial", "A-poly", r"A\(M, L\)", "Cooper.?Long", r"\bAJ\b",
                                     "colored Jones"]),
    "wrt_quantum":    dict(kind="quantum", conserved="no", domain="quantum",
                           gloss="the WRT / colored-Jones / modular quantum invariants",
                           patterns=["WRT", "colored Jones", "quantum", "modular", "S-matrix",
                                     "T-matrix", "Habiro", "Reshetikhin", "Witten", "level.rank"]),
    "lorentzian":     dict(kind="physics-bridge", conserved="no", domain="physics",
                           gloss="the Lorentzian / signature / spacetime bridge",
                           patterns=["Lorentzian", "signature", "Minkowski", r"\(2,1\)", "BKL",
                                     "Kasner", "spacetime"]),
    "firewall":       dict(kind="structure", conserved="structural", domain="meta",
                           gloss="the firewall / structural theorem / form-not-values",
                           patterns=["firewall", "form.?not.?value", "form/contents", "no scale",
                                     "architecture.?not.?furniture", "structural theorem", "monad",
                                     "Galois"]),
    "five_web":       dict(kind="arithmetic", conserved="structural", domain="arithmetic",
                           gloss="the '5' recurrence web (H2): 40a1, conductor 40, Pisano",
                           patterns=["40a1", "conductor 40", "Pisano", "period 5", "5-web"]),
    "hyperbolicity_split": dict(kind="structure", conserved="structural", domain="topology",
                           gloss="the hyperbolicity-split motif (H4): object on both sides of the divide",
                           patterns=["hyperbolicity.split", "Seifert", "Sol geometry", "two bulks",
                                     "non-hyperbolic"]),
}

# --------------------------------------------------------------------------------------------------
# THE OBSTACLE TAXONOMY (docs/atlas/FAILURE_ATLAS.md categories, keyword-matched -- heuristic)
# --------------------------------------------------------------------------------------------------
OBSTACLES = {
    "source_free":   ["source-free", "cannot move", "no rule", "not-nothing", "from nothing"],
    "cancellation":  ["cancellation", "non-cancellation", "commut", "leaves no residue"],
    "selector":      ["selector", "forced choice", "no-forced-choice", "selection rule", "which one"],
    "measure":       ["measure", "prior", "ensemble", "large-N", "large deviation"],
    "units_scale":   ["units", "scale", "dimensionful", "dimensionless", "Lambda", "no scale", "magnitude"],
    "gauge_dict":    ["gauge", "gauge group", "gauge dictionary", "sin2theta", "3/8", "cascade"],
    "particle_dict": ["particle", "mass", "Yukawa", "hierarchy", "generation", "flavor", "PMNS", "mixing"],
    "spacetime_3p1": ["3+1", "spacetime", "Lorentzian", "signature", "climb", "rank"],
    "observable":    ["observable", "value hunt", "prediction", "falsifiable", "measured"],
    "numerology":    ["numerology", "value-match", "null test", "coincidence", "chance"],
    "bridge_construction": ["by construction", "tautolog", "vacuous", "succeeds by"],
}

REF_RE = re.compile(r"\b([BKSLPHV])(\d{1,3})\b")
STATUS_WORDS = [("dead", ["tombstone", "dead", "refuted", "killed", "wrong", "retracted"]),
                ("dormant", ["dormant", "needs-specialist", "parked", "unverified", "not verified"]),
                ("banked", ["banked", "verified", "proved", "proven", "confirmed", "[math]", "exact"]),
                ("open", ["open", "conditional", "candidate"])]


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read()


def _probe_id(slug_dir):
    m = re.match(r"(B\d{1,3})_", os.path.basename(slug_dir))
    return m.group(1) if m else None


def _match_motifs(text):
    hits = []
    low = text.lower()
    for name, info in LEXICON.items():
        for pat in info["patterns"]:
            try:
                if re.search(pat, text) or re.search(pat, low):
                    hits.append(name); break
            except re.error:
                if pat.lower() in low:
                    hits.append(name); break
    return hits


def _classify_obstacle(text):
    low = text.lower()
    scores = {ob: sum(low.count(k.lower()) for k in kws) for ob, kws in OBSTACLES.items()}
    best = max(scores, key=scores.get)
    return (best, scores[best]) if scores[best] > 0 else (None, 0)


def _status(text):
    low = text.lower()[:1500]                    # status lives near the top
    for label, words in STATUS_WORDS:
        if any(w in low for w in words):
            return label
    return "open"


def _primary_domain(motifs):
    doms = [LEXICON[m]["domain"] for m in motifs if LEXICON[m]["conserved"] != "tool"]
    return Counter(doms).most_common(1)[0][0] if doms else "dynamics"


def mine():
    """Parse the frontier probes into the atlas graph. Returns a dict (also written to atlas_data.json)."""
    probes = {}
    for d in sorted(glob.glob(os.path.join(REPO, "frontier", "B*"))):
        f = os.path.join(d, "FINDINGS.md")
        if not os.path.isdir(d) or not os.path.exists(f):
            continue
        pid = _probe_id(d)
        if not pid:
            continue
        text = _read(f)
        motifs = _match_motifs(text)
        refs = sorted({f"{a}{b}" for a, b in REF_RE.findall(text)} - {pid})
        obstacle, oconf = _classify_obstacle(text)
        probes[pid] = dict(
            slug=os.path.basename(d).split("_", 1)[-1].replace("_", " "),
            motifs=motifs, refs=refs, obstacle=obstacle, obstacle_conf=oconf,
            status=_status(text), domain=_primary_domain(motifs),
        )
    return dict(lexicon={k: {kk: v[kk] for kk in ("kind", "conserved", "domain", "gloss")}
                         for k, v in LEXICON.items()},
                obstacles=list(OBSTACLES), probes=probes)


def analyze(g):
    """Recurrence frequency, co-occurrence, the 'cycle' (obstacle->motif), the conserved-vs-tool split."""
    P = g["probes"]; n = len(P)
    freq = Counter(m for p in P.values() for m in p["motifs"])
    cooc = Counter()
    for p in P.values():
        ms = sorted(set(p["motifs"]))
        for i in range(len(ms)):
            for j in range(i + 1, len(ms)):
                cooc[(ms[i], ms[j])] += 1
    cycle = defaultdict(Counter)
    for p in P.values():
        if p["obstacle"]:
            for m in p["motifs"]:
                cycle[p["obstacle"]][m] += 1
    split = Counter()
    for m, c in freq.items():
        split[LEXICON[m]["conserved"]] += c
    return dict(n_probes=n, freq=dict(freq), cooccurrence={f"{a}|{b}": c for (a, b), c in cooc.items()},
                cycle={ob: dict(c) for ob, c in cycle.items()}, conserved_vs_tool=dict(split))


# --------------------------------------------------------------------------------------------------
# THE UNITY PATTERNS -- the repo's OWN named cross-structure identifications (co-occurrence signatures).
# These are seeded from the DOCUMENTED meetings (K007/K021/B67/B121/B261/B293); the detector then
# surfaces OTHER probes matching the same signatures as CANDIDATES for human judgement. NOT a per-probe
# curated table (that would rot) -- pattern-based, so it regenerates as the corpus grows.
# --------------------------------------------------------------------------------------------------
def _conserved(m):
    return LEXICON[m]["conserved"] in ("first-integral", "structural")

UNITY_PATTERNS = [
    dict(name="two_ends", weight=3,
         gloss="the two arithmetic ends (golden √5 / Eisenstein √−3) identified as one object -- K021/B332/B261",
         needs=lambda ms: "golden" in ms and "eisenstein" in ms),
    dict(name="object=dynamics", weight=2,
         gloss="the carrier knot realized as the trace-map fixed locus / its conserved trace -- B67/K007",
         needs=lambda ms: "figure_eight" in ms and ("kappa" in ms or "trace_map" in ms)),
    dict(name="physics_bridge", weight=3,
         gloss="a conserved math structure carried across the topology/arithmetic -> physics bridge -- B121",
         needs=lambda ms: any(LEXICON[m]["kind"] == "physics-bridge" for m in ms)
                          and sum(_conserved(m) for m in ms) >= 2),
    dict(name="quantum_meeting", weight=2,
         gloss="the WRT/AJ quantum invariant meeting the arithmetic ends -- B261",
         needs=lambda ms: "wrt_quantum" in ms and any(LEXICON[m]["domain"] == "arithmetic" for m in ms)),
    dict(name="symplectic_casimir", weight=2,
         gloss="kappa realized as the Goldman symplectic Casimir -- B293",
         needs=lambda ms: "symplectic" in ms and "kappa" in ms),
]


def meeting_points(g, top=15, min_score=8):
    """Heuristic detector: a probe where DISTINCT structures are identified -- high domain-breadth AND/OR
    a documented unity-pattern (co-occurrence signature). Returns a ranked list of CANDIDATES for human
    judgement, tagged with which patterns fired -- NEVER asserted as proof (verify-don't-trust)."""
    P = g["probes"]
    scored = []
    for pid, p in P.items():
        ms = set(p["motifs"])
        doms = {LEXICON[m]["domain"] for m in ms}
        cons = sorted(m for m in ms if _conserved(m))
        cdoms = {LEXICON[m]["domain"] for m in cons}
        matched = [up for up in UNITY_PATTERNS if up["needs"](ms)]
        score = len(doms) + len(cdoms) + sum(up["weight"] for up in matched)
        if score >= min_score:
            scored.append(dict(probe=pid, slug=p["slug"], score=score, status=p["status"],
                               domains=sorted(doms), patterns=[up["name"] for up in matched],
                               conserved_motifs=cons))
    scored.sort(key=lambda r: (-r["score"], r["probe"]))
    return scored[:top]


if __name__ == "__main__":
    g = mine()
    with open(DATA, "w", encoding="utf-8") as f:
        json.dump(g, f, indent=1, ensure_ascii=False)
    a = analyze(g)
    print(f"mined {a['n_probes']} probes -> {DATA}")
    print("top motif frequencies:",
          {k: v for k, v in sorted(a["freq"].items(), key=lambda kv: -kv[1])[:6]})
    print("conserved-vs-tool recurrence:", a["conserved_vs_tool"])
    print("top meeting-point candidates:", [(m["probe"], m["score"]) for m in meeting_points(g, 8)])
