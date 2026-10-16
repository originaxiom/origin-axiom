# Mechanical manifest generation only, no science import or execution.
require 'json'
require 'digest'
require 'pathname'
root=Pathname.new(__dir__).parent.parent.parent
local=Pathname.new(__dir__).relative_path_from(root).to_s
stage=ARGV.fetch(0,'full parent reality BEFORE execution')
sources=%w[DESIGN.md PROOF.md analysis.py probe.py reference.py execute.py make_seal.rb].map { |n| local+'/'+n }
sources += [
 'tests/test_physical_bridge_surface_real_boundary.py',
 'frontier/B1138_structural_completion/verification/my_chevalley.py',
 'reports/physical_bridge_2026_09_05/surface_parent_dictionary_2026_10_13/upstream_total_metric.py',
 'reports/physical_bridge_2026_09_05/surface_parent_dictionary_2026_10_13/PROOF.md',
 'reports/physical_bridge_2026_09_05/surface_global_spin_2026_10_13/PROOF.md',
 'reports/physical_bridge_2026_09_05/surface_odd_form_2026_10_14/upstream_total_domain_PROOF.md',
 'reports/physical_bridge_2026_09_05/surface_odd_form_2026_10_14/upstream_puncture_fredholm_PROOF.md',
 'reports/physical_bridge_2026_09_05/surface_geometric_loops_2026_10_14/PROOF.md',
 'reports/physical_bridge_2026_09_05/surface_invariant_brackets_2026_10_14/analysis.py',
 'reports/physical_bridge_2026_09_05/surface_invariant_brackets_2026_10_14/reference.py',
 'reports/physical_bridge_2026_09_05/surface_mode_transport_2026_10_15/PROOF.md',
 'reports/physical_bridge_2026_09_05/surface_mode_transport_2026_10_15/execute.py'
]
sources << local+'/POST_HOC_REPAIR.md' if File.exist?(root.join(local,'POST_HOC_REPAIR.md'))
rows=sources.sort.map { |p| {'path'=>p,'sha256'=>Digest::SHA256.file(root.join(p)).hexdigest} }
metadata={'scope'=>'Specified full MW/R/compact-E8 parent and paired critical law; local interacting Higgs graph control, not complete global boundary physics',
 'runtime'=>{'python'=>'3.12.14','sympy'=>'1.14.0'},
 'shared_formulation'=>'analysis.py and Sympy; actual-frame/lower and exterior-Fock/upper engines, shared author, no independent analytic review',
 'source_files'=>rows}
File.write(root.join(local,'INPUTS.json'),JSON.pretty_generate(metadata)+"\n")
all=rows+[{'path'=>local+'/INPUTS.json','sha256'=>Digest::SHA256.file(root.join(local,'INPUTS.json')).hexdigest}]
File.write(root.join(local,'ARTIFACT_HASHES.txt'),all.map { |r| r['sha256']+'  '+r['path'] }.join("\n")+"\n")
File.open(root.join('docs/SEAL_LEDGER.md'),'a') do |f|
 f.write("\n## Full parent reality and local interacting trace: "+stage+"\n\n| date | stage | source | sha256 | scope |\n|---|---|---|---|---|\n")
 all.each { |r| f.write('| 2026-10-15 | '+stage+' | `'+r['path']+'` | `'+r['sha256']+'` | Full fermion reality/current plus local interacting graph; not complete global physical boundary law/index |'+"\n") }
end
puts JSON.generate({'pins'=>rows.length,'design_sha256'=>rows.find { |r| r['path']==local+'/DESIGN.md' }['sha256']})
