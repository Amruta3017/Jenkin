import logging
from Mynextfilm.Utilities.commonMethods import get_path


class LogGen:
    @staticmethod
    def configure_logger():
        log_filename = get_path("Logs", "automation.log")  # Set the log filename here
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', '%d/%m/%Y %I:%M:%S %p')

        # Create a file handler to save logs to the predefined log filename
        file_handler = logging.FileHandler(log_filename)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Create a console handler to display logs in the terminal
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        return logger
