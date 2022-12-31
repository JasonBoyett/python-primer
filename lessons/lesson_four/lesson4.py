from kivy.app import App
from kivy.uix.label import Label
# imports tend to follow this pattern
# from package.file import class (optional) as new_name


class MyApp(App):
    def build(self):
        return Label(text="python primer")


if __name__ == "__main__":
    MyApp().run()
