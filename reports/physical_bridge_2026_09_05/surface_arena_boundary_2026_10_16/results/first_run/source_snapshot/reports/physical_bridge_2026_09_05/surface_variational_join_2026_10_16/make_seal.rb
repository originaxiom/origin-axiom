# Mechanical manifest only; no scientific imports or execution.
require 'json'
require 'digest'
require 'pathname'
root=Pathname.new(__dir__).parent.parent.parent
local=Pathname.new(__dir__).relative_path_from(root).to_s
stage=ARGV.fetch(0,'normal variational join BEFORE execution')
prior='reports/physical_bridge_2026_09_05/surface_interacting_domain_2026_10_15/INPUTS.json'
paths=JSON.parse(File.read(root.join(prior))).fetch('source_files').map{|r|r.fetch('path')}
paths << prior
paths += %w[DESIGN.md PROOF.md SOURCE_CHECK.md analysis.py probe.py reference.py execute.py make_seal.rb validate.rb].map{|p|local+'/'+p}
paths << 'tests/test_physical_bridge_surface_variational_join.py'
repair=local+'/POST_HOC_REPAIR.md'
paths << repair if File.exist?(root.join(repair))
repair2=local+'/SECOND_INSTRUMENT_REPAIR.md'
paths << repair2 if File.exist?(root.join(repair2))
rows=paths.uniq.sort.map{|p|{'path'=>p,'sha256'=>Digest::SHA256.file(root.join(p)).hexdigest}}
data={'scope'=>'Canonical local normal action/end and one-way BPS fermion tangent; not full nonlinear SUSY boundary, literal source-action acceptance, global vacuum or SM',
 'runtime'=>{'python'=>'3.12.14','sympy'=>'1.14.0'},'shared_formulation'=>'Same author, analysis and Sympy; actual/exterior frames, lower/upper E8 root engines',
 'source_files'=>rows}
File.write(root.join(local,'INPUTS.json'),JSON.pretty_generate(data)+"\n")
all=rows+[{'path'=>local+'/INPUTS.json','sha256'=>Digest::SHA256.file(root.join(local,'INPUTS.json')).hexdigest}]
File.write(root.join(local,'ARTIFACT_HASHES.txt'),all.map{|r|r['sha256']+'  '+r['path']}.join("\n")+"\n")
File.open(root.join('docs/SEAL_LEDGER.md'),'a') do |f|
 f.write("\n## Normal variational join: "+stage+"\n\n| date | stage | source | sha256 | scope |\n|---|---|---|---|---|\n")
 all.each{|r|f.write('| 2026-10-16 | '+stage+' | `'+r['path']+'` | `'+r['sha256']+'` | Canonical local normal action/end and interacting tangent; not full physical boundary or SM |'+"\n")}
end
puts JSON.generate({'pins'=>rows.length,'design_sha256'=>rows.find{|r|r['path']==local+'/DESIGN.md'}['sha256']})
