import numpy as np, sympy as sp
from sympy import *
from IPython.display import display, Math
import itertools

def format_complex_number(val):
    """Formats a complex number into a more readable form for LaTeX."""
    if val.imag == 0:
        return str(float(val.real)) 
    elif val.real == 0:
        if val.imag == 1:
            return 'i'
        elif val.imag == -1:
            return '-i'
        else:
            return f"{val.imag}i"  
    else:
        return f"{val.real}+{val.imag}i" 

def numpy_array_to_latex(array):
    ''' converts any numpy array, complex or real, to a Latex pmatrix'''
    latex_str = r'\begin{pmatrix}'
    for row in array:
        row_str = ' & '.join(format_complex_number(val) for val in row)
        latex_str += row_str + r' \\ '
    latex_str = latex_str.rstrip(r' \\ ')  # Remove the last row separator
    latex_str += r'\end{pmatrix}'
    return latex_str

sigma = {'z' : np.array([[1,0],[0,-1]]),
         'x' : np.array([[0,1],[1,0]]),
         'y' : np.array([[0,0-1j],[0+1j,0]])
         }

spin = {'u': np.array([1,0]).reshape(-1,1),
        'd': np.array([0,1]).reshape(-1,1)
        }

t, p = symbols('t p')

P = Matrix([[cos(t), sin(t)*cos(p) - I*sin(t)*sin(p)],
            [sin(t)*cos(p) + I*sin(t)*sin(p), -cos(t)]])