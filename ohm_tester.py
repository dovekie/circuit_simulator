import ohm
import unittest

class CirkuUnitTestCase(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()