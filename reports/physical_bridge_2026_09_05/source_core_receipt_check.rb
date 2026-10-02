# Byte/exit/scope custody only; not independent physical or analytic review.
require 'digest'
require 'json'
require 'open3'
abort('Usage: source_core_receipt_check.rb RAW_ROOT') unless ARGV.size == 1
raw = ARGV.fetch(0)
base = 'reports/physical_bridge_2026_09_05/'
def need(ok, text)
  abort(text) unless ok
end
def bytes(pin, path)
  b, e, s = Open3.capture3('git', 'show', pin+':'+path)
  need(s.success?, e)
  b.b
end
seals = JSON.parse(File.read(base+'SOURCE_CORE_SEAL.json'))
ledger = File.read('docs/SEAL_LEDGER.md').scan(/`([^`]+)`\s*\|\s*`([0-9a-f]{64})`/).to_h
seals.fetch('groups').each do |group|
  group.fetch('paths').each do |r|
    path = r.fetch('path')
    b = File.binread(path)
    need(b == bytes(group.fetch('commit'), path), 'Changed frozen source: '+path)
    need(Digest::SHA256.hexdigest(b) == r.fetch('sha256') && b.bytesize == r.fetch('bytes'), 'Bad frozen digest')
    need(ledger.fetch(path) == r.fetch('sha256'), 'Bad seal row')
  end
end
inputs = JSON.parse(File.read(base+'SOURCE_CORE_INPUTS.json'))
inputs.fetch('sources').each do |r|
  b = bytes(r.fetch('commit'), r.fetch('path'))
  need(Digest::SHA256.hexdigest(b) == r.fetch('sha256') && b.bytesize == r.fetch('bytes'), 'Bad source pin')
end
red = lambda { |s| s.gsub(File.join(Dir.home, '.pyenv/versions/3.12.1'), '<python3.12-env>').gsub(raw, '<r77-raw>').gsub(Dir.pwd, '<repo>') }
d = JSON.parse(File.read(base+'SOURCE_CORE_RECEIPTS.json'))
d.fetch('runs').each_value do |r|
  stem = File.join(raw, r.fetch('raw_basename'))
  rb, lb = File.binread(stem+'.json'), File.binread(stem+'.log')
  need(Digest::SHA256.hexdigest(rb) == r.fetch('raw_receipt_sha256'), 'Changed raw receipt')
  meta = JSON.parse(rb)
  need(lb.bytesize == meta.fetch('log_bytes') && Digest::SHA256.hexdigest(lb) == meta.fetch('log_sha256'), 'Changed raw stdout')
  meta['command'] = meta.fetch('command').map { |s| red.call(s) }
  need(meta == r.fetch('receipt'), 'Public command/status differs')
  need(red.call(lb.force_encoding('UTF-8')) == r.fetch('stdout_redacted'), 'Public trace differs')
end
runs = d.fetch('runs')
need(runs['native_first']['receipt']['exit_code'] == 1 && runs['native_first']['stdout_redacted'].include?('BooleanAtom'), 'Lost original failure')
n = JSON.parse(runs['native_report_first']['stdout_redacted'])
c = JSON.parse(runs['independent_first']['stdout_redacted'])
need(n['all_checks_pass'] && n['passed'] == 49 && n['total'] == 49, 'Native scope differs')
need(c['all_checks_pass'] && c['checks'].size == 29 && c['rank'] == 24, 'Independent scope differs')
need(c['tail_coefficients'][2] == '0' && c['gradient_coefficients'][2] == '2/3', 'Lost live gradient control')
need(runs['focused_first']['receipt']['exit_code'] == 0 && runs['focused_first']['stdout_redacted'].include?('16 passed'), 'Original focused population differs')
need(runs['focused_report_first']['receipt']['exit_code'] == 0 && runs['focused_report_first']['stdout_redacted'].include?('20 passed'), 'Final focused population differs')
puts JSON.generate(frozen_paths: seals['groups'].sum { |g| g['paths'].size }, source_pins: inputs['sources'].size,
  raw_captures: runs.size, native_controls:49, independent_controls:29, final_focused_tests:20,
  scope:'custody only; analytic/global/physical acceptance remains separate')
