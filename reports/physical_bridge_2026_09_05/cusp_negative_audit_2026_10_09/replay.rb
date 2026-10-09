# Extract pinned upstream bytes, never overwrite its saved output in the repo.
require 'json'
require 'digest'
require 'open3'
base = File.dirname(__FILE__)
repo = File.expand_path('../../..', base)
raw, seal = ARGV
abort('fresh empty RAW directory and pushed seal required') unless raw && seal && File.directory?(raw) && Dir.children(raw).empty?
manifest = JSON.parse(File.read(File.join(base, 'PRESEAL.json')))
manifest.fetch('science_files').each do |row|
  bytes = File.binread(File.join(repo, row.fetch('path')))
  saved, err, status = Open3.capture3('git', 'show', seal + ':' + row.fetch('path'), chdir: repo)
  abort('science bytes changed') unless status.success? && saved.b == bytes && Digest::SHA256.hexdigest(bytes) == row.fetch('sha256')
end
server, err, status = Open3.capture3({'GIT_CONFIG_GLOBAL' => '/dev/null'}, 'git', '-c', 'credential.helper=', '-c', 'credential.helper=!gh auth git-credential', 'ls-remote', 'https://github.com/originaxiom/origin-axiom.git', 'refs/heads/audit/physical-bridge-2026-09-05', chdir: repo)
abort('seal not at server') unless status.success? && server.split.first == seal
File.binwrite(File.join(raw, 'server.log'), server)
inputs = JSON.parse(File.read(File.join(base, 'INPUTS.json')))
inputs.fetch('sources').each do |row|
  bytes, err, status = Open3.capture3('git', 'show', inputs.fetch('main') + ':' + row.fetch('path'), chdir: repo)
  abort('source mismatch') unless status.success? && bytes.bytesize == row.fetch('bytes') && Digest::SHA256.hexdigest(bytes) == row.fetch('sha256')
end
arc = inputs.fetch('arc')
archive, err, status = Open3.capture3('git', 'archive', inputs.fetch('main'), arc, chdir: repo)
abort('archive failed') unless status.success?
out, err, status = Open3.capture3('tar', '-x', '-C', raw, stdin_data: archive)
abort('extraction failed') unless status.success?
capture = File.join(repo, 'reports/physical_bridge_2026_09_05/capture_checked_run.rb')
jobs = {
  'replay' => ['python3', File.join(raw, arc, 'verification/post_seal_cusp.py')],
  'native' => ['python3', File.join(base, 'probe.py')],
  'reference' => ['python3', File.join(base, 'reference.py')],
  'focused' => ['python3', '-m', 'pytest', '-q', '-p', 'no:cacheprovider', 'tests/test_physical_bridge_cusp_negative_audit.py']
}
jobs.each do |name, argv|
  out, err, status = Open3.capture3('ruby', '-EUTF-8', capture, File.join(raw, name), *argv, chdir: repo)
  puts name + ': ' + out
  abort(err + ' failed; captured bytes preserved') unless status.success?
end
replayed = JSON.parse(File.read(File.join(raw, 'replay.log')))
native = JSON.parse(File.read(File.join(raw, 'native.log')))
reference = JSON.parse(File.read(File.join(raw, 'reference.log')))
abort('full replay differs from saved source') unless replayed == native.fetch('source_profile')
%w[counts tails exact_fraction_cells].each do |key|
  abort('different algorithms disagree ' + key) unless native[key] == reference[key]
end
abort('independent radius check differs') unless reference.fetch('P2') == replayed.fetch('P2')
abort('focused population mismatch') unless File.read(File.join(raw, 'focused.log')).match?(/7 passed in /)
%w[replay native reference focused].each do |name|
  rec = JSON.parse(File.read(File.join(raw, name + '.json')))
  bytes = File.binread(File.join(raw, name + '.log'))
  abort('capture changed') unless rec['exit_code'] == 0 && rec['signal'].nil? && rec['log_bytes'] == bytes.bytesize && rec['log_sha256'] == Digest::SHA256.hexdigest(bytes)
end
puts JSON.generate(full_upstream_replay: true, different_method_exact_fractions: native['exact_fraction_cells'], independent_finite_radius_profile: true, scientific_goal_achieved: false)
