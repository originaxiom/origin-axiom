# Complete state snapshot BEFORE launch, and after terminal completion.
require 'json'
require 'digest'
require 'pathname'
require 'open3'
root=Pathname.new(__dir__).parent.parent.parent
mode=ARGV.fetch(0);leaf=ARGV.fetch(1,mode)
raise 'Simple capture leaf required' unless leaf.match?(/\A[a-zA-Z0-9_-]+\z/)
out=Pathname.new(__dir__).join('results',leaf);Dir.mkdir(out)
python=ENV.fetch('OA_TRANSPORT_PYTHON','python3');deps=ENV.fetch('OA_TRANSPORT_DEPENDENCIES','')
command=case mode
when 'regression' then [python,'-B','-m','pytest','-q','-p','no:cacheprovider','tests/test_physical_bridge_surface_actual_tube.py']
when 'governance' then [python,'-B','scripts/gates/gates.py']
else raise 'Unrecognized capture mode'
end
pins=JSON.parse(File.read(Pathname.new(__dir__).join('INPUTS.json'))).fetch('source_files')
state=lambda do
 names,status=Open3.capture2('git','ls-files','-z',chdir:root.to_s)
 raise 'tracked inventory failed' unless status.success?
 tree=names.split("\0").sort.map{|p|[p,Digest::SHA256.file(root.join(p)).hexdigest]}
 index,status=Open3.capture2('git','ls-files','--stage','-z',chdir:root.to_s)
 raise 'index inventory failed' unless status.success?
 {'tracked_files'=>tree.length,'tree_sha256'=>Digest::SHA256.hexdigest(JSON.generate(tree)),
  'index_sha256'=>Digest::SHA256.hexdigest(index),
  'pins'=>pins.map{|r|[r['path'],Digest::SHA256.file(root.join(r['path'])).hexdigest]}}
end
before=state.call
raise 'Pin mismatch before launch' unless before['pins'].all?{|p,h|pins.find{|r|r['path']==p}['sha256']==h}
File.write(out.join('before.json'),JSON.pretty_generate(before)+"\n")
start=Process.clock_gettime(Process::CLOCK_MONOTONIC)
stdout,stderr,status=Open3.capture3({'PYTHONDONTWRITEBYTECODE'=>'1','PYTHONPATH'=>deps},*command,chdir:root.to_s)
seconds=Process.clock_gettime(Process::CLOCK_MONOTONIC)-start
File.write(out.join('stdout.log'),stdout);File.write(out.join('stderr.log'),stderr)
after=state.call;File.write(out.join('after.json'),JSON.pretty_generate(after)+"\n")
receipt={'mode'=>mode,'capture_leaf'=>leaf,'command'=>command.map{|p|p==python ? 'PYTHON3.12.14' : p},
 'exit_code'=>status.exitstatus,'seconds'=>seconds,'before_completed_before_launch'=>true,
 'state_unchanged'=>before==after,'tracked_files'=>before['tracked_files'],'source_pins'=>pins.length,
 'tree_sha256'=>before['tree_sha256'],'index_sha256'=>before['index_sha256'],
 'stdout'=>{'bytes'=>stdout.bytesize,'sha256'=>Digest::SHA256.hexdigest(stdout)},
 'stderr'=>{'bytes'=>stderr.bytesize,'sha256'=>Digest::SHA256.hexdigest(stderr)}}
File.write(out.join('RECEIPT.json'),JSON.pretty_generate(receipt)+"\n")
puts JSON.pretty_generate(receipt);puts stdout if mode=='regression'
exit(status.success? && before==after ? 0 : 1)
