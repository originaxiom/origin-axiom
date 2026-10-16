# Mechanical metadata pins and append-only design seal; no scientific execution.
require 'json'
require 'digest'
repo = File.expand_path('../../..', __dir__)
base = 'reports/physical_bridge_2026_09_05/'
meta = base + 'specification_audit_2026_10_16/'
paths = %w[PHASE8_DESIGN.md prepare_phase8.rb seal_phase8.rb reconcile_coverage.rb
  review_records.json review_records_phase2.json review_records_phase3.json
  review_records_phase4.json review_records_phase5.json review_records_phase6.json
  review_records_phase7.json review_records_phase8.json specification_inventory.json].map { |p| meta + p }
paths += %w[INTERACTING_TRACE_AND_TRANSPORT_SPECIFICATION_2026_10_16.md
  surface_based_gauge_2026_10_14/PROOF.md
  surface_invariant_brackets_2026_10_14/PROOF.md
  surface_weak_completions_2026_10_14/PROOF.md
  surface_mode_transport_2026_10_15/PROOF.md
  surface_real_boundary_2026_10_15/PROOF.md
  surface_interacting_domain_2026_10_15/PROOF.md
  surface_interacting_transport_2026_10_16/PROOF.md
  surface_variational_join_2026_10_16/PROOF.md
  surface_critical_cauchy_2026_10_16/PROOF.md
  surface_all_angular_response_2026_10_16/PROOF.md
  surface_all_boson_response_2026_10_16/PROOF.md
  surface_same_action_transmission_2026_10_16/PROOF.md
  surface_based_gauge_2026_10_14/probe.py
  surface_mode_transport_2026_10_15/probe.py
  surface_mode_transport_2026_10_15/analysis.py
  surface_interacting_domain_2026_10_15/probe.py
  surface_interacting_domain_2026_10_15/analysis.py
  surface_based_gauge_2026_10_14/REPAIR.md
  surface_invariant_brackets_2026_10_14/FINDINGS.md
  surface_weak_completions_2026_10_14/FINDINGS.md
  surface_variational_join_2026_10_16/SOURCE_CHECK.md
  surface_source_operator_2026_10_16/PROOF.md].map { |p| base + p }
paths += %w[docs/SEAL_ARTIFACT_ROLES.json docs/GIT_REFERENCE_PROVENANCE.json
  scripts/gates/gates.py scripts/gates/provenance_policy.py]
abort('source path duplication') unless paths.uniq == paths
rows = paths.map { |p| { 'path' => p, 'sha256' => Digest::SHA256.file(File.join(repo, p)).hexdigest } }
out = File.join(__dir__, 'PHASE8_INPUTS.json')
ledger = File.join(repo, 'docs/SEAL_LEDGER.md')
design = rows.find { |r| r['path'] == meta + 'PHASE8_DESIGN.md' }
tick = 96.chr
abort('phase8 already sealed') if File.exist?(out) || File.read(ledger).include?(tick + design.fetch('path') + tick)
File.open(out, 'wx') do |f|
  f.write(JSON.pretty_generate({ 'scope' => 'Source reading and metadata verification, not scientific execution',
    'source_files' => rows }) + "\n")
end
File.open(ledger, 'a') do |f|
  f.puts "| 2026-10-16 | BEFORE phase8 metadata controls | #{tick}#{design.fetch('path')}#{tick} | #{tick}#{design.fetch('sha256')}#{tick} | Only design sealed; metadata pins do not admit science or waive history. |"
end
puts JSON.generate({ 'source_pins' => rows.size, 'design_sha256' => design.fetch('sha256') })
