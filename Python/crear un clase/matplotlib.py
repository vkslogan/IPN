import matplotlib.pyplot as plt

#Cubico 1
x = [1, 2, 3, 4, 5]
y = [-2, -7, -8, 1, 26]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(x, y, linewidth=4)
ax.set_title("Cubico 1", fontsize=24)
ax.set_xlabel("x", fontsize=24)
ax.set_ylabel("y", fontsize=36)
ax.tick_params(axis='both', labelsize=14)
ax.scatter(x, y, c='red', s=200)

plt.show()

#Cubico 2


x_init = 0
x_fin = 2000


x_values = range(x_init, x_fin)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(x_values, y_values, linewidth=4)
ax.set_title("x^2", fontsize=24)
ax.set_xlabel("x", fontsize=24)
ax.set_ylabel("y", fontsize=36)
ax.tick_params(axis='both', labelsize=14)


plt.show()

