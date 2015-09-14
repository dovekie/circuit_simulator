# Ohm's law

from math import sqrt, pow
from random import randint

class Circuit(object):
	"""Circuit object class.

	>>> simple_circuit = Circuit(10)

	>>> simple_circuit.current
	10

	>>> simple_circuit.resistors
	{}
	
	>>> simple_circuit.resistors[0] = 10
	>>> simple_circuit.resistors
	{0: 10}

	"""
	def __init__(self, current):
		self.current = current
		self.resistors = {}

	def add_resistors(self):
		for resistor in range(randint(1, 6)):
			self.resistors[resistor] = randint(1, 10)

	def __repr__(self):
		"""Provide helpful information when printed!"""
		return "<Circuit object. current = %s>" %(self.current)

# calculation functions!

def calc_voltage(i=None, r=None, p=None):
	if i != None:
		if r != None:
			voltage = i * r
		else:
			voltage = p/i
	else:
		pass
		voltage = sqrt(p * r)
	return voltage

def calc_resistance(e=None, i=None, p=None):
	if e != None:
		if i != None:
			resistance = e/i
		else:
			resistance = pow(e, 2)/p
	else:
		resistance = p/pow(i, 2)
	return resistance

def calc_current(e=None, r=None, p=None):
	if e != None:
		if r != None:
			current = e/r
		else:
			current = p/e
	else:
		current = sqrt(p/r)
	return current

def calc_power(e=None, r=None, i=None):
	if r != None:
		if e != None:
			power = pow(e, 2)/r
		else:
			power = r * pow(i, 2)
	else:
		power = e * i
	return power

def calc_series_resistance(resistors = []):
	total_resistance = sum(resistors)

	return total_resistance

def calc_parallel_resistance(resistors = []):
	total_resistance = 0
	for resistor in resistors:
		total_resistance = total_resistance + 1/float(resistor)

	total_resistance = 1/total_resistance #FIXME to cut off decimals in a controlled way!

	return total_resistance