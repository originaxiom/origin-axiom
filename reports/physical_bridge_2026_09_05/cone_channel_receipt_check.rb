# R71 byte custody and fixed finite controls; not independent analytic acceptance.
require 'json'
require 'digest'
require 'open3'
abort('Usage: ruby cone_channel_receipt_check.rb RAW_DIRECTORY') unless ARGV.size==1
raw=ARGV.fetch(0)
base='reports/physical_bridge_2026_09_05/'
d=JSON.parse(File.read(base+'CONE_CHANNEL_RECEIPTS.json'))
need=lambda { |v,m| abort(m) unless v }
original=%w[CONE_CHANNEL_DESIGN.md CONE_CHANNEL_PROOF.md CONE_CHANNEL_INPUTS.json cone_channel.py].map { |p| base+p }+['tests/test_physical_bridge_cone_channel.py']
control=%w[CONE_CHANNEL_CONTROL_DESIGN.md cone_channel_control.py].map { |p| base+p }+['tests/test_physical_bridge_cone_channel_control.py']
[[d.fetch('seal'),original],[d.fetch('control_seal'),control]].each do |seal,paths|
 paths.each do |p|
  b,e,s=Open3.capture3('git','show',seal+':'+p)
  need.call(s.success?,e)
  need.call(Digest::SHA256.hexdigest(b)==Digest::SHA256.file(p).hexdigest,'science changed '+p)
 end
end
pins=JSON.parse(File.read(base+'CONE_CHANNEL_INPUTS.json')).fetch('inputs')
pins.each do |r|
 b,e,s=Open3.capture3('git','show',r.fetch('commit')+':'+r.fetch('path'))
 need.call(s.success?,e)
 need.call(b.bytesize==r.fetch('bytes') && Digest::SHA256.hexdigest(b)==r.fetch('sha256') && Digest::SHA256.file(r.fetch('path')).hexdigest==r.fetch('sha256'),'prior pin changed')
end
red=lambda { |v| v.gsub(%r{/Users/[^/]+/\.pyenv/versions/3\.12\.1},'<python3.12-env>').gsub(Dir.pwd,'<repo>').gsub(raw,'<raw>').gsub(%r{/Users/[^/]+/Documents/temp001},'<prior-raw>') }
runs,audits=d.fetch('runs'),d.fetch('audit_runs')
need.call(runs.keys.sort==%w[combined_control combined_first native_control native_first],'science run population changed')
need.call(audits.keys.sort==%w[cumulative_precommit cumulative_refreshed gates_control gates_precommit gates_repaired gates_seal],'audit population changed')
runs.merge(audits).each do |name,row|
 stem=File.join(raw,row.fetch('raw_basename')); b=File.binread(stem+'.log'); r=JSON.parse(File.read(stem+'.json'))
 need.call(Digest::SHA256.file(stem+'.json').hexdigest==row.fetch('raw_receipt_sha256'),'receipt changed')
 need.call(Digest::SHA256.hexdigest(b)==r.fetch('log_sha256') && b.bytesize==r.fetch('log_bytes'),'raw log changed')
 r['command']=r.fetch('command').map { |v| red.call(v) }
 need.call(r==row.fetch('receipt') && red.call(b.dup.force_encoding('UTF-8'))==row.fetch('stdout'),'capture mismatch '+name)
end
first=JSON.parse(runs.fetch('native_first').fetch('stdout'))
final=JSON.parse(runs.fetch('native_control').fetch('stdout'))
need.call(first.fetch('checks').size==56 && first.fetch('checks').select { |k,v| !v }.keys==['scalar/independent_scalar_charpoly'] && !first.fetch('all_checks_pass'),'first failure changed')
need.call(final.fetch('checks').size==60 && final.fetch('checks').values.all? { |v| v==true } && final.fetch('all_checks_pass'),'final controls changed')
need.call(final.fetch('groups').fetch('window').fetch('limiting_angular_dimensions')==[36,60,300],'limiting fixture population changed')
expected_first=%w[tests/test_physical_bridge_cone_fermion.py tests/test_physical_bridge_cone_multiplet.py tests/test_physical_bridge_cone_channel.py]
expected_final=expected_first[0,2]+['tests/test_physical_bridge_cone_channel_control.py']
need.call(runs.fetch('combined_first').fetch('receipt').fetch('command').grep(/^tests\//)==expected_first,'first tests changed')
need.call(runs.fetch('combined_control').fetch('receipt').fetch('command').grep(/^tests\//)==expected_final,'control tests changed')
fails=runs.fetch('combined_first').fetch('stdout').lines.grep(/^FAILED /).map { |l| l.split[1] }
need.call(fails==d.fetch('retained_first_failures') && runs.fetch('combined_first').fetch('stdout').include?('2 failed, 21 passed'),'first test failures changed')
need.call(runs.fetch('combined_control').fetch('stdout').include?('23 passed') && runs.fetch('combined_control').fetch('stdout').lines.grep(/^FAILED |^ERROR /).empty?,'control tests changed')
runs.each { |n,r| need.call(r.fetch('receipt').fetch('exit_code')==(n.end_with?('first') ? 1 : 0),'science exit changed') }
baseline=JSON.parse(File.read(base+'CONE_MULTIPLET_RECEIPTS.json')).fetch('audit_runs').fetch('gates_precommit').fetch('stdout').lines.grep(/^  FAIL /)
audits.each do |n,r|
 if n=='gates_precommit'
  expected=baseline+["  FAIL  law-map-provenance: LAW_MAP provenance -- 4 row(s) cite no arc: scoped sublemma; Every open-critical limiting Fourier tup; The zero-Fourier neutral formal critical\n"]
  need.call(r.fetch('receipt').fetch('exit_code')==1 && r.fetch('stdout').lines.grep(/^  FAIL /)==expected && r.fetch('stdout').lines.grep(/^  PASS /).size==25,'first provenance-format failure changed')
 elsif n.start_with?('gates_')
  need.call(r.fetch('receipt').fetch('exit_code')==1 && r.fetch('stdout').lines.grep(/^  FAIL /)==baseline && r.fetch('stdout').lines.grep(/^  PASS /).size==26,'historical governance changed')
 elsif n=='cumulative_precommit'
  need.call(r.fetch('receipt').fetch('exit_code')==1 && r.fetch('stdout')=="Artifact differs: reports/physical_bridge_2026_09_05/GOAL_VERDICT.md\n",'first metadata custody mismatch changed')
 else
  need.call(r.fetch('receipt').fetch('exit_code')==0,'cumulative custody failed')
 end
end
links=File.read(base+'CONE_CHANNEL.md').scan(/\]\(([^)]+)\)/).flatten.reject { |p| p.start_with?('http://','https://','#') }
links.each { |p| need.call(File.file?(File.expand_path(p.split('#').first,base)),'report link missing') }
puts JSON.generate(frozen_science_paths:original.size+control.size,input_pins:pins.size,published_captures:runs.size+audits.size,final_exact_controls:60,new_control_tests:7,focused_passes:23,retained_original_failures:fails.size,historical_governance_failures:baseline.size,report_links:links.size,scope:'Byte custody, not exact graph domains or independent physical review')
