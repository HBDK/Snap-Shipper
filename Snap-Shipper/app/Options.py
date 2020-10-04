from json import load as loadJson
from os.path import isfile
import logging

class OptionsBuilder:
    def __init__(self):
        _options = {}
        optionsFile = '/data/options.json'
        backupOptionsFile = 'local.json'

        if not isfile(optionsFile):
            logging.warning("Couldn't find the options file: {} Trying backupOptions".format(optionsFile))
            optionsFile = backupOptionsFile
            if not isfile(optionsFile):
                logging.error("Couldn't find the options file: {}".format(optionsFile))
                exit()

        with open(optionsFile) as json_file:
            _options.update(loadJson(json_file))

        self.Options = Options(_options)

class Options:
    def __init__(self, settings):
        self.DryRun = settings.get("DryRun", False)
        self.Folder = settings.get("Folder", "/backup")
        self.Sinks = settings.get("Sinks", [])