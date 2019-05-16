'''
Formatter (26pts)

Create a kivy app with the following rough layout

############
#  LABEL   #
#  SPINNER #
#  RADIOS  #
#  SLIDERS #
#  SWITCH  #
############

The label will be the formatting target for this application

- The spinner will change the font of the label (minimum 2 fonts) (6pts) ###
- The radios will be used to select the text for the label (3pts) ###
- Three sliders will be used to adjust the rgba values of the label background canvas color. (6pts) ###
- A switch will be used to change the font color from black to white. (3pts) ###

Each control will have an associated label. (8pts) ###

'''

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = (500, 700)
Window.clearcolor = [0, 0.5, 1, 1]

class FormApp(App):
    def build(self):
        return FormLayout()

class FormLayout(BoxLayout):
    def color_switch(self, value):
        if value:
            self.format.color = (0, 0, 0, 1)
        else:
            self.format.color = (1, 1, 1, 1)

    def color_slide(self, r, g, b):
        #value1 = self.slider1.value
        #value2 = self.slider2.value
        #value3 = self.slider3.value
        #color_code = [value1, value2, value3, 1]
        #print(color_code)
        Window.clearcolor = [r, g, b,1]

if __name__ == "__main__":
    app = FormApp()
    app.run()