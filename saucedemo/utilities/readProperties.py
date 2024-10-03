import configparser

config = configparser.RawConfigParser()
config.read("C:\\Automation\\saucedemo_e-commerce\\saucedemo\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getLocked_Username():
        lockedout_username = config.get('common info', 'locked_username')
        return lockedout_username

    @staticmethod
    def getProblem_Username():
        problem_username = config.get('common info', 'problem_username')
        return problem_username

    @staticmethod
    def getPerforamce_Username():
        performance_username = config.get('common info', 'performance_username')
        return performance_username

    @staticmethod
    def getInvalid_Username():
        invalid_username = config.get('common info', 'error_username')
        return invalid_username
