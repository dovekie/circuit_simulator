# Ohm's law

from math import sqrt, pow

class Circuit(object):
	"""Circuit object class.
	>>> simple_circuit = Circuit(10, 2)

	>>> simple_circuit.resistance
	2

	>>> simple_circuit.current
	10

	>>> simple_circuit.voltage
	20

	>>> simple_circuit.power
	200.0

	"""
	def __init__(self, current, resistance):
		self.resistance = resistance
		self.current = current
		self.voltage = calc_voltage(r=resistance, i=current)
		self.power = calc_power(r=resistance, i=current)

	def __repr__(self):
		"""Provide helpful information when printed!"""
		return "<Circuit object. resistance = %s current = %s>" %(self.resistance, self.current)


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


simple_circuit = Circuit(10, 2)

print "resistance:", simple_circuit.resistance
print "current:", simple_circuit.current
print "power:", simple_circuit.power
print "voltage:", simple_circuit.voltage