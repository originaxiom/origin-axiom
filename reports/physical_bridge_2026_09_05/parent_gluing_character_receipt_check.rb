# R87 byte and finite-population custody, not independent proof or physics.
require 'json'
require 'digest'
require 'open3'
abort('Usage: parent_gluing_character_receipt_check.rb RAW_ROOT') unless ARGV.size==1
raw=ARGV.fetch(0); base='reports/physical_bridge_2026_09_05/'
def need(v,msg)
  abort(msg) unless v
end
def git_bytes(c,p)
  b,e,s=Open3.capture3('git','show',c+':'+p)
  need(s.success?,e); b.b
end
seal=JSON.parse(File.read(base+'PARENT_GLUING_CHARACTER_SEAL.json',encoding:'UTF-8'))
need(seal.fetch('paths').size==6,'Science population')
ledger=File.read('docs/SEAL_LEDGER.md',encoding:'UTF-8')
header='## Parent gluing character pre execution seal October 4 2026'
need(ledger.scan(header).size==1,'Unique ledger section')
section=ledger.split(header,2).last.split(/^## /,2).first
rows=section.scan(/`([^`]+)`\s*\|\s*`([0-9a-f]{64})`/).to_h
need(rows.size==6,'Latest ledger population')
seal.fetch('paths').each do |p|
  b=File.binread(p.fetch('path'))
  need(b==git_bytes(seal.fetch('science_seal'),p.fetch('path')),'Changed science')
  need(b.bytesize==p.fetch('bytes')&&Digest::SHA256.hexdigest(b)==p.fetch('sha256'),'Science pin')
  need(rows.fetch(p.fetch('path'))==p.fetch('sha256'),'Ledger pin')
end
inputs=JSON.parse(File.read(base+'PARENT_GLUING_CHARACTER_INPUTS.json',encoding:'UTF-8'))
inputs.fetch('local_pins').each do |p|
  b=git_bytes(inputs.fetch('baseline'),p.fetch('path'))
  need(b==File.binread(p.fetch('path'))&&Digest::SHA256.hexdigest(b)==p.fetch('sha256'),'Retained source pin')
end
data=JSON.parse(File.read(base+'PARENT_GLUING_CHARACTER_RECEIPTS.json',encoding:'UTF-8'))
need(data.fetch('science_seal')==seal.fetch('science_seal'),'Science identity')
red=lambda { |v| v.gsub(raw,'<parent-character-raw>').gsub(Dir.pwd,'<repo>').gsub('/Users/dri/.pyenv/versions/3.12.1','<python3.12-env>') }
runs=data.fetch('runs')
runs.each do |key,r|
  stem=File.join(raw,r.fetch('raw_basename')); receipt=File.binread(stem+'.json'); log=File.binread(stem+'.log'); m=JSON.parse(receipt)
  need(Digest::SHA256.hexdigest(receipt)==r.fetch('raw_receipt_sha256'),'Raw receipt '+key)
  need(log.bytesize==m.fetch('log_bytes')&&Digest::SHA256.hexdigest(log)==m.fetch('log_sha256'),'Raw stdout '+key)
  m['command']=m.fetch('command').map { |v| red.call(v) }
  need(m==r.fetch('receipt'),'Actual command and exit '+key)
  need(red.call(log.force_encoding('UTF-8'))==r.fetch('stdout_redacted'),'Public stdout '+key)
  need(m.fetch('exit_code')==(key.start_with?('governance') ? 1 : 0),'Unexpected exit '+key)
end
need(runs.fetch('seal_server').fetch('stdout_redacted').split.first==seal.fetch('science_seal'),'Server confirmation')
%w[native_first reference_first].zip([145,209]).each do |key,n|
  records=runs.fetch(key).fetch('stdout_redacted').lines.map { |x| JSON.parse(x) }; summary=records.pop
  cs=records.flat_map { |r| r.fetch('checks').values + r.fetch('samples',[]).flat_map { |s| s.fetch('checks').values } }
  need(cs.size==n&&cs.all? { |v| v==true }&&summary.values_at('all','passed','total')==[true,n,n],'Finite population '+key)
  cases=records.select { |r| r['group']=='case' }
  need(cases.all? { |r| r.fetch('samples').map { |s| s.fetch('t') }==inputs.fetch('t_values') },'Sample population')
  if key=='native_first'
    need(cases.map { |r| r['character'] }==inputs.fetch('characters'),'Native characters')
    need(cases.all? { |r| r['parent_degree']==2&&r['derivative_zero']==false },'Nonconstant parent and local derivative')
    rr=records.find { |r| r['group']=='roots' }
    need(rr.values_at('root_count','total_weights')==[240,248],'Root population')
    need(rr.fetch('center_kernel')==[[0,0],[1,3],[2,1],[3,4],[4,2]],'Actual parent center kernel')
  else
    need(cases.map { |r| r.values_at('prime','root','character') }==inputs.fetch('reference_prime_roots').flat_map { |p,r| inputs.fetch('characters').map { |ab| [p,r,ab] } },'Reference population')
  end
end
need(runs.fetch('focus_first').fetch('stdout_redacted').include?('12 passed'),'Focused outcome')
ids=Hash.new(0)
runs.fetch('collect_first').fetch('stdout_redacted').lines.each { |l| ids[l.split('::').first]+=1 if l.start_with?('tests/') }
need(ids=={'tests/test_physical_bridge_parent_gluing_character.py'=>6,'tests/test_physical_bridge_gluing_freedom.py'=>6},'Focused population')
runs.select { |k,_| k.start_with?('governance') }.each do |_,r|
  out=r.fetch('stdout_redacted'); fails=out.lines.map { |l| m=l.match(/^\s*FAIL\s+([^: ]+)/); m&&m[1] }.compact.sort
  need(fails==%w[attribution relay-debt seal-provenance test-vacuity].sort,'Governance changed categories')
  need(out.lines.count { |l| l.match(/^\s*PASS\s/) }==26,'Governance pass population')
end
if runs.key?('foreign_readout_probe_first')
  pin=data.fetch('foreign_readout_pin'); b=git_bytes(pin.fetch('commit'),pin.fetch('path'))
  need(b.bytesize==pin.fetch('bytes')&&Digest::SHA256.hexdigest(b)==pin.fetch('sha256'),'Foreign diagnostic source pin')
  r=JSON.parse(runs.fetch('foreign_readout_probe_first').fetch('stdout_redacted'))
  need(r.fetch('one_cover_can_report_every_cover_read')&&r.fetch('candidate_part_F').fetch('readings')==0,'Synthetic coverage diagnostic')
  need(r.fetch('candidate_without_part_F_rows_predictions').values_at('P7','P8')==[true,true],'Synthetic vacuity diagnostic')
end
puts JSON.generate(frozen_paths:6,local_pins:5,raw_captures:runs.size,native:145,
                   reference_modular:209,focused:12,
                   scope:'R87 byte/population custody only; not independent proof, full suite, main banking or physical completion')
