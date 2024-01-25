"""playground.py

This file is for testing and playing around with the code. It has examples of
different psychopy stimuli and responses, but does not create an experiment.

Rather, you can take and adapt parts of this code to create your own experiment
or to try out different interactions with psychopy.
"""

# Import modules
from pathlib import Path
from psychopy import prefs
# set up some preferences so that the experiment looks nice on your screen
prefs.hardware["highDPI"] = True
prefs.hardware["audioLib"] = ["PTB", "sounddevice", "pyo", "pygame"] # Recommended
prefs.saveUserPrefs()

from psychopy import visual, core, event, monitors, sound, constants  # psychopy modules for running an experiment

# Basic monitor and window setup is still required
mon = monitors.Monitor(
        name='default',
        width=40,
        distance=60,
    )
# set the monitor size in px
mon.setSizePix([1920, 1080])
mon.save()

# Set up the experiment window
# You can set the size of the window, whether it is full screen, etc.
# see: https://psychopy.org/api/visual/window.html
win = visual.Window(
    size=[1920, 1080],
    units="pix",
    fullscr=False,
    color="black",
    monitor=mon,
    title=f"PsychoPy Playground",
)

# Let's define a simple "wait for space bar" function that we can
# reuse between different examples
def wait_for_spacebar(win):
    """Wait for spacebar to be pressed"""
    # Create a text stimulus
    text = visual.TextStim(
        win=win,
        text="Press spacebar to continue",
        color="white",
        pos=(0, 0),
        height=40,
        name="WaitText"
    )
    # Draw the text to the window
    text.draw()
    # Flip the window to show the stimulus
    win.flip()
    # Wait for a spacebar press
    event.waitKeys(keyList=["space"])

# Alright, let's get started with some examples!
    
# Example 1: Display a text stimulus
# see: https://psychopy.org/api/visual/textstim.html
# and: https://psychopy.org/api/visual/textbox2.html#psychopy.visual.TextBox2

# Set up the text stimulus
text = visual.TextStim(
    win=win,
    text="Hello world!",
    color="white",
    pos=(0, 0),
    height=40,
    name="HelloWorld"
)
# Draw the text to the window
text.draw()
# Flip the window to show the stimulus
win.flip()
# wait for 2 seconds
core.wait(2)
# Wait for a spacebar press
wait_for_spacebar(win)

# Using TextBox2
# Set up the text stimulus
text = visual.TextBox2(
    win=win,
    text="Hello TextBox!",
    color="white",
    pos=(0, 0),
    size=(1000, 100),
    units="pix",
    name="HelloWorld"
)

# Draw the text to the window
text.draw()
# Flip the window to show the stimulus
win.flip()
# wait for 2 seconds
core.wait(2)
# Wait for a spacebar press
wait_for_spacebar(win)

# Example 2: Display an image stimulus
# see: https://psychopy.org/api/visual/imagestim.html

# Display all the .svg files in the './res/stimuli' folder
# Get the path to the folder
image_folder = "./03_stimuli/res/stimuli"
# Get the files in the folder
image_files = Path(image_folder).glob("*.png")
# Filter out all non .svg files
# These filenames could also be in a dictionary, list, or from a CSV file
# we just want the filename and extension
image_files = [file.name for file in image_files]
# Loop through the files, there are 60 images, so let's do 10 at a time
# note, the images are cropped in the original picture (mybad sorry)
# in a 5 x 2 grid
for i in range(0, 60, 10):
    # Create a list of 10 images
    image_list = image_files[i:i+10]
    # create the 5 x 2 grid
    for row in range(2):
        for col in range(5):
            # Create an image stimulus
            image = visual.ImageStim(
                win=win,
                image=f"{image_folder}/{image_list[row * 5 + col]}",
                pos=(-500 + col * 250, 250 - row * 250),
                size=(200, 200),
                name=f"Image_{row * 5 + col}",
            )
            # Draw the image to the window
            image.draw()
    # Flip the window to show the stimulus
    win.flip()
    # Wait for 2 seconds or spacebar
    event.waitKeys(keyList=["space"], maxWait=2)

# Wait for a spacebar press
wait_for_spacebar(win)

# Example 3: Display a movie stimulus
# see: https://psychopy.org/api/visual/moviestim.html

# Create a movie stimulus
movie = visual.MovieStim(
    win=win,
    filename="./03_stimuli/res/video/SteamboatWillie.mp4",
    pos=(0, 0),
    size=(1920, 1080),
    name="SteamboatWillie",
)

# Play the movie
movie.play()
# Wait for the movie to finish, or wait for spacebar to be pressed
while movie.status != visual.FINISHED:
    movie.draw()
    win.flip()
    # Check for a spacebar press
    if event.getKeys(keyList=["space"]):
        # Stop the movie
        movie.stop()
        # exit the loop
        break

# Wait for a spacebar press
wait_for_spacebar(win)

# Example 4: Display a sound stimulus
# we will just generate some tones
# see: https://psychopy.org/api/sound/playback.html

# Create a sound stimulus
sound_stim = sound.Sound(
    value="A",
    secs=0.5,
    volume=0.5,
    name="A440",
)

# Play the sound
sound_stim.play()
# Wait for the sound to finish, or wait for spacebar to be pressed
while not sound_stim.isFinished:  # might be a bug, the status doesn't change on windows
    win.flip()
    # Check for a spacebar press
    if event.getKeys(keyList=["space"]):
        # Stop the sound
        sound_stim.stop()
        # exit the loop
        break

# Wait for a spacebar press
wait_for_spacebar(win)

# Example 5: Display the pressed keys
# see: https://psychopy.org/api/event.html

# Create a text stimulus to show the pressed key
text = visual.TextStim(
    win=win,
    text="",
    color="white",
    pos=(0, 0),
    height=40,
    name="PressedKey"
)

# create a text stimulus to show a message at the top of the screen
message = visual.TextStim(
    win=win,
    text="Press a key to see it displayed, or press spacebar to continue",
    color="white",
    pos=(0, 400),
    height=40,
    name="Message"
)

# Loop until the escape key is pressed
while True:
    # Draw the message to the window
    message.draw()
    # Draw the text to the window
    text.draw()
    # Flip the window to show the stimulus
    win.flip()
    # Check for a spacebar press
    keys = event.getKeys()
    if keys and keys[0] != text.text:
        # Set the text to the pressed key
        text.text = keys[0]
        # Check if the escape key was pressed
        if keys[0] == "space":
            # exit the loop
            break

# Wait for a spacebar press
wait_for_spacebar(win)

# Example 6: Display mouse coordinates, and pressed mouse buttons
# see: https://psychopy.org/api/event.html

# Create a text stimulus to show the mouse coordinates
text = visual.TextStim(
    win=win,
    text="",
    color="white",
    pos=(0, 0),
    height=40,
    name="MouseCoordinates"
)

# create a text stimulus to show the currently pressed buttons
buttons = visual.TextStim(
    win=win,
    text="",
    color="white",
    pos=(0, 200),
    height=40,
    name="ButtonsPressed"
)


# create a text stimulus to show a message at the top of the screen
message = visual.TextStim(
    win=win,
    text="Move the mouse around, and press the mouse buttons",
    color="white",
    pos=(0, 400),
    height=40,
    name="Message"
)

mouse = event.Mouse()
# Loop until the space key is pressed
while True:
    # Draw the message to the window
    message.draw()
    # Draw the text to the window
    text.draw()
    # Draw the buttons to the window
    buttons.draw()
    # Get the mouse coordinates
    mpos = mouse.getPos()
    x, y = mpos
    # Set the text to the mouse coordinates
    text.text = f"Mouse coordinates: {x:.2f}, {y:.2f}"
    # Get the pressed mouse buttons
    pressed_buttons = mouse.getPressed()
    # Set the text to the pressed buttons
    buttons.text = f"Pressed buttons: {pressed_buttons}"
    # Flip the window to show the stimulus
    win.flip()
    # Check if the escape key was pressed
    if event.getKeys(keyList=["space"]):
        # exit the loop
        break




win.close()
core.quit()