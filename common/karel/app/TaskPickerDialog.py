from pathlib import Path
import tkinter as tk
from tkinter import Listbox, StringVar
from tkinter.ttk import Frame
from tkinter import Event
from typing import NoReturn, Tuple, Union


class TaskPickerDialog:

    def __init__(self):
        self.karel_paths = {}
        self.karel_tasks = {}
        self.selection = (None, None, None)
        self.root = tk.Tk()
        self.root.title = 'Choose a task'

        self.repo_path = Path(__file__).parent.parent.parent.parent

        for difficulty in ['beginner', 'intermediate', 'advanced']:
            self.karel_paths[difficulty] = self.repo_path / difficulty / 'karel'
        self.master = Frame(self.root)
        self.body(self.master)
        self.master.pack()

    def body(self, master) -> NoReturn:
        self.karel_tasks = []
        for difficulty, path in self.karel_paths.items():
            self.karel_tasks.append({"value": f"-- {difficulty} --", "path": None, "difficulty": difficulty})
            for p in (path / 'solutions').glob("*.py"):
                self.karel_tasks.append({"value": p.stem, "path": p, "difficulty": difficulty})

        options = StringVar(value=[])
        listbox = Listbox(master=master, height=max(len(self.karel_tasks), 20), listvariable=options)
        listbox.pack()
        task_names = []
        for item in self.karel_tasks:
            task_names.append(item['value'])
        options.set(task_names)

        listbox.bind("<<ListboxSelect>>", self.save_selection_and_close)

    def save_selection_and_close(self, event: Event) -> NoReturn:

        if len(event.widget.curselection()) == 0:
            print("No task selected!")
            return

        selection = self.karel_tasks[event.widget.curselection()[0]]
        if selection['path'] is None:
            print("Invalid selection!")
            return

        task_path = self.repo_path / selection['path']
        worlds_dir = self.repo_path / selection['difficulty'] / 'karel' / 'worlds'
        world_path = worlds_dir / (selection['value'] + '.w')
        goal_path = worlds_dir / (selection['value'] + '.goal')
        self.root.destroy()
        self.selection = (task_path, world_path, goal_path)

    def run(self) -> Union[Tuple[Path, Path, Path], Tuple[None, None, None]]:
        self.root.mainloop()
        return self.selection
