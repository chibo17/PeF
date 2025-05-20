import matplotlib.pyplot as plt
import numpy as np
import time



# Časovna kompleksnost funkcije
def measure_time(func, n):
    start_time = time.time()
    func(n)
    end_time = time.time()
    return end_time - start_time

def plot_time_complexity(func, n_values):

    times = [measure_time(func, n) for n in n_values]
    plt.plot(n_values, times, label=f'Time complexity of {func.__name__}')
    plt.xlabel('Input size (n)')
    plt.ylabel('Time (seconds)')
    plt.title('Time Complexity')
    plt.legend()
    plt.show()


# ------------------- terke --------------------









# ------------------- barvanje --------------------






# ------------------- podmnožice --------------------





# ------------------- nahrbtnik --------------------




# ------------------- permutacije --------------------



# ------------------- kraljice --------------------