import matplotlib.pyplot as plt
import numpy as np

# Set style for the plots
plt.style.use('seaborn-v0_8-pastel')
print(plt.style.available)

# Use Numpy to generate a sample array of data
x_vals = np.linspace(0, 10, 100)

# LINE PLOTS work well when graphing functions
# for example, y =f(x) or sin/cos/tan
plt.plot(x_vals, np.sin(x_vals))
plt.plot(x_vals, np.cos(x_vals))

plt.show()
plt.savefig('lineplot.png')
plt.close()

# customization
plt.plot(x_vals, 2*x_vals)

# add titles, labels, legend
plt.title('A Simple Line: y = 2x')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.savefig('lineplot2.png')
plt.close()