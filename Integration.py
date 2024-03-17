import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.pyplot import figure,plot,axhline,axvline,cla
from matplotlib import use
from math import *

# Define Omega Var & the needed Function
w = complex(-1/2, sqrt(3)/2)

# (cos(x) + 6j * sin(2*x))
# ( e ** (w * 1j * x))

# Define the function f(x)
def f(x):
    return eval(integration_function.get())
    # return (cos(x) + 6j * sin(2*x)) * ( e ** (w * 1j * x))

# Trapezoidal rule for numerical integration
def integrate(l_bound, u_bound, dx):

    answer = 0.0
    flag = 0

    X = []
    Y = []

    if l_bound > u_bound:
        l_bound,u_bound = u_bound,l_bound
        print(l_bound,u_bound)
        flag = 1

    while l_bound <= u_bound:

        try: 
            y = f(l_bound)
            limit_at_a_point = y * dx
            X.append(l_bound)
            Y.append(y)
            answer += limit_at_a_point

        except:
            print("something went wrong")

        l_bound += dx

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
        l_bound = float(lower_bound.get())
        u_bound = float(upper_bound.get())

        dx = float(accuracy.get())

        integral = integrate(l_bound, u_bound, dx)
        print(integral)

        cartesian_result_label.config(text="Cartesian : "+ str(integral))
        polar_result_label.config(text="Polar : " + str(abs(integral)) + " * exp(" + str(atan2(integral.imag, integral.real)) + "j)")
        # analytical_result = (np.sin(b) - np.sin(a) + 6j * (2 * np.cos(2*b) - 2 * np.cos(2*a))) / (1 + 24)
        # analytical_result_label.config(text="Analytical result: " + str(analytical_result))

        f=open('history.txt','a')
        f.write('\n'+str(integration_function.get())+'\n'+'Lower: '+str(lower_bound.get())+'\n'+'Upper: '+str(upper_bound.get())+'\n'+'Cartesian = '+str(integral)+'\n'+'\n'+'Polar = '+str(abs(integral)) + " * exp(" + str(atan2(integral.imag, integral.real)) + "j)"+'\n')
        f.close()

    except Exception as e:
        messagebox.showerror("Error", "Invalid input or function: " + str(e))

# Reset Function
def reset():
    global plot_widget
    integration_function.delete(0,'end')
    lower_bound.delete(0,'end')
    upper_bound.delete(0,'end')
    cartesian_result_label.config(text='Cartesian : ')
    polar_result_label.config(text='Polar : ')
    accuracy.set(0.0005)
    cla()
    axhline(0)
    axvline(0)
    plot([],[])
    fig.canvas.draw()

def instruction():
    global rootB
    
    rootB=tk.Tk()
    rootB.geometry('480x300+400+100')

    rootB.title('Instructions')
    
    w=tk.Listbox(rootB,bg=app_theme[0])
    s='''
    Note eact zeroes are not given instead
    a value very close to zero is given.

    you must write code like if you assign it in a python varible
    '''
    s=s.split('\n')
    for c in range(len(s)):
        w.insert(c+1,s[c])
    #w.pack(expand='yes',fill='both')
    w.pack(fill='both',expand='yes')

    rootB.mainloop()

def history():
    global rootC
    
    rootC=tk.Tk()
    rootC.geometry('480x300+400+100')
    rootC.title('History')

    w=tk.Listbox(rootC,bg=app_theme[0])
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
    #w.pack(expand='yes',fill='both')
    w.pack(fill='both',expand='yes')

    rootC.mainloop()

# Create a Tkinter window
window = tk.Tk()
window.geometry("1200x700")
window.title("Signals Assignment")
window.resizable(0,0)

app_theme = ("#aaaaaa","white","#FF5733","#33B9FF")

tk.Frame(window,width=1200,height=100,bg=app_theme[1]).place(x=0,y=0)
tk.Label(window,text='Signals Assignment',font=('Algerian','26','bold'),bg=app_theme[1],fg='black').place(x=20,y=25)

tk.Frame(window,width=1600,height=700,bg=app_theme[0]).place(x=0,y=100)

tk.Button(window,text='Instruction',command= instruction,width=9,height=2,bg=app_theme[3],fg=app_theme[1],font=('Arial','9','bold')).place(x=25,y=110)
tk.Button(window,text='History',command= history, width=9,height=2,bg=app_theme[3],fg=app_theme[1],font=('Arial','9','bold')).place(x=110,y=110)
tk.Label(window,text='@Eshik-X',font=("Arial",16,'bold'),bg=app_theme[0],fg=app_theme[1]).place(x=1070,y=110)

tk.Label(window,text='S',font=('Berlin Sans FB Demi','100','bold'),bg=app_theme[0],fg=app_theme[1]).place(x=50,y=190)
tk.Label(window,text='f(x) = ',font=('Berlin Sans FB Demi','36','bold'),bg=app_theme[0],fg=app_theme[1]).place(x=130,y=240)

integration_function=tk.Entry(window,width=20,font=('Arial',20))
integration_function.place(x=260,y=255)

upper_bound=tk.Entry(window,width=4,font=('Arial',15,'bold'))
upper_bound.place(x=60,y=183)

lower_bound=tk.Entry(window,width=4,font=('Arial',15,'bold'))
lower_bound.place(x=60,y=330)

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