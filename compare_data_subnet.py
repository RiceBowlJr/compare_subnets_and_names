import csv
import os

same_addr_name = list()
same_addr = list()

with open('data_1.csv') as f_1:
    data_1 = [tuple(line) for line in csv.reader(f_1, delimiter=';')]

with open('data_2.csv') as f_2:
	data_2 = [tuple(line) for line in csv.reader(f_2, delimiter=';')]

for elt in data_2:
	for elt_1 in data_1:
		if elt == elt_1:
			same_addr_name.append(elt)
		elif elt[1] == elt_1[1]:
			same_addr.append((elt[1], elt[0], elt_1[0]))
		else:
			pass

with open('exit_same_name.csv', 'w') as exit_same_name:
	wr = csv.writer(exit_same_name, delimiter=';')
	for elt in same_addr_name:
		wr.writerow(elt)

with open('exit_same_addr.csv', 'w') as exit_same_addr:
	wr = csv.writer(exit_same_addr, delimiter=';')
	for elt in same_addr:
		wr.writerow(elt)


# Deleting blank lines

clean_lines = []
with open('exit_same_name.csv', "r") as f:
    lines = f.readlines()
    clean_lines = [l.strip() for l in lines if l.strip()]

with open('exit_same_name_PROPER.csv', "w") as f:
    f.writelines('\n'.join(clean_lines))

clean_lines = []
with open('exit_same_addr.csv', "r") as f:
    lines = f.readlines()
    clean_lines = [l.strip() for l in lines if l.strip()]

with open('exit_same_addr_PROPER.csv', "w") as f:
    f.writelines('\n'.join(clean_lines))


# Cleaning repo

os.system('del exit_same_addr.csv')
os.system('del exit_same_name.csv')
