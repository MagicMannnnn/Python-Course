import logging

logger = logging.getLogger('George')  # -> often used if there are multiple parts to one logging file, to log where it came from,
#for the shopping list could have separate loggers for adding an item, removing an item etc, alternative is to use separate files

logging.basicConfig(filename="e1.log", level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')

logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")