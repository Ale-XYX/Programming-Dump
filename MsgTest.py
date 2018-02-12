import tkinter as tk
import tkinter.messagebox as tkm
import traceback

tkm.showinfo('Complete', 'Created entry!')

try:
    prin('Hello world')
except:
    tkm.showinfo('Failed!', traceback.format_exc())
        
