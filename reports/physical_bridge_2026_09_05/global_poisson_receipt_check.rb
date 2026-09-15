# Read-only R31 custody, not independent mathematical verification.
require 'json'
require 'digest'
require 'open3'
require 'pathname'
abort('Usage: ruby global_poisson_receipt_check.rb RAW_CAPTURE_DIRECTORY') unless ARGV.size == 1
raw = Pathname.new(ARGV[0])
prefix = 'reports/physical_bridge_2026_09_05/'
def need(ok, why)
  abort(why) unless ok
end
def red(s)
  s.gsub('../../../../.pyenv/versions/3.12.1', '<python3.12-env>')
   .gsub('/Users/dri/.pyenv/versions/3.12.1', '<python3.12-env>')
   .gsub(Dir.pwd, '<repo>')
end
old_out, old_err, old_status = Open3.capture3('ruby', '-EUTF-8:UTF-8', prefix+'resolved_fermion_receipt_check.rb', raw.to_s)
need(old_status.success?, old_err + old_out)
old_custody = JSON.parse(old_out)
paths = %w[GLOBAL_POISSON_DESIGN.md GLOBAL_POISSON_PROOF.md GLOBAL_POISSON_PRIOR.md GLOBAL_POISSON_RETRIEVAL.json GLOBAL_POISSON_SOURCES.json global_poisson.py global_poisson_history_scan.rb].map { |s| prefix+s }
paths << 'tests/test_physical_bridge_global_poisson.py'
paths.each do |path|
  bytes, error, status = Open3.capture3('git', 'show', 'bd5009c4e5037513fd139ecc23e6302e526c863f:'+path)
  need(status.success?, error)
  need(Digest::SHA256.hexdigest(bytes) == Digest::SHA256.file(path).hexdigest, 'R31 changed after seal: '+path)
end
data = JSON.parse(File.read(prefix+'GLOBAL_POISSON_RUN_RECEIPTS.json', encoding: 'UTF-8'))
runs = data.fetch('runs').values + data.fetch('audit_runs').values
runs.each do |run|
  stem = raw.join(run.fetch('raw_basename')).to_s
  bytes = File.read(stem+'.log', encoding: 'UTF-8')
  receipt = JSON.parse(File.read(stem+'.json', encoding: 'UTF-8'))
  need(Digest::SHA256.file(stem+'.json').hexdigest == run.fetch('raw_receipt_sha256'), 'R31 raw receipt changed')
  need(bytes.bytesize == receipt.fetch('log_bytes') && Digest::SHA256.hexdigest(bytes) == receipt.fetch('log_sha256'), 'R31 raw log changed')
  receipt['command'] = receipt.fetch('command').map { |s| red(s) }
  need(receipt == run.fetch('receipt'), 'R31 published receipt differs')
  next unless run['public_path']
  need(File.read(run['public_path'], encoding: 'UTF-8') == red(bytes), 'R31 output changed beyond declared redaction')
  need(Digest::SHA256.file(run['public_path']).hexdigest == run.fetch('public_sha256'), 'R31 public output digest differs')
end
population = data.fetch('history_population')
history_path = raw.join(population.fetch('raw_basename')).to_s
need(File.size(history_path) == population.fetch('bytes') && Digest::SHA256.file(history_path).hexdigest == population.fetch('sha256'), 'R31 history population changed')
old = JSON.parse(File.read(prefix+'RESOLVED_FERMION_RUN_RECEIPTS.json'))['runs']['broad_first']['receipt']['command'].select { |s| s.start_with?('tests/') }
now = data['runs']['broad_first']['receipt']['command'].select { |s| s.start_with?('tests/') }
added = %w[tests/test_physical_bridge_resolved_fermion_c3_control.py tests/test_physical_bridge_global_poisson.py]
need(old.size == 52 && now.size == 54 && now == old+added, 'R31 broad population differs')
ids = lambda { |p| File.readlines(p, encoding: 'UTF-8').select { |s| s.start_with?('FAILED ', 'ERROR ') }.map(&:strip).sort }
old_ids = ids.call(prefix+'RESOLVED_FERMION_REGRESSION.txt')
new_ids = ids.call(prefix+'GLOBAL_POISSON_REGRESSION.txt')
need(old_ids.size == 24 && old_ids == new_ids, 'R31 broad failed/error IDs changed')
need(data['old_failed_error_ids'] == old_ids && data['new_failed_error_ids'] == new_ids, 'R31 published failure inventory differs')
native = JSON.parse(File.read(prefix+'GLOBAL_POISSON_NATIVE_FIRST.json'))
need(native.fetch('all_checks_pass') && native.fetch('checks').size == 12 && native['checks'].values.all? { |v| v == true }, 'Wrong native outcome receipt')
need(File.read(prefix+'GLOBAL_POISSON_TESTS_FIRST.txt').include?('47 passed'), 'Wrong new-test outcome receipt')
need(File.read(prefix+'GLOBAL_POISSON_FOCUSED_FIRST.txt').include?('115 passed'), 'Wrong focused outcome receipt')
need(File.read(prefix+'GLOBAL_POISSON_REGRESSION.txt').include?('16 failed, 508 passed, 1 warning, 8 errors'), 'Wrong broad outcome receipt')
puts JSON.generate(old_custody: old_custody, unchanged_r31_science_paths: paths.size,
  r31_raw_captures: runs.size, r31_public_copies: data['runs'].size,
  r31_broad_test_files: now.size, unchanged_failed_error_ids: new_ids.size,
  history_population_verified: true,
  scope: 'Byte custody and fixed-population outcomes, not a fresh science execution, proof review or full green.')
