# Mechanical hashing only, before scientific imports and probes.
require 'json'
require 'digest'
require 'pathname'
root=Pathname.new(__dir__).parent.parent.parent
local=Pathname.new(__dir__).relative_path_from(root).to_s
prior='reports/physical_bridge_2026_09_05/surface_interacting_transport_2026_10_16/INPUTS.json'
paths=JSON.parse(File.read(root.join(prior))).fetch('source_files').map{|r|r['path']}+[prior]
paths += %w[DESIGN.md PROOF.md analysis.py probe.py reference.py execute.py validate.rb make_seal.rb].map{|p|local+'/'+p}
paths += %w[spinor_uniformization_joint_2026_10_14/PROOF.md spinor_uniformization_joint_2026_10_14/probe.py].map{|p|'reports/physical_bridge_2026_09_05/'+p}
paths << 'tests/test_physical_bridge_surface_root_gauge_sector.py'
repair=local+'/POST_HOC_REPAIR.md';paths << repair if File.exist?(root.join(repair))
rows=paths.uniq.sort.map{|p|{'path'=>p,'sha256'=>Digest::SHA256.file(root.join(p)).hexdigest}}
data={'scope'=>'Complete chosen-root/source radial reduction and local nonlinear retained gauge multiplet, not full charged finite Cauchy response or physical SM',
 'runtime'=>{'python'=>'3.12.14','sympy'=>'1.14.0'},'shared_formulation'=>'Same author/model/conventions/algebra; actual source/lower E8/generator membership versus reconstructed MW/upper E8/projector membership',
 'source_files'=>rows}
File.write(root.join(local,'INPUTS.json'),JSON.pretty_generate(data)+"\n")
all=rows+[{'path'=>local+'/INPUTS.json','sha256'=>Digest::SHA256.file(root.join(local,'INPUTS.json')).hexdigest}]
File.write(root.join(local,'ARTIFACT_HASHES.txt'),all.map{|r|r['sha256']+'  '+r['path']}.join("\n")+"\n")
stage=ARGV.fetch(0,'complete root gauge sector BEFORE first science import')
File.open(root.join('docs/SEAL_LEDGER.md'),'a') do |f|
 f.write("\n## Complete root and retained gauge sector "+stage+"\n\n| date | stage | source | sha256 | scope |\n|---|---|---|---|---|\n")
 all.each{|r|f.write('| 2026-10-16 | '+stage+' | `'+r['path']+'` | `'+r['sha256']+'` | Supplied local root/gauge sector, not full physical SM |'+"\n")}
end
puts JSON.generate({'pins'=>rows.length,'design_sha256'=>rows.find{|r|r['path']==local+'/DESIGN.md'}['sha256']})
