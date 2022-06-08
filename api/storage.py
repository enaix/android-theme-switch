#from kivymd.uix.widget import MDWidget
from kivy.storage.jsonstore import JsonStore
import os


class Storage:
    def __init__(self):
        super().__init__()

        #self.store = JsonStore(os.path.join(os.path.dirname(os.path.abspath(__file__)),'theme.json'))
        self.store = JsonStore('theme.json')

    def save_theme(self, theme_id, ptype, path):
        self.store.put(str(theme_id) + "_" + str(ptype), path=path)

    def load_theme(self, theme_id, ptype):
        key = str(theme_id) + "_" + str(ptype)
        if self.store.exists(key):
            return self.store.get(key).get("path", "")
        else:
            return ""
