require 'json'
require 'digest'
root = File.expand_path('../../..', __dir__)
base = 'reports/physical_bridge_2026_09_05/governance_policy_2026_10_16/'
paths = %w[docs/GIT_REFERENCE_PROVENANCE.json docs/SEAL_ARTIFACT_ROLES.json scripts/gates/gates.py scripts/gates/provenance_policy.py tests/test_governance_provenance_policy.py]
paths += %w[REFERENCE_SUPPLEMENT.md corroborate_names.rb seal_supplement.rb snapshot.rb].map { |p| base + p }
rows = paths.map { |p| { 'path' => p, 'sha256' => Digest::SHA256.file(File.join(root, p)).hexdigest } }
File.open(File.join(root, base, 'INPUTS_SUPPLEMENT.json'), 'wx') do |f|
  f.write(JSON.pretty_generate({ 'scope' => 'Cross-capture ref-name corroboration before focused tests; not reconstruction of earlier tips or timing', 'source_files' => rows }) + "\n")
end
design = rows.find { |r| r['path'] == base + 'REFERENCE_SUPPLEMENT.md' }
File.open(File.join(root, 'docs/SEAL_LEDGER.md'), 'a') do |f|
  f.write("\n## Cross capture reference names before maintenance verification\n\n| date | stage | source | sha256 | scope |\n|---|---|---|---|---|\n")
  f.write('| 2026-10-16 | BEFORE supplementary focused tests | `' + design['path'] + '` | `' + design['sha256'] + '` | Existing pinned corroboration, not earlier tips/timing. INPUTS_SUPPLEMENT pins unchanged verifier and changed test/policy. |' + "\n")
end
puts JSON.generate({ 'source_pins' => rows.size, 'design_sha256' => design['sha256'] })
