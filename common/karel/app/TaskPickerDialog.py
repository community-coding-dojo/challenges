import os
from pathlib import Path
import tkinter as tk
from tkinter.simpledialog import Dialog
from tkinter import Listbox, StringVar
from tkinter.ttk import Button, Frame
from typing import NoReturn, Tuple


class TaskPickerDialog:

    def __init__(self):
        self.listbox = None
        self.karel_paths = {}
        self.karel_tasks = {}
        self.selection = (None, None, None)
        self.root = tk.Tk()

        self.repo_path = Path(__file__).parent.parent.parent.parent

        for difficulty in ['beginner', 'intermediate']:
            self.karel_paths[difficulty] = self.repo_path / difficulty / 'karel'
        self.master = Frame(self.root)
        self.body(self.master)
        self.buttonbox(self.master)
        self.master.pack()

    def body(self, master) -> NoReturn:
        self.karel_tasks = []
        for difficulty, path in self.karel_paths.items():
            self.karel_tasks.append({"value": f"-- difficulty --", "path": None, "difficulty": difficulty})
            for p in (path / 'solutions').glob("*.py"):
                self.karel_tasks.append({"value": p.stem, "path": p, "difficulty": difficulty})

        options = StringVar(value=[])
        self.listbox = Listbox(master=master, height=max(len(self.karel_tasks), 20), listvariable=options)
        self.listbox.pack()
        task_names = []
        for item in self.karel_tasks:
            task_names.append(item['value'])
        options.set(task_names)

    def buttonbox(self, master) -> NoReturn:
        ok_button = Button(master=master, text="Ok", command=self.save_selection_and_close)
        ok_button.pack()

    def save_selection_and_close(self) -> NoReturn:
        if len(self.listbox.curselection()) == 0:
            print("No task selected!")
            return

        selection = self.karel_tasks[self.listbox.curselection()[0]]
        if selection['path'] is None:
            print("Invalid selection!")
            return

        task_path = self.repo_path / selection['path']
        worlds_dir = self.repo_path / selection['difficulty'] / 'karel' / 'worlds'
        world_path = worlds_dir / (selection['value'] + '.w')
        goal_path = worlds_dir / (selection['value'] + '.goal')
        self.root.destroy()
        self.selection = (task_path, world_path, goal_path)

    def run(self) -> Tuple[Path, Path, Path]:
        self.root.mainloop()
        return self.selection
