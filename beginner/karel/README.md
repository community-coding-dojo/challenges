# Karel the Robot

**Author**: [theCalcaholic][1]

## Description

In this challenge, you take control over Karel, a little robot, which has to solve various tasks.

![karel-screenshot][5]

### Concepts and libraries you should be familiar with:

- functions (limited understanding sufficient)
- loops (task 02 and later)
- virtual environments (venv) (recommended, not required)

## Setup

*The following instructions assume that you are currently in the beginner/karel directory.*

### Linux

1. Install the package python3-tk. For example, on Ubuntu: 
    ```sh
    apt install python3-tk
    ```
2. Install the dependencies for the karel challenges with the following command.
   [Creating and activating a virtual environment is recommended][3]
   ```sh
   pip install -r requirements.txt
   ```


### Windows

1. Install the dependencies for the karel challenges with the following command.
   [Creating and activating a virtual environment is recommended][3]
   ```sh
   pip install -r requirements.txt
   ```


**All challenges require the [essentials][2] to be set up!**

## Run

To run and test your solutions to the various Karel tasks, execute the following command:

```sh
python ./run.py
```

A dialog will open, showing you all the Karel tasks. Select the one you want to run and confirm.
Now you will be presented two windows: One shows the state of the map after you have solved the task (Karel Goal) and
the other one shows the solution runner, where you can see your script in action.

## Task

You will find multiple python scripts in the solutions folder. These act as solution templates and contain 
further instructions on how to solve each task.

Within all solutions, you are given access to a number of functions which control the behaviour of Karel the robot:


| Karel Commands       |                        |                          |
| -------------------- | ---------------------- | ------------------------ |
| `move()`             | `right_is_clear()`     | `facing_east()`          |
| `turn_left()`        | `right_is_blocked()`   | `not_facing_east()`      |
| `put_beeper()`       | `beepers_present()`    | `facing_west()`          |
| `pick_beeper()`      | `no_beepers_present()` | `not_facing_west()`      |
| `front_is_clear()`   | `beepers_in_bag()`     | `facing_south()`         |
| `front_is_blocked()` | `no_beepers_in_bag()`  | `not_facing_south()`     |
| `left_is_clear()`    | `facing_north()`       | `paint_corner(color)`    |
| `left_is_blocked()`  | `not_facing_north()`   | `corner_color_is(color)` |

For most tasks, only a subset of these commands will be required. This subset will usually be
explained within the solution template.

## Run the program

After you have written your code you first need to run (and save) it in your programming software
before you can open and run the visual game.

----

Further information on Karel (and more examples) can be found [here][4]

---

# GLHF!

[1]: https://github.com/theCalcaholic
[2]: ../../docs/Essentials.md
[3]: ../../docs/venv.md
[4]: https://compedu.stanford.edu/karel-reader/docs/python/en/intro.html
[5]: karel_screenshot.png
