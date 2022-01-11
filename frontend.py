from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar

from random import randint
from potionsDict import potions
 
class MyApp(MDApp):
    def build(self):
        screen = MDScreen()
        
        #UI Widgets go here

        title = MDLabel(
            text="Mystery Potion Finder", 
            pos_hint = {'center_x': 0.5, 'center_y': 0.5}
            )
        
        screen.add_widget(title)
        
        
        
        return screen
 
if __name__ == '__main__':
    MyApp().run()