import tkinter as tk
from tkinter import filedialog, StringVar, messagebox, ttk
from tags_to_csv import sortTags
from utils import Checkbar, checkTextboxInput, processCheckboxes
from constants import VALID_TAGS


def selectTagFolder(event=None):
    """
    Selects the source folder where tags are contained
    Executed by the 'Select' button
    """
    filepath = filedialog.askdirectory()
    tagspath.set(filepath)


def selectCSVPath(event=None):
    """
    Selects the destination folder where CSV file is to be saved
    Executed by the 'Select' button
    """
    csvpathinput = filedialog.askdirectory()
    csvpath.set(csvpathinput)


def run(tagspath_str, csvpath_str, progress, checkboxes):
    """
    Checks source, destination, API key, and checkboxes, and runs tagsFilesTask
    Executed by the 'Generate Tags' button
    :param tagspath_str: str - The selection made by the user for the tags source folder
    :param csvpath_str: str - The selection made by the user for the csv file destination folder
    :param progress: - tkinter Progressbar object
    :param checkboxes: list - A list of Checkbar objects
    :return: 'DONE' messagebox if successful, error message if not
    """

    tagspath_run = checkTextboxInput(tags_folder_textbox, tagspath_str)
    csvpath_run = checkTextboxInput(csv_directory_textbox, csvpath_str)

    tags_list = processCheckboxes(checkboxes, VALID_TAGS)

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
