import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.pyplot import figure,plot,axhline,axvline,cla
from matplotlib import use
import sympy as sp
from math import *
import re
import numpy as np
import warnings

# Suppress the ComplexWarning  who Read Fokak Men De
warnings.filterwarnings("ignore", category=np.ComplexWarning)

# Needed
# (cos(x)+6*1j*sin(2*x))*(e**(w*1j*x))

# Define Omega Var
w = 0
t0 = pi
w0 = (2*pi)/t0

# Define the function f(x)
def f(x):
    return (eval(integration_function.get())) * (e**(w*1j*x))

# Trapezoidal rule for numerical integration
def integrate(func,lower_bound, upper_bound, dx):

    X = []
    Y = []

    if(lower_bound == upper_bound):
        return complex(0)
    
    answer = 0.0
    flag = 0

    if lower_bound > upper_bound:
        lower_bound,upper_bound = upper_bound,lower_bound
        flag = 1

    while lower_bound <= upper_bound:

        try: 
            y = func(lower_bound)
            limit_at_a_point = y * dx
            X.append(lower_bound)
            Y.append(y)
            answer += limit_at_a_point

        except Exception as e:
            print("something went wrong => " + e)

        lower_bound += dx

    if flag : answer *= -1

    cla()
    axhline(0)
    axvline(0)
    plot([],[])
    fig.canvas.draw()
    plot(X,Y)
    fig.canvas.draw() 

    return answer

# Function to handle integration button click
def integrate_function():
    try:        
        # Bounds
        lower_bound = float(lower_bound_entry.get())
        upper_bound = float(upper_bound_entry.get())

        dx = float(accuracy.get())

        integral = integrate(f,lower_bound, upper_bound, dx)
  
        cartesian_result_label.config(text="Cartesian : "+ str(integral.real))

        imag_polar = 0
        if isinstance(integral,complex):
            imag_polar = integral.imag            
        else:
            imag_polar = str(atan2(integral.imag,integral.real))

        polar_result_label.config(text="Polar : " + str((integral.real)) + " * exp(" + str(imag_polar) + "j)")
        analytical_result_label.config(text="Analytical result: " + str(analytical_result()))

        my_series = fourier_series(5,dx)

        a0 = my_series[0]
        coefficients = my_series[1]

        fourier_representation = f"{round(a0,4)}/2 \n"

        for coefficient in coefficients:
            fourier_representation += f"+ [({round(coefficient[1],4)} * cos({coefficient[0]} * {w0} * t)) + {round(coefficient[2],4)} * cos({coefficient[0]} * {w0} * t)]\n"

        my_fourier_window(fourier_representation)

        sympy_series = analytical_fourier_series(5)

        a0 = sympy_series[0]
        coefficients = sympy_series[1]

        sympy_fourier_representation = f"{a0}/2 \n"

        for coefficient in coefficients:
            sympy_fourier_representation += f"+ [({coefficient[1]} * cos({coefficient[0]} * {w0} * t)) + {coefficient[2]} * cos({coefficient[0]} * {w0} * t)]\n"

        sympy_fourier_window(sympy_fourier_representation)

        file=open('history.txt','a')
        file.write('\n'+str(integration_function.get())+'\n'+'Lower: '+str(lower_bound_entry.get())+'\n'+'Upper: '+str(upper_bound_entry.get())+'\n'+'Cartesian = '+str(integral)+'\n'+'Polar = '+str(abs(integral)) + " * exp(" + str(atan2(integral.imag, integral.real)) + "j)"+'\n'+ "Fourier Series: " + fourier_representation)
        file.close()

    except Exception as e:
        messagebox.showerror("Error", "Invalid input or function: " + str(e))

# # Fourier Coefficients

def fourier_coefficient(k,dx):

    def ak_fourier_function(t):
        return f(t) * cos(k*w0*t)

    def bk_fourier_function(t):
        return f(t) * sin(k*w0*t)

    a_k = 2/t0 * integrate(ak_fourier_function,0,t0,dx)
    b_k = 2/t0 * integrate(bk_fourier_function,0,t0,dx)

    return a_k, b_k

# Fourier Series
def fourier_series(number_of_terms,dx):
    series = []

    def a0_fourier_function(t):
        return f(t)
    
    a_0 = 2/t0 * integrate(a0_fourier_function,0,t0,dx)

    for n in range(-number_of_terms, number_of_terms+1):
        a_n, b_n = fourier_coefficient(n,dx)
        series.append((n,a_n.real, b_n.real))

    return a_0.real,series

# Analytical result using sympy     
def analytical_result():

    lower_bound = float(lower_bound_entry.get())
    upper_bound = float(upper_bound_entry.get())
    
    if lower_bound > upper_bound:
        lower_bound,upper_bound = upper_bound,lower_bound

    x = sp.symbols('x',real = True)

    integral = sp.integrate(sympy_f(x) ,(x,lower_bound,upper_bound))

    # Simplify the integral (optional)
    result = sp.simplify(integral)

    # Convert the expression to a lambda function for numerical evaluation
    f = sp.lambdify(x, result, modules=['numpy'])  # Use numpy for numerical evaluation

    # Evaluate the integral numerically (real and imaginary parts)
    real_part = np.real(f(np.linspace(lower_bound, upper_bound, 100)))  # Evaluate at 100 points
    imag_part = np.imag(f(np.linspace(lower_bound, upper_bound, 100)))

    return str(real_part) + " * exp(" + str(imag_part) + "j)"

# Calculate Analytical Fourier Series
def analytical_fourier_series(number_of_terms):
    series = []
    t = sp.symbols('t')
    T = sp.pi  # Period of the signal
    N = 2  # Number of coefficients to calculate

    k = sp.symbols('k')
    ak = (2 / T) * sp.integrate(sympy_f(t) * sp.cos(2 * sp.pi * k * t / T), (t, 0, T))
    bk = (2 / T) * sp.integrate(sympy_f(t) * sp.sin(2 * sp.pi * k * t / T), (t, 0, T))
    
    for i in range(-number_of_terms, number_of_terms+1):
        series.append((i,ak.subs(k, i), bk.subs(k, i)))

    return ak.subs(k,0),series


def convert_to_sympy_function(fx_string):
    # Replace 'cos' with 'sp.cos'
    fx_string = re.sub(r'cos', r'sp.cos', fx_string)
    # Replace 'sin' with 'sp.sin'
    fx_string = re.sub(r'sin', r'sp.sin', fx_string)
    # Replace 'j' preceded by a number with '* sp.I'
    fx_string = re.sub(r'(\d+)j', r'\1 * sp.I', fx_string)
    # Replace 'j' without any number with '* sp.I'
    fx_string = re.sub(r'j', r'sp.I', fx_string)
    # Replace 'e **' or 'e**' with 'sp.exp'
    fx_string = re.sub(r'e\s*\*\*\s*', r'sp.exp', fx_string)
    # Replace 'log10' with 'sp.log(expr, 10)'
    fx_string = re.sub(r'log', r'sp.log', fx_string)
    print(fx_string)
    return fx_string

def sympy_f(x):
    return (eval(convert_to_sympy_function(integration_function.get())) * (sp.exp(w*sp.I*x)))


# Reset Function
def reset():
    global plot_widget
    integration_function.delete(0,'end')
    lower_bound_entry.delete(0,'end')
    upper_bound_entry.delete(0,'end')
    cartesian_result_label.config(text='Cartesian : ')
    polar_result_label.config(text='Polar : ')
    analytical_result_label.config(text="Analytical result: ")
    accuracy.set(0.0005)
    X = []
    Y = []
    cla()
    axhline(0)
    axvline(0)
    plot([],[])
    fig.canvas.draw()

def instruction():

    instruction_window = tk.Toplevel(window)

    instruction_window.geometry('520x420+400+100')

    instruction_window.title('Instructions')
    
    w=tk.Listbox(instruction_window,bg=app_theme[0], font=("Arial",14))
    s='''
    Note eact zeroes are not given instead
    a value very close to zero is given.

    you must write code like if you assign it in a python varible
    ex:
        cosx = cos(x)
        sinx = sin(x)
        tanx = tan(x)
        cos^-1 x = acos(x)
        sin^-1 x = asin(x)
        tan^-1 x = atan(x)
        log(10) = log(10,2)
        expon. = e
        pi = pi
        w0 of fourier = w0
        w0 of integration w
        I = 1j
    '''
    s=s.split('\n')
    for c in range(len(s)):
        w.insert(c+1,s[c])
    w.pack(fill='both',expand='yes')

def history():
    
    history_window = tk.Toplevel(window)
    history_window.geometry('520x420+400+100')
    history_window.title('History')

    w=tk.Listbox(history_window,bg=app_theme[0], font=("Arial",14))
    try:
        f=open('history.txt','r')
        s=f.read()
        f.close()
    except:
        f=open('history.txt','w')
        f.close()
        s=''
    s=s.split('\n')
    for c in range(len(s)):
        w.insert(c+1,s[c])
    w.pack(fill='both',expand='yes')

def my_fourier_window(s):

    my_fourier_window=tk.Toplevel(window)
    my_fourier_window.geometry('520x420+400+100')

    my_fourier_window.title('my_fourier_Sequence')
    
    w=tk.Listbox(my_fourier_window,bg=app_theme[0], font=("Arial",14))

    s=s.split('\n')
    for c in range(len(s)):
        w.insert(c+1,s[c])
    w.pack(fill='both',expand='yes')


    
def sympy_fourier_window(s):

    sympy_fourier_window=tk.Toplevel(window)
    sympy_fourier_window.geometry('520x420+400+100')

    sympy_fourier_window.title('sympy_fourier_Sequence')
    
    w=tk.Listbox(sympy_fourier_window,bg=app_theme[0], font=("Arial",14))

    s=s.split('\n')
    for c in range(len(s)):
        w.insert(c+1,s[c])
    w.pack(fill='both',expand='yes')

# Create a Tkinter window
window = tk.Tk()
window.geometry("1200x710")
window.title("Signals Assignment")
window.resizable(0,0)

app_theme = ("#aaaaaa","white","#FF5733","#33B9FF")

tk.Frame(window,width=1200,height=100,bg=app_theme[1]).place(x=0,y=0)
tk.Label(window,text='Signals Assignment',font=('Algerian','26','bold'),bg=app_theme[1],fg='black').place(x=20,y=25)

tk.Frame(window,width=1600,height=820,bg=app_theme[0]).place(x=0,y=100)

tk.Button(window,text='Instruction',command= instruction,width=9,height=2,bg=app_theme[3],fg=app_theme[1],font=('Arial','9','bold')).place(x=25,y=110)
tk.Button(window,text='History',command= history, width=9,height=2,bg=app_theme[3],fg=app_theme[1],font=('Arial','9','bold')).place(x=110,y=110)
tk.Label(window,text='@Eshik-X',font=("Arial",16,'bold'),bg=app_theme[0],fg=app_theme[1]).place(x=1070,y=110)

tk.Label(window,text='S',font=('Berlin Sans FB Demi','100','bold'),bg=app_theme[0],fg=app_theme[1]).place(x=50,y=190)
tk.Label(window,text='f(x) = ',font=('Berlin Sans FB Demi','36','bold'),bg=app_theme[0],fg=app_theme[1]).place(x=130,y=240)

integration_function=tk.Entry(window,width=20,font=('Arial',20))
integration_function.place(x=260,y=255)

upper_bound_entry=tk.Entry(window,width=4,font=('Arial',15,'bold'))
upper_bound_entry.place(x=60,y=183)

lower_bound_entry=tk.Entry(window,width=4,font=('Arial',15,'bold'))
lower_bound_entry.place(x=60,y=330)

tk.Label(window,text='dx',font=('Berlin Sans FB Demi','36','bold'),bg=app_theme[0],fg=app_theme[1]).place(x=570,y=240)

ans_label=tk.Label(window,text='Answer: ',font=('Berlin Sans FB Demi','22','bold'),bg=app_theme[0],fg=app_theme[1])
ans_label.place(x=50,y=550)

# Labels for displaying results
cartesian_result_label = tk.Label(window, text="Cartesian : ",font=('Berlin Sans FB Demi','12','bold'))
cartesian_result_label.place(x=80,y=600)

polar_result_label = tk.Label(window, text="Polar : ",font=('Berlin Sans FB Demi','12','bold'))
polar_result_label.place(x=80,y=630)

analytical_result_label = tk.Label(window, text="Analytical : ",font=('Berlin Sans FB Demi','12','bold'))
analytical_result_label.place(x=80,y=660)

accuracy=tk.Scale(window,bg=app_theme[0],fg=app_theme[1],from_=0.001,to=0.00001,resolution=0.00001,orient='horizontal',length=250,relief='groove',label=' <== SPEED                  ::         ACCURACY ==>   ',activebackground=app_theme[0])
accuracy.set(0.0005)
accuracy.place(x=45,y=450)

tk.Button(window,bg=app_theme[2],command=reset,fg=app_theme[1],text='Reset',width=8,height=2,activebackground=app_theme[0] ,font=('Arial','9','bold')).place(x=355,y=470)

tk.Button(window,command = integrate_function,bg=app_theme[3],fg=app_theme[1],text='Integrate',width=8,height=2,activebackground=app_theme[0],font=('Arial','9','bold')).place(x=435,y=470)


use('TkAgg')
fig=figure(1,figsize=(5,5))
canvas=FigureCanvasTkAgg(fig,master=window)
plot_widget=canvas.get_tk_widget()

axhline(0)
axvline(0)

plot([],[])


plot_widget.place(x=650,y=165)


# Main Loop
window.mainloop()