from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
from kivymd.toast import toast
from plyer import filechooser
from kivy.app import App
from kivy.clock import Clock


class ImageCard(MDCard, RoundedRectangularElevationBehavior):
    text = StringProperty()
    image = StringProperty()
    theme = StringProperty()
    ptype = StringProperty() 

    def on_touch_down(self, touch):
        if not self.collide_point(touch.x, touch.y):
            return
        #toast(self.theme)
        try:
            paths = filechooser.open_file(on_selection=self.handle_click)
        except BaseException:
            toast("Cannot open Downloads folder, please navigate to it from the filesystem root")

    def handle_click(self, paths):
        if paths is None:
            return
        if len(paths) == 0 or str(paths[0]) == "[]":
            toast("Could not fetch filepicker app or the file is not an image. Please check app permissions")
        else:
            self.image_path = str(paths[0])
            Clock.schedule_once(self.save_path)

    def save_path(self, *args, **kwargs):
        self.image = self.image_path

        db = App.get_running_app().db
        db.save_theme(self.theme, self.ptype, self.image)
        db.save_file()


