import logging
import os
import sys


def InitLogger():
# Set up the logger
    logger = logging.getLogger(os.path.basename(sys.argv[0])) # use program name as logger name
    logger.setLevel(logging.DEBUG)

    # Create a console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)

    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(filename)s - %(levelname)s - %(message)s')

    # Add the formatter to the handler and the handler to the logger
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger
