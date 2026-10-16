# Execution-only successor; all scientific/test source pins are unchanged.
require 'json'
require 'digest'
require 'open3'

python, raw_arg, expected_head = ARGV
abort('Usage: execute.rb EXISTING_PYTHON EMPTY_SCRATCH PUBLISHED_HEAD') unless
  python && raw_arg && expected_head && ARGV.size == 3
repo = File.expand_path('../../..', __dir__)
raw = File.realpath(raw_arg)
abort('scratch must be an empty directory outside the repository') unless
  File.directory?(raw) && Dir.children(raw).empty? && !raw.start_with?(repo + '/') && raw != repo
abort('Python executable must exist') unless File.file?(python) && File.executable?(python)
inputs = JSON.parse(File.read(File.join(__dir__, 'INPUTS.json')))
base = __dir__.delete_prefix(repo + '/')
git = lambda do |*args|
  out, err, status = Open3.capture3('git', '-C', repo, *args)
  abort(err) unless status.success?
  out
end
snapshot = lambda do
  files = git.call('ls-files', '-z').split("\0").sort.to_h do |path|
    full = File.join(repo, path)
    [path, File.symlink?(full) ? ['symlink', File.readlink(full)] :
      [File.size(full), Digest::SHA256.file(full).hexdigest]]
  end
  pins = inputs.fetch('source_files').to_h do |row|
    [row.fetch('path'), Digest::SHA256.file(File.join(repo, row.fetch('path'))).hexdigest]
  end
  { 'head' => git.call('rev-parse', 'HEAD').strip, 'files' => files, 'pins' => pins,
    'index_sha256' => Digest::SHA256.hexdigest(git.call('ls-files', '--stage', '-z')) }
end
before = snapshot.call
abort('source head differs from published argument') unless before['head'] == expected_head
abort('tracked/index edits before execution') unless git.call('diff', '--name-only', 'HEAD').empty?
abort('original pins changed') unless inputs.fetch('source_files').all? do |row|
  before['pins'][row.fetch('path')] == row.fetch('sha256')
end
File.open(File.join(raw, 'before.json'), 'wx') { |f| f.write(JSON.pretty_generate(before) + "\n") }
commands = {
  'focused' => [python, '-B', '-m', 'pytest', '-q', '--noconftest', '-p', 'no:cacheprovider', '-o', 'addopts=',
    'tests/test_physical_bridge_family_domain.py::test_original_mathematical_lock_with_exact_domain',
    'tests/test_physical_bridge_family_domain.py::test_delegated_sealed_lock_rejects_changed_computed_result',
    'tests/test_physical_bridge_quantum_shift.py::test_vector_and_complex_Weyl_mass_derivatives',
    'tests/test_physical_bridge_quantum_shift.py::test_mass_derivative_predicate_has_positive_and_rejecting_controls'],
  'metadata_capture' => ['ruby', '-EUTF-8', base + '/inventory.rb', File.join(raw, 'metadata_payload.json')],
  'vacuity' => [python, '-B', 'scripts/checks/check_test_vacuity.py'],
  'relay' => [python, '-B', 'scripts/checks/relay_debt.py'],
  'governance' => [python, '-B', 'scripts/gates/gates.py']
}
names = commands.keys.flat_map { |name| [name + '.log', name + '.json',
  name + '.capture.stdout.log', name + '.capture.stderr.log'] } +
  %w[metadata_payload.json before.json after.json RUN.json environment.json]
abort('case-insensitive output collision') unless names.map(&:downcase).uniq.size == names.size
env = { 'PYTHONDONTWRITEBYTECODE' => '1', 'PYTHONPATH' => nil }
metadata_code = 'import sys, json, importlib.metadata as m, importlib.util as u; ' \
  'print(json.dumps({"python":sys.version,"executable":sys.executable,' \
  '"packages":{n:{"version":m.version(n),"origin":u.find_spec(n).origin}' \
  ' for n in ["scipy","numpy","sympy","pytest"]}},indent=2))'
metadata, metadata_error, metadata_status = Open3.capture3(env, python, '-B', '-c', metadata_code, chdir: repo)
File.open(File.join(raw, 'environment.json'), 'wx') { |f| f.write(metadata) }
abort('environment metadata failed: ' + metadata_error) unless metadata_status.success?
jobs = commands.map do |name, command|
  Thread.new do
    out, err, status = Open3.capture3(env, 'ruby', '-EUTF-8',
      File.join(repo, 'reports/physical_bridge_2026_09_05/capture_checked_run.rb'),
      File.join(raw, name), *command, chdir: repo)
    File.open(File.join(raw, name + '.capture.stdout.log'), 'wx') { |f| f.write(out) }
    File.open(File.join(raw, name + '.capture.stderr.log'), 'wx') { |f| f.write(err) }
    [name, status.exitstatus]
  end
end
exits = jobs.map(&:value).to_h
after = snapshot.call
File.open(File.join(raw, 'after.json'), 'wx') { |f| f.write(JSON.pretty_generate(after) + "\n") }
receipt = { 'source_head' => before['head'], 'pins' => before['pins'].size,
  'tracked_files' => before['files'].size, 'tree_index_pins_unchanged' => before == after,
  'exit_codes' => exits, 'before_sha256' => Digest::SHA256.file(File.join(raw, 'before.json')).hexdigest,
  'after_sha256' => Digest::SHA256.file(File.join(raw, 'after.json')).hexdigest,
  'new_scientific_experiment' => false, 'full_suite_run' => false, 'physical_goal_achieved' => false }
receipt['expected_maintenance_outcomes'] = before == after &&
  %w[focused metadata_capture vacuity].all? { |name| exits[name] == 0 }
File.open(File.join(raw, 'RUN.json'), 'wx') { |f| f.write(JSON.pretty_generate(receipt) + "\n") }
puts JSON.pretty_generate(receipt)
exit(receipt['expected_maintenance_outcomes'] ? 0 : 1)
