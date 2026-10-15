# Mechanical manifest only; no science import, compilation or producer execution.
require 'json'
require 'digest'
require 'pathname'
root=Pathname.new(__dir__).parent.parent.parent
local=Pathname.new(__dir__).relative_path_from(root).to_s
stage=ARGV.fetch(0,'interacting fibre BEFORE execution')
prior='reports/physical_bridge_2026_09_05/surface_real_boundary_2026_10_15/INPUTS.json'
paths=JSON.parse(File.read(root.join(prior))).fetch('source_files').map{|r|r.fetch('path')}
paths << prior
paths += %w[DESIGN.md PROOF.md analysis.py probe.py reference.py execute.py make_seal.rb].map{|p|local+'/'+p}
paths << 'tests/test_physical_bridge_surface_interacting_domain.py'
repair=local+'/POST_HOC_REPAIR.md'
paths << repair if File.exist?(root.join(repair))
rows=paths.uniq.sort.map{|p|{'path'=>p,'sha256'=>Digest::SHA256.file(root.join(p)).hexdigest}}
data={'scope'=>'Authored fixed-fibre interacting domain argument and local nonabelian/action controls; not full surface or physical spectrum',
 'runtime'=>{'python'=>'3.12.14','sympy'=>'1.14.0'},
 'shared_formulation'=>'analysis and author; actual/exterior frame and lower/upper root implementation diversity, not nonauthor analytic acceptance',
 'source_files'=>rows}
File.write(root.join(local,'INPUTS.json'),JSON.pretty_generate(data)+"\n")
all=rows+[{'path'=>local+'/INPUTS.json','sha256'=>Digest::SHA256.file(root.join(local,'INPUTS.json')).hexdigest}]
File.write(root.join(local,'ARTIFACT_HASHES.txt'),all.map{|r|r['sha256']+'  '+r['path']}.join("\n")+"\n")
File.open(root.join('docs/SEAL_LEDGER.md'),'a') do |f|
 f.write("\n## Interacting finite-fibre domain and local end controls: "+stage+"\n\n| date | stage | source | sha256 | scope |\n|---|---|---|---|---|\n")
 all.each{|r|f.write('| 2026-10-15 | '+stage+' | `'+r['path']+'` | `'+r['sha256']+'` | Fixed-fibre interacting domain/local backreaction and end controls; not full global physical boundary law/index |'+"\n")}
end
puts JSON.generate({'pins'=>rows.length,'design_sha256'=>rows.find{|r|r['path']==local+'/DESIGN.md'}['sha256']})
