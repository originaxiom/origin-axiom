# Read-only R63 custody; not independent analytic or physical verification.
require 'json'
require 'digest'
require 'open3'
abort('Usage: ruby cone_spectrum_receipt_check.rb RAW_DIRECTORY') unless ARGV.size==1
base='reports/physical_bridge_2026_09_05/'
raw=ARGV.fetch(0)
need=lambda { |ok,msg| abort(msg) unless ok }
original_seal='a7b9167149cb69db12411fd99a76016921dc47e3'
control_seal='6933cee152caef2f4a7cc79ef6b5b1a452f0cdc3'
original=%w[CONE_SPECTRUM_DESIGN.md CONE_SPECTRUM_INPUTS.json cone_spectrum.py].map { |p| base+p }+['tests/test_physical_bridge_cone_spectrum.py']
control=%w[CONE_SPECTRUM_CONTROL_DESIGN.md cone_spectrum_control.py].map { |p| base+p }+['tests/test_physical_bridge_cone_spectrum_control.py']
[[original_seal,original],[control_seal,control]].each do |seal,paths|
  paths.each do |path|
    bytes,err,status=Open3.capture3('git','show',seal+':'+path)
    need.call(status.success?,err)
    need.call(Digest::SHA256.hexdigest(bytes)==Digest::SHA256.file(path).hexdigest,'sealed file changed: '+path)
  end
end
inputs=JSON.parse(File.read(base+'CONE_SPECTRUM_INPUTS.json')).fetch('inputs')
inputs.each do |row|
  bytes,err,status=Open3.capture3('git','show',row.fetch('commit')+':'+row.fetch('path'))
  need.call(status.success?,err)
  need.call(Digest::SHA256.hexdigest(bytes)==row.fetch('sha256'),'commit pin differs')
  need.call(Digest::SHA256.file(row.fetch('path')).hexdigest==row.fetch('sha256'),'current input differs')
end
red=lambda { |v| v.gsub(%r{/Users/[^/]+/\.pyenv/versions/3\.12\.1},'<python3.12-env>').gsub(Dir.pwd,'<repo>').gsub(raw,'<raw>').gsub(%r{/Users/[^/]+/Documents/temp001},'<prior-raw>') }
data=JSON.parse(File.read(base+'CONE_SPECTRUM_RECEIPTS.json'))
need.call(data.fetch('seals')=={'original'=>original_seal,'control'=>control_seal},'seal receipt differs')
runs=data.fetch('runs')
audits=data.fetch('audit_runs')
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
expected_exits={'native_first'=>1,'focused_first'=>1,'control_native'=>0,'control_tests'=>0,'combined_first'=>1}
need.call(runs.keys.sort==expected_exits.keys.sort,'scientific population differs')
expected_exits.each { |name,code| need.call(runs.fetch(name).fetch('receipt').fetch('exit_code')==code,'unexpected scientific exit: '+name) }
first=JSON.parse(runs.fetch('native_first').fetch('stdout'))
fixed=JSON.parse(runs.fetch('control_native').fetch('stdout'))
failed=first.fetch('checks').select { |k,v| v!=true }.keys
need.call(first.fetch('checks').size==69 && failed==['spectrum_characteristic_polynomial'] && !first.fetch('all_checks_pass'),'original outcome differs')
need.call(fixed.fetch('original_checks')==first.fetch('checks') && !fixed.fetch('original_all_checks_pass'),'original failure hidden')
need.call(fixed.fetch('effective_checks').size==73 && fixed.fetch('effective_checks').values.all? { |v| v==true } && fixed.fetch('all_effective_checks_pass'),'repair outcome differs')
need.call(fixed.fetch('repair').fetch('checks').size==6 && fixed.fetch('repair').fetch('checks').values.all? { |v| v==true },'repair safeguards differ')
need.call(first.fetch('groups').fetch('spectrum').fetch('polynomial')==fixed.fetch('repair').fetch('polynomial'),'original polynomial changed')
ids=lambda { |text| text.lines.select { |l| l.start_with?('FAILED ') }.map(&:strip).sort }
expected_ids=%w[test_generic_symbol_and_complex_unitary_reduction test_scope_and_all_control_groups].map { |t| 'FAILED tests/test_physical_bridge_cone_spectrum.py::'+t }.sort
need.call(ids.call(runs.fetch('focused_first').fetch('stdout'))==expected_ids && ids.call(runs.fetch('combined_first').fetch('stdout'))==expected_ids,'failed IDs changed')
need.call(runs.fetch('focused_first').fetch('stdout').include?('2 failed, 26 passed') && runs.fetch('combined_first').fetch('stdout').include?('2 failed, 30 passed') && runs.fetch('control_tests').fetch('stdout').include?('4 passed'),'test counts differ')
population=lambda { |name| runs.fetch(name).fetch('receipt').fetch('command').select { |x| x.start_with?('tests/') } }
need.call(population.call('focused_first')==%w[tests/test_physical_bridge_cone_spectrum.py tests/test_physical_bridge_cone_interaction.py tests/test_physical_bridge_fermion_end.py],'original test population differs')
need.call(population.call('combined_first')==population.call('focused_first')+['tests/test_physical_bridge_cone_spectrum_control.py'],'combined test population differs')
old=JSON.parse(File.read(base+'CONE_INTERACTION_RECEIPTS.json')).fetch('audit_runs').fetch('gates_precommit').fetch('stdout').lines.select { |l| l.start_with?('  FAIL ') }
audits.each do |name,row|
  if name.start_with?('gates_')
    need.call(row.fetch('receipt').fetch('exit_code')==1 && row.fetch('stdout').lines.select { |l| l.start_with?('  FAIL ') }==old,'governance failure population changed')
  else
    need.call(row.fetch('receipt').fetch('exit_code')==0,'diagnostic or custody run failed')
  end
end
puts JSON.generate(frozen_science_paths:original.size+control.size,input_pins:inputs.size,raw_captures:runs.size+audits.size,original_checks_passed:68,original_checks_total:69,effective_checks:73,combined_passes:30,retained_failed_ids:expected_ids.size,
                   scope:'Byte custody and recorded outcomes, not a proof review, full suite or physical completion')
