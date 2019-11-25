from abc import ABC, abstractmethod
import configparser as cp


# Template
class ConfigType(ABC):

    def __init__(self, new_config_file, new_arguments):
        self.config_file = new_config_file
        self.arguments = new_arguments
        self.config = cp.ConfigParser()

    '''Template Operation'''
    def parse(self):
        self.read_file()
        return self.parse_content()

    '''Primitive Operation'''
    @abstractmethod
    def read_file(self):
        pass

    '''Hook Method'''
    def parse_content(self):
        for section in self.config.sections():
            for option in self.config.options(section):
                self.arguments['--' + option] = self.config.get(section, option)
        return self.arguments
