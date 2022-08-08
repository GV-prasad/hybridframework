import logging

class LogGen():
    @staticmethod
    def loggen():
        logging.basicConfig(filename="C://Users//Sharath Kumar//PycharmProjects//hybridframework//Logs//automation.log",
                            format="%(asctime)s: %(levelname)s: %(messages)s",
                            datefmt="%d/%m/%y  %I:%M:%S %p")
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
