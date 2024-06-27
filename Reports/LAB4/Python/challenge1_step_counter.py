import numpy as np
import matplotlib.pyplot as plt
import ECE16Lib.DSP as filt

def load_data(filename):
    return np.genfromtxt(filename, delimiter=',')

data = load_data("./data/accelerometer.csv")
t = data[:, 0]  
ax = data[:, 1]
ay = data[:, 2]
az = data[:, 3]


l1 = filt.l1_norm(ax, ay, az)


detrended = filt.detrend(l1, win=50)


bl, al = filt.create_filter(3, 1, 'lowpass', 50)
low_passed = filt.filter(bl, al, detrended)


gradient = filt.gradient(low_passed)


smoothed = filt.moving_average(gradient, 20)

count, peaks = filt.count_peaks(smoothed, thresh_low=0.3, thresh_high=1.5)  

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(t, smoothed)
plt.plot(t[peaks], smoothed[peaks], 'rx', label='Peaks')
plt.title(f"Detected Steps: {count}")
plt.xlabel("Time (s)")
plt.ylabel("Signal Amplitude")
plt.legend()
plt.show()