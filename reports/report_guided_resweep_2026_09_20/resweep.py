"""Second-pass retrieval keyed to the preceding report, not a scientific producer.

Reuse the first scanner with no extension whitelist and a 32 MB size bound.
Thus shell heredocs, extensionless text and notebooks are candidates as well.
NUL-containing binary data are excluded. A matching binary/PDF byte string is
not a full-text or visual reading. This is retrieval, not semantic absence proof.
"""
import importlib.util
from pathlib import Path
import sys

PATTERNS = {
    '01_admissibility': 'harmonic metric|corlette|polystab|finite-energy|finite energy|nonsemisimple|nonsplit|non-split',
    '02_action_sources': 'moment map|moment-map|noncentral|non-central|defect action|fayet|parabolic weight|coadjoint|source action|parent action',
    '03_operator_domain': 'self-adjoint extension|operator domain|finite-width|renormalized defect|renormalised defect|vanishing capacity|capacity-zero|boundary condition',
    '04_mirror_gap': 'mirror gap|mirror-gap|mirror remov|symmetric mass|quartic|whole eigenspace|overlap matrix',
    '05_anomaly': 'anomaly inflow|anomaly matching|eta invariant|η invariant|dai-freed|bordism|witten anomaly|spectator chirality',
    '06_four_dimensions': 'neutral channel|neutral cusp|effective four|4d limit|four-dimensional limit|spectral measure|warp factor|warped metric',
    '07_parent_maps': 'hecke|correspondence|equivariant bundle|descent datum|arithmetic parent|binary tetrahedral|tannakian',
    '08_state_selection': 'vacuum alignment|effective potential|state selection|spontaneous|kahler potential|kähler potential|stability parameter',
    '09_gauge_selector': 'hypercharge direction|hypercharge normalization|hypercharge normalisation|cocharacter|embedding index|regular embedding|gauge kinetic',
    '10_higgs_exotics': 'doublet-triplet|doublet–triplet|proton decay|proton-decay|wilson line|triplet mass',
    '11_observable_quotient': 'canonical normalization|canonical normalisation|field redefinition|kinetic metric|kinetic matrix|physical quotient|observable map',
    '12_flavor': 'hollow texture|mixing invariant|mass hierarchy|jarlskog|yukawa texture|kinetic matrix|full texture',
    '13_global_geometry': 'torsion-free g2|torsion free g2|coassociative|ale fibration|acharya-witten|maximal isotropy|curved cone|curved-cone',
    '14_gravity': 'fierz-pauli|einstein-hilbert|universal coupling|stress tensor|ghost-free|lorentzian|spin-two',
    '15_index_certificate': '3d index|3d-index|tetrahedron index|summation tail|coerciv|step17_rigor|saturated lattice|index structure',
    '16_partial_filling': 'partial filling|partially fill|partial dehn|relative gluing|dehn filling formula|dehn-filling formula|klllplqkcefegijjiijiieldllxtxa',
    '17_quantum_states': 'hilbert space|hilbert-space|reflection positivity|positive representation|unitary representation|andersen|kashaev|born rule',
    '18_thresholds': 'friedmann|primed determinant|non-acyclic|nonacyclic|zero-mode normalization|torsion threshold',
    '19_physical_scale': 'renormalization group|renormalisation group|coarse-graining|coarse graining|scale map|tower growth|dimensional transmutation',
    '20_cusped_determinant': 'scattering determinant|scattering matrix|leading laurent|graviton determinant|functional equation|residue 2',
    '21_index_mechanism': 'index jump|jump locus|jump loci|t12835|higher-sym|higher sym|extension space|metabelian',
    '22_laboratory': 'isospectral|localization split|localisation split|per-gap|polariton|photonic|experimental resolution',
    'f01_hypotheses': 'busemann|horosphere|invariant subbundle|invariant complement|weighted harmonic|weighted energy|renormalized energy|renormalised energy|dirichlet problem',
    'heredoc_control': '553/64',
}


if __name__ == '__main__':
    source = Path(__file__).resolve().parents[1]/'whole_picture_audit_2026_09_20'/'scan.py'
    spec = importlib.util.spec_from_file_location('prior_audit_scanner', source)
    scanner = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(scanner)
    scanner.main(sys.argv[1], topic_patterns=PATTERNS, text_extensions=None, max_bytes=32_000_000)
