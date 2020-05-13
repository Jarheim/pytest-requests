import os
import sys

from simple_settings import settings, LazySettings


class Configuration:
    default_config = "settings_sql.yaml"

    def __init__(self):
        s = self.init_settings()
        self.CONNECTION_STRING = s.CONNECTION_STRING
        self.SERVER = s.SERVER

    def init_settings(self):
        default_config = "settings_sql.yaml"

        while (not os.path.exists(default_config)):
            # In order to pickup files from root dir, if tests being triggered from within test directory
            os.chdir('..')

        cmd_contains_settings = any("--settings" in s for s in sys.argv)
        return settings if cmd_contains_settings else LazySettings(default_config)
