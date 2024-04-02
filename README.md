# **Integration Solving Tool** _'Python utility app'_

### ***Description :***  A tool built with Python that solves integrals.


## ![Image](https://github.com/Mohamedkhaled2310/Mohamedkhaled/blob/main/signal.project.PNG)

## Development Platform (Frame work):

-  ***Programming Language:*** Python
- ***Libraries:***
    - ***Gui:*** TKinter
    - ***Ploting:*** matplotlib
    - ***symbolic mathematics:*** sympy

## Functionalities & Features
- ***Functionalities:*** 
1. Input Function: The tool would accept the user's input in the form of a mathematical function.
2. Integration Bounds: The user would specify the bounds of integration (lower and upper limits).
3. Numerical Integration Algorithm: The tool would employ a numerical integration algorithm to approximate the value of the integral. Common algorithms include the Trapezoidal Rule,.
4. Output: The tool would output the approximate value of the integral along with any relevant information, such as the error estimate or number of iterations used in the calculation.

- ***Features:***
    - show the results in both Cartesian and polar forms.
    - Compare you results with respect to the analytical form.


- **List Of Funcitons**


  - [f(x)](#fx)
  - [integrate(func, lower_bound, upper_bound, dx)](#integratefunc-lower_bound-upper_bound-dx)
  - [integrate_function()](#integrate_function)
  - [fourier_coefficient(k, dx)](#fourier_coefficientk-dx)
  - [fourier_series(number_of_terms, dx)](#fourier_seriesnumber_of_terms-dx)
  - [analytical_result()](#analytical_result)
  - [analytical_fourier_series(number_of_terms)](#analytical_fourier_seriesnumber_of_terms)
  - [convert_to_sympy_function(fx_string)](#convert_to_sympy_functionfx_string)
  - [sympy_f(x)](#sympy_fx)
  - [reset()](#reset)
  - [instruction()](#instruction)
  - [history()](#history)
  - [my_fourier_window(s)](#my_fourier_windows)
  - [sympy_fourier_window(s)](#sympy_fourier_windows)

## Functions

### `f(x)`
- This function evaluates the expression provided by the user in the `integration_function` entry field multiplied by `e^(w * 1j * x)`.
  
### `integrate(func, lower_bound, upper_bound, dx)`
- Performs numerical integration using the trapezoidal rule.
- Parameters:
  - `func`: The function to be integrated.
  - `lower_bound`: Lower integration bound.
  - `upper_bound`: Upper integration bound.
  - `dx`: Step size for numerical integration.

### `integrate_function()`
- Triggered when the "Integrate" button is clicked in the GUI.
- Integrates the function using the `integrate()` function and displays the results in the GUI.
- Calculates and displays the Fourier series representation of the integrated function.

### `fourier_coefficient(k, dx)`
- Calculates the Fourier coefficients `a_k` and `b_k` for a given `k` using numerical integration.

### `fourier_series(number_of_terms, dx)`
- Calculates the Fourier series of the integrated function up to a specified number of terms.

### `analytical_result()`
- Calculates the analytical result of the integration using Sympy.

### `analytical_fourier_series(number_of_terms)`
- Calculates the analytical Fourier series using symbolic integration with Sympy.

### `convert_to_sympy_function(fx_string)`
- Converts the user-provided function string into a format compatible with Sympy.

### `sympy_f(x)`
- Defines the function to be integrated using Sympy.

### `reset()`, `instruction()`, `history()`, `my_fourier_window(s)`, `sympy_fourier_window(s)`
- Functions to handle resetting GUI inputs, displaying instructions, showing history, and displaying Fourier series representations in separate windows, respectively.


