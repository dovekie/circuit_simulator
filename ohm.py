# Ohm's law

from math import sqrt, pow
from random import randint, sample, choice

class Resistor_group(object):
	"""Group of resistors object"""
	def __init__(self, rg_ident, relationship, resistors=None):
		self.rg_ident = rg_ident # a synthetic ID
		self.relationship = relationship # either str "series" or "parallel"
		self.resistors = resistors # this is a list
		self.resistance = self.calculate_group_resistance()

	# Groups of resistors can contain groups of resistors

	# I call this method on myself and no one else should call it.
	def calculate_group_resistance(self):
		self.resistances = []
		for resistor in self.resistors:
			self.resistances.append(resistor.resistance)
		if self.relationship == "series":
			self.resistance = calc_series_resistance(self.resistances)
		else:
			self.resistance = calc_parallel_resistance(self.resistances)
		return self.resistance



class Resistor(object):
	"""Resistor object class"""

	def __init__(self, ident, resistance):
		self.ident = ident
		self.resistance = resistance
		self.relations = set() # what groups this resistor belongs to

	def __repr__(self):
		"""Provide helpful information when printed!"""
		return "<Resistor object. ID = %s Resistance = %s>" %(self.ident, self.resistance)

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
		self.current = current # Circuit's current does not change.
		self.number_of_resistors = 0 # this should never actually be 0
		self.resistors = []

	def add_resistors(self, num = None): # add resistors to the circuit.
		if num == None: # if the number of resistors is not defined, pick at random.
			self.number_of_resistors = randint(1, 6)
		else:
			self.number_of_resistors = num 

		for resistor_ident in range(self.number_of_resistors): # once the resistors exist, assign resistance values
			self.resistors.append(Resistor(resistor_ident, randint(1, 10)))

	def group_resistors(self):
		states = ["series", "parallel"]
		# start with each resistor in its own group
		# while there is more than one group of resistors
		# put two resistors into either a series or parallel group 
		# the resistance of the last group should be the resistance of the whole circuit
		while len(self.resistors) > 1:
			series_or_parallel = choice(states) # pick either series or parallel
			print series_or_parallel
			# pick two items out of the list of resistors
			# remove them from the list
			# make them part of a resistor group
			# add the resistor group back into the list
			new_group = Resistor_group(len(self.resistors), series_or_parallel, [self.resistors.pop(-1), self.resistors.pop(-1)])
			print self.resistors
			self.resistors.append(new_group)

	def get_resistance(self):
		self.resistance = self.resistors[0].resistance


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