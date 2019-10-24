import tkinter as tk
from tkinter import filedialog, StringVar, messagebox, ttk
from tags_to_csv import sortTags
from utils import Checkbar
from constants import VALID_TAGS

def processText(tag):

    while tag[0] == " ":
        tag = tag[1:]

    while tag[-1] == " ":
        tag = tag[:-1]

    return tag

def selectTagFolder(event=None):

    filepath = filedialog.askdirectory()
    tagspath.set(filepath)


def selectCSVPath(event=None):

    csvpathinput = filedialog.askdirectory()
    csvpath.set(csvpathinput)


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
            tag_selection.append(VALID_TAGS[i])

    return tag_selection


def run(tagspath_str, csvpath_str, progress, checkboxes):

    tagspath_run = checkTextboxInput(tags_folder_textbox, tagspath_str)
    csvpath_run = checkTextboxInput(csv_directory_textbox, csvpath_str)

    tags_list = processCheckboxes(checkboxes)

    e = sortTags(tagspath_run, csvpath_run, tags_list, progress)

    if e:
        return messagebox.showerror("Error", e)

    return messagebox.showinfo("DONE", "DONE: CSV File 'tags.csv' located at: {}".format(csvpath_run))


if __name__ == '__main__':

    root = tk.Tk()
    root.title('Convert Tags to CSV')

    tagspath = StringVar()
    csvpath = StringVar()
    tags = StringVar()

    tagspath_str = str()
    csvpath_str = str()

    # Labels
    tk.Label(root, text="Tag Folder: ").grid(row=0)
    tk.Label(root, text='Write CSV to Directory: ').grid(row=1)

    # Textboxes
    tags_folder_textbox = tk.Entry(root, textvariable=tagspath, width=40)
    tags_folder_textbox.grid(row=0, column=1)

    csv_directory_textbox = tk.Entry(root, textvariable=csvpath, width=40)
    csv_directory_textbox.grid(row=1, column=1)

    # Progress Bar
    progress = ttk.Progressbar(root, length=120, mode="determinate")
    progress.grid(row=2, column=1, sticky='w')

    # Checkboxes
    tag_checkboxes1 = Checkbar(root, VALID_TAGS[:5])
    tag_checkboxes1.grid(row=0, column=5, sticky='w')
    tag_checkboxes2 = Checkbar(root, VALID_TAGS[5:10])
    tag_checkboxes2.grid(row=1, column=5, sticky='w')
    tag_checkboxes3 = Checkbar(root, VALID_TAGS[10:14])
    tag_checkboxes3.grid(row=2, column=5, sticky='w')
    tag_checkboxes4 = Checkbar(root, VALID_TAGS[14:])
    tag_checkboxes4.grid(row=3, column=5, sticky='w')

    checkboxes = [tag_checkboxes1, tag_checkboxes2, tag_checkboxes3, tag_checkboxes4]

    # Buttons
    button_tag_path = tk.Button(root, text='Select', command=selectTagFolder)
    button_tag_path.grid(row=0, column=2)

    button_tag_csv_path = tk.Button(root, text='Select', command=selectCSVPath)
    button_tag_csv_path.grid(row=1, column=2)

    button_generate_csv = tk.Button(root, text='Generate CSV File', command=lambda: run(tagspath_str, csvpath_str, progress, checkboxes))
    button_generate_csv.grid(row=2, column=1, sticky='e')

    button_run = tk.Button(root)

    root.mainloop()
