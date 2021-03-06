import ohm
import unittest
from decimal import Decimal

class CirkuUnitTestCase(unittest.TestCase):

	def setUp(self):
		# Setup for resistor tests
		self.res = ohm.Resistor("a", 8)

		# Setup for resistor group tests
		self.res_a = ohm.Resistor("a", 1)
		self.res_b = ohm.Resistor("b", 3)
		self.res_group = ohm.Resistor_group("ab", "series", [self.res_a, self.res_b])

		# Setup for circuit tests
		self.circ = ohm.Circuit(10, 2)
		self.circ.group_all_resistors()
		self.circ.get_resistance()
		self.resistance_a = self.circ.resistors[0].resistors[0].resistance
		self.resistance_b = self.circ.resistors[0].resistors[1].resistance
		self.resistor_list = self.circ.resistors[0].resistors
		self.relationship = self.circ.resistors[0].relationship

	def test_circuit_init_no_build_current(self):
		assert(self.circ.current == 10)	

	def test_circuit_init_with_build_resistor(self):
		self.circ_build = ohm.Circuit(10, 2, True)
		assert(len(self.circ_build.resistors) == 1)

	def test_circuit_init_with_build_power(self):
		self.circ_build = ohm.Circuit(10, 2, True)
		assert(hasattr(self.circ_build, "power"))

	def test_circuit_init_with_build_voltage(self):
		self.circ_build = ohm.Circuit(10, 2, True)
		assert(hasattr(self.circ_build, "voltage"))

	def test_add_resistors(self):
		assert(len(self.resistor_list) == 2)

	def test_group_all_resistors(self):
		assert(isinstance(self.circ.resistors[0], ohm.Resistor_group))

	def test_get_resistance(self):
		if self.relationship == "series":
			print self.relationship
			assert(self.circ.resistance == self.resistance_a + self.resistance_b)
		if self.relationship == "parallel":
			print self.relationship
			inverse_a = 1/self.resistance_a
			inverse_b = 1/self.resistance_b
			inverse_sum = inverse_a + inverse_b
			assert(self.circ.resistance == 1/inverse_sum)

	def test_random_resistors(self):
		self.circ.resistors = []
		self.circ.add_resistors()
		self.resistor_list = self.circ.resistors
		assert(len(self.resistor_list) > 0 and len(self.resistor_list) < 7)

	def test_resistor_init(self):
		assert(self.res.ident == "a" and self.res.resistance == 8)

	def test_resistor_repr(self):
		represent = repr(self.res)
		assert(represent == '<Resistor object. ID = a Resistance = 8>')


	def test_resistor_group_init(self):
		assert(self.res_group.rg_ident == "ab" and self.res_group.relationship == "series")

	def test_resistor_group_calculate_resistance_series(self):
		assert(self.res_group.resistance == 4)

	def test_resistor_group_calculate_resistance_parallel(self):
		self.res_group.relationship = "parallel"
		self.res_group.calculate_group_resistance()
		correct_result = 1/(( 1/Decimal(1) ) + ( 1/Decimal(3) ))
		assert(self.res_group.resistance == correct_result)

	def test_resistor_group_repr(self):
		represent_group = repr(self.res_group)
		assert(represent_group == '<Resistor Group object. ID = ab relationship = series resistance = 4 contains = [<Resistor object. ID = a Resistance = 1>, <Resistor object. ID = b Resistance = 3>]>')


	def test_volts_i_times_r(self):
		i = 10
		r = 20
		correct_result = 200
		assert(ohm.calc_voltage(i=i, r=r) == correct_result)

	def test_volts_p_over_i(self):
		p = 10
		i = 2
		correct_result = 5
		assert(ohm.calc_voltage(p=p, i=i) == correct_result)

	def test_volts(self):
		p = 12
		r = 3
		correct_result = 6
		assert(ohm.calc_voltage(p=p, r =r) == correct_result)

	def test_resistance_e_over_i(self):
		e = 50
		i = 25
		correct_result = 2
		assert(ohm.calc_resistance(e=e, i=i) == correct_result)

	def test_resistance_e_squared_over_p(self):
		e = 4
		p = 2
		correct_result = 8
		assert(ohm.calc_resistance(e=e, p=p) == correct_result)

	def test_resistance_p_over_i_squared(self):
		p = 32
		i = 4
		correct_result = 2
		assert(ohm.calc_resistance(p=p, i=i) == correct_result)

	def test_current_e_over_r(self):
		e = 16
		r = 2
		correct_result = 8
		assert(ohm.calc_current(e=e, r=r) == correct_result)

	def test_current_p_over_e(self):
		p = 20
		e = 10
		correct_result = 2
		assert(ohm.calc_current(p=p, e=e) == correct_result)

	def test_current_sqrt_p_over_r(self):
		p = 64
		r = 4
		correct_result = 4
		assert(ohm.calc_current(p=p, r=r) == correct_result)

	def test_power_e_squared_over_r(self):
		e = 4
		r = 2
		correct_result = 8
		assert(ohm.calc_power(e=e, r=r) == correct_result)

	def test_power_r_times_i_squared(self):
		r = 2
		i = 3
		correct_result = 18
		assert(ohm.calc_power(r=r, i=i) == correct_result)

	def test_power_e_times_i(self):
		e = 5
		i = 3
		correct_result = 15
		assert(ohm.calc_power(e=e, i=i) == correct_result)

	def test_series_resistance(self):
		resistors = [3, 2, 5, 10]
		correct_result = 20
		assert(ohm.calc_series_resistance(resistors) == correct_result)

	def test_parallel_resistance(self):
		resistors = [2, 10, 1, 5]
		correct_result = 1/(( 1/Decimal(2) ) + ( 1/Decimal(10) ) + ( 1/Decimal(1) ) + ( 1/Decimal(5) )) # aka .5 repeating. FIXME to cut off decimals in a controlled way!
		assert(ohm.calc_parallel_resistance(resistors) == correct_result)

	def test_transitive_resistance(self):
		circ = ohm.Circuit(10, 3)
		res1 = circ.resistors[0].resistance
		res2 = circ.resistors[1].resistance
		res3 = circ.resistors[2].resistance
		circ.group_resistor_pair(0, [0, 1], "parallel")
		circ.group_resistor_pair(1, [0, 1], "parallel")
		circ.get_resistance()
		correct_result = 1/((1/res1) + (1/res2) + (1/res3))
		assert(circ.resistance == correct_result)

if __name__ == "__main__":
    unittest.main()