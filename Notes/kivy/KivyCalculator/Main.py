from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = (300, 400)

class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()

class CalculatorLayout(BoxLayout):
    # all functions go in here
    def calculate(self, equation):
        try:
            answer = eval(equation)
            self.display.text = str(answer)

        except:
            pass

    def clear(self):
        self.display.text = ""

if __name__ == "__main__":
    app = CalculatorApp()
    app.run()