# Exact metadata/source pins and design seal; never execute scientific code.
require 'json'
require 'digest'
repo = File.expand_path('../../..', __dir__)
base = 'reports/physical_bridge_2026_09_05/'
meta = base + 'specification_audit_2026_10_16/'
paths = %w[PHASE9_DESIGN.md prepare_phase9.rb seal_phase9.rb reconcile_coverage.rb
  review_records.json review_records_phase2.json review_records_phase3.json
  review_records_phase4.json review_records_phase5.json review_records_phase6.json
  review_records_phase7.json review_records_phase8.json review_records_phase9.json
  specification_inventory.json].map { |p| meta + p }
paths += %w[GLOBAL_END_AND_GAUGE_SPECIFICATION_2026_10_16.md
  surface_weighted_hessian_2026_10_16/PROOF.md
  surface_real_fermion_work_2026_10_16/PROOF.md
  surface_real_superfield_2026_10_16/PROOF.md
  surface_gauss_charge_2026_10_16/PROOF.md
  surface_actual_tube_2026_10_16/PROOF.md
  surface_arena_boundary_2026_10_16/PROOF.md
  surface_curved_boson_2026_10_16/PROOF.md
  surface_inner_cauchy_2026_10_16/PROOF.md
  surface_root_gauge_sector_2026_10_16/PROOF.md
  surface_angular_response_2026_10_16/PROOF.md
  surface_gauss_charge_2026_10_16/analysis.py
  surface_actual_tube_2026_10_16/analysis.py
  surface_arena_boundary_2026_10_16/analysis.py
  surface_gauss_charge_2026_10_16/probe.py
  surface_actual_tube_2026_10_16/probe.py
  surface_arena_boundary_2026_10_16/probe.py
  surface_actual_tube_2026_10_16/POST_HOC_REPAIR.md
  surface_arena_boundary_2026_10_16/POST_HOC_REPAIR.md
  surface_real_fermion_work_2026_10_16/POST_HOC_REPAIR.md
  surface_global_boundary_variation_2026_10_16/PROOF.md].map { |p| base + p }
paths += %w[docs/SEAL_ARTIFACT_ROLES.json docs/GIT_REFERENCE_PROVENANCE.json
  scripts/gates/gates.py scripts/gates/provenance_policy.py]
abort('source path duplication') unless paths.uniq == paths
rows = paths.map { |p| { 'path' => p, 'sha256' => Digest::SHA256.file(File.join(repo, p)).hexdigest } }
out = File.join(__dir__, 'PHASE9_INPUTS.json')
ledger = File.join(repo, 'docs/SEAL_LEDGER.md')
design = rows.find { |r| r['path'] == meta + 'PHASE9_DESIGN.md' }
tick = 96.chr
abort('phase9 already sealed') if File.exist?(out) || File.read(ledger).include?(tick + design.fetch('path') + tick)
File.open(out, 'wx') do |f|
  f.write(JSON.pretty_generate({ 'scope' => 'Source reading and metadata verification, not scientific execution',
    'source_files' => rows }) + "\n")
end
File.open(ledger, 'a') do |f|
  f.puts "| 2026-10-16 | BEFORE phase9 metadata controls | #{tick}#{design.fetch('path')}#{tick} | #{tick}#{design.fetch('sha256')}#{tick} | Only design sealed; metadata pins do not admit science or waive history. |"
end
puts JSON.generate({ 'source_pins' => rows.size, 'design_sha256' => design.fetch('sha256') })
