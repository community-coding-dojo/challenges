import sys
import os
from os import path
from pathlib import Path
import re
import tkinter as tk
from tkinter import filedialog
from typing import Tuple, NoReturn
from stanfordkarel.karel import Karel
from stanfordkarel.karel_application import KarelApplication
from app import GoalDialog, TaskPickerDialog


def get_task_selection(solutions_path, pattern="") -> Tuple[Path, Path, Path]:
    if len(sys.argv) >= 2:
        task_path = Path(sys.argv[1])
        world_dir = task_path.parent.parent / 'worlds'
        world_path = world_dir / task_path.stem + '.w'
        goal_path = world_dir / task_path.stem + '.goal'
        return task_path, world_path, goal_path
    else:
        # solution_file = filedialog.askopenfilename(master=dialog_root, initialdir=solutions_path,
        #                                            filetypes=[("Python file", "*.py")],
        #                                            title="Select your solution")
        # dialog_root.destroy()

        task_picker = TaskPickerDialog()
        return task_picker.run()


def get_karel_app(solution_file=None, world_file="", master=None):
    # Extract the name of the file the student is executing

    # Can uncomment this code to allow the file name to match the intended file
    # if world_file is None:
    #     base_filename = os.path.basename(student_code_file)
    #     world_file = os.path.splitext(base_filename)[0]

    # Create Karel and assign it to live in the newly created world
    karel = Karel(world_file)

    # Initialize root Tk Window and spawn Karel application
    root = tk.Tk() if master is None else master
    return KarelApplication(karel, solution_file, master=root)


def count_karel_commands(solution_file: Path) -> int:

    with solution_file.open('r') as handle:
        code = handle.read()

        code = re.sub(r'#.*\n', "", code)
        code = "".join(re.split(r'"""', code)[::2])

        karel_commands = [
            "move",
            "turn_left",
            "pick_beeper",
            "put_beeper",
            "facing_north",
            "facing_south",
            "facing_east",
            "facing_west",
            "not_facing_north",
            "not_facing_south",
            "not_facing_east",
            "not_facing_west",
            "front_is_clear",
            "beepers_present",
            "no_beepers_present",
            "beepers_in_bag",
            "no_beepers_in_bag",
            "front_is_blocked",
            "left_is_blocked",
            "left_is_clear",
            "right_is_blocked",
            "right_is_clear",
            "paint_corner",
            "corner_color_is",
        ]
        total_count = 0
        for command in karel_commands:
            total_count += code.count(command)
        return total_count


if __name__ == "__main__":
    repo_dir = path.join(path.dirname(__file__), os.pardir, os.pardir)
    task_file, world_file, goal_file = get_task_selection(path.join(repo_dir, 'beginner', 'karel', 'solutions'))

    if task_file is None:
        print("User aborted. Exiting...")
        exit(0)

    print(f"Your Karel command score is: {count_karel_commands(task_file)}")

    root = tk.Tk()
    # worlds_path = path.join(repo_dir, "beginner", "karel", "worlds")
    # world_file_base = path.join(worlds_path, path.splitext(path.basename(solution_file))[0])
    # world_file = world_file_base + ".w"
    # goal_file = world_file_base + ".goal"
    if not world_file.is_file():
        print(f"WARNING: Could not find world file {world_file}! Please name your solution in accordance with the "
              f"world file.")

    print(f"solution: {task_file}, world: {world_file}")

    app = get_karel_app(str(task_file), world_file=str(world_file.absolute()), master=root)

    def reset_app() -> NoReturn:
        global app
        app.pack_forget()
        app.destroy()
        app = get_karel_app(str(task_file), world_file=str(world_file), master=root)


    if goal_file.is_file():
        goal_dialog = GoalDialog(str(goal_file), parent=root, refresh_fn=reset_app)
    else:
        print(f"WARNING: No goal definition found!")

    app.mainloop()
