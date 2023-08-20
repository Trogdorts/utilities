import os
import sys

# Add the path to the utilities package to the system path
sys.path.append(r'C:\git\utilities')

# Import the custom_logger function and the logging module
from logging_utils import custom_logger
import logging

# Define a main function to demonstrate the usage of the custom logger
def main():
    # Get the directory of the current script
    main_dir = os.path.dirname(__file__)

    # Create a logger using the custom_logger function
    # Set the logger name to 'my_logger'
    # Specify the main directory for log files
    # Set the log level to DEBUG, meaning both INFO and DEBUG messages will be logged
    logger = custom_logger(name='my_logger', main_dir=main_dir, log_level=logging.DEBUG)

    # Log an info message
    logger.info("This is an info message")

    # Log a debug message
    logger.debug("This is a debug message")

# Check if the script is being run as the main module
if __name__ == "__main__":
    # Call the main function to demonstrate the logger usage
    main()
