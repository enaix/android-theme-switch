#from kivymd.uix.widget import MDWidget
from kivy.storage.jsonstore import JsonStore
from kivy.logger import Logger
from kivy.utils import platform
import os
import json


class Storage:
    def __init__(self, abspath):
        if platform == "android":
            from android.storage import app_storage_path
            abspath = os.path.join(app_storage_path(), "app")
        
        db_path = os.path.join(abspath, 'db')
        if not os.path.exists(db_path):
            os.mkdir(db_path)
        
        self.settings_file = os.path.join(db_path, 'theme.json')
        self.data = None
        #self.store = JsonStore(os.path.join(db_path, 'theme.json'))
        Logger.info("Directory path: " + self.settings_file)
        #self.store = JsonStore(os.path.join(os.path.abspath(__file__), 'theme.json'))

    def save_theme(self, theme_id, ptype, path):
        if self.data is None:
            self.load_file()
        
        self.data[str(theme_id) + "_" + str(ptype)] = path

    def save_file(self):
        if self.data is None:
            Logger.info("No data to write...")
            return
        
        Logger.info("Writing file: " + str(self.data))
        with open(self.settings_file, 'w') as f:
            json.dump(self.data, f)

    def load_file(self):
        if not os.path.exists(self.settings_file):
            self.data = {}
            return

        with open(self.settings_file, 'r') as f:
            self.data = json.load(f)
        
        if self.data is None:
            self.data = {}

    def load_theme(self, theme_id, ptype):
        if self.data is None:
            self.load_file()

        key = str(theme_id) + "_" + str(ptype)
        path = self.data.get(key, None)
        if path is not None:
            if os.path.exists(path):
                return path
            return ""
        return ""
