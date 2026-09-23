# Read-only R43 custody and reported outcomes, not scientific certification.
require 'json'
require 'digest'
require 'open3'
abort('Usage: projective_mode_reception_check.rb RAW_DIRECTORY') unless ARGV.size == 1
raw = ARGV.fetch(0)
base = 'reports/physical_bridge_2026_09_05/'
def need(ok, why)
  abort(why) unless ok
end
def sha(bytes)
  Digest::SHA256.hexdigest(bytes)
end
def red(bytes, raw)
  host = File.dirname(File.dirname(raw))
  bytes.gsub(File.join(host,'.pyenv/versions/3.12.1'),'<python3.12-env>')
       .gsub(raw,'<raw-directory>').gsub(Dir.pwd,'<repo>')
end
def git_bytes(pin, path)
  bytes, error, status = Open3.capture3('git','show',pin+':'+path)
  need(status.success?, error)
  bytes.b
end
data = JSON.parse(File.read(base+'PROJECTIVE_MODE_RECEPTION_RECEIPTS.json'))
incoming = data.fetch('incoming')
incoming.fetch('verified_seal_entries').each do |row|
  bytes = git_bytes(incoming.fetch('source_pin'),row.fetch('path'))
  need(bytes.bytesize == row['bytes'] && sha(bytes) == row['sha256'], 'Changed incoming pin bytes')
  need(bytes == git_bytes(row.fetch('seal_pin'),row.fetch('path')), 'Incoming seal differs')
  path = File.join(raw,incoming.fetch('execution_snapshot_basename'),row.fetch('path'))
  need(File.binread(path) == bytes, 'Execution snapshot differs: '+row['path'])
end
data.fetch('incoming_read_sources').each do |row|
  bytes = git_bytes(incoming.fetch('source_pin'),row.fetch('path'))
  need(bytes.bytesize == row['bytes'] && sha(bytes) == row['sha256'], 'Changed read-source bytes')
end
data.fetch('frozen_own_inputs').each do |row|
  bytes = File.binread(row.fetch('path'))
  need(bytes.bytesize == row['bytes'] && sha(bytes) == row['sha256'], 'Changed frozen own input')
  need(bytes == git_bytes(data.fetch('own_input_pin'),row.fetch('path')), 'Own input differs from pin')
end
data.fetch('primary_artifacts').each do |row|
  path = File.join(raw,row.fetch('local_container_basename'),row.fetch('basename'))
  need(File.size(path) == row['bytes'] && Digest::SHA256.file(path).hexdigest == row['sha256'], 'Changed paper artifact')
end
data.fetch('runs').each do |key,row|
  stem = File.join(raw,row.fetch('raw_basename'))
  need(Digest::SHA256.file(stem+'.json').hexdigest == row['raw_receipt_sha256'], 'Changed raw receipt')
  receipt = JSON.parse(File.read(stem+'.json'))
  bytes = File.binread(stem+'.log')
  need(bytes.bytesize == receipt['log_bytes'] && sha(bytes) == receipt['log_sha256'], 'Changed raw log')
  receipt['command'] = receipt.fetch('command').map { |x| red(x,raw) }
  need(receipt == row['receipt'], 'Published run metadata differs: '+key)
  public_bytes = red(bytes.force_encoding('UTF-8'),raw).b
  if row['public_path']
    need(File.binread(row['public_path']) == public_bytes, 'Public output differs')
    need(sha(public_bytes) == row['public_sha256'], 'Public output hash differs')
  else
    need(row.fetch('raw_log_with_environment_redaction').b == public_bytes, 'Embedded raw output differs')
  end
  expected = %w[original_tests broad_prior].include?(key) ? 1 : 0
  need(receipt['exit_code'] == expected && receipt['signal'].nil?, 'Unexpected run exit: '+key)
end
original = File.read(data['runs']['original_tests']['public_path'])
corrected = File.read(data['runs']['corrected_tests']['public_path'])
failed = original.lines.select { |s| s.start_with?('FAILED ') }.map(&:strip)
need(failed == data['failed_ids'] && failed.size == 3, 'Original failure population changed')
need(failed.all? { |s| s.include?('test_every_positive_rank_exception_is_geometric[phase') }, 'Different original failed expectation')
need(original.include?('3 failed, 27 passed'), 'Original counts differ')
need(corrected.include?('40 passed') && corrected.lines.none? { |s| s.start_with?('FAILED ','ERROR ') }, 'Corrected counts differ')
%w[original_tests corrected_tests].each do |key|
  command = data['runs'][key]['receipt']['command']
  selected = command.select { |s| s.start_with?('reports/') && s.end_with?('.py') }
  expected = 'reports/projective_cusp_spectrum_2026_09_21/'+(key == 'original_tests' ? 'test_verify.py' : 'test_verify_v2.py')
  need(selected == [expected], 'Reuse test population differs')
  need(command.include?('--import-mode=importlib') && command.include?('no:cacheprovider') && command.include?('no:randomly'), 'Reuse options changed')
end
puts JSON.generate(incoming_seal_entries:incoming['verified_seal_entries'].size,
  incoming_distinct_paths:incoming['verified_seal_entries'].map { |r| r['path'] }.uniq.size,
  read_source_paths:data['incoming_read_sources'].size, frozen_own_inputs:data['frozen_own_inputs'].size,
  primary_artifacts:data['primary_artifacts'].size, raw_runs:data['runs'].size,
  original:{passed:27,failed:3}, corrected:{passed:40,failed:0},
  scope:'Byte custody and same-implementation reuse, not independent analytic certification or physical chirality.')
