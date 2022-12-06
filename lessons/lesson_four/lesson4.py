from kivy.app import App
from kivy.uix.label import Label
#from package.file import class (optional) as new name


class MyApp(App):
    def build(self):
        return Label(text="python primer")


if __name__ == "__main__":
    MyApp().run() 
