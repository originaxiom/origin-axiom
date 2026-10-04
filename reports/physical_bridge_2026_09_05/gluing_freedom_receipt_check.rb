# R86 byte and population custody; not proof, PDE or physical certification.
require 'json'
require 'digest'
require 'open3'
abort('Usage: gluing_freedom_receipt_check.rb RAW_ROOT') unless ARGV.size==1
raw=ARGV.fetch(0); base='reports/physical_bridge_2026_09_05/'
def need(v,msg)
  abort(msg) unless v
end
def git_bytes(c,p)
  b,e,s=Open3.capture3('git','show',c+':'+p)
  need(s.success?,e); b.b
end
seal=JSON.parse(File.read(base+'GLUING_FREEDOM_SEAL.json',encoding:'UTF-8'))
need(seal.fetch('paths').size==6,'Science population')
section=File.read('docs/SEAL_LEDGER.md',encoding:'UTF-8').split('## Relative gluing repaired seal latest path rows October 4 2026',2).last
need(section,'Latest ledger section')
rows=section.split(/^## /,2).first.scan(/`([^`]+)`\s*\|\s*`([0-9a-f]{64})`/).to_h
need(rows.size==6,'Latest ledger population')
seal.fetch('paths').each do |p|
  b=File.binread(p.fetch('path'))
  need(b==git_bytes(seal.fetch('science_seal'),p.fetch('path')),'Changed science')
  need(b.bytesize==p.fetch('bytes')&&Digest::SHA256.hexdigest(b)==p.fetch('sha256'),'Science pin')
  need(rows.fetch(p.fetch('path'))==p.fetch('sha256'),'Ledger pin')
end
inputs=JSON.parse(File.read(base+'GLUING_FREEDOM_INPUTS.json',encoding:'UTF-8'))
inputs.fetch('local_pins').each do |p|
  b=git_bytes(inputs.fetch('baseline'),p.fetch('path'))
  need(b==File.binread(p.fetch('path'))&&Digest::SHA256.hexdigest(b)==p.fetch('sha256'),'Retained source pin')
end
paper=JSON.parse(File.read(base+'JOINED_BACKGROUND_INPUTS.json')).fetch('paper')
pb=File.binread(paper.fetch('local_path'))
need(pb.bytesize==paper.fetch('bytes')&&Digest::SHA256.hexdigest(pb)==paper.fetch('sha256'),'Retained primary PDF')
data=JSON.parse(File.read(base+'GLUING_FREEDOM_RECEIPTS.json',encoding:'UTF-8'))
need(data.fetch('science_seal')==seal.fetch('science_seal'),'Science identity')
red=lambda { |v| v.gsub(raw,'<glue-raw>').gsub(Dir.pwd,'<repo>').gsub('/Users/dri/.pyenv/versions/3.12.1','<python3.12-env>') }
runs=data.fetch('runs')
runs.each do |key,r|
  stem=File.join(raw,r.fetch('raw_basename')); receipt=File.binread(stem+'.json'); log=File.binread(stem+'.log'); m=JSON.parse(receipt)
  need(Digest::SHA256.hexdigest(receipt)==r.fetch('raw_receipt_sha256'),'Raw receipt '+key)
  need(log.bytesize==m.fetch('log_bytes')&&Digest::SHA256.hexdigest(log)==m.fetch('log_sha256'),'Raw stdout '+key)
  m['command']=m.fetch('command').map { |v| red.call(v) }
  need(m==r.fetch('receipt'),'Actual command and exit '+key)
  need(red.call(log.force_encoding('UTF-8'))==r.fetch('stdout_redacted'),'Public stdout '+key)
  expected=(key=='native_first'||key.start_with?('governance')) ? 1 : 0
  need(m.fetch('exit_code')==expected,'Unexpected exit '+key)
end
%w[seal_server repair_server ledger_server].zip([seal.fetch('failed_original_seal'),seal.fetch('scientific_repair'),seal.fetch('science_seal')]).each do |key,c|
  need(runs.fetch(key).fetch('stdout_redacted').split.first==c,'Server confirmation '+key)
end
%w[native_repaired reference_first].zip([84,141]).each do |key,n|
  records=runs.fetch(key).fetch('stdout_redacted').lines.map { |x| JSON.parse(x) }; summary=records.pop
  cs=records.flat_map { |r| r.fetch('checks').values }
  need(cs.size==n&&cs.all? { |v| v==true }&&summary.values_at('all','passed','total')==[true,n,n],'Finite population '+key)
  cases=records.select { |r| %w[case witness].include?(r['group']) }
  if key=='native_repaired'
    need(cases.map { |r| r['character'] }==inputs.fetch('characters'),'Native characters')
    need(cases.all? { |r| r.values_at('left_algebra_dimension','right_algebra_dimension','neutral_h1_lower_bound','coboundary_rank','joined_rank')==[21,21,4,24,28] },'Actual neutral lower bound')
  else
    need(cases.map { |r| r.values_at('prime','root','character') }==inputs.fetch('reference_prime_roots').flat_map { |p,r| inputs.fetch('characters').map { |ab| [p,r,ab] } },'Reference population')
  end
end
original=runs.fetch('native_first').fetch('stdout_redacted').lines.map { |x| JSON.parse(x) }.last
need(original.values_at('all','passed','total')==[false,76,84],'Original failure retained')
need(runs.fetch('diagnosis_first').fetch('stdout_redacted').include?('Kzero == intzero False'),'Scalar diagnosis retained')
need(runs.fetch('focus_first').fetch('stdout_redacted').include?('12 passed'),'Focused outcome')
ids=Hash.new(0)
runs.fetch('collect_first').fetch('stdout_redacted').lines.each { |l| ids[l.split('::').first]+=1 if l.start_with?('tests/') }
need(ids=={'tests/test_physical_bridge_gluing_freedom.py'=>6,'tests/test_physical_bridge_joined_background.py'=>6},'Focused population')
runs.select { |k,_| k.start_with?('governance') }.each do |_,rec|
  out=rec.fetch('stdout_redacted'); fails=out.lines.map { |l| m=l.match(/^\s*FAIL\s+([^: ]+)/); m&&m[1] }.compact.sort
  need(fails==%w[attribution relay-debt seal-provenance test-vacuity].sort,'Governance changed categories')
  need(out.lines.count { |l| l.match(/^\s*PASS\s/) }==26,'Governance pass population')
end
puts JSON.generate(frozen_paths:6,local_pins:5,primary_pdf_pins:1,raw_captures:runs.size,
                   failed_originals:1,native:84,reference_modular:141,focused:12,
                   scope:'R86 byte/population custody only; not independent proof, full suite, main banking or physical completion')
