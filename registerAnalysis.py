#!/usr/bin/python
import json

f = file("format.json");
s = json.load(f)
f.close


title = s["Title"]
numbits = int(s["nbits"])
registers = s["registers"]
reference=0xff

if numbits == 8:
	referencd=0xff
elif numbits == 16:
	reference=0xffff
elif numbits == 32:
	reference=0xffffffff
else:
	print 'Invalid numbits'
	exit(1)

print 'Title:', title
print 'Numberbits:', numbits
#print registers

def printbit(bit,value):
	print('Bit%s %s' %(bit["bitranges"],bit["bitmeans"]))
	d = bit["meaings"]
	firstbit=int(bit["bitranges"].split('-')[0])
	lastbit=int(bit["bitranges"].split('-')[1])
	result = (value>>firstbit)&(~(reference<<(lastbit-firstbit)))
	print bin(result)
	print(d["000"])
	return 0


def printbits(bits,value):
	for bit in bits:
		printbit(bit, value)
	return 0

def printregister(register):
	print 'Description:', register["descriptions"]
#	registervalue=raw_input()
#	print registervalue
	printbits(register["bits"], 0x36)
	return 0



def parseregisters(registers):
	for register in registers:
		printregister(register)
	return 0

printregister(registers[0])
#parseregisters(registers)
