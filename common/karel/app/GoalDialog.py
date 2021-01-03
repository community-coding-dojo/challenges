from stanfordkarel.karel import Karel
from stanfordkarel.karel_application import KarelCanvas
from tkinter import ttk, Toplevel
import tkinter as tk


class GoalDialog(Toplevel):

    def __init__(self, goal_file, parent=None, refresh_fn=None):
        super().__init__(parent)
        self.goal_file = goal_file
        self.refresh_fn = refresh_fn
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
        if self.refresh_fn is not None:
            refresh_button = ttk.Button(self, text="Refresh Program", command=self.refresh_fn)
            refresh_button.pack()
