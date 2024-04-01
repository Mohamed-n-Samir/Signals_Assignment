# import sympy as sp
# # from math import * 

# w = 0

# # Analytical result using sympy     
# def analytical_result():

#     lower_bound = 1
#     upper_bound = 10
    
#     if lower_bound > upper_bound:
#         lower_bound,upper_bound = upper_bound,lower_bound

#     x = sp.symbols('x',real = True)

#     def func(x):
#         # return eval(convert_to_sympy_function(integration_function.get()))
#         return (sp.cos(x) + 6 * sp.I * sp.sin(2*x)) * ( sp.exp(w * 1 * sp.I * x))

#     integral = sp.integrate(func(x) ,(x,lower_bound,upper_bound))
#     return integral

# print(analytical_result())










# import sympy as sp

# def analytical_result():

#   w = 0  
#   lower_bound = 1
#   upper_bound = 10

#   if lower_bound > upper_bound:
#     lower_bound, upper_bound = upper_bound, lower_bound

#   x = sp.symbols('x', real=True)  # Declare x as real

#   def func(x):
#     return (sp.cos(x) + 6 * sp.I * sp.sin(2*x)) * (sp.exp(w * 1 * sp.I * x))

#   integral = sp.integrate(func(x), (x, lower_bound, upper_bound))

#   # Simplify the integral and separate real and imaginary parts
#   result = sp.simplify(integral)
#   real_part = sp.re(result)  # Extract real part
#   imag_part = sp.im(result)  # Extract imaginary part

#   # Print the result in Cartesian form
#   print(f"Real part: {real_part}")
#   print(f"Imaginary part: {imag_part}")

# analytical_result()





# import math
# import cmath

# def custom_integration(f, a, b, w):
#     def integrand(x):
#         return (f(x) * cmath.exp(w * x * 1j))

#     dx = 0.0001  # small step for numerical integration
#     area = 0
#     x = a

#     while x < b:
#         area += integrand(x) * dx
#         x += dx

#     return area  # Return the complex result

# # Define your function f(x) here
# def f(x):
#     return math.cos(x) + math.sin(x)


# # User-defined variables a, b, and w
# a = -1
# b = 1
# w = (2+3j)

# result = custom_integration(f, a, b, w)
# print(result)






# import sympy as sp
# import numpy as np  # Import NumPy for numerical evaluation

# def analytical_result():

#   lower_bound = 1
#   upper_bound = 10
#   w = 0

#   if lower_bound > upper_bound:
#     lower_bound, upper_bound = upper_bound, lower_bound

#   x = sp.symbols('x', real=True)  # Declare x as real

#   def func(x):
#     return (sp.cos(x))

#   integral = sp.integrate(func(x), (x, lower_bound, upper_bound))

#   # Simplify the integral (optional)
#   result = sp.simplify(integral)

#   # Convert the expression to a lambda function for numerical evaluation
#   f = sp.lambdify(x, result, modules=['numpy'])  # Use numpy for numerical evaluation

#   # Evaluate the integral numerically (real and imaginary parts)
#   real_part = np.real(f(np.linspace(lower_bound, upper_bound, 100)))  # Evaluate at 100 points
#   imag_part = np.imag(f(np.linspace(lower_bound, upper_bound, 100)))

#   # Print the results
#   print(f"Real part (array): {real_part}")
#   print(f"Imaginary part (array): {imag_part}")

# analytical_result()


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
#     ak_0, _ = calculate_coefficients(x(t), 0, T0)  # a0/2 term
#     result = 0.5 * ak_0
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











# import math
# import cmath

# def custom_integration(f, a, b, w):
#     def integrand(x):
#         return (f(x) * cmath.exp(w * x * 1j))

#     dx = 0.0001  # small step for numerical integration
#     area = 0
#     x = a

#     while x < b:
#         area += integrand(x) * dx
#         x += dx

#     return area  # Return the complex result

# # Define your function f(x) here
# def f(x):
#     return math.cos(x)


# # User-defined variables a, b, and w
# a = -1
# b = 1
# t0 = math.pi
# w = (2 * math.pi) / t0

# number_of_coefficients = 5

# def ak_integration(x)

# ak = [(2/t0) *  custom_integration(f * math.cos(k * w * x),1,10,w) for k in range(1,number_of_coefficients)]



# result = custom_integration(f, a, b, w)
# print(result)



import sympy as sp

def calculate_ak_bk_sympy(signal_func, T, N):
    """
    Calculate ak and bk coefficients of a trigonometric periodic signal symbolically using SymPy.

    Parameters:
        signal_func (sympy.Function): Symbolic function representing the signal.
        T (sympy.Symbol or int): Period of the signal.
        N (int): Number of coefficients to calculate.

    Returns:
        None (Prints the coefficients).
    """
    k = sp.symbols('k')
    ak = (2 / T) * sp.integrate(signal_func * sp.cos(2 * sp.pi * k * t / T), (t, 0, T))
    bk = (2 / T) * sp.integrate(signal_func * sp.sin(2 * sp.pi * k * t / T), (t, 0, T))
    
    for i in range(-N, N+1):
        if i == 0:
            continue
        print(f"a_{i} = {ak.subs(k, i)}")
        print(f"b_{i} = {bk.subs(k, i)}")

# Example usage:
t = sp.symbols('t')
T = sp.pi  # Period of the signal
N = 2  # Number of coefficients to calculate
signal_func = sp.cos(t) + sp.sin(t)

calculate_ak_bk_sympy(signal_func, T, N)
