# Read-only integrity checks on the literature retrieval, not physical tests.
require 'json'
require 'digest'
require 'open3'

prefix = 'reports/physical_bridge_2026_09_05/'
abort('Usage: ruby punctured_torus_receipt_check.rb RAW_HISTORY.json') unless ARGV.size == 1
raw = JSON.parse(File.read(ARGV[0], encoding: 'UTF-8'))
pub = JSON.parse(File.read(prefix + 'PUNCTURED_TORUS_HISTORY_2026_09_14.json', encoding: 'UTF-8'))
abort('Raw receipt bytes differ') unless File.size(ARGV[0]) == pub['raw_receipt']['bytes']
abort('Raw receipt digest differs') unless Digest::SHA256.file(ARGV[0]).hexdigest == pub['raw_receipt']['sha256']
%w[scope extra_tips patterns unique_objects_sha256 counts blob_bytes term_hit_blobs hits].each do |k|
  abort("Published data differ: #{k}") unless raw[k] == pub[k]
end
abort('Reference SHA population changed') unless raw['refs'].map { |r| r['sha'] } == pub['head_aliases'].map { |r| r['sha'] }

patterns = pub['patterns'].transform_values { |s| Regexp.new(s, Regexp::IGNORECASE, 'n') }
Open3.popen3('git', 'cat-file', '--batch') do |input, output, error, wait|
  input.binmode
  output.binmode
  pub['hits'].each do |h|
    input.write(h['oid'] + "\n")
    input.flush
    oid, type, n = output.gets.split
    abort('Unexpected object header') unless oid == h['oid'] && type == 'blob'
    b = output.read(Integer(n))
    abort('Short object') unless b.bytesize == Integer(n) && output.read(1) == "\n"
    lines = {}
    patterns.each do |k, regex|
      next unless b.match?(regex)
      lines[k] = []
      b.each_line.with_index(1) { |l, i| lines[k] << i if l.match?(regex) }
    end
    abort("Line matches differ: #{oid}") unless lines == h['matching_lines_by_term']
  end
  input.close
  abort(error.read) unless wait.value.success?
end

files = JSON.parse(File.read(prefix + 'PUNCTURED_TORUS_REPO_RECEIPTS_2026_09_14.json', encoding: 'UTF-8'))
late = JSON.parse(File.read(prefix + 'PUNCTURED_TORUS_LATE_FETCH_2026_09_14.json', encoding: 'UTF-8'))
files += late.fetch('files')
files.each do |r|
  b, e, s = Open3.capture3('git', 'show', r['commit'] + ':' + r['path'])
  abort(e) unless s.success?
  abort("Source receipt differs: #{r['path']}") unless b.bytesize == r['bytes'] && Digest::SHA256.hexdigest(b) == r['sha256']
end
puts JSON.generate(published_transform: 'PASS', raw_sha256: 'PASS',
                   ref_shas: pub['head_aliases'].size, checked_hit_blobs: pub['hits'].size,
                   matched_line_lists: 'PASS', pinned_source_files: files.size,
                   scope: 'Checks recorded hits and byte custody. Does not repeat the all-object absence scan or certify any mathematical/physical claim.')
