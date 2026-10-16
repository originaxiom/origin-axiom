# Mechanical manifest, no science imports/execution.
require 'json'
require 'digest'
require 'pathname'
root=Pathname.new(__dir__).parent.parent.parent
local=Pathname.new(__dir__).relative_path_from(root).to_s
stage=ARGV.fetch(0,'weighted normal Hessian BEFORE execution')
prior='reports/physical_bridge_2026_09_05/surface_source_operator_2026_10_16/INPUTS.json'
paths=JSON.parse(File.read(root.join(prior))).fetch('source_files').map{|r|r.fetch('path')}+[prior]
paths += %w[DESIGN.md PROOF.md analysis.py probe.py reference.py execute.py make_seal.rb validate.rb].map{|p|local+'/'+p}
paths << 'tests/test_physical_bridge_surface_weighted_hessian.py'
repair=local+'/POST_HOC_REPAIR.md';paths << repair if File.exist?(root.join(repair))
rows=paths.uniq.sort.map{|p|{'path'=>p,'sha256'=>Digest::SHA256.file(root.join(p)).hexdigest}}
data={'scope'=>'Local weighted residual Hessian/completed-source/annulus-end join; supplied action, no full printed identification or nonlinear/global physics',
 'runtime'=>{'python'=>'3.12.14','sympy'=>'1.14.0'},'shared_formulation'=>'Same author/source expansion/Sympy; actual and exterior Fock frames',
 'source_files'=>rows}
File.write(root.join(local,'INPUTS.json'),JSON.pretty_generate(data)+"\n")
all=rows+[{'path'=>local+'/INPUTS.json','sha256'=>Digest::SHA256.file(root.join(local,'INPUTS.json')).hexdigest}]
File.write(root.join(local,'ARTIFACT_HASHES.txt'),all.map{|r|r['sha256']+'  '+r['path']}.join("\n")+"\n")
File.open(root.join('docs/SEAL_LEDGER.md'),'a') do |f|
 f.write("\n## Weighted normal Hessian and completed-source operator: "+stage+"\n\n| date | stage | source | sha256 | scope |\n|---|---|---|---|---|\n")
 all.each{|r|f.write('| 2026-10-16 | '+stage+' | `'+r['path']+'` | `'+r['sha256']+'` | Local weighted normal join, not full printed/global physics |'+"\n")}
end
puts JSON.generate({'pins'=>rows.length,'design_sha256'=>rows.find{|r|r['path']==local+'/DESIGN.md'}['sha256']})
