# Byte/source/exit custody, not science or independent analytic acceptance.
require 'json'
require 'digest'
require 'open3'
base=File.dirname(__FILE__)
repo=File.expand_path('../../..',base)
mode,raw,commit=ARGV
abort('preflight|final RAW SEAL_COMMIT required') unless %w[preflight final].include?(mode) && raw && commit
read=lambda{|p|JSON.parse(File.read(p,encoding:'UTF-8'))}
inputs=read.call(File.join(base,'INPUTS.json'))
seal=read.call(File.join(base,'PRESEAL.json'))
inputs.fetch('sources').each do |row|
  bytes,error,status=Open3.capture3('git','-C',repo,'show',row['ref']+':'+row['path'])
  abort('source mismatch '+row['path']) unless status.success? && bytes.bytesize==row['bytes'] && Digest::SHA256.hexdigest(bytes)==row['sha256']
end
seal.fetch('science_files').each do |row|
  bytes=File.binread(File.join(repo,row['path']))
  old,error,status=Open3.capture3('git','-C',repo,'show',commit+':'+row['path'])
  abort('science mismatch '+row['path']) unless status.success? && old.b==bytes && bytes.bytesize==row['bytes'] && Digest::SHA256.hexdigest(bytes)==row['sha256']
end
abort('server seal differs') unless File.read(File.join(raw,'server_seal.log')).split.first==commit
if mode=='final'
  %w[native reference focused].each do |stem|
    rec=read.call(File.join(raw,stem+'.json'));bytes=File.binread(File.join(raw,stem+'.log'))
    abort('failed/changed capture '+stem) unless rec['exit_code']==0 && rec['signal'].nil? && rec['log_bytes']==bytes.bytesize && rec['log_sha256']==Digest::SHA256.hexdigest(bytes)
    if stem=='focused'
      abort('wrong selected tests') unless bytes.match?(/10 passed in [0-9.]+s/)
    else
      data=JSON.parse(bytes)
      abort('failed/overclaimed science') unless data['checks'].size>0 && data['checks'].values.all?{|v|v==true} && data['failed']==[] && data['passed']==data['checks'].size && data['physical_kernel_computed']==false && data['full_superfield_domain_closed']==false && data['physical_goal_achieved']==false && data['non_author_acceptance']==false
      if stem=='native'
        abort('wrong native parent/population') unless data['profiles'].size==4 && data['parent']['allowed_dimension']==992
      else
        abort('wrong reference population') unless data['finite_symbol_directions']==96 && data['helicities']==2 && data['coefficient_patterns']==2
      end
    end
  end
end
puts JSON.generate(mode:mode,source_pins:inputs['sources'].size,science_files:seal['science_files'].size,bytes_unchanged:true,physical_goal_achieved:false,non_author_acceptance:false)
