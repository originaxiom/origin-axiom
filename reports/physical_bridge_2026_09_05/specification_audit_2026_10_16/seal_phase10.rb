# Source/metadata pins and append-only design seal; no scientific execution.
require 'json'
require 'digest'
repo = File.expand_path('../../..', __dir__)
base = 'reports/physical_bridge_2026_09_05/'
meta = base + 'specification_audit_2026_10_16/'
paths = %w[PHASE10_DESIGN.md prepare_phase10.rb seal_phase10.rb reconcile_coverage.rb
  review_records.json review_records_phase2.json review_records_phase3.json
  review_records_phase4.json review_records_phase5.json review_records_phase6.json
  review_records_phase7.json review_records_phase8.json review_records_phase9.json
  review_records_phase10.json specification_inventory.json].map { |p| meta + p }
paths += %w[HISTORICAL_DOMAIN_AND_SYMMETRY_SPECIFICATION_2026_10_16.md
  AFFINE_BACKGROUND_PROOF.md CANONICAL_CUSP_PROOF.md
  CANONICAL_INTERACTION_PROOF.md CANONICAL_DUALITY_PROOF.md
  CROSS_BRANCH_POSITIVES_PROOF.md DIRICHLET_ADMISSION_PROOF.md
  GLUING_FREEDOM_PROOF.md FLAT_DOMAIN_PROOF.md CS_SECTOR_SCOPE_PROOF.md
  AFFINE_SPIN_PROOF.md affine_spin.py affine_spin_reference.py
  cs_sector_scope.py cs_sector_scope_control.py
  flat_domain_audit.py flat_domain_reference.py
  FLAT_DOMAIN_INPUTS.json FLAT_DOMAIN_AUDIT.md CS_SECTOR_SCOPE.md
  PARENT_CUSP_PROOF.md].map { |p| base + p }
paths += %w[docs/SEAL_ARTIFACT_ROLES.json docs/GIT_REFERENCE_PROVENANCE.json
  scripts/gates/gates.py scripts/gates/provenance_policy.py]
abort('source path duplication') unless paths.uniq == paths
rows = paths.map { |p| { 'path' => p, 'sha256' => Digest::SHA256.file(File.join(repo, p)).hexdigest } }
out = File.join(__dir__, 'PHASE10_INPUTS.json')
ledger = File.join(repo, 'docs/SEAL_LEDGER.md')
design = rows.find { |r| r['path'] == meta + 'PHASE10_DESIGN.md' }
tick = 96.chr
abort('phase10 already sealed') if File.exist?(out) || File.read(ledger).include?(tick + design.fetch('path') + tick)
File.open(out, 'wx') do |f|
  f.write(JSON.pretty_generate({ 'scope' => 'Source reading and metadata verification, not scientific execution',
    'source_files' => rows }) + "\n")
end
File.open(ledger, 'a') do |f|
  f.puts "| 2026-10-16 | BEFORE phase10 metadata controls | #{tick}#{design.fetch('path')}#{tick} | #{tick}#{design.fetch('sha256')}#{tick} | Only design sealed; metadata pins do not admit science or waive history. |"
end
puts JSON.generate({ 'source_pins' => rows.size, 'design_sha256' => design.fetch('sha256') })
