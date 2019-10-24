import tkinter as tk
from tkinter import filedialog, StringVar, messagebox, ttk
from generate_tags import Tagger
from constants import TAGS, KEY
from utils import Checkbar


def selectSourceFolder(event=None):

    filepath = filedialog.askdirectory()
    sourcepath.set(filepath)


def selectDestFolder(event=None):

    destpathinput = filedialog.askdirectory()
    destpath.set(destpathinput)


def checkTextboxInput(textbox, selection_str):

    output = selection_str

    text = StringVar()
    textinput = textbox.get()
    text.set(textinput)
    text_str = text.get()

    if text_str != selection_str:
        output = text_str

    return output

def processCheckboxes(checkboxes):

    tag_selection_bin = list()
    tag_selection = list()
    for checkbox in checkboxes:
        tag_selection_bin += list(checkbox.state())

    for i, tag in enumerate(tag_selection_bin):
        if tag:
            tag_selection.append(TAGS[i])

    return tag_selection


def run(sourcepath_str, destpath_str, api_key, progress, checkboxes):

    api_key_run = api_key.get()

    if len(api_key_run) == 0:
        return messagebox.showerror("Error", "API Key is not entered")

    tag_selection = processCheckboxes(checkboxes)

    t = Tagger()
    progress_str = StringVar()

    sourcepath_run = checkTextboxInput(source_textbox, sourcepath_str)
    destpath_run = checkTextboxInput(dest_textbox, destpath_str)

    progress_str.set('In Progress')
    progress_label = tk.Label(root, textvariable=progress_str)
    progress_label.grid(row=3, column=0)
    e = t.tagFilesTask(source_path=sourcepath_run, destination_path=destpath_run, tag_selection=tag_selection, progress=progress, progress_str=progress_str, api_key=api_key_run)

    if e:
        return messagebox.showerror("Error", e)

    progress_str.set('DONE')

    return messagebox.showinfo("DONE", "DONE: Tags located at: {}".format(destpath_run))


if __name__ == '__main__':

    root = tk.Tk()
    root.title('Generate Tags')

    sourcepath = StringVar()
    destpath = StringVar()
    api_key = StringVar(value=KEY)

    sourcepath_str = str()
    destpath_str = str()

    # Labels
    tk.Label(root, text="Source Folder: ").grid(row=0)
    tk.Label(root, text='Destination Folder: ').grid(row=1)
    tk.Label(root, text='API Key:').grid(row=2)

    # Textboxes
    source_textbox = tk.Entry(root, textvariable=sourcepath, width=40)
    source_textbox.grid(row=0, column=1)

    dest_textbox = tk.Entry(root, textvariable=destpath, width=40)
    dest_textbox.grid(row=1, column=1)

    api_textbox = tk.Entry(root, textvariable=api_key, width=40)
    api_textbox.grid(row=2, column=1)

    # Progress Bar
    progress = ttk.Progressbar(root, length=120, mode="determinate")
    progress.grid(row=3, column=1, sticky='w')
    progress['maximum'] = 100

    # Checkboxes
    tag_checkboxes1 = Checkbar(root, TAGS[:4])
    tag_checkboxes1.grid(row=0, column=5)
    tag_checkboxes2 = Checkbar(root, TAGS[4:])
    tag_checkboxes2.grid(row=1, column=5)
    checkboxes = [tag_checkboxes1, tag_checkboxes2]

    # Buttons
    button_tag_path = tk.Button(root, text='Select', command=selectSourceFolder)
    button_tag_path.grid(row=0, column=2)

    button_tag_csv_path = tk.Button(root, text='Select', command=selectDestFolder)
    button_tag_csv_path.grid(row=1, column=2)

    button_generate_csv = tk.Button(root, text='Generate Tags', command=lambda: run(sourcepath_str, destpath_str, api_key, progress, checkboxes))
    button_generate_csv.grid(row=2, column=5)

    button_run = tk.Button(root)

    root.mainloop()
