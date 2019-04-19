import visa
import time
import csv

rm = visa.ResourceManager()
inst = rm.open_resource('GPIB0::5::INSTR')
inst.write('*RST')
inst.write('*CLS')
inst.write('VOLT 0')
inst.write('CURR 40e-3')
inst.write('OUTP ON')
time.sleep(1)

with open('const-power.csv', 'a+', newline='') as csvfile:
	csv = csv.writer(csvfile, delimiter=';')

	while True:
		inst.write('MEAS:VOLT?')
		volt = float(inst.read())
		inst.write('MEAS:CURR?')
		curr = float(inst.read())
		print(time.ctime() + ' --- Voltage: {v:.3f}V, Current: {c:.3f}A'.format(v=volt,c=curr))
		csv.writerow([time.ctime(), time.time(), volt, curr])
		csvfile.flush()
		if volt < 3:
			break
		time.sleep(10)

inst.write('OUTP OFF')
