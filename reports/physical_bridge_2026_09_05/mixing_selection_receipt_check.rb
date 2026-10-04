# R83 six-row byte/population custody, not analytic or physical certification.
require 'json'
require 'digest'
require 'open3'
abort('Usage: mixing_selection_receipt_check.rb RAW_ROOT') unless ARGV.size==1
raw=ARGV.fetch(0);base='reports/physical_bridge_2026_09_05/'
def need(ok,msg)
  abort(msg) unless ok
end
def git_bytes(commit,path)
  b,e,s=Open3.capture3('git','show',commit+':'+path)
  need(s.success?,e);b.b
end
seal=JSON.parse(File.read(base+'MIXING_SELECTION_SEAL.json',encoding:'UTF-8'))
section=File.read('docs/SEAL_LEDGER.md',encoding:'UTF-8').split('## R83 mixing/order-selection reply, 2026-10-04',2).last
need(section,'Missing R83 section')
rows=section.split(/^## /,2).first.scan(/`([^`]+)`\s*\|\s*`([0-9a-f]{64})`/).to_h
need(rows.size==6,'Wrong ledger population')
seal.fetch('paths').each do |r|
  b=File.binread(r.fetch('path'))
  need(b==git_bytes(seal.fetch('science_seal'),r.fetch('path')),'Changed science')
  need(b.bytesize==r.fetch('bytes')&&Digest::SHA256.hexdigest(b)==r.fetch('sha256'),'Science hash')
  need(rows.fetch(r.fetch('path'))==r.fetch('sha256'),'Ledger hash')
end
inputs=JSON.parse(File.read(base+'MIXING_SELECTION_INPUTS.json',encoding:'UTF-8'))
inputs.fetch('dependencies').each do |r|
  b=git_bytes(inputs.fetch('baseline'),r.fetch('path'))
  need(b==File.binread(r.fetch('path')),'Changed local context')
  need(b.bytesize==r.fetch('bytes')&&Digest::SHA256.hexdigest(b)==r.fetch('sha256'),'Context pin')
end
inputs.fetch('foreign').each do |r|
  b=git_bytes(r.fetch('commit'),r.fetch('path'))
  need(b.bytesize==r.fetch('bytes')&&Digest::SHA256.hexdigest(b)==r.fetch('sha256'),'Foreign pin')
end
data=JSON.parse(File.read(base+'MIXING_SELECTION_RECEIPTS.json',encoding:'UTF-8'))
need(data.fetch('science_seal')==seal.fetch('science_seal'),'Science seal mismatch')
red=lambda{|v|v.gsub(raw,'<mixing-raw>').gsub(Dir.pwd,'<repo>').gsub('/Users/dri/.pyenv/versions/3.12.1','<python3.12-env>').gsub('cla'+'ude/','<seat>/')}
data.fetch('runs').each do |key,r|
  stem=File.join(raw,r.fetch('raw_basename'))
  b=File.binread(stem+'.json');log=File.binread(stem+'.log');meta=JSON.parse(b)
  need(Digest::SHA256.hexdigest(b)==r.fetch('raw_receipt_sha256'),'Raw receipt drift')
  need(log.bytesize==meta.fetch('log_bytes')&&Digest::SHA256.hexdigest(log)==meta.fetch('log_sha256'),'Raw log drift')
  meta['command']=meta.fetch('command').map{|x|red.call(x)}
  need(meta==r.fetch('receipt'),'Command/status drift')
  need(red.call(log.force_encoding('UTF-8'))==r.fetch('stdout_redacted'),'Public log drift') if r['stdout_redacted']
  expected=(key=='prior'||key.start_with?('governance')) ? 1 : 0
  need(meta.fetch('exit_code')==expected,'Unexpected first exit '+key)
end
runs=data.fetch('runs')
native=JSON.parse(runs.fetch('native_first').fetch('stdout_redacted'))
values=native.fetch('groups').values.flat_map{|g|g.fetch('checks').values}
need(native.fetch('passed')==33&&native.fetch('total')==33&&values.size==33&&values.all?{|x|x==true},'Native population')
ref=JSON.parse(runs.fetch('reference_first').fetch('stdout_redacted'))
need(ref.fetch('passed')==413&&ref.fetch('total')==413&&ref.fetch('all_checks_pass'),'Reference population')
need(runs.fetch('focus_first').fetch('stdout_redacted').include?('18 passed'),'Focused outcome')
counts=Hash.new(0)
runs.fetch('collection_first').fetch('stdout_redacted').lines.each{|l|counts[l.split('::').first]+=1 if l.start_with?('tests/')}
need(counts=={'tests/test_physical_bridge_mixing_selection.py'=>8,'tests/test_physical_bridge_dirichlet_admission.py'=>10},'Focused population')
need(runs.fetch('seal_server').fetch('stdout_redacted').split.first==seal.fetch('science_seal'),'Server seal mismatch')
runs.select{|k,_|k.start_with?('governance')}.each do |_,r|
  fails=r.fetch('stdout_redacted').lines.map{|l|m=l.match(/^\s*FAIL\s+([^: ]+)/);m&&m[1]}.compact.sort
  need(fails==%w[attribution relay-debt seal-provenance test-vacuity].sort,'Governance baseline differs')
end
puts JSON.generate(frozen_science_paths:6,local_pins:7,foreign_pins:6,raw_captures:runs.size,native:33,reference:413,focused:18,scope:'R83 byte/population custody only; no whole-ledger or nonauthor analytic certificate')
