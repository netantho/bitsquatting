#! /usr/bin/env python2

# https://www.gandi.net/domain/register

import sys
import re

def generate_bitstream(name):
	"""Generate the bit stream from a name"""
	stream = ""
	for letter in name:
		l = bin(ord(letter))[2:]
		while len(l) != 7:
			l += '0'
		stream += l
	return stream

def flip(bitstream):
	"""Flip bits in the bit stream and give all the possibilities"""
	flips = []
	for i in range(len(bitstream)):
		new_bitstream = bitstream
		if bitstream[i] == '1':
			bit = '0'
		else:
			bit = '1'
		flips.append(bitstream[:i]+bit+bitstream[(i+1):])
	return flips

def output_domain(flip):
	letters = []
	j = 7
	while j <= len(flip):
		letters.append(flip[(j-7):j])
		j += 7
	for l in letters:
		l = int(l, 2)
		if not re.match(r'^[-a-z0-9]$', chr(l)):
			return None
		else:
			l = chr(l)
	#return (''.join(map(lambda l: chr(int(l,2)), letters)), letters)
	return ''.join(map(lambda l: chr(int(l,2)), letters))

def main(domain):
	domain = domain.split('.')
	name = domain[0]
	bitstream = generate_bitstream(name)
	#print bitstream
	for f in flip(bitstream):
		output = output_domain(f)
		if output:
			print output+'.'+domain[1]
		# TODO: do not display already taken domains 

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print "Usage: python ./main.py <domain>"
	else:
		main(sys.argv[1])
