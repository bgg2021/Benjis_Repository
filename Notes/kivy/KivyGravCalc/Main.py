# kivy Universal Gravity Calculator (30pts)

# When we learned about exceptions, I asked you to make a Universal Gravity calculator

# G is the universal gravity constant (6.674×10−11 N m^2 / kg^2)
# m1 is the mass of object 1 in kg
# m2 is the mass of object 2 in kg
# r is the distance between the two objects in meters (center to center distance)
# F is force in Newtons
# F = G * (m1 * m2) / r ** 2

# Make a universal gravity calculator app using kivy
# Your app will have the following:
# -a label widget that shows the title of your app (2pts) ##
# -a label widget and TextInput to input two masses and the radius (6pts) ##
# -textInput widgets should not accept non-numerical input. (2pts) ##
# -a calculate button to execute the gravity calculation (3pts) ##
# -answer label to show the calculation after you click on the button (3pts) ##
# -when calculate button pressed, the answer appears in the answer label (5pts)##
# -value errors, and divide by zero errors do not occur (4pts) ##
# -answer is formatted in scientific notation to two decimals (2pts)
# -layout is formatted in a meaningful way to make application user friendly and attractive (3pts)


#A few things I'd like to fix if I can
#1) Change the background colors in of the "Mass 1", "Mass 2," and "Radius"
# I never could quite figure out how to give those labels a color other than black
#2) Adjust the color scheme once I figure out how to do new background colors
#3) Find a way to round well without eliminating very small answers. Don't want too many decimal points, but I also
#don't want to make it such that e-10 numbers don't show. The "round" function does poorly in this regard, maybe
#normal formatting would work

# this is Main(3) btw

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = (800, 600)

class GravApp(App):
    def build(self):
        return GravLayout()

class GravLayout(BoxLayout):
    def gravcalc(self):
        g = 6.674e-11
        answer = 0
        try:
            answer = g * (float(self.mass1.text) * float(self.mass2.text)) / float(self.radius.text) ** 2
            new_answer = "{:.2e}".format(answer)
            self.output.text = str(new_answer)
        except:
            self.output.text = "Radius Cannot Be 0"

if __name__ == "__main__":
    app = GravApp()
    app.run()