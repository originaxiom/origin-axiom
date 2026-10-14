# Mechanical source hashing/metadata generation, never the science producer.
require 'json'
require 'digest'
require 'pathname'

root = Pathname.new(__dir__).parent.parent.parent
local = Pathname.new(__dir__).relative_path_from(root).to_s
sources = %w[DESIGN.md PROOF.md SEAL_PREPARATION.md analysis.py probe.py reference.py execute.py make_seal.rb].map { |n| local+'/'+n }
sources << local+'/POST_HOC_REPAIR.md' if File.exist?(root.join(local,'POST_HOC_REPAIR.md'))
stage=ARGV.fetch(0,'actual invariant15 BEFORE execution')
sources += [
  'tests/test_physical_bridge_surface_invariant_brackets.py',
  'frontier/B1138_structural_completion/verification/my_chevalley.py',
  'reports/physical_bridge_2026_09_05/weave_registered_embedding_2026_10_13/probe.py',
  'reports/physical_bridge_2026_09_05/weave_registered_embedding_2026_10_13/PROOF.md',
  'reports/physical_bridge_2026_09_05/surface_based_gauge_2026_10_14/probe.py',
  'reports/physical_bridge_2026_09_05/surface_based_gauge_2026_10_14/PROOF.md',
  'reports/physical_bridge_2026_09_05/surface_weak_completions_2026_10_14/probe.py',
  'reports/physical_bridge_2026_09_05/surface_weak_completions_2026_10_14/PROOF.md',
  'reports/physical_bridge_2026_09_05/surface_geometric_loops_2026_10_14/PROOF.md'
]
rows = sources.sort.map { |p| {'path'=>p,'sha256'=>Digest::SHA256.file(root+p).hexdigest} }
metadata = {'scope'=>'Actual invariant algebra in the fixed based compact E8 lifts, all commuting weak corrections; not every background or physical spectrum',
  'runtime'=>{'python'=>'3.12.14','sympy'=>'1.14.0'}, 'shared_formulation'=>'analysis.py; separate lower/dense and upper/sparse bracket engines',
  'source_files'=>rows}
File.write(root.join(local,'INPUTS.json'),JSON.pretty_generate(metadata)+"\n")
all=rows+[{'path'=>local+'/INPUTS.json','sha256'=>Digest::SHA256.file(root.join(local,'INPUTS.json')).hexdigest}]
File.write(root.join(local,'ARTIFACT_HASHES.txt'),all.map { |r| r['sha256']+'  '+r['path'] }.join("\n")+"\n")
ledger = root+'docs/SEAL_LEDGER.md'
File.open(ledger,'a') do |f|
  f.write("\n## Actual invariant15 brackets: "+stage+"\n\n| date | stage | source | sha256 | scope |\n|---|---|---|---|---|\n")
  all.each { |r| f.write('| 2026-10-15 | '+stage+' | `'+r['path']+'` | `'+r['sha256']+'` | Actual closure/real form/roots; no dimension-only or physical SM identification |'+"\n") }
end
puts JSON.generate({'pins'=>rows.length,'design_sha256'=>rows.find { |r| r['path']==local+'/DESIGN.md' }['sha256']})
