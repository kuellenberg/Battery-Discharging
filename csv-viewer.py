import csv
import matplotlib.pyplot as plt

with open('discharge.csv', 'r', newline='') as csvfile:
	csv = csv.reader(csvfile, delimiter=';')
	first = next(csv)
	start_time = float(first[1])
	time = []
	volt = []
	for row in csv:
		time.append((float(row[1]) - start_time)/(60*60))
		volt.append(float(row[2]))
	plt.plot(time,volt)
	plt.ylabel('Spannung/V')
	plt.xlabel('Zeit/h')
	plt.grid(True)
	plt.show()
