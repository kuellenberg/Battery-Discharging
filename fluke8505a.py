import visa
import time
import datetime as dt
import csv

rm = visa.ResourceManager()
inst = rm.open_resource('GPIB0::0::INSTR')
inst.write('VRH2') # Volt, Auto-Range, 2^10 Samples per reading = 4.3s
time.sleep(1)

with open('discharge.csv', 'a+', newline='') as csvfile:
	csv = csv.writer(csvfile, delimiter=';')

	while True:
		inst.write('?')
		time.sleep(5)
		volt = float(inst.read())
		print(time.ctime() + ' --- Voltage: {v:.5f}V'.format(v=volt))
		csv.writerow([time.ctime(), time.time(), volt])
		csvfile.flush()
		if volt < 1.0:
			break
		time.sleep(10)
