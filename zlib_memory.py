# This is the sameple memory calculation for python compression rate
#

import zlib

original_data = 'This is the original text.'
fmt = '%15s %15s'
print fmt % ('len(data)', 'len(compressed)')
print fmt % ('-' * 15, '-' * 15)

for i in xrange(10):
	data = original_data * i
	compressed = zlib.compress(data) 
	highlight = '*' if len(data) < len(compressed) else ''
	print fmt % (len(data), len(compressed)), highlight
