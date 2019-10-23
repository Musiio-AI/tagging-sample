import tkinter as tk
from tkinter import Frame

class Checkbar(Frame):

   def __init__(self, parent=None, picks=[], side='left', anchor='w'):

      Frame.__init__(self, parent)
      self.vars = []

      for pick in picks:
         var = tk.IntVar(value=1)
         check = tk.Checkbutton(self, text=pick, variable=var)
         check.pack(side=side, anchor=anchor, expand='yes')
         self.vars.append(var)

   def state(self):

      return map((lambda var: var.get()), self.vars)