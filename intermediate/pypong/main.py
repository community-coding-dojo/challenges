#!/usr/bin/env python3

###############
# DO NOT EDIT #
###############

# This is the start script for your game. It set's up an environment for your pong game.
# You don't need to change anything here, all your code goes into pong/core.py
# (of course you can add more files if you like to)
# Start the program with python3 main.py

from threading import Thread
from tkinter import Tk, Canvas

from pong import game_loop, key_down, key_up

canvas_width = 1280
canvas_height = 960


class SignalContainer(object):
    def __init__(self):
        self.Code = -1


app = Tk()

canvas = Canvas(app, height=canvas_height, width=canvas_width)

app.bind("<KeyPress>", key_down)
app.bind("<KeyRelease>", key_up)

signal = SignalContainer()
game_thread = Thread(target=game_loop, args=(canvas, signal))

game_thread.start()

canvas.pack()
app.mainloop()
signal.Code = 0
game_thread.join()
