# Durable stdout/exit custody for an unchanged command. Not a science producer.
require 'json'
require 'open3'
require 'digest'

stem = ARGV.shift
abort('Usage: ruby capture_checked_run.rb NEW_STEM COMMAND [ARG...]') unless stem && !ARGV.empty?
log_path = stem + '.log'
receipt_path = stem + '.json'
abort('Refusing to overwrite a previous capture') if File.exist?(log_path) || File.exist?(receipt_path)
started = Process.clock_gettime(Process::CLOCK_MONOTONIC)
status = nil
File.open(log_path, 'wx') do |log|
  log.binmode
  Open3.popen2e(*ARGV) do |input, output, waiter|
    input.close
    output.binmode
    loop do
      chunk = output.readpartial(16_384)
      log.write(chunk)
      log.flush
    rescue EOFError
      break
    end
    status = waiter.value
  end
end
receipt = {
  command: ARGV,
  exit_code: status.exitstatus,
  signal: status.termsig,
  elapsed_seconds: Process.clock_gettime(Process::CLOCK_MONOTONIC) - started,
  log_bytes: File.size(log_path),
  log_sha256: Digest::SHA256.file(log_path).hexdigest
}
File.open(receipt_path, 'wx') { |f| f.write(JSON.pretty_generate(receipt) + "\n") }
puts JSON.generate(receipt.reject { |k, _| k == :command })
exit(status.exitstatus || 128 + status.termsig)
