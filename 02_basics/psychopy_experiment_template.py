"""psychopy_experiment_template.py

This is a template that you can use to start your own experiments.
It contains some basic code that you will need for most experiments.
"""

# Import modules
import logging  # inbuilt python module for logging to the console
import os  # inbuilt python module for interacting with the operating system
import sys  # inbuilt python module for interacting with the interpreter (python itself)
import platform  # inbuilt python module for getting information about the operating system
from psychopy import visual, core, event, data, gui
import pandas as pd  # pandas is a module for working with data

# Set up logging, if you want to log to a file, you can
# add a filename to the basicConfig function
# e.g. logging.basicConfig(level=logging.INFO, format="\n%(message)s", filename="my_log_file.log")
logging.basicConfig(
    level=logging.INFO,
    format="\n%(message)s",
)
logger = logging.getLogger("Experiment")

# Print out operating system
system = platform.system()
system_arch = platform.architecture()[0]
operating_system = platform.platform()
operating_system_version = platform.release()
logger.info(f"Operating system:\n\t{system} ({system_arch}): {operating_system} ({operating_system_version})")

# Print out Python version
python_version = sys.version
logger.info(f"Python version:\n\t{python_version}")

