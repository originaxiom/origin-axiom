# R73 byte custody and finite population check, not independent analytic acceptance.
require 'json'
require 'digest'
require 'open3'
abort('Usage: ruby cone_orbit_receipt_check.rb RAW_DIRECTORY') unless ARGV.size==1
raw=ARGV.fetch(0); base='reports/physical_bridge_2026_09_05/'
need=lambda { |v,m| abort(m) unless v }
d=JSON.parse(File.read(base+'CONE_ORBIT_RECEIPTS.json'))
science=%w[CONE_ORBIT_DESIGN.md CONE_ORBIT_PROOF.md CONE_ORBIT_INPUTS.json cone_orbit.py].map { |p| base+p }+['tests/test_physical_bridge_cone_orbit.py']
repair=%w[CONE_ORBIT_CONTROL_DESIGN.md cone_orbit_control.py].map { |p| base+p }+['tests/test_physical_bridge_cone_orbit_control.py']
[[d.fetch('seal'),science],[d.fetch('repair_seal'),repair]].each do |h,paths|
 paths.each do |p|
  b,e,st=Open3.capture3('git','show',h+':'+p)
  need.call(st.success?,e)
  need.call(Digest::SHA256.hexdigest(b)==Digest::SHA256.file(p).hexdigest,'frozen science changed '+p)
 end
end
pins=JSON.parse(File.read(base+'CONE_ORBIT_INPUTS.json')).fetch('inputs')
pins.each do |r|
 b,e,st=Open3.capture3('git','show',r.fetch('commit')+':'+r.fetch('path'))
 need.call(st.success?,e)
 need.call(b.bytesize==r.fetch('bytes') && Digest::SHA256.hexdigest(b)==r.fetch('sha256') && Digest::SHA256.file(r.fetch('path')).hexdigest==r.fetch('sha256'),'prior input pin changed')
end
red=lambda { |v| v.gsub(%r{/Users/[^/]+/\.pyenv/versions/3\.12\.1},'<python3.12-env>').gsub(Dir.pwd,'<repo>').gsub(raw,'<raw>').gsub(%r{/Users/[^/]+/Documents/temp001},'<prior-raw>') }
runs,audits=d.fetch('runs'),d.fetch('audit_runs')
need.call(runs.keys.sort==%w[combined_first native_first repair_combined repair_native],'scientific population changed')
need.call(audits.keys.sort==%w[cumulative_precommit cumulative_repaired gates_precommit gates_seal],'audit population changed')
runs.merge(audits).each do |n,row|
 p=File.join(raw,row.fetch('raw_basename')); bytes=File.binread(p+'.log'); rec=JSON.parse(File.read(p+'.json'))
 need.call(Digest::SHA256.file(p+'.json').hexdigest==row.fetch('raw_receipt_sha256'),'raw receipt changed')
 need.call(Digest::SHA256.hexdigest(bytes)==rec.fetch('log_sha256') && bytes.bytesize==rec.fetch('log_bytes'),'raw log changed')
 rec['command']=rec.fetch('command').map { |v| red.call(v) }
 need.call(rec==row.fetch('receipt') && red.call(bytes.dup.force_encoding('UTF-8'))==row.fetch('stdout'),'capture mismatch '+n)
end
first=JSON.parse(runs.fetch('native_first').fetch('stdout'))
final=JSON.parse(runs.fetch('repair_native').fetch('stdout'))
need.call(first.fetch('checks').size==59 && first.fetch('checks').select { |k,v| v!=true }.keys.sort==%w[operator/exact_Z_trace_unchanged tangent/orbit_difference_L4_leading_positive] && first.fetch('all_checks_pass')==false,'original failure population changed')
need.call(final.fetch('checks').size==66 && final.fetch('checks').values.all? { |v| v==true } && final.fetch('all_checks_pass'),'final controls changed')
need.call(final.fetch('groups').keys.sort==%w[compensator covariance operator orbit tangent],'group population changed')
need.call(final.fetch('groups').fetch('operator').fetch('form_dimension')==72,'actual operator dimension changed')
need.call(runs.fetch('native_first').fetch('receipt').fetch('exit_code')==1 && runs.fetch('combined_first').fetch('receipt').fetch('exit_code')==1,'first failures erased')
need.call(runs.fetch('combined_first').fetch('stdout').include?('3 failed, 19 passed'),'first focused result changed')
%w[repair_native repair_combined].each { |n| need.call(runs.fetch(n).fetch('receipt').fetch('exit_code')==0,'separate controls failed') }
tests=runs.fetch('repair_combined').fetch('receipt').fetch('command').grep(/^tests\//)
need.call(tests==%w[tests/test_physical_bridge_cone_multiplet.py tests/test_physical_bridge_cone_exact.py tests/test_physical_bridge_cone_orbit_control.py],'focused test population changed')
need.call(runs.fetch('repair_combined').fetch('stdout').include?('22 passed') && runs.fetch('repair_combined').fetch('stdout').lines.grep(/^FAILED |^ERROR /).empty?,'final focused result changed')
baseline=JSON.parse(File.read(base+'CONE_EXACT_RECEIPTS.json')).fetch('audit_runs').fetch('gates_precommit').fetch('stdout').lines.grep(/^  FAIL /)
audits.each do |n,row|
 if n.start_with?('gates_')
  need.call(row.fetch('receipt').fetch('exit_code')==1 && row.fetch('stdout').lines.grep(/^  FAIL /)==baseline && row.fetch('stdout').lines.grep(/^  PASS /).size==26,'historical governance population changed')
 elsif n=='cumulative_precommit'
  need.call(row.fetch('receipt').fetch('exit_code')==1 && row.fetch('stdout')=="Artifact differs: docs/SEAL_LEDGER.md\n",'original metadata failure changed')
 else
  need.call(row.fetch('receipt').fetch('exit_code')==0,'cumulative custody failed')
 end
end
links=File.read(base+'CONE_ORBIT.md').scan(/\]\(([^)]+)\)/).flatten.reject { |p| p.start_with?('https://','http://','#') }
links.each { |p| need.call(File.file?(File.expand_path(p.split('#').first,base)),'report link missing') }
puts JSON.generate(frozen_science_paths:science.size,repair_science_paths:repair.size,input_pins:pins.size,published_captures:runs.size+audits.size,final_controls:66,original_failed_controls:2,original_failed_tests:3,new_tests:6,focused_passes:22,historical_governance_failures:baseline.size,report_links:links.size,scope:'Byte custody and fixed finite populations, not independent analytic acceptance or physics')
