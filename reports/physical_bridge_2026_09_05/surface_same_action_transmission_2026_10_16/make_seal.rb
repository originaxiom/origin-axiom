# BANKED IDENTITY: transitive actual source closure. PRIOR ART: all-boson seal.
require 'json'
require 'digest'
require 'pathname'
root=Pathname.new(__dir__).parent.parent.parent
local=Pathname.new(__dir__).relative_path_from(root).to_s
prior='reports/physical_bridge_2026_09_05/surface_all_boson_response_2026_10_16/INPUTS.json'
paths=JSON.parse(File.read(root.join(prior))).fetch('source_files').map{|r|r.fetch('path')}+[prior]
paths+=%w[DESIGN.md PROOF.md analysis.py probe.py reference.py execute.py validate.rb make_seal.rb].map{|p|local+'/'+p}
paths << 'reports/physical_bridge_2026_09_05/surface_all_boson_response_2026_10_16/execute.py'
paths << 'reports/physical_bridge_2026_09_05/surface_interacting_transport_2026_10_16/validate.rb'
paths << 'tests/test_physical_bridge_surface_same_action_transmission.py'
paths << 'tests/test_physical_bridge_surface_root_gauge_sector.py'
repair=local+'/POST_HOC_REPAIR.md';paths << repair if File.exist?(root.join(repair))
rows=paths.uniq.sort.map{|p|{'path'=>p,'sha256'=>Digest::SHA256.file(root.join(p)).hexdigest}}
data={'scope'=>'Same source two-sided smooth interface; not true physical end selection, global stationary Higgs or full SM',
 'BANKED IDENTITY:'=>'Actual full80 root controls and generic source action checks freshly replayed in both methods.',
 'PRIOR ART:'=>'DESIGN/PROOF credit R30/R89, all-boson/angular/Gauss/root packets and Bar--Ballmann transmission.',
 'runtime'=>{'python'=>'3.12.14','sympy'=>'1.14.0'},
 'shared_formulation'=>'Same author, proof and Sympy; not independent analytic acceptance.', 'source_files'=>rows}
File.write(root.join(local,'INPUTS.json'),JSON.pretty_generate(data)+"\n")
all=rows+[{'path'=>local+'/INPUTS.json','sha256'=>Digest::SHA256.file(root.join(local,'INPUTS.json')).hexdigest}]
File.write(root.join(local,'ARTIFACT_HASHES.txt'),all.map{|r|r['sha256']+'  '+r['path']}.join("\n")+"\n")
stage=ARGV.fetch(0,'BEFORE first scientific import')
File.open(root.join('docs/SEAL_LEDGER.md'),'a') do |f|
 f.write("\n## Same-action transmission "+stage+"\n\n| date | stage | source | sha256 | scope |\n|---|---|---|---|---|\n")
 all.select{|r|[local+'/DESIGN.md',local+'/INPUTS.json'].include?(r['path'])}.each{|r|f.write('| 2026-10-16 | '+stage+' | `'+r['path']+'` | `'+r['sha256']+'` | Actual same-action interface, not a selected true boundary or spectrum |'+"\n")}
end
puts JSON.generate({'pins'=>rows.length,'design_sha256'=>rows.find{|r|r['path']==local+'/DESIGN.md'}['sha256']})
