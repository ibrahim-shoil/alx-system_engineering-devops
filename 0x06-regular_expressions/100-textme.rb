#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(\S+)\]/).join + "," + ARGV[0].scan(/\[to:(\S+)\]/).join + "," + ARGV[0].scan(/\[flags:(\S+)\]/).join

