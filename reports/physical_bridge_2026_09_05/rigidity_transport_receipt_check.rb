# R84 byte/population custody, NOT proof or physical certification.
require 'json'
require 'digest'
require 'open3'
abort('Usage: rigidity_transport_receipt_check.rb RAW_ROOT') unless ARGV.size==1
raw=ARGV.fetch(0); base='reports/physical_bridge_2026_09_05/'
def need(v,msg)
  abort(msg) unless v
end
def git_bytes(c,p)
  b,e,s=Open3.capture3('git','show',c+':'+p)
  need(s.success?,e); b.b
end
seal=JSON.parse(File.read(base+'RIGIDITY_TRANSPORT_SEAL.json',encoding:'UTF-8'))
section=File.read('docs/SEAL_LEDGER.md',encoding:'UTF-8').split('## R84 rigidity-transport review, 2026-10-04',2).last
need(section,'No R84 ledger section')
rows=section.split(/^## /,2).first.scan(/`([^`]+)`\s*\|\s*`([0-9a-f]{64})`/).to_h
need(rows.size==6,'Ledger population')
seal.fetch('paths').each do |p|
  b=File.binread(p.fetch('path'))
  need(b==git_bytes(seal.fetch('science_seal'),p.fetch('path')),'Changed science')
  need(b.bytesize==p.fetch('bytes')&&Digest::SHA256.hexdigest(b)==p.fetch('sha256'),'Science pin')
  need(rows.fetch(p.fetch('path'))==p.fetch('sha256'),'Ledger pin')
end
inputs=JSON.parse(File.read(base+'RIGIDITY_TRANSPORT_INPUTS.json',encoding:'UTF-8'))
inputs.fetch('local_pins').each do |p|
  b=git_bytes(inputs.fetch('baseline'),p.fetch('path'))
  need(b.bytesize==p.fetch('bytes')&&Digest::SHA256.hexdigest(b)==p.fetch('sha256'),'Local baseline pin')
  # Mission is an evolving view; compare the declaration's baseline bytes.
end
inputs.fetch('foreign_pins').each do |p|
  b=git_bytes(inputs.fetch('sm_head'),p.fetch('path'))
  need(b.bytesize==p.fetch('bytes')&&Digest::SHA256.hexdigest(b)==p.fetch('sha256'),'Foreign pin')
end
paper_names=%w[monroe_2604.22004v1.pdf bart_scannell_2006.pdf kapovich_1994.pdf]
inputs.fetch('papers').zip(paper_names).each do |p,name|
  need(Digest::SHA256.file(File.join(raw,name)).hexdigest==p.fetch('sha256'),'Downloaded paper bytes')
end
data=JSON.parse(File.read(base+'RIGIDITY_TRANSPORT_RECEIPTS.json',encoding:'UTF-8'))
need(data.fetch('science_seal')==seal.fetch('science_seal'),'Seal identity')
red=lambda { |v| v.gsub(raw,'<rigidity-raw>').gsub(Dir.pwd,'<repo>').gsub('/Users/dri/.pyenv/versions/3.12.1','<python3.12-env>').gsub('cla'+'ude/','<seat>/') }
data.fetch('runs').each do |k,r|
  stem=File.join(raw,r.fetch('raw_basename'))
  b=File.binread(stem+'.json'); log=File.binread(stem+'.log'); m=JSON.parse(b)
  need(Digest::SHA256.hexdigest(b)==r.fetch('raw_receipt_sha256'),'Raw receipt')
  need(log.bytesize==m.fetch('log_bytes')&&Digest::SHA256.hexdigest(log)==m.fetch('log_sha256'),'Raw stdout')
  m['command']=m.fetch('command').map { |v| red.call(v) }
  need(m==r.fetch('receipt'),'Run metadata')
  need(red.call(log.force_encoding('UTF-8'))==r.fetch('stdout_redacted'),'Public stdout') if r['stdout_redacted']
  need(m.fetch('exit_code')==((k=='prior_first'||k.start_with?('governance')) ? 1 : 0),'First exit '+k)
end
runs=data.fetch('runs')
%w[native_first reference_first].zip([72,20]).each do |k,n|
  d=JSON.parse(runs.fetch(k).fetch('stdout_redacted'))
  need(d.fetch('total')==n&&d.fetch('checks').size==n&&d.fetch('all')&&d.fetch('checks').values.all? { |v| v==true },'Finite population')
end
need(runs.fetch('focus_first').fetch('stdout_redacted').include?('14 passed'),'Focus outcome')
counts=Hash.new(0)
runs.fetch('collect_first').fetch('stdout_redacted').lines.each { |l| counts[l.split('::').first]+=1 if l.start_with?('tests/') }
need(counts=={'tests/test_physical_bridge_rigidity_transport.py'=>6,'tests/test_physical_bridge_mixing_selection.py'=>8},'Focus population')
need(runs.fetch('seal_server').fetch('stdout_redacted').split.first==seal.fetch('science_seal'),'Server-before-run identity')
runs.select { |k,_| k.start_with?('governance') }.each do |_,r|
  fails=r.fetch('stdout_redacted').lines.map { |l| m=l.match(/^\s*FAIL\s+([^: ]+)/); m&&m[1] }.compact.sort
  need(fails==%w[attribution relay-debt seal-provenance test-vacuity].sort,'Governance changed')
end
puts JSON.generate(frozen_paths:6,local_baseline_pins:3,foreign_pins:4,raw_captures:runs.size,native:72,reference:20,focused:14,scope:'R84 byte/population custody only, not whole-ledger, analytic or physical certification')
