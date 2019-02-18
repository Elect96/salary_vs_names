#! /usr/bin/python
import numpy as np
import matplotlib.pyplot as plt


names = np.genfromtxt("names.txt", dtype='str', delimiter=",")
salary = np.fromfile("salaries.txt", dtype=int, sep=",")

# x contains a list of numbers from 0 to number of names
x = np.arange(len(names))

plt.bar(x, salary)
plt.xticks(x, names)

plt.ylabel("Salaries")
plt.xlabel("Names")
plt.title("Salary of 10 random people")
plt.show()

# numpy supports many functions like below
# print(np.max(salary), np.min(salary), np.average(salary), np.median(salary))
