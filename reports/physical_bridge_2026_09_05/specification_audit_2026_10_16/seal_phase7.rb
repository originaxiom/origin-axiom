# Mechanical metadata pins and append-only design seal; no scientific execution.
require 'json'
require 'digest'
repo = File.expand_path('../../..', __dir__)
base = 'reports/physical_bridge_2026_09_05/'
meta = base + 'specification_audit_2026_10_16/'
paths = %w[PHASE7_DESIGN.md prepare_phase7.rb seal_phase7.rb reconcile_coverage.rb
  review_records.json review_records_phase2.json review_records_phase3.json
  review_records_phase4.json review_records_phase5.json review_records_phase6.json
  review_records_phase7.json specification_inventory.json].map { |p| meta + p }
paths += %w[PHYSICAL_INDEX_AND_QUANTUM_END_SPECIFICATION_2026_10_16.md
  weave_physical_mass_2026_10_08/PROOF.md
  weave_cusp_anomaly_2026_10_08/PROOF.md
  weave_cusp_heat_2026_10_08/PROOF.md
  weave_cusp_ward_2026_10_08/PROOF.md
  weave_gauge_limit_2026_10_08/PROOF.md
  weave_companion_roster_2026_10_08/PROOF.md
  weave_physical_mass_2026_10_08/probe.py
  weave_cusp_heat_2026_10_08/probe.py
  weave_cusp_ward_2026_10_08/probe.py
  weave_gauge_limit_2026_10_08/probe.py
  weave_two_neutral_index_2026_10_08/PROOF.md
  weave_paired_phase_2026_10_08/PROOF.md].map { |p| base + p }
paths += %w[tests/test_physical_bridge_weave_physical_mass.py
  tests/test_physical_bridge_weave_cusp_heat.py
  tests/test_physical_bridge_weave_cusp_ward.py
  docs/SEAL_ARTIFACT_ROLES.json docs/GIT_REFERENCE_PROVENANCE.json
  scripts/gates/gates.py scripts/gates/provenance_policy.py]
abort('source path duplication') unless paths.uniq == paths
rows = paths.map { |p| { 'path' => p, 'sha256' => Digest::SHA256.file(File.join(repo, p)).hexdigest } }
out = File.join(__dir__, 'PHASE7_INPUTS.json')
ledger = File.join(repo, 'docs/SEAL_LEDGER.md')
design = rows.find { |r| r['path'] == meta + 'PHASE7_DESIGN.md' }
tick = 96.chr
abort('phase7 already sealed') if File.exist?(out) || File.read(ledger).include?(tick + design.fetch('path') + tick)
File.open(out, 'wx') do |f|
  f.write(JSON.pretty_generate({ 'scope' => 'Source reading and metadata verification, not scientific execution',
    'source_files' => rows }) + "\n")
end
File.open(ledger, 'a') do |f|
  f.puts "| 2026-10-16 | BEFORE phase7 metadata controls | #{tick}#{design.fetch('path')}#{tick} | #{tick}#{design.fetch('sha256')}#{tick} | Only design sealed; metadata pins do not admit science or waive history. |"
end
puts JSON.generate({ 'source_pins' => rows.size, 'design_sha256' => design.fetch('sha256') })
