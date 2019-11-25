from tigr.config.templateConfig import ConfigType
import yaml


class YmlConfig(ConfigType):

    def read_file(self):
        with open(self.config_file, 'r') as stream:
            try:
                self.config = yaml.safe_load(stream)
                return self.config
            except yaml.YAMLError as e:
                print(e)
                return {}

    def parse_content(self):
        for section in self.config:
            for option in self.config[section]:
                self.arguments['--' + option] = self.config[section][option]
        return self.arguments
