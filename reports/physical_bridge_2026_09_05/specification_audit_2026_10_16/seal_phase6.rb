# Mechanical metadata pins and append-only design seal; no scientific execution.
require 'json'
require 'digest'
repo = File.expand_path('../../..', __dir__)
base = 'reports/physical_bridge_2026_09_05/'
meta = base + 'specification_audit_2026_10_16/'
paths = %w[PHASE6_DESIGN.md prepare_phase6.rb seal_phase6.rb reconcile_coverage.rb
  review_records.json review_records_phase2.json review_records_phase3.json
  review_records_phase4.json review_records_phase5.json review_records_phase6.json
  specification_inventory.json].map { |p| meta + p }
paths += %w[END_MECHANISMS_AND_MAGNETIC_SCOPE_2026_10_16.md
  weave_global_condensate_2026_10_08/PROOF.md
  weave_graded_condensate_2026_10_08/PROOF.md
  weave_two_field_gauge_2026_10_08/PROOF.md
  weave_magnetic_stationarity_2026_10_08/PROOF.md
  weave_two_neutral_index_2026_10_08/PROOF.md
  weave_two_neutral_index_2026_10_08/probe.py
  weave_paired_phase_2026_10_08/PROOF.md
  weave_paired_phase_2026_10_08/probe.py
  weave_end_gaussian_2026_10_09/PROOF.md
  weave_end_gaussian_2026_10_09/probe.py
  weave_end_gaussian_2026_10_09/CORRECTION.md
  cusp_negative_audit_2026_10_09/PROOF.md
  cusp_negative_audit_2026_10_09/POST_PUBLICATION_INTAKE.md
  weave_boundary_lift_2026_10_09/PROOF.md
  weave_boundary_index_2026_10_09/PROOF.md].map { |p| base + p }
paths += %w[docs/SEAL_ARTIFACT_ROLES.json docs/GIT_REFERENCE_PROVENANCE.json
  scripts/gates/gates.py scripts/gates/provenance_policy.py]
abort('source path duplication') unless paths.uniq == paths
rows = paths.map { |p| { 'path' => p, 'sha256' => Digest::SHA256.file(File.join(repo, p)).hexdigest } }
out = File.join(__dir__, 'PHASE6_INPUTS.json')
ledger = File.join(repo, 'docs/SEAL_LEDGER.md')
design = rows.find { |r| r['path'] == meta + 'PHASE6_DESIGN.md' }
abort('phase6 already sealed') if File.exist?(out) || File.read(ledger).include?('`' + design.fetch('path') + '`')
File.open(out, 'wx') do |f|
  f.write(JSON.pretty_generate({ 'scope' => 'Source reading and metadata verification, not scientific execution',
    'source_files' => rows }) + "\n")
end
File.open(ledger, 'a') do |f|
  f.puts "| 2026-10-16 | BEFORE phase6 metadata controls | `#{design.fetch('path')}` | `#{design.fetch('sha256')}` | Only design sealed; metadata pins do not admit science or waive history. |"
end
puts JSON.generate({ 'source_pins' => rows.size, 'design_sha256' => design.fetch('sha256') })
