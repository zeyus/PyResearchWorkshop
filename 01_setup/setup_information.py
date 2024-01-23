"""setup_information.py

This file will print out the following information:
    - Operating system
    - Python version
    - Python executable path
    - Conda environment path
    - PsychoPy version
"""

import logging
import sys
import platform
import os
import psychopy

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="\n%(message)s",
)
logger = logging.getLogger("Setup Information")

# Print out operating system
system = platform.system()
system_arch = platform.architecture()[0]
operating_system = platform.platform()
operating_system_version = platform.release()
logger.info(f"Operating system:\n\t{system} ({system_arch}): {operating_system} ({operating_system_version})")

# Print out Python version
python_version = sys.version
logger.info(f"Python version:\n\t{python_version}")

# Print out Python executable path
python_executable = sys.executable
logger.info(f"Python executable path:\n\t{python_executable}")

# Get conda environment from $CONDA_DEFAULT_ENV
conda_env = os.environ.get("CONDA_DEFAULT_ENV")
logging.info(f"Conda environment:\n\t{conda_env}")

# Print out PsychoPy version
psychopy_version = psychopy.__version__
logger.info(f"PsychoPy version:\n\t{psychopy_version}")

