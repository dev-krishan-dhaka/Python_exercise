import matplotlib.pyplot as plt
import numpy as np

# 2 Plots
x = np.linspace(0, 10, 100)

# Plot 1
plt.plot(x, np.sin(x))
plt.title("Plot 1: Sine Wave")
plt.savefig("plot1.png")

# Plot 2
plt.bar(["A", "B", "C"], [3, 7, 5])
plt.title("Plot 2: Bar Chart")
plt.savefig("plot2.png")