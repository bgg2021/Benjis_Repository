from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.animation import Animation

class AnimationApp(App):
    def build(self):
        return(AniLayout())

class AniLayout(Widget):
    def on_touch_down(self, touch):
        self.ani.move_ani(touch.x, touch.y)

class ClockRect(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update, 1/60)
        self.speedx = 3
        self.speedy = 5
        self.pos = 100, 100

    def update(self, *args):
        self.x += self.speedx
        if self.right > Window.width or self.x < 0:
            self.speedx *= -1
        self.y += self.speedy
        if self.top > Window.height or self.y < 0:
            self.speedy *= -1

class AniRect(Widget):
    def move_ani(self, x, y):
        #self.center_x = x
        #self.center_y = y
        if self.width < 300:
            new_width = self.width * 2
        else:
            new_width = 70
        anim1 = Animation(center_x=x,
                          center_y=y,
                          width=new_width,
                          duration=1,
                          transition="out_elastic")
        anim1.start(self)

if __name__ == "__main__":
    app = AnimationApp()
    app.run()