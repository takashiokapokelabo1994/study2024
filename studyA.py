import random
import csv

#for i in range(0,20):
out = []
while len(out) < 20:
	n = random.randint(0, 100000)
	if not n in out:
		out.append(n)
	with open('studyA.csv','a',newline='') as f:
		writer = csv.writer(f)
		writer.writerow([n])
