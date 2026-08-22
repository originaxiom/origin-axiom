"""STEP 2 -- load the sealed SM targets verbatim; record sha256 + count."""
import hashlib, json, os

_REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PDG_PATH = os.path.join(_REPO, 'frontier', 'B743_rung1_widened', 'pdg_targets.json')

def load_targets():
    with open(PDG_PATH, 'rb') as f:
        raw = f.read()
    sha = hashlib.sha256(raw).hexdigest()
    targets = json.loads(raw)
    return targets, sha

if __name__ == '__main__':
    targets, sha = load_targets()
    print('sha256:', sha)
    print('count:', len(targets))
    for t in targets:
        print(f"  {t['name']:28s} value={t['value']:>16s} digits={t['digits']} rel_unc={t['rel_unc']}")
