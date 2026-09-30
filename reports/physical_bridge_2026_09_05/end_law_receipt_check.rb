# Read-only R60 custody, not independent physical or analytic verification.
require 'json'
require 'digest'
require 'open3'
abort('Usage: ruby end_law_receipt_check.rb RAW_DIRECTORY') unless ARGV.size == 1
base='reports/physical_bridge_2026_09_05/'
raw=ARGV.fetch(0)
seal='48c04785b641d57b103ae21e2bc9d6c9426dfa1d'
need=lambda { |ok,msg| abort(msg) unless ok }
paths=%w[END_LAW_DESIGN.md END_LAW_INPUTS.json end_law.py].map { |p| base+p } + ['tests/test_physical_bridge_end_law.py']
paths.each do |path|
  bytes,err,status=Open3.capture3('git','show',seal+':'+path)
  need.call(status.success?,err)
  need.call(Digest::SHA256.hexdigest(bytes)==Digest::SHA256.file(path).hexdigest,'sealed path changed: '+path)
end
inputs=JSON.parse(File.read(base+'END_LAW_INPUTS.json')).fetch('inputs')
inputs.each do |r|
  bytes,err,status=Open3.capture3('git','show',r.fetch('commit')+':'+r.fetch('path'))
  need.call(status.success?,err)
  need.call(Digest::SHA256.hexdigest(bytes)==r.fetch('sha256'),'pinned input changed')
end
red=lambda { |v| v.gsub(%r{/Users/[^/]+/\.pyenv/versions/3\.12\.1},'<python3.12-env>').gsub(Dir.pwd,'<repo>').gsub(raw,'<raw>') }
data=JSON.parse(File.read(base+'END_LAW_RECEIPTS.json'))
runs=data.fetch('runs')
audits=data.fetch('audit_runs',{})
runs.merge(audits).each do |name,r|
  stem=File.join(raw,r.fetch('raw_basename'))
  bytes=File.binread(stem+'.log')
  receipt=JSON.parse(File.read(stem+'.json'))
  need.call(Digest::SHA256.file(stem+'.json').hexdigest==r.fetch('raw_receipt_sha256'),'raw receipt changed')
  need.call(Digest::SHA256.hexdigest(bytes)==receipt.fetch('log_sha256') && bytes.bytesize==receipt.fetch('log_bytes'),'raw log changed')
  receipt['command']=receipt.fetch('command').map { |x| red.call(x) }
  need.call(receipt==r.fetch('receipt'),'public receipt differs')
  need.call(red.call(bytes.dup.force_encoding('UTF-8'))==r.fetch('stdout'),'public output differs')
end
native=JSON.parse(runs.fetch('native_first').fetch('stdout'))
need.call(native.fetch('checks').size==30 && native.fetch('checks').values.all? && native.fetch('all_checks_pass'),'native outcome differs')
need.call(runs.fetch('focused_first').fetch('stdout').include?('15 passed'),'focused outcome differs')
foreign=JSON.parse(runs.fetch('foreign_lemma_first').fetch('stdout'))
need.call(foreign.fetch('entries')==26 && foreign.fetch('rotations')==7 && foreign.fetch('all_checks_pass'),'foreign lemma differs')
need.call(runs.values.all? { |r| r.fetch('receipt').fetch('exit_code')==0 },'a captured run failed')
if audits.key?('gates_first')
  failures=audits.fetch('gates_first').fetch('stdout').lines.select { |l| l.start_with?('  FAIL ') }
  old=JSON.parse(File.read(base+'PARENT_TENSORS_RECEIPTS.json')).fetch('runs').fetch('gates_before_seal').fetch('stdout').lines.select { |l| l.start_with?('  FAIL ') }
  need.call(failures==old,'governance failure population changed')
end
puts JSON.generate(sealed_science_paths:paths.size,input_pins:inputs.size,raw_captures:runs.size+audits.size,native_checks:30,focused_tests:15,
                   scope:'Byte custody and recorded outcomes, not an independent proof, full suite or physical completion')
