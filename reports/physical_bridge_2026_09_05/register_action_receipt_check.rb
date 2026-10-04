require 'json'
require 'digest'
require 'open3'
base=File.dirname(__FILE__)
repo=File.expand_path('../..',base)
raw=ARGV.shift
abort('raw directory required') unless raw && File.directory?(raw)
inputs=JSON.parse(File.read(File.join(base,'REGISTER_ACTION_INPUTS.json'),encoding:'UTF-8'))
seal=JSON.parse(File.read(File.join(base,'REGISTER_ACTION_SEAL.json'),encoding:'UTF-8'))
receipts=JSON.parse(File.read(File.join(base,'REGISTER_ACTION_RECEIPTS.json'),encoding:'UTF-8'))
seal['science_files'].each do |r|
  b=File.binread(File.join(repo,r['path']))
  old,e,s=Open3.capture3('git','-C',repo,'show',seal['commit']+':'+r['path'])
  abort('science mismatch '+r['path']) unless s.success? && b==old && b.bytesize==r['bytes'] && Digest::SHA256.hexdigest(b)==r['sha256']
end
inputs['sources'].each do |r|
  b,e,s=Open3.capture3('git','-C',repo,'show',r['ref']+':'+r['path'])
  abort('source pin mismatch '+r['path']) unless s.success? && b.bytesize==r['bytes'] && Digest::SHA256.hexdigest(b)==r['sha256']
end
inputs['external_pdfs'].each do |r|
  b=File.binread(File.join(raw,r['external_basename']))
  abort('PDF mismatch') unless b.bytesize==r['bytes'] && Digest::SHA256.hexdigest(b)==r['sha256']
end
receipts['captures'].each do |stem,r|
  actual=JSON.parse(File.read(File.join(raw,stem+'.json'),encoding:'UTF-8'))
  b=File.binread(File.join(raw,stem+'.log'))
  normalized=Marshal.load(Marshal.dump(actual))
  normalized['command']=normalized['command'].map{|v|v.gsub(raw,'<raw-root>').gsub('/Users/dri/.pyenv/versions/3.12.1','<python3.12-env>')}
  abort('receipt mismatch '+stem) unless normalized==r && b.bytesize==r['log_bytes'] && Digest::SHA256.hexdigest(b)==r['log_sha256']
  pub=receipts.fetch('public_logs',{})[stem]
  abort('public log mismatch '+stem) if pub && b!=File.binread(File.join(base,pub))
end
%w[native reference].each do |stem|
  d=JSON.parse(File.read(File.join(raw,stem+'.log'),encoding:'UTF-8'))
  expected=stem=='native' ? 73 : 1913
  abort('science does not pass '+stem) unless receipts['captures'][stem]['exit_code']==0 && receipts['captures'][stem]['signal'].nil? && d['checks'].length==expected && d['checks'].values.all?{|v|v==true} && d['total']==expected && d['passed']==expected && d['failed']==[] && d['physical_goal_achieved']==false
  abort('summary mismatch') unless d.reject{|k,v|k=='checks'}==receipts[stem+'_summary']
end
abort('focused mismatch') unless receipts['captures']['focused']['exit_code']==0 && File.read(File.join(raw,'focused.log')).match?(/20 passed in [0-9.]+s/)
abort('server seal mismatch') unless File.read(File.join(raw,'server_seal.log')).split.first==seal['commit']
receipts.fetch('custody_checks',{}).each do |stem,row|
  actual=JSON.parse(File.read(File.join(raw,stem+'.json'),encoding:'UTF-8'))
  b=File.binread(File.join(raw,stem+'.log'))
  normalized=Marshal.load(Marshal.dump(actual))
  normalized['command']=normalized['command'].map{|v|v.gsub(raw,'<raw-root>')}
  abort('custody snapshot mismatch') unless normalized==row['receipt'] && actual['exit_code']==0 && actual['signal'].nil? && actual['log_bytes']==b.bytesize && actual['log_sha256']==Digest::SHA256.hexdigest(b) && b==File.binread(File.join(base,row['public_log']))
end
abort('unearned certification') unless receipts['governance_first_invalidated_by_concurrent_publication_edit']==true && seal['non_author_acceptance']==false && seal['analytic_proof_independently_verified']==false && seal['physical_goal_achieved']==false
puts JSON.generate(science_files:6,source_pins:15,primary_pdfs:2,raw_captures:receipts['captures'].length,native:73,reference:1913,focused:20,unchanged_science:true,bytes_and_true_exits_match:true,first_governance_invalidated:true,non_author_acceptance:false,physical_goal_achieved:false)
