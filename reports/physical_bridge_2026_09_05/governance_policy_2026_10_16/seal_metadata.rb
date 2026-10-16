# Mechanical source hashes and append-only design seal. No scientific execution.
require 'json'
require 'digest'
root = File.expand_path('../../..', __dir__)
base = 'reports/physical_bridge_2026_09_05/governance_policy_2026_10_16/'
paths = %w[scripts/gates/gates.py scripts/gates/provenance_policy.py tests/test_governance_provenance_policy.py docs/PRACTICES.md docs/SEAL_ARTIFACT_ROLES.json docs/GIT_REFERENCE_PROVENANCE.json]
paths += %w[DESIGN.md adopt_records.rb snapshot.rb seal_metadata.rb].map { |p| base + p }
rows = paths.map { |p| { 'path' => p, 'sha256' => Digest::SHA256.file(File.join(root, p)).hexdigest } }
File.open(File.join(root, base, 'INPUTS.json'), 'wx') do |f|
  f.write(JSON.pretty_generate({ 'scope' => 'Initial approved governance implementation before focused tests; not science or green certification', 'source_files' => rows }) + "\n")
end
design = rows.find { |r| r['path'] == base + 'DESIGN.md' }
File.open(File.join(root, 'docs/SEAL_LEDGER.md'), 'a') do |f|
  f.write("\n## Evidence preserving governance policy before first maintenance tests\n\n| date | stage | source | sha256 | scope |\n|---|---|---|---|---|\n")
  f.write('| 2026-10-16 | BEFORE first focused policy tests | `' + design['path'] + '` | `' + design['sha256'] + '` | Owner-approved typed enforcement; historical violations remain failures. Only this design is a preregistration; INPUTS holds source pins. |' + "\n")
end
puts JSON.generate({ 'source_pins' => rows.size, 'design_sha256' => design['sha256'] })
