import tkinter as tk
from tkinter import *
from tkinter import ttk

LARGE_FONT= ("Verdana", 12)

class PagePHProbes(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="pH Probes", font=LARGE_FONT)
        label.pack(side=TOP, pady=10, anchor=W)
