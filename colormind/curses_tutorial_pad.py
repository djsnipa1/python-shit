# coding=utf-8
"""
Tutorial from here:
Curses in Windows with Python | DevDungeon
https://www.devdungeon.com/content/curses-windows-python
"""
import curses

screen = curses.initscr()
# Make a pad 100 lines tall 20 chars wide
# Make the pad large enough to fit the contents you want
# You cannot add text larger than the pad
# We are only going to add one line and barely use any of the space
pad = curses.newpad(100, 100)
pad.addstr("This text is thirty characters.")

# Start printing text from (0,2) of the pad (first line, 3rd char)
# on the screen at position (5,5)
# with the maximum portion of the pad displayed being 20 chars x 15 lines
# Since we only have one line, the 15 lines is overkill, but the 20 chars
# will only show 20 characters before cutting off
pad.refresh(0, 2, 5, 5, 15, 20)

curses.napms(5000)
curses.endwin()
