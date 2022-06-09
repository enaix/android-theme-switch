from kivymd.app import MDApp
from ui.base import MainWidget
from api.storage import Storage
from kivy.lang import Builder
from kivy.utils import platform
#from jnius import autoclass
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
        self.abspath = os.path.dirname(os.path.abspath(__file__))
        self.db = Storage(self.abspath)

        self.main_wid = MainWidget()
        #Builder.unload_file("kv/Debug.kv")

    def build(self):
        if platform == 'android':
            from android import AndroidService # it will crash on other platforms otherwise
            service = AndroidService('Main service', 'running')
            service.start('Main service started')
            self.service = service
            #service = autoclass('com.enaix.theme.ServiceMain')#AndroidService('my pong service', 'running')
            #mActivity = autoclass('com.kivy.android.PythonActivity').mActivity
            #service.start(mActivity, 'Launch')
            #self.service = service
        
        return self.main_wid


if __name__ == "__main__":
    load_kv_files()
    app = MainApp()
    app.run()

