"""Tigr.

Usage:
  tigr.py [FILES ...] [-c c.ini] [-e tkinter] [-s 5] [-p regex] [--pencolor black] [--pensize 1] [-i]

You can also run all the unittest by this command: python -m unittest discover tigr/test
You can also run all the doc-test by this command: python -m doctest -v tigr/drawer/tkinter_worker.py

Options:
  -h --help                  Show this screen.
  -c 1.ini --config 1.ini    Specify the ini config file name
  -e turtle --engine turtle  Specify the drawer engine, tkinter or turtle. [default: turtle]
  -s 5 --speed 5             Specify the drawer speed, 1 slowest, 9 fastest [default: 5]
  -p regex --parser regex    Specify the instruction parser [default: peg]
  --pencolor black           Specify pen color [default: black]
  --pensize 1                Specify pen size [default: 1]
  -i --interactive           Specify if enter interactive mode when the script files were executed done [default: 0]
  --version                  Show version

Attention:

If an option is found in config file and command line arguments at the same time,
this program will use the value from the ini file.
"""
from docopt import docopt
import configparser as cp
from abc import ABC, abstractmethod
import os.path


# client
class Config:
    def __init__(self):
        self.arguments = docopt(__doc__, version='Tigr 1.0')
        self.config_file = self.arguments['--config']
        self.config_type = None
        self.config_exist = 0
        self.os_path_exists = 0
        self.config_type_exists = 0

    def check_config_exists(self):
        if self.arguments['--config'] is not None:
            self.config_exist = 1

    def check_os_path_exists(self):
        if os.path.exists(self.config_file):
            self.os_path_exists = 1
        else:
            print(f'config file does not exist: {self.config_file}')

    def identify_config(self):
        name, ext = os.path.splitext(self.config_file)
        if ext.lower() == '.ini':
            self.config_type_exists = 1
            self.config_type = InitConfig()
        elif ext.lower() in ['.yml', '.yaml']:
            self.config_type_exists = 1
            self.config_type = YmlConfig()
        else:
            print(f'invalid config file: {self.config_file}', 'unrecognized ext name')

    def do_config(self):
        self.check_config_exists()
        # print(self.config_exist)
        if self.config_exist:
            self.check_os_path_exists()
            if self.os_path_exists:
                self.identify_config()
                if self.config_type_exists:
                    self.config_type.do_config(self.config_file, self.arguments)
        return self.arguments


# Abstract Strategy
class ConfigType(ABC):
    @abstractmethod
    def do_config(self, config_file, new_arguments):
        pass


# Concrete Strategy A
class InitConfig(ConfigType):
    def do_config(self, config_file, new_arguments):
        config1 = cp.ConfigParser()
        config1.read(config_file)
        for section in config1.sections():
            for option in config1.options(section):
                new_arguments['--' + option] = config1.get(section, option)
                return new_arguments


# Concrete Strategy B
class YmlConfig(ConfigType):
    def do_config(self, config_file, new_arguments):
        import yaml
        with open(config_file, 'r') as stream:
            try:
                config2 = yaml.safe_load(stream)
                for section in config2:
                    for option in config2[section]:
                        new_arguments['--' + option] = config2[section][option]
                        return new_arguments
            except yaml.YAMLError as e:
                print(e)


if __name__ == '__main__':
    import tigr
    config = Config()
    tigr.main(config.do_config())
