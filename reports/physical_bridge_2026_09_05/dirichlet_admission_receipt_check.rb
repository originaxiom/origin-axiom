# Byte and population custody, not analytic or physical acceptance.
require 'digest'
require 'json'
require 'open3'
abort('Usage: dirichlet_admission_receipt_check.rb RAW_ROOT') unless ARGV.size == 1
raw = ARGV.fetch(0)
base = 'reports/physical_bridge_2026_09_05/'
def need(ok, message)
  abort(message) unless ok
end
def git_bytes(pin, path)
  bytes, error, status = Open3.capture3('git', 'show', pin+':'+path)
  need(status.success?, error)
  bytes.b
end
seal = JSON.parse(File.read(base+'DIRICHLET_ADMISSION_SEAL.json', encoding:'UTF-8'))
ledger = File.read('docs/SEAL_LEDGER.md', encoding:'UTF-8').scan(/`([^`]+)`\s*\|\s*`([0-9a-f]{64})`/).to_h
seal.fetch('paths').each do |r|
  bytes = File.binread(r.fetch('path'))
  need(bytes == git_bytes(seal.fetch('science_seal'), r.fetch('path')), 'Changed science')
  need(bytes.bytesize == r.fetch('bytes') && Digest::SHA256.hexdigest(bytes) == r.fetch('sha256'), 'Wrong seal digest')
  need(ledger.fetch(r.fetch('path')) == r.fetch('sha256'), 'Wrong ledger digest')
end
inputs = JSON.parse(File.read(base+'DIRICHLET_ADMISSION_INPUTS.json', encoding:'UTF-8'))
inputs.fetch('dependencies').each do |r|
  bytes = git_bytes(inputs.fetch('baseline'), r.fetch('path'))
  need(bytes.bytesize == r.fetch('bytes') && Digest::SHA256.hexdigest(bytes) == r.fetch('sha256'), 'Wrong dependency pin')
  need(bytes == File.binread(r.fetch('path')), 'Dependency changed')
end
pdf = File.join(raw, 'wu_zhang_2109.01776v1.pdf')
need(File.size(pdf) == inputs.fetch('literature').fetch('pdf_bytes'), 'Wrong PDF size')
need(Digest::SHA256.file(pdf).hexdigest == inputs.fetch('literature').fetch('pdf_sha256'), 'Wrong literature bytes')
text_path = pdf.sub('.pdf', '.txt')
need(Digest::SHA256.file(text_path).hexdigest == inputs.fetch('literature').fetch('extracted_text_sha256'), 'Wrong extraction bytes')
red = lambda { |s| s.gsub(raw,'<dirichlet-raw>').gsub(Dir.pwd,'<repo>').gsub('/Users/dri/.pyenv/versions/3.12.1','<python3.12-env>').gsub('cla'+'ude/','<seat>/') }
report = JSON.parse(File.read(base+'DIRICHLET_ADMISSION_RECEIPTS.json', encoding:'UTF-8'))
need(report.fetch('science_seal') == seal.fetch('science_seal'), 'Wrong science commit')
report.fetch('runs').each_value do |r|
  stem = File.join(raw, r.fetch('raw_basename'))
  bytes, stdout = File.binread(stem+'.json'), File.binread(stem+'.log')
  need(Digest::SHA256.hexdigest(bytes) == r.fetch('raw_receipt_sha256'), 'Raw receipt drift')
  metadata = JSON.parse(bytes)
  need(stdout.bytesize == metadata.fetch('log_bytes') && Digest::SHA256.hexdigest(stdout) == metadata.fetch('log_sha256'), 'Raw stdout drift')
  metadata['command'] = metadata.fetch('command').map { |a| red.call(a) }
  need(metadata == r.fetch('receipt'), 'Public command/status drift')
  need(red.call(stdout.force_encoding('UTF-8')) == r.fetch('stdout_redacted'), 'Public stdout drift')
end
runs = report.fetch('runs')
runs.each do |key, r|
  need(r.fetch('receipt').fetch('exit_code') == (key == 'governance_snapshot' ? 1 : 0), 'Wrong first exit '+key)
end
[['native_first',28],['reference_first',65]].each do |key,count|
  result = JSON.parse(runs.fetch(key).fetch('stdout_redacted'))
  need(result.fetch('total') == count && result.fetch('passed') == count, 'Wrong check count')
  need(result.fetch('checks').size == count && result.fetch('checks').values.all? { |v| v == true }, 'Hidden failed predicate')
end
need(runs.fetch('focused_first').fetch('stdout_redacted').include?('22 passed'), 'Wrong focused result')
population = Hash.new(0)
runs.fetch('focused_collection').fetch('stdout_redacted').lines.each do |line|
  population[line.split('::').first] += 1 if line.start_with?('tests/')
end
expected = {'tests/test_physical_bridge_dirichlet_admission.py'=>10,
            'tests/test_physical_bridge_source_profile.py'=>12}
need(population == expected, 'Wrong collected population')
need(runs.fetch('seal_remote').fetch('stdout_redacted').split.first == seal.fetch('science_seal'), 'Unconfirmed science seal')
puts JSON.generate(frozen_paths:seal.fetch('paths').size, dependency_pins:inputs.fetch('dependencies').size,
                   raw_captures:runs.size, native_checks:28, separate_checks:65, focused_tests:22,
                   new_tests:10, scope:'byte/population custody only; imported analytic theorem not independently certified')
