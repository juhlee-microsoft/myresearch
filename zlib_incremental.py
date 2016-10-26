import zlib
import binascii

compressor = zlib.compressobj(1)

with open('lorem.txt', 'r') as input:
	while True:
		block = input.read(128)
		if not block:
			break
		compressed = compressor.compress(block)
		if compressed:
			print('Compressed: %s' % binascii.hexlify(compressed))
		else:
			print('buffering....')

	remaining = compressor.flush()
	print('Flushed: %s' % binascii.hexlify(remaining))

