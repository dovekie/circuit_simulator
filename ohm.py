# Ohm's law

from math import sqrt
from random import randint, choice, randrange
from decimal import Decimal, getcontext

class Resistor_group(object):
	"""
	A Resistor Group object can contain either Resistor objects
	or other Resistor Group objects, so long as they have .resistance attributes
	"""
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

	def __repr__(self):
		"""Provide helpful information when printed!"""
		return "<Resistor Group object. ID = %s relationship = %s resistance = %s contains = %s>" %(self.rg_ident, self.relationship, self.resistance, self.resistors)

class Resistor(object):
	"""
	Resistor object

	A resistor object has a resistance
	and a relationship, either series or parallel,
	to every other resistor in the circuit.
	"""

	def __init__(self, ident, resistance):
		self.ident = ident
		self.resistance = Decimal(resistance)

	def __repr__(self):
		"""Provide helpful information when printed!"""
		return "<Resistor object. ID = %s Resistance = %s>" %(self.ident, self.resistance)

class Circuit(object):
	"""
	Circuit object class.
	Circuits have resistors that are grouped into Resistor Group objects.
	The Circuit object's .current attribute is defined when the circuit is created.
	All other values are derived.

	>>> simple_circuit = Circuit(10, 2)

	>>> simple_circuit.current
	Decimal('10')

	"""
	def __init__(self, current, num_resistors = None):
		self.current = Decimal(current) # Circuit's current does not change.
		self.resistors = []
		self.number_of_resistors = num_resistors
		self.add_resistors(self.number_of_resistors)
		self.group_resistors()
		self.get_resistance()
		self.get_voltage()
		self.get_power()

	def add_resistors(self, num = None): # add resistors to the circuit.
		if num == None: # if the number of resistors is not defined, pick at random.
			self.number_of_resistors = randint(1, 6)
		else:
			self.number_of_resistors = num 

		for resistor_ident in range(self.number_of_resistors): # once the resistors exist, assign resistance values
			self.resistors.append(Resistor(resistor_ident, randint(1, 10)))

	def group_resistors(self):
		"""
		Pick two items out of the list of resistors at random
		remove them from the list
		make them part of a resistor group
		add the resistor group back into the list
		"""
		states = ["series", "parallel"]  # list for a choice() coinflip
		rg_ident = 0 # constant int for the group's ID
		while len(self.resistors) > 1:
			series_or_parallel = choice(states) # pick either series or parallel
			new_group = Resistor_group(rg_ident, series_or_parallel,
			            [self.resistors.pop(randrange(len(self.resistors))), # pop two random elements and
			            self.resistors.pop(randrange(len(self.resistors)))])  # create a new Resistance Group object
			self.resistors.append(new_group) # add the new object back to the list
			rg_ident += 1
		self.resistors = self.resistors[0] # Change a list containing one object into one object for sanity

	def get_resistance(self): #FIXME This should only happen after group_resistors. 
		self.resistance = self.resistors.resistance

	def get_voltage(self):
		self.voltage = self.current * self.resistance

	def get_power(self):
		self.power = self.resistance * (self.current**Decimal(2))

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
			resistance = (e**2)/p
	else:
		resistance = p/(i**2)
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
			power = (e**2)/r
		else:
			power = r * (i**2)
	else:
		power = e * i
	return power

def calc_series_resistance(resistors = []):
	total_resistance = sum(resistors)

	return total_resistance

def calc_parallel_resistance(resistors = []):
	total_resistance = 0
	for resistor in resistors:
		total_resistance = total_resistance + 1/Decimal(resistor)

	total_resistance = 1/total_resistance #FIXME to cut off decimals in a controlled way!

	return total_resistance