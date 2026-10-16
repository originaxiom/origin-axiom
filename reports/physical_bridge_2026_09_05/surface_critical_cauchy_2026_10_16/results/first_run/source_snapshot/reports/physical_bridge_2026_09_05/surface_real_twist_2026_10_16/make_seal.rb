# Mechanical source manifest only, no science import or execution.
require 'json'
require 'digest'
require 'pathname'
root=Pathname.new(__dir__).parent.parent.parent
local=Pathname.new(__dir__).relative_path_from(root).to_s
prior='reports/physical_bridge_2026_09_05/surface_full_real_parent_2026_10_16/INPUTS.json'
paths=JSON.parse(File.read(root.join(prior))).fetch('source_files').map{|r|r.fetch('path')}+[prior]
paths += %w[surface_parent_dictionary_2026_10_13/upstream_total_metric.py surface_parent_dictionary_2026_10_13/probe.py surface_parent_dictionary_2026_10_13/PROOF.md surface_global_spin_2026_10_13/PROOF.md surface_global_spin_2026_10_13/probe.py surface_global_spin_2026_10_13/reference.py surface_mode_transport_2026_10_15/PROOF.md].map{|p|'reports/physical_bridge_2026_09_05/'+p}
paths += %w[DESIGN.md PROOF.md analysis.py probe.py reference.py execute.py validate.rb make_seal.rb].map{|p|local+'/'+p}
paths << 'tests/test_physical_bridge_surface_real_twist.py'
repair=local+'/POST_HOC_REPAIR.md';paths << repair if File.exist?(root.join(repair))
rows=paths.uniq.sort.map{|p|{'path'=>p,'sha256'=>Digest::SHA256.file(root.join(p)).hexdigest}}
data={'scope'=>'Actual supplied real-action scalar charge and opposite MW curved connection/chart/cutoff gate; not physical SM/three/gravity',
 'runtime'=>{'python'=>'3.12.14','sympy'=>'1.14.0'},
 'shared_formulation'=>'Same author/frozen action data/math conventions/Sympy; coordinate versus closed-coframe geometry',
 'source_files'=>rows}
File.write(root.join(local,'INPUTS.json'),JSON.pretty_generate(data)+"\n")
all=rows+[{'path'=>local+'/INPUTS.json','sha256'=>Digest::SHA256.file(root.join(local,'INPUTS.json')).hexdigest}]
File.write(root.join(local,'ARTIFACT_HASHES.txt'),all.map{|r|r['sha256']+'  '+r['path']}.join("\n")+"\n")
stage=ARGV.fetch(0,'actual charge and opposite MW full curved map BEFORE science execution')
File.open(root.join('docs/SEAL_LEDGER.md'),'a') do |f|
 f.write("\n## Actual real action spin twist connection "+stage+"\n\n| date | stage | source | sha256 | scope |\n|---|---|---|---|---|\n")
 all.each{|r|f.write('| 2026-10-16 | '+stage+' | `'+r['path']+'` | `'+r['sha256']+'` | Supplied actual fermion bundle map, not singular domain or physical SM |'+"\n")}
end
puts JSON.generate({'pins'=>rows.length,'design_sha256'=>rows.find{|r|r['path']==local+'/DESIGN.md'}['sha256']})
