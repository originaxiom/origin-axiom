# R93 byte/exit/population custody, not analytic or physical acceptance.
require 'json'
require 'digest'
base=File.dirname(__FILE__)
Dir.chdir(File.expand_path('../..',base))
raw=ARGV[0]
abort('Usage: joined_wilson_receipt_check.rb RAW_ROOT') unless raw
seal=JSON.parse(File.read(File.join(base,'JOINED_WILSON_SEAL.json'),encoding:'UTF-8'))
corrected=JSON.parse(File.read(File.join(base,'JOINED_WILSON_CORRECTED_SEAL.json'),encoding:'UTF-8'))
receipts=JSON.parse(File.read(File.join(base,'JOINED_WILSON_RECEIPTS.json'),encoding:'UTF-8'))
inputs=JSON.parse(File.read(File.join(base,'JOINED_WILSON_INPUTS.json'),encoding:'UTF-8'))
ledger={}
File.foreach(File.join(base,'ARTIFACT_HASHES.txt'),encoding:'UTF-8') do |line|
  m=line.match(/^([a-f0-9]{64})  (.+)$/)
  ledger[m[2]]=m[1] if m
end
def git_bytes(ref,path)
  b=IO.popen(['git','show',ref+':'+path],'rb',&:read)
  abort('Git pin read failed: '+path) unless $?.success?
  b
end
seal.fetch('science_files').each do |row|
  b=git_bytes(seal['commit'],row['path'])
  abort('Original science not preserved: '+row['path']) unless b.bytesize==row['bytes'] && Digest::SHA256.hexdigest(b)==row['sha256']
end
corrected.fetch('science_files').each do |row|
  path=row.fetch('path'); b=File.binread(path); hash=Digest::SHA256.hexdigest(b)
  abort('Science changed: '+path) unless b.bytesize==row['bytes'] && hash==row['sha256']
  abort('Pre-run bytes differ: '+path) unless b==git_bytes(corrected['commit'],path)
  abort('Science ledger differs: '+path) unless ledger[path]==hash
end
inputs.fetch('sources').each do |row|
  b=git_bytes(row['ref'],row['path'])
  abort('Source changed: '+row['path']) unless b.bytesize==row['bytes'] && Digest::SHA256.hexdigest(b)==row['sha256']
end
abort('Raw root wrong') unless File.basename(raw)==receipts['raw_directory_basename']
receipts.fetch('captures').each do |stem,wanted|
  actual=JSON.parse(File.read(File.join(raw,stem+'.json'),encoding:'UTF-8'))
  b=File.binread(File.join(raw,stem+'.log'))
  abort('Raw byte mismatch: '+stem) unless b.bytesize==actual['log_bytes'] && Digest::SHA256.hexdigest(b)==actual['log_sha256']
  normalized=Marshal.load(Marshal.dump(actual))
  normalized['command']=normalized['command'].map{|v|v.gsub(raw,'<raw-root>').gsub(%r{/Users/[^/]+/\.pyenv/versions/3\.12\.1},'<python3.12-env>')}
  abort('Receipt mismatch: '+stem) unless wanted==normalized
  target=receipts.fetch('public_logs')[stem]
  if target
    abort('Published log mismatch: '+stem) unless b==File.binread(File.join(base,target))
  else
    abort('Unregistered raw-only: '+stem) unless receipts.fetch('raw_only').include?(stem)
  end
  expected=stem.start_with?('governance_') ? 1 : 0
  abort('Wrong exit: '+stem) unless actual['exit_code']==expected && actual['signal'].nil?
end
abort('Server differs') unless File.read(File.join(raw,'server_seal.log')).split.first==seal['commit']
abort('Corrected server differs') unless File.read(File.join(raw,'server_corrected.log')).split.first==corrected['commit']
native=File.readlines(File.join(raw,'native_first.log'),encoding:'UTF-8').map{|l|JSON.parse(l)}
summary=native.last
abort('Native summary differs') unless summary==receipts['native_summary'] && summary['passed']==81 && summary['total']==81 && summary['failed']==[]
joins=native.select{|row|row.fetch('group','').start_with?('join_')}
abort('Actual join population differs') unless joins.map{|row|row['character']}==[[0,1],[1,1],[1,0]] && joins.all?{|row|row['algebra_dimension']==25 && row['checks'].values.all?}
%w[physical_goal_achieved generated_SM_selection physical_chirality_derived non_author_acceptance quantum_moduli_lifting_computed].each do |field|
  abort('Unlicensed acceptance: '+field) unless summary[field]==false
end
ref=JSON.parse(File.read(File.join(raw,'reference_first.log'),encoding:'UTF-8'))
small=ref.reject{|k,v|k=='checks'}
abort('Reference differs') unless small==receipts['reference_summary'] && ref['passed']==65 && ref['total']==65 && ref['failed']==[] && ref['checks'].length==65 && ref['checks'].values.all? && ref['all_actual_characters']==3
abort('Focused differs') unless File.read(File.join(raw,'focused_first.log')).match?(/18 passed in [0-9.]+s/)
cn=JSON.parse(File.readlines(File.join(raw,'native_corrected.log'),encoding:'UTF-8').last)
abort('Corrected native differs') unless cn==receipts['corrected_native_summary'] && cn['passed']==83 && cn['total']==83 && cn['failed']==[]
%w[physical_goal_achieved generated_SM_selection physical_chirality_derived non_author_acceptance quantum_moduli_lifting_computed].each do |field|
  abort('Corrected unlicensed acceptance: '+field) unless cn[field]==false
end
cr=JSON.parse(File.read(File.join(raw,'reference_corrected.log'),encoding:'UTF-8'))
abort('Corrected reference differs') unless cr.reject{|k,v|k=='checks'}==receipts['corrected_reference_summary'] && cr['passed']==67 && cr['total']==67 && cr['failed']==[] && cr['checks'].length==67 && cr['checks'].values.all?
abort('Corrected focused differs') unless File.read(File.join(raw,'focused_corrected.log')).match?(/18 passed in [0-9.]+s/)
receipts.fetch('custody_checks',{}).each do |stem,row|
  actual=JSON.parse(File.read(File.join(raw,stem+'.json'),encoding:'UTF-8'))
  b=File.binread(File.join(raw,stem+'.log'))
  normalized=Marshal.load(Marshal.dump(actual))
  normalized['command']=normalized['command'].map{|v|v.gsub(raw,'<raw-root>')}
  abort('Custody snapshot differs') unless normalized==row['receipt'] && actual['exit_code']==0 && actual['signal'].nil? && b.bytesize==actual['log_bytes'] && Digest::SHA256.hexdigest(b)==actual['log_sha256'] && b==File.binread(File.join(base,row['public_log']))
end
puts JSON.generate(original_science_files:seal['science_files'].length,corrected_science_files:corrected['science_files'].length,input_pins:inputs['sources'].length,
                   raw_captures:receipts['captures'].length,original_native:81,original_reference:65,
                   corrected_native:83,corrected_reference:67,focused:18,
                   actual_joins:3,bytes_and_exits_match:true,analytic_admission_independently_verified:false,
                   non_author_acceptance:false,physical_goal_achieved:false)
