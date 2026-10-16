# Lossless custody of completed staged checks; never rerun or rewrite their results.
require 'json'
require 'digest'
require 'zlib'
require 'stringio'
require 'open3'
raw = File.expand_path(ARGV.fetch(0))
repo = File.expand_path('../../..', __dir__)
dest = File.join(__dir__, 'results_phase8_prechecks')
abort('refusing overwrite') if File.exist?(dest)
git = lambda do |*args|
  out, err, status = Open3.capture3('git', '-C', repo, *args)
  abort(err) unless status.success?
  out
end
packets = {
  'phase7-publication' => '47cdde88b',
  'phase8-design' => '98d614113',
  'phase8-source' => 'b20a3280d'
}.map do |prefix, short|
  captures = %w[before governance after].to_h do |kind|
    stem = File.join(raw, prefix + '-' + kind + '-first')
    bytes = File.binread(stem + '.log')
    receipt_bytes = File.binread(stem + '.json')
    receipt = JSON.parse(receipt_bytes)
    abort('capture custody mismatch') unless Digest::SHA256.hexdigest(bytes) == receipt.fetch('log_sha256') &&
      bytes.bytesize == receipt.fetch('log_bytes') && receipt.fetch('signal').nil?
    abort('unexpected exit') unless receipt.fetch('exit_code') == (kind == 'governance' ? 1 : 0)
    [kind, [bytes, receipt, receipt_bytes]]
  end
  abort('tracked envelope changed') unless captures['before'][0] == captures['after'][0]
  state = JSON.parse(captures['before'][0])
  result = JSON.parse(captures['governance'][0]).fetch('results')
  abort('wrong gate population') unless result.size == 30 &&
    result.reject { |_, v| v[0] }.keys == ['seal-provenance']
  historical = result.fetch('seal-provenance')[1].fetch('problems')
  abort('historical population changed') unless historical.size == 643 &&
    historical.group_by { |r| r.fetch('status') }.transform_values(&:size) ==
      { 'unclassified' => 562, 'historical_noncompliant' => 5, 'missing_fields' => 76 }
  commit = git.call('rev-parse', short).strip
  index_bytes = git.call('ls-tree', '-r', '-z', commit).split("\0").map do |row|
    meta, path = row.split("\t", 2)
    mode, type, blob = meta.split(' ')
    abort('nonblob staged artifact') unless type == 'blob'
    "#{mode} #{blob} 0\t#{path}\0"
  end.join
  abort('staged tree does not equal published commit') unless
    Digest::SHA256.hexdigest(index_bytes) == state.fetch('index_sha256')
  [prefix, commit, captures, state]
end
Dir.mkdir(dest)
write = lambda { |name, bytes| File.open(File.join(dest, name), 'wx') { |f| f.binmode; f.write(bytes) } }
custody = []
packets.each do |prefix, commit, captures, state|
  stream = StringIO.new(''.b)
  zipper = Zlib::GzipWriter.new(stream); zipper.mtime = 0
  zipper.write(captures['before'][0]); zipper.close
  compressed = stream.string
  abort('state roundtrip') unless Zlib::GzipReader.new(StringIO.new(compressed)).read.b == captures['before'][0]
  state_path = prefix + '-before-and-after.log.gz'
  write.call(state_path, compressed)
  governance_path = prefix + '-governance.log'
  write.call(governance_path, captures['governance'][0])
  captures.each do |kind, (_, receipt, original)|
    shown = receipt.merge('command' => receipt.fetch('command').map do |s|
      normalized = s.gsub(raw, '<workspace>')
      normalized.end_with?('/bin/python3') ? '[PROJECT_PYTHON]' : normalized
    end, 'presentation' => 'Command paths normalized; original receipt bytes retained locally.',
      'original_receipt_sha256' => Digest::SHA256.hexdigest(original))
    write.call(prefix + '-' + kind + '.json', JSON.pretty_generate(shown) + "\n")
  end
  custody << { 'prefix' => prefix, 'published_staged_commit' => commit,
    'precheck_head' => state.fetch('head'), 'tracked_files' => state.fetch('tracked_count'),
    'source_pins' => state.fetch('source_pins').size,
    'index_sha256' => state.fetch('index_sha256'), 'before_after_identical' => true,
    'state_path' => state_path, 'state_sha256' => Digest::SHA256.hexdigest(compressed),
    'uncompressed_state_sha256' => Digest::SHA256.hexdigest(captures['before'][0]),
    'governance_path' => governance_path,
    'governance_sha256' => Digest::SHA256.hexdigest(captures['governance'][0]),
    'pass' => 29, 'fail' => 1, 'historical_problems' => 643 }
end
files = Dir.children(dest).sort.map do |name|
  { 'path' => name, 'bytes' => File.size(File.join(dest, name)),
    'sha256' => Digest::SHA256.file(File.join(dest, name)).hexdigest }
end
write.call('CUSTODY.json', JSON.pretty_generate({ 'grade' => 'Completed maintenance checks, not scientific admission',
  'packets' => custody, 'files' => files }) + "\n")
puts JSON.pretty_generate(custody)
