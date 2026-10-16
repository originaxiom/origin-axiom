# Mechanical source pins and append-only design seal; no scientific execution.
require 'json'
require 'digest'
repo = File.expand_path('../../..', __dir__)
base = 'reports/physical_bridge_2026_09_05/'
meta = base + 'specification_audit_2026_10_16/'
paths = %w[PHASE5_DESIGN.md prepare_phase5.rb seal_phase5.rb reconcile_coverage.rb
  review_records.json review_records_phase2.json review_records_phase3.json
  review_records_phase4.json review_records_phase5.json specification_inventory.json].map { |p| meta + p }
paths += %w[KINETIC_AND_END_SPECIFICATION_2026_10_16.md
  surface_geometric_loops_2026_10_14/PROOF.md
  surface_geometric_loops_2026_10_14/ORIENTATION_REPAIR.md
  based_transition_prerequisite_2026_10_13/PROOF.md
  weave_cusp_condensate_2026_10_08/PROOF.md
  weave_sm_parallel_2026_10_08/PROOF.md
  weave_neutral_stability_2026_10_08/PROOF.md
  weave_magnetic_index_2026_10_08/PROOF.md
  surface_even_channels_2026_10_14/PROOF.md
  surface_even_channels_2026_10_14/FULL_EVEN_PROOF.md
  surface_parent_dictionary_2026_10_13/PROOF.md
  surface_parent_dictionary_2026_10_13/SCOPE_REVIEW.md
  surface_global_spin_2026_10_13/PROOF.md
  spinor_uniformization_joint_2026_10_14/PROOF.md
  surface_odd_form_2026_10_14/PROOF.md].map { |p| base + p }
paths += %w[docs/SEAL_ARTIFACT_ROLES.json docs/GIT_REFERENCE_PROVENANCE.json
  scripts/gates/gates.py scripts/gates/provenance_policy.py]
abort('source path duplication') unless paths.uniq == paths
rows = paths.map { |p| { 'path' => p, 'sha256' => Digest::SHA256.file(File.join(repo, p)).hexdigest } }
out = File.join(__dir__, 'PHASE5_INPUTS.json')
ledger = File.join(repo, 'docs/SEAL_LEDGER.md')
design = rows.find { |r| r['path'] == meta + 'PHASE5_DESIGN.md' }
abort('phase5 already sealed') if File.exist?(out) || File.read(ledger).include?('`' + design.fetch('path') + '`')
File.open(out, 'wx') do |f|
  f.write(JSON.pretty_generate({ 'scope' => 'Source reading and metadata verification, not scientific execution',
    'source_files' => rows }) + "\n")
end
File.open(ledger, 'a') do |f|
  f.puts "| 2026-10-16 | BEFORE phase5 metadata controls | `#{design.fetch('path')}` | `#{design.fetch('sha256')}` | Only design sealed; metadata pins do not admit science or waive history. |"
end
puts JSON.generate({ 'source_pins' => rows.size, 'design_sha256' => design.fetch('sha256') })
