# BANKED IDENTITY: complete actual geometry/source closure. PRIOR ART: capture seals.
require 'json'
require 'digest'
require 'pathname'
root=Pathname.new(__dir__).parent.parent.parent
local=Pathname.new(__dir__).relative_path_from(root).to_s
inputs=%w[reports/physical_bridge_2026_09_05/surface_same_action_transmission_2026_10_16/INPUTS.json reports/physical_bridge_2026_09_05/surface_geometric_loops_2026_10_14/INPUTS.json]
paths=inputs.flat_map{|p|JSON.parse(File.read(root.join(p))).fetch('source_files').map{|r|r.fetch('path')}}+inputs
paths+=%w[DESIGN.md PROOF.md analysis.py probe.py reference.py execute.py validate.rb make_seal.rb].map{|p|local+'/'+p}
paths+=%w[tests/test_physical_bridge_surface_arena_boundary.py tests/test_physical_bridge_surface_real_twist.py tests/test_physical_bridge_surface_geometric_loops.py]
repair=local+'/POST_HOC_REPAIR.md';paths << repair if File.exist?(root.join(repair))
rows=paths.uniq.sort.map{|p|{'path'=>p,'sha256'=>Digest::SHA256.file(root.join(p)).hexdigest}}
data={'scope'=>'Normal arena/global embedded contact tube and actual source map; not true end dynamics or full physical SM',
 'BANKED IDENTITY:'=>'Both geometric329/32 records and actual source/tensor dictionary freshly replayed.',
 'PRIOR ART:'=>'DESIGN/PROOF credit Hain, Ghys and the actual geometric/source/tube/transmission packets.',
 'runtime'=>{'python'=>'3.12.14','sympy'=>'1.14.0'},
 'shared_formulation'=>'Same author/proof/Sympy; not independent analytic acceptance.', 'source_files'=>rows}
File.write(root.join(local,'INPUTS.json'),JSON.pretty_generate(data)+"\n")
all=rows+[{'path'=>local+'/INPUTS.json','sha256'=>Digest::SHA256.file(root.join(local,'INPUTS.json')).hexdigest}]
File.write(root.join(local,'ARTIFACT_HASHES.txt'),all.map{|r|r['sha256']+'  '+r['path']}.join("\n")+"\n")
stage=ARGV.fetch(0,'BEFORE first scientific import')
File.open(root.join('docs/SEAL_LEDGER.md'),'a') do |f|
 f.write("\n## Surface arena boundary "+stage+"\n\n| date | stage | source | sha256 | scope |\n|---|---|---|---|---|\n")
 all.select{|r|[local+'/DESIGN.md',local+'/INPUTS.json'].include?(r['path'])}.each{|r|f.write('| 2026-10-16 | '+stage+' | `'+r['path']+'` | `'+r['sha256']+'` | Preregistered actual arena/boundary/source map and global tube; not a selected physical end |'+"\n")}
end
puts JSON.generate({'pins'=>rows.length,'design_sha256'=>rows.find{|r|r['path']==local+'/DESIGN.md'}['sha256']})
