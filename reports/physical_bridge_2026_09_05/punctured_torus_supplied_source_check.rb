# Read-only byte/page custody, not a mathematical proof checker.
require 'json'
require 'digest'

abort('Usage: ruby punctured_torus_supplied_source_check.rb PDF_DIRECTORY IMAGE_DIRECTORY') unless ARGV.size == 2
prefix = 'reports/physical_bridge_2026_09_05/'
rows = JSON.parse(File.read(prefix + 'PUNCTURED_TORUS_SUPPLIED_SOURCES_2026_09_14.json', encoding: 'UTF-8'))
abort('Expected one PDF and twelve page images') unless rows.size == 13
abort('PDF page map changed') unless rows[0]['printed_pages'] == (1..32).to_a
abort('Image page map incomplete or duplicated') unless rows.drop(1).map { |r| r['printed_pages'] } == (61..72).map { |p| [p] }
abort('Duplicate source filename') unless rows.map { |r| r['local_filename'] }.uniq.size == rows.size
rows.each_with_index do |r, i|
  name = r.fetch('local_filename')
  abort('Receipt must contain only basenames') unless File.basename(name) == name
  path = File.join(ARGV[i == 0 ? 0 : 1], name)
  abort("Byte count differs: #{name}") unless File.size(path) == r.fetch('bytes')
  abort("Digest differs: #{name}") unless Digest::SHA256.file(path).hexdigest == r.fetch('sha256')
  magic = File.binread(path, 8)
  abort("Unexpected file signature: #{name}") unless i == 0 ? magic.start_with?('%PDF-') : magic == "\x89PNG\r\n\x1a\n".b
end
puts JSON.generate(files: rows.size, bytes_and_sha256: 'PASS', pdf_signature: 'PASS',
                   png_signatures: 'PASS', declared_page_sequence: 'PASS',
                   scope: 'Byte custody only. Page content and personal reading are manually attested, not certified by this checker.')
