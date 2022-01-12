from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

screen_helper = """
ScreenManager:
    HomeScreen:
    PotionScreen:
<HomeScreen>:
    name: 'home'
    
    MDTextField:
        id: rollInput
        hint_text: "Enter Roll"
        helper_text: "Enter the d100 roll of your player"
        helper_text_mode:"on_focus"
        required: True
        max_text_length: 3
        icon_right: "dice-d20"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x':0.5, 'center_y':0.7}
        size_hint_x:None
        width:300
    
    MDLabel:
        text: "Mystery Potion Finder"
        halign: 'center'
        pos_hint: {'center_y':0.9}
        font_style: 'H1'
        theme_text_color: "Custom"
        text_color: 243, 160, 81, 1
    
    MDFillRoundFlatButton:
        text:'Search'
        pos_hint: {'center_x':0.5, 'center_y':0.6}
        on_press:
            root.addPotion()
            root.manager.transition.direction = 'left'
            root.manager.current = 'potion'
    
    MDFillRoundFlatButton:
        text: 'Roll'
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        on_press:
            root.manager.transition.direction = 'left'
            root.manager.current = 'potion'
    
    MDTextField:
        id: optionsInput
        hint_text: ""
        helper_text: "Enter the die roll of your player"
        helper_text_mode:"on_focus"
        required: True
        visible: True
        max_text_length: 2
        pos_hint:{'center_x':0.5, 'center_y':0.2}
        size_hint_x: None if self.visible else 0
        width:150
    
    MDIconButton:
        icon:'dice-d20'
        theme_icon_color: 'app.theme_cls.primary_color'
        pos_hint: {'center_x':0.5, 'center_y':0.1}
        on_press:
            potionNameOption()
            root.manager.transition.direction = 'left'
            root.manager.current = 'potion'
    
<PotionScreen>:
    name: 'potion'
    
    MDLabel:
        id: potionName
        text: "Potion"
        halign: 'center'
        pos_hint: {'center_y':0.9}
        font_style: 'H1'
        theme_text_color: "Custom"
        text_color: 243, 160, 81, 1
    
    MDFillRoundFlatButton:
        text: 'Show'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press:
            root.addPotions()

    MDFillRoundFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.transition.direction = 'right'
            root.manager.current = 'home'
"""


class HomeScreen(Screen):
    def addPotion(self):
        potionScreen = self.manager.get_screen('potion')
        potionScreen.ids.potionName.text = "YOUR POTION"
    
    def potionNameOption(self):
        pass



class PotionScreen(Screen):
        def addPotions(self):
            self.ids.potionName.text = "my potion"

        def testingPotions(self):
            mainMenu = self.manager.get_screen('home')
            dialog = MDDialog(
                text=mainMenu.ids.rollInput.text
            )
            dialog.open()

# Create the screen manager
sm = ScreenManager()
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(PotionScreen(name='potion'))

class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        self.theme_cls.theme_style = 'Dark'
        return screen


DemoApp().run()