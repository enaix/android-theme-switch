from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.bottomnavigation import MDBottomNavigation
from ui.mainlayout import MainLayout
from ui.homenav import HomeNav
from kivy.app import App


class MainWidget(MDBottomNavigation):
    def __init__(self, **kwargs):
        #super(ScreenManager, self).__init__(**kwargs)
        super().__init__()
        #self.homescreen = Screen(name='Home')
        db = App.get_running_app().db
        images1 = [db.load_theme(0, 0), db.load_theme(0, 1)]
        images2 = [db.load_theme(1, 0), db.load_theme(1, 1)]

        self.layout1 = MainLayout(theme="0", images=images1)
        self.layout2 = MainLayout(theme="1", images=images2)

        self.nav1 = HomeNav(name="Base theme", icon="numeric-1-box", theme="0")
        self.nav2 = HomeNav(name="Second theme", icon="numeric-2-box", theme="1")

        self.nav1.add_widget(self.layout1)
        self.nav2.add_widget(self.layout2)

        self.add_widget(self.nav1)
        self.add_widget(self.nav2)

