#!/usr/bin/env ruby
# matches only CAPITAl letters
puts ARGV[0].scan(/[A-Z]*/).join
