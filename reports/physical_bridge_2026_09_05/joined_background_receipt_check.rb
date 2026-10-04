# R85 byte/population custody only; not proof, PDE or physical certification.
require 'json'
require 'digest'
require 'open3'
abort('Usage: joined_background_receipt_check.rb RAW_ROOT') unless ARGV.size==1
raw=ARGV.fetch(0); base='reports/physical_bridge_2026_09_05/'
def need(v,msg)
  abort(msg) unless v
end
def git_bytes(c,p)
  b,e,s=Open3.capture3('git','show',c+':'+p)
  need(s.success?,e); b.b
end
seal=JSON.parse(File.read(base+'JOINED_BACKGROUND_SEAL.json',encoding:'UTF-8'))
need(seal.fetch('paths').size==6,'Seal population')
section=File.read('docs/SEAL_LEDGER.md',encoding:'UTF-8').split('## R85 field determinant API repair reseal, 2026-10-04',2).last
need(section,'Missing repaired ledger seal')
rows=section.split(/^## /,2).first.scan(/`([^`]+)`\s*\|\s*`([0-9a-f]{64})`/).to_h
need(rows.size==6,'Latest ledger population')
seal.fetch('paths').each do |p|
  b=File.binread(p.fetch('path'))
  need(b==git_bytes(seal.fetch('science_seal'),p.fetch('path')),'Changed science')
  need(b.bytesize==p.fetch('bytes')&&Digest::SHA256.hexdigest(b)==p.fetch('sha256'),'Science pin')
  need(rows.fetch(p.fetch('path'))==p.fetch('sha256'),'Ledger pin')
end
inputs=JSON.parse(File.read(base+'JOINED_BACKGROUND_INPUTS.json',encoding:'UTF-8'))
inputs.fetch('local_pins').each do |p|
  b=git_bytes(inputs.fetch('baseline'),p.fetch('path'))
  need(b==File.binread(p.fetch('path')),'Changed retained local source')
  need(b.bytesize==p.fetch('bytes')&&Digest::SHA256.hexdigest(b)==p.fetch('sha256'),'Local source pin')
end
paper=inputs.fetch('paper'); pb=File.binread(paper.fetch('local_path'))
need(pb.bytesize==paper.fetch('bytes')&&Digest::SHA256.hexdigest(pb)==paper.fetch('sha256'),'Primary PDF pin')
data=JSON.parse(File.read(base+'JOINED_BACKGROUND_RECEIPTS.json',encoding:'UTF-8'))
need(data.fetch('science_seal')==seal.fetch('science_seal'),'Seal receipt identity')
red=lambda { |v| v.gsub(raw,'<join-raw>').gsub(Dir.pwd,'<repo>').gsub('/Users/dri/.pyenv/versions/3.12.1','<python3.12-env>') }
runs=data.fetch('runs')
runs.each do |key,r|
  stem=File.join(raw,r.fetch('raw_basename')); b=File.binread(stem+'.json'); log=File.binread(stem+'.log'); m=JSON.parse(b)
  need(Digest::SHA256.hexdigest(b)==r.fetch('raw_receipt_sha256'),'Raw receipt '+key)
  need(log.bytesize==m.fetch('log_bytes')&&Digest::SHA256.hexdigest(log)==m.fetch('log_sha256'),'Raw stdout '+key)
  m['command']=m.fetch('command').map { |v| red.call(v) }
  need(m==r.fetch('receipt'),'Command/exit receipt '+key)
  need(red.call(log.force_encoding('UTF-8'))==r.fetch('stdout_redacted'),'Public stdout '+key)
  expected=(%w[native_first native_repaired].include?(key)||key.start_with?('governance')) ? 1 : 0
  need(m.fetch('exit_code')==expected,'Actual exit '+key)
end
%w[seal_server repair_server field_det_server].zip(seal.fetch('failed_attempted_seals')+[seal.fetch('science_seal')]).each do |key,c|
  need(runs.fetch(key).fetch('stdout_redacted').split.first==c,'Server seal '+key)
end
need(runs.fetch('native_first').fetch('stdout_redacted').include?('TypeError'),'First failure retained')
need(runs.fetch('native_repaired').fetch('stdout_redacted').include?('ExactQuotientFailed'),'Second failure retained')
%w[native_field_det reference_first].zip([60,75]).each do |key,n|
  recs=runs.fetch(key).fetch('stdout_redacted').lines.map { |l| JSON.parse(l) }
  summary=recs.pop; checks=recs.flat_map { |r| r.fetch('checks').values }
  need(checks.size==n&&checks.all? { |v| v==true }&&summary.fetch('all')&&summary.fetch('passed')==n&&summary.fetch('total')==n,'Finite population '+key)
  if key=='native_field_det'
    cases=recs.select { |r| r['group']=='case' }
    need(cases.map { |r| r['character'] }==inputs.fetch('characters'),'Character population')
    need(cases.all? { |r| r['algebra_dimension']==25&&r.fetch('witness').fetch('span_words').size==25 },'Word witnesses')
    spectrum=recs.find { |r| r['group']=='spectrum' }
    need(spectrum.fetch('representative')==inputs.fetch('count_representative'),'Count representative')
    need(%w[rank_five dual_five].all? { |k| spectrum.fetch(k).values_at('h0','h1','d0_rank','d1_rank')==[0,2,5,23] },'Exact five counts')
    need(spectrum.fetch('exterior_join_h1')==2&&spectrum.fetch('dual_exterior_join_h1')==2,'Exact exterior counts')
  else
    need(summary.fetch('selected_prime_roots')==[[1031,695],[1033,162]],'Modular witness population')
    need(recs.count { |r| r['group']=='witness' }==6,'Six reference witnesses')
  end
end
need(runs.fetch('focus_first').fetch('stdout_redacted').include?('12 passed'),'Focused outcome')
count=Hash.new(0)
runs.fetch('collect_first').fetch('stdout_redacted').lines.each { |l| count[l.split('::').first]+=1 if l.start_with?('tests/') }
need(count=={'tests/test_physical_bridge_joined_background.py'=>6,'tests/test_physical_bridge_cross_branch_positives.py'=>6},'Focused IDs')
runs.select { |k,_| k.start_with?('governance') }.each do |_,r|
  out=r.fetch('stdout_redacted'); fails=out.lines.map { |l| m=l.match(/^\s*FAIL\s+([^: ]+)/); m&&m[1] }.compact.sort
  need(fails==%w[attribution relay-debt seal-provenance test-vacuity].sort,'Governance changed categories')
  need(out.lines.count { |l| l.match(/^\s*PASS\s/) }==26,'Governance pass population')
end
puts JSON.generate(frozen_paths:6,local_pins:3,primary_pdf_pins:1,raw_captures:runs.size,
                   failed_attempted_seals:2,native:60,reference_modular:75,focused:12,
                   scope:'R85 byte/population custody only, not analytic proof, main banking or physical completion')
