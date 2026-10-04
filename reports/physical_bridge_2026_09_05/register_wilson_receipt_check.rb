# Byte and exit custody, not mathematical or physical certification.
require 'json'
require 'digest'

base = File.dirname(__FILE__)
repo = File.expand_path('../..', base)
Dir.chdir(repo)
seal = JSON.parse(File.read(File.join(base, 'REGISTER_WILSON_SEAL.json'), encoding: 'UTF-8'))
inputs = JSON.parse(File.read(File.join(base, 'REGISTER_WILSON_INPUTS.json'), encoding: 'UTF-8'))
receipts = JSON.parse(File.read(File.join(base, 'REGISTER_WILSON_RECEIPTS.json'), encoding: 'UTF-8'))
raw_root = ARGV[0] || receipts.fetch('raw_root')
latest = {}
File.read(File.join(base, 'ARTIFACT_HASHES.txt'), encoding: 'UTF-8').each_line do |line|
  m = line.match(/^([0-9a-f]{64})  (.+)$/)
  latest[m[2]] = m[1] if m
end
def git_bytes(ref, path)
  raw = IO.popen(['git', 'show', ref + ':' + path], 'rb', &:read)
  abort('git show failed: ' + path) unless $?.success?
  raw
end
seal.fetch('science_files').each do |r|
  p = r.fetch('path')
  raw = File.binread(p)
  sha = Digest::SHA256.hexdigest(raw)
  abort('science bytes mismatch: ' + p) unless sha == r['sha256'] && raw.bytesize == r['bytes']
  abort('science ledger mismatch: ' + p) unless latest[p] == sha
  abort('science commit mismatch: ' + p) unless raw == git_bytes(seal.fetch('scientific_commit'), p)
end
inputs.fetch('sources').each do |r|
  raw = r['ref'] ? git_bytes(r['ref'], r['path']) : File.binread(r['path'])
  abort('source mismatch: ' + r['path']) unless Digest::SHA256.hexdigest(raw) == r['sha256']
end
receipts.fetch('captures').each do |stem, expected|
  actual = JSON.parse(File.read(File.join(raw_root, stem + '.json'), encoding: 'UTF-8'))
  abort('capture receipt changed: ' + stem) unless actual == expected
  raw = File.binread(File.join(raw_root, stem + '.log'))
  abort('capture hash changed: ' + stem) unless raw.bytesize == actual['log_bytes'] && Digest::SHA256.hexdigest(raw) == actual['log_sha256']
  published = receipts.fetch('public_logs')[stem]
  if published
    abort('public log differs: ' + stem) unless File.binread(File.join(base, published)) == raw
  else
    abort('undisclosed raw-only capture: ' + stem) unless receipts.fetch('raw_only').include?(stem)
  end
  want = if %w[whitespace_repeat whitespace_raw_only].include?(stem)
           2
         elsif %w[already_banked governance_first governance_final].include?(stem)
           1
         else
           0
         end
  abort('unexpected captured exit: ' + stem) unless actual['exit_code'] == want && actual['signal'].nil?
end
server = File.read(File.join(raw_root, 'server_seal.log'), encoding: 'UTF-8').split.first
abort('server seal mismatch') unless server == seal.fetch('scientific_commit')
lines = File.readlines(File.join(raw_root, 'native_first.log'), encoding: 'UTF-8').map { |l| JSON.parse(l) }
predicates = lines.select { |r| r.key?('pass') }
native = lines.last
abort('native population/result mismatch') unless predicates.length == 77 && predicates.all? { |r| r['pass'] == true } && native == receipts.fetch('native_summary')
abort('physical completion overclaimed') unless native['source_generated'] == false && native['physical_chirality_derived'] == false && native['quantum_measure_derived'] == false && native['full_goal_achieved'] == false
reference = JSON.parse(File.readlines(File.join(raw_root, 'reference_first.log'), encoding: 'UTF-8').last)
abort('reference result mismatch') unless reference == receipts.fetch('reference_summary') && reference['passed'] == 371 && reference['total'] == 371
focused = File.read(File.join(raw_root, 'focused_first.log'), encoding: 'UTF-8')
abort('focused population mismatch') unless focused.match?(/18 passed in [0-9.]+s/)
puts JSON.generate(science_files: seal['science_files'].length, source_pins: inputs['sources'].length,
                   raw_captures: receipts['captures'].length, native: 77, reference: 371, focused: 18,
                   bytes_and_exits_match: true, mathematical_review: false, physics_derived: false)
