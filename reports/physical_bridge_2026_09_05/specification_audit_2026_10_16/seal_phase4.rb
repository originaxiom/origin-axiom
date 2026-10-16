# Mechanical metadata source manifest and append-only design seal; no scientific imports.
require 'json'
require 'digest'
repo = File.expand_path('../../..', __dir__)
base = 'reports/physical_bridge_2026_09_05/specification_audit_2026_10_16/'
paths = %w[PHASE4_DESIGN.md prepare_phase4.rb seal_phase4.rb reconcile_coverage.rb review_records.json review_records_phase2.json review_records_phase3.json review_records_phase4.json specification_inventory.json role_pin_candidates_phase4.json].map { |p| base + p }
paths += %w[reports/physical_bridge_2026_09_05/ACTION_PARENT_SPECIFICATION_2026_10_16.md docs/SEAL_ARTIFACT_ROLES.json docs/GIT_REFERENCE_PROVENANCE.json scripts/gates/gates.py scripts/gates/provenance_policy.py]
rows = paths.map { |p| { 'path' => p, 'sha256' => Digest::SHA256.file(File.join(repo, p)).hexdigest } }
File.open(File.join(__dir__, 'PHASE4_INPUTS.json'), 'wx') do |f|
  f.write(JSON.pretty_generate({ 'scope' => 'Source audit/metadata verification before controls; no new scientific experiment', 'source_files' => rows }) + "\n")
end
design = rows.find { |r| r['path'] == base + 'PHASE4_DESIGN.md' }
File.open(File.join(repo, 'docs/SEAL_LEDGER.md'), 'a') do |f|
  f.write("\n## Phase4 action parent specification metadata before controls\n\n| date | stage | source | sha256 | scope |\n|---|---|---|---|---|\n")
  f.write('| 2026-10-16 | BEFORE phase4 metadata controls/reconciliation | `' + design['path'] + '` | `' + design['sha256'] + '` | Only this design is a preregistration; PHASE4_INPUTS pins metadata/source audit. Old scientific sources and live role policy unchanged. |' + "\n")
end
puts JSON.generate({ 'source_pins' => rows.size, 'design_sha256' => design['sha256'] })
