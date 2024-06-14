import numpy as np
import matplotlib.pyplot as plt

def r1(theta):
    numerator = np.abs(np.cos(3*theta)) + 2*(0.25 - np.abs(np.cos(3*theta + np.pi/2)))
    denominator = 2 + 8*np.abs(np.cos(6*theta + np.pi/2))
    return 1 + numerator / denominator



theta_values = np.linspace(0, 2*np.pi, 1000)
r_values = r1(theta_values)

plt.figure(figsize=(8, 6))
plt.polar(theta_values, r_values)
plt.title(r'$r_{1}(\theta) = 1 + \frac{|\cos(3\theta)| + 2(0.25 - |\cos(3\theta + \frac{\pi}{2})|)}{2 + 8|\cos(6\theta + \frac{\pi}{2})|}$')
plt.show()
