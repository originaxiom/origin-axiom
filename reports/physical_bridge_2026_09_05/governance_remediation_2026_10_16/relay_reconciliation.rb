# Post-run metadata reconciliation, not a scientific computation or disposition.
require 'json'
require 'digest'
require 'open3'

main_head, capture, dest = ARGV
abort('Usage: relay_reconciliation.rb PINNED_MAIN_HEAD UNTRUNCATED_RELAY_LOG NEW_JSON') unless ARGV.size == 3
abort('refusing overwrite') if File.exist?(dest)
repo = File.expand_path('../../..', __dir__)
source, error, status = Open3.capture3('git', '-C', repo, 'show', main_head + ':docs/RELAY_LEDGER.md')
abort(error) unless status.success?
main_rows = {}
source.lines.each.with_index(1) do |line, number|
  m = line.match(/^\|\s*`?([A-Za-z0-9_.\-]+\.md)`?[^|]*\|\s*(BANKED|DECLINED|OPEN)\s*\|\s*([0-9]{4}-[0-9]{2}-[0-9]{2}|—|-)\s*\|/)
  next unless m
  main_rows[m[1]] = { 'line' => number, 'status' => m[2], 'date' => m[3],
    'row' => line.chomp, 'sha256' => Digest::SHA256.hexdigest(line) }
end
log = File.read(capture)
stale_names = log.scan(/^\s+([A-Za-z0-9_.\-]+\.md): OPEN /).flatten
invisible_names = log.scan(/^\s+([A-Za-z0-9_.\-]+\.md): INVISIBLE WORK/).flatten
rows = stale_names.map do |name|
  { 'name' => name, 'main' => main_rows[name],
    'sender_owned' => name.start_with?('CODEX_TO_'),
    'main_escalation_marker' => main_rows[name] && main_rows[name]['row'].match?(/ESCALATED\(\s*[0-9]{4}-[0-9]{2}-[0-9]{2}/) }
end
obj = { 'grade' => 'post-run metadata inventory; neither new science nor receiver acceptance',
  'source_main_head' => main_head, 'source_main_ledger_sha256' => Digest::SHA256.hexdigest(source),
  'untruncated_relay_log_sha256' => Digest::SHA256.file(capture).hexdigest,
  'stale_rows' => rows, 'invisible_names' => invisible_names,
  'stale_count' => rows.size, 'main_status_counts' => rows.group_by { |r| r['main'] && r['main']['status'] }.transform_values(&:size),
  'main_open_without_escalation' => rows.select { |r| r['main'] && r['main']['status'] == 'OPEN' && !r['main_escalation_marker'] }.map { |r| r['name'] },
  'invisible_count' => invisible_names.size, 'ledger_modified' => false }
File.open(dest, 'wx') { |f| f.write(JSON.pretty_generate(obj) + "\n") }
puts JSON.pretty_generate(obj.reject { |k, _| %w[stale_rows invisible_names].include?(k) })
