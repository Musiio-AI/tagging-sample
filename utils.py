import tkinter as tk
from tkinter import Frame, StringVar

class Checkbar(Frame):

   def __init__(self, parent=None, picks=[], side='left', anchor='w'):
      """
      Initialises a row of checkboxes
      :param parent: - The tkinter parent object
      :param picks: list - A list of strings with each string representing the text to display for a checkbox
      """

      Frame.__init__(self, parent)
      self.vars = []

      for pick in picks:
         var = tk.IntVar(value=1)
         check = tk.Checkbutton(self, text=pick, variable=var)
         check.pack(side=side, anchor=anchor, expand='yes')
         self.vars.append(var)

   def state(self):
      """
      :return: map representing the state of each checkbox, 1 or 0
      """
      return map((lambda var: var.get()), self.vars)


def checkTextboxInput(textbox, selection_str):
   """
   Checks to see if the textbox input is different from the selection and if so, makes the selection the textbox input
   :param textbox: - A tkinter Entry object
   :param selection_str: str - A string representing the selection made by the user
   :return: output: string
   """
   output = selection_str

   text = StringVar()
   textinput = textbox.get()
   text.set(textinput)
   text_str = text.get()

   if text_str != selection_str:
      output = text_str

   return output


def processCheckboxes(checkboxes, options):
   """
   Process the GUI checkboxes and return a list containing strings denoting which boxes were checked
   :param checkboxes: list - A list of Checkbar objects
   :param options: list - A list of all options represented by this group of checkboxes
   :return: tag_selection: list - A list containing the type of tags to tag the track for
   """

   tag_selection_bin = list()
   tag_selection = list()
   for checkbox in checkboxes:
      tag_selection_bin += list(checkbox.state())

   for i, tag in enumerate(tag_selection_bin):
      if tag:
         tag_selection.append(options[i])

   return tag_selection