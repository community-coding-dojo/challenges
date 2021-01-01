import sys
from os import path, listdir
import tkinter as tk
from tkinter import ttk, Toplevel, filedialog
from stanfordkarel.karel import Karel
from stanfordkarel.karel_application import KarelApplication, KarelCanvas


def get_solution_file(solutions_path, pattern=""):
    solution_file = None
    if len(sys.argv) >= 2:
        solution_file = sys.argv[1]
    else:
        # options = [option for option in listdir(solutions_path) if option.startswith(pattern)]
        # if len(options) == 1:
        #     solution_file = options[0]
        # else:
        root = tk.Tk()
        solution_file = filedialog.askopenfilename(master=root, initialdir=solutions_path,
                                                   filetypes=[("Python file", "*.py")],
                                                   title="Select your solution")
        root.destroy()

    # elif path.isfile("00_karel_intro.py"):
    #     solution_file = "00_karel_intro.py"
    # else:
    #     solution_file = input("Please enter the path to your 00_karel_intro.py: ")

    return solution_file


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


class GoalDialog(Toplevel):

    def __init__(self, goal_file, parent=None):
        super().__init__(parent)
        self.goal_file = goal_file
        body = ttk.Frame(self, width=620, height=440)
        self.initial_focus = self.body(body)
        body.pack(expand=True, fill=tk.BOTH)
        self.buttonbox()
        if not self.initial_focus:
            self.initial_focus = self
        self.geometry("620x480+20+20")
        self.initial_focus.focus_set()
        self.canvas.redraw_all()

    def body(self, master):
        description_label = ttk.Label(master, text="This is how the map should look like, after you solved the "
                                                   "challenge:")
        description_label.pack()
        karel = Karel(self.goal_file)
        self.canvas = KarelCanvas(600, 400, master=master, world=karel.world, karel=karel)
        #canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.config(width=600, height=400)
        self.canvas.pack()

    def buttonbox(self):
        ok_button = ttk.Button(self, text="Okay", command=self.destroy)
        ok_button.pack()


if __name__ == "__main__":
    solution_file = get_solution_file(path.join(path.dirname(__file__), 'solutions'))
    root = tk.Tk()
    worlds_path = path.join(path.dirname(__file__), "worlds")
    world_file_base = path.join(worlds_path, path.splitext(path.basename(solution_file))[0])
    world_file = world_file_base + ".w"
    goal_file = world_file_base + "_end.w"
    if not path.isfile(world_file):
        print(f"WARNING: Could not find world file {world_file}! Please name your solution in accordance with the world "
              f"file.")

    print(f"solution: {solution_file}, world: {world_file}")

    app = get_karel_app(solution_file, world_file=world_file, master=root)

    if path.isfile(goal_file):
        goal_dialog = GoalDialog(goal_file, parent=root)
    else:
        print(f"WARNING: No goal definition found!")

    app.mainloop()
