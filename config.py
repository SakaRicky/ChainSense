import os
from dotenv import load_dotenv
import logging
import colorlog

load_dotenv()

# Set up colorized logging
logger = logging.getLogger()
logHandler = colorlog.StreamHandler()

formatter = colorlog.ColoredFormatter(
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    }
)
logHandler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
