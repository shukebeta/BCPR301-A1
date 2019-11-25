from tigr.config.templateConfig import ConfigType



class IniConfig(ConfigType):

    def read_file(self):
        self.config.read(self.config_file)
        return self.config.sections()


