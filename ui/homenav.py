from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivy.clock import Clock
from kivy.app import App
from kivy.properties import StringProperty
from kivymd.toast import toast
from api.switch import set_wallpaper



class HomeNav(MDBottomNavigationItem):
    name = StringProperty()
    theme = StringProperty()
    icon = StringProperty()

    def __init__(self, **kwargs):
        super(MDBottomNavigationItem, self).__init__(**kwargs)
        self.debug_enabled = False
        Clock.schedule_once(self.set_debug_btn)

    def set_debug_btn(self, *args, **kwargs):
        self.ids.debug_btn.bind(on_press=self.switch_debug)

    def switch_debug(self, *args, **kwargs):
        app = App.get_running_app()
        self.color_children(app.main_wid.children, int(not self.debug_enabled))
        self.debug_enabled = not self.debug_enabled

    def set_theme(self):
        db = App.get_running_app().db
        db.load_file()
        home_path = db.load_theme(self.theme, 0)
        lock_path = db.load_theme(self.theme, 1)

        if home_path == "" and lock_path == "":
            toast("There is nothing to do")
            return

        set_wallpaper(home_path, lock_path)

    def color_children(self, elems, opacity):
        if len(elems) == 0:
            return
        for elem in elems:
                for c in elem.canvas.after.children:
                    if str(type(c)).find('Color') != -1:
                        color = list(c.rgba)
                        color[3] = opacity
                        c.rgba = tuple(color)
                self.color_children(elem.children, opacity)


