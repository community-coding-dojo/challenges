from time import sleep

# You can define configuration variables here.
bg_color = "#AAAAAA"

# If you need to change a configuration variable from within a function, you need to
# declare a global variable with the same name inside the function. Otherwise, the variable will be read-only
# (inside the function). For example, let's write a function which can change the bg_color variable:


def change_bg_variable():
    global bg_color
    bg_color = "#BBBBBB"


def game_loop(canvas, signal=None):
    # The canvas is where your game happens. You can, for example draw shapes on it and move them around
    canvas.configure(bg=bg_color)  # <-- This sets the canvas' background color

    # This draws a circle on the canvas. You can pass the coordinates of any opposing corners to define it's size
    # and position:
    circle = canvas.create_oval((100, 100,  # <-- top-left corner coordinates
                                 120, 120   # <-- bottom-right corner coordinates
                                 ), fill='blue', outline="black")

    # let's wait a few seconds:
    sleep(3)
    # You can move elements on the canvas like this:
    canvas.move(circle, 30, 0)

    # If you want to find out more about the canvas and it's functions, search the internet for 'tkinter canvas'
    # or have a look at the official documentation at https://tkdocs.com/tutorial/canvas.html

    while signal is None or signal.Code < 0:
        # Here goes the game's main loop. The signal variable is just used to tell the game loop to terminate,
        # e.g. when the window is closed.
        # You can ignore it for now, since it already does everything it's supposed to
        pass


def key_down(event):
    # Whenever a key is pressed down, this method will be called.
    print("Key pressed: '{}'".format(event.keysym))


def key_up(event):
    # Whenever a pressed key is being released, this method will be called
    print("Key released: '{}'".format(event.keysym))

    # You can use it to react to user input
    if event.keysym == 'space':
        print("SPACE")
