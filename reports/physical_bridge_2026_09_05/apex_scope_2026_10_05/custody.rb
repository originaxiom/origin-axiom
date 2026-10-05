# Non-scientific custody, with fail-closed full census readout.
require 'json'
require 'digest'
require 'open3'
base=File.dirname(__FILE__)
repo=File.expand_path('../../..',base)
mode,raw,commit=ARGV
abort('preflight|final RAW SEAL_COMMIT required') unless %w[preflight final].include?(mode) && raw && commit
read=lambda{|path|JSON.parse(File.read(path,encoding:'UTF-8'))}
seal=read.call(File.join(base,'PRESEAL.json'))
inputs=read.call(File.join(base,'INPUTS.json'))
seal.fetch('science_files').each do |row|
  bytes=File.binread(File.join(repo,row.fetch('path')))
  old,error,status=Open3.capture3('git','-C',repo,'show',commit+':'+row.fetch('path'))
  abort('science mismatch '+row['path']) unless status.success? && old.b==bytes && bytes.bytesize==row['bytes'] && Digest::SHA256.hexdigest(bytes)==row['sha256']
end
inputs.fetch('sources').each do |row|
  bytes,error,status=Open3.capture3('git','-C',repo,'show',row['ref']+':'+row['path'])
  abort('source mismatch '+row['path']) unless status.success? && bytes.bytesize==row['bytes'] && Digest::SHA256.hexdigest(bytes)==row['sha256']
end
abort('server seal differs') unless File.read(File.join(raw,'server_seal.log')).split.first==commit
if mode=='final'
  a,b=%w[native reference].map do |stem|
    receipt=read.call(File.join(raw,stem+'.json'))
    bytes=File.binread(File.join(raw,stem+'.log'))
    abort('capture changed '+stem) unless receipt['exit_code']==0 && receipt['signal'].nil? && bytes.bytesize==receipt['log_bytes'] && Digest::SHA256.hexdigest(bytes)==receipt['log_sha256']
    data=JSON.parse(bytes)
    abort('failed science '+stem) unless data['checks'].size>0 && data['checks'].values.all?{|v|v==true} && data['failed']==[] && data['passed']==data['checks'].size && data['total']==data['checks'].size
    abort('physical overclaim '+stem) unless data['physical_goal_achieved']==false && data['non_author_acceptance']==false
    data
  end
  key=lambda{|row|[row.fetch('six'),row.fetch('a'),row.fetch('b'),row.fetch('char')]}
  maps=[a,b].map do |data|
    rows=data.fetch('rows')
    abort('duplicate or incomplete rows') unless rows.size==1152 && rows.map{|row|key.call(row)}.uniq.size==1152
    abort('missing or equal witness') unless rows.all?{|row|row['witness'].is_a?(String) && row['witness'].size.between?(1,6) && row['trace']!=row['deck_trace']}
    rows.to_h{|row|[key.call(row),row]}
  end
  abort('reference semantic census differs') unless maps[0]==maps[1] && a['rank_cases']==b['rank_cases']
  tests=read.call(File.join(raw,'focused.json'))
  abort('focused tests failed') unless tests['exit_code']==0 && tests['signal'].nil?
  bytes=File.binread(File.join(raw,'focused.log'))
  abort('focused capture changed') unless bytes.bytesize==tests['log_bytes'] && Digest::SHA256.hexdigest(bytes)==tests['log_sha256']
  abort('focused incomplete') unless bytes.match?(/8 passed in [0-9.]+s/)
end
puts JSON.generate(mode:mode,science_files:seal['science_files'].size,source_pins:inputs['sources'].size,science_unchanged:true,source_bytes_match:true,non_author_acceptance:false,physical_goal_achieved:false)
