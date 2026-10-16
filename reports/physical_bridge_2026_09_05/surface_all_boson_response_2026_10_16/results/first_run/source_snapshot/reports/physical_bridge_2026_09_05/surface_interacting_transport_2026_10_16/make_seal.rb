# Mechanical manifest only; publish before mathematical imports/execution.
require 'json'
require 'digest'
require 'pathname'
root=Pathname.new(__dir__).parent.parent.parent
local=Pathname.new(__dir__).relative_path_from(root).to_s
priors=%w[surface_inner_cauchy_2026_10_16 surface_interacting_domain_2026_10_15].map{|p|'reports/physical_bridge_2026_09_05/'+p+'/INPUTS.json'}
paths=priors.flat_map{|p|JSON.parse(File.read(root.join(p))).fetch('source_files').map{|r|r['path']}+[p]}
paths += %w[DESIGN.md PROOF.md analysis.py probe.py reference.py execute.py validate.rb make_seal.rb].map{|p|local+'/'+p}
paths += %w[surface_variational_join_2026_10_16/PROOF.md surface_curved_boson_2026_10_16/PROOF.md].map{|p|'reports/physical_bridge_2026_09_05/'+p}
paths << 'tests/test_physical_bridge_surface_interacting_transport.py'
repair=local+'/POST_HOC_REPAIR.md';paths << repair if File.exist?(root.join(repair))
rows=paths.uniq.sort.map{|p|{'path'=>p,'sha256'=>Digest::SHA256.file(root.join(p)).hexdigest}}
data={'scope'=>'Actual source complementary MW interacting normal operator, E8 nonnormal root, coupled angular system and conditional dressed-domain/tangent join; not full physical boundary theory',
 'runtime'=>{'python'=>'3.12.14','sympy'=>'1.14.0'},'shared_formulation'=>'Same author/model/conventions/algebra; actual source/lower E8 versus reconstructed MW/exterior Fock/aligned upper E8',
 'source_files'=>rows}
File.write(root.join(local,'INPUTS.json'),JSON.pretty_generate(data)+"\n")
all=rows+[{'path'=>local+'/INPUTS.json','sha256'=>Digest::SHA256.file(root.join(local,'INPUTS.json')).hexdigest}]
File.write(root.join(local,'ARTIFACT_HASHES.txt'),all.map{|r|r['sha256']+'  '+r['path']}.join("\n")+"\n")
stage=ARGV.fetch(0,'actual interacting source BEFORE first science import')
File.open(root.join('docs/SEAL_LEDGER.md'),'a') do |f|
 f.write("\n## Actual interacting normal transport "+stage+"\n\n| date | stage | source | sha256 | scope |\n|---|---|---|---|---|\n")
 all.each{|r|f.write('| 2026-10-16 | '+stage+' | `'+r['path']+'` | `'+r['sha256']+'` | Supplied interacting normal source, not full physical SM |'+"\n")}
end
puts JSON.generate({'pins'=>rows.length,'design_sha256'=>rows.find{|r|r['path']==local+'/DESIGN.md'}['sha256']})
