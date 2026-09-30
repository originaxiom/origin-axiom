# Read-only R61 custody, not independent physical or analytic verification.
require 'json'
require 'digest'
require 'open3'
abort('Usage: ruby fermion_end_receipt_check.rb RAW_DIRECTORY') unless ARGV.size == 1
base='reports/physical_bridge_2026_09_05/'
raw=ARGV.fetch(0)
seal='7427a24df7d78cb4b0cbd4892d0406b195a546d7'
need=lambda { |ok,msg| abort(msg) unless ok }
paths=%w[FERMION_END_DESIGN.md FERMION_END_INPUTS.json fermion_end.py].map { |p| base+p } + ['tests/test_physical_bridge_fermion_end.py']
paths.each do |path|
  bytes,err,status=Open3.capture3('git','show',seal+':'+path)
  need.call(status.success?,err)
  need.call(Digest::SHA256.hexdigest(bytes)==Digest::SHA256.file(path).hexdigest,'sealed path changed: '+path)
end
inputs=JSON.parse(File.read(base+'FERMION_END_INPUTS.json')).fetch('inputs')
inputs.each do |r|
  bytes,err,status=Open3.capture3('git','show',r.fetch('commit')+':'+r.fetch('path'))
  need.call(status.success?,err)
  need.call(Digest::SHA256.hexdigest(bytes)==r.fetch('sha256'),'pinned input changed')
end
red=lambda { |v| v.gsub(%r{/Users/[^/]+/\.pyenv/versions/3\.12\.1},'<python3.12-env>').gsub(Dir.pwd,'<repo>').gsub(raw,'<raw>') }
data=JSON.parse(File.read(base+'FERMION_END_RECEIPTS.json'))
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
need.call(native.fetch('checks').size==50 && native.fetch('checks').values.all? && native.fetch('all_checks_pass'),'native outcome differs')
need.call(runs.fetch('focused_first').fetch('stdout').include?('20 passed'),'focused outcome differs')
need.call(runs.values.all? { |r| r.fetch('receipt').fetch('exit_code')==0 },'a captured run failed')
audits.each do |name,audit|
  next unless name.start_with?('gates_')
  failures=audit.fetch('stdout').lines.select { |l| l.start_with?('  FAIL ') }
  old=JSON.parse(File.read(base+'END_LAW_RECEIPTS.json')).fetch('audit_runs').fetch('gates_first').fetch('stdout').lines.select { |l| l.start_with?('  FAIL ') }
  if name == 'gates_precommit'
    additional=failures-old
    need.call(additional.size==1 && additional.first.start_with?('  FAIL  law-map-provenance:') && (old-failures).empty?, 'initial documentation failure differs')
  else
    need.call(failures==old,'governance failure population changed')
  end
end
puts JSON.generate(sealed_science_paths:paths.size,input_pins:inputs.size,raw_captures:runs.size+audits.size,native_checks:50,focused_tests:20,
                   scope:'Byte custody and recorded outcomes, not an independent proof, full suite or physical completion')
