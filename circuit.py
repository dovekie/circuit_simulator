import ohm

def Print_Circuit_Values(circuit):

	print "Current: ", circuit.current
	print "Resistance: ", circuit.resistance
	print "Resistors: ", circuit.resistors[0] 
	print "Voltage: ", circuit.voltage 
	print "Power: ", circuit.power 

def Get_Circuit_Values(circuit):
	circuit.get_resistance()
	circuit.get_voltage()
	circuit.get_power()

def Make_Circuits():

	circ0 = ohm.Circuit(30, 1)

	circ1 = ohm.Circuit(10, 4)
	circ1.group_resistor_pair(0, [0, 1], "parallel")
	circ1.group_resistor_pair(1, [0, 1], "parallel")
	circ1.group_resistor_pair(2, [0, 1], "series")

	circ2 = ohm.Circuit(20, 2)
	circ2.group_resistor_pair(0, [0, 1], "series")

	circ3 = ohm.Circuit(40, 3)
	circ3.group_resistor_pair(0, [0, 1], "series")
	circ3.group_resistor_pair(1, [0, 1], "series")

	circ4 = ohm.Circuit(5, 2)
	circ4.group_resistor_pair(0, [0, 1], "parallel")

	circ5 = ohm.Circuit(15, 3)
	circ5.group_resistor_pair(0, [0, 1], "series")
	circ5.group_resistor_pair(1, [0, 1], "parallel")

	circ6 = ohm.Circuit(25, 4)
	circ6.group_resistor_pair(0, [0, 1], "series")
	circ6.group_resistor_pair(1, [0, 1], "series")
	circ6.group_resistor_pair(2, [0, 1], "parallel")

	circ7 = ohm.Circuit(35, 3)
	circ7.group_resistor_pair(0, [0, 1], "parallel")
	circ7.group_resistor_pair(1, [0, 1], "parallel")


	circuits = []

	circuits.append(circ0)
	circuits.append(circ1)
	circuits.append(circ2)
	circuits.append(circ3)
	circuits.append(circ4)
	circuits.append(circ5)
	circuits.append(circ6)

	return circuits


for circuit in Make_Circuits():
	Get_Circuit_Values(circuit)
	Print_Circuit_Values(circuit)