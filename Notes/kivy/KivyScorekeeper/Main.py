from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = (400, 600)

class ScoreApp(App):
    def build(self):
        return ScoreLayout()


class ScoreLayout(BoxLayout):
    # root widget which will contain all functions
    def change_score(self, label, value):
        new_score = int(label.text) + value
        label.text = str(new_score)

if __name__ == "__main__":
    app = ScoreApp()
    app.run()