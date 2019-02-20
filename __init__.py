#! /usr/bin/python
import numpy as np
import matplotlib.pyplot as plt


names = np.genfromtxt("names.txt", dtype='str', delimiter=",")
salary = np.fromfile("salaries.txt", dtype=int, sep=",")

# x contains a list of numbers from 0 to number of names
# x = np.arange(len(names))
#
# plt.bar(x, salary)
# plt.xticks(x, names)
#
# plt.ylabel("Salaries")
# plt.xlabel("Names")
# plt.title("Salary graph")
# plt.show()

# numpy supports many functions like below
# print(np.max(salary), np.min(salary), np.average(salary), np.median(salary))

# [a:-b] - start from a, subtract b from the end of the list
salaries_new = salary[2:-2]
names_new = names[2:-2]

x = np.arange(len(names_new))

plt.bar(x, salaries_new)
plt.xticks(x, names_new)

plt.ylabel("Salaries")
plt.xlabel("Names")
plt.title("Salary graph")
plt.show()
