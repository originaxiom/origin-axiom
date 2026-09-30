# R64 read-only byte custody and recorded populations, not independent proof review.
require 'json'
require 'digest'
require 'open3'
abort('Usage: ruby cone_gauge_receipt_check.rb RAW_DIRECTORY') unless ARGV.size==1
base='reports/physical_bridge_2026_09_05/'
raw=ARGV.fetch(0)
need=lambda { |ok,msg| abort(msg) unless ok }
seals={'original'=>'a99477919b97d924bdd9d5d476bb66aaf83f37aa','control'=>'fde9a76988ec164e97c20e59ba232b2fbb3fd636'}
original=%w[CONE_GAUGE_DESIGN.md CONE_GAUGE_PROOF.md CONE_GAUGE_INPUTS.json cone_gauge.py].map { |p| base+p }+['tests/test_physical_bridge_cone_gauge.py']
control=%w[CONE_GAUGE_CONTROL_DESIGN.md cone_gauge_control.py].map { |p| base+p }+['tests/test_physical_bridge_cone_gauge_control.py']
[[seals.fetch('original'),original],[seals.fetch('control'),control]].each do |seal,paths|
  paths.each do |path|
    bytes,err,status=Open3.capture3('git','show',seal+':'+path)
    need.call(status.success?,err)
    need.call(Digest::SHA256.hexdigest(bytes)==Digest::SHA256.file(path).hexdigest,'sealed path changed: '+path)
  end
end
inputs=JSON.parse(File.read(base+'CONE_GAUGE_INPUTS.json')).fetch('inputs')
inputs.each do |row|
  bytes,err,status=Open3.capture3('git','show',row.fetch('commit')+':'+row.fetch('path'))
  need.call(status.success?,err)
  need.call(Digest::SHA256.hexdigest(bytes)==row.fetch('sha256'),'commit pin differs')
  need.call(Digest::SHA256.file(row.fetch('path')).hexdigest==row.fetch('sha256'),'current input differs')
end
red=lambda { |v| v.gsub(%r{/Users/[^/]+/\.pyenv/versions/3\.12\.1},'<python3.12-env>').gsub(Dir.pwd,'<repo>').gsub(raw,'<raw>').gsub(%r{/Users/[^/]+/Documents/temp001},'<prior-raw>') }
data=JSON.parse(File.read(base+'CONE_GAUGE_RECEIPTS.json'))
need.call(data.fetch('seals')==seals,'seals differ')
runs,audits=data.fetch('runs'),data.fetch('audit_runs')
runs.merge(audits).each do |name,row|
  stem=File.join(raw,row.fetch('raw_basename'))
  bytes=File.binread(stem+'.log')
  receipt=JSON.parse(File.read(stem+'.json'))
  need.call(Digest::SHA256.file(stem+'.json').hexdigest==row.fetch('raw_receipt_sha256'),'raw receipt changed: '+name)
  need.call(Digest::SHA256.hexdigest(bytes)==receipt.fetch('log_sha256') && bytes.bytesize==receipt.fetch('log_bytes'),'raw log changed: '+name)
  receipt['command']=receipt.fetch('command').map { |s| red.call(s) }
  need.call(receipt==row.fetch('receipt'),'public receipt differs: '+name)
  need.call(red.call(bytes.dup.force_encoding('UTF-8'))==row.fetch('stdout'),'public output differs: '+name)
end
exits={'native_first'=>1,'focused_first'=>1,'combined_first'=>1,'control_native'=>0,'control_tests'=>0,'combined_repaired'=>1}
need.call(runs.keys.sort==exits.keys.sort,'scientific population differs')
exits.each { |n,c| need.call(runs.fetch(n).fetch('receipt').fetch('exit_code')==c,'unexpected scientific exit: '+n) }
first=JSON.parse(runs.fetch('native_first').fetch('stdout'))
fixed=JSON.parse(runs.fetch('control_native').fetch('stdout'))
need.call(first.fetch('checks').size==95 && first.fetch('checks').select { |k,v| v!=true }.keys==['volterra_kernel_positive_control'] && !first.fetch('all_checks_pass'),'original outcome differs')
need.call(fixed.fetch('original_checks')==first.fetch('checks') && !fixed.fetch('original_all_checks_pass'),'original failure hidden')
need.call(fixed.fetch('effective_checks').size==99 && fixed.fetch('effective_checks').values.all? { |v| v==true } && fixed.fetch('all_effective_checks_pass'),'effective outcome differs')
first.fetch('checks').each { |k,v| need.call(fixed.fetch('effective_checks').fetch(k)==v,'undeclared replacement') unless k=='volterra_kernel_positive_control' }
need.call(fixed.fetch('repair').fetch('checks').size==5 && fixed.fetch('repair').fetch('checks').values.all? { |v| v==true },'repair safeguards differ')
need.call(fixed.fetch('repair').fetch('original_sign_inference').nil?,'unknown sign erased')
ids=lambda { |v| v.lines.select { |l| l.start_with?('FAILED ') }.map(&:strip).sort }
own=%w[test_volterra_inverse_cubic_and_strict_contraction test_all_groups_and_invalid_link_scope].map { |t| 'FAILED tests/test_physical_bridge_cone_gauge.py::'+t }.sort
old_data=JSON.parse(File.read(base+'CONE_SPECTRUM_RECEIPTS.json'))
older=ids.call(old_data.fetch('runs').fetch('combined_first').fetch('stdout'))
need.call(older.size==2,'older failure population differs')
combined=(own+older).sort
need.call(ids.call(runs.fetch('focused_first').fetch('stdout'))==own,'dedicated failed IDs differ')
%w[combined_first combined_repaired].each { |n| need.call(ids.call(runs.fetch(n).fetch('stdout'))==combined,'combined failed IDs differ') }
counts={'focused_first'=>'2 failed, 7 passed','combined_first'=>'4 failed, 37 passed','control_tests'=>'3 passed','combined_repaired'=>'4 failed, 40 passed'}
counts.each { |n,v| need.call(runs.fetch(n).fetch('stdout').include?(v),'test count differs: '+n) }
population=lambda { |row| row.fetch('receipt').fetch('command').select { |v| v.start_with?('tests/') } }
prior=population.call(old_data.fetch('runs').fetch('combined_first'))
need.call(population.call(runs.fetch('combined_first'))==prior+['tests/test_physical_bridge_cone_gauge.py'],'original combined population differs')
need.call(population.call(runs.fetch('combined_repaired'))==prior+%w[tests/test_physical_bridge_cone_gauge.py tests/test_physical_bridge_cone_gauge_control.py],'repaired combined population differs')
fail_rows=old_data.fetch('audit_runs').fetch('gates_precommit').fetch('stdout').lines.select { |l| l.start_with?('  FAIL ') }
audits.each do |n,row|
  if n.start_with?('gates_')
    need.call(row.fetch('receipt').fetch('exit_code')==1 && row.fetch('stdout').lines.select { |l| l.start_with?('  FAIL ') }==fail_rows,'governance failure population changed')
  else
    need.call(row.fetch('receipt').fetch('exit_code')==0,'diagnostic or custody failure')
  end
end
diagnostic=JSON.parse(audits.fetch('sign_diagnostic').fetch('stdout'))
need.call(diagnostic.fetch('raw_is_positive').nil? && diagnostic.fetch('clean_is_positive').nil? && diagnostic.fetch('derivative_is_positive')==true,'diagnostic differs')
report_links=File.read(base+'CONE_GAUGE.md').scan(/\]\(([^)]+)\)/).flatten.reject { |v| v.start_with?('https://','http://','#') }
report_links.each { |p| need.call(File.file?(File.expand_path(p.split('#').first,base)),'new report link missing: '+p) }
puts JSON.generate(frozen_science_paths:original.size+control.size,input_pins:inputs.size,raw_captures:runs.size+audits.size,original_checks_passed:94,original_checks_total:95,effective_checks:99,combined_passes:40,retained_failed_ids:combined.size,new_report_links:report_links.size,
                   scope:'Byte custody and recorded populations; not independent analytic review, full suite or physical completion')
