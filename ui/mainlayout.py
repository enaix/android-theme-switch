from kivymd.uix.boxlayout import BoxLayout
from ui.imagecard import ImageCard


class MainLayout(BoxLayout):
    def __init__(self, theme, images):
        super().__init__()
        self.theme = theme
        

        card1 = ImageCard(text="Home screen", image=images[0], theme=self.theme, ptype="0")
        self.add_widget(card1)
        card2 = ImageCard(text="Lock screen", image=images[1], theme=self.theme, ptype="1")
        self.add_widget(card2)

