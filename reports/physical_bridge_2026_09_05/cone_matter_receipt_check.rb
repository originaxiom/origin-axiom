# R74 byte custody/fixed populations, not independent proof or physics review.
require 'json'
require 'digest'
require 'open3'
abort('Usage: ruby cone_matter_receipt_check.rb RAW_DIRECTORY') unless ARGV.size==1
raw=ARGV.fetch(0);base='reports/physical_bridge_2026_09_05/'
need=lambda{|v,m|abort(m) unless v}
d=JSON.parse(File.read(base+'CONE_MATTER_RECEIPTS.json'))
paths=%w[CONE_MATTER_DESIGN.md CONE_MATTER_PROOF.md CONE_MATTER_INPUTS.json cone_matter.py].map{|p|base+p}+['tests/test_physical_bridge_cone_matter.py']
paths.each do |p|
 b,e,st=Open3.capture3('git','show',d.fetch('seal')+':'+p)
 need.call(st.success?,e)
 need.call(b.b==File.binread(p),'frozen science changed '+p)
end
manifest=JSON.parse(File.read(base+'CONE_MATTER_INPUTS.json'))
manifest.fetch('inputs').each do |r|
 b,e,st=Open3.capture3('git','show',r.fetch('commit')+':'+r.fetch('path'))
 need.call(st.success?,e)
 need.call(b.bytesize==r.fetch('bytes') && Digest::SHA256.hexdigest(b)==r.fetch('sha256') && b.b==File.binread(r.fetch('path')),'local input pin changed')
end
manifest.fetch('received_context').each do |r|
 b,e,st=Open3.capture3('git','show',r.fetch('commit')+':'+r.fetch('path'))
 need.call(st.success?,e)
 need.call(b.bytesize==r.fetch('bytes') && Digest::SHA256.hexdigest(b)==r.fetch('sha256'),'received context changed')
end
red=lambda{|v|v.gsub(%r{/Users/[^/]+/\.pyenv/versions/3\.12\.1},'<python3.12-env>').gsub(Dir.pwd,'<repo>').gsub(raw,'<raw>').gsub(%r{/Users/[^/]+/Documents/temp001},'<prior-raw>')}
runs,audits=d.fetch('runs'),d.fetch('audit_runs')
need.call(runs.keys.sort==%w[combined_first native_first],'science capture population changed')
need.call(audits.keys.sort==%w[gates_prebank gates_seal],'published audit population changed')
runs.merge(audits).merge('custody_first'=>d.fetch('metadata_capture')).each do |name,row|
 stem=File.join(raw,row.fetch('raw_basename'));b=File.binread(stem+'.log');r=JSON.parse(File.read(stem+'.json'))
 need.call(Digest::SHA256.file(stem+'.json').hexdigest==row.fetch('raw_receipt_sha256'),'raw receipt changed')
 need.call(b.bytesize==r.fetch('log_bytes') && Digest::SHA256.hexdigest(b)==r.fetch('log_sha256'),'raw log changed')
 r['command']=r.fetch('command').map{|v|red.call(v)}
 need.call(r==row.fetch('receipt') && red.call(b.dup.force_encoding('UTF-8'))==row.fetch('stdout'),'public capture differs '+name)
end
out=JSON.parse(runs.fetch('native_first').fetch('stdout'))
need.call(d.fetch('metadata_capture').fetch('receipt').fetch('exit_code')==1 && d.fetch('metadata_capture').fetch('stdout').include?('frozen science changed'),'first metadata failure lost')
need.call(out.fetch('checks').size==67 && out.fetch('checks').values.all?{|v|v==true} && out.fetch('all_checks_pass'),'control population changed')
expected={'actual'=>10,'coefficient'=>18,'contraction'=>10,'limit'=>10,'products'=>8,'scalar'=>11}
need.call(out.fetch('groups').transform_values{|v|v.fetch('checks').size}==expected,'group population changed')
g=out.fetch('groups')
need.call(g.fetch('coefficient').fetch('coefficient_dimension')==6 && g.fetch('actual').fetch('form_dimension')==48,'actual dimensions changed')
need.call(g.fetch('contraction').fetch('witnessed_quotient_dimension')==24 && g.fetch('contraction').fetch('witnessed_signature')==[12,12] && g.fetch('scalar').fetch('scalar_seed_dimension')==6,'witnessed constants changed')
runs.each{|n,r|need.call(r.fetch('receipt').fetch('exit_code')==0,'scientific capture failed')}
tests=runs.fetch('combined_first').fetch('receipt').fetch('command').grep(/^tests\//)
need.call(tests==%w[tests/test_physical_bridge_cone_fermion.py tests/test_physical_bridge_cone_exact.py tests/test_physical_bridge_cone_matter.py],'focused population changed')
need.call(runs.fetch('combined_first').fetch('stdout').include?('24 passed') && runs.fetch('combined_first').fetch('stdout').lines.grep(/^FAILED |^ERROR /).empty?,'test results changed')
need.call(d.fetch('population')=={'controls'=>67,'focused_passes'=>24,'new_tests'=>8,'focused_test_files'=>3} && d.fetch('first_scientific_failures')==[],'published population changed')
baseline=JSON.parse(File.read(base+'CONE_ORBIT_RECEIPTS.json')).fetch('audit_runs').fetch('gates_precommit').fetch('stdout').lines.grep(/^  FAIL /)
audits.each do |n,r|
 need.call(r.fetch('receipt').fetch('exit_code')==1 && r.fetch('stdout').lines.grep(/^  FAIL /)==baseline && r.fetch('stdout').lines.grep(/^  PASS /).size==26,'historical governance changed')
end
links=File.read(base+'CONE_MATTER.md').scan(/\]\(([^)]+)\)/).flatten.reject{|p|p.start_with?('http://','https://','#')}
links.each{|p|need.call(File.file?(File.expand_path(p.split('#').first,base)),'report link missing')}
puts JSON.generate(frozen_science_paths:paths.size,local_input_pins:manifest.fetch('inputs').size,received_context_pins:manifest.fetch('received_context').size,published_captures:runs.size+audits.size+1,preserved_metadata_failures:1,finite_controls:67,new_tests:8,focused_passes:24,historical_governance_failures:baseline.size,report_links:links.size,scope:'Fixed finite populations and byte custody, not independent analytic acceptance, full-repository certification or physics')
