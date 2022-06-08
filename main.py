from kivymd.app import MDApp
from ui.base import MainWidget
from api.storage import Storage
from kivy.lang import Builder
import os
import weakref

def load_kv_files():
    path = os.path.join(os.getcwd(), 'kv')
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    for f in files:
        if f.endswith('.kv'):
            Builder.load_file(os.path.join(path, f))

class MainApp(MDApp):
    def __init__(self):
        super().__init__()
        self.theme_cls.material_style = "M3"
        self.db = Storage()

        self.main_wid = MainWidget()
        #Builder.unload_file("kv/Debug.kv")

    def build(self):
        return self.main_wid


if __name__ == "__main__":
    load_kv_files()
    app = MainApp()
    app.run()

