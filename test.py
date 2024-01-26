from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
class MyApp(App):
    def build(self):
       
        gridLayout = GridLayout(cols=7)
       
        gridLayout.add_widget( Widget())
        gridLayout.add_widget( Widget())
        gridLayout.add_widget( Widget())
        gridLayout.add_widget( Button())
        gridLayout.add_widget( Widget())
        gridLayout.add_widget( Widget())
        gridLayout.add_widget( Widget())
        gridLayout.add_widget( Widget())
        
        return gridLayout
    def btn_press(self,instance):
            self.text = "ghfnn"
if __name__ == "__main__":
    MyApp().run()