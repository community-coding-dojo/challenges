from stanfordkarel import *

"""
Karel has recently started a job as a road worker. It has been assigned to a road with multiple pot holes.
Help Karel to fix them up by placing beepers.

Thankfully, Karel has been equipped with an endless bag of beepers.

In the last task you may have noticed, that specifying all commands manually can be cumbersome.
In this task, try to find a cleverer solution. ;)

One more thing: In order to encourage clever, segmented code, we introduce a high score of Karel commands that are being
used per program. It is not relevant, how often they are called, but how often they appear in the code.
Lower is obviously better.
For your convenience, the Karel command score will be calculated for you when you execute run.py - have a look at the
console output.

==Leaderboard==

high score: ? Karel commands
"""

"""
In this task, Karel learns how to work on any street, not just specific ones.
Adapt the program you wrote the for the last task to work on this task's map as well (it should still work on the last
task's map - you can test this, by pressing 'Load Map' in the Karel application and selecting it).

To do this, you can use if conditions and loops to have Karel detect holes dynamically.  
"""


def main():
    #######################################################################################################
    # This function contains the code which will control the karel robot.                                 #
    # For this task you will need the following functions:                                                #
    #   move()              Move karel one field in the direction it is facing                            #
    #   turn_left()         Turn karel left (90 degrees)                                                  #
    #   beepers_present()   Returns True if Karel is standing on a beeper                                 #
    #   pick_beeper()       Makes Karel pick up the beeper it is standing on                              #
    #   put_beeper()        Makes Karel put a beeper at the current location                              #
    #   front_is_clear()    Returns True if Karel could move on the field it is facing                    #
    #   front_is_blocked()  Returns False if Karel could move on the field it is facing                   #
    #   right_is_clear()    Returns True if Karel could move on the field to its right (or 'beneath' it)  #
    #   right_is_blocked()  Returns False if Karel could move on the field to its right (or 'beneath' it) #
    #######################################################################################################
    pass
