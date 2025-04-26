"""Main module."""
from src.weather.exception import CustomException
from src.weather.logger import logging

if __name__ == "__main__":
    try:
        logging.info("Starting the main module.")
        # Your main code logic goes here
        logging.info("Main module executed successfully.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise CustomException(e, sys) from e