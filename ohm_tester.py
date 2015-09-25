import ohm
import unittest

class CirkuUnitTestCase(unittest.TestCase):

	def setUp(self):
		# Setup for resistor tests
		self.res = ohm.Resistor("a", 8)

		# Setup for resistor group tests
		self.res_a = ohm.Resistor("a", 1)
		self.res_b = ohm.Resistor("b", 3)
		self.res_group = ohm.Resistor_group("ab", "series", [self.res_a, self.res_b])


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
		assert(self.res_group.resistance == 0.75)

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
		correct_result = (1/1.8) # aka .5 repeating. FIXME to cut off decimals in a controlled way!
		assert(ohm.calc_parallel_resistance(resistors) == correct_result)

if __name__ == "__main__":
    unittest.main()