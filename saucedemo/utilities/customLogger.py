import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        runtime_path = os.getenv('RUNTIME_PATH', '<default_path>')
        logging.basicConfig(filename="runtime_path\\saucedemo_e-commerce\\saucedemo\\Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)



        return logger