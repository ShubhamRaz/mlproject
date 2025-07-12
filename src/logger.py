import logging
import os
from datetime import datetime

# Create log file name based on current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create directory path: current_directory/logs/timestamp.log
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Full log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Set up logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s',
    level=logging.INFO,
)
