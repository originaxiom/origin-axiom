# Binary-safe metadata correction; original failed checker is retained unchanged.
# Completed retrieval custody; not mathematical verification or semantic absence.
require 'json'
require 'digest'
require 'zlib'
require 'open3'

abort('Usage: history_v2_custody.rb RAW_DIRECTORY [--create]') unless [1, 2].include?(ARGV.size)
raw, mode = ARGV
abort('Unknown mode') unless mode.nil? || mode == '--create'
base = 'reports/physical_bridge_2026_09_05/'
stem = 'oa_r39_swipe_history_v2_20260920'
public_archive = base+'CORPUS_RECONCILIATION_HISTORY_V2_2026_09_20.json.gz'
public_receipt = base+'CORPUS_RECONCILIATION_HISTORY_V2_CUSTODY_2026_09_20.json'

def need(ok, reason)
  abort(reason) unless ok
end
def sha(bytes)
  Digest::SHA256.hexdigest(bytes)
end
def git!(*args, input: nil)
  out, err, status = Open3.capture3('git', *args, stdin_data: input.to_s)
  need(status.success?, 'Git failed: '+err)
  out
end
def new_artifact(path, bytes)
  File.open(path, 'wx') { |file| file.binmode; file.write(bytes) }
end

encoded = File.binread(File.join(raw, stem+'.json'))
run = JSON.parse(encoded)
log = File.binread(File.join(raw, stem+'.log'))
need(run['exit_code'] == 0 && run['signal'].nil?, 'History run failed')
need(log.bytesize == run['log_bytes'] && sha(log) == run['log_sha256'], 'Raw capture mismatch')
records = log.lines.map { |s| JSON.parse(s) }
complete = records.select { |r| r['kind'] == 'complete' }
need(complete.size == 1, 'Missing or repeated completion')
complete = complete.first
archive = File.binread(File.join(raw, stem+'.json.gz'))
need(sha(archive) == complete['receipt_sha256'], 'Export changed')
data = JSON.parse(Zlib::GzipReader.open(File.join(raw, stem+'.json.gz'), &:read))
need(data['counts'] == complete['counts'], 'Population receipt mismatch')
tips = (data['refs'].values+data['extra_tips']).uniq
oids = git!('rev-list', '--objects', *tips).lines.map { |s| s.split(' ', 2).first.strip }.uniq
need(sha(oids.sort.join("\n")+"\n") == data['object_inventory_sha256'], 'Pinned object population mismatch')
headers = git!('cat-file', '--batch-check=%(objectname) %(objecttype) %(objectsize)', input: oids.join("\n")+"\n").lines.map(&:split)
need(headers.map(&:first) == oids, 'Independent object traversal mismatch')
counts = Hash.new(0)
blob_bytes = 0
headers.each do |oid, type, size|
  need(size && size.match?(/\A\d+\z/), 'Missing object '+oid.to_s)
  counts[type] += 1
  blob_bytes += size.to_i if type == 'blob'
end
need(counts == data['counts'] && blob_bytes == data['blob_bytes'], 'Independent type/size census mismatch')
need(data['patterns'].size == 13 && data['head_trees'].size == 15, 'Wrong retrieval version/population')
need(data['refs']['refs/heads/audit/physical-bridge-2026-09-05'] == '3450f704cd57dff90ea8502cf6e81485d238a2bd', 'Wrong own scan-start pin')
need(data['refs']['refs/heads/audit/fork-2026-09-20'] == 'be669308089aa47e632e330bda58129a3184b8c5', 'Wrong fork pin')
term_counts = data['patterns'].keys.map { |k| [k, data['historical_blob_hits'].count { |_, h| h['lines'].key?(k) }] }.to_h
need(term_counts == data['term_blob_counts'] && term_counts == complete['term_blob_counts'], 'Term counts mismatch')
need(data['historical_blob_hits'].size == complete['matched_blobs'] && data['working_tree_hits'].size == complete['worktree_hits'], 'Hit count mismatch')
names = git!('log', '--format=', '--name-only', '-z', *tips).split("\0").map(&:strip).reject(&:empty?).uniq
need(names.size == data['historical_name_count'], 'Historical-name census mismatch')
data['head_trees'].each do |ref, tree|
  need(tree['oid'] == data['refs'].fetch(ref), 'Head receipt pin mismatch')
  entries = git!('ls-tree', '-rz', tree['oid']).split("\0").map { |r| meta, path = r.split("\t", 2); [path, meta.split.last] }.to_h
  need(tree['hits'].all? { |h| entries[h['path']] == h['oid'] }, 'Head hit is not the named blob')
end
sources = %w[corpus_reconciliation_scan.rb corpus_reconciliation_scan_v2.rb].map do |s|
  path = base+s
  bytes = git!('show', '3450f704cd57dff90ea8502cf6e81485d238a2bd:'+path)
  need(bytes.b == File.binread(path), 'Reader changed while running')
  {path: path, bytes: bytes.bytesize, sha256: sha(bytes)}
end
red = lambda { |s| s.gsub(raw, '<raw-directory>') }
payload = {
  scope: 'Completed literal/regex retrieval custody, independently checked object/name/head populations. Not semantic absence, full reading, novelty or mathematical verification.',
  raw_basename: stem, raw_receipt_sha256: sha(encoded),
  receipt: run.merge('command' => run.fetch('command').map(&red)),
  public_log: log.force_encoding('UTF-8'), reader_sources: sources,
  archive: {path: public_archive, bytes: archive.bytesize, sha256: sha(archive)},
  object_inventory_sha256: data['object_inventory_sha256'], counts: counts,
  blob_bytes: blob_bytes, current_head_trees_at_start: data['head_trees'].size,
  historical_names: names.size, tag_refs: data['refs'].keys.count { |s| s.start_with?('refs/tags/') },
  extra_tip_count: data['extra_tips'].size, matched_blobs: data['historical_blob_hits'].size,
  term_blob_counts: term_counts, working_tree_hits_at_end: data['working_tree_hits'].size,
  sampling_boundary: 'Refs and reachable Git bytes are pinned at start; nonignored worktree is sampled later. Outgoing drafts/results are not independent prior work. Compressed document contents are not decoded.',
  prior_failure_retained: 'oa_r39_swipe_history_20260920 exited 1 during export; original empty gzip and failed capture are not overwritten.'
}
bytes = JSON.pretty_generate(payload)+"\n"
if mode == '--create'
  need(!File.exist?(public_archive) && !File.exist?(public_receipt), 'Refusing to overwrite published evidence')
  new_artifact(public_archive, archive)
  new_artifact(public_receipt, bytes)
else
  need(File.binread(public_archive) == archive, 'Published archive differs')
  need(File.binread(public_receipt) == bytes, 'Published receipt differs')
end
puts JSON.generate(objects: oids.size, counts: counts, blob_bytes: blob_bytes,
  head_trees: data['head_trees'].size, historical_names: names.size, patterns: data['patterns'].size,
  archive_bytes: archive.bytesize, archive_sha256: sha(archive), verified: true,
  scope: 'Byte/population custody only; not semantic absence, proof or full reading.')
