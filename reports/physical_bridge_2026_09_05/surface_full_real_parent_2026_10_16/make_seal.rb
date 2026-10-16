# Mechanical manifest, no science imports/execution.
require 'json'
require 'digest'
require 'pathname'
root=Pathname.new(__dir__).parent.parent.parent
local=Pathname.new(__dir__).relative_path_from(root).to_s
stage=ARGV.fetch(0,'full real K D gaugino parent BEFORE execution')
prior='reports/physical_bridge_2026_09_05/surface_real_superfield_2026_10_16/INPUTS.json'
paths=JSON.parse(File.read(root.join(prior))).fetch('source_files').map{|r|r.fetch('path')}+[prior]
paths += %w[weave_curved_action_2026_10_08/PROOF.md weave_curved_action_2026_10_08/probe.py weave_curved_action_2026_10_08/reference.py silver_superfield_response_2026_10_10/PROOF.md silver_superfield_response_2026_10_10/probe.py silver_superfield_covariance_2026_10_11/PROOF.md silver_superfield_covariance_2026_10_11/reference.py CONE_MULTIPLET_PROOF.md CONE_CHANNEL_PROOF.md silver_fermion_action_2026_10_11/PROOF.md silver_fermion_action_2026_10_11/probe.py silver_fermion_action_2026_10_11/reference.py].map{|p|'reports/physical_bridge_2026_09_05/'+p}
paths += %w[DESIGN.md PROOF.md analysis.py superfield.py probe.py reference.py execute.py make_seal.rb validate.rb].map{|p|local+'/'+p}
paths << 'tests/test_physical_bridge_surface_full_real_parent.py'
repair=local+'/POST_HOC_REPAIR.md';paths << repair if File.exist?(root.join(repair))
repair_trace=local+'/TRACE_NORMALIZATION_REPAIR.md';paths << repair_trace if File.exist?(root.join(repair_trace))
%w[CLIFFORD_DIAGNOSTIC_DESIGN.md clifford_diagnostic.py results/gauge_frame_run/probe.stdout.log].each{|p|paths << local+'/'+p if File.exist?(root.join(local,p))}
rows=paths.uniq.sort.map{|p|{'path'=>p,'sha256'=>Digest::SHA256.file(root.join(p)).hexdigest}}
data={'scope'=>'Full supplied local K D gaugino and physical operator gate; not printed BHV, singular/global or SM selection',
 'runtime'=>{'python'=>'3.12.14','sympy'=>'1.14.0'},'shared_formulation'=>'Same author/primary and graded algebra/Sympy; full superfield versus ordered components, actual/exterior frames',
 'source_files'=>rows}
File.write(root.join(local,'INPUTS.json'),JSON.pretty_generate(data)+"\n")
all=rows+[{'path'=>local+'/INPUTS.json','sha256'=>Digest::SHA256.file(root.join(local,'INPUTS.json')).hexdigest}]
File.write(root.join(local,'ARTIFACT_HASHES.txt'),all.map{|r|r['sha256']+'  '+r['path']}.join("\n")+"\n")
File.open(root.join('docs/SEAL_LEDGER.md'),'a') do |f|
 f.write("\n## Full real local parent and actual operator dictionary: "+stage+"\n\n| date | stage | source | sha256 | scope |\n|---|---|---|---|---|\n")
 all.each{|r|f.write('| 2026-10-16 | '+stage+' | `'+r['path']+'` | `'+r['sha256']+'` | Supplied full local action/operator gate, not complete physical model |'+"\n")}
end
puts JSON.generate({'pins'=>rows.length,'design_sha256'=>rows.find{|r|r['path']==local+'/DESIGN.md'}['sha256']})
