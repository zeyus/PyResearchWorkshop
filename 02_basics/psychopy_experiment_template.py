"""psychopy_experiment_template.py

This is a template that you can use to start your own experiments.
It contains some basic code that you will need for most experiments.
"""

# Import modules
from psychopy import prefs
# set up some preferences so that the experiment looks nice on your screen
prefs.hardware["highDPI"] = True
prefs.hardware["audioLib"] = ["PTB", "sounddevice", "pyo", "pygame"] # Recommended
prefs.saveUserPrefs()

from psychopy import visual, core, event, data, gui, logging, clock, monitors  # psychopy modules for running an experiment


# Some general settings

class Settings:
    """A class to hold settings for the experiment"""
    # Set up some variables that we will use throughout the experiment
    # These are called "class variables" and are accessed using the class name
    EXPERIMENT_NAME = "psychopy_experiment_template"
    EXPERIMENT_VERSION = "0.1"
    # e.g. Settings.DATA_PATH
    DATA_PATH = "data"
    # Set up the window size
    WIN_SIZE = [1920, 1080]
    # Set up the window units
    WIN_UNITS = "pix"
    # Set up the window background color (r, g, b)
    WIN_COLOR = [0, 0, 0]
    # Set up the window monitor
    MONITOR = "default"
    # Monitor size in px
    MONITOR_SIZE = [1920, 1080]
    # Monitor width in cm
    MONITOR_WIDTH = 40
    # Monitor distance in cm
    MONITOR_DISTANCE = 60
    # Full screen or not
    WIN_FULL_SCREEN = False

    # Define trials, this can be as many as you want, and can
    # be used to define condition specific settings, such as
    # stimulus position, stimulus color, etc.
    # this could also be loaded from a CSV
    TRIALS = [
        {"condition": "congruent", "target": "<--", "correct_response": "z"},
        {"condition": "congruent", "target": "-->", "correct_response": "m"},
        {"condition": "incongruent", "target": "<-|", "correct_response": "m"},
        {"condition": "incongruent", "target": "|->", "correct_response": "z"},
    ]
    # Number of times to repeat each condition
    N_REPS = 4
    # Can be "random" or "sequential" or "fullRandom"
    # see https://psychopy.org/api/data.html#psychopy.data.TrialHandler
    ORDER_METHOD = "random"

    # list of keys to exit the experiment
    EXIT_KEY = "escape"

    # list of keys to continue the experiment
    CONTINUE_KEYS = ["space"]

class Experiment:
    run_log = None
    win = None
    mon = None
    participant = None
    experiment = None
    trials = None
    start_timestamp = None

def display_participant_dialogue() -> list:
    """Show participant information dialogue box"""
    participant = None
    # Only accept the ID if it is numeric
    while not isinstance(participant, list):
        #pylint: enable=unsubscriptable-object
        # Standard psychopy dialogue box
        dlg = gui.Dlg(title="Please enter participant information")
        dlg.addField(label='ID')
        # you could add additional fields here such as participant age
        # dlg.addField(label='Age', choices=[x for x in range(18, 70)])

        # Show dialogue box
        # if the user presses OK, participant will be a list with the first element being the ID
        # and the second element being the age (if you added that field), and so forth.
        participant = dlg.show()
        # Quit if cancel button on dialogue is pressed
        if participant is None or not dlg.OK:
            core.quit()
    return participant


# Set up the experiment window, monitor, and logging
def experiment_setup(exp=None):
    """Set up the experiment window, monitor, and logging"""

    if exp is None:
        exp = Experiment()
    elif not isinstance(exp, Experiment):
        raise TypeError("exp must be an Experiment object")
    exp.start_timestamp = clock.getAbsTime()
    # display participant dialogue
    participant = display_participant_dialogue()
    exp.participant = participant
    # exp.experiment = data.ExperimentHandler(
    #     name=Settings.EXPERIMENT_NAME,
    #     version=Settings.EXPERIMENT_VERSION,
    #     extraInfo={
    #         "participant": participant[0],
    #         # "age": participant[1],
    #     },
    #     savePickle=True,
    #     saveWideText=True,
    #     dataFileName=f"{Settings.DATA_PATH}/data_{exp.start_timestamp}",
    #     autoLog=True,
    # )


    # Set up the trials
    # see: https://psychopy.org/api/data.html#psychopy.data.TrialHandler
    exp.trials = data.TrialHandler(
        nReps=Settings.N_REPS,
        method=Settings.ORDER_METHOD,
        trialList=Settings.TRIALS,
        name="trials",
        extraInfo={
            "participant": exp.participant[0],
            # "age": participant[1],
        },
    )

    # exp.trials.setExp(exp.experiment)
    # Set up the monitor
    # see: https://psychopy.org/api/monitors.html
    mon = monitors.Monitor(
        name=Settings.MONITOR,
        width=Settings.MONITOR_WIDTH,
        distance=Settings.MONITOR_DISTANCE,
    )
    # set the monitor size in px
    mon.setSizePix(Settings.MONITOR_SIZE)
    mon.save()

    exp.mon = mon

    # Set up the experiment window
    # You can set the size of the window, whether it is full screen, etc.
    # see: https://psychopy.org/api/visual/window.html
    win = visual.Window(
        size=Settings.WIN_SIZE,
        units=Settings.WIN_UNITS,
        fullscr=Settings.WIN_FULL_SCREEN,
        color=Settings.WIN_COLOR,
        monitor=Settings.MONITOR,
        title=f"{Settings.EXPERIMENT_NAME} v{Settings.EXPERIMENT_VERSION}",
    )

    exp.win = win
    # Set up logging
    # see: https://psychopy.org/api/logging.html
    logging.console.setLevel(logging.INFO)
    # create a (non-experimental-data) log file
    run_log = logging.LogFile(f"{Settings.DATA_PATH}/run_{exp.start_timestamp}.log", level=logging.INFO, filemode="w")

    exp.run_log = run_log

    return exp



def wait_for_keys(keys=[]):
    """Wait for a key press to continue"""
    # Wait for one of the keys specified to be pressed
    key = event.waitKeys(keyList=keys + [Settings.EXIT_KEY])
    return key

def display_text_message(exp, text, wait=True):
    """Display a text message"""
    # Set up the text stimulus
    # see: https://psychopy.org/api/visual/textstim.html
    text_stim = visual.TextStim(
        win=exp.win,
        text=text,
        color="white",
        height=40,
        wrapWidth=1000,
    )
    # Draw the text stimulus to the window
    text_stim.draw()
    # Flip the window to make the stimulus visible
    exp.win.flip()
    # Wait for a key press to continue
    if wait:
        wait_for_keys(Settings.CONTINUE_KEYS)

# the following line ensures that the code will only run if this file is called directly
# meaning for example `python psychopy_experiment_template.py` in the terminal
def run_experiment():
    """Run the experiment"""

    # Set up the experiment
    exp = experiment_setup()

    # Display a message to the participant
    display_text_message(exp, "Welcome to the experiment!")
    
    visual_stim = visual.TextStim(
        win=exp.win,
        text="",
        color="white",
        height=40,
        wrapWidth=1000,
        name="blank",
    )
    trial_timer = core.Clock()
    # Loop through the trials
    for trial in exp.trials:
        trial_timer.reset()
        trial_done = False
        awaiting_response = False
        response = ''
        response_time = None
        correct = False
        while not trial_done:
            elapsed_time = trial_timer.getTime()
            # Display a fixation cross for the first 500 ms
            if elapsed_time < 0.5:
                if visual_stim.text != "+":
                    visual_stim.name = "fixation"
                    visual_stim.setText("+")
            # Display the target for 500 ms
            elif elapsed_time < 1:
                if visual_stim.text != trial["target"]:
                    visual_stim.name = "target"
                    visual_stim.setText(trial["target"])
                awaiting_response = True
                # in case a key was pressed before the target was shown
                event.clearEvents()
            # Display a blank screen for 1000 ms
            elif elapsed_time < 2:
                if visual_stim.text != "":
                    visual_stim.name = "blank"
                    visual_stim.setText("")
            else:
                event.clearEvents()
                trial_done = True
                awaiting_response = False
            # Draw the stimulus to the window
            visual_stim.draw()
            # Flip the window to make the stimulus visible
            exp.win.flip()
            # Check for a response
            if awaiting_response:
                keypress = event.getKeys(["z", "m"])
                if keypress:
                    # save the response and response time
                    response = keypress[0]
                    response_time = trial_timer.getTime()
                    # check if the response was correct
                    correct = response == trial["correct_response"]
                    trial_done = True
                    awaiting_response = False
        # save the trial data
        exp.trials.addData("response", response)
        exp.trials.addData("response_time", response_time)
        exp.trials.addData("correct", correct)

    # Save the data to a CSV file
    exp.trials.saveAsWideText(f"{Settings.DATA_PATH}/data_{exp.start_timestamp}.csv")
    
    # Display a message to the participant
    display_text_message(exp, "Thank you for participating!")
    # Close the experiment window
    exp.win.close()
    # Quit the experiment
    core.quit()


# the following line ensures that the code will only run if this file is called directly
if __name__ == "__main__":
    run_experiment()