import os
import tkinter as tk
from tkinter import ttk
import subprocess

from .utils import unix_time_to_yyyy_mm_dd


def display_projects(directory: str, executable: str) -> None:
    """
    Displays project folders in the project directory using Tkinter.

    Args:
    - directory (str): The path to the directory containing the projects.
    - executable (str): The program to execute for opening a selected project.
    """
    app = ProjectSelector(directory, executable)
    app.mainloop()


class ProjectSelector(tk.Tk):
    def __init__(self, directory: str, executable: str):
        super().__init__()
        self.title("Folder Selector")
        self.directory = directory
        self.executable = executable
        self.sort_orders: dict[str, str] = {}
        self.setup_ui()
        self.sort_tree("Last Modified")

    def setup_ui(self) -> None:
        self.title("Project Hopper")

        self.tree = ttk.Treeview(self, columns=("Folder Name", "Path", "Last Modified"))
        self.tree.heading("#0")
        self.tree.heading("Folder Name", text="Folder Name", command=lambda: self.sort_tree("Folder Name"))
        self.tree.heading("Path", text="Path", command=lambda: self.sort_tree("Path"))
        self.tree.heading("Last Modified", text="Last Modified", command=lambda: self.sort_tree("Last Modified"))

        self.tree.column("#0", width=0)
        self.tree.column("Folder Name", stretch=tk.YES, anchor=tk.W)
        self.tree.column("Path", stretch=tk.YES)
        self.tree.column("Last Modified", stretch=tk.YES, anchor=tk.CENTER)

        self.tree.bind("<Double-1>", self.on_double_click)  # type: ignore

        self.tree.pack(expand=tk.YES, fill=tk.BOTH)

        self.populate_treeview()

    def populate_treeview(self) -> None:
        iid = 0
        for folder in os.listdir(self.directory):
            folder_path = os.path.join(self.directory, folder)
            if os.path.isdir(folder_path):
                last_modified = self.get_last_modified(folder_path)
                self.tree.insert("", "end", text=folder_path, values=(folder, folder_path, last_modified))
                iid += 1

    def get_last_modified(self, folder: str) -> str:
        unix_time = os.path.getmtime(folder)
        return unix_time_to_yyyy_mm_dd(unix_time)

    def on_double_click(self, event) -> None:  # type: ignore
        item = self.tree.selection()[0]
        selected_folder = self.tree.item(item, "values")[1]
        subprocess.Popen([self.executable, selected_folder], shell=True, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.quit()

    def sort_tree(self, column_name: str) -> None:
        current_order = self.sort_orders.get(column_name, "ascending")
        if current_order == "ascending":
            order = "descending"
        else:
            order = "ascending"
        children = [(self.tree.set(child, column_name).lower(), child) for child in self.tree.get_children("")]
        children.sort(reverse=(order == "descending"))
        for index, (_, child) in enumerate(children):
            self.tree.move(child, "", index)
        self.sort_orders[column_name] = order  # Update sorting order for the column
        self.tree.heading(column_name, command=lambda: self.sort_tree(column_name), anchor="w")
