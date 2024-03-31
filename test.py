# import numpy as np
# import tkinter as tk
# from tkinter import ttk
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import matplotlib.pyplot as plt
# from matplotlib.cm import get_cmap

# # Define the function to create the Fourier series plot
# def plot_fourier_series():
#     # Define domain
#     dx = 0.001
#     L = np.pi
#     x = L * np.arange(-1 + dx, 1 + dx, dx)
#     n = len(x)
#     nquart = int(np.floor(n / 4))

#     # Define hat function
#     f = np.zeros_like(x)
#     f[nquart:2 * nquart] = (4 / n) * np.arange(1, nquart + 1)
#     f[2 * nquart:3 * nquart] = np.ones(nquart) - (4 / n) * np.arange(0, nquart)

#     # Create figure and axis
#     fig, ax = plt.subplots()
#     ax.plot(x, f, '-', color='k', linewidth=2)

#     # Compute Fourier series
#     name = "Accent"
#     cmap = get_cmap('tab10')
#     colors = cmap.colors
#     ax.set_prop_cycle(color=colors)

#     A0 = np.sum(f ) * dx
#     fFS = A0 / 2

#     A = np.zeros(20)
#     B = np.zeros(20)
#     for k in range(20):
#         A[k] = np.sum(f * np.cos(np.pi * (k + 1) * x / L)) * dx  # Inner product
#         B[k] = np.sum(f * np.sin(np.pi * (k + 1) * x / L)) * dx
#         fFS = fFS + A[k] * np.cos((k + 1) * np.pi * x / L) + B[k] * np.sin((k + 1) * np.pi * x / L)
#         ax.plot(x, fFS, '-')

#     # Embed the plot into Tkinter
#     canvas = FigureCanvasTkAgg(fig, master=window)
#     canvas.draw()
#     canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# # Create Tkinter window
# window = tk.Tk()
# window.geometry("800x800")
# window.title("Fourier Series Plot")

# # Button to plot Fourier series
# plot_button = ttk.Button(window, text="Plot Fourier Series", command=plot_fourier_series)
# plot_button.pack(side=tk.TOP, pady=10)

# # Start Tkinter event loop
# window.mainloop()





import sympy as sp
import re

def convert_to_sympy_function(fx_string):
    # Replace 'cos' with 'sp.cos'
    fx_string = re.sub(r'cos', r'sp.cos', fx_string)
    # Replace 'sin' with 'sp.sin'
    fx_string = re.sub(r'sin', r'sp.sin', fx_string)
    # Replace 'j' preceded by a number with '* sp.I'
    fx_string = re.sub(r'(\d+)j', r'\1 * sp.I', fx_string)
    # Replace 'j' without any number with '* sp.I'
    fx_string = re.sub(r'j', r'sp.I', fx_string)
    # Replace 'e' with 'sp.exp'
    fx_string = re.sub(r'e', r'sp.exp', fx_string)
    return fx_string

# Example usage
fx_string = "(cos(x) + 0j * sin(2*x)) * (e ** (w * 1j * x))"
sympy_fx_string = convert_to_sympy_function(fx_string)
print("Converted function:", sympy_fx_string)





# import numpy as np
# import matplotlib.pyplot as plt

# # Define your periodic function x(t)
# def x(t):
#     # Example: A square wave with period T0
#     T0 = 2 * np.pi  # Fundamental period (adjust as needed)
#     return np.sign(np.sin(t))  # Square wave function

# # Calculate Fourier coefficients
# def calculate_coefficients(x, k, T0):
#     omega_0 = 2 * np.pi / T0
#     ak = (2 / T0) * np.trapz(x * np.cos(k * omega_0 * np.arange(0, T0, 0.001)), dx=0.001)
#     bk = (2 / T0) * np.trapz(x * np.sin(k * omega_0 * np.arange(0, T0, 0.001)), dx=0.001)
#     return ak, bk

# # Sum up the Fourier series
# def fourier_series(t, N):
#     T0 = 2 * np.pi
#     omega_0 = 2 * np.pi / T0
#     result = 0.5 * calculate_coefficients(x(t), 0, T0)[0]  # a0/2 term
#     for k in range(1, N + 1):
#         ak, bk = calculate_coefficients(x(t), k, T0)
#         result += ak * np.cos(k * omega_0 * t) + bk * np.sin(k * omega_0 * t)
#     return result

# # Generate time values
# t_values = np.arange(0, 10 * np.pi, 0.01)

# # Compute Fourier series for N terms
# N_terms = 5
# series_values = fourier_series(t_values, N_terms)

# # Plot the original function and its Fourier series
# plt.figure(figsize=(8, 6))
# plt.plot(t_values, x(t_values), label="Original x(t)")
# plt.plot(t_values, series_values, label=f"Fourier Series (N={N_terms})")
# plt.xlabel("t")
# plt.ylabel("x(t)")
# plt.title("Fourier Series Representation")
# plt.legend()
# plt.grid(True)
# plt.show()