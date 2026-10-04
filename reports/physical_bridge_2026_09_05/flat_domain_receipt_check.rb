# Metadata/byte/exit custody check, not mathematical or physical certification.
require 'json'
require 'digest'

base = File.dirname(__FILE__)
repo = File.expand_path('../..', base)
Dir.chdir(repo)
seal = JSON.parse(File.read(File.join(base, 'FLAT_DOMAIN_SEAL.json'), encoding: 'UTF-8'))
inputs = JSON.parse(File.read(File.join(base, 'FLAT_DOMAIN_INPUTS.json'), encoding: 'UTF-8'))
intake = JSON.parse(File.read(File.join(base, 'FLAT_DOMAIN_INTAKE.json'), encoding: 'UTF-8'))
receipts = JSON.parse(File.read(File.join(base, 'FLAT_DOMAIN_RECEIPTS.json'), encoding: 'UTF-8'))
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
  abort('science byte mismatch: ' + p) unless sha == r['sha256'] && raw.bytesize == r['bytes']
  abort('science ledger mismatch: ' + p) unless latest[p] == sha
  abort('science commit mismatch: ' + p) unless raw == git_bytes(seal.fetch('scientific_commit'), p)
end
sources = inputs.fetch('sources') + intake.fetch('sources').map { |r| r.merge('ref' => intake.fetch('ref')) }
sources.each do |r|
  raw = r['ref'] ? git_bytes(r['ref'], r['path']) : File.binread(r['path'])
  abort('source mismatch: ' + r['path']) unless Digest::SHA256.hexdigest(raw) == r['sha256']
end
receipts.fetch('captures').each do |stem, expected|
  actual = JSON.parse(File.read(File.join(raw_root, stem + '.json'), encoding: 'UTF-8'))
  abort('capture receipt changed: ' + stem) unless actual == expected
  log = File.binread(File.join(raw_root, stem + '.log'))
  abort('capture bytes/hash changed: ' + stem) unless log.bytesize == actual['log_bytes'] && Digest::SHA256.hexdigest(log) == actual['log_sha256']
  published = receipts.fetch('public_logs')[stem]
  abort('public log missing: ' + stem) unless published
  abort('public log differs: ' + stem) unless File.binread(File.join(base, published)) == log
  want = stem == 'governance_final' ? 1 : 0
  abort('unexpected captured exit: ' + stem) unless actual['exit_code'] == want && actual['signal'].nil?
end
native_lines = File.readlines(File.join(raw_root, 'native_first.log'), encoding: 'UTF-8').grep(/^\{/).map { |l| JSON.parse(l) }
predicates = native_lines.select { |r| r.key?('pass') }
native = native_lines.last
abort('native predicates/report mismatch') unless predicates.length == 181 && predicates.all? { |r| r['pass'] == true } && native == receipts['native_summary'].merge('rows' => native.fetch('rows'))
abort('physical completion overclaimed') unless native['physics_derived'] == false && native['source_domain_generated'] == false
reference = JSON.parse(File.readlines(File.join(raw_root, 'reference_first.log'), encoding: 'UTF-8').last)
abort('reference summary mismatch') unless reference.reject { |k, _| k == 'rows' } == receipts['reference_summary'] && reference['passed'] == 100
focused = File.read(File.join(raw_root, 'focused_first.log'), encoding: 'UTF-8')
abort('focused population mismatch') unless focused.match?(/16 passed in [0-9.]+s/)
puts JSON.generate(science_files: seal['science_files'].length, source_pins: sources.length,
                   raw_captures: receipts['captures'].length, native: 181, reference: 100, focused: 16,
                   bytes_and_exits_match: true, mathematical_review: false, physics_derived: false)
