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












import sympy as sp
import numpy as np  # Import NumPy for numerical evaluation

def analytical_result():

  lower_bound = 1
  upper_bound = 10
  w = 0

  if lower_bound > upper_bound:
    lower_bound, upper_bound = upper_bound, lower_bound

  x = sp.symbols('x', real=True)  # Declare x as real

  def func(x):
    return (sp.cos(x))

  integral = sp.integrate(func(x), (x, lower_bound, upper_bound))

  # Simplify the integral (optional)
  result = sp.simplify(integral)

  # Convert the expression to a lambda function for numerical evaluation
  f = sp.lambdify(x, result, modules=['numpy'])  # Use numpy for numerical evaluation

  # Evaluate the integral numerically (real and imaginary parts)
  real_part = np.real(f(np.linspace(lower_bound, upper_bound, 100)))  # Evaluate at 100 points
  imag_part = np.imag(f(np.linspace(lower_bound, upper_bound, 100)))

  # Print the results
  print(f"Real part (array): {real_part}")
  print(f"Imaginary part (array): {imag_part}")

analytical_result()