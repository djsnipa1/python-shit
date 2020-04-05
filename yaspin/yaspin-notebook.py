# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.1
#   kernelspec:
#     argv:
#     - C:\Users\Chad\.virtualenvs\python-shit-Hatrr_zd\Scripts\python.exe
#     - -m
#     - ipykernel_launcher
#     - -f
#     - '{connection_file}'
#     display_name: hydrogen-python-shit
#     language: python
#     name: hydrogen-python-shit
# ---

# + [markdown] nteract={"transient": {"deleting": false}}
# # yaspin notebook
# - - -
#

# + [markdown] nteract={"transient": {"deleting": false}}
# ### `import` libraries

# + jupyter={"source_hidden": false, "outputs_hidden": false} nteract={"transient": {"deleting": false}}
import time
from yaspin import yaspin

# Context manager:
with yaspin():
    time.sleep(3)  # time consuming code

# Function decorator:
@yaspin(text="Loading...")
def some_operations():
    time.sleep(30)  # time consuming code

some_operations()


# + jupyter={"source_hidden": false, "outputs_hidden": false} nteract={"transient": {"deleting": false}}

with yaspin().white.bold.shark.on_blue as sp:
    sp.text = "White bold shark in a blue sea"
    time.sleep(5)

sp.text = "chad"

# + jupyter={"source_hidden": false, "outputs_hidden": false} nteract={"transient": {"deleting": false}}
from random import randint

with yaspin(text="Loading", color="yellow") as spinner:
    time.sleep(2)  # time consuming code

    success = randint(0, 1)
    if success:
        spinner.ok(" ")
        print("OK")
    else:
        spinner.fail(" ")
        print("FAIL")


# + [markdown] nteract={"transient": {"deleting": false}}
# ### Call any spinner manually
#

# + jupyter={"source_hidden": false, "outputs_hidden": false} nteract={"transient": {"deleting": false}}
spinner = yaspin()
spinner.start()

time.sleep(3)  # time consuming tasks

spinner.stop()


# + [markdown] nteract={"transient": {"deleting": false}}
# ### Run any spinner from cli-spinners
# earth > moon > triangle > grenade
#

# + jupyter={"source_hidden": false, "outputs_hidden": false} nteract={"transient": {"deleting": false}}
from yaspin.spinners import Spinners

with yaspin(Spinners.earth, text="Earth") as sp:
    time.sleep(2)                # time consuming code

    # change spinner
    sp.spinner = Spinners.moon
    sp.text = "Moon"

    time.sleep(2)                # time consuming code

    sp.spinner = Spinners.triangle
    sp.text = "triangle"

    time.sleep(2)

    sp.spinner = Spinners.grenade
    sp.text = "grenade"

    time.sleep(2)


# + [markdown] nteract={"transient": {"deleting": false}}
# ### any color you like...
#

# + jupyter={"source_hidden": false, "outputs_hidden": false} nteract={"transient": {"deleting": false}}
with yaspin(text="Colors!") as sp:
    # Support all basic termcolor text colors
    colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

    for color in colors:
        sp.color, sp.text = color, color
        time.sleep(1)
        sp.spinner = Spinners.dots10


# + [markdown] nteract={"transient": {"deleting": false}}
# ### advanced color usage
#

# + jupyter={"source_hidden": false, "outputs_hidden": false} nteract={"transient": {"deleting": false}}
text = "Bold blink magenta spinner on cyan color"
with yaspin().bold.blink.magenta.bouncingBall.on_cyan as sp:
    sp.text = text
    time.sleep(3)


# + jupyter={"source_hidden": false, "outputs_hidden": false} nteract={"transient": {"deleting": false}}
# The same result can be achieved by passing arguments directly
with yaspin(
    Spinners.bouncingBall,
    color="magenta",
    on_color="on_cyan",
    attrs=["bold", "blink"],
) as sp:
    sp.text = text
    time.sleep(3)


# + [markdown] nteract={"transient": {"deleting": false}}
#

# + jupyter={"source_hidden": false, "outputs_hidden": false} nteract={"transient": {"deleting": false}}
from yaspin import yaspin, Spinner

# Compose new spinners with custom frame sequence and interval value
sp = Spinner(["😼", "😸", "😾", "😽", "😻", "😿", "💊", "💉", "🔫"], 200)

with yaspin(sp, text="Cat!"):
    time.sleep(3)  # cat consuming code :)


# + jupyter={"source_hidden": false, "outputs_hidden": false} nteract={"transient": {"deleting": false}}
sp_drugs = Spinner(["😦", "💊", "❗", "😅", "💊","❗","😅","💉","❗","💉"], 800)

with yaspin(sp_drugs, text="Drugs!"):
    time.sleep(10)  # cat consuming code :)


# + [markdown] nteract={"transient": {"deleting": false}}
# ## change spinner properties on the fly
#

# + jupyter={"source_hidden": false, "outputs_hidden": false} nteract={"transient": {"deleting": false}}
with yaspin(Spinners.noise, text="Noise spinner") as sp:
    time.sleep(2)

    sp.spinner = Spinners.arc  # spinner type
    sp.text = "Arc spinner"    # text along with spinner
    sp.color = "yellow"         # spinner color
    sp.side = "right"          # put spinner to the right
    sp.reversal = True

    time.sleep(2)


# + [markdown] nteract={"transient": {"deleting": false}}
# ### Writing messages
# You should not write any message in the terminal using print while spinner
# is open. To write messages in the terminal without any collision with yaspin 
# spinner, a ``.write()`` method is provided:
#

# + jupyter={"source_hidden": false, "outputs_hidden": false} nteract={"transient": {"deleting": false}}
with yaspin(text="Downloading images", color="cyan") as sp:
    # task 1
    time.sleep(2)
    sp.write("> image 1 download complete")

    # task 2
    time.sleep(2)
    sp.write("> image 2 download complete")

    # finalize
    sp.ok("")

