import numpy as np, sympy as sp
from sympy import *
from IPython.display import display, Math

# making it pretty
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
    latex_str = r'\begin{pmatrix}'
    for row in array:
        row_str = ' & '.join(format_complex_number(val) for val in row)
        latex_str += row_str + r' \\ '
    latex_str = latex_str.rstrip(r' \\ ')  # Remove the last row separator
    latex_str += r'\end{pmatrix}'
    return latex_str

pauli = {'Oz' : np.array([[1,0],[0,-1]]),
         'Ox' : np.array([[0,1],[1,0]]),
         'Oy' : np.array([[0,0-1j],[0+1j,0]])
         }