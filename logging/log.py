import sys
import logging

logger = logging.getLogger('Reganto' + __name__)


# Define handlers for specific outputs
file_handler = logging.FileHandler(filename='/tmp/file.log', mode='a')
stream_handler = logging.StreamHandler(sys.stdout)

# Define formatters for format LogRecords
file_formatter = logging.Formatter('%(process)d - %(levelname)s - %(name)s - %(asctime)s - %(message)s')
stream_formatter = logging.Formatter('%(process)d - %(levelname)s - %(name)s - %(asctime)s - %(message)s')

# Add formatters to handlers
file_handler.setFormatter(file_formatter)
stream_handler.setFormatter(stream_formatter)


# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

