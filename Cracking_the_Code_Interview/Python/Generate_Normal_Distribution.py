# Write a function to generate N samples from a normal distribution and plot the histogram.


import numpy as np 
import matplotlib.pyplot as plt

def generate_and_plot_samples(N): 
    mean = 0 
    std = 1 
    data = np.random.normal(mean, std, N) 
    plt.hist(data) 
    plt.show()