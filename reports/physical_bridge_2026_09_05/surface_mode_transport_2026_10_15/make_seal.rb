# Mechanical manifests only; does not import or execute the science.
require 'json'
require 'digest'
require 'pathname'
root=Pathname.new(__dir__).parent.parent.parent
local=Pathname.new(__dir__).relative_path_from(root).to_s
stage=ARGV.fetch(0,'actual cusp sections BEFORE execution')
sources=%w[DESIGN.md PROOF.md analysis.py probe.py reference.py execute.py make_seal.rb].map { |n| local+'/'+n }
sources += [
  'tests/test_physical_bridge_surface_mode_transport.py',
  'reports/physical_bridge_2026_09_05/finite_twist_reductivity.py',
  'reports/physical_bridge_2026_09_05/surface_odd_form_2026_10_14/PROOF.md',
  'reports/physical_bridge_2026_09_05/surface_odd_form_2026_10_14/upstream_vertical_cusp_gap_PROOF.md',
  'reports/physical_bridge_2026_09_05/surface_odd_form_2026_10_14/upstream_horizontal_projection_PROOF.md',
  'reports/physical_bridge_2026_09_05/surface_even_channels_2026_10_14/FULL_EVEN_PROOF.md',
  'reports/physical_bridge_2026_09_05/surface_based_gauge_2026_10_14/PROOF.md',
  'reports/physical_bridge_2026_09_05/surface_weak_completions_2026_10_14/PROOF.md',
  'reports/physical_bridge_2026_09_05/surface_geometric_loops_2026_10_14/PROOF.md',
  'reports/physical_bridge_2026_09_05/surface_geometric_loops_2026_10_14/results/corrected_science/probe.stdout.log'
]
sources << local+'/POST_HOC_REPAIR.md' if File.exist?(root.join(local,'POST_HOC_REPAIR.md'))
rows=sources.sort.map { |p| {'path'=>p,'sha256'=>Digest::SHA256.file(root.join(p)).hexdigest} }
metadata={'scope'=>'Specified completed E8 coefficient: actual cusp kernel sections under credited graph/projection hypotheses, all commuting weak completions; not a physical index',
  'runtime'=>{'python'=>'3.12.14','sympy'=>'1.14.0'},
  'shared_formulation'=>'analysis.py and Sympy; separate prefix/reverse word engines, not independent analytic review',
  'source_files'=>rows}
File.write(root.join(local,'INPUTS.json'),JSON.pretty_generate(metadata)+"\n")
all=rows+[{'path'=>local+'/INPUTS.json','sha256'=>Digest::SHA256.file(root.join(local,'INPUTS.json')).hexdigest}]
File.write(root.join(local,'ARTIFACT_HASHES.txt'),all.map { |r| r['sha256']+'  '+r['path'] }.join("\n")+"\n")
File.open(root.join('docs/SEAL_LEDGER.md'),'a') do |f|
  f.write("\n## Actual cusp kernel transport: "+stage+"\n\n| date | stage | source | sha256 | scope |\n|---|---|---|---|---|\n")
  all.each { |r| f.write('| 2026-10-15 | '+stage+' | `'+r['path']+'` | `'+r['sha256']+'` | Cusp sections/normalized operator; not global real-parent admission or physical index |'+"\n") }
end
puts JSON.generate({'pins'=>rows.length,'design_sha256'=>rows.find { |r| r['path']==local+'/DESIGN.md' }['sha256']})
